
"""
1-
a = [1, 0, 5, -2, -5, 7]
print(a)
soma = a[0] + a[1] + a[5]
print(soma)
a[4] = 100
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
"""

"""
2-
a = list()
for n in range(6):
    a.append(int(input('Valor: ')))
print(a)
"""

"""
3-
a = []
q = []
for n in range(10):
    a.append(float(input('Valor: ')))
    q.append(a[n] ** 2)
print(a)
print(q)
"""

"""
4-
a = []
for n in range(1, 9):
    a.append(int(input('valor: ')))
print('Informe as duas posições: ')
x = 10
y = 10
while x and y < 8:
    x = int(input('Primeira posição: '))
    y = int(input('Segunda posição: '))
soma = a[x-1] + a[y-1]
print(a)
print(f'Soma dos números nas posições {a[x-1]} e {a[y-1]} = {soma}.')
"""

"""
5-
a = []
con = 0
for n in range(10):
    a.append(int(input('Valor: ')))
    if n % 2 == 0:
        con += 1
print(a)
print(con)
print(f'if a[n] % 2 == 0:')
"""

"""
6-
a = []
for n in range(11):
    a.append(int(input('Valor: ')))
print(max(a))
print(min(a))
"""

"""
7-
a = []
for i in range(10):
    a.append(int(input('Valor: ')))
print(a)
print(max(a))
print(a.index(max(a)))
"""

"""
8-
a = []
for i in range(5):
    a.append(int(input('Valor: ')))
a.reverse()
print(a)
"""

"""
9-
a = []
b = 0
while b < 6:
    num = int(input('Valor: '))
    if num % 2 == 0:
        a.append(num)
        b += 1
    else:
        print('Informe um valor válido: ')
a.reverse()
print(a)
"""

"""
10-
a = []
for i in range(15):
    a.append(int(input(f'Informe a nota do {i+1}º Aluno: ')))
media = sum(a)/len(a)
print(f'\n\tNotas dos 15 alunos: \n{a}')
print(f'\n\tMédia dos 15 alunos: \n{media}')
"""

"""
11-
v = []
cn = 0
soma = 0
for i in range(10):
    v.append(float(input('Valor: ')))
for x in v:
    if x < 0:
        print(x)
        cn += 1
    elif x > 0:
        print(x)
        soma += x
print(f'Vetor: {v}')
print(f'Quantidade de Negativos: {cn}')
print(f'Soma dos positivos: {soma}')
"""

"""
12-
a = []
soma = 0
for i in range(5):
    a.append(int(input('Valor: ')))
for x in a:
    soma += x
print(f'Vetor: {a}.\nMaior Número = {max(a)}.\nMenor número = {min(a)}.\nMédia = {soma / len(a)}.')
"""

"""
13-
a = []
for i in range(5):
    a.append(int(input('Valor: ')))
print(a.index(max(a))+1)
print(a.index(min(a))+1)
"""

"""
14-
a = []
for i in range(10):
    a.append(int(input('Valor: ')))
for x in a:
    b = a.index(x)
    if a[b] in a[b+1::]:
        print(a[b])
"""

"""
15-
a = []
for i in range(10):
    a.append(int(input('Valor: ')))
for x in a:
    b = a.index(x)
    if not a[b] in a[b+1::]:
        print(a[b])
"""

"""
16-
a = []
for i in range(5):
    a.append(float(input('Valor: ')))
cod = int(input('Código: '))
if cod == 0:
    print('Programa finalizado!')
else:
    while 1 != cod != 2:
        cod = int(input("informe um código válido: "))
    else:
        if cod == 1:
            print(a)
        else:
            a.reverse()
            print(a)
"""

"""
17-
a = []
for i in range(10):
    a.append(int(input(f'Número {i+1}/10: ')))
print(a)

for i, v in enumerate(a):
    if v < 0:
        a[i] = 0
print(a)
"""

"""
18-
a = []
con = 0
for i in range(10):
    a.append(int(input('Número: ')))
num = int(input('Informe um número: '))
while num not in a:
    num = int(input('Informe um dos valores do vetor: '))
else:
    for i in a:
        if i % num == 0 and i > num:
            con += 1
print(f'        Vetor          {a}.')
a.sort()
print(f'Vetor em ordem direta: {a}')
print(f'Quantidade de múltiplos de {num} no vetor: {con}.')
"""

"""
19-
a = []
for i in range(10):
    a.append((i+(5*i)) % (i+1))
print(a)
"""

"""
20-
vetor = []
impar = []

for i in range(10):
    a = int(input('valor entre 0 e 50: '))
    while not -1 < a < 51:
        a = int(input('digite um valor entre 0 e 50: '))
    vetor.append(a)
for i in vetor:
    if i % 2 != 0:
        impar.append(i)
print(f'\nVetor:\n{vetor}')
print('Vetor de dois e dois:')
x = 0
while x < 10:
    print(f'{vetor[x]}, {vetor[x+1]}.')
    x += 2

print(f'\nVetor só de impares:\n{impar}')
print(f'Vetor de dois em dois:')
y = len(impar)
n = 0
while n < y:
    if n % 2 == 0:
        print(impar[n], end=', ')
    else:
        print(impar[n])
    n += 1
"""

