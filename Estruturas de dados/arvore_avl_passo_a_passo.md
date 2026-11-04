# Construção e atualização de uma árvore AVL

Este material apresenta, passo a passo, a inserção dos valores
`10, 20, 30, 40 e 25` em uma árvore AVL, seguida da remoção dos valores
`30` e `10`.

## 1. Conceitos fundamentais

Uma **árvore AVL** é uma árvore binária de busca autobalanceada. Após
cada inserção ou remoção, verifica-se se a árvore continua balanceada.
Caso necessário, são realizadas rotações.

Neste material, o fator de balanceamento é definido por:

\[ FB(n) = altura(esquerda(n)) - altura(direita(n)) \]

Uma árvore AVL está balanceada quando todos os nós apresentam:

\[ FB(n) `\in `{=tex}{-1, 0, +1} \]

Convenção de altura: uma árvore vazia tem altura `-1` e uma folha tem
altura `0`.

## 2. Inserção dos valores 10, 20, 30, 40 e 25

### Passo 1 --- Inserir 10

Como a árvore está vazia, `10` torna-se a raiz.

``` text
10
```

Fator de balanceamento:

-   `FB(10) = 0`

A árvore está balanceada.

### Passo 2 --- Inserir 20

Como `20 > 10`, o novo nó é inserido à direita de 10.

``` text
10
  \
   20
```

Fatores de balanceamento:

-   `FB(20) = 0`
-   `FB(10) = -1`

A árvore continua balanceada. Nenhuma rotação é necessária.

### Passo 3 --- Inserir 30

Como `30 > 10` e `30 > 20`, o novo nó é inserido à direita de 20.

Antes do balanceamento:

``` text
10
  \
   20
     \
      30
```

Fatores de balanceamento:

-   `FB(30) = 0`
-   `FB(20) = -1`
-   `FB(10) = -2`

O nó 10 está desbalanceado. A inserção ocorreu na subárvore direita do
filho direito, caracterizando o caso **RR (Right-Right)**.

**Correção: rotação simples à esquerda no nó 10.**

Após a rotação:

``` text
    20
   /  \
 10    30
```

Agora, os fatores de balanceamento dos três nós são iguais a zero.

### Passo 4 --- Inserir 40

Como `40 > 20` e `40 > 30`, o novo nó é inserido à direita de 30.

``` text
    20
   /  \
 10    30
         \
          40
```

Fatores de balanceamento:

-   `FB(10) = 0`
-   `FB(40) = 0`
-   `FB(30) = -1`
-   `FB(20) = -1`

A árvore continua balanceada. Nenhuma rotação é necessária.

### Passo 5 --- Inserir 25

A busca pela posição de inserção segue este caminho:

-   `25 > 20`: segue para a direita;
-   `25 < 30`: segue para a esquerda.

Assim, 25 é inserido como filho esquerdo de 30.

``` text
       20
      /  \
    10    30
         /  \
        25   40
```

Fatores de balanceamento:

-   `FB(10) = 0`
-   `FB(25) = 0`
-   `FB(40) = 0`
-   `FB(30) = 0`
-   `FB(20) = -1`

A árvore continua balanceada. Nenhuma rotação é necessária.

### Resultado após as inserções

``` text
       20
      /  \
    10    30
         /  \
        25   40
```

A única rotação realizada durante as inserções foi a rotação simples à
esquerda no nó 10, após a inserção de 30.

## 3. Remoção do valor 30

Partimos da árvore:

``` text
       20
      /  \
    10    30
         /  \
        25   40
```

### Passo 1 --- Localizar o nó 30

O nó 30 possui dois filhos: 25 à esquerda e 40 à direita.

Quando um nó com dois filhos é removido de uma árvore binária de busca,
uma possibilidade é substituí-lo pelo seu **sucessor em ordem**, isto é,
o menor valor da sua subárvore direita.

Nesse caso, o sucessor em ordem de 30 é 40.

### Passo 2 --- Substituir 30 por 40

O valor 40 assume a posição de 30. O nó original 40 é então removido de
sua posição anterior.

``` text
       20
      /  \
    10    40
         /
        25
```

### Passo 3 --- Verificar o balanceamento

  Nó     Altura da esquerda   Altura da direita   FB
  ---- -------------------- ------------------- ----
  10                     -1                  -1    0
  25                     -1                  -1    0
  40                      0                  -1   +1
  20                      0                   1   -1

Todos os fatores estão no intervalo permitido, `[-1, +1]`.

