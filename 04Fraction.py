class Fraction:
    """
    A class to represent a mathematical fraction and demonstrate operator overloading.
    """

    def __init__(self, numerator, denominator):
        """
        Initializes the fraction with numerator and denominator.
        """
        self.num = numerator
        self.den = denominator

    def __str__(self):
        """
        Returns the string representation of the fraction.
        """
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        """
        Overloads the + operator to add two fractions.
        """
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """
        Overloads the - operator to subtract two fractions.
        """
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """
        Overloads the * operator to multiply two fractions.
        """
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """
        Overloads the / operator to divide two fractions.
        """
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def convert_to_decimal(self):
        """
        Converts the fraction to its decimal form.
        """
        return self.num / self.den


# Create two fraction objects
f1 = Fraction(2, 3)
f2 = Fraction(3, 5)

# Test operations
print("Addition:", f1 + f2)         # 19/15
print("Subtraction:", f1 - f2)      # 1/15
print("Multiplication:", f1 * f2)   # 6/15
print("Division:", f1 / f2)         # 10/9
print("Decimal of f1:", f1.convert_to_decimal())  # 0.666...
