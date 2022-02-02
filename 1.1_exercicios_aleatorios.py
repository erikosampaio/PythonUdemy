"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.

mbarato = str('')
pbarato = 100000
m1000 = 0
digito = str('')
con = 0
while digito != 'n':
    nome = str(input('Informe o nome do produto: '))
    preco = int(input('Informe o preço do produto: '))
    con += preco
    if preco > 1000:
        m1000 += 1
    if preco < pbarato:
        pbarato = preco
        mbarato = nome
    digito = str(input('Deseja continuar s/n: ')).lower()
print(f'Valor total das compras: R$ {con}')
print(f'Quantos produtos custam mais de R$ 1000: {m1000}')
print(f'Nome do produto mais barato: {mbarato}')
"""


"""
Exercício Python 071: Crie um programa que simule o funcionamento
de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print(f'{"BANCO PYTHON":=^30}')
print('=' * 30)
valor = int(input('Informe o valor do saque: '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
"""

"""
maior = 0
n = int(input("Informe um número, sendo '0' para encerrar: "))
while n != 0:
    n = int(input("Informe um número, sendo '0' para encerrar: "))
    if n > maior:
        maior = n
print(f'Maior número lido: {maior}')
"""

"""
for n in range(1, 101):
    if n % 10 == 0 and n > 10:
        print(f'{n} - Múltiplo de 10')
"""

"""
for n in range(100, 201):
    if n % 2 == 1:
        print(n)
"""

"""
maior = 0
menor = 100000
soma = 0
for n in range(10):
    num = int(input('Informe um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
media = soma / 10
print(maior)
print(menor)
print(media)
"""

"""
nome = input('Informe o nome de usuário: ')
senha = input('Informe a senha de usuário: ')
while nome == senha:
    print('Sua senha não pode ser a mesma do nome de usuário:')
    nome = input('Informe o nome de usuário: ')
    senha = input('Informe o nome de usuário: ')
print('Logado!')
"""

"""
num = int(input('Informe o número do qual deseja ver a tabudada: '))
print(f'Tabuada de {num}:')
for n in range(1, 11):
    print(f'{num} x {n} = {num * n}')
"""

"""
print('\033[31m=\033[m' * 30)
print(f'\033[33m{"LEVANTAMENTO MOUSES":^30}\033[m')
print('\033[31m=\033[m' * 30)
con = 0
n_esfera = 0
n_limpeza = 0
n_troca_cabo_conector = 0
quebrado = 0
ide = int(input("Informe o número de identificação. Digite '0' para finalizar: "))
while ide != 0:
    print('Identifique o tipo de defeito, sendo:\n1 - Necessita da esfera.'
    '\n2 -'' Necessita de limpeza.\n3 - Necessita de troca'          
    'de cabo ou conector.\n4 - Quebrado ou inutilizado.')
    sit = int(input('Opção: '))
    while 0 < sit > 4:
        sit = int(input('Informe uma opção válida: '))
    if sit == 1:
        n_esfera += 1
    elif sit == 2:
        n_limpeza += 1
    elif sit == 3:
        n_troca_cabo_conector += 1
    else:
        quebrado += 1
    con += 1
    ide = int(input("Informe o número de identificação. Digite '0' para finalizar: "))
if con > 0:
    p_esfera = n_esfera / con * 100
    p_limpeza = n_limpeza / con * 100
    p_troca = n_troca_cabo_conector / con * 100
    p_quebrado = quebrado / con * 100
    print(f'Quantidade de mouses: {con}.')
    print(f'\033[32mSituação                                           Quantidade                     Percentual\033[m  ')
    print(f'1 - Necessita da esfera                                {n_esfera}                            {p_esfera:.2f}%  ')
    print(f'2 - Necessita de limpeza                               {n_limpeza}                            {p_limpeza:.2f}% ')
    print(f'3 - Necessita de troca de cabo ou conector             {n_troca_cabo_conector}                            {p_troca:.2f}%   ')
    print(f'4 - Quebrado ou inutilizado                            {quebrado}                            {p_quebrado:.2f}%')
else:
    print('Programa finalizado!')

"""

"""
print('Informe 4 números: ')
n1 = int(input('1º: '))
n2 = int(input('2º: '))
n3 = int(input('3º: '))
n4 = int(input('4º: '))
q3 = n3 ** 2
if q3 >= 1000:
    print(f'Quadrado de {n3} = {q3}')
else:
    q1 = n1 ** 2
    q2 = n2 ** 2
    q4 = n4 ** 2
    print(f'1º valor lido: {n1}. Seu quadrado = {q1}')
    print(f'1º valor lido: {n2}. Seu quadrado = {q2}')
    print(f'1º valor lido: {n3}. Seu quadrado = {q3}')
    print(f'1º valor lido: {n4}. Seu quadrado = {q4}')
"""

"""
num = int(input('Informe um número: '))
if num < 0 and num != 0:
    print('Número negativo!')
elif num == 0:
    print('Número neutro!')
else:
    print('Número positivo!')
if num % 2 == 0:
    print('Número par!')
else:
    print('Número ímpar!')
"""


"""
1 -
"""
# num1 = int(input('Informe o primeiro número: '))
# num2 = int(input('Informe o segundo número: '))
# soma = num1 + num2
# multiplicacao = soma * num1
# print(f'Resultado da multiplicação é: {multiplicacao}')

"""
2 -
"""
# qmin = int(input('Informe a quantidade mínima: '))
# qmax = int(input('Informe a quantidade máxima: '))
# medio = (qmin + qmax) / 2
# print('O estoque médio é {0}'.format(medio))

"""
3 -
"""
# m = int(input('Informe o valor em metros: '))
# cm = m / 100
# print('{0} metros em cm é: {1}'.format(cm, m))

"""
4 -
"""
# valor_hora = float(input('Informe qual seu ganho por hora: '))
# horas = int(input('Informe o número de horas trabalhadas: '))
# salario = valor_hora * horas
# print('Seu salário no mês é R$: {0:.2f}'.format(salario))

"""
5 -
"""
# alt = float(input('Qual sua altura: '))
# peso_ideal = (72.3 * alt) - 58
# print('Seu peso ideal é {0:.2f}'.format(peso_ideal))

"""
6 -
"""
# n = int(input('Informe um número: '))
# if n > 100:
#     print(n)
# else:
#     n = 0
#     print(n)

"""
7 -
"""
# num = int(input('Informe um número: '))
# if num > 0:
#     a = num
#     print('Valor positivo.')
# else:
#     b = num
#     print('Valor negativo.')
# print(num)

"""
8 -
"""
# p = 0
# i = 0
# num = int(input('Infome um número: '))
# if num % 2 == 0:
#     p = num
#     print("Número par.")
# else:
#     i = num
# print(p)
# print(i)

"""
9 -
"""
# alt = float(input('Informe sua altura: '))
# sexo = (input('Informe seu sexo m/f: '))
# if sexo.lower() == 'm':
#     peso_ideal = (72.7 * alt) - 58
# elif sexo.lower() == 'f':
#     peso_ideal = (62.1 * alt) - 44.7
# else:
#     peso_ideal = 0
#     print('Sexo não reconhecido.')
# print('Peso ideal é: {0:.2f}'.format(peso_ideal))

"""
10 -
"""
# p = float(input('Informe o peso dos peixes: '))
# if p > 50:
#     m = (p - 50) * 4.00
#     e = 'excesso'
#     print('Você deverá pagar R$ {0:.2f}'.format(m))
# else:
#     m = 0
#     e = 0
#     print('Multas: {0}'.format(m))
#     print('Excesso: {0}'.format(e))

"""
11 -
"""
# valor_hora = 10.00
# valor_hora_execedente = 20.00
# e = 0
# c = int(input('Informe o código: '))
# n = float(input('Informe o número de horas trabalhadas: '))
# if n > 50:
#     e = (n - 50) * valor_hora_execedente
#     salario = (50 * valor_hora) + e
#     print('Salário total R$ {0:.2f}'.format(salario))
#     print('Salário excedente R$ {0:.2f}'.format(e))
# else:
#     salario = (n * valor_hora)
#     print('Salário total R$ {0:.2f}'.format(salario))
#     print('Salário excedente R$ {0:.2f}'.format(e))

"""
12 -
"""
# alt = float(input('Informe sua altura: '))
# peso = float(input('Informe seu peso: '))
# imc = peso / (alt ** 2)
# if imc < 18.5:
#     print('IMC: {0:.2f}'.format(imc))
#     print('Abaixo do peso!')
# elif 18.6 <= imc <= 24.9:
#     print('IMC: {0:.2f}'.format(imc))
#     print('Saudável!')
# elif 25 <= imc <= 29.9:
#     print('IMC: {0:.2f}'.format(imc))
#     print('Peso em excesso!')
# elif 30 <= imc <= 34.9:
#     print('IMC: {0:.2f}'.format(imc))
#     print('Obesidade grau I!')
# elif 35 <= imc <= 39.9:
#     print('IMC: {0:.2f}'.format(imc))
#     print('Obesidade grau II (severa!')
# else:
#     print('IMC: {0:.2f}'.format(imc))
#     print('Obesidade grau III (mórbida)!')

"""
13 - 
"""
# indice = float(input('Informe o Índice de poluição: '))
# if 0.3 <= indice < 0.4:
#     print('Grupo 1: Intimação para suspensão de atividades!')
# elif 0.4 <= indice < 0.5:
#     print('Grupo 1 e 2: Intimação para suspensão de atividades!')
# elif indice >= 0.5:
#     print('Suspensão total das atividades!')
# else:
#     print('Níves aceitáveis.')

"""
13 - 
"""
# for i in range(1, 101):
#     print(i)
#     if i % 10 == 0:
#        print('Múltiplo de 10!')
#

"""
14 - 
"""
# for i in range(100, 201):
#     if i % 2 != 0:
#         print(i)

"""
15 - 
"""
# maior = -999
# menor = 999
# soma = 0
# for i in range(1, 11):
#     valor = int(input("Informe um valor: "))
#     if valor > 0:
#         if valor > maior:
#             maior = valor
#         if valor < menor:
#             menor = valor
#         soma = soma + valor
#     else:
#         valor = int(input("Informe um valor: "))
# media = soma / 10
# print(f'O maior número é: {maior}')
# print(f'O menor número é: {menor}')
# print(f'A média dos números é: {media}')

"""
16 - 
"""
# nome = input("Informe o nome de usuário: ")
# senha = (input("Informe senha: "))
# while senha == nome:
#     print("ERRO. Informe uma senha difente do nome de usuário.\n")
#     nome = input("Informe o nome de usuário: ")
#     senha = (input("Informe senha: "))

"""
17 - 
"""
# numero = int(input("Informe um número: "))
# while numero < 1 or numero > 10:
#     print("Informe um número: ")
# for n in range(1, 11):
#     print('{0} * {1} = {2}'.format(numero, n, (numero * n)))
