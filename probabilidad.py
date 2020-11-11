import math


class probabilidad:

    def __init__(self,ValoresPoblacio):
        self.ValoresPoblacion=ValoresPoblacio
        self.tama=len(self.ValoresPoblacion)
        self.promedio = 0
        self.modas=[]
        #pass

##funcion incesaria
    def cal_tama(self):
        pass


    def Cal_promedio(self):
        sumaTotal=0
        for i in self.ValoresPoblacion:
            sumaTotal= sumaTotal + i

        self.promedio = (sumaTotal)/self.tama
        print(self.promedio)
        #return self.promedio


#        pass


    def media(self):
        pass


    def Cal_moda(self):
        # moda
        repeticiones = 0
        for i in self.ValoresPoblacion:
            apariciones = self.ValoresPoblacion.count(i)
            if apariciones > repeticiones:
                repeticiones = apariciones

        modas = []
        for i in self.ValoresPoblacion:
            apariciones = self.ValoresPoblacion.count(i)
            if apariciones == repeticiones and i not in modas:
                modas.append(i)
        self.modas =modas
        print("moda:", self.modas)


        pass


    def deviancion_Estandar(self):
        pass




#A=[10,1,10,34,35,67,89,98,11]

#proba=probabilidad(A)
#proba.Cal_promedio()
#print(proba.promedio)
#proba.Cal_moda()