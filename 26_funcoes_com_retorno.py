"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é 'None'.

OBS: Funções Pyhton que retornam valores, devem retornar estes valores com a
palavra reservada 'return'.

OBS: Não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções.

# Vamor refatorar essa função para que ela retorne o valor:
# Refatorar é melhorar código sem alterar sua representação externa.

# Antes de refatorar
# def quadrado_de_7():
#     print(7*7)
# ret = quadrado_de_7()
# print(f'Retorno {ret}')


# Refatorando
def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f'Retorno {ret}')
# O de cima é igual ao abaixo.
print(f'Retorno: {quadrado_de_7()}')


# Refatorando a primeira função:

# Antes
def diz_oi():
    print('oi!')

# Refatorando:
def diz_oi():
    return 'Oi '  # A vantagem de usar o return é a flexibilidade de manuseio do código.

alguem = 'Pedro!'

print(diz_oi())
print(alguem)

OBS: Sobre a palavra reservada return.


# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')


print(diz_oi())


# Exemplo 2 - Podemos ter, em uma função, diferentes returns;

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores;

def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(type(outra_funcao()))
print(outra_funcao())

# Vamos criar uma função para jogar a moeda;

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1;
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


# Erros comuns na utilização do retorno de uma função, que na verdade nem é erro, mas sim codificação desnecessária.

#ERRADO
def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    else:
        return False

#CORRETO
def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
"""
