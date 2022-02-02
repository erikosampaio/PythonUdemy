"""
Conjuntos

- Conjuntos em qualquer linguagem de programaçao, estamos fazendo referência à Teoria
dos Conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

 - Sets (conjuntos) não possuem valores duplicados;
 - Sets (conjuntos) não possuem valores ordenados;
 - Elementos não são acessíveis via índice, ou seja, conjuntos não são indexados;


Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1:

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2:

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto.
if 3 in s:
    print('Tem o 3.')
else:
    print('Não tem o 3.')


# Importante lembrar que, em conjunto, além de não termos valores duplicado, não temos ordem.

# Listas aceitam valores duplicados, então temos 10 elementos.
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]  # Ordem permanece.
print(f'Lista: {lista} com {len(lista)} elementos.')

# Tuplas aceitam valores duplicados, então temos 10 elementos.
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34  # Ordem permanece.
print(f'Lista: {tupla} com {len(tupla)} elementos.')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos.
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')  # Ordem permanece.
print(f'Lista: {dicionario} com {len(dicionario)} elementos.')

# Conjutnos não aceitam valores duplicadas, então temos 8 elementos.
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}  # Não permanece na ordem.
print(f'Lista: {conjunto} com {len(conjunto)} elementos.')



# Usos interessantes com sets.

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou
# museu, e os visitantes informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Pyhton, já que em
# uma lista podemos adicionar novos elementos e ter repetição.


# Assim como todo outro conjunto Pyhton, podemos colocar tipos de dados misturados e Sets.

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente.
for valor in s:
    print(valor)


cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:
print(len(set(cidades)))


# Adicionando elementos em um conjunto.
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Remover elemento em um conjunto.
s = {1, 2, 3}
print(s)

# Forma 1 - Caso o valor não seja encontrado, será gerado o erro 'KeyeError'.
s.remove(3)  # NÃO é índice! Informamos o valor a ser removido.
print(s)

# Forma 2 - Não gera nenhum 'error' se valor não for encontrado. Nenhum valor é retornado.
s.discard(2)
print(s)



# Copiando um conjunto para outro...

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy.
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)


# Forma 2 - Shallow Copy.
novo = s
print(novo)
novo.add(4)
print(novo)
print(s)



s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto.
s.clear()
print(s)




# Métodos matemáticos de Conjuntos.

# Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}


# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union.

unicos1 = estudantes_python.union(estudantes_java)
# {'Patrícia', 'Ana', 'Ellen', 'Gustavo', 'Marcos', 'Pedro', 'Guilherme', 'Fernando', 'Julia'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Ana', 'Ellen', 'Julia', 'Guilherme', 'Marcos', 'Gustavo', 'Fernando', 'Pedro', 'Patrícia'}
print(unicos1)


# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)



# Veja que alguns alundos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1  - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)


# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)



# Gerar um conjunto de estudantes que não estão no outro.

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho.
# * Se os valores forem todos inteiros ou reais.

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""


