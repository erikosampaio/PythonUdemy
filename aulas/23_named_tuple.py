"""
Módulo Collections -  Named Tuple

# Recapitulando Tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros.
exemplo:
tupla = (num1: 1, num2: 2, num3: 3)


# Fazendo o import
from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raça nome')
# cachorro é o nome da tupla, e idade, raça e nome são variáveis para o cachorro.

# Forma 2 - Named Tuple
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])


# Usando

ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados.

# Forma 1.
print(ray[0])  # Idade
print(ray[1])  # Nome
print(ray[2])  # Raça

# Forma 2.
print(ray.idade)  # Idade
print(ray.raça)  # Raça
print(ray.nome)  # Nome


print(ray.index('Chow-Chow'))  # Em qual índice Chow-Chow está na tupla?
print(ray.count('Chow-Chow'))  # Quantas vezes ocorre Chow-Chow na tupla?
"""
