import moeda
from moeda import diminuir

p = float(input('digite o Preço: R$'))

print(f'a metade de {p} e {moeda.metade(p)}')