from Point import Point 
import pyxel 

class Pow:

    def __init__(self):
        #self.tocado = False
        self.point = Point(120, 200, 15, 15, 0, 0)
        self.estatico = True
    
    def draw(self):
        pyxel.blt(self.point.x, self.point.y, 0, 134, 5, 16, 15)



