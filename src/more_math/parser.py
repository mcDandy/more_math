class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  # List of (type, value) tuples
        self.pos = 0

    def peek(self):
        # Přeskoč NEWLINE/INDENT/DEDENT
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in {"INDENT", "DEDENT", "NEWLINE"}:
            self.pos += 1
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('ENDMARKER', '')

    def consume(self):
        token = self.peek()
        self.pos += 1
        return token

    def parse_expression(self):
        # Logický OR
        left = self.parse_xor()
        while True:
            tok_type, value = self.peek()
            if value == '|':
                self.consume()
                right = self.parse_xor()
                left = ('BINOP', ('|', left, right))
            else:
                break
        return left

    def parse_xor(self):
        # XOR
        left = self.parse_and()
        while True:
            tok_type, value = self.peek()
            if value == '^':
                self.consume()
                right = self.parse_and()
                left = ('BINOP', ('^', left, right))
            else:
                break
        return left

    def parse_and(self):
        # Logický AND
        left = self.parse_add_sub()
        while True:
            tok_type, value = self.peek()
            if value == '&':
                self.consume()
                right = self.parse_add_sub()
                left = ('BINOP', ('&', left, right))
            else:
                break
        return left

    def parse_add_sub(self):
        # Sčítání, odčítání
        left = self.parse_mul_div_mod()
        while True:
            tok_type, value = self.peek()
            if value in ['+', '-']:
                op = value
                self.consume()
                right = self.parse_mul_div_mod()
                left = ('BINOP', (op, left, right))
            else:
                break
        return left

    def parse_mul_div_mod(self):
        # Násobení, dělení, modulo
        left = self.parse_unary()
        while True:
            tok_type, value = self.peek()
            if value in ['*', '/', '%']:
                op = value
                self.consume()
                right = self.parse_unary()
                left = ('BINOP', (op, left, right))
            else:
                break
        return left

    def parse_unary(self):
        # Unární operátory: !, +, -
        tok_type, value = self.peek()
        if tok_type == 'OP' and value in ('+', '-', '!'):
            op = value
            self.consume()
            operand = self.parse_unary()
            return ('UNARYOP', (op, operand))
        return self.parse_factor()

    def parse_arguments(self):
        args = []
        if self.peek()[0] == 'OP' and self.peek()[1] == ')':
            return args  # žádné argumenty
        while True:
            arg = self.parse_expression()
            args.append(arg)
            tok_type, value = self.peek()
            if tok_type == 'OP' and value == ',':
                self.consume()
            else:
                break
        return args

    def parse_factor(self):
        tok_type, value = self.peek()

        if tok_type == 'OP' and value == '(':
            self.consume()  # Skip '('
            expr = self.parse_expression()
            if self.peek()[0] != 'OP' or self.peek()[1] != ')':
                raise SyntaxError(
                    f"Missing closing parenthesis at position {self.pos}."
                )
            self.consume()  # Skip ')'
            return ('PARENTHESIS', expr)

        elif tok_type == 'NAME':
            name = value
            self.consume()
            # Podpora matematických konstant
            if name.lower() == 'pi':
                return ('LITERAL', 3.141592653589793)
            if name.lower() == 'e':
                return ('LITERAL', 2.718281828459045)
            if self.peek()[0] == 'OP' and self.peek()[1] == '(':
                self.consume()  # Skip '('
                args = self.parse_arguments()
                if self.peek()[0] != 'OP' or self.peek()[1] != ')':
                    raise SyntaxError(
                        f"Missing closing parenthesis for function '{name}' at position {self.pos}."
                    )
                self.consume()
                return ('FUNCTION', (name.upper(), args))
            else:
                return ('VARIABLE', name)

        elif tok_type == 'NUMBER':
            try:
                num = float(value)
            except Exception:
                raise SyntaxError(
                    f"Invalid number '{value}' at position {self.pos}."
                )
            self.consume()
            return ('LITERAL', num)

        elif tok_type == 'OP' and value == ')':
            raise SyntaxError(
                f"Unexpected right parenthesis ')' at position {self.pos}."
            )

        elif tok_type == 'ENDMARKER':
            raise SyntaxError(
                "Unexpected end of input. Check for missing arguments or closing parentheses."
            )

        else:
            raise SyntaxError(
                f"Unexpected token '{value}' of type {tok_type} at position {self.pos}."
            )
