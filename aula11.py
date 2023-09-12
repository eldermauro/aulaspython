'''
class Funcionarios:

    nome = 'elena'
    sobrenome = 'cabral'

usuario =  Funcionarios()

print(usuario.nome)
print(usuario.sobrenome)


'''
# modulo
from datetime import datetime


# criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome  + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# criar objeto
usuario1 = Funcionarios('elena', 'cabral', 2009)
usuario2 = Funcionarios('lucia', 'lima', 2005)
usuario3 = Funcionarios('lucia', 'lima', 2003)

#print(usuario1.nome  + ' ' + usuario1.sobrenome)
#print(usuario1.nome_completo())
print(Funcionarios.idade_funcionario(usuario1))

# criar parametros ######################################
#usuario1.nome = 'elena'
#usuario1.sobrenome = 'cabral'
#usuario1.data_nascimento = '12/01/2009'

#usuario2.nome = 'lucia'
#usuario2.sobrenome = 'lima'
#usuario2.data_nascimento = '12/01/2023'
######################################################
#print


# exercico
# criem uma class chamada Automoveis com parametros =  marca, ano
# obejtos locadora1, locadora2, locadora3 e imprima valores marca, ano


# criar a classe
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ExibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

    def Desligar(self):
        print('estou desligando')        
       
# criar objeto
computador1 = Computador('Asus', '16gb', 'Samsung')

computador1.ExibirInformacoes()
computador1.Desligar()

# exercico
# criem uma class chamada Automoveis com parametros =  marca, ano
# obejtos locadora1, locadora2, locadora3 e imprima valores marca, ano
