## Explicação do Lexer do Compilador Cleber

O código apresentado define o lexer (analisador léxico) do compilador para a linguagem Cleber, utilizando a biblioteca `ply.lex` do Python. O lexer é responsável por dividir o código-fonte em tokens, que são unidades básicas de significado para o compilador.

**1. Definição de Tokens:**

* A lista `tokens` define os tipos de tokens que o lexer irá reconhecer. Cada token representa um elemento da linguagem Cleber, como palavras-chave, operadores, identificadores, números, strings e booleanos.

**2. Funções de Reconhecimento de Tokens:**

* **`t_IFCLEBER`, `t_ELSECLEBER`, `t_CLEBER`, `t_CLEBERINT`, `t_CLEBERSTRING`, `t_CLEBERBOOL`, `t_CLEBERPRINT`:** Reconhecem as palavras-chave da linguagem Cleber, como `ifCleber`, `elseCleber`, `cleber`, `cleberInt`, `cleberString`, `cleberBool` e `cleberPrint`.
* **`t_IDENTIFIER`:** Reconhece identificadores, que são nomes de variáveis, funções e outras entidades.
* **`t_STRING`:** Reconhece strings literais, que são sequências de caracteres entre aspas duplas. O código trata de sequências de escape e converte a string para UTF-8.
* **`t_INTEGER`:** Reconhece números inteiros.
* **`t_BOOLEAN`:** Reconhece valores booleanos (`cleberVerdadeiro` e `cleberFalso`).
* **`t_ASSIGN`, `t_SEMICOLON`, `t_LPAREN`, `t_RPAREN`, `t_LBRACE`, `t_RBRACE`, `t_PLUS`, `t_MINUS`, `t_TIMES`, `t_DIVIDE`, `t_EQUALS`, `t_GREATER`, `t_LESS`, `t_GTE`, `t_LTE`, `t_NOTEQUAL`:** Reconhecem os operadores da linguagem Cleber.

**3. Ignorar Caracteres:**

* **`t_ignore`:** Define os caracteres que devem ser ignorados pelo lexer, como espaços, tabulações e quebras de linha.

**4. Tratamento de Erros:**

* **`t_error`:** Define o comportamento do lexer ao encontrar um caractere inválido. Imprime uma mensagem de erro e pula o caractere.

**5. Criar o Lexer:**

* **`lexer = lex.lex()`:** Cria o objeto lexer a partir das definições de tokens e regras.

**6. Função de Teste:**

* **`test_lexer(data)`:** Função para testar o lexer com um trecho de código e imprimir os tokens reconhecidos.

**Em resumo, o lexer é a primeira etapa do processo de compilação, responsável por transformar o código-fonte em uma sequência de tokens que o analisador sintático (parser) irá interpretar para gerar o código de máquina final.**
