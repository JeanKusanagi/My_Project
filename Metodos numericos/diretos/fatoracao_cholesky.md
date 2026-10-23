# Fatoração de Cholesky

A **fatoração de Cholesky** (ou decomposição de Cholesky) é uma técnica da álgebra linear que decompõe uma matriz hermitiana, simétrica e **positiva-definida** no produto de uma matriz triangular inferior e sua transposta (or transposta conjugada).

## Condições de Aplicação
* **Simétrica:** A matriz $A$ deve ser igual à sua transposta ($A = A^T$).
* **Positiva-definida:** Todos os seus menores principais devem ter determinantes estritamente positivos (ou $x^TAx > 0$ para todo vetor $x \neq 0$).

## Formulação Matemática
Para uma matriz real $A$, a decomposição de Cholesky é dada por:

$$A = L L^T$$

Onde:
* $L$ é uma **matriz triangular inferior** com elementos positivos na diagonal principal.
* $L^T$ é a matriz transposta de $L$.

## Principais Vantagens
* **Eficiência:** É aproximadamente **duas vezes mais rápida** do que a decomposição LU tradicional para resolver sistemas de equações lineares.
* **Menor custo computacional:** Requer cerca de $\frac{n^3}{3}$ operações, reduzindo o esforço pela metade em comparação com outros métodos diretos.

---

## Exemplo Numérico Passo a Passo

Vamos realizar a fatoração para a seguinte matriz simétrica e positiva-definida de ordem $3 \times 3$:

$$A = \begin{pmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{pmatrix}$$

O objetivo é encontrar uma matriz triangular inferior $L$ tal que $A = L L^T$:

$$\begin{pmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{pmatrix} = \begin{pmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{pmatrix} \begin{pmatrix} l_{11} & l_{21} & l_{31} \\ 0 & l_{22} & l_{32} \\ 0 & 0 & l_{33} \end{pmatrix}$$

### Passo 1: Calculando a Primeira Coluna de $L$
* **Elemento $l_{11}$:** 
  $$l_{11}^2 = a_{11} \implies l_{11}^2 = 4 \implies l_{11} = \sqrt{4} = 2$$
* **Elemento $l_{21}$:**
  $$l_{21} \cdot l_{11} = a_{21} \implies l_{21} \cdot 2 = 12 \implies l_{21} = \frac{12}{2} = 6$$
* **Elemento $l_{31}$:**
  $$l_{31} \cdot l_{11} = a_{31} \implies l_{31} \cdot 2 = -16 \implies l_{31} = \frac{-16}{2} = -8$$

Matriz parcial:
$$L = \begin{pmatrix} 2 & 0 & 0 \\ 6 & l_{22} & 0 \\ -8 & l_{32} & l_{33} \end{pmatrix}$$

### Passo 2: Calculando a Segunda Coluna de $L$
* **Elemento $l_{22}$:**
  $$l_{21}^2 + l_{22}^2 = a_{22} \implies 6^2 + l_{22}^2 = 37 \implies 36 + l_{22}^2 = 37 \implies l_{22} = \sqrt{1} = 1$$
* **Elemento $l_{32}$:**
  $$(l_{31} \cdot l_{21}) + (l_{32} \cdot l_{22}) = a_{32} \implies ((-8) \cdot 6) + (l_{32} \cdot 1) = -43$$
  $$-48 + l_{32} = -43 \implies l_{32} = -43 + 48 = 5$$

Matriz parcial:
$$L = \begin{pmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & l_{33} \end{pmatrix}$$

### Passo 3: Calculando a Terceira Coluna de $L$
* **Elemento $l_{33}$:**
  $$l_{31}^2 + l_{32}^2 + l_{33}^2 = a_{33} \implies (-8)^2 + 5^2 + l_{33}^2 = 98$$
  $$64 + 25 + l_{33}^2 = 98 \implies 89 + l_{33}^2 = 98 \implies l_{33} = \sqrt{9} = 3$$

### Matriz Resultante $L$
$$L = \begin{pmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{pmatrix}$$

---

## Resolução de um Sistema de Equações Lineares ($Ax = b$)

Aproveitando que $A = LL^T$, dividimos o sistema em duas etapas triangulares rápidas:
1. **Substituição para frente:** Resolver $Ly = b$
2. **Substituição para trás:** Resolver $L^Tx = y$

Definindo o vetor de termos independentes $b = \begin{pmatrix} 4 \\ 22 \\ -23 \end{pmatrix}$:

### 1. Resolver $Ly = b$
$$\begin{pmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 22 \\ -23 \end{pmatrix}$$

* **Linha 1:** $2y_1 = 4 \implies y_1 = 2$
* **Linha 2:** $6y_1 + y_2 = 22 \implies 6(2) + y_2 = 22 \implies y_2 = 10$
* **Linha 3:** $-8y_1 + 5y_2 + 3y_3 = -23 \implies -8(2) + 5(10) + 3y_3 = -23$
  $$-16 + 50 + 3y_3 = -23 \implies 34 + 3y_3 = -23 \implies 3y_3 = -57 \implies y_3 = -19$$

Vetor intermediário: $y = \begin{pmatrix} 2 \\ 10 \\ -19 \end{pmatrix}$

### 2. Resolver $L^Tx = y$
$$\begin{pmatrix} 2 & 6 & -8 \\ 0 & 1 & 5 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 2 \\ 10 \\ -19 \end{pmatrix}$$

* **Linha 3:** $3x_3 = -19 \implies x_3 = -\frac{19}{3}$
* **Linha 2:** $x_2 + 5x_3 = 10 \implies x_2 + 5\left(-\frac{19}{3}\right) = 10 \implies x_2 - \frac{95}{3} = \frac{30}{3} \implies x_2 = \frac{125}{3}$
* **Linha 1:** $2x_1 + 6x_2 - 8x_3 = 2 \implies 2x_1 + 6\left(\frac{125}{3}\right) - 8\left(-\frac{19}{3}\right) = 2$
  $$2x_1 + 250 + \frac{152}{3} = 2 \implies 2x_1 = 2 - 250 - \frac{152}{3} = -248 - \frac{152}{3} = -\frac{896}{3}$$
  $$x_1 = -\frac{448}{3}$$

### Vetor Solução Final $x$
$$x = \begin{pmatrix} -\frac{448}{3} \\ \frac{125}{3} \\ -\frac{19}{3} \end{pmatrix} \approx \begin{pmatrix} -149.33 \\ 41.67 \\ -6.33 \end{pmatrix}$$

---

## Exemplo Prático com Matriz 3x3

Vamos fatorar a seguinte matriz $A$:
$$A = \begin{bmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{bmatrix}$$

Queremos encontrar $L$ tal que:
$$\begin{bmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{bmatrix} = \begin{bmatrix} L_{11} & 0 & 0 \\ L_{21} & L_{22} & 0 \\ L_{31} & L_{32} & L_{33} \end{bmatrix} \begin{bmatrix} L_{11} & L_{21} & L_{31} \\ 0 & L_{22} & L_{32} \\ 0 & 0 & L_{33} \end{bmatrix}$$

### Passo 1: Primeira coluna de $L$
* **$L_{11}$** (diagonal):
  $$L_{11} = \sqrt{A_{11}} = \sqrt{4} = 2$$
* **$L_{21}$**:
  $$L_{21} = \frac{A_{21}}{L_{11}} = \frac{12}{2} = 6$$
* **$L_{31}$**:
  $$L_{31} = \frac{A_{31}}{L_{11}} = \frac{-16}{2} = -8$$

### Passo 2: Segunda coluna de $L$
* **$L_{22}$** (diagonal):
  $$L_{22} = \sqrt{A_{22} - L_{21}^2} = \sqrt{37 - 6^2} = \sqrt{37 - 36} = \sqrt{1} = 1$$
* **$L_{32}$**:
  $$L_{32} = \frac{A_{32} - (L_{31} \cdot L_{21})}{L_{22}} = \frac{-43 - (-8 \cdot 6)}{1} = \frac{-43 + 48}{1} = 5$$

### Passo 3: Terceira coluna de $L$
* **$L_{33}$** (diagonal):
  $$L_{33} = \sqrt{A_{33} - (L_{31}^2 + L_{32}^2)} = \sqrt{98 - ((-8)^2 + 5^2)} = \sqrt{98 - (64 + 25)} = \sqrt{9} = 3$$

---

## Resultado Final

A matriz **$L$** e sua transposta **$L^T$** são:

$$L = \begin{bmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{bmatrix}, \quad L^T = \begin{bmatrix} 2 & 6 & -8 \\ 0 & 1 & 5 \\ 0 & 0 & 3 \end{bmatrix}$$
