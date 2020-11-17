'''
Esta clase se usa para graficar la primera respuesta de las  solucuciones con el proposito
de ver graficamente como seria la respuesta
'''

class GraficarRespuestas:
    #se pasa al contructor al individuo que sera imprimido
    def __init__(self,individuo):
        self.individuo=individuo
        self.tama=len(self.individuo)
        self.listaImprimible=[]

    #se contruye cada linea con la repesentacion de la ubicacion de la reina
    def construirLinea(self,N):
        Zeros=[0]*self.tama
        j=1
        for i in Zeros:
            #print(i)
            if j == N:
                Zeros[j-1]=1

            j = j + 1

        return Zeros

    #se costruye la lista con la ubicacion de cada individuo
    def construir_impresion(self):
        self.listaImprimible=[]
        for i in self.individuo:
            self.listaImprimible.append(self.construirLinea(i))

    #se imprime el tablero con las reinas
    def imprimir(self):
        self.construir_impresion()
        for i in self.listaImprimible:
            print(i)

