# Método de Gauss-Jordan

O **método de Gauss-Jordan** é um algoritmo da álgebra linear usado para resolver sistemas de equações lineares e encontrar a matriz inversa. Ele é uma extensão da eliminação gaussiana.

## Conceito Principal

Enquanto a eliminação gaussiana transforma a matriz original em uma matriz triangular superior, o método de Gauss-Jordan vai além e a transforma em uma **matriz escalonada reduzida por linhas** (geralmente uma matriz identidade).

Ao alcançar o formato de matriz identidade do lado esquerdo de uma matriz aumentada, os valores das incógnitas ou os elementos da matriz inversa podem ser lidos diretamente no lado direito.

## Operações Elementares de Linha

Para manipulação da matriz aumentada, são permitidas apenas três operações:
1. **Permutação:** Trocar a posição de duas linhas ($L_i \leftrightarrow L_j$).
2. **Multiplicação:** Multiplicar todos os elementos de uma linha por um escalar não nulo ($L_i \leftarrow k \cdot L_i$, onde $k \neq 0$).
3. **Substituição:** Substituir uma linha pela soma dela mesma com o múltiplo de outra linha ($L_i \leftarrow L_i + k \cdot L_j$).

## Exemplo de Aplicação (Sistema 2x2)

Dado o sistema:
$$
\begin{cases} 
2x + y = 5 \\
x - 3y = -1 
\end{cases}
$$

### 1. Matriz Aumentada Inicial
$$
\left[
\begin{array}{cc|c}
2 & 1 & 5 \\
1 & -3 & -1
\end{array}
\right]
$$

### 2. Passo a Passo do Escalonamento

* **Trocar a Linha 1 com a Linha 2 ($L_1 \leftrightarrow L_2$)** para obter o pivô 1 na primeira linha:
$$
\left[
\begin{array}{cc|c}
1 & -3 & -1 \\
2 & 1 & 5
\end{array}
\right]
$$

* **Zerar o elemento abaixo do primeiro pivô ($L_2 \leftarrow L_2 - 2L_1$):**
$$
\left[
\begin{array}{cc|c}
1 & -3 & -1 \\
0 & 7 & 7
\end{array}
\right]
$$

* **Transformar o próximo pivô em 1 ($L_2 \leftarrow \frac{1}{7}L_2$):**
$$
\left[
\begin{array}{cc|c}
1 & -3 & -1 \\
0 & 1 & 1
\end{array}
\right]
$$

* **Zerar o elemento acima do novo pivô ($L_1 \leftarrow L_1 + 3L_2$):**
$$
\left[
\begin{array}{cc|c}
1 & 0 & 2 \\
0 & 1 & 1
\end{array}
\right]
$$

### 3. Resultado
A matriz à esquerda tornou-se a matriz identidade. A solução do sistema é lida diretamente na última coluna:
* **$x = 2$**
* **$y = 1$**

# Método de Gauss-Jordan: Exemplo Prático 3x3

Este documento apresenta a resolução passo a passo de um sistema linear de equações utilizando o **Método de Gauss-Jordan**. No final do processo, quando o sistema possui **solução única**, a matriz dos coeficientes transforma-se na **matriz identidade**.

---

## O Sistema Linear

Consideramos o seguinte sistema de 3 equações e 3 incógnitas:

$$
\begin{cases} 
x + 2y + z = 8 \\ 
2x + y - z = 1 \\ 
-x + y - 2z = -7 
\end{cases}
$$

---

## Resolução Passo a Passo

### Passo 1: Montar a Matriz Aumentada
Agrupamos os coeficientes das variáveis e os termos independentes em uma única matriz:

$$
\begin{bmatrix}
1 & 2 & 1 & \bigm\vert & 8 \\
2 & 1 & -1 & \bigm\vert & 1 \\
-x + 1 & 1 & -2 & \bigm\vert & -7
\end{bmatrix}
$$
*(Nota: A terceira linha corresponde aos coeficientes $[-1, 1, -2 \mid -7]$)*

$$
\begin{bmatrix}
1 & 2 & 1 & \bigm\vert & 8 \\
2 & 1 & -1 & \bigm\vert & 1 \\
-1 & 1 & -2 & \bigm\vert & -7
\end{bmatrix}
$$

### Passo 2: Zerar os elementos abaixo do primeiro pivô (Coluna 1)
O pivô da primeira linha e primeira coluna já é igual a **1**. Usamos a Linha 1 ($L_1$) para zerar os elementos abaixo dele:
* $L_2 \leftarrow L_2 - 2 \cdot L_1$
* $L_3 \leftarrow L_3 + L_1$

$$
\begin{bmatrix}
1 & 2 & 1 & \bigm\vert & 8 \\
0 & -3 & -3 & \bigm\vert & -15 \\
0 & 3 & -1 & \bigm\vert & 1
\end{bmatrix}
$$

### Passo 3: Criar o segundo pivô (Linha 2, Coluna 2)
Dividimos a Linha 2 por $-3$ para obtermos o pivô igual a **1**:
* $L_2 \leftarrow \frac{L_2}{-3}$

$$
\begin{bmatrix}
1 & 2 & 1 & \bigm\vert & 8 \\
0 & 1 & 1 & \bigm\vert & 5 \\
0 & 3 & -1 & \bigm\vert & 1
\end{bmatrix}
$$

### Passo 4: Zerar os elementos na Coluna 2 (Acima e Abaixo do pivô)
Utilizamos a Linha 2 ($L_2$) para limpar a segunda coluna:
* $L_1 \leftarrow L_1 - 2 \cdot L_2$
* $L_3 \leftarrow L_3 - 3 \cdot L_2$

$$
\begin{bmatrix}
1 & 0 & -1 & \bigm\vert & -2 \\
0 & 1 & 1 & \bigm\vert & 5 \\
0 & 0 & -4 & \bigm\vert & -14
\end{bmatrix}
$$

### Passo 5: Criar o terceiro pivô (Linha 3, Coluna 3)
Dividimos a Linha 3 por $-4$ para obtermos o pivô igual a **1**:
* $L_3 \leftarrow \frac{L_3}{-4}$

$$
\begin{bmatrix}
1 & 0 & -1 & \bigm\vert & -2 \\
0 & 1 & 1 & \bigm\vert & 5 \\
0 & 0 & 1 & \bigm\vert & 3.5
\end{bmatrix}
$$

### Passo 6: Zerar os elementos acima do terceiro pivô (Coluna 3)
Utilizamos a Linha 3 ($L_3$) para finalizar o escalonamento reduzido:
* $L_1 \leftarrow L_1 + L_3$
* $L_2 \leftarrow L_2 - L_3$

$$
\begin{bmatrix}
1 & 0 & 0 & \bigm\vert & 1.5 \\
0 & 1 & 0 & \bigm\vert & 1.5 \\
0 & 0 & 1 & \bigm\vert & 3.5
\end{bmatrix}
$$

---

## Conclusão e Resultado

Como o sistema possui uma **solução única**, o lado esquerdo da matriz foi completamente transformado na **Matriz Identidade $3 \times 3$**.

A leitura dos valores resultantes na coluna da direita nos dá diretamente o conjunto solução:
* **$x = 1.5$**
* **$y = 1.5$**
* **$z = 3.5$**
