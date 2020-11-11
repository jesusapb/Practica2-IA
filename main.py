from mutacion import *
from GenerarPoblacion import *
from intercambiar import *
from seleccionar import *

##se define el numero de reinas
##el numero de casillas y con ello la logitud de los bits de los individuos


##se crea la poblacion
## idealmente esta poblacion sera de 100 o 1000 miembros y cada uno tendra N*N bits
Nueva_poblacion= GenerarPoblacion(64,10)
Nueva_poblacion.crear_poblacion()
#poblacion=Nueva_poblacion.crear_poblacion2()
#print(poblacion)
mutar= mutacion(1, Nueva_poblacion.poblacion[1])
mutar.mutar_individuo()

cadena = intercambiar(Nueva_poblacion.poblacion[0],Nueva_poblacion.poblacion[1],60)
cadena.procesoCruzamiento()
cadena.resultado_reproduccion()

seleccion = seleccionar(8,cadena.hijoA)
seleccion.procesoDSelccion()

print(seleccion.MenorAlN())


