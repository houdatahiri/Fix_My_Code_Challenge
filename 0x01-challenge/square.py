#!/usr/bin/python3

class Square:
    """
    This class represents a square shape with a side length.
    """

    def __init__(self, side_length):
        """
        Initializes a new Square object.

        Args:
            side_length (float): The length of a side of the square.
        """

        self.side_length = side_length

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """

        return self.side_length * self.side_length

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """

        return 4 * self.side_length

    def __str__(self):
"""
        Returns a string representation of the square in the format "side_length".
        """

        return f"Square(side_length={self.side_length})"

if __name__ == "__main__":
    square1 = Square(10)
    print(square1)  # Output: Square(side_length=10)
    print(square1.area())  # Output: 100.0
