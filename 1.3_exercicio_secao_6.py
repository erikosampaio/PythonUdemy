"""
1 -
"""
# for n in range(1, 6):
#   print(f'{n * 3}')

"""
2 - 
"""
# for n in range(1, 101):
#     print(n)

# n = 0
# while n < 100:
#     n += 1
#     print(n)

"""
3 -
"""
# con = 10
# while con > -1:
#     print(con)
#     con -= 1
# print('FIM!')

"""
4 -
"""
# num = int(input('Informe um número: '))
# for n in range(0, 100000+1, 1000):
#     print(n)

"""
5 - 
"""
# som = 0
# for _ in range(1, 11):
#     x = int(input('Informe um número: '))
#     som = som + x
# print('Soma = {0}'.format(som))

"""
6 - 
"""
# media = 0
# soma = 0
# for _ in range(1, 10+1):
#     a = int(input('Informe um número: '))
#     soma += a
# media = soma / 10
# print(f'Média = {media}')

"""
7- 
"""
# soma = 0
# con = 0
# for n in range(1, 10+1):
#     a = int(input('Informe um número positivo: '))
#     if a > 0:
#         soma += a
#         con += 1
# media = soma / con
# print(f'Média = {media}')

"""
8 - 
"""
# a = int(input('Informe um número: '))
# menor_valor = a
# maior_valor = a
# for x in range(2, 11):
#     a = int(input('Informe um número: '))
#     if menor_valor > a:
#         menor_valor = a
#     elif maior_valor < a:
#         maior_valor = a
# print(menor_valor)
# print(maior_valor)

"""
9 - 
"""
# num = int(input('Informe um número: '))
# con = 0
# for n in range(1, (num*2)+1):
#     if n % 2 == 1:
#         con += 1
#         print(n)
# print(f'\n{num} Primeiros ímpares.')

"""
10 - 
"""
# soma = 0
# for n in range(0, 51, 2):
#         soma += n
#         print(n)
# print(f'Soma dos 50 primeiros números pares = {soma}')

"""
11 - 
"""
# n = int(input('Informe um número: '))
# for x in range(n + 1):
#    print(x)

"""
12 - 
"""
# n = int(input('Informe um número: '))
# for x in range(n, -1, -1):
#     print(x)

"""
13 - 
"""
# num = int(input('Informe um número par: '))
# while num % 2 != 0:
#     print('Número não é par!')
#     num = int(input('Informe um número par: '))
# if num % 2 == 0:
#     for n in range(0, num+1, 2):
#         print(n)

"""
14 - 
"""
# num = int(input('Informe um número par: '))
# while num % 2 != 0:
#     print('Número não é par!')
#     num = int(input('Informe um número par: '))
# if num % 2 == 0:
#     for n in range(num, -1, -2):
#         print(n)


"""
15 - 
"""
# num = int(input('Informe um número ímpar: '))
# while num % 2 != 1:
#     print('Número não é ímpar.')
#     num = int(input('Informe um número ímpar: '))
# for n in range(1, num+1, 2):
#     print(n)

"""
16 - 
"""
# num = int(input('Informe um número ímpar: '))
# while num % 2 != 1:
#     print('Número não é ímpar.')
#     num = int(input('Informe um número ímpar: '))
# for n in range(num, 0, -2):
#     print(n)

"""
17 - 
"""
# soma = 0
# num = int(input('Informe um número: '))
# for n in range(num+1):
#     soma += n
# print(f'Soma dos {num} primeiros números naturais: {soma}')

"""
18 - 
"""
# num = 0
# maior = 0
# con = 0
# q = int(input('Informe a quantidade de números a serem lidos: '))
# for _ in range(q):
#     num = int(input('Informe um número: '))
#     if num > maior:
#         maior = num
# print(f'Maior valor = {maior}')
# print(f'Quantas vezes repete o Maior valor = {con}')

"""
19 - 
"""
# num = int(input('Informe um número entre 100 e 999: '))
# while 100 > num or num > 999:
#     num = int(input('Informe um número entre 100 e 999: '))
# num = str(num)
# print(f'{num[0]}\n{num[1]}\n{num[2]}')

"""
20 - 
"""
# par = 0
# con = 0
# print("Informe números, sendo '1000' o valor para encerrar: ")
# n = int(input('Informe um número: '))
# while n != 1000:
#     if n % 2 == 0:
#         print(f'Número par!')
#         par += 1
#         con += 1
#         n = int(input('Informe um número: '))
#     else:
#         print(f'Não é número par!')
#         n = int(input('Informe um número: '))
#         con += 1
# print(f'Quantidade de Números lidos: {con}')
# print(f'Quantidade de Números pares: {par}')

"""
21 - 
"""
# imp = 1
# par = 0
# print('Informe dois números: ')
# n1 = int(input('1º Valor: '))
# n2 = int(input('2º Valor: '))
# for n in range(n1, n2+1):
#     if n % 2 == 0:
#         par += n
#     else:
#         imp *= n
# print(f'Soma dos números pares de {n1} até {n2} = {par}.')
# print(f'A multiplicação dos números ímpares de {n1} até {n2} = {imp}.')

