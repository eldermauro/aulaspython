'''
CLAASS CARRO
VELOCIDADE MAXIMA, COR , LIGADO
'''

class Carro:
    def __init__(self, velMax, ligado, cor):
        self.velMax = velMax
        self.ligado = ligado
        self.cor = cor
    
    def Mostrar(self):
        print('Velocidade maxima: ' + str(self.velMax))
        print('cor..............: ' + self.cor)
        estado = 'sim' if self.ligado else 'N'
        print('ligado...........: ' + estado)
        print('...............................')

    def ligar(self):
        self.ligado=True

    def desligar(self):
        self.ligado=False


c1 = Carro(200,False,'preto')
c2 = Carro(120,False,'branco')   
c3 = Carro(300,False,'vermelho') 

c1.ligar()

c1.Mostrar()
c2.Mostrar()       
c3.Mostrar() 

        
  