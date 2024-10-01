from Point import Point 
import pyxel 



class Mario:

    def __init__(self):
        self.point = Point(0, 250, 15, 21, 0, 0)
        self.vidas = 40
        self.saltando = False
        self.puntuacion = 0
        self.derecha = False #esta variable la creamos para mejorar el personaje de Mario
        self.estatico = False

    def update(self):
        self.point.y -= self.point.vy
        self.point.vy -= 1
        self.point.vx = 4
        if self.point.y > 225: #suelo
            self.point.y = 225
            self.saltando = False 

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.point.x += self.point.vx
        if pyxel.btn(pyxel.KEY_LEFT):
            self.point.x  -= self.point.vx
        if pyxel.btnp(pyxel.KEY_UP) and not self.saltando:
            self.point.y -= 12
            self.point.vy = 12
            self.saltando = True

        #para que si se sale por la dcha vuelva por la izquierda y viceversa
        if self.point.x <- 15:
            self.point.x = 256
        if self.point.x > 256:
            self.point.x =- 15

    def draw(self):


        if pyxel.btn(pyxel.KEY_RIGHT):
            self.derecha = True
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.derecha = False

        if self.derecha:
            pyxel.blt(self.point._x, self.point._y, 1, 7, 113, 15, 20, 0)
        else:
            pyxel.blt(self.point._x, self.point._y, 1, 5, 77, 15, 20, 0)

  
