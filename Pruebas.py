from Mutacion2 import *
from GenerarPoblacion import *
from intercambiar import *
from seleccionar import *
from probabilidad import *
from CrearPoblacion import *
from Analisis import *
from GraficarRespuestas import *

'''clase exitosa pero debe ser  borrada'''
##se define el numero de reinas
##el numero de casillas y con ello la logitud de los bits de los individuos


##se crea la poblacion
## idealmente esta poblacion sera de 100 o 1000 miembros y cada uno tendra N*N bits
poblacion_inicial= CrearPoblacion(8,10)
poblacion_inicial.CrearNuevaPoblacion()
print(poblacion_inicial.poblacion)

nuevaPoblacion=[]
respuestas=[]
Fitnest=[]

#se evalua la poblacion inicial para ver si en ella no se encuentra alguna respuesta

for i in poblacion_inicial.poblacion:
    buscar = Analisis(i)
    buscar.SolucionIdeal()
    #if buscar.contador_der == 0 and buscar.contador_izq == 0:
    if buscar.contador_total==0:
        #print("Es respuesta")
        respuestas.append(i)

    Fitnest.append(buscar.contador_total)

print("Estos son respuestas:")
print(respuestas)
print(len(respuestas))
if len(respuestas)>1:
    imprimir= GraficarRespuestas(respuestas[0])
    imprimir.imprimir()


print("El fitnes del corrimiento es")
print(Fitnest)


#se define el proceso de mutacion con un porcentaje pequeño de cambio
#for i in poblacion_inicial.poblacion:
#    print("comienza el proceso de mutacion:")
#    muta = Mutacion2(40,i)
    #mutar.mutar_individuo()
#    nuevaPoblacion.append(muta.mutar_individuo())
#print(nuevaPoblacion) '




#pesos=[]
#listaNDunos=[]
#for i in nuevaPoblacion:
#    PesoValor=[]
#    selec=seleccionar(i,8)
#    NDUnos=selec.procesoDselcccion2()
#    listaNDunos.append(NDUnos)
#    PesoValor=(NDUnos,i)
#    pesos.append(PesoValor)
#
#print(pesos)
#print(listaNDunos)
#probas=probabilidad(listaNDunos)
#probas.Cal_promedio()
#print(probas.promedio)
#probas.Cal_moda()
#print(probas.modas)






