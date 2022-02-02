"""
Recebendo dados usuário

input() -> Todo dado recebido via input é do tipo String.

Em Pyhton, string é que tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados
# print("Qual seu nome? ") #Modo normal
# nome = input()  # Input -> Entrada

nome = input('Qual seu Nome? ') #Modo otimizado

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print ('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}!')

# print("Qual sua idade? ") #Modo normal
# idade = input()

idade = int(input('Qual sua idade? ')) #Modo otimizado

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print ('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
# print(f'A {nome} tem {idade} anos.') -> mesclei com a saída 'nascimento', gerando uma única saída.
"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
# print(f'A {nome} nasceu em {2018 - int(idade)}') -> mesclei com a saida 'idade', gerando uma única saída.
print(f'A {nome} tem {idade} anos, logo, nasceu em {2021 - idade}.')
