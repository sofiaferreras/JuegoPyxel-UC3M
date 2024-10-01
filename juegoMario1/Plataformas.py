

from Point import Point
import pyxel 

class Plataformas:

    def __init__(self, nivel, x, y, w, h):
        self.nivel = nivel
        self.point = Point(x, y, w, h)
        self.estatico = True
        
        #creamos los points de las tuberias
        self.point_ti_a = Point(0, 20, 48, 28, 0, 0)
        self.point_ti_ab = Point(0, 220, 32, 17, 0, 0)
        self.point_td_a = Point(209, 20, 48, 28, 0, 0)
        self.point_td_ab = Point(224, 220, 32, 17, 0, 0)


    def draw(self):

        pyxel.blt(self.point_ti_a.x, self.point_ti_a.y, 0, 52, 8, self.point_ti_a.w, self.point_ti_a.h, 0) #tuberia arriba-izq
        pyxel.blt(self.point_ti_ab.x, self.point_ti_ab.y, 0, 212, 196, self.point_ti_ab.w, self.point_ti_ab.h, 0) #tuberia bajo-izq
        pyxel.blt(self.point_td_a.x, self.point_td_a.y, 0, 202, 222, self.point_td_a.w, self.point_td_a.h, 0) #tuberia arriba-dcha
        pyxel.blt(self.point_td_ab.x, self.point_td_ab.y, 0, 11, 20, self.point_td_ab.w, self.point_td_ab.h, 0) #tuberia bajo-dcha
        if self.nivel == 1:
            pyxel.blt(self.point.x, self.point.y, 0, 134, 28, self.point.w, self.point.h, 0)
        
        if self.nivel == 2:
            pyxel.blt(self.point.x, self.point.y, 0, 134, 28, self.point.w, self.point.h, 4)

        if self.nivel == 3:
            pyxel.blt(self.point.x, self.point.y, 0, 134, 28, self.point.w, self.point.h, 9)

        if self.nivel == 4:
            pyxel.blt(self.point.x, self.point.y, 0, 134, 28, self.point.w, self.point.h, 6)

  
