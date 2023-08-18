# functions (funções)
#Parâmetros e Argumentos

# default =  aquele que vvocê define o valor no parametro

# non-default = Aquele que você não define o valor no parametro

def boas_vindas(quantidade, nome='marcos'):
    print(f'ola {nome}.')
    print(f'temos {str(quantidade)} laptops em estoque')

boas_vindas(7)


# print  realiza uma tarefa
# return  calcula e retorna um valor

def cliente1(nome):
    print(f'ola {nome}')
  

 
def cliente2(nome):
    return f'ola {nome}'


x = cliente1('maria')
y = cliente2('jose')

print(x)
print(y)

# criar uma função que soma varios numeros

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
  
x= soma(2,3,4,20)

print(x)

# define função
def somador(valor1, valor2):
    soma = valor1 * valor2
    return soma
# chama a função
res = somador(3,4)
print(f' valor e {res}')


#declaração da função
def imprime_msg(nomePessoa):
    print(f'o usuario {nomePessoa} escreveu uma mensagem')

#chamando a função
nome = input('digite seu nome: ')
imprime_msg(nome)


# criar uma função que armazena numeros e strings (dados)

#varios argumentos 

def agencia(**carro):
    return carro

print(agencia(marca='gol'))
print(agencia(marca='fiat', cor='azul', motor=1.0))
print(agencia(marca='siena', cor='branca', motor=1.0 , placa=1444))




#qual e o numero fatorial de 4


# 4 * 3 * 2 * 1 = 24

#bibliotecas prontas
import math

print(math.factorial(4))
print(math.floor(2.7))
print(math.ceil(4))



fatorial = 4 * 3 * 2 * 1
print(fatorial)


  




