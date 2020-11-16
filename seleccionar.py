import math
''''
clase fallida borrarla

'''


class seleccionar:

    def __init__(self,indv,NR=0):
        #Numero de Reinas
        self.NR=NR
        #lista con la que se va a trabajar
        self.indv=indv
        self.NDunos=0

    def procesoDSelccion(self):
        numeroDunos=self.indv.count(1)
        print("Numero de unos: ")
        self.NDunos=numeroDunos
        print(numeroDunos)

        # Diferencias entre ellos, este regresa el numero de unos atravez del return
    def procesoDselcccion2(self):
        numeroDunos = self.indv.count(1)
        #print("Numero de unos: ")
        #print(numeroDunos)
        return numeroDunos

#tiene menos unos al numero de reinas que se solicita
    def MenorAlN(self):
        self.procesoDSelccion()
        if self.NDunos <= self.NR:
            return True
        else:
            return False


    def UnosEnLineas(self):
        lineas=[]
        print(len(self.indv))
        NL = math.sqrt(len(self.indv))
        print("numero de lineas")
        print(NL)
        for i in self.indv :
            print("se recorre al indivuo")



#A=[1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1]
#sel= seleccionar(4,A)
#sel.procesoDSelccion()
#print(sel.MenorAlN())
#sel.UnosEnLineas()



