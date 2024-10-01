from Point import Point
import pyxel


class Tortuga:
    def __init__(self,x,y):
        self.point = Point(x, y, 14, 14, 1, 0)
        self._vidas = 3
        self.estaVivo = True
        self.estatico=False 
        self.direccion=1



    def update(self):
        if self._vidas==0:
            self.estaVivo=False 
        if self.estaVivo and not self.estatico:
            self.point.x += self.direccion * self.point.vx
            if (self.point.x <=160 or self.point.x >=240):
                self.direccion *= -1

        if self.estatico and self.estaVivo:
            self.point.vx=0
            self.point.vy=0
    
    def draw(self):
        if self.estaVivo and not self.estatico and self.direccion>0:
            pyxel.blt(self.point.x, self.point._y, 0, 8, 96, 15, 15,0) #se mueve el bicho
        if self.estaVivo and not self.estatico and self.direccion<0:
            pyxel.blt(self.point.x, self.point._y, 0, 29, 96, 19, 19,0) #se mueve el bicho
        if self.estatico and self.estaVivo:
            pyxel.blt(self.point.x, self.point._y+4, 0, 235, 99, 11, 11,0) #se para el bicho





