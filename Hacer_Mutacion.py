from Mutacion2 import *

class Hacer_Mutacion:

    def __init__(self,poblacion,probabilidad):
        self.poblacion = poblacion
        self.probabilidad = probabilidad
        self.nuevaPoblacion = []

    def MutarPoblacion(self):
        for i in self.poblacion:
            muta = Mutacion2(self.probabilidad,i)
            self.nuevaPoblacion.append(muta.mutar_individuo())




#A= [[3,7,8,4,6,5,2,1],[2,4,3,1,5,6,7,8],[7,3,2,5,4,6,8,1],[3,7,8,5,2,1,6,4],[7,5,1,8,6,4,2,3],[3,8,4,5,1,6,2,7],[4,2,5,7,1,3,6,8],[7,4,8,3,5,6,1,2]]

#mutar = Hacer_Mutacion(A,40)
#mutar.MutarPoblacion()
#print(mutar.nuevaPoblacion)

