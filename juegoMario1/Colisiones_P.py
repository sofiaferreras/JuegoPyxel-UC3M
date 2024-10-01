

class Colisiones_P():
    def colide( x1, y1, x2, y2, w1, h1, w2, h2):     
        return (x2 >= x1 and x1 + w1 >= x2 and y2 >= y1 and y1 + h1 >= y2) or (x1 >= x2 and x2 + w2 >= x1 and y1 >= y2 and y2 + h2 >= y1)
    
    def colide1(objeto1,objeto2):
        # Calcular las coordenadas de los bordes de los rect�ngulos
        x1min, x1max, y1min, y1max = objeto1.point.x, objeto1.point.x + objeto1.point.w, objeto1.point.y, objeto1.point.y + objeto1.point.h
        x2min, x2max, y2min, y2max = objeto2.point.x, objeto2.point.x + objeto2.point.w, objeto2.point.y, objeto2.point.y + objeto2.point.h        
        # Verificar la falta de colisi�n en cualquiera de las direcciones


        if ((y1min<=y2max and y1min <= y2min) and (y1max >= y2min and y1max < y2max))\
              and ((x1min <= x2max and x1min<=x2min and x1max >= x2min and x1max <= x2max)\
                    or (x1max>=x2min and x1max >= x2max and x1min >= x2min and x1min <=x2max) \
                        or (x1min >= x2min and x1min <= x2max and x1max >= x2min and x1max <= x2max ) \
                            or (x1min <= x2min and x1min <= x2max and x1max >= x2min and x1max >= x2max)):
            return True
        elif ((y1max >= y2min and y1max >= y2max) and (y1min <= y2max and y1min > y2min)) \
            and ((x1min <= x2max and x1min<=x2min and x1max >= x2min and x1max <= x2max) \
                 or (x1max>=x2min and x1max >= x2max and x1min >= x2min and x1min <=x2max) \
                    or (x1min >= x2min and x1min <= x2max and x1max >= x2min and x1max <= x2max ) \
                        or (x1min <= x2min and x1min <= x2max and x1max >= x2min and x1max >= x2max)):
            return True