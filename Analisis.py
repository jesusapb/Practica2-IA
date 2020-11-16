

class Analisis:

    def __init__(self,valores):
        self.valores = valores
        self.EsRespuesta= True
        self.contador_izq=0
        self.contador_der=0
        self.contador_rep=0
        self.contador_total=0


    def SeRepiten(self):
        if len(self.valores) == len(set(self.valores)):
            #print("no se repite ningun elemento")
            #self.contador_rep = len(set(self.valores))
            return True
        else:
            #print("se repite uno o mas elementos")
            self.contador_rep = len(set(self.valores))
            return False
        #pass


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




##es la diagonal izquierda
##esta es la respuesta

    def tieneDiagonalIzq(self):
        j=0
        self.contador=0
        print("se verifica si tiene diangonal Izquierda")
        for i in self.valores:
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            l=0
            for k in listaTemporal:
                l = l + 1
                nuevaLista=listaTemporal[:l]
                print(nuevaLista)
                ## aqui empieza la prueba
                inicio = nuevaLista[0] + l - 1
                print(inicio)
                final = nuevaLista[l - 1]
                print(final)
                if len(nuevaLista) != 1:
                    if inicio == final:
                        print("si")
                        #aqui retornara que no cumple con evitar choques en diagonal
                        #return True
                        self.contador_izq= self.contador_izq + 1
                    else:
                        print("no")

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
                    #else:
                        #print("no")



    def tieneDiagonalDer(self):
        j=0
        print("se verifica si tiene diangonal derecha")
        for i in self.valores:
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            l=0
            for k in listaTemporal:
                nuevaLista=listaTemporal[:l + 1]
                print(nuevaLista)
                ## aqui empieza la prueba
                inicio = nuevaLista[0]
                print("contador:", l)
                print(inicio)
                final = nuevaLista[l] + l
                print(final)
                if len(nuevaLista) != 1:
                    if inicio == final:
                        print("si")
                        #aqui retornara que no cumple con evitar choques en diagonal
                        #return True
                    else:
                        print("no")
                l= l+1



    def tieneDiagonalDer2(self):
        j=0
        self.contador_der=0
        print("se verifica si tiene diagonal derecha")
        for i in self.valores:
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            l=0
            for k in listaTemporal:
                nuevaLista=listaTemporal[:l + 1]
                print(nuevaLista)
                ## aqui empieza la prueba
                inicio = nuevaLista[0]
                print("contador:", l)
                print(inicio)
                final = nuevaLista[l] + l
                print(final)
                if len(nuevaLista) != 1:
                    if inicio == final:
                        print("si")
                        #aqui retornara que no cumple con evitar choques en diagonal
                        #return True
                        self.contador_der = self.contador_der + 1
                    else:
                        print("no")
                l= l+1
        #return contador


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
                    #else:
                     #   print("no")
                l= l+1
        #return contador


    def SolucionIdeal(self):
        self.SeRepiten2()
        self.tieneDiagonalIzq3()
        self.tieneDiagonalDer3()
        self.contador_total = self.contador_izq + self.contador_der + self.contador_rep

