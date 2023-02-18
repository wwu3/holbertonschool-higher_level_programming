#!/usr/bin/python3
"""Import class Basee"""
from models.base import Base


class Rectangle(Base):
    """Initialize the data"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def validate_positive(self, value, name):
        """
        Function validate_positive pass the parameters value and name
        """
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_positive_or_zero(self, value, name):
        """
        Function validate_positive_or_zero pass the parameters value and name
        """
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @width.setter
    def width(self, value):
        self.validate_positive(value, "width")
        self.__width = value

    @height.setter
    def height(self, value):
        self.validate_positive(value, "height")
        self.__height = value

    @x.setter
    def x(self, value):
        self.validate_positive_or_zero(value, "x")
        self.__x = value

    @y.setter
    def y(self, value):
        self.validate_positive_or_zero(value, "y")
        self.__y = value

    def area(self):
        """
        Function area
        """
        return self.width * self.height

    def display(self):
        """
        Function display
        """
        for a in range(self.y):
            print()
        for i in range(self.height):
            print(self.x * " " + "#" * self.width)

    def __str__(self):
        """
        Function __str__ returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        str1 = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        str2 = f" - {self.width}/{self.height}"
        return str1 + str2

    def update(self, *args, **kwargs):
        """
        Function update
        """
        if len(args) > 0:
            if len(args) > 0 and args[0] is not None:
                self.id = args[0]
            if len(args) > 1 and args[1] is not None:
                self.width = args[1]
            if len(args) > 2 and args[2] is not None:
                self.height = args[2]
            if len(args) > 3 and args[3] is not None:
                self.x = args[3]
            if len(args) > 4 and args[4] is not None:
                self.y = args[4]
            return
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'height' in kwargs:
            self.height = kwargs['height']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
