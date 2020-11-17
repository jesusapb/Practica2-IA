from Mutacion import *

'''
En esta clase se hace la mutacion de la poblacion, atraves de la clase mutacion 
la cual muta a los individuos uno por uno
'''
class Hacer_Mutacion:

    # al constructor se le pasa la poblacion que sera mutada y la probabilidad de mutacion respectivamente
    def __init__(self,poblacion,probabilidad):
        self.poblacion = poblacion
        self.probabilidad = probabilidad
        self.nuevaPoblacion = []

    def MutarPoblacion(self):
        for i in self.poblacion:
            #se pasa la probabilidad de mutacion y el individuo que sera mutado a la clase Mutacion
            muta = Mutacion(self.probabilidad,i)
            self.nuevaPoblacion.append(muta.mutar_individuo())
