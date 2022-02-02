"""
Saindo de loops com break

Funciona da mesma forma que nas linguaguens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop.')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
"""


a = []
b = []
c = []
for _ in range(10):
    a.append(int(input('Valor para vetor A: ')))
print(f'\n')
for _ in range(10):
    b.append(int(input('Valor para vetor B: ')))
for _ in range(10):
    x = a[_]-b[_]
    c.append(x)
print(a)
print(b)
print(c)