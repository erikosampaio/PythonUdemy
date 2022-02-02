"""
Módulo Collections - Default Dict

# Recapitulação Dicinários
dicionario = {'curso': 'Programação em Pyhton: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # ??? KeyError. Chave não existe em dicionário.

Default Dict -> Ao criar um dicionário, nós informamos um valor default, podendo utilizar um lambda pra isso.
Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.


# Fazendo import.
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui não.

print(dicionario)
"""
