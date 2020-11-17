
'''
En esta clase se analiza si el individos es una solucion o no, ademas genera su
valor de fitnest( atraves del contador total de choques), si es cero es solucion,
mientras mas grande sea su valor mas lejos esta de ser solucion.
'''

class Analisis:

    # Se le pasa al contructor los valores del invidividuo que
    # sera analizado atraves de la variables valores
    def __init__(self,valores):
        self.valores = valores
        self.EsRespuesta= True
        self.contador_izq=0
        self.contador_der=0
        self.contador_rep=0
        self.contador_total=0

    # se valua cuantas veces se repite la posion de una reina en el tablero
    def SeRepiten2(self):
        if len(self.valores) != len(set(self.valores)):
            rep = len(self.valores) - len(set(self.valores))
            i = 0
            k = 0
            while i <= rep:
                k = i + k
                i = i + 1
            self.contador_rep = k
        else:
            self.contador_rep= 0

    #se valua cuantos choques en diagonal  a la izquierda se
    # pueden producir para cada reina en el tablero
    def tieneDiagonalIzq3(self):
        j=0
        self.contador=0
        for i in self.valores:
            j+=1
            listaTemporal=self.valores[j-1:]
            l=0
            for k in listaTemporal:
                l = l + 1
                nuevaLista=listaTemporal[:l]
                inicio = nuevaLista[0] + l - 1
                final = nuevaLista[l - 1]
                if len(nuevaLista) != 1:
                    if inicio == final:
                        self.contador_izq= self.contador_izq + 1


    # se valua cuantos choques en diagonal a la derecha se
    # pueden producir para cada reina en el tablero
    def tieneDiagonalDer3(self):
        j=0
        self.contador_der=0
        for i in self.valores:
            j+=1
            listaTemporal=self.valores[j-1:]
            l=0
            for k in listaTemporal:
                nuevaLista=listaTemporal[:l + 1]
                inicio = nuevaLista[0]
                final = nuevaLista[l] + l
                if len(nuevaLista) != 1:
                    if inicio == final:
                        self.contador_der = self.contador_der + 1
                l= l+1

    # se evaluan los choque totales que se pueden producir y al
    # final se regresan cuantos choques tuvo en total
    def SolucionIdeal(self):
        self.SeRepiten2()
        self.tieneDiagonalIzq3()
        self.tieneDiagonalDer3()
        self.contador_total = self.contador_izq + self.contador_der + self.contador_rep

