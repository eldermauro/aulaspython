# functions (funções)



'''
def boas_vindas():
    print( 'ola marcos')
    print('temos 5 laptops em estoque')
    print('obrigado')

boas_vindas()


def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

def somar_dois_numero1():
    numero1 = 10
    numero2 = 2
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros()
somar_dois_numero1()
'''

# functions (funções) Parâmetros e Argumentos


def boas_vindas(nome, quantidade):
    print(f'ola {nome}.')
    print(f'temos {str(quantidade)} laptops em estoque')

boas_vindas('marcos',5)
boas_vindas('lucia',5)
boas_vindas('pedro',5)

'''
def boas_vindas_marcos():
    print( 'ola marcos')
    print('temos 5 laptops em estoque')

def boas_vindas_lucia():
    print( 'ola lucia')
    print('temos 5 laptops em estoque')    
   
def boas_vindas_pedro():
    print( 'ola pedro')
    print('temos 5 laptops em estoque')   


boas_vindas_lucia()
boas_vindas_marcos()
boas_vindas_pedro()
'''