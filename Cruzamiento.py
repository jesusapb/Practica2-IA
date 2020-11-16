import random
''' En esta clase se intercabian las colas apartir de un punto aleatorio, se usa la cola
del otro padre para completar al hijo y el resto con numeros aletorios evitando repeticion'''


##se cambiara el nombre a cruzar

class Cruzamiento:

    def __init__(self,ind_A,ind_B, probabilidad):
        self.ind_A = ind_A
        self.ind_B = ind_B
        self.hijoA = []
        self.hijoB = []
        self.mutoAPartirD = 0
        self.probabilidad = probabilidad


    def numero_aleatorio(self):
        tama = len(self.ind_A)
        return random.randint(0, tama)
    #        return random.randint(1,tama-1)


    def prob_Cruzamiento(self):
        numero = random.randint(0,100)
        if numero <= self.probabilidad:
            # print(numero)
            return True
        else:
            # print(numero)
            return False



    def Construir_Hijos(self):
        subA=[]
        subB=[]
        ApartirD = self.numero_aleatorio()
        self.mutoAPartirD = ApartirD
        i = 0
        for A, B in zip(self.ind_A, self.ind_B):
            #print(A)
            #print(B)
            #print("el nivel de bits recorridos es:", i)
            # print(i)
            i = i + 1
            if i > ApartirD :
                #print("se edita")
                #print("el numero aleatorio es:", ApartirD)
                #se debe verificar que no se repita
                self.hijoA.append(B)
                self.hijoB.append(A)

            else:
                #print("no se edita")
                self.hijoA.append(A)
                self.hijoB.append(B)

        subA = []
        for item in self.hijoA:
            if item not in subA:
                subA.append(item)
        self.hijoA.clear()
        self.hijoA= subA

        subB = []
        for item in self.hijoB:
            if item not in subB:
                subB.append(item)
        self.hijoB.clear()
        self.hijoB = subB

        ale_A=[]
        ale_A =random.sample(list(range(1,9)),8)
        ale_B= random.sample(list(range(1,9)),8)

        for k in self.hijoA:
            ale_A.remove(k)


        for k in self.hijoB:
            ale_B.remove(k)

        for i in ale_A:
            self.hijoA.append(i)

        for i in ale_B:
            self.hijoB.append(i)


    def procesoCruzamiento(self):
        self.hijoA=[]
        self.hijoB=[]
        #print(self.prob_Cruzamiento())
        if self.prob_Cruzamiento() ==True:
            #print("si se cruzaron")
            self.Construir_Hijos()
        else:
            #print("no se cruzaron")
            self.hijoA = self.ind_A
            self.hijoB = self.ind_B

    def resultado_reproduccion(self):
        #print("Padres")
        print(self.ind_A)
        print(self.ind_B)
        #print("hijos")
        print(self.hijoA)
        print(self.hijoB)
        if self.mutoAPartirD > 0:
            print("Se intercambio a partir de: ")
            print(self.mutoAPartirD)
        else:
            print("no hubo intercambio")

        print(self.probabilidad)



#A=[1,1,0,1]
#B=[1,0,0,1]


#C= [8,7,6,5,4,3,2,1]
#D= [1,2,3,4,5,6,7,8]

#B1 = [4,8,1,6,5,3,7,2]
#B2 = [3,6,5,8,4,2,7,1]

#cadena=intercambiar3(B1,B2,90)

#print(cadena.numero_aleatorio())
#cadena.Construir_Hijos()
#cadena.procesoCruzamiento()
#cadena.resultado_reproduccion()

#cadena.procesoCruzamiento()