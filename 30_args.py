"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com *(asterisco).

*xis

Mas por convenção, utilizamos *args para definí-lo.

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então, desde
já, lembre-se que tuplas são imutáveis.


# Exemplos - Como fica limitado sem o *args

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))
# print(soma_todos_numeros(4, 6))  # TypeError. Faltou passar um valor
# print(soma_todos_numeros(4, 6, 9, 5)) TypeError. Foi passado um valor a mais.


# Entendendo o *args

def soma_todos_numeros(nome, sobrenome, *args):
    print(f'nome: {nome}')
    print(f'nome: {sobrenome}')
    print(f'nome: {args}')
    return f'Soma dos args: {sum(args)}\n'


print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de quem você é!'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""

"""
def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
# num1, num2, num3, num4, num5, num6, num7 = numeros
# print(soma_todos_numeros(numeros, 4, 5, 6))  # TypeError. Não é possível passar lista, pois args é tupla.
print(soma_todos_numeros(*numeros))
# OBS: O asterisco (*) serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará desempacotar estes dados.
"""


def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
# num1, num2, num3, num4, num5, num6, num7 = numeros