Portanto, **nenhuma rotação é necessária**.

### Resultado após remover 30

``` text
       20
      /  \
    10    40
         /
        25
```

## 4. Remoção do valor 10

Agora partimos da árvore resultante da remoção de 30:

``` text
       20
      /  \
    10    40
         /
        25
```

### Passo 1 --- Localizar e remover o nó 10

O nó 10 é uma folha, pois não possui filhos. Portanto, basta removê-lo.

Após a remoção:

``` text
       20
         \
          40
         /
        25
```

### Passo 2 --- Verificar o balanceamento

  Nó     Altura da esquerda   Altura da direita   FB
  ---- -------------------- ------------------- ----
  25                     -1                  -1    0
  40                      0                  -1   +1
  20                     -1                   1   -2

O nó 20 está desbalanceado:

\[ FB(20) = -1 - 1 = -2 \]

Seu filho direito, o nó 40, apresenta:

\[ FB(40) = +1 \]

Como o nó desbalanceado está pesado à direita e seu filho direito está
pesado à esquerda, temos o caso **RL (Right-Left)**.

A correção exige uma rotação dupla: primeiro à direita no filho direito
e depois à esquerda no nó desbalanceado.

### Passo 3 --- Primeira rotação: rotação à direita no nó 40

A subárvore com raiz em 40 é rotacionada à direita. O nó 25 passa a
ocupar a posição de 40, e 40 torna-se seu filho direito.

``` text
    20
      \
       25
         \
          40
```

### Passo 4 --- Segunda rotação: rotação à esquerda no nó 20

Agora realizamos uma rotação à esquerda no nó 20. O nó 25 torna-se a
nova raiz da árvore.

``` text
       25
      /  \
    20    40
```

### Passo 5 --- Verificar o balanceamento final

  Nó     Altura da esquerda   Altura da direita   FB
  ---- -------------------- ------------------- ----
  20                     -1                  -1    0
  40                     -1                  -1    0
  25                      0                   0    0

Todos os nós estão balanceados.

### Resultado após remover 10

``` text
       25
      /  \
    20    40
```

A remoção de 10 provocou um desbalanceamento no nó 20, corrigido por uma
rotação dupla RL.

## 5. Resumo das operações

  -----------------------------------------------------------------------
  Operação                Situação                Balanceamento
  ----------------------- ----------------------- -----------------------
  Inserir 10              Criação da raiz         Nenhuma rotação

  Inserir 20              Inserção à direita de   Nenhuma rotação
                          10                      

  Inserir 30              Caso RR no nó 10        Rotação simples à
                                                  esquerda em 10

  Inserir 40              Inserção à direita de   Nenhuma rotação
                          30                      

  Inserir 25              Inserção à esquerda de  Nenhuma rotação
                          30                      

  Remover 30              Nó com dois filhos;     Nenhuma rotação
                          substituição pelo       
                          sucessor 40             

  Remover 10              Remoção de uma folha;   Rotação à direita em 40
                          caso RL no nó 20        e, depois, à esquerda
                                                  em 20
  -----------------------------------------------------------------------

## 6. Os quatro casos de desbalanceamento AVL

  -----------------------------------------------------------------------
  Caso                    Onde ocorre a inserção  Rotação corretiva
                          (ou o aumento de        
                          altura)                 
  ----------------------- ----------------------- -----------------------
  LL (Left-Left)          Subárvore esquerda do   Simples à direita
                          filho esquerdo          

  RR (Right-Right)        Subárvore direita do    Simples à esquerda
                          filho direito           

  LR (Left-Right)         Subárvore direita do    Dupla: esquerda no
                          filho esquerdo          filho e direita no nó
                                                  desbalanceado

  RL (Right-Left)         Subárvore esquerda do   Dupla: direita no filho
                          filho direito           e esquerda no nó
                                                  desbalanceado
  -----------------------------------------------------------------------

**Observação:** durante uma remoção, o desbalanceamento pode propagar-se
para os ancestrais. Por isso, pode ser necessário realizar rotações em
mais de um nível da árvore.

## 7. Complexidade

Em uma árvore AVL, a altura é `O(log n)`. Consequentemente, as operações
de busca, inserção e remoção possuem complexidade de tempo:

\[ `\boxed{O(\log n)}`{=tex} \]

As rotações são operações locais e possuem custo `O(1)` cada. O custo
total da atualização permanece `O(log n)`, pois pode ser necessário
percorrer o caminho entre o nó alterado e a raiz.
