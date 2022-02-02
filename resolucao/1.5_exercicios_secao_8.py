"""
1 - Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.

def dobro(numero):
    return numero*2


num = int(input("Informe um número: "))

print(dobro(num))
"""

"""
2 -  Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na
tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro
de 2000.

"""

"""

# Primeiro modo (pesquisado)
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')


def retorna_data_extenso(data_string):
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de data inválida. Data deve ser DD/MM/AAAA.")
    else:
        data_datetime = datetime.strptime(data_string, '%d/%m/%Y')
        return datetime.strftime(data_datetime, '%d de %B de %Y')

    # dia = datetime.strftime(data_datetime, '%d')
    # mes = datetime.strftime(data_datetime, '%B')
    # ano = datetime.strftime(data_datetime, '%Y')
    # return dia + " de " mes[0].upper() + mes[1:] + " de " ano
    # return dia + " de " mes.capitalize() + " de " ano


data = input("Informe uma data: ")
data_extenso = retorna_data_extenso(data)

if data_extenso is not None:
    print(data_extenso)
    
# Segundo modo

mes_tupla = ('janeiro', 'fevereiro', 'março',
             'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro'
             )


def retorna_data_extenso(d, m, a):
    while True:
        if d < 29 and m == 2:
            if 0 < d <= 31 and 0 < m <= len(mes_tupla):
                break
            break
        else:
            print("Digite uma data válida!")
            d = int(input("Dia: "))
            m = int(input("Mês: "))
            a = int(input("Ano: "))
    return f'{d} de {mes_tupla[m-1]} de {a}'


print("Informe uma data.")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))


print(retorna_data_extenso(dia, mes, ano))
"""

"""
3 - Faça uma função para verificar se um número é positivo ou negativo. Sendo que o
valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual

def verifica_numero(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


num = int(input("Informe um número: "))
print(verifica_numero(num))

"""

"""
4 - Faça uma função para verificar se um número é um quadrado perfeito. Um quadradro perfeito
é um número inteiro não negativo que pode ser expresso como o quadrado de outro número. Ex: 1, 4, 9...

def numero_perfeito(numero):
    for i in range(1, numero+1):
        if numero ** 0.5 == i:
            return f'{numero} é um quadrado perfeito!'
    return f'{numero} não é quadrado perfeito!'


num = int(input("Informe um número: "))
print(numero_perfeito(num))
"""

"""
5 - Faça uma função e um programa de teste para o cálculo do volume de uma esfera
Sendo que o raio é passado por parâmetro.

V = 4/3 * PI * R³


pi = 3.141592


def volume_esfera(r):
    valor = 4 / 3 * pi * r ** 3
    return valor


raio = float(input("Informe o valor do raio: "))
print(volume_esfera(raio))
"""

"""
6 - Faça uma função que receba 3 números inteiros como parâmetro, representando
horas, minutos e segundos, e os converta em segundos.


def converte_segundos(h, m, s):
    h = h * 60 * 60
    m = m * 60
    total = h + m + s
    return total

hora = int(input("Informe a quantidade de horas: "))
minuto = int(input("Informe a quantidade de minutos: "))
segundo = int(input("Informe a quantidade de segundos: "))

print(converte_segundos(hora, minuto, segundo))
"""

"""
7 - Faça uma função que receba uma temperatura em graus Celsius e retorne-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0 / 5.0) +
32.0, sendo F a temperatura em Farhrenheit e C a temperatura em Celsius.


def converte_temperatura(valor_celsius):
    valor_fahrenheit = valor_celsius * (9.0 / 5.0) + 32.0
    return valor_fahrenheit

celsius = float(input("Informe uma temperatura em graus Celsius: "))
farhrenheit = converte_temperatura(celsius)

print(f'Valor em Fahrenheit = {fahrenheit}')
"""

"""
8 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela
equação: hipotenusa = raiz de a² + b². Faça uma função que receba os valores de
 a e b e calcule o valor da hipotenusa através da equação.

def hipotenusa(a, b):
    return (a*2 + b2) * 0.5

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))

print(f'Valor da hipotenusa = {hipotenusa(a, b):.2f}')
"""

