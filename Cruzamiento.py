import random

''' En esta clase se intercabian las colas apartir de un punto aleatorio, se usa la cola
del otro padre para completar al hijo y el resto con numeros aletorios evitando repeticion'''
class Cruzamiento:

    # se pasa al constructor el individuo A, el individuo B y la probabilidad de cruzamiento
    def __init__(self,ind_A,ind_B, probabilidad):
        self.ind_A = ind_A
        self.ind_B = ind_B
        self.hijoA = []
        self.hijoB = []
        self.mutoAPartirD = 0
        self.probabilidad = probabilidad

    #se genera el numero aleatorio apartir del cual se parte para hacer el cruzamiento
    def numero_aleatorio(self):
        tama = len(self.ind_A)
        return random.randint(0, tama)


    def prob_Cruzamiento(self):
        numero = random.randint(0,100)
        if numero <= self.probabilidad:
            # print(numero)
            return True
        else:
            # print(numero)
            return False


    # se constuyen los hijos tomando bases de sus padres, ser intenrcambian
    # y se eliminan los elementos repetidos
    def Construir_Hijos(self):
        subA=[]
        subB=[]
        ApartirD = self.numero_aleatorio()
        self.mutoAPartirD = ApartirD
        i = 0
        for A, B in zip(self.ind_A, self.ind_B):
            i = i + 1
            if i > ApartirD:
                self.hijoA.append(B)
                self.hijoB.append(A)

            else:
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
