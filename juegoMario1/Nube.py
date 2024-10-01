# -*- coding: utf-8 -*-

from Point import Point 
import pyxel 

class Nube:
    
    def __init__(self, x, y):
        self.point= Point( x, y, 0, 0, 0, 0)
        
        
    def draw(self):
        pyxel.blt(self.point._x, self.point._y, 1, 240, 0, 16, 16, 12)
        



