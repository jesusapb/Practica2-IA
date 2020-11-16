#la poblacion podria ser una clase propiamente
##se importara la clase seleccionar solo como parte de una prueba


import random

'''
Clase fallida borrarla
'''


class reproduccion:

    def __init__(self,poblacion,tamaPoblacion=0):
        self.poblacion=poblacion
        self.tamaPoblacion=tamaPoblacion
        self.nuevaPoblacion=[]

    def mezclarPoblacion(self):
        print("se mezcla a la poblacion para forma una nueva")
        if self.tamaPoblacion==0:
            self.tamaPoblacion=len(self.poblacion)
        self.nuevaPoblacion=random.sample(self.poblacion,self.tamaPoblacion)
        #return self.nuevaPoblacion

    def formarNuevaPoblacion(self):
        #se mezcla a la poblacion
        self.mezclarPoblacion()
        #se les cruza(intercambian colas o bits

        # muta

        #se regresa a la poblacion para ser analizada




    def imprimir_poblacion(self):


        print(self.nuevaPoblacion)
        ##pass





A=[[1,1,1,1],[0,1,1,0],[0,0,0,0],[1,0,0,1],[0,0,1,1]]
repro=reproduccion(A)
#repro.mezclarPoblacion()
repro.formarNuevaPoblacion()
repro.imprimir_poblacion()



