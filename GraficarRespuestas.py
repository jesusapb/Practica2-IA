

class GraficarRespuestas:

    def __init__(self,individuo):
        self.individuo=individuo
        self.tama=len(self.individuo)
        self.listaImprimible=[]

    def construirLinea(self,N):

        Zeros=[0]*self.tama
        j=1
        for i in Zeros:
            #print(i)
            if j == N:
                Zeros[j-1]=1

            j = j + 1

        return Zeros

    def construir_impresion(self):
        self.listaImprimible=[]
        for i in self.individuo:
            self.listaImprimible.append(self.construirLinea(i))




    def imprimir(self):
        self.construir_impresion()

        for i in self.listaImprimible:
            print(i)






A = [1,2,3,4,5,6,7,8]
A1= [1,8,2,7,3,6,4,5]
A2= [5,2,4,7,3,8,6,1]
A3= [1,5,8,6,3,7,2,4]





imprimir=GraficarRespuestas(A3)
#imprimir.construirLinea(8)
#imprimir.construir_impresion()
imprimir.imprimir()
