# calculator.py

class Calculator:
    """
    A simple calculator class to demonstrate a merge conflict.
    """

    def __init__(self, name="Calculator"):
        """Initializes the calculator."""
        self.name = name

    def add(self, a, b):
        """
        This function takes two numbers and returns their sum.
        """
        return a + b

    def subtract(self, a, b):
        """
        This function takes two numbers and returns their difference.
        """
        return a - b

if __name__ == "__main__":
    calc = Calculator("My Calc")
    print(f"Using {calc.name}")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 1 = {calc.subtract(5, 1)}")