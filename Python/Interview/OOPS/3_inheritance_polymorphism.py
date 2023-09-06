"""
   - Create a base class `Shape` with subclasses `Circle` and `Rectangle`.
   Implement methods to calculate area for each shape.
"""


class Shape:
    def __init__(self, length) -> None:
        self.length = length

    def display(self):
        print(f"The length is {self.length}")


class Circle(Shape):
    def __init__(self, length) -> None:
        super().__init__(length)

    def area_of_circle(self):
        print(f"Area of a circle is {3.14 * self.length * self.length}")


class Rectange(Shape):
    def __init__(self, length, breadth) -> None:
        super().__init__(length)
        self.breadth = breadth

    def area_of_rectange(self):
        print(f"Area of a rectange is {self.length * self.breadth}")


New_circle = Circle(12)
New_circle.area_of_circle()

New_Rectangle = Rectange(12, 12)
New_Rectangle.area_of_rectange()
