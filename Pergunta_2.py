class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Montando a árvore
maca = No("Maçã")
morango = No("Morango")
pera = No("Pera")
goiaba = No("Goiaba")
limao = No("Limão")
abacaxi = No("Abacaxi")
laranja = No("Laranja")
banana = No("Banana")
cebola = No("Cebola")

maca.esquerda = morango
maca.direita = pera

morango.esquerda = goiaba
morango.direita = limao

pera.esquerda = abacaxi
pera.direita = laranja

laranja.esquerda = banana
laranja.direita = cebola

def caminhoBusca(no, palavra, caminho=""):
    if no is None:
        return None
    if no.valor == palavra:
        return caminho + no.valor


print(caminhoBusca(maca, "Maçã"))