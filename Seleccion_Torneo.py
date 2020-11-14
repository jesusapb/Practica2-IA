import random

class seleccion_torneo:

    def __init__(self,poblacion,valoresFitnes):
        print("seleccion por torneo")
        self.poblacion = poblacion
        self.valoresFitnes = valoresFitnes
        self.tama=len(self.poblacion)
        self.NuevaPoblacion = []


    def torneo(self):
        for i in range(0,self.tama):
            print(self.valoresFitnes[i])
            print(self.poblacion[i])
            num_Ale1= random.randint(0,self.tama)
            num_Ale2 = random.randint(0, self.tama)
            print("numero aleatorio 1:", num_Ale1)
            print("numero aleatorio 2:", num_Ale2)
            if self.valoresFitnes[i] > self.valoresFitnes[num_Ale1]:
                self.NuevaPoblacion.append(self.poblacion[i])
            else:
                self.NuevaPoblacion.append(self.poblacion[num_Ale1])




F=[1,3,4,5,6,2,1,8,6]

pobla= [[8,3,5,4,2,7,6,1], [5,2,8,3,7,1,4,6], [6,8,2,3,4,7,5,1], [2,4,8,7,6,3,5,1], [7,5,3,6,1,8,2,4], [2,6,8,7,1,5,4,3]]


seleccion = seleccion_torneo(pobla,F)
seleccion.torneo()
print(seleccion.NuevaPoblacion)


























