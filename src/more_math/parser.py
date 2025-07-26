class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  # List of (type, value) tuples
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('ENDMARKER', '')

    def consume(self):
        token = self.peek()
        self.pos += 1
        return token

    def parse_expression(self):
        """Expression: term (PLUS|MINUS term)*"""
        left = self.parse_term()
        while True:
            tok_type, value = self.peek()
            if value in ['+', '-']:
                op = value
                self.consume()  # Consume '+' or '-'
                right = self.parse_term()
                left = ('BINOP', (op, left, right))
            else:
                break
        return left

    def parse_term(self):
        """Term: factor (MULT|DIVIDE factor)*"""
        left = self.parse_factor()
        while True:
            tok_type, value = self.peek()
            if value in ['*', '/']:
                op = value
                self.consume()  # Consume '*' or '/'
                right = self.parse_factor()
                left = ('BINOP', (op, left, right))
            else:
                break
        return left

    def parse_factor(self):
        """Factor: variable | function_call | number | parenthesis"""
        tok_type, value = self.peek()

        if tok_type == 'OP' and value == '(':
            self.consume()  # Skip '('
            expr = self.parse_expression()
            assert self.peek()[0] == 'OP' and self.peek()[1] == ')', "Missing closing parenthesis"
            self.consume()  # Skip ')'
            return ('PARENTHESIS', expr)

        elif tok_type == 'NAME':
            func_name = value
            self.consume()
            if self.peek()[0] == 'OP' and self.peek()[1] == '(':
                self.consume()  # Skip '('
                arg = self.parse_expression()
                assert self.peek()[0] == 'OP' and self.peek()[1] == ')', "Missing closing parenthesis"
                self.consume()
                return ('FUNCTION', (func_name.upper(), arg))
            else:
                return ('VARIABLE', func_name)

        elif tok_type == 'NUMBER':
            num = float(value)
            self.consume()
            return ('LITERAL', num)
