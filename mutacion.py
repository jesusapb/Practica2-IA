import random

## Esta clase se usa para mutar a los invividuos bit por bit

class mutacion:

    def __init__(self, porcentaje, ind_ori):
        self.porcentaje = porcentaje
        self.ind_ori = ind_ori
        self.ind_nuevo = []

    def numero_aleatorio(self):
        return random.randint(1, 100)

    def muta_o_no(self):
        numero = self.numero_aleatorio()
        if numero <= self.porcentaje:
            #print(numero)
            return True
        else:
            #print(numero)
            return False

    def mutar_individuo(self):
        #print(self.ind_ori)
        #print(self.porcentaje)
        for i in self.ind_ori:
            mutar=self.muta_o_no()
            #print(i)
            #print(mutar)
            if mutar == True:
                #print(i)
                print("si muta")
                #print(mutar)
                if i == 1:
                    self.ind_nuevo.append(0)
                else:
                    self.ind_nuevo.append(1)
            else:
                #print(i)
                print("no muta")
                #print(mutar)
                self.ind_nuevo.append(i)

        #print(self.ind_ori)
        #print(self.ind_nuevo)
        return  self.ind_nuevo

#A=[1,1,0,1]

#num= mutacion(45,A)
#num.mutar_individuo()

#B=[1,0,0,1,1,1,0,0]
#num=mutacion(80,B)
#num.mutar_individuo()

#C=[1,1,1,1,1,1,1]
#num=mutacion(40,C)
#num.mutar_individuo()


