'''

numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
mtultiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma)  # 7
print(subtracao) # 3
print(mtultiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25

#Uma característica importante a ser observada quando falamos dos operadores matemáticos é a precedência. Essa característica é relativa à ordem da execução deles e acontece quando mais de um operador está presente numa expressão. Segue a precedência dos operadores no Python
 
print((2 + 5) * 3) # resultado e 21 precedência ()

print ( 1 + 5**2 ) # resultado e 26 precedência **

print ( 5 * 3 + 8) # resultado 23 precedência * /


#Operadores de atribuição
#Os operadores de atribuição atribuem valor a uma variável. 

x = 10 
#x = x + 5

x += 5

print(x)

#Operadores de comparação
#Os operadores de comparação são usados para comparar valores, o que vai retornar True ou False, dependendo da condição.

numero_1 = 4
numero_2 = 6

soma = numero_1 + numero_2

if soma < 10:
    print ("soma não e maior que 10")
else:
    print("soma e maior ou igual a 10")




soma_1 = 7 + 7
soma_2 = 10 + 5



if soma_1 == soma_2:
    print ("os resultados são iguais")
else:
    print("os resultados são diferentes")

    '''

# >(Maior que)	Verifica se um valor é maior que outro	x > 5
# <(Menor que)	Verifica se um valor é menor que outro	x < 5
# == (Igual a)	Verifica se um valor é igual a outro	x == 5
# != (Diferente de)	Verifica se um valor é diferente de outro	x != 5
# >= (Maior ou igual a)	Verifica se um valor é maior ou igual a outro	x >= 5
# <= (Menor ou igual a)	Verifica se um valor é menor ou igual a outro	x <= 5

velocidade = 50

if velocidade > 110:
    print('Acima da velocidade permitida')
    print('Fvor reduzir a sua velocidade')
elif velocidade < 60:
    print(' favor dirigir acima de 80km/h')
else:
    print('velocidade ok')
