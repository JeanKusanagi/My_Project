# Método de Eliminação de Gauss

O **Método de Eliminação de Gauss** (ou escalonamento) é um algoritmo da álgebra linear usado para resolver sistemas de equações lineares. 

O objetivo principal é transformar a matriz original dos coeficientes em uma **matriz triangular superior** (onde todos os elementos abaixo da diagonal principal são iguais a zero), facilitando o cálculo das variáveis.

---

## Como funciona o método

1. **Montagem da Matriz Aumentada**: Escreve-se o sistema de equações na forma de uma matriz combinando os coeficientes das variáveis e os termos independentes após o sinal de igual.
2. **Operações Elementares**: Utiliza-se três tipos de operações válidas para zerar os elementos abaixo da diagonal principal:
   * Trocar duas linhas de posição ($L_i \leftrightarrow L_j$).
   * Multiplicar uma linha por um número diferente de zero ($c \cdot L_i$).
   * Somar a uma linha um múltiplo de outra linha ($L_i + k \cdot L_j$).
3. **Substituição Retroativa (ou Regressiva)**: Após a matriz estar escalonada, a última equação terá apenas uma incógnita. Resolve-se de baixo para cima, substituindo os valores encontrados nas equações anteriores para achar todas as variáveis.

---

## Exemplo prático de cálculo

Para o sistema linear:
* $2x + y = 5$
* $x - y = 1$

1. **Matriz aumentada**:
   $$\begin{pmatrix} 2 & 1 & \vert{} & 5 \\ 1 & -1 & \vert{} & 1 \end{pmatrix}$$

2. **Escalonamento** (zerando o elemento abaixo do 2 na primeira coluna):
   * Nova linha 2 = Linha 2 - $(1/2) \times$ Linha 1
   $$\begin{pmatrix} 2 & 1 & \vert{} & 5 \\ 0 & -1.5 & \vert{} & -1.5 \end{pmatrix}$$

3. **Resolução por substituição**:
   * Da segunda linha: $-1.5y = -1.5 \implies y = 1$.
   * Da primeira linha: $2x + 1 = 5 \implies 2x = 4 \implies x = 2$.
   * **Solução**: $x = 2$ e $y = 1$.

---

## Diferença para o Método de Gauss-Jordan

* **Eliminação de Gauss**: Para na forma triangular superior e utiliza substituição retroativa para encontrar as incógnitas.
* **Gauss-Jordan**: Continua as operações elementares até transformar a matriz dos coeficientes em uma **matriz identidade** (com 1 na diagonal principal e 0 em todas as outras posições), fornecendo os resultados diretamente sem necessidade de substituição.

# Exemplo de Eliminação Gaussiana (Método de Gauss)

Este documento apresenta o passo a passo da **Eliminação Gaussiana** aplicada a um sistema linear $3 \times 3$ com solução única.

O objetivo deste método é transformar a matriz de coeficientes em uma **matriz triangular superior** (com zeros abaixo da diagonal principal) e depois encontrar as variáveis usando substituição regressiva (de baixo para cima).

---

## Sistema Linear Proposto

$$
\begin{cases} 
x + 2y + z = 8 \\ 
2x + y - z = 1 \\ 
-x + y - 2z = -7 
\end{cases}
$$

---

## Passo a Passo do Escalonamento

### Passo 1: Montar a matriz aumentada
Reunimos os coeficientes das variáveis e os termos independentes na mesma matriz:

$$
\begin{bmatrix} 
1 & 2 & 1 & \bigm\vert{} & 8 \\ 
2 & 1 & -1 & \bigm\vert{} & 1 \\ 
-1 & 1 & -2 & \bigm\vert{} & -7 
\end{bmatrix}
$$

### Passo 2: Zerar a primeira coluna (abaixo do pivô da Linha 1)
O pivô da primeira linha já vale $1$. Usaremos a Linha 1 ($L_1$) para zerar os elementos abaixo dela:
* **Substituição na Linha 2:** $L_2 \leftarrow L_2 - 2 \cdot L_1$
* **Substituição na Linha 3:** $L_3 \leftarrow L_3 + L_1$

$$
\begin{bmatrix} 
1 & 2 & 1 & \bigm\vert{} & 8 \\ 
\mathbf{0} & -3 & -3 & \bigm\vert{} & -15 \\ 
\mathbf{0} & 3 & -1 & \bigm\vert{} & 1 
\end{bmatrix}
$$

### Passo 3: Zerar a segunda coluna (abaixo do pivô da Linha 2)
Agora, precisamos zerar o elemento $3$ localizado na Linha 3, Coluna 2. Como o elemento correspondente na Linha 2 é $-3$, basta somar as duas linhas:
* **Substituição na Linha 3:** $L_3 \leftarrow L_3 + L_2$

$$
\begin{bmatrix} 
1 & 2 & 1 & \bigm\vert{} & 8 \\ 
0 & -3 & -3 & \bigm\vert{} & -15 \\ 
\mathbf{0} & \mathbf{0} & -4 & \bigm\vert{} & -14 
\end{bmatrix}
$$

---

## Fim do Escalonamento (Matriz Triangular Superior)

Note que na Eliminação Gaussiana tradicional nós **paramos aqui**. Não há necessidade de transformar os pivôs da diagonal principal em $1$, nem de zerar a parte superior da matriz. 

A matriz resultante tem o seguinte formato de equações:

1. $x + 2y + z = 8$
2. $-3y - 3z = -15$
3. $-4z = -14$

---

## Substituição Regressiva (De baixo para cima)

### 1. Encontrando $z$ (usando a Linha 3):
$$ -4z = -14 \implies z = \frac{-14}{-4} \implies \mathbf{z = 3.5} $$

### 2. Encontrando $y$ (usando a Linha 2):
Substituímos $z = 3.5$ na segunda equação:
$$ -3y - 3(3.5) = -15 $$
$$ -3y - 10.5 = -15 $$
$$ -3y = -15 + 10.5 $$
$$ -3y = -4.5 \implies y = \frac{-4.5}{-3} \implies \mathbf{y = 1.5} $$

### 3. Encontrando $x$ (usando a Linha 1):
Substituímos $y = 1.5$ e $z = 3.5$ na primeira equação:
$$ x + 2(1.5) + 3.5 = 8 $$
$$ x + 3 + 3.5 = 8 $$
$$ x + 6.5 = 8 \implies x = 8 - 6.5 \implies \mathbf{x = 1.5} $$

---

## Solução do Sistema
O sistema possui **solução única**:
* $\mathbf{x = 1.5}$
* $\mathbf{y = 1.5}$
* $\mathbf{z = 3.5}$
