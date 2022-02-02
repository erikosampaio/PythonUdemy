"""
1 - Faça um programa que receba dois números e mostre qual deles é o maior.
"""
# print('Informe dois números: ')
# n1 = int(input())
# # n2 = int(input())
# # if n1 > n2:
#     print(n1)
# else:
#     print(n2)
from random import randrange

"""
2 - 
"""
# numero = int(input('Informe um número: '))
# if numero > 0:
#     print(f'{numero ** 0.5}')
# else:
#     print('Número inválido!')

"""
3 - 
"""
# num = float(input('Informe um número: '))
# if num > 0:
#     print(f'{num ** 0.5}')
# else:
#     print(f'{num ** 2}')

"""
4 - 
"""
# num = float(input('Informe um número: '))
# if num > 0:
#     print(f'{num ** 2}')
#     print(f'{num ** 0.5}')
# else:
#     print('Número inválido!')

"""
5 - 
"""
# num = int(input('Informe um número: '))
# if num % 2 == 0:
#     print('Número Par')
# else:
#     print('Número ímpar')

"""
6 - 
"""
# print('Informe dois números: ')
# n1 = int(input())
# n2 = int(input())
# if n1 > n2:
#     print(n1)
#     print(f'{n1 - n2}')
# else:
#     print(n2)
#     print(f'{n2 - n1}')

"""
7 - 
"""
# print('Informe dois números: ')
# n1 = int(input())
# n2 = int(input())
# if n1 > n2:
#     print(n1)
# elif n1 == n2:
#     print('Números iguais!')
# else:
#     print(n2)

"""
8 - 
"""
# print('Informe as duas notas: ')
# n1 = float(input())
# n2 = float(input())
# if 0 <= n1 <= 10 and 0 <= n2 <= 10:
#     med = (n1 + n2) / 2
#     print(med)
# else:
#     print('Nota Inválida!')

"""
9 - 
"""
# print('Salário: R$ ')
# sal = float(input())
# print('Valor empréstimo/mês: R$ ')
# emp = float(input())
# if emp > sal * 0.2:
#     print('Empréstimo não concedido!')
# else:
#     print('Empréstimo concedido!')

"""
10 - 
"""
# print('Informe sua altura: ')
# alt = float(input())
# sexo = int(input('Digite 1 para Masculino e 2 para Feminino: '))
# if sexo == 1:
#     pih = (72.7 * alt) - 58
#     print(f'Peso ideal: {pih}')
# else:
#     pim = (62.1 * alt) - 44.7
#     print(f'Peso ideal: {pim}')

"""
11 -  
"""
# num = int(input('Informe um número: '))
# if num > 0:
#     print(num.split())
#     print(type(num))
# else:
#     print('Número inválido')

"""
12 -  
"""
# num = int(input('Informe um número: '))
# if num < 0:
#     print('Número inválido!')
# else:

"""
13 -  
"""
# print('Informe as 3 notas: ')
# n1 = float(input()) * 1
# n2 = float(input()) * 1
# n3 = float(input()) * 2
# med = (n1 + n2 + n3) / (1 + 1 + 2)
# if med >= 60:
#     print('Aluno aprovado!')
#     print(f'{med}')
# else:
#     print('Aluno reprovado!')
#     print(f'{med}')

"""
14 -  
"""
# print('Informe, respectivamente, sua nota de lab, av. sem. ex. final: ')
# lab = float(input()) * 2
# sem = float(input()) * 3
# exa = float(input()) * 5
# nota_final = (lab + sem + exa) / (2 + 3 + 5)
# if 0 <= nota_final <= 2.9:
#     print('Reprovado!')
# elif 3 <= nota_final <= 4:
#     print('Recuperação!')
# else:
#     print('Aprovado!')
# print(f'{nota_final}')

"""
15 -  
"""
# num = int(input('Informe um número de 1 a 7: '))
# if num == 1:
#     print('Domingo')
# elif num == 2:
#     print('Segunda-feira')
# elif num == 3:
#     print('Terça-feira')
# elif num == 4:
#     print('Quarta-feira')
# elif num == 5:
#     print('Quinta-feira')
# elif num == 6:
#     print('Sexta-feira')
# elif num == 7:
#     print('Sábado')
# else:
#     print('Inválido')

"""
17 -  
"""
# print('Informe os valores, respectivamente, da Bm, bm, altura: ')
# B = float(input())
# b = float(input())
# alt = float(input())
# if B > 0 and b > 0:
#     area = ((B + b) * alt) / 2
#     print(f'{area}')
# else:
#     print('Inválido')

"""
18 -  
"""
# digito = int(input('1 - adição, 2 - subtração \n3 - multiplicação - 4 para divisão:\n'))
# if digito == 1:
#     print('Informe dois valores: ')
#     v1 = int(input())
#     v2 = int(input())
#     print(f'{v1 + v2}')
# elif digito == 2:
#     print('Informe dois valores: ')
#     v1 = int(input())
#     v2 = int(input())
#     print(f'{v1 - v2}')
# elif digito == 3:
# print('Informe dois valores: ')
#     v1 = int(input())
#     v2 = int(input())
#     print(f'{v1 * v2}')
# elif digito == 4:
#     print('Informe dois valores: ')
#     v1 = float(input())
#     v2 = float(input())
#     print(f'{v1 / v2}')
# else:
#     print('Inválido!')

