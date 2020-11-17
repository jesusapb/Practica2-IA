from Ocho_Reinas import *

if __name__ == "__main__":
    '''se pasa al constructor de ocho reinas, el numero de reinas, el tamaño de la poblacion, 
    el numero de iteraciones maximas, la probalilidad de cruzamiento y la probalidad de mutacion'''
    buscar = Ocho_Reinas(8,100,50,80,80)
    buscar.Generar_Poblacion()
    buscar.Buscar_Solucion()
    buscar.imprimir_Solucion()
    buscar.Graficar_Soluciones()
