import random

## Esta clase se usa cuando se crea a la poblacion inicial

class GenerarPoblacion:

    def __init__(self,N, tama):
        self.N=N
        #tamaño de la poblacion
        self.tama=tama
        #poblacion
        self.poblacion = []

    def definirBit(self):
        numero_A=random.randint(1, 100)
        numero = numero_A
        if numero < 50:
            # print(numero)
            return True
        else:
            # print(numero)
            return False

#se crea la lista con el numero de bits pedidos
    def crear_indiviiduo(self):
        individuo=[]
        for i in range(self.N):
            bit=self.definirBit()
            if bit == True:
                individuo.append(1)
            else:
                individuo.append(0)

        return individuo


##se crea una lista de listas con el numero de individuos pedidos
    def crear_poblacion(self):
        i=0
        while i < self.tama:
            nuevoIndividuo=self.crear_indiviiduo()
            self.poblacion.append(nuevoIndividuo)
            i= i + 1

        print(self.poblacion)


    def crea_individuo2(self):
        individuo = []
        for i in range(self.N):
            bit = self.definirBit()
            if bit == True:
                individuo.append(1)
            else:
                individuo.append(0)
        return individuo



##este metodo devuelve el valor en el return
    def crear_poblacion2(self):
        i=0
        while i < self.tama:
            nuevoIndividuo=self.crear_indiviiduo()
            self.poblacion.append(nuevoIndividuo)
            i= i + 1
        #print(self.poblacion)
        return  self.poblacion






#Nuevo_ind = GenerarPoblacion(10,4)
#print(Nuevo_ind.crear_indiviiduo())
#Nuevo_ind.crear_poblacion()

#print(Nuevo_ind.poblacion[1])





