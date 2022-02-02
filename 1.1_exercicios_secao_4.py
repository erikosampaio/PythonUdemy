"""
1 - Faça um programa que leia um número inteiro e o imprima.
"""
# inteiro = input('Informe um número inteiro: ')
# print(f'O valor inteiro informado é: {inteiro}')

"""
2 - Faça um programa que leia um número inteiro real e o imprima.
"""
# real = float(input('Informe um número inteiro: '))
# print(f'O valor inteiro informado é: {real}')

"""
3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
"""
# print('Informe 3 valores inteiros: ')
# v1 = int(input())
# v2 = int(input())
# v3 = int(input())
# vtotal = v1 + v2 + v3
# print(f'O resultado da soma dos valores {v1}, {v2} e {v3} é: {vtotal}!')

"""
4 - Leia um número real e imprima o resultado do quadrado desse número.
"""
# real1 = float(input('Informe um número real: '))
# quadrado = (real ** 2)
# print(f'O valor quadrado do número {real} é: {quadrado}!')

"""
5 - Leia um número real e imprima a quinta parte deste número.
"""
# real2 = float(input('Informe um número real: '))
# v5 = float(real2 / 5)
# print(f'A quinta parte do número {real2} é: {v5}!')

"""
6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura Fahrenheit e C a Celsius.
"""
# c = float(input('Informe um valor de temperatura conforme a escala Celsius: '))
# f = float(c*(9.0/5.0)+32)
# print(f'A temperatura informada após conversão para Fahrenheit é: {f}!')

"""
7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0*(F - 32.0)/9, sendo C a temperatura Celsius e F a Fahrenheit.
"""
# f = float(input('Informe um valor de temperatura conforme a escala Fahrenheit: '))
# c = float(5.0*(f - 32.0)/9)
# print(f'A temperatura informada após conversão para Celsius é: {c}!')

"""
8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = K - 273,15, sendo C a temperatura Celsius e K a Kelvin.
"""
# k = float(input('Informe um valor de temperatura conforme a escala Kelvin: '))
# c = float(k - 273.15)
# print(f'A temperatura informada após conversão para Celsius é: {c}')

"""
9 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: C = K + 273,15, sendo C a temperatura Celsius e K a Kelvin.
"""
# c = float(input('Informe um valor de temperatura conforme a escala Celsius: '))
# k = float(c + 273.15)
# print(f'A temperatura informada após conversão para Kelvin é: {k}')

"""
10 - Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).
A fórmula de conversão é: M = K/3,6, sendo K a velocidade em km/h e M em m/s.
"""
# km = float(input('Informe um valor de velocidade conforme a escala Km/h: '))
# ms = float(km/3.6)
# print(f'A velocidade informada após conversão para m/s é: {ms}!')

"""
11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
A fórmula de conversão é: K = M*3.6, sendo K a velocidade em km/h e M em m/s.
"""
# ms = float(input('Informe um valor de velocidade conforme a escala m/s: '))
# km = float(ms*3.6)
# print(f'A velocidade informada após conversão para m/s é: {km}!')

"""
12 - Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1,61 * M,
sendo K a distância em quilômetros e M e milhas.
"""
# m = float(input('Informe um valor de distância conforme a escala milhas: '))
# k = float(1.61*m)
# print(f'A distância informada após conversão para quilômetros é: {k}')

"""
28 - Faça uma leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""
# print('Informe três valores: ')
# v1 = int(input())
# v2 = int(input())
# v3 = int(input())
# q1 = v1 ** 2
# q2 = v1 ** 2
# q3 = v1 ** 2
# sq = q1 + q2 + q3
# print(f'O resultado da somas dos quadrados dos valores informados é: {sq}')

"""
29 - Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
# print('Informe as 4 notas: ')
# n1 = float(input())
# n2 = float(input())
# n3 = float(input())
# n4 = float(input())
# sn = n1 + n2 + n3 + n4
# mn = sn/4
# print(f'A média aritmética das notas informadas é: {mn}')

"""
30 - Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""
# real = float(input('Informe um valor em R$: '))
# dolar = float(5.20)
# con = float(real/5.20)
# print(f'O valor em dólares após conversão é: $ {con}')

"""
31 - Leia um número inteiro e imprima o seu antecessor e o sucessor.
"""
# numero = int(input('Informe um número: '))
# nmenos = numero - 1
# nmais = numero + 1
# print(f'Antecessor do número {numero}: {nmenos}. Sucessor: {nmais}!')

"""
32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""
# numero = int(input('Informa um número: '))
# triplo = numero * 3
# dobro = numero * 2
# suctriplo = triplo + 1
# antdobro = dobro - 1
# soma = suctriplo + antdobro
# print(f'O resultado da soma do sucessor do triplo do número informado com o antecessor do seu dobro é: {soma}')