"""
9 - Faça uma função que receba a altura e o raio de um cilindro circular e
retorne o volume do cilindro. O volume de um cilindro circular é calculado por
meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.141592.


pi = 3.14

def volume_cilindro_circular(a, r):
    vol = pi * (r**2) * a
    return f'Valor do volume do cilindro circular = {vol:.2f}cm³'


altura = float(input("Informe a altura do cilindro em cm: "))
raio = float(input("Informe o raio do cilindro em cm: "))

print(volume_cilindro_circular(altura, raio))
"""

"""
10 - Faça uma função que receba dois números e retorne qual deles é o maior.

def maior(a, b):
    if a == b:
        return "Números iguais."
    elif a > b:
        return a
    return b


num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o primeiro número: "))

print(maior(num1, num2))
"""

"""
11 - Elabora um função que receba três notas de um aluno como parâmetros e
uma letra. Se a letra for A, a função deverá calcular a média aritmética das
notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 3, 2.

def nota_media(n1, n2, n3, l):
    if l == 'A':
        return f'Média Aritmética = {(n1 + n2 + n3) / 3:.2f}'
    if l == 'P':
        return f'Média Ponderada = {(n1*5 + n2*3 + n3*2) / (5+3+2):.2f}'
    return 'Letra inválida. Média não calculada!'


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
letra = input("Informe a letra (A/P): ").upper()

print(nota_media(nota1, nota2, nota3, letra))
"""

"""
12 - Escreva um função que receba um número inteiro maior que zero e retorne a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o
valor 8 (2 + 5 + 1). Se o número lido não for maior que zero, o programa termina-
rá com a  mensagem "Número inválido".

def retorna_soma_algarismos(num):
    num = str(num)
    soma = 0
    for i in num:
        soma += int(i)
    return soma
    
    

numero = int(input("Informe um número: "))
if numero > 0:
    print(retorna_soma_algarismos(numero))
else:
    print("Número inválido!")
"""

"""
13 - Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará
a operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma adição,
se for - uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.

def retorna_operacao(n1, n2, s):
    if s == '+':
        return n1 + n2
    elif s == '-':
        return n1 - n2
    elif s == 'x' or s == '*':
        return n1 * n2
    elif s == '/':
        if n2 == 0:
            return 'Divisão por 0.'
        return n1 / n2
    return 'Símbolo inválido!'


num1 = int(input("Informe um número: "))
num2 = int(input("Informe um número: "))
simbolo = input("Digite: +, -, x ou /: ")

print(retorna_operacao(num1, num2, simbolo))
"""

"""
14 - Faça um função que receba a distância em Km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO         Km/l            Mensagem
menor que        8           Venda o carro!
entre          8 e 14        Econômico!
maior que        12          Super econômico!

def condicao_carro(d, l):
    if d / l < 8:
        return 'Venda o carro!'
    elif d / l >= 8:
        return 'Econômico!'
    elif d / l > 8:
        return 'Super econômico!'
    return 'Valor inválido!'


d_km = int(input("Informe a distância em km: "))
litro = int(input("Informe a quantidade de litros consumidos: "))

print(condicao_carro(d_km, litro))
"""

"""
15 - Crie um programa que receba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:
a) Determinar se esses lados formam um triângulo, sabendo que:
    - O comprimento de cada lado de um triângulo é menor do que a soma do outros dois lados.

b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo, sendo que:
    - Chama-se equilátero o triângulo que tem três lados iguais.
    - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.  

resultado = ''


def verifica_se_triangulo(a, b, c):
    global resultado
    if a >= b + c or b >= a + c or c >= a + b:
        return 'Valores informados não correspondem a um triângulo!'
    resultado = 'valido'
    return 'processando tipo do triângulo ...'


def tipo_triangulo(a, b, c):
    if a == b and a == c and b == c:
        return 'Triângulo equilátero!'
    elif a == b or a == c or b == c:
        return 'Triângulo isóceles!'
    return 'Triângulo escaleno!'


l1 = 0
l2 = 0
l3 = 0
while True:
    l1 = float(input(f"Informe o valor do 1º lado: "))
    l2 = float(input(f"Informe o valor do 2º lado: "))
    l3 = float(input(f"Informe o valor do 3º lado: "))
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        print("Informe lados superiores a 0!")
    else:
        break
print(verifica_se_triangulo(l1, l2, l3))
if resultado == 'ok':
    print(tipo_triangulo(l1, l2, l3))
"""

