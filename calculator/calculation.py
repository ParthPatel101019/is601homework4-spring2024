from calculations import Operation


class Calculator:

    def __init__(self):
        self.calculations = Operation()

    def add(self, a, b):
        self.calculations.add_history(a, b, self.add)
        return a + b

    def subtract(self, a, b):
        self.calculations.add_history(a, b, self.subtract)
        return a - b

    def multiply(self, a, b):
        self.calculations.add_history(a, b, self.multiply)
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        # Adding only if there is no error
        self.calculations.add_history(a, b, self.divide)
        return round(a / b, 4)
    
    def get_history(self):
        return self.calculations.get_history()



# def main():
#     c = Calculator()
#     print(c.add(1, 3))
#     print(c.subtract(1, 4))
#     print(c.subtract(5, 3)    )
#     print(c.multiply(20, 3))
#     print(c.divide(10, 2))
#     print(c.divide(3, 7))
#     print(c.get_history())
    

# main()
