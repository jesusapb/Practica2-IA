import copy
from CrearPoblacion import *
from Analisis import *
from Seleccion_Torneo import *
from Hacer_Mutacion import *
from  Hacer_Cruzamiento import *
from GraficarRespuestas import *

'''
Aqui se desarrolla el algoritmo de programacion genetica
'''


class Ocho_Reinas:
    #se pasa al constructor el numero de reinas, el tamaño de la poblacion,
    # el numero de iteraciones, la probabilidad de mutacion y la probabilidad de cruzamiento
    def __init__(self, NR, Tama,Num_iteraciones, Prob_Mutacion, Prob_Cruzamiento):
        self.NR = NR
        self.Tama = Tama
        self.Prob_Mutacion = Prob_Mutacion
        self.Prob_Cruzamiento = Prob_Cruzamiento
        self.Num_iteraciones = Num_iteraciones
        self.PoblacionInicial = []
        self.PoblacionNueva = []
        self.Respuestas = []

    # se genera la poblacion inicial y se crea la nueva poblacion
    def Generar_Poblacion(self):
        poblacion = CrearPoblacion(self.NR,self.Tama)
        poblacion.CrearNuevaPoblacion()
        self.PoblacionInicial = poblacion.poblacion
        print("Poblacion Inicial: ",self.PoblacionInicial)
        self.PoblacionNueva = copy.copy(self.PoblacionInicial)

    #se busca la solucion evaluando la poblacion, haciedo el torneo, cruzamiento
    # y mutacion de la poblacion, esto se repite por el numero de iteraciones indicada
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
            torneo.torneo4()
            torneo.mezclar_poblacion()
            poblacionTorneo = torneo.NuevaPoblacion
            Fitnest.clear()

            #cruzamiento
            cruzamiento = Hacer_cruzamiento(poblacionTorneo,self.Prob_Cruzamiento)
            cruzamiento.cruzarPoblacion()
            poblacionIntercambio = cruzamiento.nuevaPoblacion

            #Mutacion
            Mutar = Hacer_Mutacion(poblacionIntercambio, self.Prob_Mutacion)
            Mutar.MutarPoblacion()
            poblacionMutada = Mutar.nuevaPoblacion

            self.PoblacionNueva.clear()
            self.PoblacionNueva = copy.deepcopy(poblacionMutada)
            j = j + 1
            #print(self.PoblacionNueva)


    #se imprime las respuestas y el numero de respuestas
    def imprimir_Solucion(self):
        print("poblacion final:", self.PoblacionNueva)
        print("respuestas: ", self.Respuestas)
        print("Numero de Soluciones:", len(self.Respuestas))



    # se grafica la primera solucion como ejemplo de como leer las respuestas
    def Graficar_Soluciones(self):
        if len(self.Respuestas) >1:
            imprimir=GraficarRespuestas(self.Respuestas[0])
            imprimir.imprimir()
