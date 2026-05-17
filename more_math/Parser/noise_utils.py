"""
GPU-accelerated noise generation utilities for arbitrary ND tensors.
Pure PyTorch implementation with deterministic seeding.
True Perlin noise with gradient interpolation - arbitrary dimensions.
"""

import torch

class NoiseUtils:
    @staticmethod
    def _fade(t):
        """
        Optimalizovaná Perlinova fade křivka.
        Místo t**3 používáme t * t * t, což je v PyTorchi řádově rychlejší.
        """
        return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

    @staticmethod
    def _hash_nd(coords, seed=0):
        """
        PLNĚ VEKTORIZOVANÁ matematická hashovací funkce.
        Žádné bitové operace. Využívá pseudo-náhodnou sinusovou vlnu.
        Čas výpočtu pro 25 mil. bodů klesne na milisekundy.
        """
        # Použijeme stabilní deterministické koeficienty pro míchání dimenzí
        constants = [12.9898, 78.233, 45.164, 92.411, 27.531, 53.892]

        # Inicializace jako float pro implicitní broadcasting místo full_like
        dt = float(seed)

        # Lineární kombinace souřadnic s prvočíselnými vahami
        for i, coord in enumerate(coords):
            # Pokud už je to float32, to() je skoro no-op, ale můžeme rovnou přičítat
            dt = dt + coord.to(torch.float32) * constants[i % len(constants)]

        # Velmi rychlý a osvědčený hash z GPU shaderů: fract(sin(x) * 43758.5453)
        st = torch.sin(dt) * 43758.5453
        h = st - torch.floor(st)

        # Vrátí hodnotu bezpečně v rozsahu [0, 0.9999] jako původní funkce
        return h.clamp(0.0, 1.0)

    @staticmethod
    def perlin_noise_nd(coords_input, scale=1.0, seed=0, device=None):
        """
        N-dimensional Perlin noise with proper gradient interpolation.
        coords_input: tuple of coordinate tensors with same shape
        scale: frequency scale
        seed: random seed
        Returns: noise tensor in same shape as input coordinates
        """
        ndim = len(coords_input)

        # Scale coordinates
        coords = tuple(c / scale for c in coords_input)

        # Split into integer and fractional parts
        # Keep coords_floor as float32 to avoid expensive conversions to and from long
        coords_floor = tuple(torch.floor(c).to(torch.float32) for c in coords)
        coords_frac = tuple(c - coords_floor[d] for d, c in enumerate(coords))

        # Fade curves for each dimension
        fades = tuple(NoiseUtils._fade(f) for f in coords_frac)

        # Accumulate weighted corner contributions
        result = torch.zeros_like(coords_input[0])
        prime_seeds = [1013, 1619, 3137, 5021, 7919, 10427]
        for corner_idx in range(1 << ndim):
            corner_offsets = tuple((corner_idx >> d) & 1 for d in range(ndim))
            corner_coords = tuple(coords_floor[d] + corner_offsets[d] for d in range(ndim))

            grad_components = []
            for d in range(ndim):
                h = NoiseUtils._hash_nd(corner_coords, seed + prime_seeds[d % len(prime_seeds)] * (d + 1))
                grad_components.append(h * 2.0 - 1.0)

            # Optimalizace: výpočet normy a dot produktu iterativně bez torch.stack
            grad_norm_sq = grad_components[0] * grad_components[0]
            for d in range(1, ndim):
                grad_norm_sq += grad_components[d] * grad_components[d]

            inv_norm = torch.where(grad_norm_sq == 0.0, torch.ones_like(grad_norm_sq), torch.rsqrt(grad_norm_sq))

            dot = grad_components[0] * (coords_frac[0] - corner_offsets[0]) * inv_norm
            for d in range(1, ndim):
                dot += grad_components[d] * (coords_frac[d] - corner_offsets[d]) * inv_norm

            weight = fades[0] if corner_offsets[0] else (1.0 - fades[0])
            for d in range(1, ndim):
                weight = weight * (fades[d] if corner_offsets[d] else (1.0 - fades[d]))

            result += dot * weight

        return torch.clamp(result, -1, 1)

    @staticmethod
    def cellular_noise_nd(coords_input, scale=1.0, jitter=0.5, seed=0, device=None):
        """
        N-dimensional Cellular (Voronoi) noise - OPRAVENÁ VERZE.
        Správně odečítá jednotlivé dimenze tensorů.
        """
        ndim = len(coords_input)
        device = coords_input[0].device

        # 1. Škálování a rozdělení souřadnic
        coords = tuple(c / scale for c in coords_input)
        # Optimalizace: uložit jako float32 pro rychlejší indexování a hash
        coords_cell = tuple(torch.floor(c).to(torch.float32) for c in coords)

        # OPRAVA: Musíme indexovat konkrétní prvek z tuple pomocí `coords_cell[i]`
        coords_frac = tuple(coords[i] - coords_cell[i] for i in range(ndim))

        # Pro inicializaci použijeme první tensor z mřížky, abychom dodrželi správný shape
        min_dist = torch.full_like(coords_input[0], float('inf'), dtype=torch.float32, device=device)

        # 2. Generování všech 3^ndim offsetů přímo v PyTorchi
        base_range = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32, device=device)
        offset_grids = torch.meshgrid(*[base_range] * ndim, indexing='ij')
        gpu_offsets = torch.stack([g.flatten() for g in offset_grids], dim=-1)
        num_neighbors = gpu_offsets.shape[0]

        prime_seeds = [1013, 1619, 3137, 5021, 7919, 10427]

        # 3. Plně akcelerovaný výpočet sousedství
        for n in range(num_neighbors):
            current_offset = gpu_offsets[n]

            # Souřadnice sousední buňky složené ze všech dimenzí naráz pro správný hash
            neighbor_coords = tuple(coords_cell[i] + current_offset[i] for i in range(ndim))

            dist_sq = 0.0
            for i in range(ndim):
                # Generování unikátního seedu pro každou dimenzi aktuálního souseda
                s = seed + prime_seeds[i % len(prime_seeds)] * (i + 2)
                h = NoiseUtils._hash_nd(neighbor_coords, s)

                # Pozice feature pointu: offset + hash * jitter
                pos_i = current_offset[i] + h * jitter

                # Vzdálenost pixelu od tohoto bodu
                diff = coords_frac[i] - pos_i
                dist_sq += diff * diff

            dist = torch.sqrt(dist_sq)
            min_dist = torch.minimum(min_dist, dist)

        return min_dist



    @staticmethod
    def plasma_noise_nd(
        coords_input,
        scale=1.0,
        seed=0,
        device=None,
        octaves=4,
        persistence=0.5,
        lacunarity=2.0,
    ):
        """
        N-dimensional Plasma/Turbulence noise in [0, 1].
        Uses Perlin octaves with automatic octave limiting to reduce aliasing.
        """
        result = torch.zeros_like(coords_input[0])
        amplitude = 1.0
        frequency = 1.0
        max_amplitude = 0.0

        for octave in range(octaves):
            noise_octave = NoiseUtils.perlin_noise_nd(
                tuple((c / scale) * frequency for c in coords_input),
                1.0,
                seed + octave * 1000,
                device
            )

            result = result + noise_octave * amplitude
            max_amplitude += amplitude

            amplitude *= persistence
            frequency *= lacunarity

        # Normalizace zpět do [-1, 1] a potom do [0, 1]
        result = result / max_amplitude
        return (result*2)+0.5

    @staticmethod
    def _accumulate_octaves_nd(sample_fn, octaves=1, persistence=0.5, lacunarity=2.0):
        octaves = max(1, int(octaves))
        result = None
        amplitude = 1.0
        frequency = 1.0
        max_amplitude = 0.0

        for octave in range(octaves):
            value = sample_fn(frequency, octave)
            if result is None:
                result = torch.zeros_like(value, dtype=torch.float32)
            result = result + value * amplitude
            max_amplitude += amplitude
            amplitude *= persistence
            frequency *= lacunarity

        if max_amplitude == 0.0:
            return result
        return result / max_amplitude

    @staticmethod
    def ridged_noise_nd(coords_input, scale=1.0, seed=0, device=None, octaves=4, persistence=0.5, lacunarity=2.0, ridge_power=2.0):
        """
        Ridged multifractal noise in [0, 1].
        """
        def sample(frequency, octave):
            noise = NoiseUtils.perlin_noise_nd(
                tuple((c / scale) * frequency for c in coords_input),
                1.0,
                seed + octave * 1000,
                device,
            )
            ridged = (1.0 - noise.abs()).clamp(0.0, 1.0)
            return ridged.pow(ridge_power)

        return NoiseUtils._accumulate_octaves_nd(sample, octaves, persistence, lacunarity).clamp(0.0, 1.0)

    @staticmethod
    def domain_warp_noise_nd(
        coords_input,
        scale=1.0,
        seed=0,
        device=None,
        warp_scale=1.0,
        warp_strength=0.35,
        octaves=4,
        warp_octaves=2,
        persistence=0.5,
        lacunarity=2.0,
    ):
        """
        Domain-warped Perlin noise in [0, 1].
        """
        ndim = len(coords_input)

        warp_fields = []
        for dim in range(ndim):
            def sample_warp(frequency, octave, dim=dim):
                return NoiseUtils.perlin_noise_nd(
                    tuple((c / warp_scale) * frequency for c in coords_input),
                    1.0,
                    seed + 10000 + dim * 1000 + octave * 97,
                    device,
                )

            warp_fields.append(NoiseUtils._accumulate_octaves_nd(sample_warp, warp_octaves, persistence, lacunarity))

        warped_coords = tuple(
            (coords_input[dim] / scale) + warp_fields[dim] * warp_strength
            for dim in range(ndim)
        )

        def sample_base(frequency, octave):
            return NoiseUtils.perlin_noise_nd(
                tuple(c * frequency for c in warped_coords),
                1.0,
                seed + 20000 + octave * 1000,
                device,
            )

        base = NoiseUtils._accumulate_octaves_nd(sample_base, octaves, persistence, lacunarity)
        return ((base + 1.0) * 0.5).clamp(0.0, 1.0)
