#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """init class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def height(self):
        """returns the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """sets the height"""
        self.__height = value
        
    @property
    def width(self):
        """returns the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value
        
    @property
    def x(self):
        """returns the value x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets the value x"""
        self.__x = value
        
    @property
    def y(self):
        """returns the value y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """sets the value y"""
        self.__y = value