"""
33 - Leia o tamanho do lado de um quadrado e imprima com resultado a sua área.
"""
# lado = float(input('Informe o tamanho de um lado do quadrado: '))
# area = lado ** 2
# print(f'A área do quadrado a partir do tamanho informado é: {area}!')

"""
34 - Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do círculo é pi*raio². Considere pi = 3,141592.
"""
# raio = float(input('Informe o valor do raio do círculo: '))
# pi = 3.141592
# area = pi * raio ** 2
# print(f'O valor da área do raio informado é: {area}!')

"""
35 - Sejam 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = (a² + b²)^2.
"""
# print('Informe dois valores para a e b: ')
# a = float(input())
# b = float(input())
# hip = ((a ** 2) + (b ** 2))*0.5
# print(f'O valor da hipotenusa dos valores informados é: {hip}')

# num = input('Informe um número: ')
# raiz = float(num) ** 0.5
# print(f'A raiz quadrada de {num} é {raiz}')


"""
37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto,
tendo em vista que o desconto foi de 12%.
"""
# valor1 = int(input('Informe o valor do produto: R$ '))
# desc = (valor1 * 12) // 100
# valor2 = valor1 - desc
# print(f'Valor do produto após desconto de 12%: R$ {valor2}')

"""
38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""
# sal1 = int(input('Informe seu salário atual: R$ '))
# aumento = (sal1 * 25) // 100
# sal2 = sal1 + aumento
# print(f'Seu novo salário após o aumento de de 25% é: R$ {sal2}')

"""
39 - A importância de R$ 780.000,00 será dividida entre três
ganhadores de um concurso, sendo que da quantia total:
- O primeiro ganhador receberá 46%;
- O segundo ganhador receberá 32%;
- O terceiro ganhador receberá o restante;

Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

# premio = 780000
# print(f'O valor do prêmio é de: R$ {premio}')
# g1 = premio * 0.46
# g2 = premio * 0.32
# g3 = premio - g1 - g2
# print(f'O primeiro ganhador receberá a quantia de R$ {g1}. \nO segundo ganhador receberá a quantia de R$ {g2}.'
#       f' \nO terceiro ganhador receberá a quantia de R$ {g3}.')

"""
40 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número
de dias trabalahdos pelo encanador e imprima a quantia líquida que deverá ser pega, sabedo-se que
são descontados 8% para imposto de renda.
"""
# dias = int(input('Informe a quantidade de dias trabalhados: '))
# sal1 = dias * 30
# ir = sal1 * 8 // 100
# sal2 = sal1 - ir
# print(f'Valor bruto: R$ {sal1},00')
# print(f'Valor líquido a receber: R$ {sal2},00')
# print(f'Desconto IRRF: R$ {ir},00')

"""
41 - Faça um programa que leia o valor da hora de trabalhado (em reais) e número de horas trabalhadas
no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""
# vht = float(input('Informe o valor da hora de trabalho em R$: '))
# nht = float(input('Informe o número de horas trabalhadas no mês: '))
# valor1 = (vht * nht) * 1.08  # forma mais exemplificativa (1 + 0.08)
# print(f'Valor a receber: R$ {valor1}')


"""
43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- O total a pagar com desconto de 10%.
- O valor de cada parcela, no parcelamento de 3x sem juros.
- A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto).
- A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).
"""

"""
51 - Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0). 
"""
# print('Informe as coordenadas de x e y: ')
# x = float(input())
# y = float(input())
# r2 = ((x * x) + (y * y)) ** 0.5
# print(r2)

"""
52 - Aposta de três amigos para ganhar proporcionalmente o valor do prêmio. 
"""
# premio = float(input('Valor do prêmio: R$ '))
# j1 = float(input('Valor investido Jogador 1: R$ '))
# j2 = float(input('Valor investido Jogador 2: R$ '))
# j3 = float(input('Valor investido Jogador 3: R$ '))
# aposta = j1 + j2 + j3
# vj1 = premio * (j1 / aposta)
# vj2 = premio * (j2 / aposta)
# vj3 = premio * (j3 / aposta)
# print(vj1)
# print(vj2)
# print(vj3)
