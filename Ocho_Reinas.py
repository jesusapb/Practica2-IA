import copy
from CrearPoblacion import *
from Analisis import *
from Mutacion2 import *
from Seleccion_Torneo import *
from Hacer_Mutacion import *
from  Hacer_Cruzamiento import *

class Ocho_Reinas:

    def __init__(self, NR, Tama, Prob_Mutacion, Prob_Intercambio, Num_iteraciones):
        self.NR = NR
        self.Tama = Tama
        self.Prob_Mutacion = Prob_Mutacion
        self.Prob_Intercambio = Prob_Intercambio
        self.Num_iteraciones = Num_iteraciones
        self.PoblacionInicial = []
        self.PoblacionNueva = []
        self.Respuestas = []
        #self.PoblacionTorneo = []

    def Generar_Poblacion(self):
        poblacion = CrearPoblacion(self.NR,self.Tama)
        poblacion.CrearNuevaPoblacion()
        self.PoblacionInicial = poblacion.poblacion
        print(self.PoblacionInicial)
        self.PoblacionNueva = copy.copy(self.PoblacionInicial)


    def Buscar_Solucion(self):

        j =0
        while j < self.Num_iteraciones:
            Fitnest = []
            for i in self.PoblacionNueva:
                buscar = Analisis(i)
                buscar.SolucionIdeal()
                if buscar.contador_total == 0:
                    self.Respuestas.append(i)
                Fitnest.append(buscar.contador_total)

            #Torneo
            torneo = seleccion_torneo(self.PoblacionNueva, Fitnest)
            torneo.torneo3()
            torneo.mezclar_poblacion()
            poblacionTorneo = torneo.NuevaPoblacion
            Fitnest.clear()

            #cruzamiento

            cruzamiento = Hacer_cruzamiento(poblacionTorneo, 80)
            cruzamiento.cruzarPoblacion()
            poblacionIntercambio = cruzamiento.nuevaPoblacion

            #Mutacion
            Mutar = Hacer_Mutacion(poblacionIntercambio, 40)
            Mutar.MutarPoblacion()
            poblacionMutada = Mutar.nuevaPoblacion

            self.PoblacionNueva.clear()
            self.PoblacionNueva = copy.deepcopy(poblacionMutada)
            #print(self.PoblacionNueva)

            j = j + 1

        #print(self.Respuestas)



    def imprimir_Solucion(self):
        print("respuestas: ", self.Respuestas)





buscar = Ocho_Reinas(8,100,40,40,100)
buscar.Generar_Poblacion()
buscar.Buscar_Solucion()
buscar.imprimir_Solucion()