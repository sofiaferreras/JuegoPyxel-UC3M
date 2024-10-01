
from Niveles import Niveles
import pyxel 

class Juego:    
    def __init__(self):
        pyxel.init(256,256,title = "Mario Bros", fps=30)
        pyxel.load("assets/marios.pyxres")

        self.nivel=Niveles()
        

        pyxel.run(self.update,self.draw)

    def update(self):
            self.nivel.update()
            
    def draw(self):
        self.nivel.draw()
Juego()
