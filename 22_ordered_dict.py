"""
Ordered Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é farantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

OrderedDcit -> É um dicionário que nos garante a ordem de inserção dos elementos.
# Fazendo import.
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}. Valor = {valor}')

# Entendendo a diferença entre Dict e Ordered Dict.

# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True, já que a ordem dos elementos não importa para o dicionário.

# Ordered Dict.
from collections import OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odcit2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odcit2)  # False, Já que a ordem do elementos importam em Ordered Dict.
"""


