
from Point import Point
import pyxel

class Mosca:
    def __init__(self,x,y):
        self.point = Point(x, y, 14, 14, 1, 1)
        self._vidas = 3
        self.estaVivo = True
        self.estatico=False 
        self.estaMuerto=False
        self.direccion = 1

    def update(self):
        if self._vidas==0:
            self.estaVivo=False 
        if self.estaVivo and not self.estatico:
            self.point.x += self.point.vx
            self.point.y += self.point.vy * self.direccion
        # Si el objeto alcanza los límites de la ventana, invertir la dirección
            if self.point.y <=195 or self.point.y >= 230:
                self.direccion *= -1
            if (self.point.x>=200 and self.point.x<=255) and self.point.y>=231:  # Si el objeto sale del borde derecho abajo
                self.point.x = 56
                self.point.y = 20
                self.point.vy=8
            if (self.point.x<=55 and self.point.x>=1) and self.point.y>=231: # Si el objeto sale del borde izquierda abajo
                self.point.x = 200
                self.point.y = 20
            if self.point.x>=200 and self.point.x<=255: # Si el objeto sale del borde derecho arriba
                self.point.x = 56
                self.point.y = 231
            if self.point.x<=55 and self.point.x>=1:
                self.point.x = 200
                self.point.y = 231
        if self.estatico and self.estaVivo:
            self.point.vx=0
            self.point.vy=0

    def draw(self):
        if self.estaVivo and not self.estatico:
            pyxel.blt(self.point._x, self.point._y, 1, 10, 185, 14, 14,0)  #se mueve el bicho 
        if self.estatico and self.estaVivo:
            self.point.vx=0
            pyxel.blt(self.point._x, self.point._y, 1, 10, 185, 14, 14,0)  #se para el bicho




