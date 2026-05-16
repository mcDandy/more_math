class LambdaFunction:
    __slots__ = ("params", "body", "env")
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env.copy() if env is not None else {}