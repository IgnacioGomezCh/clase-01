class Calculator:
    """
    A simple calculator class to demonstrate a merge conflict.
    """

    def init(self, name="Calculator"):
        """Initializes the calculator."""
        self.name = name

    def add(self, a, b):
        """
        This function takes two numbers and returns their sum.
        """
        # Friend's change: Add a more descriptive comment and a different return format
        # This function calculates the sum of two inputs
        result = a + b
        return f"The sum is: {result}"

    def subtract(self, a, b):
        """
        This function takes two numbers and returns their difference.
        """
        return a - b

if name == "main":
    calc = Calculator("My Calc")
    print(f"Using {calc.name}")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 1 = {calc.subtract(5, 1)}")

