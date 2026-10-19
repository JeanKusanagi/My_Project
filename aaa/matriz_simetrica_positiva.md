# Matrizes Simétricas Definidas Positivas e Fatoração de Cholesky

Uma **matriz simétrica definida positiva** é uma matriz quadrada $A$ que é igual à sua transposta ($A = A^T$) e cumpre a condição de que a sua forma quadrática é estritamente positiva para qualquer vetor não nulo, ou seja, $x^T A x > 0$ para todo $x \neq 0$.

---

## 1. Condições Equivalentes
Uma matriz simétrica $A$ de ordem $n \times n$ é definida positiva se, e somente se, atender a qualquer um dos seguintes critérios:

* **Autovalores positivos:** Todos os autovalores ($\lambda_i$) de $A$ são estritamente maiores que zero ($\lambda_i > 0$).
* **Critério de Sylvester (Menores Principais Líderes):** Os determinantes de todas as submatrizes superiores esquerdas $k \times k$ (com $k = 1, \dots, n$) são estritamente positivos.
* **Fatoração de Cholesky:** A matriz pode ser decomposta unicamente na forma $A = L L^T$, onde $L$ é uma matriz triangular inferior com elementos da diagonal estritamente positivos.
* **Pivôs positivos:** Todos os pivôs resultantes da eliminação gaussiana sem troca de linhas são positivos.

---

## 2. Exemplo 1: Verificação Completa (Matriz $2 \times 2$)

Seja a matriz simétrica $A$:
$$A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

### A. Teste dos Menores Principais Líderes
* **$D_1$** (submatriz $1 \times 1$): $\det(2) = \mathbf{2 > 0}$
* **$D_2$** (submatriz $2 \times 2$): $\det(A) = (2 \times 2) - (-1 \times -1) = 4 - 1 = \mathbf{3 > 0}$
Como ambos os determinantes são positivos, a matriz é definida positiva.

### B. Teste dos Autovalores
Calculando o polinômio característico $\det(A - \lambda I) = 0$:
$$\det \begin{pmatrix} 2 - \lambda & -1 \\ -1 & 2 - \lambda \end{pmatrix} = 0 \implies (2 - \lambda)^2 - 1 = 0$$
$$\lambda^2 - 4\lambda + 3 = 0 \implies \lambda_1 = \mathbf{3}, \quad \lambda_2 = \mathbf{1}$$
Ambos os autovalores são maiores que zero, confirmando a propriedade.

### C. Teste da Forma Quadrática
Para um vetor $x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \neq 0$:
$$x^T A x = \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 2x_1^2 - 2x_1x_2 + 2x_2^2$$
Completando o quadrado:
$$x^T A x = x_1^2 + (x_1 - x_2)^2 + x_2^2 > 0 \quad (\forall x \neq 0)$$

---

## 3. Fatoração de Cholesky

### Definição
A **Fatoração de Cholesky** é uma decomposição exclusiva para matrizes simétricas definidas positivas. Ela decompõe a matriz $A$ no produto de uma matriz triangular inferior $L$ pela sua transposta $L^T$:
$$A = L L^T$$
Onde os elementos de $L$ podem ser calculados iterativamente pelas fórmulas:
* Elementos da diagonal: $l_{jj} = \sqrt{a_{jj} - \sum_{k=1}^{j-1} l_{jk}^2}$
* Elementos fora da diagonal ($i > j$): $l_{ij} = \frac{1}{l_{jj}} \left( a_{ij} - \sum_{k=1}^{j-1} l_{ik}l_{jk} \right)$

### Exemplo Numérico de Fatoração ($A = L L^T$)
Usando a mesma matriz $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, procuramos $L = \begin{pmatrix} l_{11} & 0 \\ l_{21} & l_{22} \end{pmatrix}$:

1. **Encontrando $l_{11}$:**
   $$l_{11}^2 = a_{11} \implies l_{11}^2 = 2 \implies \mathbf{l_{11} = \sqrt{2}}$$

2. **Encontrando $l_{21}$:**
   $$l_{21} \cdot l_{11} = a_{21} \implies l_{21} \cdot \sqrt{2} = -1 \implies \mathbf{l_{21} = -\frac{1}{\sqrt{2}}}$$

3. **Encontrando $l_{22}$:**
   $$l_{21}^2 + l_{22}^2 = a_{22} \implies \left(-\frac{1}{\sqrt{2}}\right)^2 + l_{22}^2 = 2$$
   $$\frac{1}{2} + l_{22}^2 = 2 \implies l_{22}^2 = \frac{3}{2} \implies \mathbf{l_{22} = \sqrt{\frac{3}{2}}}$$

Assim, a matriz triangular inferior de Cholesky é:
$$L = \begin{pmatrix} \sqrt{2} & 0 \\ -\frac{1}{\sqrt{2}} & \sqrt{\frac{3}{2}} \end{pmatrix}$$

---

## 4. Exemplo 2: Matriz $3 \times 3$

Seja a matriz simétrica $B$:

$$
B = 
\begin{pmatrix}
3 & 1 & 1 \\
1 & 2 & 0 \\
1 & 0 & 2
\end{pmatrix}
$$

Aplicando o Critério de Sylvester:
1. **$D_1$**: $\det(3) = \mathbf{3 > 0}$
2. **$D_2$**:

$\det
\begin{pmatrix} 3 & 1 \\
1 & 2
\end{pmatrix} = (3 \times 2) - (1 \times 1) = 6 - 1 = \mathbf{5 > 0}
$
3. **$D_3$**: $\det(B) = 3(4 - 0) - 1(2 - 0) + 1(0 - 2) = 12 - 2 - 2 = \mathbf{8 > 0}$

Como todos os menores principais líderes são positivos ($3, 5, 8$), a matriz $B$ também é **definida positiva**.
