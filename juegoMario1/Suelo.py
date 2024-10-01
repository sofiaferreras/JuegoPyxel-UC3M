from Point import Point 
import pyxel 

class Suelo:

    def __init__(self):
        self.point=Point(0, 245, 0, 0, 0, 0)
    
    def draw(self):
        pyxel.blt(self.point._x, self.point._y, 1, 0, 240, 255, 15)


    



