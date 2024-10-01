import pyxel
from Point import Point

"""
Las verdes presentan un movimiento ondulatorio en sentido horizontal y desaparecen al poco tiempo. 
Las rojas son un poco mas lentas, rebotan y no desaparecen hasta que son destruidas. 
Golpeandolas cuando toquen la plataforma desaparecen.
"""


class FireBall:
    def __init__(self, x, y):
        self.point = Point(x, y, 14, 14, 1, 1)
        self.estatico = False
        self.estaVivo = True 
        self._vidas = 1

    def update(self):
        if self._vidas == 0:
            self.estaVivo = False
        elif self.estaVivo and not self.estatico:
            self.point.x += self.point.vx
            self.point.y = 230
        elif self.estaVivo and self.estatico:
            self.point.vx = 0
            self.point.vy = 0

    def draw(self):
        if self.estaVivo:
            imagenes = [1, 2, 3, 4]
            for i in imagenes:
                if i == 1:
                    pyxel.blt(self.point.x, self.point.y, 0, 73, 216, self.point.w, self.point.h, 0)
                elif i == 2:
                    pyxel.blt(self.point.x, self.point.y, 0, 159, 215, self.point.w, self.point.h, 0)
                elif i == 3:
                    pyxel.blt(self.point.x, self.point.y, 0, 11, 216, self.point.w, self.point.h, 0)
                else:
                    pyxel.blt(self.point.x, self.point.y, 0, 94, 215, self.point.w, self.point.h, 0)