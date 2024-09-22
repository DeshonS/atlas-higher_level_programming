#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class declaration"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id, x, y, size, size)
        
    def __str__(self):
        """return info about Square"""
        return "[Square] ({}} {}/{} - {}".format(self.id, 
        self.x, self.y, self.width)
    
    @property
    def size(self):
        """gets the size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value