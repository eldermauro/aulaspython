# criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede
#o usuario devera fornecer as seguintes informações:
# Rendimento, altura e lagura
#o programa deve mostrar na tela a mensagem 
# "voçe necessita de x latas de tinta"

redimento = int(input('Qual e o redimento da lata? '))
altura = int(input('qual e altura da parede? '))
largura = int(input('qual e a largura da parede? '))

# altura * lagura / rendimento = qtd de latas
def calculo_tinta():
    area = altura * largura
    total = area / redimento
    print(f'você precisa de {total} latas de tinta')

calculo_tinta()