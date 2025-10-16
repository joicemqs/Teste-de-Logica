class No: #Classe No
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

#Criação dos Nós
maca = No("Maçã")
morango = No("Morango")
pera = No("Pera")
goiaba = No("Goiaba")
limao = No("Limão")
abacaxi = No("Abacaxi")
laranja = No("Laranja")
banana = No("Banana")
cebola = No("Cebola")

#Posicionamento
maca.esquerda = morango
maca.direita = pera

morango.esquerda = goiaba
morango.direita = limao

pera.direita = abacaxi

abacaxi.direita = laranja

laranja.esquerda = banana
laranja.direita = cebola

def caminhoBusca(no, palavra, caminho=""):
    if no is None: #Retorna ao chegar na folha da árvore
        return None
    if no.valor == palavra:
        return caminho + no.valor #Retorna o caminho e o valor do proprio nó ao cehgar na palavra-chave
    esquerda = caminhoBusca(no.esquerda, palavra, caminho + no.valor + "--> ") #recebe o caminho se o galho possuir a palavra-chave
    direita = caminhoBusca(no.direita, palavra, caminho + no.valor + "--> ")#recebe o caminho se o galho possuir a palavra-chave
    if esquerda: 
        return esquerda #Retorna o caminho da esquerda se ele não possuir valor None
    if direita:
        return direita #Retorna o caminho da direita se ele não possuir valor None

print("\n-----------------------------------------------------")
palavra = (input("Digite a palavra-chave para busca na árvore: "))

if caminhoBusca(maca, palavra):
    print(caminhoBusca(maca, palavra))
else:
    print("\nNenhum item correspondente foi encontrado na árvore!")
print("-----------------------------------------------------\n")