"""
GPU-accelerated noise generation utilities for arbitrary ND tensors.
Pure PyTorch implementation with deterministic seeding.
True Perlin noise with gradient interpolation - arbitrary dimensions.
"""

import torch


class NoiseUtils:
    """GPU-accelerated Perlin noise generation with support for arbitrary dimensions."""

    @staticmethod
    def _hash_nd(coords, seed=0):
        """
        Hash function for N-dimensional coordinates.
        coords: tuple or list of coordinate tensors
        Returns: hash value in [0, 1)
        """
        h = seed
        # Combine all coordinates into hash
        for i, coord in enumerate(coords):
            prime = [73856093, 19349663, 83492791, 39916801, 56962349, 76978801][i % 6]
            h ^= (torch.floor(coord).long() * prime)

        h = h ^ (h >> 13)
        h = (h * 377119761) & 0x7fffffff
        return (h.float() / 0x7fffffff).clamp(0, 0.9999)

    @staticmethod
    def _fade(t):
        """Perlin fade curve: 6t^5 - 15t^4 + 10t^3"""
        return t**3 * (t * (t * 6 - 15) + 10)

    @staticmethod
    def _build_grid_samples(coords_frac, coords_floor):
        """
        Build all 2^n corner samples for n-dimensional Perlin noise.
        coords_frac: tuple of fractional parts (for fading)
        coords_floor: tuple of integer parts (for grid corners)
        Returns: list of (corner_coords, fade_values) tuples
        """
        ndim = len(coords_floor)
        samples = []

        # Generate all 2^ndim corners
        for i in range(1 << ndim):
            corner_coords = []
            for d in range(ndim):
                # Extract bit d from i to determine if we add 1 to this dimension
                if (i >> d) & 1:
                    corner_coords.append(coords_floor[d] + 1)
                else:
                    corner_coords.append(coords_floor[d])
            samples.append(tuple(corner_coords))

        return samples

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
        coords_floor = tuple(torch.floor(c).long() for c in coords)
        coords_frac = tuple(c - torch.floor(c) for c in coords)

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
            grad = torch.stack(grad_components, dim=0)
            grad_norm = torch.linalg.norm(grad, dim=0, keepdim=True)
            grad = grad / torch.where(grad_norm == 0, torch.ones_like(grad_norm), grad_norm)

            dist_components = [coords_frac[d] - corner_offsets[d] for d in range(ndim)]
            dist = torch.stack(dist_components, dim=0)
            dot = torch.sum(grad * dist, dim=0)

            weight = 1.0
            for d in range(ndim):
                if corner_offsets[d]:
                    weight = weight * fades[d]
                else:
                    weight = weight * (1 - fades[d])

            result = result + dot * weight

        return torch.clamp(result, -1, 1)

    @staticmethod
    def cellular_noise_nd(coords_input, scale=1.0, jitter=0.5, seed=0, device=None):
        """
        N-dimensional Cellular (Voronoi) noise.
        coords_input: tuple of coordinate tensors
        Returns: distance to nearest feature point in [0, 1]
        """
        ndim = len(coords_input)

        # Scale coordinates
        coords = tuple(c / scale for c in coords_input)

        # Integer grid cell and position within cell
        coords_cell = tuple(torch.floor(c).long() for c in coords)
        coords_frac = tuple(c - torch.floor(c) for c in coords)

        # Search neighborhood (3^ndim cells)
        min_dist = torch.full_like(coords[0], float('inf'))

        def generate_offsets(d):
            """Generate all offsets for neighborhood search"""
            if d == 0:
                return [[]]
            return [[i] + offset for i in [-1, 0, 1] for offset in generate_offsets(d - 1)]

        offsets = generate_offsets(ndim)

        for offset in offsets:
            # Neighbor cell coordinates
            neighbor_coords = tuple(coords_cell[i] + offset[i] for i in range(ndim))

            # Hash-based feature point in neighbor cell
            hash_vals = []
            for seed_mult in range(ndim):
                h = NoiseUtils._hash_nd(neighbor_coords, seed * (seed_mult + 2))
                hash_vals.append(h * jitter)

            # Feature point position (cell + jitter)
            feature_pos = tuple(
                offset[i] + hash_vals[i]
                for i in range(ndim)
            )

            # Distance to feature point
            dist_sq = sum((coords_frac[i] - feature_pos[i])**2 for i in range(ndim))
            dist = torch.sqrt(dist_sq)

            min_dist = torch.minimum(min_dist, dist)

        return min_dist+0.5

    @staticmethod
    def plasma_noise_nd(coords_input, scale=1.0, seed=0, device=None):
        """
        N-dimensional Plasma/Turbulence noise - high-frequency chaotic patterns.
        Uses interpolated noise for smooth results.
        coords_input: tuple of coordinate tensors
        """
        ndim = len(coords_input)
        result = torch.zeros_like(coords_input[0])
        amplitude = 1.0
        frequency = 1.0
        max_amplitude = 0.0

        for octave in range(4):
            # Scale coordinates by frequency and base scale
            scaled_coords = tuple((c / scale) * frequency for c in coords_input)

            # Use Perlin-like interpolation for smooth plasma
            noise_octave = NoiseUtils.perlin_noise_nd(
                tuple((c / scale) * frequency for c in coords_input),
                1.0,  # scale already applied above
                seed + octave * 1000,
                device
            )

            # Add this octave
            result = result + noise_octave * amplitude
            max_amplitude += amplitude

            # Update for next octave
            amplitude *= 0.5
            frequency *= 2.0

        result = result / max_amplitude
        return (result*2)+0.5     