"""
21-
va = []
vb = []
vc = []
print('Informe 10 números para o primeiro vetor.')
for i in range(10):
    va.append(int(input("Valor: ")))
print('Informe 10 números para o segundo vetor.')
for n in range(10):
    vb.append(int(input("Valor: ")))
print(f'Vetor A: {va}.')
print(f'Vetor B: {vb}.')
for x in range(10):
    vc.append(va[x]-vb[x])
print(f'Vetor C: {vc}.')
"""

"""
22-

a = []
b = []
c = []

for i in range(5):
    a.append(int(input('Valor a: ')))
print('\n')

for i in range(5):
    b.append(int(input('Valor b: ')))

x = 0
y = 0
i = 0
while i < 10:
    if i % 2 == 0:
        c.append(a[x])
        x += 1
    else:
        c.append(b[y])
        y += 1
    i += 1

print(a)
print(b)
print(c)
"""

"""
23-
from random import randrange as rd

a = []
b = []
soma = 0
for n in range(5):
    a.append(float(rd(1, 50)))
    b.append(float(rd(51, 100)))
    pe = a[n] * b[n]
    soma += pe

print(a)
print(b)
print(soma)
soma = 0

"""

"""
24-
from random import randrange as rd
a = []
b = []

for i in range(5):
    a.append(str(input('Nome: ')))
    b.append(float(rd(1, 10)))

print(a)
print(b)
maximo = b.index(max(b))
minimo = b.index(min(b))
print(f'Nome mais alto = {a[maximo]}. Altura mais alto = {b[maximo]}')
print(f'Nome mais baixo = {a[minimo]}. Altura mais baixo = {b[minimo]}')

"""

"""
25-
a = []

con = 0
num = 1
while con < 100:
    x = str(num)
    if num % 7 != 0 and x[-1] != '7':
        a.append(num)
        con += 1
    num += 1
print(a)
print(len(a))
"""

"""
27 - 
a = []
for i in range(1, 11):
    a.append(int(input(f'Valor {i}/10: ')))

for indice, valor in enumerate(a):
    print(f'posição = {indice + 1}ª - número = {valor}')

print('\n')
for x in a:
    con = 0
    for n in range(1, x + 1):
        if x % n == 0:
            con += 1
    if con == 2:
        print(f'O {x} é primo e está na posição {x}!')
"""


"""
29 - 
a = []
imp = 0
soma = 0
for i in range(6):
    a.append(int(input(f'{i+1}/6: ')))
print('Pares: ')
for i in a:
    if i % 2 == 0:
        print(i)
        soma += i
print('\nÍmpares: ')
for i in a:
    if i % 2 == 1:
        print(i)
        imp += 1
print(f'Quantidade de números ímpares: {imp}')
"""


"""
30 - 
a = set()
b = set()

for i in range(10):
    a.add(int(input(f'Valor {i+1}/10: ')))
print(a)

for i in range(10):
    b.add(int(input(f'Valor {i+1}/10: ')))
print(b)

c = a.intersection(b)
print(c)
"""


"""
31 - 
a = set()
b = set()

for i in range(20, 30):
    a.add(i)
print(a)

for i in range(6, 10):
    b.add(i)
print(b)

c = a.union(b)
print(c)
"""


"""
32 - 
x = []
y = []

con1 = 1
while con1 <= 5:
    valor = int(input('Valor a): '))
    if valor not in x:
        x.append(valor)
        con1 += 1
print(x)


con2 = 1
while con2 <= 5:
    valor2 = (int(input('Valor y): ')))
    if valor2 not in y:
        y.append(valor2)
        con2 += 1
print(y)

for i in range(5):
    print(f'Soma da {i+1}ª posicão: {x[i] + y[i]}')  # 1

for i in range(5):
    print(f'Produto da {i+1}ª posição: {x[i] * y[i]}')  # 2

xset = set(x)
yset = set(y)
ix = xset.intersection(yset)
dx = xset.difference(yset)
uxy = xset.union(yset)
print(f'Diferença entre x e y: {dx}')
print(f'Intercessão entre x e y: {ix}')  # 4
print(f'União entre x e y, sendo todos de x e todos de y que não estão em x: {uxy}')  # 5
"""


"""
33 - 
a = []
for i in range(15):
    num = int(input('Valor: '))
    if num != 0:
        a.append(num)
print(a)
"""

"""
34 - 
a = []
con = 1
print('Informe 10 números diferentes.')
while con <= 10:
    num = int(input('número: '))
    if num not in a:
        a.append(num)
        con += 1
    else:
        print('Digite outro número ainda não digitado.')
print('Vetor final:')
for i, v in enumerate(a):
    print(f'{i+1}º número: {v}')
"""

"""
35 - Falta fazer

"""

"""
36 - 
a = []

for i in range(10):
    a.append(float(input('Valor real: ')))
print(a)
a.sort()
print(a)
"""
