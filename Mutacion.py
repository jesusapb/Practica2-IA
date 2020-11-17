import random
import copy

'''
En esta clase se hace la mutacion de cada inviduo, la cual consiste en el intercambio de dos posicones al azar.
La clase recibe el porcentaje de probabilidad de mutacion y el individuo que sera mutado
'''
class Mutacion:
    # se pasa en el constructor el porcentaje de mutacion y el individuo a mutar
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

    # se muta al individuo, intercambiando dos posicones al azar
    def mutar(self):
        ind1 =random.randint(0,7)
        ind2 = random.randint(0,7)

        ##se usa el metodo copy para disminuir
        self.ind_nuevo= copy.copy( self.ind_ori)
        bitA= self.ind_nuevo[ind1]
        bitB = self.ind_nuevo[ind2]
        self.ind_nuevo[ind1] = bitB
        self.ind_nuevo[ind2] = bitA
        return self.ind_nuevo

    # se muta o no al individuo y si es el caso
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


