

class Analisis:

    def __init__(self,valores):
        self.valores = valores
        self.EsRespuesta= True
        self.contador_izq=0
        self.contador_der=0
        self.contador_rep=0
        #pass


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
        #if self.SeRepiten()==False:
        #    print("se repiten valores")
            #print(self.contador_rep)
        #self.tieneDiagonalIzq()
        #self.tieneDiagonalDer2()
        self.tieneDiagonalIzq3()
        self.tieneDiagonalDer3()
        #print("Pesos:")
        #print(self.contador_izq)
        #print(self.contador_der)

    




A=[5,2,4,7,3,8,6,1]
A1=[5,6,7,8,2,1,3,4]
A2=[5,6,4,7,3,8,2,1]
B=[4,7,3,8,2,5,1,6]
C1=[1,2,3,4,5,6,7,8]
C2=[8,7,6,5,4,3,2,1]
C3=[1,2,3,4,8,7,6,5]
C4=[1,8,2,7,3,6,4,5]
C5=[1,1,1,1,2,2,2,2]
#Prueba = NuevaPrueba(A)
#print(Prueba.SeRepiten())


#A= [1,2,3,5,3,4,4,5]

#Prueba= Analisis(B)
#print(Prueba.SeRepiten())
#Prueba2.tieneDiagonalIzq3()
#Prueba2.tieneDiagonalIzq()
#Prueba.tieneDiagonalDer2()
#print(Prueba.contador_der)


#Prueba = Analisis(C5)
#Prueba2.tieneDiagonalDer2()
#print(Prueba2.contador_der)
#Prueba.SolucionIdeal()