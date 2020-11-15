from Mutacion2 import *
from CrearPoblacion import *
from Analisis import *
#from GraficarRespuestas import *
from Seleccion_Torneo import *
from Hacer_Cruzamiento import *
from Hacer_Mutacion import *

poblacion_inicial= CrearPoblacion(8,50)
poblacion_inicial.CrearNuevaPoblacion()
print(poblacion_inicial.poblacion)

nuevaPoblacion=[]
respuestas=[]

#se evalua la poblacion inicial para ver si en ella no se encuentra alguna respuesta

nuevaPoblacion=copy.deepcopy(poblacion_inicial.poblacion)

j=0

while j<100:
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
    torneo.torneo3()
    torneo.mezclar_poblacion()
    poblacionToneo = torneo.NuevaPoblacion
    Fitnest.clear()

    #intercambio
    poblacionIntercambio=[]
    cruzamiento= Hacer_cruzamiento(poblacionToneo,80)
    cruzamiento.cruzarPoblacion()
    poblacionIntercambio = cruzamiento.nuevaPoblacion

    #mutacion
    poblacionMutada = []
    #print(j)
    Mutar= Hacer_Mutacion(poblacionIntercambio,40)
    Mutar.MutarPoblacion()
    poblacionMutada = Mutar.nuevaPoblacion

    nuevaPoblacion.clear()
    nuevaPoblacion= copy.deepcopy(poblacionMutada)
    print(nuevaPoblacion)

    j = j+1


print("poblacion final: ",nuevaPoblacion)
print("respuestas:", respuestas)
