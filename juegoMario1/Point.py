# -*- coding: utf-8 -*-


class Point():
    def __init__(self, x, y, w, h, vx = 0, vy= 0): #x, y, ancho, altura, velocidad en x, velocidad en y
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._vx = vx
        self._vy = vy
        
    @property 
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x=value 
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y=value

    @property 
    def w(self):
        return self._w

    @w.setter
    def w(self,value):
        self._w=value

    @property 
    def h(self):
        return self._h

    @h.setter
    def h(self,value):
        self._h=value
     
    @property 
    def vx(self):
        return self._vx

    @vx.setter
    def vx(self,value):
        self._vx = value 

    @property 
    def vy(self):
        return self._vy

    @vy.setter
    def vy(self,value):
        self._vy = value 