"""
16 - Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando vários símbolos de igual
(EX: =======). A função recebe por parãmetro quantos sinais de igual serão mostrados.

def DesenhaLinha(quantidade):
    for i in range(1, quantidade+1):
        print('=', end='')


qtd = int(input("Informe a quantidade de traços a serem desenhadas: "))
DesenhaLinha(qtd)
"""

"""
17 - Faça uma questão que receba dois números inteiros positivos por parâmetro e retorne a
soma dos N números inteiros existentes entre eles:

def soma_entre_numeros(a, b):
    soma = 0
    if a <= 0 or b <= 0:
        return 'Válido somente valores positivos e inteiros'
    elif a == b:
        return 'Números iguais.'
    elif a > b:
        for i in range(b+1, a):
            soma += i
        return soma
    else:
        for i in range(a+1, b):
            soma += i
        return soma


num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

print(soma_entre_numeros(num1, num2))
"""

"""
18 - Faça uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o resultado de X^Z para
o programa principal. Atenção. Não utilize nenhuma função pronta de exponenciação.

def exponencial(x, z):
    return x**z


n1 = int(input("1º Valor: "))
n2 = int(input("2º Valor: "))

print(exponencial(n1, n2))
"""

"""
19 - Faça uma função que retorne o maior fator primo de um número.


def maior_fator(n):
    primo = 0
    for i in range(1, n+1):
        con = 0
        for x in range(1, i+1):
            if i % x == 0:
                con += 1
        if con == 2 and i < n and n % i == 0:
            primo = i
    if primo > 0:
        return primo
    return 'Número não possui fator primo!'


num = int(input("Informe um número: "))
print(f'Maior fator primo = {maior_fator(num)}')
"""

"""
20 - Faça um algoritmo que receba um número positivo n e calcule o seu fatorial, n!.

def fatorial(n):
    fat = n
    n1 = n
    while n > 1:
        fat = fat * (n-1)
        n -= 1
    return f'Fatorial de {n1} = {fat}.'


num = int(input("Informe um número: "))
print(fatorial(num))
"""

"""
21 - Escreva uma função para determinar a quantidade de números primos abaixo de N.


def primos_ate_numero(numero):
    soma = 0
    for i in range(1, numero):
        con = 0
        for x in range(1, i + 1):
            if i % x == 0:
                con += 1
        if con == 2:
            print(i)
            soma += 1
    return f'Quantidade de primos até {numero} = {soma}'


num = int(input("Informe um número: "))
print(primos_ate_numero(num))
"""

"""
22 - Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos
de exclamação, conforme o exemplo abaixo (para n = 5):

!
!!
!!!
!!!!
!!!!!

def numero_linhas(quantidade):
    a = '!'
    for i in range(1, quantidade+1):
        print(a)
        a += '!'
    return None


n = int(input("Informe a quantidade de linhas que deseja imprimir: "))
numero_linhas(n)
"""

"""
23 - Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura.
Por exemplo, a saída para n = 4 seria:


             *
             **
             ***
             ****
             ***
             **
             *


def triangulo_lateral(n):
    a = []
    i = 0
    while i < n:
        a.append('*')
        print(a)
        i += 1

    while i < 2 * n - 1:
        a.remove('*')
        print(a)
        i += 1


triangulo_lateral(4)
"""

"""
24 - Escreva um programa que gera um triângulo de altura e lados n e base 2*n-1.
Por exemplo, a saída para n = 6 seira:


                *
               ***
              *****
             *******
            *********
           ***********
           
"""

"""
25 - Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado
da seguinte série:
S = 2/4 + 5/5 + 10/6 + ... (N² + 1) / (N + 3)

def calcula_serie(n):
    s = 0
    x = 0
    for i in range(1, n+1):

    return s


num = int(input("Informe um número: "))
print(calcula_serie(num))

"""

