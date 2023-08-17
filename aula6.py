

# For loop - utilizando If e Else

# eviar um email com detalhes da compra online (Maximo 3 tentativas)
# para compras confirmadas


compra_confirmada = True
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para seu email')
        break
else:
    print('falha na compra')


    # For loop - Nested Loops ( Laços aninhados)

    # outer loop  (laço externo)

    # inner loop  (loop interno)

    # For loop - Nested Loops ( Laços aninhados)
    
    # outer loop  (laço externo)

    # inner loop  (loop interno)

'''
for numero1 in range(5):
  print(numero1)
  for numero2 in range(5):
      print(numero1, numero2)
  
   

for numero1 in range(1,6):
  print('produto ' +  str(numero1))
  for numero2 in range(5):
      print(numero1, numero2)
 
# modificar de  FANTASTICO  PARA   F A N T A S T I C O


palavra = 'FANTASTICO'

for spaco in palavra:
  print( f' {spaco}', end='')
 ''' 

# criar um retangulo de 6x6
'''
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''
'''
linha = 6
colunas = 6
simbolo = '@'

for l in range(linha):
    for c in range(colunas):
        print(simbolo , end='')
    print()  

    
#== while loops ===

# excelente para loops dependentes de uma condição

# Eu preciso criar uma promoção para um produto no valor de 100 reais.

#Só que a promoção tem um porém ela começa a 100 reais e depois ela vai baixando vai para 95 reais 90

# reais 85 reais 80 reais eu quero que a cada dia ela vai ficando 5 reais mais barata.

valor = 100
dia = 1

while valor > 20:
    dia += 1
    print(f' No dia {dia} o produto vai ser vendido por {valor}')

    valor -= 5


    # operador ternario

idade = 20

#if idade >= 16:
 #   resultado = print('voto nao permitido')
#else:
  #  resultado = print('voto não permitido')

resultado = 'voto permitido' if idade >= 16 else 'voto não permitido'
print(resultado)

'''
# publicar um produto com comissão de 10% se for acima de R$: 20

valor = int(input('digite o valor do seu produto em R$: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f' o valor final do seu produto será de R${valor}')
    break