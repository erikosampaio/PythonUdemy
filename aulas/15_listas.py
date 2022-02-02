"""
Listas (list)

Em python funcionam como vetores/matrize (sarrays) em outras linguagens, com a
diferença de serem DINÂMICOS e também podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array tipo int e com tamanho 5, este
    array será SEMPRE do tipo inteiro e poderá SEMPRE no máximo 5 valores.

Jé em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir
adicionando elementos (enquanto a memória suportar);
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar
qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis, ou seja, elas podem mudar constantemente.


type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')



#  Podemos facilmente checar se determinado valor está contido na lista.
num = 7
if num in lista4:
    print(f'Encontrei o número {num}.')
else:
    print(f'Não encontrei o número {num}.')



#  Podemos facilmente ordenar uma lista.
lista1.sort()
print(lista1)



#  Podemos facilmente contar o número de ocorrências de um valor em uma lista.
print(lista1.count(1))
print(lista5.count('e'))


# Podemos adicionar elementos em litas, utilizando a função append.
print(lista1)
lista1.append(42)
print(lista1)

#  OBS: Com append, nós só conseguimos adicionar um elemento por vez.
#  lista1.append(12, 34, 56)  # Erro

lista1.append([8, 3, 1])  # Coloca a lista como elemente único
# (sublista), ou seja, # é criado uma lista dentro da "principal".
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista.')
else:
    print('Não encontrei a lista.')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional
à lista, ou seja, o valor é inserido individualmente na lista "principal".
print(lista1)



#  Podemos inserir um novo elemento na lista informando a posição no índice.
#  OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita na lista.
lista1.insert(2, 'Novo valor')
print(lista1)



# Podemos facilmente juntar duas listas.
lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)



#  Podemos facilmente inverter uma lista.
#  Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])



#  Copiar uma lista.
lista6 = lista2.copy()
print(lista6)



#  Podemos contar quantos elemente existem dentro de uma lista
print(len(lista5))



#  Podemos remover facilmente o último elemento de uma lista.
#  OBS: O pop não somente remove o último elemento, mas também o retorna.
print(lista5)
lista5.pop()
print(lista5)
#  Podemos remover um elemento pelo índice.
#  OBS:  Os elementos a direita deste índice serão deslocados à esquerda.
#  OBS: Se não houver elemento no índice informado, teremos o erro 'index error'.
lista5.pop(2)
print(lista5)



#  Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)



#  Podemos facilmente repetir elementos em uma lista.
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)



#  Podemos facilmente converter uma string para uma lista.
#  OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.
# Exemplo 1:
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#  Exemplo 2:
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)



#  Convertendo uma lista em uma string.
lista6 = ['Programação', 'em', 'Phyton:', 'Essencial']
print(lista6)
print(type(lista6))

#  Abaixo estamos falando: Pega a 'lista6', coloca espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista6)
print(curso)
print(type(curso))

#  Abaixo estamos falando: Pega a 'lista6', coloca cifrão entre cada elemento e transforma em uma string.
curso = '$'.join(lista6)
print(curso)



#  Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados.
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(lista6)
print(type(lista6))


#  Iterando sobre listas.
#  Exemplo 1 - Utilizando for:
soma = 0
for elemento in lista4:
    print(elemento)
    soma += elemento
print(soma)

#  Exemplo 2 - Utilizando while:
carrinho = []
produto = ''
while produto != 'sair':
    produto = input("Digite um produto na lista ou digite 'sair' para sair: ").lower()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)



#  Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada.
#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa.
# Para entender melhor o índice negativo pense na lista como um
# círculo, onde o final de um elemento # está ligado ao fim da lista.

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # Erro, pois não existe índice -5.


# Imprimindo listas com loops.
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


# Gerando índice em um for.
for indice, cor in enumerate(cores):
    print(indice, cor)



# Listas aceitam valores repetidos.
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)


# Outros métodos não tão importantes, mas também úteis.
# Encontrar um índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
# Qual o índice na lista do número 6?
print(numeros.index(6))

# Qual o índice na lista do número 9?
print(numeros.index(9))

# OBS: Caso não tenha o elemento requerido na lista, será apresentado erro 'ValueError'.
# print(numeros.index(19)) # 19 não existe na lista.

# Retorna o índice do primeiro elemente encontrado.
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar.
print(numeros.index(5, 1))  # Buscando a partir do índice 1.
print(numeros.index(5, 2))  # Buscando a partir do índice 2.
print(numeros.index(5, 3))  # Buscando a partir do índice 3.
# print(numeros.index(5, 4))  # Buscando a partir do índice 4.
# OBS: Caso não tenha o elemento requerido na lista, será apresentada erro 'ValueError'.

# Podemos fazer busca dentro de um range, início/fim.
print(numeros.index(8, 3, 6))  # Buscar o índice do valor 8, entre os índices 3 e 6.




# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio, fim, passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'.

lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes.
print(lista[::])  # Iniciando no índice 0 e pegando todos os elementos restantes, pois
# não indiquei nenhum numero inicial, nem final, e nem o passo (lista[nada:nada:nada].

# Trabalhando com slice de lista com o parâmetro 'fim'.
print(lista[:2])  # Começa em 0, pega até o índice 2 não inclusive (2 - 1).
print(lista[:4])  # Começa em 0, pega até o índice 4 não inclusive (4 - 1).
print(lista[1:3])  # Começa em 1, pega até o índice 3 não inclusive (3 - 1).

# Trabalhando com slice de lista com o parâmetro 'fim'.
print(lista[1::2])  # Começa no índice 1, vai até o final, de 2 em 2.
print(lista[::2])  # Começa no índice 0, vai até o final, de 2 em 2.
print(lista[1::-1])  # Começa no índice 1, e conta voltando conforme o passo (1).
print(lista[1:-1])  # Começa no índice 1, vai até o final menos o último índice.
print(lista[:-1])  # Começa no índice 0, vai até o final menos o último índice.
print(lista[::-1])  # Retorna a lista invertida, conforme o passo (1).



# Invertendo valores em uma lista.
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)




# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho*.

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # Soma.
print(max(lista))  # Valor Máximo.
print(min(lista))  # Valor Mínimo.
print(len(lista))  # Tamanho da lista.




# Transformar lista em tupla.
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))




# Desempacotamento de listas.

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou
# variáveis para receber os dados, teremos 'ValueError'.




# Copiando uma lista para outra (Shallow COpy e Deep Copy)
# Forma 1 - Deep Copy:

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta
# a outra. Isso em Python, é chamado de 'Deep Copy' (Cópia Profunda).




# Forma 2 - Shallow Copy:
lista = [1, 2, 3]
print(lista)

nova = lista  # Cópia
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista,
# mas, após realizar modificação em uma das listas, essa modificação refletiu em ambas as listas.
# Isso em Pyhton é chamado 'Shallow Copy'

"""