"""
26 - Faça um algoritmo que receba um número inteiro positivo
n e calcule o somátorio de 1 até n.

def somatorio_ate_numero(numero):
    soma = 0
    for i in range(1, numero+1):
        soma += i
    return soma


n = int(input("Informe um número: "))
print(somatorio_ate_numero(n))
"""

"""
27 - Faça uma função que receba como parâmetro o valor de um ângulo em graus e
calcule o valor do seno desse ângulo usando sua respectiva série de Taylor:
"""

"""
31 - Faça uma função para calcular o número neperiano usando uma série. A função deve ter como
parâmetro o número de termos que serão somados (note que, quanto maior o número, mais próxima
a resposta estará do valor e).

e = 1/n! = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ...

import math

def neperiano(n):
    e = 0
    fat = 0
    for i in range(0, n+1):
        e += 1 / math.factorial(fat)
        fat += 1
    return e


# num = int(input("Informe um número: "))
print(neperiano(4))
"""

"""
32 - Faça uma função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador de uma fração.
Esta função deve simplificar a fração recebida dividindo o numerador e o denominador pelo maior fator possível.
Por exemplo, a fração 36/60 simplifica para 3/5 dividindo o numerador e o denominador por 12. A função deve
modificar as varáveis passadas como parâmetro.

def simplifica(numerador, denominador):
    fator = 0
    for i in range(1, denominador):
        if numerador % i == 0 and denominador % i == 0:
            fator = i
    numerador = numerador / fator
    denominador = denominador / fator
    return f'Fração simplificadada para {numerador:.0f}/{denominador:.0f}.\nMaior fator: {fator}'


num = int(input("Informe o numerador: "))
den = int(input("Informe o denominador: "))
print(simplifica(num, den))
"""

"""
33 - Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
Ex: se N = 4, N! = 24. Logo, a soma dos seus algarismos é 2 + 4 = 6.

import math


def soma_algarismos_fatorial(n):
    fat = math.factorial(n)
    fat = str(fat)
    soma = 0
    for i in fat:
        soma += int(i)
    return f'Fatorial = {fat}. Somas dos algarismo = {soma}.'


num = int(input("Número: "))
print(soma_algarismos_fatorial(num))
"""

"""
34 -  Faça uma função não-recursiva que receba um número inteiro positivo ímpar N e retorne o
fatorial duplo desse número. O fatorial duplo é definido como o produto de todos os números
naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é:

5!! = 1 * 3 * 5 = 15

def fatorial_duplo(n):
    f_duplo = 1
    for i in range(1, n+1, 2):
        f_duplo *= i
    return f_duplo


while True:
    num = int(input("Informe um número ímpar: "))
    if num % 2 != 0:
        break
    else:
        print('Número par!')


print(fatorial_duplo(num))
"""

"""
35 -  Faça uma função não-recursiva que receba um número inteiro positivo N e retorne o
fatorial quadrúplo desse número. O fatorial quádruplo de um número n é dado por: (2n)!/n!


def fatorial_duplo(n):
    aux = n
    fatoriral_n_vezes2 = n2 = 2 * n
    fatorial_n = n

    print(f'Fatorial de (2*{n})!/({n})! = ', end='')
    while n2 > 1:
        fatoriral_n_vezes2 = fatoriral_n_vezes2 * (n2 - 1)
        n2 -= 1
    print(f'{fatoriral_n_vezes2}')

    print(f'Fatorial de {aux} = ', end='')
    while aux > 1:
        fatorial_n = fatorial_n * (aux - 1)
        aux -= 1
    print(f'{fatorial_n}')

    fat_duplo = fatoriral_n_vezes2 / fatorial_n

    return f'Fatorial quádruplo de {n} = {fat_duplo:.2f}'


num = int(input("Número: "))
print(fatorial_duplo(num)) 
"""

"""
36 - Faça uma função não-recursiva que receba um número inteiro positivo N e retorne o superfatorial desse número.
O superfatorial de um número N é definidade pelo produto dos N primeiros fatoriais de N. Assim, o superfatorial de
4 é sf(4) = 1! * 2! * 3! * 4! * = 288.

def super_fatorial(n):
    fat = 1
    for x in range(1, n+1):
        fat_cada = 1
        for i in range(1, x+1):
            fat_cada *= i
        fat *= fat_cada
    return f'Superfatorial de {n} = {fat}'


print(super_fatorial(4))


# Outro método com biblioteca e recursividade!
import math

def super_fatorial(n):
    sp = 1
    for i in range(1, n+1):
        sp *= math.factorial(i)
    return sp


print(super_fatorial(4))

"""

