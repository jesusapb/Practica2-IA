from Mutacion2 import *
from GenerarPoblacion import *
from intercambiar import *
from seleccionar import *
from probabilidad import *
from CrearPoblacion import *


##se define el numero de reinas
##el numero de casillas y con ello la logitud de los bits de los individuos


##se crea la poblacion
## idealmente esta poblacion sera de 100 o 1000 miembros y cada uno tendra N*N bits
poblacion_inicial= CrearPoblacion(8,4)
poblacion_inicial.CrearNuevaPoblacion()
print(poblacion_inicial.poblacion)

nuevaPoblacion=[]
respuestas=[]





#se define el proceso de mutacion con un porcentaje pequeño de cambio
for i in poblacion_inicial.poblacion:
    #print(i)
    print("comienza el proceso de mutacion:")
    muta = Mutacion2(40,i)
    #mutar.mutar_individuo()
    nuevaPoblacion.append(muta.mutar_individuo())


print(nuevaPoblacion)




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






