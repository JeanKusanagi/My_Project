# GMRES e o Processo de Arnoldi: Explicação Matemática Detalhada

O **GMRES** (**G**eneralized **M**inimal **R**esidual method) é um algoritmo iterativo projetado para resolver sistemas lineares da forma $Ax = b$, onde a matriz $A$ é grande, esparsa e não necessariamente simétrica. O coração deste método é o **Processo de Arnoldi**, aliado às **Rotações de Givens** para resolver um problema de mínimos quadrados projetado.

---

## 1. O Processo de Arnoldi
O objetivo do Processo de Arnoldi é construir uma base ortonormal para o **Espaço de Krylov** de ordem $m$, definido por:
$$\mathcal{K}_m(A, v_1) = \text{span}\{v_1, Av_1, A^2v_1, \dots, A^{m-1}v_1\}$$

Ao final de $m$ passos, o algoritmo estabelece a **Relação de Arnoldi**:
$$A V_m = V_{m+1} \bar{H}_m$$

Onde:
*   $V_m \in \mathbb{R}^{n \times m}$ possui colunas ortonormais ($V_m^T V_m = I_m$).
*   $\bar{H}_m \in \mathbb{R}^{(m+1) \times m}$ é uma **Matriz de Hessenberg Superior** (todos os elementos abaixo da primeira subdiagonal são zero).

### Algoritmo do Processo de Arnoldi (Passo $j$)
Para $j = 1, 2, \dots, m$:
1.  **Multiplicação:** $w_j = A v_j$
2.  **Ortogonalização (Gram-Schmidt):** Para $i = 1$ até $j$:
    *   $h_{i,j} = \langle w_j, v_i \rangle = v_i^T w_j$
    *   $w_j = w_j - h_{i,j} v_i$
3.  **Normalização:**
    *   $h_{j+1,j} = \|w_j\|_2$
    *   $v_{j+1} = \frac{w_j}{h_{j+1,j}}$ (se $h_{j+1,j} \neq 0$)

---

## 2. Redução a Mínimos Quadrados e Rotações de Givens
O GMRES busca uma aproximação $x = x_0 + V_m y$ que minimize a norma do resíduo $\|b - Ax\|_2$. Usando a relação de Arnoldi e a propriedade de isometria de $V_{m+1}$, o problema de dimensão $n$ é projetado em uma dimensão $m+1$:
$$\min_{y} \|b - Ax\|_2 = \min_{y} \|\beta e_1 - \bar{H}_m y\|_2$$
Onde $\beta = \|r_0\|_2$ e $e_1 = [1, 0, \dots, 0]^T$.

### Aplicação das Rotações de Givens
Como $\bar{H}_m$ possui apenas uma subdiagonal não-nula, usamos matrizes de rotação de Givens $G_i$ para eliminar os elementos subdiagonais um por um, transformando $\bar{H}_m$ em uma matriz triangular superior $R_m$:

$$Q_m \bar{H}_m = \begin{bmatrix} R_m \\ 0 \end{bmatrix}, \quad Q_m (\beta e_1) = \begin{bmatrix} g_m \\ \gamma_m \end{bmatrix}$$

Onde $Q_m = G_m G_{m-1} \dots G_1$. O sistema de mínimos quadrados reduz-se a:
$$\min_{y} \left( \|R_m y - g_m\|_2^2 + |\gamma_m|^2 \right)$$

A solução ótima é encontrada instantaneamente resolvendo a matriz triangular por substituição retroativa: $R_m y = g_m$. O resíduo atual do sistema é dado diretamente por $|\gamma_m|$, eliminando a necessidade de calcular $x$ a cada iteração.

---

## 3. Exemplo Numérico Manual: 1 Iteração do Arnoldi

### Definição do Problema
Sejam:
$$A = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 1 \end{bmatrix}, \quad b = \begin{bmatrix} 3 \\ 0 \\ 4 \end{bmatrix}, \quad x_0 = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

### Passo 0: Inicialização de $v_1$
1.  **Norma do resíduo inicial ($r_0 = b - Ax_0 = b$):**
    $$\beta = \|b\|_2 = \sqrt{3^2 + 0^2 + 4^2} = \sqrt{25} = 5$$
2.  **Construção de $v_1$:**
    $$v_1 = \frac{b}{5} = \begin{bmatrix} 0.6 \\ 0 \\ 0.8 \end{bmatrix}$$

### Passo 1: Iteração $j = 1$
1.  **Multiplicação pela matriz ($w_1 = A v_1$):**
    $$w_1 = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 1 \end{bmatrix} egin{bmatrix} 0.6 \\ 0 \\ 0.8 \end{bmatrix} = \begin{bmatrix} 2.2 \\ 0.8 \\ 2.0 \end{bmatrix}$$

2.  **Ortogonalização ($i = 1$):**
    *   Cálculo de $h_{1,1} = \langle w_1, v_1 \rangle$:
        $$h_{1,1} = (2.2 \cdot 0.6) + (0.8 \cdot 0) + (2.0 \cdot 0.8) = 1.32 + 0 + 1.6 = 2.92$$
    *   Subtração da projeção:
        $$w_1 = w_1 - h_{1,1} v_1 = \begin{bmatrix} 2.2 \\ 0.8 \\ 2.0 \end{bmatrix} - 2.92 \begin{bmatrix} 0.6 \\ 0 \\ 0.8 \end{bmatrix} = \begin{bmatrix} 0.448 \\ 0.8 \\ -0.336 \end{bmatrix}$$

3.  **Normalização para $v_2$:**
    *   Cálculo de $h_{2,1} = \|w_1\|_2$:
        $$h_{2,1} = \sqrt{0.448^2 + 0.8^2 + (-0.336)^2} = \sqrt{0.9536} \approx 0.976524$$
    *   Construção de $v_2$:
        $$v_2 = \frac{1}{0.976524} \begin{bmatrix} 0.448 \\ 0.8 \\ -0.336 \end{bmatrix} \approx \begin{bmatrix} 0.45877 \\ 0.81923 \\ -0.34408 \end{bmatrix}$$

### Estruturas Resultantes no Passo 1
*   **Base Ortogonal Parcial:**
    $$V_2 = \begin{bmatrix} 0.6 & 0.45877 \\ 0 & 0.81923 \\ 0.8 & -0.34408 \end{bmatrix}$$
*   **Matriz de Hessenberg Reduzida:**
    $$\bar{H}_1 = \begin{bmatrix} h_{1,1} \\ h_{2,1} \end{bmatrix} = \begin{bmatrix} 2.92 \\ 0.976524 \end{bmatrix}$$

---

## 4. Escolha de Pré-condicionadores
O pré-condicionamento transforma o sistema original em $M^{-1}Ax = M^{-1}b$. O objetivo é aproximar $M^{-1}A \approx I$ mantendo o custo computacional baixo.

### Principais Abordagens:
*   **Jacobi (Diagonal):** Útil para matrizes estritamente diagonais dominantes.
*   **ILU (Fatoração LU Incompleta):** O padrão geral para matrizes não-simétricas na engenharia.
*   **Multigrid (AMG/MG):** Essencial para grandes problemas vindos de Equações Diferenciais Parciais (EDPs).
*   **FGMRES (Flexible GMRES):** Obrigatório caso o pré-condicionador varie a cada iteração (ex: se o pré-condicionador for outro método iterativo).