"""
37 - Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o hiperfatorial desse número.
O hiperfatorial de um número n, escrito H(n), é definido por:

H(n) = II^n base k=1 k^k = 1¹.2².3³...(n-1)^n-1.n^n


def hiperfatorial(n):
    hp = 1
    for i in range(1, n+1):
        hp *= i ** i
    return f'Hiperfatorial de {n} = {hp}'


print(hiperfatorial(2))
"""

"""
38 - Faça um função não-recursiva que receba um número inteiro positivo n e retorne o fatorial
exponecial desse número. Um fatorial exponencial é um inteiro positivo n elevado à potência
de n-1, que por sua vez é elevado à potência de n-2 e assim em diante. Ou seja:

n**(n-1)**(n-2)...


"""

"""
39 - 

def Troque(a, b):
    print(f'Valor de a --> {a}. Valor de b --> {b}.')
    aux = 0
    aux = a
    a = b
    b = aux
    print('Depois da troca:')
    return f'Valor de a --> {a}. Valor de b --> {b}.'


a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

print(Troque(a, b))
"""

"""
40 - 

def retorna_pares(vetor):
    pares = 0
    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
    return f'Existem {pares} números pares na lista'

lista = []
while True:
    lista.append(int(input("Digite um vetor de números. Digite 0 para encerrar: ")))
    if 0 in lista:
        lista.remove(0)
        break

print(lista)
print(retorna_pares(lista))
"""

"""
41 - 

def maior_valor(vetor):
    for numero in vetor:
        return f'Maior valor na lista = {max(vetor)}'


lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    if 0 in lista:
        lista.remove(0)
        break

print(lista)
print(maior_valor(lista))
"""

"""
42 - 

def media_vetor(vetor):
    media = sum(vetor) / len(vetor)
    return f'Média do vetor = {media:.2f}'


lista = []
while True:
    lista.append(float(input("Digite um número: ")))
    if 0 in lista:
        lista.remove(0)
        break

print(lista)
print(media_vetor(lista))
"""

"""
43 - 

"""

"""
44 - 

def retorna_vetores(vetor):
    A = []
    B = []
    for i in vetor:
        if i % 2 == 0:
            A.append(i)
        else:
            B.append(i)
    return f'Vetor  par: {A}\nVetor ímpar: {B}'


x = []

for i in range(1, 31):
    x.append(i)

print(retorna_vetores(x))
"""

"""
45 - 

v = list(range(1, 31))

media = float(sum(v) / len(v))

aux = 0
for i in v:
    aux += (i - media)**2


dp = (aux / len(v)) ** 0.5

print(f'Vetor: {v}')
print(f'Média aritmética: {media:.2f}')
print(f'Desvio padrão: {dp:.4f}')
"""

"""
46 - 

def vetor(v):
    return v


def vetor_inverso(v):
    v.reverse()
    return v


def vetor_media(v):
    return sum(v) / len(v)


V = list(range(1, 21))

print(vetor(V))
print(vetor_inverso(V))
print(vetor_media(V))
"""

"""
47 - 

def retorna_maior_que_10(matriz):
    qtd = 0
    for l in range(0, 4):
        for c in range(0, 4):
            if matriz[l][c] > 10:
                qtd += 1

    for l in range(0, 4):
        for c in range(0, 4):
            print(f'{lista[l][c]:^5}', end='')
        print()
    return f'quantidade números na matriz mariores que 10: {qtd}'


lista = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        lista[l][c] = (int(input(f'Informe o valor na posição [{l}][{c}]: ')))

print(retorna_maior_que_10(lista))
"""

"""
48 -

def soma_acima_diagonal_principal(matriz):
    soma = 0
    soma += matriz[0][1] + matriz[0][2] + matriz[1][2]
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'{matriz[l][c]:^5}', end='')
        print()
    print()
    return f'Soma dos números acima da diagonal principal: {soma}'


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número na posição [{l}][{c}]: '))

print(soma_acima_diagonal_principal(matriz))
"""

