from Mutacion2 import *

class Hacer_Mutacion:

    def __init__(self,poblacion,probabilidad):
        print("Hacer mutacion")
        self.poblacion = poblacion
        self.probabilidad = probabilidad
        self.nuevaPoblacion = []

    def MutarPoblacion(self):
        for i in self.poblacion:
            muta = Mutacion2(self.probabilidad,i)
            self.nuevaPoblacion.append(muta.mutar_individuo())
