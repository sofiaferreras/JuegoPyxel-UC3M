import pyxel 
from Point import Point

"""
Convierte la plataforma central y las dos inferiores en hielo resbaladizo si llega al centro de ellas. 
Se autodestruyen en el proceso de congelacion. 
Golpeando la plataforma justo debajo de ellos los Slipices desaparecen.
Para evitar que las plataformas se congelen Mario debe destruirlos rapidamente. 
Al comenzar una nueva fase todas las plataformas se descongelan.
"""

class Picos:
    def _init_(self, x, y):
        self.point = Point(x, y, 13, 15, 5, 5)
        self.estatico = False
        self.estaVivo = True
        self._vidas = 1 #cuando tocan la plataforma se autodestruyen despues de un tiempo

    def update(self):
        if self._vidas == 0:
            self.estaVivo = False
        elif self.estaVivo and not self.estatico:
            self.point.x = 50
            self.point.y = 210
            #podemos hacer que aparezca en un lugar random de la pantalla, (random dentro de las coordenadas de las plataformas)
        elif self.estatico and self.estaVivo:
            self.point.vy = 0
            self.point.vx = 0

    def draw(self):
        if self.estaVivo:
            pyxel.blt(self.point.x, self.point.y, 1, 30, 22, self.point.w, self.point.h, 0)