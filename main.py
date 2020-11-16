from Ocho_Reinas import *

if __name__ == "__main__":
    buscar = Ocho_Reinas(8, 100, 80, 40, 100)
    buscar.Generar_Poblacion()
    buscar.Buscar_Solucion()
    buscar.imprimir_Solucion()
    buscar.Graficar_Soluciones()