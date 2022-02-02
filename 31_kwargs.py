"""
**kwargs

Poderíamos chamar este parâmetro e **xis, mas por convenção chamamos de **kwargs.

Este é só mais um parâmetro mas diferente do *args que coloca os valores extra em um tupla, o **kwargs exige que
utilizemos parâmetros nomeados, e transforma esses parâmetros em um dicionário (dict).


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor.title()}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='navy')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek'].title()} Geek!"
    return 'Não tenho certeza de quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))



# Nas nossas funções, podemos ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs;

# Exemplo:
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)



# Entenda por quê é importante a ordem dos parâmetros na declaração.

# Função com a ordem correta de parâmetros:
# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#     return [a, b, args, instrutor, kwargs]
# print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Fica assim o print:
# a = 1
# b = 2
# arg = (3,)
# instrutor = 'Geek'
# kwrags = {'sobrenome': 'University', 'cargo': 'Instrutor'}


# Função com a ordem incorreta de parâmetros:
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Fica assim o print:
# a = 1
# b = 2
# arg = ()
# instrutor = 3
# kwrags = {'sobrenome': 'University', 'cargo': 'Instrutor'}


# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(nome='Felicity', sobrenome='Jones'))
print(mostra_nomes(**nomes))  # Desempacotando o **kwargs
"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

    
lista = [1, 1, 1]
tupla = (2, 2, 2)
conjunto = {1, 2, 3, 3, 3, 3}

soma_multiplos_numeros(*lista)  # Desempacotando a lista para se adequar a função.
soma_multiplos_numeros(*tupla)  # Desempacotando a tupla para se adequar a função.
soma_multiplos_numeros(*conjunto)  # Desempacotando o conjunto para se adequar a função.

dicionario = dict(a=4, b=4, c=4)

soma_multiplos_numeros(**dicionario)  # Desempacotando o dicionário.

# OBS: Os nomes das chaves em um dicionário deve ser o mesmo dos parâmetros da função!

# Exemplo de erro se usarmos valores difentes entre as chaves e os parâmetros da função:
dicionario2 = dict(d=4, e=4, f=4)
# soma_multiplos_numeros(**dicionario)  # Desempacotando o dicionário.

# Podemos passar outros valores além dos exigidos.
dicionario2 = dict(a=4, b=4, c=4, nome='Geek')
soma_multiplos_numeros(**dicionario2, lang='Python')
