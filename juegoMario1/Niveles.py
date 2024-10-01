import pyxel  
import random


from Nube import Nube 
from Mario import Mario
from Suelo import Suelo 
from Pow import Pow
from Plataformas import Plataformas 
from Colisiones_P import Colisiones_P
from Colisiones_E import Colisiones_E
from Enemigos import Enemigos
from Moneda import Moneda


class Niveles:    
    def __init__(self):
        self.jugando = False
        self.mario = Mario()
        self.nivel = 1
        self.pow = Pow()
        self.suelo = Suelo()
        self.contador = 0
        self.moneda = []
        self.enemigos = []
        self.plataformas = []
        self.plataformas=self.crearplataformas()
        self.moneda=[]
        self.contadormonedas=0
        self.nubes = []
        for i in range(9):
            self.nubes.append(Nube(random.randint(0,250), random.randint(30, 150)))
        self.Colisiones_E= Colisiones_E()


        pyxel.run(self.update,self.draw)
    
        
    #funcion para crear las plataformas
    def crearplataformas(self):
        x=[156, 181, 166]
        y=[56,125,190]
        w=[100,75,90]
        for j in range(3):
            self.plataformas.append(Plataformas(self.nivel, 0, y[j], w[j], 7))
        for k in range(3):
            self.plataformas.append(Plataformas(self.nivel, x[k], y[k], w[k], 7))
        self.plataformas.append(Plataformas(self.nivel, 100, 110, 55, 7))
        return self.plataformas 
    
    
    #funcion para crear a los enemigos 
    def crearBichos(self, a):
        t=100
        if self.nivel==2:
            t-=50
        elif self.nivel==3:
            t-=50
        elif self.nivel==4:
            t-=50
        if pyxel.frame_count%t==0 and len(a)<=7:
            b=random.randint(1,3)
            if b==1:
                a.append(Enemigos(1,random.randint(160,200), 176))
            if b==2:
                a.append(Enemigos(2, random.randint(56,80), 231))
            if b==3:
                a.append(Enemigos(3, random.randint(14,40), 111))

        return a
    
    def crearmonedas(self,a):
        a.append(Moneda(random.randint(50,200), random.randint(50,200)))
        
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_ALT):
            self.jugando=True
        if self.jugando:
            self.mario.update()
            self.enemigos=self.crearBichos(self.enemigos)
            for e in self.enemigos:
                e.enemigo.update()
            if pyxel.frame_count%100==0:
                self.crearmonedas(self.moneda)
            
            if self.mario.puntuacion>800 and self.nivel <2:
                self.nivel=2
                self.jugando=False
                self.enemigos=[]
                for i in self.plataformas:
                    i.nivel=2
            if self.mario.puntuacion>1600 and self.nivel<3:
                self.nivel=3
                self.jugando=False
                self.enemigos=[]
                for i in self.plataformas:
                    i.nivel=3
            if self.mario.puntuacion>2400 and self.nivel<4:
                self.nivel=4
                self.jugando=False
                self.enemigos=[]
                for i in self.plataformas:
                    i.nivel=4
            if self.mario.puntuacion>3200:
                self.nivel=1
                self.jugando=False
                self.mario.puntuacion=0
                self.enemigos=[]
                for i in self.plataformas:
                    i.nivel=1
                


            #colisiones con mario y pow, si colisiona, todos los enemigos se paran
            if self.Colisiones_E.colisionObjetos(self.mario, self.pow):
                for e in self.enemigos:
                    e.enemigo.estatico = True

            #colisiones con mario y moneda, si colisiona, la puntuacion de mario sube y removemos moneda de la lista
            for m in self.moneda:
                colisionMoneda = self.Colisiones_E.colisionObjetos(self.mario, m)
                if colisionMoneda:
                    self.mario.puntuacion += 10
                    m.estaVivo = False
                    self.moneda.remove(m)
                    self.contadormonedas+=1
                    colisionMoneda = False
                    #if pyxel.frame_count % 4000 == 0:
                    #    self.moneda.append(Moneda(random.randint(30, 190), random.randint(40, 235)))



            #colisiones con mario y enemigos
            for e in self.enemigos:
                ataque = self.Colisiones_E.colisionObjetos(self.mario, e.enemigo)
                if ataque == True and e.enemigo.estatico == True:
                    e.enemigo._vidas -= 1
                    if e.enemigo._vidas == 0: #cuando ya no tenga vidas lo retiramos de la lista
                        self.enemigos.remove(e)
                        self.mario.puntuacion += 200
                elif ataque == True and e.enemigo.estatico == False:
                        self.mario.vidas -= 1
                        self.mario.point.x+=2 
                #podriamos hacer un move de enemigos para ponerlo aqui y asi hacer que se sigan moviendo

            #colisiones con mario, las plataformas y las tuberias
            for i in self.plataformas:
                if self.mario.point.vy >0:
                    if Colisiones_P.colide(i.point.x, i.point.y,self.mario.point.x,self.mario.point.y,i.point.w,i.point.h,self.mario.point.w,self.mario.point.h) and self.mario.saltando:
                        self.mario.point.vy = 0

                        self.mario.point.y = i.point.y + i.point.h+1
                        self.mario.saltando = False
                if self.mario.point.vy <0:
                    if Colisiones_P.colide1(self.mario, i):
                        self.mario.point.vy = 0
                        self.mario.saltando = False

            
            
    def draw(self):
        if self.jugando == False and self.mario.vidas > 0:
            
            pyxel.cls(0)
            pyxel.blt(27, 70, 2, 22, 10, 223, 75)
            pyxel.text(80,180, "Presiona ALT para jugar", 8)
            pyxel.text(110, 200, "NIVEL " + str(self.nivel), 9)
            if pyxel.btn(pyxel.KEY_ALT):
                self.jugando=True
            
        else:
            if self.mario.vidas==0:
                pyxel.cls(0)
                pyxel.blt(27, 70, 2, 22, 10, 223, 75)
                pyxel.text(100,180, "GAME OVER", 8)
                pyxel.text(80,210, "PRESIONA Q PARA SALIR", 8)
                if pyxel.btn(pyxel.KEY_ALT):
                    self.jugando=True
                    self.mario.puntuacion = 0

            if self.mario.vidas>0 and self.jugando==True: 
                if self.nivel==1:
                    pyxel.cls(12)
                if self.nivel==2:
                    pyxel.cls(3)
                if self.nivel==3:
                    pyxel.cls(11)
                if self.nivel==4:
                    pyxel.cls(13)
                
                pyxel.blt(10, 5, 0, 212, 173, 6, 6, 0)
                puntuacion = " = " + str(self.mario.puntuacion)
                pyxel.text(15, 6, puntuacion, 2)
                monedas="--" + str(self.contadormonedas)
                pyxel.blt(180, 10, 2, 168, 137, 10, 10 ,0)
                pyxel.text(190, 15, monedas, 2  )
                vidas="VIDAS-" + str(self.mario.vidas)
                pyxel.text(110, 5, vidas, 2  )

                for i in self.nubes:
                    i.draw()

                self.pow.draw()

                for e in self.enemigos:
                    e.enemigo.draw()

                self.suelo.draw()

                for m in self.moneda:
                    m.draw()

                for i in self.plataformas:
                    i.draw()

                # for t in self.tuberias:
                #     t.draw()

                self.mario.draw()
