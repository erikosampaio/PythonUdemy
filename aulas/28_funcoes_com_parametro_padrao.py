"""
Funções com parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmtro seja opcional;

# Exemplo de função print, o parâmetro é opcional.
print('Geek University')
print()


# Exemplo de função onde a passagem de parãmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())  # TypeError


def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão, eleve ao quadrado.
print(exponencial(3, 5))  # Eleva à potência informada pelo usuário.

# OBS:
# Se o usuário passa somente um argumento, este será atriuído ao
# parâmetro número, e será calculado o quadrado deste número;

# Se o usuário passar 2 argumentos, o primeiro será atruído ao parâmetro número,
# e so segundo ao parâmetro potência. Então será calculada esta potência.



# OBS: Em funções Python, os parâmetros com valores default (padrão), DEVEM sempre estar ao final da declaração.

# ERRO:
# def teste(num=2, potencia):
#    return num ** potencia

# print(teste(6))


# CERTO:
def teste(potencia, num=2):
    return num ** potencia


print(teste(6))



# Outros exemplos:


# def soma(num1, num2):
#     return num1 + num2


# print(soma(4, 3))
# print(soma(4))  # TypeError. O último parâmetro precisa ser informado, para que o
# único argumento digitado seja para o primeiro parâmetro. Parâmetro obrigatório.
# print(soma())  # TypeERROR. Como não existe nenhuma parâmetro default (padrão, ou seja, informado),
# ele não pode ser impresso por não possuir nenhum valor informado.  Parâmetro obrigatório.


# Pra corrigir:

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))  # A função retornará sua execução com os argumentos informados.


def soma(num1, num2=2):
    return num1 + num2

print(soma(4))  # A função retornará sua execução, sendo
# o argumento informado o valor do primeiro parâmetro (num1).


def soma(num1=5, num2=2):
    return num1 + num2

print(soma())  # A função retornará por padrão os valores que estão no parâmetro.


# Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'Bem-vindo Instrutor {nome}'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))  # Dessa forma o true vai ser atribuído para o primeiro parâmetro (nome).
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))


# Por que utilizar parâmetro com valor default (padrão)?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;


# Quais tipos de dados podemos utilizar como valor default para parâmetros?

- Qualquer tipo de dados:
    - Números, strings, floats, booleanos, listas, dicionários, funções e etc;


# Funções como parâmetro de um função:

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))



# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local.
    return f'Oi {instrutor}'  # -> Python


print(instrutor)  # -> Geek
print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma
# variável global, a local terá precedência dentro da função.



def diz_oi():
    prof = 'Geek'  # Variável local.
    return f'Olá {prof}'


print(diz_oi())

# print(prof)  # NameError. Não será impressa por ser uma variável local pedindo para ser
# impressa fora de seu lugar onde foi criada. Poderia ser impressa se fosse global.




# Atenção com variáveis globais (se puder evitar, evite!).

total = 0  # Variável global.
print(total)

# ERRADO:
def incrementa():
    total = total + 1  # UnboundLocalError. Não pode ser realizado uma operação
    # com uma variável que não foi inicializada dentro da função.
    return total


print(incrementa())


# CERTO:
def incrementa():
    global total  # Avisando que queremos utilizar a variável global.

    total = total + 1  # Agora pode ser processado a operação devido termos 'avisado' para a função,
    # (linha 216) ou seja, estamos inicializando a variável global dentro da função.
    return total


print(incrementa())
print(incrementa())
print(incrementa())

print(total)
# OBS: Ao chamarmos uma variável global para uma função, as operações que a utilizam afetarão seu valor.
# No início, o valor de total era '0'. Depois da função executada 3 vezes, seu valor modificou para '3'.




# Podemos ter funções que são declaradas dentro de funções, e também uma forma especial de escopo de variável.


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # nonlocal. Está na função anterior. Não é nem local, nem global.
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

# print(dentro())  # NameError. É uma função que é reconhecida dentro da função 'fora'.
"""