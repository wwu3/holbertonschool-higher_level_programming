#!/usr/bin/python3
"""Import class Rectanglee"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialize the data"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Function update
        """
        nargs = args
        nkwargs = kwargs
        if len(args) > 1:
            nargs = nargs[0:2] + nargs[1:]
        if 'size' in kwargs:
            kwargs['width'] = kwargs['size']
            kwargs['height'] = kwargs['size']
        super().update(*nargs, **nkwargs)
