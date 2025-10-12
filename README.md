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

### Ordem Cronológica

A seguir está descrito o processo de desenvolvimento de cada pergunta exatamente na ordem cronologica da implementação das soluções.

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

### Desenvolvimento da Pergunta 3

A ideia inicial foi percorrer o array subtraindo de x o primeiro valor do array por exemplo  e conferir  se o valor restante existe dentro do próprio array, caso exista quer dizer que o valor de x corresponde a uma soma existente entre os números. 

![Alt ou título da imagem](/imagens/P3-1.png)

Ao desenvolver a função ela apresentava resultados concretos porém com alguns desvios, por exemplo ao atribuir o valor 10 a x o retorno seria `True`, o que não deveria acontecer pois nenhuma soma feita com os números da array resultam em 10. 

O problema a ser corrigido é que quando o array é percorrido na busca do valor da diferença ele também  encontra o número que já faz parte da soma, fazendo com que o valor 10 retorne `True` devido a presença do número 5. 

Para resolver foi necessário fazer com que o laço de repetição que procura a diferença ignore o valor da atual posição do laço de repetição i. 

Então foi adicionada a condição que compara os valores de i e j , caso eles sejam iguais o laço que procura a diferença é pulado, e primeiro laço continua para o próximo valor: 

![Alt ou título da imagem](/imagens/P3-2.png)

Resultando em `False` quando valores como 30 (dobro de 15) e 10 (dobro de 5) são inseridos como parâmetro.

### Desenvolvimento da Pergunta 4

Primeiro foi desenvolvida uma função que apenas adiciona os números faltantes do array a partir do maior valor dentro dele: 

![Alt ou título da imagem](/imagens/P4-1.png)

Agora que os números que faltavam já estavam no array bastava ordená-lo. Para isso foi utilizazdo o mesmo algoritmo de ordenação implementado na primeira pergunta dentro da mesma função: 

![Alt ou título da imagem](/imagens/P4-2.png)

Resultando na adição dos números faltantes de 0 até o maior número do array em ordem crescente:

![Alt ou título da imagem](/imagens/P4-3.png)





