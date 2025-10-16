# Teste de Lógica

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

Essa é uma aplicação construída para resolver questões de lógica que envolvem arrays e árvore binária, a linguagem escolhida para desenvolvimento foi Python, pela facilidade tanto de aprendizado quanto pela simplicidade ao se trabalhar com arrays.

## Pré-requisitos

### 1. Instalação da linguagem de programação 
O instalador do Python pode ser baixado pelo site oficial tanto para Windows quanto para MacOS ou Linux em:

<https://www.python.org/downloads/>

Para usuários de Windows o Python pode ser instalado diretamente da Microsoft Store, forma recomendada para a maioria dos usuários segundo a própria página de download do site. 

Após instalação para consultar a versão instalada Podemos utilizar no cmd o comando: 

`python –version` 
 
 E em seguida a versão será exibida.

### 2. Instalação do Visual Studio Code e extensões

Para executar os programas foi utilizado o software Visual Studio Code disponível para download em:

<https://code.visualstudio.com/download>

Foram necessárias duas extensões para rodar o código no programa,  a primeira delas é a extensão Python disponível na aba extensões na lateral esquerda: 

![Extensão 1 na aba lateral](/imagens/extensao1.png)

A segunda extensão utilizada foi  a extensão Python Debugger também disponível na aba lateral: 

![Extensão 2 na aba lateral](/imagens/extensao2.png)

### 3. Instalação do Git

Para controle do versionamento foi utilizada a ferrmaenta Git que pode ser baixada em diferentes sistemas operacionais pelo link a seguir: 

<https://git-scm.com/downloads> 

## Como Executar as Soluções

Para executar as soluções será necessário baixar a pasta TesteLogico do repositório e abrí-la no VsCode. 

### Pergunta 1

Dentro do programa clique no arquivo Pergunta 1, depois clique no indicador de versão, no canto inferior direito, e escolha na lista a versão de compilador que desejar, escolhido o compilador basta clicar no icone de "Play" no canto superior direito que o arquivo aberto será executado.

Lista de compiladores:

![Seleção do compilador](/imagens/compiilador.png)

Após clicar para executar o código o terminal aparecerá e mostrará a execução do código como na imagem abaixo:

![Execução da Pergunta 1](/imagens/execucao1.png)

### Pergunta 2

Dentro do programa clique no arquivo Pergunta 2, depois clique no icone de "Play" no canto superior direito que o arquivo aberto será executado.

![Execução da Pergunta 2 - parte 1](/imagens/execucao2-1.png)

Clique no terminal para digitar a palavra-chave a ser procurada e pressione a tecla Enter, então o resultado aparecerá.

No exemplo abaixo a palavra digitada foi "Goiaba", resultando no caminho percorrido até ela na árvore binária:

![Execução da Pergunta 2 - parte 2](/imagens/execucao2-2.png)

Ao executar o programa pela segunda vez a palavra "Mamão" foi digitada no terminal, porém ela não foi encontrada na árvore:
![Execução da Pergunta 2 - parte 3](/imagens/execucao2-3.png)


### Pergunta 3

Dentro do programa clique no arquivo Pergunta 3, depois clique no icone de "Play" no canto superior direito que o arquivo aberto será executado.

![Execução da Pergunta 3 - parte 1](/imagens/execucao3-1.png)

Clique no terminal para digitar a soma que deseja encontrar no array e pressione a tecla Enter, então o resultado aparecerá.

Neste exemplo o número digitado foi 10, e o resultado informado foi que a soma não existe dentro do array:

![Execução da Pergunta 3 - parte 2](/imagens/execucao3-2.png)

Neste segundo exemplo o número digitado foi 20, e o resultado informado foi que a soma existe dentro do array:

![Execução da Pergunta 3 - parte 3](/imagens/execucao3-3.png)

### Pergunta 4

Dentro do programa clique no arquivo Pergunta 4, depois clique no icone de "Play" no canto superior direito que o arquivo aberto será executado.

