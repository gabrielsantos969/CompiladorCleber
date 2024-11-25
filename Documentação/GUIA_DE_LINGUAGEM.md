# Guia de declarações

## Declarações de Variáveis

```
    cleber cleberInt idade = 12;
```
Descrição: Declara uma variável do tipo cleberInt (inteiro) chamada idade e a inicializa com o valor 12.


```
    cleber cleberString nome = "Gabriel";
```
Descrição: Declara uma variável do tipo cleberString (string) chamada nome e a inicializa com o valor "Gabriel".


```
    cleber cleberBool deMaior = "cleberFalso";
```
Descrição: Declara uma variável do tipo cleberBool (booleano) chamada deMaior e a inicializa com o valor cleberFalso.


```
    cleber cleberString nmPai;
```
Descrição: Declara uma variável do tipo cleberString (string) chamada nmPai sem inicializá-la.

## Atribuição de Valores

```
    nmPai = "João";
```
Descrição: Atribui o valor "João" à variável nmPai.

## Impressão de Valores

```
    cleberPrint(nmPai);
```
Descrição: Imprime o valor da variável nmPai.

## Declarações Condicionais

```
    cleberIf(1 == 1){
        cleberPrint("Declaração Igual");
    }
```
Descrição: Se a condição 1 == 1 for verdadeira, imprime "Declaração Igual".


```
    cleberIf(1 <= 1){
        cleberPrint("Declaração Menor ou Igual");
    }
```
Descrição: Se a condição 1 <= 1 for verdadeira, imprime "Declaração Menor ou Igual".


```
    cleberIf(1 >= 1){
        cleberPrint("Declaração Maior ou Igual");
    }
```
Descrição: Se a condição 1 >= 1 for verdadeira, imprime "Declaração Maior ou Igual".


```
    cleberIf(5 > 1){
        cleberPrint("Declaração Maior Que");
    }
```
Descrição: Se a condição 5 > 1 for verdadeira, imprime "Declaração Maior Que".


```
    cleberIf(1 < 5){
        cleberPrint("Declaração Menor Que");
    }
```
Descrição: Se a condição 1 < 5 for verdadeira, imprime "Declaração Menor Que".


```
    cleberIf(1 != 5){
        cleberPrint("Declaração Diferente de");
    }
```
Descrição: Se a condição 1 != 5 for verdadeira, imprime "Declaração Diferente de".

## Declarações Condicionais com Else

```
    cleberIf(1 == 2){
        cleberPrint("FOI");
    }cleberElse{
        cleberPrint("Não Foi");
    }
```
Descrição: Se a condição 1 == 2 for verdadeira, imprime "FOI"; caso contrário, imprime "Não Foi".

## Laço de Repetição For

```
    cleberFor(cleber cleberInt i = 0, i < 5, i = i + 1){
        cleberPrint(i);
    }
```
Descrição: Laço for que inicializa a variável i com 0, e enquanto i < 5 for verdadeiro, incrementa i em 1 a cada iteração e imprime o valor de i.

## Operações Aritméticas

```
    cleberPrint(1 + 1);
```
Descrição: Imprime o resultado da soma 1 + 1, que é 2.


```
    cleberPrint(2 - 1);
```
Descrição: Imprime o resultado da subtração 2 - 1, que é 1.


```
    cleberPrint(5 * 5);
```
Descrição: Imprime o resultado da multiplicação 5 * 5, que é 25.


```
    cleberPrint(10 / 2);
```
Descrição: Imprime o resultado da divisão 10 / 2, que é 5.