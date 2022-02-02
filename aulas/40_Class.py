class Pessoa:
    def __init__(self, nome, idade, altura, cor, profissao):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cor = cor
        self.profissao = profissao

    def beleza(self, opniao):
        if opniao == "ela":
            print("Linda")
        elif opniao == "ele":
            print("Lindo")
    #  métodos do controle remoto:
    #      - passar de canal
    #      - mexer no volume
    #      - abrir netflix
    #      - desligar tv


eriko = Pessoa("Ériko", "28 anos", "1.75", "negro", "Developer")
nayara = Pessoa("Nayara", "26 anos", "1.57", "negra", "Analista de DP")

print(eriko.nome)
print(eriko.profissao)
print(eriko.altura)
eriko.beleza("ele".lower())
print(type(eriko))

print("\n")
print(nayara.nome)
print(nayara.profissao)
print(nayara.altura)
nayara.beleza("ela".lower())
print(type(nayara))