O terminal aparecerá e mostrará a execução do código como na imagem abaixo:

![Execução da Pergunta 4](/imagens/execucao4.png)


Caso encontre problemas acesse o link <https://code.visualstudio.com/docs/python/run> para mais informações sobre como executar um arquivo Python no Visual Studio Code.


## Desenvolvimento

Ao longo do desenvolvimento a ferramenta git foi utilizada para atualizar o codigo e manter o controle do versionamento, após a impelmentação da primeira pergunta foram realizados o primeiro commit e a criação do repositório no GitHub. 

A partir desse ponto os commits aconteceram de acordo com a constrtução solida de etapas da programação.

As alterações foram feitas diretamente na branch main e depois do desenvolvimento de todas as perguntas do teste foi realizado o push para o repositorio remoto.

### Ordem Cronológica

A seguir está descrito o processo de desenvolvimento de cada pergunta na ordem cronologica da implementação das soluções.

### Desenvolvimento da Pergunta 1

Para preservar a ordem dos números diferentes de 1 um pode ser implementado um método parecido com o algoritmo de ordenação inserção direta, um método simples de ordenação de dados que mantem os números já ordenados em suas posições relativas. 

Primeiro foi implementado o algoritmo, com o auxílio de pesquisas simples, de forma que ele ordenasse todos os números do array normalmente: 

![Codigo inicial da pergnta 1](/imagens/P1-1.png)

Sendo o resultado a ordenação padrão do menor ao maior número: 

![Resultado inicial da pergunta 1](/imagens/P1-2.png)

Com o resultado ordenado seria  necessário ajustar o algoritmo para movimentar apenas os números 1 para o início do array, então o nome da função foi mudado para umNaFrente, e a condição do laço de repetição while para que ele fosse executado apenas quando o valor de aux fosse 1, ou seja o número da posição atual a ser movimentado fosse um número 1:

![codigo modificado da pergunta 1](/imagens/P1-3.png)

Sendo o resultado todos os números 1 no início do array: 

![resulatdo modificado pergnta 1](/imagens/P1-4.png)

### Desenvolvimento da Pergunta 3

A ideia inicial foi percorrer o array subtraindo de x o primeiro valor do array por exemplo  e conferir  se o valor restante existe dentro do próprio array, caso exista quer dizer que o valor de x corresponde a uma soma existente entre os números. 

![codigo inicial pergunta 3](/imagens/P3-1.png)

Ao desenvolver a função ela apresentava resultados concretos porém com alguns desvios, por exemplo ao atribuir o valor 10 a x o retorno seria `True`, o que não deveria acontecer pois nenhuma soma feita com os números da array resultam em 10. 

O problema a ser corrigido é que quando o array é percorrido na busca do valor da diferença ele também  encontra o número que já faz parte da soma, fazendo com que o valor 10 retorne `True` devido a presença do número 5. 

Para resolver foi necessário fazer com que o laço de repetição que procura a diferença ignore o valor da atual posição do laço de repetição i. 

Então foi adicionada a condição que compara os valores de i e j , caso eles sejam iguais o laço que procura a diferença é pulado, e primeiro laço continua para o próximo valor: 

![codigo modificado pergunta 3](/imagens/P3-2.png)

Resultando em `False` quando valores como 30 (dobro de 15) e 10 (dobro de 5) são inseridos como parâmetro.

### Desenvolvimento da Pergunta 4

Primeiro foi desenvolvida uma função que apenas adiciona os números faltantes do array a partir do maior valor dentro dele: 

![codigo inicial pergunta 4](/imagens/P4-1.png)

Agora que os números que faltavam já estavam no array bastava ordená-lo. Para isso foi utilizazdo o mesmo algoritmo de ordenação implementado na primeira pergunta dentro da mesma função: 

![codigo modificado pergunta 4](/imagens/P4-2.png)

Resultando na adição dos números faltantes de 0 até o maior número do array em ordem crescente:

