# Fatoração QR (Decomposição QR)

A **fatoração QR** decompõe uma matriz real $A$ de dimensão $m \times n$ no produto de duas matrizes específicas: $A = QR$. Ela é amplamente utilizada para resolver sistemas lineares, problemas de mínimos quadrados e no cálculo de autovalores.

---

## As Matrizes Componentes

*   **Matriz $Q$ ($m \times n$):** Suas colunas formam um conjunto de **vetores ortonormais** (comprimento igual a 1 e perpendiculares entre si). Possui a propriedade fundamental de que $Q^T Q = I$.
*   **Matriz $R$ ($n \times n$):** Matriz **triangular superior**, onde todos os elementos abaixo da diagonal principal são iguais a zero.

---

## Exemplo Numérico Passo a Passo (Gram-Schmidt)

Vamos fatorar a seguinte matriz $A$:
$$A = \begin{bmatrix} 3 & 1 \\ 4 & 2 \end{bmatrix}$$

Separando as colunas de $A$ em vetores:
$$v_1 = \begin{bmatrix} 3 \\ 4 \end{bmatrix}, \quad v_2 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$

### Passo 1: Construir a Matriz Ortogonal $Q$

#### Encontrando a primeira coluna ($q_1$)
Normalizamos o vetor $v_1$ dividindo-o pela sua norma:
1. **Norma de $v_1$:** 
   $$\|v_1\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$
2. **Vetor unitário $q_1$:**
   $$q_1 = \frac{v_1}{\|v_1\|} = \frac{1}{5} \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}$$

#### Encontrando a segunda coluna ($q_2$)
Subtraímos de $v_2$ a sua projeção sobre $q_1$ para obter um vetor ortogonal $u_2$:
1. **Produto escalar $v_2 \cdot q_1$:**
   $$v_2 \cdot q_1 = (1 \cdot 0.6) + (2 \cdot 0.8) = 0.6 + 1.6 = 2.2$$
2. **Vetor ortogonal $u_2$:**
   $$u_2 = v_2 - (v_2 \cdot q_1)q_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix} - 2.2 \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix} = \begin{bmatrix} -0.32 \\ 0.24 \end{bmatrix}$$
3. **Norma de $u_2$:**
   $$\|u_2\| = \sqrt{(-0.32)^2 + (0.24)^2} = \sqrt{0.1024 + 0.0576} = \sqrt{0.16} = 0.4$$
4. **Vetor unitário $q_2$:**
   $$q_2 = \frac{u_2}{\|u_2\|} = \frac{1}{0.4} \begin{bmatrix} -0.32 \\ 0.24 \end{bmatrix} = \begin{bmatrix} -0.8 \\ 0.6 \end{bmatrix}$$

Montando a matriz **$Q$**:
$$Q = \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}$$

---

### Passo 2: Construir a Matriz Triangular Superior $R$

Os elementos de $R$ correspondem aos coeficientes das projeções:
*   $R_{11} = \|v_1\| = 5$
*   $R_{12} = v_2 \cdot q_1 = 2.2$
*   $R_{21} = 0$
*   $R_{22} = v_2 \cdot q_2 = (1 \cdot -0.8) + (2 \cdot 0.6) = 0.4$

Montando a matriz **$R$**:
$$R = \begin{bmatrix} 5 & 2.2 \\ 0 & 0.4 \end{bmatrix}$$

---

### Resultado Final

$$A = QR \implies \begin{bmatrix} 3 & 1 \\ 4 & 2 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix} \begin{bmatrix} 5 & 2.2 \\ 0 & 0.4 \end{bmatrix}$$
