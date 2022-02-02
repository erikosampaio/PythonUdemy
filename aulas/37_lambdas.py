"""
Utilizando Lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambda, são funções sem nome, ou seja,
funções anônimas.

# Função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda:
lambda x: 3 * x + 1

# E como utilizar a expressão Lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))


# Podemos ter expressões Lambdas com múltiplas entradas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY', ' jones '))


# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também.

amar = lambda: 'Como não amar Pyhton'

uma = lambda x: 2 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)


print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS 1: Se passarmos mais argumentos do que parâmetros esperados teremos #TypeError.
# OBS 2: Se declararmos mais parâmetros do que argumentos teremos #TypeError.


# Outro exemplo

autores = [
            'Isaac Newton',
            'Ray Bradbury',
            'Robert Heinlein',
            'Arthur C. Clarke',
            'Frank Herbert',
            'Orson Card',
            'Douglas Adams',
            'H. G. Wells',
            'Leigh Brackett'
            ]

print(autores)


autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())  # Ordenando de maneira alfabética pelo sobrenome.
print(autores)



# Função Quadrática
# f(x) = a * x ** 2 + b * x + c  # a, b, c são valores que recebemos para poder achar o valor de x.

# Definindo a função:


def geradora_funcao_quadratica(a, b, c):
    'Retorna a função f(x) = a * x ** 2 + b * x + c'
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# Ou
print(geradora_funcao_quadratica(3, 0, 1)(2))  # Onde dois é o valor de x em Lambda.
"""


def reverse_words_order_and_swap_cases(sentence):
    for i in range(len(sentence)):
        if sentence[i] == sentence[i].lower:
            sentence[i] = sentence[i].upper()
        else:
            sentence[i] = sentence[i].lower()
        sentence = sentence.split(' ')
    return sentence[::-1]


sentence = input('nome: ')
print(reverse_words_order_and_swap_cases(sentence))
