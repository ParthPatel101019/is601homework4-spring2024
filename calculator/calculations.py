class Operation:

    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    @staticmethod   
    def create(a, b, op):
        return Operation(a, b, op)

    def perform(self):
        return self.op(self.a, self.b)

    def __str__(self):
        return f"{self.op.__name__}({self.a}, {self.b})"
    
    def __repr__(self):
        return f"{self.op.__name__}({self.a}, {self.b})"