"""
22 - 
"""
# soma = 0
# con = 0
# print('Informe uma nota válida entre 10 e 20: ')
# n = int(input('Nota: '))
# while 10 <= n <= 20:
#     if 10 <= n <= 20:
#         soma += n
#         con += 1
#         n = int(input('Nota: '))
# media = soma / con
# print(f'Media =  {media}!')

"""
23 - 
"""
# num = int(input('Informe um número: '))
# for n in range(1, num+1):
#     if num % n == 0:
#         print(f'{n} - Divisor de {num}.')

"""
24 - 
"""
# soma = 0
# num = int(input('Informe um número: '))
# for n in range(1, num+1):
#     if num % n == 0:
#         print(f'{n} - Divisor de {num}.')
#         soma += n
# print(f'Soma dos divisores de {num} = {soma}.')

"""
25 - 
"""
# soma = 0
# for n in range(1, 101):
#     if n % 3 == 0 or n % 5 == 0:
#         if n > 5:
#             print(n)
#             soma += n
# print(f'Soma dos múltiplos de = {soma}')

"""
26 - 
"""
# num = int(input('Informe um número: '))
# for n in range(num, num ** 2):
#     if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
#         print(n)
#         break
# else:
#     print('Não há múltiplo de 11, 13 ou 17')

"""
26 - 
"""
# produto = 1
# e = 0
# n = int(input('valor: '))
# for i in range(1 , n+1):
#     produto *= i
#     print(f'\nprduto {i} : {produto}')
#     e += 1/produto
#     print(f'aumulado de produtos = {e}')
# print(f'{e:.2f}')

"""
35 - 
"""
# soma = 0
# print('Informe o valor inicial e valor final: ')
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# if a > b:
#     print('Intervalo de valores inválidos!')
# print(f'Números ímpares dentro do intervalo de {a} e {b}:')
# for n in range(a, b):
#     if n % 2 == 1:
#         print(n)
#         soma += n
# print(f'Soma dos números ímpares dentro do intervalo de {a} e {b}: {soma}.')

"""
36 - 
"""
# soma = 0
# soma_quadrados = 0
# for n in range(1, 11):
#     soma_quadrados += (n ** 2)
#     soma += n
# quadrado_soma = (soma ** 2)
# diferenca = quadrado_soma - soma_quadrados
# print(f'Soma dos quadrados dos primeiros 100 números naturais: {soma_quadrados}.')
# print(f'Quadrado da soma dos primeiros 100 números naturais: {quadrado_soma}.')
# print(f'Diferença entre {quadrado_soma} e {soma_quadrados} = {diferenca}.')

"""
37 - 
"""
# for i in range(1000, 9999):
#     a = str(i)
#     b = a[0:2]
#     c = a[2:4]
#     x = int(b)
#     y = int(c)
#     if x + y == i ** 0.5:
#         print(i)

"""
39 - 
"""
# print('Informe e base e altura do triângulo em cm: ')
# base = float(input('Base: '))
# altura = float(input('Altura: '))
# while base <= 0 or altura <= 0:
#     print('Valor inválido!')
#     print('Informe valores válidos: ')
#     base = float(input('Base: '))
#     altura = float(input('Altura: '))
# area = (base * altura) / 2
# metro = area / 100
# print(f'Área = {area} cm ou {metro:.2f} m.')

"""
40 - 
"""
# maior = 0
# menor = 1000000
# print('Informe uma sequência de números, sendo um\nnúmero negativo pra finalizar. ')
# n = int(input('Número: '))
# while n >= 0:
#     if n > maior:
#         maior = n
#     elif n < menor:
#         menor = n
#     n = int(input('Número: '))
# print(f'Maior número lido: {maior}.')
# print(f'Menor número lido: {menor}.')

"""
46 - 
"""
# aleatorio = randrange(1000)
# contador = 1
# chute = int(input('Informe um número: '))
# while aleatorio != chute:
#     if chute > aleatorio:
#         print('Chute pra mais.')
#     else:
#         print('Chute pra menos.')
#     chute = int(input('Informe um número: '))
#     contador += 1
# print('Acertou miserávi!')
# print(f'Tu tentou {contador} vezes até acertar.')

"""
60 - 
"""
# c = 0
# soma = 0
# maior = 0
# menor = 10000
# par = 0
# print("Informe uma sequência de números. Digite '0' para encerrar!")
# n = int(input('Informe um número: '))
# while n != 0:
#     if n > 0:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
#         c += 1
#         soma += n
#     if n % 2 == 0:
#         par += n
#     n = int(input('Informe um número: '))
# media = soma / c
# print(f'a) Soma do números: {soma}')
# print(f'b) Quantidade dos números digitados: {c}')
# print(f'c) Média dos números digitados: {media}')
# print(f'd) Maior número digitado: {maior}')
# print(f'e) Menor número digitado: {menor}')
# print(f'f) Média dos números pares: {par}')

"""
62 - 
"""
# soma = 1
# for n in range(1, 1001):
#     number_p1 = num2words(n, lang='pt_BR')
#     soma += number_p1.count('')
# print(soma)

# from num2words import num2words
# soma = 0
# for n in range(1, 6):
#     number_p1 = num2words(n, lang='pt_BR')
#     a = number_p1.count('') - 1
#     soma += a
#     print(f'letras em {n} = {a}')
#     print(f'soma = {soma}')
# print(soma)

