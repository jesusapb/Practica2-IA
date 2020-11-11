

class Analisis:

    def __init__(self,valores):
        self.valores = valores
        self.EsRespuesta= True
        self.contador_izq=0
        self.contador_der=0
        #pass


    def SeRepiten(self):
        if len(self.valores) == len(set(self.valores)):
            print("no se repite ningun elemento")
            return True
        else:
            print("se repite uno o mas elementos")
            return False
        #pass


    def tieneDiagonalDer(self):
        j=0
        print("se verifica si tiene diangonal derecha")
        for i in self.valores:
            #print("El valor del bit es:")
            #print(i)
            #print("El numero de bit es:")
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[:j]
            print(listaTemporal)
            print(listaTemporal[0])
            print(listaTemporal[j-1])


            inicio=listaTemporal[0]  + j - 1
            final = listaTemporal[j-1]
            if len(listaTemporal)!= 1:
                if inicio == final:
                    print("si")
                else:
                    print("no")


    def tieneDiagonalDer2(self):
        j=0
        print("se verifica si tiene diangonal derecha")
        for i in self.valores:
            #print("El valor del bit es:")
            #print(i)
            #print("El numero de bit es:")
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            #print(listaTemporal)
            l=0
            for k in listaTemporal:
                print("hola")
                l = l + 1
                nuevaLista=listaTemporal[:l]
                print(nuevaLista)


##es la diagonal izquierda
##esta es la respuesta

    def tieneDiagonalIzq3(self):
        j=0
        self.contador=0
        print("se verifica si tiene diangonal Izquierda")
        for i in self.valores:
            #print("El valor del bit es:")
            #print(i)
            #print("El numero de bit es:")
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            #print(listaTemporal)
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









    def tieneDiagonalDer2(self):
        j=0
        print("se verifica si tiene diangonal derecha")
        for i in self.valores:
            #print("El valor del bit es:")
            #print(i)
            #print("El numero de bit es:")
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            #print(listaTemporal)
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



    def tieneDiagonalDer3(self):
        j=0
        self.contador_der=0
        print("se verifica si tiene diangonal derecha")
        for i in self.valores:
            #print("El valor del bit es:")
            #print(i)
            #print("El numero de bit es:")
            j+=1
            print("numero iteracion interna:",j)
            listaTemporal=self.valores[j-1:]
            #print(listaTemporal)
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





    def SolucionIdeal(self):
        pass

    




A=[5,2,4,7,3,8,6,1]
A1=[5,6,7,8,2,1,3,4]
A2=[5,6,4,7,3,8,2,1]
B=[4,7,3,8,2,5,1,6]
#Prueba = NuevaPrueba(A)
#print(Prueba.SeRepiten())


#A= [1,2,3,5,3,4,4,5]

Prueba= Analisis(B)
print(Prueba.SeRepiten())
#Prueba2.tieneDiagonalIzq3()
#Prueba2.tieneDiagonalIzq()
Prueba.tieneDiagonalDer3()
print(Prueba.contador_der)


Prueba2 = Analisis(A)
Prueba2.tieneDiagonalDer3()
print(Prueba2.contador_der)