
"""
qtde = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtde + 1):
    num = int(input(f'Informe o {n}/{qtde} valor: '))
    soma = soma + num
print(f'A soma é {soma}.')


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for valor in enumerate(nome):
    print(valor)

nome = 'Geek University'
for indice in nome:
    print(indice, end='') -> esse termo ->end=<- serve para não pular de linha

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

"""Original: U+1F60D
# Modificado: U0001F60D

# emoji = 'U0001F605'

# for _ in range(3):
#     for num in range(1, 11):
#         print('\U0001F605' * num)
"""

nome = 'Geek University'
for letra in nome:
    print(letra, end='')
