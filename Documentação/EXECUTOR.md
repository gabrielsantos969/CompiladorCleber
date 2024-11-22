# Executor do Compilador Cleber

Este repositório contém a implementação do executor para o compilador da linguagem Cleber. O executor é responsável por executar o código-fonte já analisado pelo parser, manipulando variáveis e realizando operações, como atribuições, impressões e condições.

## Descrição

O executor processa uma lista de instruções (representadas como tuplas), que podem incluir declarações de variáveis, atribuições, operações matemáticas, comparações e impressões. O programa é executado com base em um conjunto de instruções, utilizando um dicionário para armazenar o estado das variáveis e avaliando expressões conforme necessário.

## Funcionalidades

### 1. Execução de Programa

A função principal do executor, `execute_program`, recebe um programa e executa cada instrução. Se o programa for válido (não for `None`), ele irá processar todas as instruções do programa. Caso contrário, uma mensagem de erro será exibida.

### 2. Execução de Instruções

A função `execute_statement` processa cada instrução individualmente, lidando com diferentes tipos de comandos no programa:

- **Declaração de Variáveis**: Quando uma variável é declarada, ela é armazenada no dicionário `variables` com o tipo e o valor inicial (se houver). Isso permite que as variáveis sejam utilizadas nas instruções subsequentes.
  
- **Atribuição de Valor**: Quando uma instrução de atribuição é encontrada, o executor atualiza o valor da variável correspondente, se ela já foi declarada previamente. Se a variável não for encontrada no dicionário, um erro é gerado.
  
- **Impressão de Valores**: O executor processa instruções de impressão, avaliando a expressão fornecida e exibindo o resultado no console. Isso pode incluir variáveis, operações matemáticas ou textos diretamente fornecidos.

- **Condição `if`**: O executor verifica expressões condicionais, avaliando a condição especificada. Se a condição for verdadeira, o bloco de código associado ao `if` é executado. Caso contrário, o bloco `else` (se presente) será executado.

### 3. Execução de Blocos

Blocos de código, como aqueles presentes em condições `if`, são executados pela função `execute_block`. Essa função recebe uma lista de instruções e executa cada uma delas individualmente.

### 4. Avaliação de Expressões

A função `evaluate_expression` é responsável por avaliar as expressões utilizadas nas instruções. Isso pode envolver:

- **Operações Matemáticas**: Como soma, subtração, multiplicação e divisão.
  
- **Comparações**: Como igualdade, maior que, menor que e outras comparações relacionais.
  
- **Variáveis e Valores**: Quando a expressão é uma variável ou um valor constante, a função retorna o valor correspondente.

- **Valores Lógicos**: Expressões podem incluir valores lógicos como `cleberVerdadeiro` e `cleberFalso`.

A função também lida com strings, números inteiros e operadores lógicos, garantindo que todas as operações e expressões sejam corretamente avaliadas.

## Estrutura de Dados

O executor usa o dicionário `variables` para armazenar o estado das variáveis. Cada variável é armazenada como uma tupla contendo seu tipo e seu valor. Isso permite que o executor faça verificações de tipo e atualize valores conforme necessário.

## Conclusão

O executor Cleber oferece uma implementação básica para interpretar e executar programas escritos na linguagem Cleber. Ele é capaz de manipular variáveis, realizar operações matemáticas e lógicas, e executar blocos condicionais de forma eficiente.
