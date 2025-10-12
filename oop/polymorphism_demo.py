import math

class Shape:
    """Base class for all shapes with area calculation capability."""
    
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    """Represents a rectangle with length and width attributes."""
    
    def __init__(self, length, width):
        """Initialize rectangle with given length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate rectangle area using length × width."""
        return self.length * self.width


class Circle(Shape):
    """Represents a circle with radius attribute."""
    
    def __init__(self, radius):
        """Initialize circle with given radius."""
        self.radius = radius
    
    def area(self):
        """Calculate circle area using π × radius²."""
        return math.pi * (self.radius ** 2)