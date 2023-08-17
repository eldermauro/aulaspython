# calculando a idade com input
# variaveis guardam valores e podem ser utilizados em todo codigo..
'''
ano_nascimento = 1985
idade = 2020 - ano_nascimento

print (idade)


ano_nascimento = input('Em que ano você  nasceu? ')
idade = 2023 - int(ano_nascimento)

print(idade)

# exemplos de type
x = 2
y = 'ola'

print(type(x))
print(type(y))

# A slice()função retorna um objeto de fatia.

#Um objeto de fatia é usado para especificar como fatiar uma sequência. Você pode especificar onde começar a fatiar e onde terminar. Você também pode especificar a etapa, que permite, por exemplo, fatiar apenas itens alternados

fruta = 'Abacate'

#index   0123456
print(fruta[-1])

a = ('a', 'b', 'c', 'd', 'e', 'f')

x = slice(-1)

print(a[x])



# o marcos silva e um execelente [programador]

# formated string

#Para usar strings literais formatadas, comece uma string com f ou F antes das aspas de abertura ou aspas triplas. Dentro dessa string, você pode escrever uma expressão Python entre os caracteres { e } que podem se referir a variáveis ​​ou valores literais.

nome = 'marcos'
sobrenome = 'silva'
profissao = 'programador'

texto = 'o ' +  nome  +  sobrenome +  ' e um excelente ' + '[' + profissao +']'

texto2 = f' o {nome}  {sobrenome} e um execelente [{profissao}] '

print(texto)
print(texto2)

'''
#calculo = 2 + 2 * 3 /2
calculodois = 2 ** (3 + 4)

print(calculodois)