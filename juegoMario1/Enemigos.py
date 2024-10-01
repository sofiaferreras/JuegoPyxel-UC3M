
from Cangrejo import Cangrejo
from Mosca import Mosca
from Tortuga import Tortuga
from Picos import Picos 
from Fireball import FireBall

class Enemigos:
    def __init__(self, tipo,x,y):
        #podria crear posiciones aleatorias en esta 
        # clase o desde la clase main llamando a esta clase
        self._tipo = tipo
        if self._tipo == 1:
            self.enemigo = Tortuga(x,y)
            
        if self._tipo == 2:
            self.enemigo = Mosca(x,y)
            
        if self._tipo == 3:
            self.enemigo = Cangrejo(x,y)

        if self._tipo== 4:
            self.enemigos = Picos(x,y )

        if self._tipo== 5:
            self.enemigos = FireBall(x,y )

    def update(self):
        self.enemigo.update()

    def draw(self):
        self.enemigo.draw()
    
            
        




