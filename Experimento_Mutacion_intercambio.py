from Mutacion2 import *
from GenerarPoblacion import *
from intercambiar import *
#from seleccionar import *
#from probabilidad import *
from CrearPoblacion import *
from Analisis import *
#from GraficarRespuestas import *
from Seleccion_Torneo import *



poblacion_inicial= CrearPoblacion(8,100)
poblacion_inicial.CrearNuevaPoblacion()
print(poblacion_inicial.poblacion)

nuevaPoblacion=[]
respuestas=[]


#se evalua la poblacion inicial para ver si en ella no se encuentra alguna respuesta

nuevaPoblacion=copy.deepcopy(poblacion_inicial.poblacion)

j=0

while j<10:
    Fitnest = []
    for i in nuevaPoblacion:
        buscar = Analisis(i)
        buscar.SolucionIdeal()
        #if buscar.contador_der == 0 and buscar.contador_izq == 0:
        if buscar.contador_total ==0:
            #print("Es respuesta")
            respuestas.append(i)
        Fitnest.append(buscar.contador_total)


    # Torneo
    poblacionToneo=[]
    torneo = seleccion_torneo(nuevaPoblacion,Fitnest)
    torneo.torneo4()
    poblacionToneo = torneo.NuevaPoblacion

    Fitnest.clear()

    #intercambio

    #print("mutacion")
    poblacionMutada = []
    print(j)
    print("comienza el proceso de mutacion:")
    for i in poblacionToneo:
        #print("comienza el proceso de mutacion:")
        muta = Mutacion2(40,i)
        #mutar.mutar_individuo()
        poblacionMutada.append(muta.mutar_individuo())

    nuevaPoblacion.clear()
    nuevaPoblacion= copy.deepcopy(poblacionMutada)
    print(nuevaPoblacion)

    j = j+1


print("respuestas:", respuestas)
print("poblacion inicial:",nuevaPoblacion)
