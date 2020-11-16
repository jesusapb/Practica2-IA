import  random
'''  
En esta clase se crea a la poblacion, en base a la logitud y al tamaño que se pasan en el constructor
se regresa a traves del atributo poblacion
'''

class CrearPoblacion:

    def __init__(self,longitud, tama):
        #longitud de la cadena
        self.longitud= longitud
        #tamaño de la poblacion
        self.tama=tama
        #la poblacio, se crea la lista vacia para facilitar el manejo
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





#poblacion= CrearPoblacion(8,8)
#poblacion.CrearNuevaPoblacion()
#print(poblacion.poblacion)




