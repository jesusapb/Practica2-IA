import random
import copy

''' 
clase fallida borrarla
'''

class Mutacion2:

    def __init__(self, porcentaje, ind_ori):
        self.porcentaje = porcentaje
        self.ind_ori = ind_ori
        self.ind_nuevo = []

    def numero_aleatorio(self):
        return random.randint(1, 100)

    def muta_o_no(self):
        numero = self.numero_aleatorio()
        if numero <= self.porcentaje:
            return True
        else:
            return False


    def mutar(self):
        ind1 =random.randint(0,7)
        ind2 = random.randint(0,7)

        ##se usa el metodo copy para disminuir
        self.ind_nuevo= copy.copy( self.ind_ori)
        bitA= self.ind_nuevo[ind1]
        bitB = self.ind_nuevo[ind2]
        self.ind_nuevo[ind1] = bitB
        self.ind_nuevo[ind2] = bitA
#        print(self.ind_ori)
        return self.ind_nuevo

    def mutar_individuo(self):
        self.ind_nuevo=[]
        mutar=self.muta_o_no()
        if mutar == True:
            #print("Si muta")
            self.ind_nuevo= self.mutar()
            return self.ind_nuevo
        else:
            #print("No muta")
            return self.ind_ori




#A=[1,2,3,4,5,6,7,8]
#muta= Mutacion2(80,A)
#muta.mutar_individuo()
#print(muta.mutar_individuo())