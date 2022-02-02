"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estruturade de dados chamados de arrays;
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);s

Em Python nós temos as listas
numeros = [1, 'b', 3.234, True, 5]


# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3;
print(listas)
print(type(listas))


# Como acessar os dados?

print(listas[0][1])  # 2
print(listas[2][1])  # 8


print('Abaixo temos a primeira lista:')
print(listas[0][0])
print(listas[0][1])  # Imprimindo cada posição da primeira lista dentro da lista;
print(listas[0][2])
# ou
print([numero for numero in listas[0]])

print('Abaixo temos a segunda lista:')
print(listas[1][0])
print(listas[1][1])  # Imprimindo cada posição da segunda lista dentro da lista;
print(listas[1][2])
# ou
print([numero for numero in listas[1]])

print('Abaixo temos a terceira lista:')
print(listas[2][0])
print(listas[2][1])  # Imprimindo cada posição da terceira lista dentro da lista;
print(listas[2][2])
# ou
print([numero for numero in listas[2]])


# Iterando com loops em uma lista aninhada:
print('\nListas em lista aninhada:')
for lista in listas:
    for numero in lista:
        print(numero)


# List Comprehension:
[[print(valor) for valor in lista] for lista in listas]
# Lê-se: Para cada lista em listas; Para cada valor em lista, imprima valor;
"""

# Outros Exemplos

# Gerando um tabuleiro/matriz 3x3.

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

# Gerando jogadas para o jogo da velha:
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for numero in range(1, 4)]
print(velha)
# ou
[print(valor) for valor in velha]  # Para imprimir em formato do jogo.


# Gerando valor iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