"""
19 -  
"""
# num = int(input('Informe um número: '))
# if num % 3 == 0:
#     if not num % 5 == 0:
#         print('Divisível por 3')
# elif num % 5 == 0:
#     if not num % 3 == 0:
#         print('Divisível por 5')
# elif num % 3 == 0 and num % 5 == 0:
#     print('Número divisível por 3 e 5!')
# else:
#     print('Número não divisível por 3 ou 5')

"""
20 -  
"""
# print('Informe 3 valores: ')
# a = float(input())
# b = float(input())
# c = float(input())
# if a < b + c and b < a + c and c < a + b:
#     if a == b and b == c:
#         print('Triângulo Equilátero!')
#     elif a == b or a == c or b == c:
#         print('Triângulo Isóceles!')
#     if a != b and a != c and b != c:
#         print('Triângulo Escaleno')
# else:
#     print('Não é triângulo!')

"""
21 -  
"""
# print('Informe uma das opções abaixo:\n1 - Soma de 2 números;\n2 - Diferença entre 2 números (maior pelo menor);'
#       '\n3 - Produto entre números;\n4 - Divisão entre 2 números (o denominador não pode ser zero);')
# escolha = int(input())
# if escolha == 1:
#     print('Informe dois números: ')
#     n1 = int(input())
#     n2 = int(input())
#     print(f'{n1 + n2}')
# elif escolha == 2:
#     print('Informe dois números: ')
#     n1 = int(input())
#     n2 = int(input())
#     if n1 > n2:
#         print(f'{n1 - n2}')
#     else:
#         print(f'{n2 - n1}')
# elif escolha == 3:
#     print('Informe dois números: ')
#     n1 = int(input())
#     n2 = int(input())
#     print(f'{n1 * n2}')
# elif escolha == 4:
#     print('Informe dois números: ')
#     n1 = float(input())
#     n2 = float(input())
#     if n2 > 0:
#         print(f'{n1 / n2}')
#     else:
#         print('Denominador não pode ser zero!')
# else:
#     print('Informação inválida!')

"""
22 -  
"""
# print('Informe sua idade e tempo de serviço (em anos):')
# idade = int(input())
# tempo = int(input())
# if idade <= tempo:
#     print('Valor inválido!')
# elif idade >= 65 or tempo >= 30 or idade == 60 and tempo >= 25:
#     print('Pode aposentar!')
# else:
#     print('Não pode aposentar!')

"""
23 -  
"""
# ano = int(input('Informe um ano: '))
# if ano % 400 == 0:
#     print('Ano bissexto!')
# elif ano % 4 == 0 or ano % 100 == 0:
#     print('Ano bissexto!')
# else:
#     print('Ano não é bissexto')

"""
24 -  
"""
# print('Informe o valor do produto em R$: ')
# valor = float(input())
# estado = int(input('Informe o estado, sendo:\n1 - Minas Gerais;\n2 - São Paulo;'
#                    '\n3 - Rio de janeiro;\n4 - Mato Grosso do Sul;\n'))
# if estado == 1:
#     print(valor * 1.07))
# elif estado == 2:
#     print(valor * 1.12))
# elif estado == 3:
#     print(valor * 1.15))
# elif estado == 4:
#     print(valor * 1.08))
# else:
#     print('Erro!')

"""
26 -  
"""
# print('Informe a distância (em Km) e a quantidade de litros de gasolina: ')
# km = int(input())
# dis = int(input())
# con = float(km / dis)
# if con < 8:
#     print('Venda o carro!')
# elif 8 <= con <= 14:
#     print('Econômico!')
# else:
#     print('Super enonômico!')

"""
27 -  
"""
# idade = int(input('Informe a idade do nadador:\n'))
# if 5 <= idade <= 7:
#     print('Infantil A')
# elif 8 <= idade <= 10:
#     print('Infantil B')
# elif 11 <= idade <= 13:
#     print('Juvenil A')
# elif 14 <= idade <= 17:
#     print('Juvenil B')
# elif idade >= 18:
#     print('Sênior')
# else:
#     print('Inválido')

"""
28 -  
"""
# print('Informe 3 números inteiros: ')
# x = int(input())
# y = int(input())
# z = int(input())
# # item = str(input('Digite:\n\na) Geométrica;\nb) Ponderada;\nc) Harmônica;\nd) Aritmética;\n'))
# if item == 'a':
#     print((x*y*z)**(1/3))
# elif item == 'b':
#     print((x+(2*y)+(3*z))/6)
# elif item == 'c':
#     print(1/(x**(-1)+(y**(-1)+(z**-1))))
# elif item == 'd':
#     print((x+y+z)/3)
# else:
#     print('Inválido!')

"""
30 -  
"""
# print('Informe três números: ')
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b > c:
#     print(f'{a}\n{b}\n{c}')
# elif a > c > b:
#     print(f'{a}\n{c}\n{b}')
# elif b > a > c:
#     print(f'{b}\n{a}\n{c}')
# elif b > c > a:
#     print(f'{b}\n{c}\n{a}')
# elif c > a > b:
#     print(f'{c}\n{a}\n{b}')
# else:
#     print(f'{c}\n{b}\n{a}')