"""
49 - 


def soma_abaixo_diagonal_principal(matriz):
    soma = 0
    soma += matriz[1][0] + matriz[2][0] + matriz[2][1]
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'{matriz[l][c]:^5}', end='')
        print()
    print()
    return f'Soma dos números abaixo da diagonal principal: {soma}'


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número na posição [{l}][{c}]: '))

print(soma_abaixo_diagonal_principal(matriz))
"""

"""
50 -

def diagonal_principal(matriz):
    soma = 0
    soma += matriz[0][0] + matriz[1][1] + matriz[2][2]
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'{matriz[l][c]:^5}', end='')
        print()
    print()
    return f'Soma dos números da diagonal principal: {soma}'


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número na posição [{l}][{c}]: '))

print(diagonal_principal(matriz))
"""

"""
51 - 

def diagonal_secundaria(matriz):
    soma = 0
    soma += matriz[0][2] + matriz[1][1] + matriz[2][0]
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'{matriz[l][c]:^5}', end='')
        print()
    print()
    return f'Soma dos números acima da diagonal principal: {soma}'


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número na posição [{l}][{c}]: '))

print(diagonal_secundaria(matriz))
"""

"""
52 - 


"""

"""
def matriz_transposta(m, tam):
    m2 = m
    for l in range(0, tam):
        for c in range(0, tam):
            m2[l][c] = m[c][l]

    print('Matriz: ')
    for l in range(0, tam):
        for c in range(0, tam):
            print(f'{m[l][c]:^5}', end='')
        print()

    print('Matriz transposta: ')
    for l in range(0, tam):
        for c in range(0, tam):
            print(f'{m2[l][c]:^5}', end='')
        print()
    return f'Ok!'
"""

"""
53 - 

def matriz_identidade(m):
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if l == c and matriz[l][c] != 1:
                return 'Matriz Não Identidade!'
            elif l != c and matriz[l][c] != 0:
                return 'Matriz Não Identidade!'
    return 'Matriz Identidade!'


ordem = int(input("Informe a ordem da matriz: "))
matriz = [0] * ordem
for i in range(ordem):
    matriz[i] = [0] * ordem

for l in range(ordem):
    for c in range(ordem):
        matriz[l][c] = int(input(f"Número [{l}][{c}]: "))

print()
print('Matriz: ')
for l in range(ordem):
    for c in range(ordem):
        print(f'{matriz[l][c]:^5}', end='')
    print()

print()
print(matriz_identidade(matriz))

"""

"""
54 - 

def soma_matriz(m):
    soma = 0
    for l in range(4):
        for c in range(4):
            soma += matriz[l][c]
    return f'Soma da matriz = {soma}'


matriz = [0] * 4
for i in range(4):
    matriz[i] = [0] * 4

for l in range(4):
    for c in range(4):
        matriz[l][c] = int(input(f"Informe número [{l}][{c}]: "))

for l in range(4):
    for c in range(4):
        print(f'{matriz[l][c]:^5}', end='')
    print()


print(soma_matriz(matriz))
"""

"""
55 - 

def somas_diagonais(m):
    somaP = 0
    somaS = 0
    for l in range(len(m)):
        for c in range(len(m)):
            if l == c:
                somaP += m[l][c]

    c = len(m) - 1
    for l in range(len(m)):
        somaS += m[l][c]
        c -= 1

    texto = f'''
    Soma diagonal principal: {somaP}
    Soma diagonal secundária: {somaS}
        '''
    return texto



matriz = [0] * 3
for i in range(3):
    matriz[i] = [0] * 3


for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = int(input(f"Informe o número [{l}][{c}]: "))
print()

print('Matriz:')
for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f'{matriz[l][c]:^5}', end='')
    print()

print(somas_diagonais(matriz))
"""