![Resultado pergunta 4](/imagens/P4-3.png)

### Desenvolvimento da Pergunta 2

Nessa pergunta foi utilizada a inteligencia artifical *Copilot*, da Microsoft, para elaboração da resposta.

O primeiro passo foi implementar uma forma de reperesentar a árvore binária de Strings fornecida, isso foi feito por meio da classe "No", que possui os atributos "valor", "esquerda", e "direita", eles armazenam respectivamente o valor do nó , o nó à esquerda e o nó à direita.

Estando criada a classe de nós, todos os nós da árvore foram criados e posicionados de acordo com as posições já fornecidas:

![Codigo inicial pergunta 2](/imagens/P2-1.png)

A proxíma etapa foi criar a função que recebe a árvore e a palavra-chave para busca, de início a função apenas retornava o o caminho do nó raiz "Maçã" e None caso o valor a ser buscado não existisse:

![Função inicial pergunta 2](/imagens/P2-2.png)

Para percorrer a árvore a recursividade foi utilizada por meio das variaveis direita e esquerda que recebem o valor do nó (nome da fruta) caso a palavra passada seja encontrada:

![Função modificada pergunta 2](/imagens/P2-3.png)

Após implementar a busca na árvore foram feitas as alterações para que a função retornasse não só o item encontrado, mas todo o caminho percorrido. Conforme a função chama ela mesma o caminho é formado, ao passar como parametro o caminho já percorrido e o valor do nó atual:

![Segunda modificação da função pergunta 2](/imagens/P2-4.png)

Por fim foi adicionada a entrada de dados que recebe a palavra-chave, e as mesnagens que informam o caminho ou uma mensagem de item não encontrado:

![Resultado 1 pergunta 2](/imagens/P2-5.png)
![Resultado 2 pergunta 2](/imagens/P2-6.png)

## Uso de IA

Durante o desenvolvimento do teste recursos de inteligência artificial foram pouco utilizados, como mencionado anteriormente o *Copilot* foi utilizado somente na pergunta 3 que implementa uma árvore binária de Strings. Porém, ao realizar buscas simples no Google como por exemplo sintaxes da linguagem Pyhton, foram aproveitadas as respostas fornecidas pelo *Gemini*, exibidas logo abaixo da pesquisa na própria página de resultado das buscas.

### Prompts e respostas utilizadas

O primeiro prompt enviado foi:

`como posso inserir essa arvore binaria no python`

Em conjunto com o anexo da árvore fornecida:

![Árvore binária fornecida](/imagens/arvore.png)

A resposta fornecida continha uma estrutura de classe, a criação dos nós e a montagem da árvore:

```python
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
```
Pórem o codigo dessa forma está incorreto, pois ao posicionar os filhos do nó "Pera" o codigo determina "Abacaxi" e "Laranja" como nós à esquerda e direita dele, o que não corresponde à imagem.

Então esse erro foi corrigido e implementando com o posicionamento correto da árvore.


O segundo Prompt enviado foi:

`como implementar essa função`

Junto com a imagem:

![Pergunta 22](/imagens/pergunta2.png)

A resposta recebida incluia o código:

```python
def buscar_com_caminho(no, palavra, caminho=""):
    if no is None:
        return None
    if no.valor == palavra:
        return caminho + no.valor
    # Tenta buscar na esquerda
    resultado_esquerda = buscar_com_caminho(no.esquerda, palavra, caminho + no.valor + " -> ")
    if resultado_esquerda:
        return resultado_esquerda
    # Tenta buscar na direita
    resultado_direita = buscar_com_caminho(no.direita, palavra, caminho + no.valor + " -> ")
    if resultado_direita:
        return resultado_direita
    return None
```

A partir dessa resposta a função foi implementada e testada em etapas como descrito anterirormente. Inicialmente ela retornava somente None ou o valor do primeiro nó, depois retornava apenas a palavra se ela fosse encontrada, e por fim todo o caminho até a palavra-chave.
