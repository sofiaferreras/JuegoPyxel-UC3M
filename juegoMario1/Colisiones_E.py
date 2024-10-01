

class Colisiones_E:

    def colide2(self, objeto1,objeto2):
        # Calcular las coordenadas de los bordes de los rect�ngulos
        x1min, x1max, y1min, y1max = objeto1.point.x, objeto1.point.x + objeto1.point.w, objeto1.point.y, objeto1.point.y + objeto1.point.h
        x2min, x2max, y2min, y2max = objeto2.point.x, objeto2.point.x + objeto2.point.w, objeto2.point.y, objeto2.point.y + objeto2.point.h        
        # Verificar la falta de colisi�n en cualquiera de las direcciones


        if ((y1min<=y2max and y1min <= y2min) and (y1max >= y2min and y1max < y2max))\
              and ((x1min <= x2max and x1min<=x2min and x1max >= x2min and x1max <= x2max)\
                    or (x1max>=x2min and x1max >= x2max and x1min >= x2min and x1min <=x2max) \
                        or (x1min >= x2min and x1min <= x2max and x1max >= x2min and x1max <= x2max ) \
                            or (x1min <= x2min and x1min <= x2max and x1max >= x2min and x1max >= x2max)):
            return ["arriba", y2min - objeto1.point.h] #nos sirve para cuando ambos objetos se mueven?

        elif ((y1max >= y2min and y1max >= y2max) and (y1min <= y2max and y1min > y2min)) \
            and ((x1min <= x2max and x1min<=x2min and x1max >= x2min and x1max <= x2max) \
                 or (x1max>=x2min and x1max >= x2max and x1min >= x2min and x1min <=x2max) \
                    or (x1min >= x2min and x1min <= x2max and x1max >= x2min and x1max <= x2max ) \
                        or (x1min <= x2min and x1min <= x2max and x1max >= x2min and x1max >= x2max)):
            return ["abajo", y2max]
        
        elif (((x1max >= x2min and x1max >= x2max) and (x1min <= x2max and x1min >= x2min)) \
              and ((y1min <= y2min and y1min <= y2max and y1max >= y2min and y1max <= y2max) \
                   or (y1min >= y2min and y1min <= y2max and y1max >= y2min and y1max <= y2max) \
                    or (y1min >= y2min and y1min <= y2max and y1max >= y2min and y1max >= y2max) \
                        or (y1min <= y2min and y1min <= y2max and y1max >= y2min and y1max >= y2max))):
            return ["derecha", x2max] #se acerca por la derecha
        
        elif (((x1min <= x2min and x1min <= x2max) and (x1max >= x2min and x1max <= x2max)) \
              and ((y1min <= y2min and y1min <= y2max and y1max >= y2min and y1max <= y2max) \
                   or (y1min >= y2min and y1min <= y2max and y1max >= y2min and y1max <= y2max) \
                    or (y1min >= y2min and y1min <= y2max and y1max >= y2min and y1max >= y2max) \
                        or (y1min <= y2min and y1min <= y2max and y1max >= y2min and y1max >= y2max))):
            return ["izquierda",x2min - objeto1.point.w] #se acerca por la izquierda


    #llamamos a nuestra funcion colisiones; si colisionan dos objetos, dependiendo de donde y como, pasan x cosas
    def colisionObjetos(self, objeto1, objeto2):
        a = self.colide2(objeto1,objeto2)
        objeto1 = objeto1
        objeto2 = objeto2
    
        if a is not None:        
            if a[0]== "arriba":
                objeto1.point.y = a[1]
                objeto1.point.vy = 0
                objeto1.saltando = False
                objeto1.point.x =  objeto1.point.x

            if a[0] == "abajo":
                objeto1.point.y = a[1]
               
                if a[1] >= 225:
                    objeto1.point.y = 245 -    objeto1.point.h
                    objeto2.point.y = 245 - objeto2.point.h
                    objeto1.point.x =  objeto1.point.x
                    objeto1.point.vy -= 1
              
               
            if a[0] == "derecha": 
                objeto1.point.x = a[1]
                if not  objeto1.estatico and not objeto2.estatico:
                    objeto2.point.x =  objeto1.point.x -    objeto2.point.w
                    objeto1.point.vx = 0
                    objeto1.point.vy = 0
                    objeto2.point.vx = 0
                    objeto2.point.vy = 0
                
            if a[0] == "izquierda":
                objeto1.point.x = a[1]
                if not  objeto1.estatico and not objeto2.estatico:
                    objeto2.point.x =  objeto1.point.x -    objeto2.point.w
                    objeto1.point.vx = 0
                    objeto1.point.vy = 0
                    objeto2.point.vx = 0
                    objeto2.point.vy = 0
            return True