"""
56 - 

def retorna_soma_linha(m, l):
    soma = 0
    for c in range(len(m)-1):
        soma += m[l-1][c]
    return f'Soma da linha {l}: {soma}'


matriz = []
for l in range(7):
    linha = []
    for c in range(6):
        linha.append(int(input(f"Número [{l}][{c}]: ")))
    matriz = matriz + [linha]

while True:
    numero = int(input("Informe uma linha: "))
    if numero > len(matriz) or numero <= 0:
        print('Informe uma linha válida!')
    else:
        break

print()
for l in range(len(matriz)):
    linha = []
    print(f'{l + 1} --> ', end='')
    for c in range(len(matriz)-1):
        print(f'{matriz[l][c]:^5}', end='')
    print("\n\n")


print(retorna_soma_linha(matriz, numero))
"""

"""
57 - 

def retorna_soma_linha(m, c):
    soma = 0
    for l in range(len(m)):
        soma += m[l][c - 1]
    return f'Soma da coluna {c}: {soma}'


matriz = []
for l in range(7):
    linha = []
    for c in range(6):
        linha.append(int(input(f"Número [{l}][{c}]: ")))
    matriz = matriz + [linha]

while True:
    numero = int(input("Informe uma linha: "))
    if numero > len(matriz) or numero <= 0:
        print('Informe uma linha válida!')
    else:
        break

print()
for l in range(len(matriz)):
    linha = []
    for c in range(len(matriz)-1):
        print(f'{matriz[l][c]:^5}', end='')
    print("\n\n")


print(retorna_soma_linha(matriz, numero))
"""

"""
58 -

def produto_matiricial(a, b, c):
    for n in range(len(c)):
        for i in range(len(c)):
            for j in range(len(c)):
                c[n][i] += a[n][j] * b[j][i]

    print('Produto Matricial:')
    for lin in range(len(c)):
        for col in range(len(c)):
            print(f'{c[lin][col]:^5}', end='')
        print("\n")
    return 'Foi difícil!'


ordem = int(input("Ordem da matriz: "))
print()
A = []
for l in range(ordem):
    linhaA = []
    for c in range(ordem):
        linhaA.append(int(input(f"Informe Matriz A [{l}][{c}]: ")))
    A += [linhaA]


print()
B = []
for l in range(ordem):
    linhaB = []
    for c in range(ordem):
        linhaB.append(int(input(f"Informe Matriz B [{l}][{c}]: ")))
    B += [linhaB]

C = [0] * len(A)
for i in range(len(C)):
    C[i] = [0] * len(B)

print('\nMatriz A:')
for l in range(len(A)):
    for c in range(len(A)):
        print(f'{A[l][c]:^5}', end='')
    print("\n")

print('Matriz B:')
for l in range(len(B)):
    for c in range(len(B)):
        print(f'{B[l][c]:^5}', end='')
    print("\n")

print(produto_matiricial(A, B, C))


# Matrizes com dimensões diferentes:

def produto_matiricial(a, b, c):
    for n in range(qtd_linhaA):
        for i in range(qtd_colunaB):
            for j in range(len(c)+1):
                c[n][i] += a[n][j] * b[j][i]

    print('Produto Matricial:')
    for lin in range(qtd_linhaA):
        for col in range(qtd_colunaB):
            print(f'{c[lin][col]:^5}', end='')
        print("\n")
    return 'Foi difícil!'


qtd_linhaA = int(input("Quantas linhas Matriz A: "))
qtd_colunaA = int(input("Quantas colunas Matriz A: "))
A = []
print()
for l in range(qtd_linhaA):
    linhaA = []
    for c in range(qtd_colunaA):
        linhaA.append(int(input(f"Informe Matriz A [{l}][{c}]: ")))
    A += [linhaA]


print()
qtd_linhaB = int(input("Quantas linhas Matriz B: "))
qtd_colunaB = int(input("Quantas colunas Matriz B: "))
B = []
print()
for l in range(qtd_linhaB):
    linhaB = []
    for c in range(qtd_colunaB):
        linhaB.append(int(input(f"Informe Matriz A [{l}][{c}]: ")))
    B += [linhaB]

C = [0] * qtd_colunaB
for i in range(len(C)):
    C[i] = [0] * qtd_colunaA

print('\nMatriz A:')
for l in range(qtd_linhaA):
    for c in range(qtd_colunaA):
        print(f'{A[l][c]:^5}', end='')
    print("\n")

print('Matriz B:')
for l in range(qtd_linhaB):
    for c in range(qtd_colunaB):
        print(f'{B[l][c]:^5}', end='')
    print("\n")

print(produto_matiricial(A, B, C))
"""

