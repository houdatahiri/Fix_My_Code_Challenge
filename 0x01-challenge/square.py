#!/usr/bin/python3

class Square:
    """
    This class represents a square.
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialize the square with width and height.

        Args:
          *args: Optional arguments (not used in this case).
          **kwargs: Keyword arguments (width and height).
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
          The area of the square (width * width).
        """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.

        Returns:
          The perimeter of the square (2 * width + 2 * height).
        """
        return (2 * self.width + 2 * self.height)

    def __str__(self):
        """
        Returns a string representation of the square (width/height).
        """
        return ("%d/%d" % (self.width, self.height))

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)  # Output: 12/9
    print(s.area_of_my_square())  # Output: 144
    print(s.perimeter_of_my_square())  # Output: 42
