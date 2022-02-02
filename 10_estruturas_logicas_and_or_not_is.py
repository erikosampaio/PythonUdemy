"""
Estruturas lógicas: and (e), or (ou), not (não), is (é).

Operadores unários:
    - not.
Operadores binários:
    - and, or, is.

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser 'True'.
Para o 'or', um ou outro valor precisa ser 'True'.
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se fpr False. vira True.
Para o 'is', um valor é comparado com um outro.

"""

# And:
# if ativo and logado:
# print("Bem-vindo usuário.")
# else:
# print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")

# Or:
# if ativo or logado:
# print("Bem-vindo usuário.")
# else:
# print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")

# Not:
# Obs: print(not False) imprime o valor oposto (True).
#      print(not True) imprime o valor oposto (False).
#  if not ativo:
#  print("Você precisa ativar sua conta. Por favor, cheque seu email.")
#  else:
#  print("Bem-vindo usuário.")

# 1º Método Is:
# if ativo is False:
#  print("Você precisa ativar sua conta. Por favor, cheque seu email.")
#  else:
#  print("Bem-vindo usuário.")

# 2º Método Is, otimizado:
# if ativo:
# print("Bem-vindo usuário.")
# else:
# print("Você precisa ativar sua conta. Por favor, cheque seu email.")

ativo = True
logado = True