"""
59 - 

def uniao(a, b):
    c = []
    for i in range(10):
        c.append(a[i])
        c.append(b[i])
    c_set = set(c)
    return f'Vetor união: {c_set}'


A = []
for i in range(10):
    A.append(int(input(f"Número {i+1}/10 do vetor A: ")))


B = []
print()
for i in range(10):
    B.append(int(input(f"Número {i+1}/10 do vetor B: ")))

print(f'Vetor A: {A}')
print(f'Vetor B: {B}')
print(uniao(A, B))
"""


"""
60 - 

def retorna_strings(string):
    if string == '':
        return -1
    args = str(string)
    return args[0]


s1 = input("String: ")

print(retorna_strings(s1))
"""


"""
61 - 

def anagrama(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if b[i] not in a:
            return False
    return True


s1 = input("Primeira string: ")
s2 = input("Segunda string: ")

print(anagrama(s1, s2))
"""


"""
62 - 

def tamanho_string(s):
    soma = 0
    for i in s:
        soma += 1
    return f'Tamanho da string: {soma}'


string = input("String: ")

print(tamanho_string(string))
"""

"""
63 - 

def retorna_igualdade_string(s1, s2):
    if s1 == s2:
        return 'Strings iguais!'
    return 'Strings diferentes!'


string1 = input("Informe a primeira string: ")
string2 = input("Informe a segunda string: ")

print(retorna_igualdade_string(string1, string2))
"""

"""
64 -

def concatena_strings(str1, str2):
    concatena = f"{str1 + ' ' + str2}"
    return concatena


s1 = input("Primeira frase: ")
s2 = input("Segunda frase: ")

print(concatena_strings(s1, s2))
"""

"""
65 - 

def concatena_valor_n(str1, str2, n):
    str1 += str2[:n]
    return str1


s1 = input("Primeira frase: ")
s2 = input("Segunda frase: ")
num = int(input("Valor de N: "))

print(concatena_valor_n(s1, s2, num))
"""


"""
66 - 

def retorna_maiusculo(c):
    return c.upper()


car = input("Frase: ")

print(retorna_maiusculo(car))

"""

"""
# def funcao(vetor, tam_vetor):


v = input("Frase: ")

print(funcao(v, len(v)))


"""

"""
67 - 
"""


"""
68 - 

def concatena_intercalado(s1, s2):
    a = [0] * (len(s1) + len(s2))

    y = 0
    if len(s1) > len(s2):
        for i in range(0, len(a), 2):
            a[i] = s1[y]
            y += 1

        y = 0
        for i in range(1, len(a)-1, 2):
            a[i] = s2[y]
            y += 1

        s1 = a

        for i in s1:
            print(i, end='')
    else:
        y = 0
        for i in range(0, len(a), 2):
            a[i] = s2[y]
            y += 1

        y = 0
        for i in range(1, len(a)-1, 2):
            a[i] = s1[y]
            y += 1

        s1 = a

        for i in s1:
            print(i, end='')

    return ''


str1 = input("Primeira frase: ")
str2 = input("Segunda frase: ")

print(concatena_intercalado(str1, str2))
"""


"""
68 - 

def concatena_intercalado(s1, s2):
    s3 = ' ' * (len(s1) + len(s2))
    i = 0
    y = 0
    while i < len(s3):
        s3 += s1[i]
        i += 1
        if i == len(s1):
            break
        if y <= len(s2):
            s3 += s2[y]
            y += 1
            if y == len(s2):
                break
    return s3.split()


str1 = input("Primeira frase: ")
str2 = input("Segunda frase: ")

print(concatena_intercalado(str1, str2))
"""

pessoas = {'Bruno': 25, 'Ana': 33, 'Paulo': 43}

nomes = []
idades = []
pessoas_new = ''

for nome, idade in pessoas.items():
    nomes.append(nome)
    idades.append(idade)
    pessoas_new += nome + ' '

print(pessoas_new)
print(nomes)
print(idades)
