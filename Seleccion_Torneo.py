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
            print("Fitnes: ",self.valoresFitnes[i])
            print("El individuo de la poblacion: ",self.poblacion[i])
            num_Ale1= random.randint(0,self.tama)
            num_Ale2 = random.randint(0, self.tama)
            print("numero aleatorio 1:", num_Ale1)
            print("numero aleatorio 2:", num_Ale2)
            if self.valoresFitnes[i] < self.valoresFitnes[num_Ale1]:
                self.NuevaPoblacion.append(self.poblacion[i])
            else:
                self.NuevaPoblacion.append(self.poblacion[num_Ale1])


    def torneo2(self):
        for i in range(0,self.tama):
            print("Fitnes: ",self.valoresFitnes[i])
            print("El individuo de la poblacion: ",self.poblacion[i])
            num_Ale1= random.randint(0,self.tama)
            num_Ale2 = random.randint(0, self.tama)
            print("numero aleatorio 1:", num_Ale1)
            print("numero aleatorio 2:", num_Ale2)
            if self.valoresFitnes[i] < self.valoresFitnes[num_Ale1]:
                self.NuevaPoblacion.append(self.poblacion[i])
            else:
                self.NuevaPoblacion.append(self.poblacion[num_Ale1])



    def torneo3(self):
        i=0
        while i< self.tama:
            if self.valoresFitnes[(i % self.tama)] < self.valoresFitnes[((i + 1)% self.tama)]:
                self.NuevaPoblacion.append(self.poblacion[(i % self.tama)])
            else:
                self.NuevaPoblacion.append(self.poblacion[(i + 1)% self.tama])
            i = i +1

    def torneo4(self):
        i=0
        while i< self.tama:
            if self.valoresFitnes[(i % self.tama)] < self.valoresFitnes[((i + 1)% self.tama)] and self.valoresFitnes[(i % self.tama)] < self.valoresFitnes[((i + 2)% self.tama)]:
                self.NuevaPoblacion.append(self.poblacion[(i % self.tama)])
            else:
                if self.valoresFitnes[((i + 1) % self.tama)] < self.valoresFitnes[(i % self.tama)] and self.valoresFitnes[((i+ 1) % self.tama)] < self.valoresFitnes[((i + 2) % self.tama)]:
                    self.NuevaPoblacion.append(self.poblacion[(i + 1) % self.tama])

                else:
                    self.NuevaPoblacion.append(self.poblacion[(i + 2) % self.tama])

            i = i + 1




F=[1,3,4,5,6,2]

pobla= [[8,3,5,4,2,7,6,1], [5,2,8,3,7,1,4,6], [6,8,2,3,4,7,5,1], [2,4,8,7,6,3,5,1], [7,5,3,6,1,8,2,4], [2,6,8,7,1,5,4,3]]


seleccion = seleccion_torneo(pobla,F)
seleccion.torneo3()
print(seleccion.NuevaPoblacion)


























