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


