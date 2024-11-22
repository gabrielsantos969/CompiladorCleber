# Parser do Compilador Cleber

Este repositório contém a implementação do parser do compilador para a linguagem Cleber, utilizando a biblioteca `ply.yacc` do Python. O parser é responsável por analisar a sequência de tokens gerada pelo lexer e verificar se o código-fonte segue a gramática da linguagem Cleber.

## Descrição

O parser transforma o código-fonte da linguagem Cleber, que foi dividido em tokens pelo lexer, em uma árvore de análise sintática. Ele verifica se o código segue as regras gramaticais definidas e gera uma estrutura de dados que pode ser usada para a execução ou geração de código.

## Funcionalidades

### 1. Definição de Regras Gramaticais

O parser é construído com base em regras gramaticais que descrevem a sintaxe da linguagem Cleber. Cada regra é definida por uma função que usa a biblioteca `ply.yacc` para mapear a estrutura das expressões e declarações da linguagem.

### 2. Regras Gramaticais

As principais regras gramaticais da linguagem Cleber incluem:

- **Programas** consistem em uma lista de instruções.
- **Instruções** podem ser declarações, atribuições, impressões ou instruções condicionais (`if` e `else`).
- **Declarações** podem ser de variáveis, com ou sem atribuição inicial.
- **Atribuições** são feitas para variáveis.
- **Instruções `if`** verificam condições e podem incluir um bloco `else`.
- **Expressões** podem ser operações aritméticas ou comparações.

### 3. Funções de Análise Sintática

As funções de análise sintática implementam as regras gramaticais da linguagem Cleber. Cada função corresponde a uma produção da gramática e descreve como um determinado tipo de instrução ou expressão deve ser estruturado.

Exemplos de funções de análise sintática:

- **`p_program(p)`**: Define um programa como uma lista de instruções.
- **`p_statement_list(p)`**: Define uma lista de instruções, que pode ser composta por uma ou mais instruções.
- **`p_if_statement(p)`**: Define a sintaxe para uma instrução condicional `if`.
- **`p_else_statement(p)`**: Define a sintaxe para a instrução `else`, podendo ser um bloco ou vazio.
- **`p_declaration(p)`**: Define a sintaxe para declarações de variáveis.
- **`p_assignment(p)`**: Define a sintaxe para atribuições de valores a variáveis.
- **`p_print_statement(p)`**: Define a sintaxe para imprimir valores.
- **`p_expression(p)`**: Define as expressões possíveis na linguagem, como operações aritméticas e comparações.
- **`p_value(p)`**: Define os tipos de valores que podem ser usados em expressões (inteiros, strings, booleanos, identificadores).
- **`p_type(p)`**: Define os tipos de dados suportados pela linguagem (inteiros, strings, booleanos).

### 4. Tratamento de Erros

O parser também possui um mecanismo de tratamento de erros para quando uma entrada não segue a gramática definida. A função **`p_error(p)`** imprime uma mensagem de erro detalhada indicando a posição e o tipo do erro encontrado.

### 5. Construção do Parser

O parser é criado a partir das regras gramaticais definidas, utilizando a função `yacc.yacc()`:

```python
parser = yacc.yacc()
```