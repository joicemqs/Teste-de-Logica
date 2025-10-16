class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Criando os nós
maca = No("Maçã")
morango = No("Morango")
pera = No("Pera")
goiaba = No("Goiaba")
limao = No("Limão")
abacaxi = No("Abacaxi")
laranja = No("Laranja")
banana = No("Banana")
cebola = No("Cebola")

# Montando a árvore
maca.esquerda = morango
maca.direita = pera

morango.esquerda = goiaba
morango.direita = limao

pera.esquerda = abacaxi
pera.direita = laranja

laranja.esquerda = banana
laranja.direita = cebola
