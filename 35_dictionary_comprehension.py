"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)  # 1, 2, 3, 4

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionário = {'a': 1,'b': 2, 'c': 3, 'd': 4}
# Sintaxe dicionário comprehension:
{chave: valor for valor in interável}

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print({valor for valor in numeros.items()})

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)
# Ou
print({chave: valor ** 2 for chave, valor in numeros.items()})


# Exemplos

numeros = [1, 2, 3, 4, 5]

# Transformando lista em um dicionário:
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)
# Ou
print({valor: valor ** 2 for valor in numeros})


chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
print(chaves)
print(valores)

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
# Ou
print({chaves[i]: valores[i] for i in range(0, len(chaves))})


nomes = ['eriko', 'nayara', 'tarciane', 'paula', 'valdecio']
idades = []

mistura_dados = {}
for i, nome in enumerate(nomes):
    if nomes[i] == 'eriko':
        idades.append(28)
    elif nomes[i] == 'tarciane':
        idades.append(24)
    elif nomes[i] == 'nayara':
        idades.append(26)
    elif nomes[i] == 'valdecio':
        idades.append(21)
    elif nomes[i] == 'paula':
        idades.append(70)

mistura_dados = {nomes[i]: idades[i] for i in range(0, len(nomes))}
print(mistura_dados)
for chave, valor in mistura_dados.items():
    print(f'{chave.title()}, {valor} anos.')

for i in range(0, len(nomes)):
    print(f'{nomes[i].title()}, {idades[i]} anos.')


# Exemplo com lógica condicional:
numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
"""
