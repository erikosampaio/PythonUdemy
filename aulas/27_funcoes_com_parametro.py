"""
Funções com parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;



# Refatorando uma função


# Antes:
def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())


# Depois:
def quadrado(numero):  # Esta função está recebendo um parâmetro obrigatório.
    #  return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# OU:
ret = quadrado(6)
print(ret)

# print(quadrado())  # TypeError.


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Ériko')



# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# quantos parâmetros forem necessários. Eles são separados por vírgula;

# Exemplos:
def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))


# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos #TypeError.

# print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais.
# print(soma(4))  # TypeError - Passando argumentos a menos.


# Nomeando parâmetros.

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença de parâmetros e argumentos:
# Parâmetros são varíaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de um função;

# A ordem dos parâmetros importa!
nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem.

print(nome_completo(nome='Anjelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))


"""

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        # return f'Total da soma de ímpares: {total}'  # OBS: Return aqui finaliza a primeira condição atendida.
    return f'Total da soma de ímpares: {total}'  # OBS: Return finaliza a função.


lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
print(soma_impares(lista))


tupla = (1, 2, 3, 4, 5, 6, 7)
print(tupla)
print(soma_impares(tupla))

