"""
Dicionários.

OBS: Em algumas linguagens de programação. os dicionários Python são conhecidos por 'mapas'.:key

Dicionários são coleções do tipo chave/valor.

listas:
[0, 1, 2] (chave)
[1, 2, 3] (valor)

tuplas:
(0, 1, 2) (chave)
(1, 2, 3) (valor)

Dicionários são representados por chaves {}.
print(type(paises))

OBS: Sobre dicionários
    - Chave e valor são separados por 'chave:valor';
    - Tanto chave quanto valor podem ter ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários!

# Forma 1 (Mais comum):
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum):
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))



# Acessando elementos!

# Forma 1 = Acessando via CHAVE, da mesma forma que lista/tupla.
print(paises['br'])
# print(paises['ru'])
# OBS: Caso tentemos fazer um acesso utilizando uma chave que não existe, teremos o erro 'KeyError'.

# Forma 2 - Acessando via GET (Recomendada).
print(paises.get('br'))
print(paises.get('ru'))
# Caso o get não encontre o objeto com a chave informada,
será retornado o valor None e não será gerado 'KeyError'.
if pais:
    print(f'Encontrei o país.')
else:
    print('Não encontrei país.')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada.
pais = paises.get('br', 'Não encontrado')  # Caso não exista a chave
# informada(antes da vírgula) retorne o valor da 2ª Caso haja, informe o valor.
print(f'Encontrei o país {pais}')  # pais aqui é a variável recebendo a condição acima.


# Podemos verificar se determinada chave se encontra em um dicionário.
print('br' in paises)  # True. Está no dicionário.
print('ru' in paises)  # False. Não está no dicionário.
print('Estados Unidos' in paises)  # False. Ele busca chav. Isso é um valor.
if 'ru' in paises:
    russia = paises['ru']


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean),
# inclusive lista, tupla, dicionário, chaves de dicionários.
# Tuplas, por exemplo, são bastantes interessante de serem utilizado
# como chave de dicionários, pois as mesmas são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))



# Adicionar elementos em um dicionário.

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum:
receita['abr'] = 350
print(receita)


# Forma 2 - Menos Comum:
novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário.
# Forma 1:
receita['mai'] = 550
print(receita)

# Forma 2:
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar elementes ou atualizar dados em um dicionário é a mesma.
# CONCLUSAO 2: Em dicionários NÃO podemos ter chaves repetidas (Elas serão atualizadas).



# Remover dados de um dicionário.

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)


# Forma 1 - Mais comum.
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado.

# Forma 2 - Menos comum.
del receita['fev']
print(receita)
# Se a chave não existir, será gerado um KeyError.
# OBS: Neste caso o valor removido NÃO é retornado.


# Imagine que você tem um comércio eletrônico, onde temos um carrinho e compras na qual a dicionamos produtos.
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        quantidade;
        preço

# 1 - Poderíamos utilizar uma Lista para isso? Sim!

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto (lista).

# 2 - Poderíamos utilizar uma Tupla para isso? Sim.

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto (lista).

# 3 - Poderíamos utilizar um dicionário para isso? Sim.

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeaz sobre cada informação.




# Métodos de dicionários.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (Zerar dados):
d.clear()
print(d)


# Copiar um diciocário para outro.

# Forma 1 - Deep Copy = Copia sem alterar o primeiro dicionário.
novo = d.copy()  # criando um dicionário chamado 'novo' sendo cópia do dicionário 'd'.
print(novo)
novo['d'] = 4  # Adicionando uma nova chave chamada 'd' recebendo o valor 4.
print(d)
print(novo)

# Forma 2 - Shallow Copy = Copia podendo posteriormente
# alterar o primeiro dicionário ao alterar o segundo.
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)
"""

# Forma não usual de criação de dicionário.

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
# acima temos uma lista dentro de um dicionário, virando cada item da lista numa chave, e
# o valor 'desconhecido' tornando-se valor de cada item da lista (que virou chave).
print(usuario)
print(type(usuario))

# O método 'fromkeys' recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável um chave
# e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

