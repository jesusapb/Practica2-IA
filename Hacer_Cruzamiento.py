from intercambiar3 import *

class Hacer_cruzamiento:

    def __init__(self, poblacion, probabilidad):
        self.poblacion = poblacion
        self.nuevaPoblacion = []
        self.tama = len(self.poblacion)
        self.probabilidad = probabilidad
        print("hacer cruzamiento")



    def cruzarPoblacion(self):
        i =0
        while i < self.tama:

            A = self.poblacion[i]
            B = self.poblacion[i+1]

            cambio = intercambiar3(A,B, self.probabilidad)
            cambio.procesoCruzamiento()
            self.nuevaPoblacion.append(cambio.hijoA)
            self.nuevaPoblacion.append(cambio.hijoB)
            i= i + 2


#A = [[3,7,8,4,6,5,2,1],[2,4,3,1,5,6,7,8],[7,3,2,5,4,6,8,1],[3,7,8,5,2,1,6,4],[7,5,1,8,6,4,2,3],[3,8,4,5,1,6,2,7],[4,2,5,7,1,3,6,8],[7,4,8,3,5,6,1,2]]

#cruzamiento = Hacer_cruzamiento(A,80)
#cruzamiento.cruzarPoblacion()
#print(cruzamiento.nuevaPoblacion)
