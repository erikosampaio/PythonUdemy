# Copiar Listas em Python da forma certa!

lista_a = ["Eriko", "Nayara", "Tarciane"]
# ERRADA:
# lista_b = lista_a --> Apenas atribue lista_b para o mesmo endereço de lista_a.

# 1ª Forma correta:
lista_b = lista_a[:]

# 2ª Forma correta:
lista_b = lista_a.copy()

lista_b.append("Arroz")
print(lista_a)
print(lista_b)

texto_a = "Eriko"
texto_b = texto_a
texto_b = texto_b.replace("E", "A")
print(texto_a)
print(texto_b)

# Para listas de listas, temos que pensar diferente!
produtos = [
    ["Ipad", 5000],
    ["Iphone", 4500],
]

produtos2 = produtos[:]
produtos2[0][1] = 6000
print(produtos)
print(produtos2)


# Solução é um deepcopy (Cópia profunda)
import copy
produtos3 = copy.deepcopy(produtos)
produtos3[0][1] = 1000
print(produtos)
print(produtos3)
