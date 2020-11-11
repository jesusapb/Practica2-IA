import  random

class CrearPoblacion:

    def __init__(self,longitud, tama):
        #longitud de la cadena
        self.longitud= longitud
        #tamaño de la poblacion
        self.tama=tama
        #poblacion
        self.poblacion = []


    def crearIndivuo(self):
        lista = list(range(1,9))
        return lista


    def creacromosoma(self):
        return random.randint(1,8)


    def crearIndividuo2(self):
        i=0
        individuo=[]
        while i < 8 :
            individuo.append(self.creacromosoma())
            i=i+1
        return individuo


    def CrearNuevaPoblacion(self):
        i=0

        while  i < self.tama:
            nuevoIndividuo= random.sample(self.crearIndivuo(),8)
            #nuevoIndividuo= self.crearIndividuo2()
            self.poblacion.append(nuevoIndividuo)
            i = i + 1

        return self.poblacion