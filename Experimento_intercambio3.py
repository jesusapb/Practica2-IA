from intercambiar3 import *
from CrearPoblacion import *



poblacion_inicial= CrearPoblacion(8,6)
poblacion_inicial.CrearNuevaPoblacion()
print(poblacion_inicial.poblacion)

nuevaPoblacion=[]

tama = len(poblacion_inicial.poblacion)

i =0
while i< tama:
    print(i)
    A= poblacion_inicial.poblacion[i]
    B= poblacion_inicial.poblacion[i +1]
    print("valor 1;",A)
    print("valor 2:",B)
    cadena = intercambiar3(A,B,80)
    cadena.procesoCruzamiento()
    nuevaPoblacion.append(cadena.hijoA)
    nuevaPoblacion.append(cadena.hijoB)
    i = i + 2

print("poblacion inicial")
print(poblacion_inicial.poblacion)

print("nueva poblacion:")
print(nuevaPoblacion)



print("tama:",tama)











