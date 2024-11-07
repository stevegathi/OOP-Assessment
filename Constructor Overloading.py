class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = self.width = length  # Square case
        else:
            self.length = length
            self.width = width
    
    def area(self):
        return self.length * self.width

# Demonstration
square = Rectangle(5)
rectangle = Rectangle(5, 10)
print("Square Area:", square.area())
print("Rectangle Area:", rectangle.area())