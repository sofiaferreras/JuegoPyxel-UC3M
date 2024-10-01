from Point import Point
import pyxel

class Moneda():
    def __init__(self, x, y):
        self.point = Point(x, y, 10, 10)
        self.estaVivo = True
        self.estatico = True
    def update(self):
        if not self.estaVivo:
            if pyxel.frame_count % 4000 ==0:
                self.estaVivo = True
            else:
                self.estaVivo = False
                
    def draw(self):
         if self.estaVivo:
            pyxel.blt(self.point.x, self.point.y, 2, 168, 137, self.point.w, self.point.h,0)
