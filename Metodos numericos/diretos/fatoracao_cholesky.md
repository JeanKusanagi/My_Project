# Fatoração de Cholesky - Exemplo 3x3

A **fatoração de Cholesky** (ou decomposição de Cholesky) é a decomposição de uma matriz simétrica e definida positiva em um produto de uma matriz triangular inferior e a sua transposta.

## Definição Matemática
Dada uma matriz $A$ simétrica e definida positiva, ela pode ser fatorada como:
$$A = L L^T$$
onde $L$ é uma matriz triangular inferior com elementos positivos na diagonal principal.

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
