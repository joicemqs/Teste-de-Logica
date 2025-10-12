# Teste de Lógica

Essa é uma aplicação construída para resolver questões de lógica que envolvem arrays e árvore binária, a linguagem escolhida para desenvolvimento foi Python, pela facilidade tanto de aprendizado quanto pela simplicidade ao se trabalhar com arrays.

## Instalação

### 1. Instalação da linguagem de programação 
O instalador do Python pode ser baixado pelo site oficial tanto para Windows quanto para MacOS ou Linux em:

<https://www.python.org/downloads/>

Para usuários de Windows o Python pode ser instalado diretamente da Microsoft Store, forma recomendada para a maioria dos usuários segundo a própria página de download do site. 

Após instalação para consultar a versão instalada Podemos utilizar no cmd o comando: 

`python –version` 
 
 E em seguida a versão será exibida.

### 2. Instalação do Visual Studio Code e exytensões

Para executar os programas foi utilizado o software Visual Studio Code disponível para download em:

<https://code.visualstudio.com/download>

Foram necessárias duas extensões para rodar o código no programa,  a primeira delas é a extensão Python disponível na aba extensões na lateral esquerda: 

![Alt ou título da imagem](/imagens/extensao1.png)

A segunda extensão utilizada foi  a extensão Python Debugger também disponível na aba lateral: 

![Alt ou título da imagem](/imagens/extensao2.png)

### 3. Instalação do Git

Para controle do versionamento foi utilizada a ferrmaenta Git que pode ser baixada em diferentes sistemas operacionais pelo link seguir: 

<https://git-scm.com/downloads> 


## Desenvolvimento

Ao longo do desenvolvimento a ferramenta git foi utilizada para atualizar o codigo e manter o controle do versionamento, após a impelmentação da primeira pergunta foram realizados o primeiro commit e a criação do repositório no GitHub. 

A partir desse ponto os commits aconteceram de acordo com a constrtução solida de etapas da programação.

As alterações foram feitas diretamente a branch main e depois do desenvolvimento de todas as perguntas do teste foi realizado o push para o repositorio remoto e o merge.

### Desenvolvimento da Pergunta 1

Para preservar a ordem dos números diferentes de 1 um pode ser implementado um método parecido com o algoritmo de ordenação inserção direta, um método simples de ordenação de dados que mantem os números já ordenados em suas posições relativas. 

Primeiro foi implementado o algoritmo, com o auxílio de pesquisas simples, de forma que ele ordenasse todos os números do array normalmente: 

![Alt ou título da imagem](/imagens/P1-1.png)

Sendo o resultado a ordenação padrão do menor ao maior número: 

![Alt ou título da imagem](/imagens/P1-2.png)

Com o resultado ordenado seria  necessário ajustar o algoritmo para movimentar apenas os números 1 para o início do array, então o nome da função foi mudado para umNaFrente, e a condição do laço de repetição while para que ele fosse executado apenas quando o valor de aux fosse 1, ou seja o número da posição atual a ser movimentado fosse um número 1:

![Alt ou título da imagem](/imagens/P1-3.png)

Sendo o resultado todos os números 1 no início do array: 

![Alt ou título da imagem](/imagens/P1-4.png)

