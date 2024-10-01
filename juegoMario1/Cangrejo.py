from Point import Point
import pyxel
import random

class Cangrejo:
    def __init__(self,x,y):
        self.point = Point(x, y, 14, 14, 1, 0)
        self._vidas = 3
        self.estaVivo = True
        self.estatico=False 
        self.estaMuerto=False
        self.direccion=1
        self.direccion2=1

    def update(self):
        if self._vidas==0:
            self.estaVivo=False 
        if self.estaVivo and not self.estatico:

            self.point.x += self.direccion * self.point.vx
            if (self.point.x <= 0 or self.point.x >=63):
                self.direccion *= -1    
        if self.estatico and self.estaVivo:
            self.point.vx=0
            self.point.vy=0

    def draw(self):
        if self.estaVivo and not self.estatico:
            pyxel.blt(self.point._x, self.point._y, 1, 8, 168, 15, 14,0) #se mueve el bicho 
        if self.estatico and self.estaVivo:
            self.point.vx=0
            pyxel.blt(self.point._x, self.point.y, 1, 8, 168, 15, 14, 0) #se para el bicho







