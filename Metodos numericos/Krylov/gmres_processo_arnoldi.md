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

## 5. Algoritmo GMRES com Rotações de Givens (Pseudocódigo)

---

```text
ALGORITMO GMRES(A, b, x0, tol, m_max)
    // ENTRADAS:
    // A: Matriz do sistema (n x n)
    // b: Vetor do lado direito (n x 1)
    // x0: Palpite inicial (n x 1)
    // tol: Tolerância de parada (ex: 1e-6)
    // m_max: Número máximo de iterações antes de parar ou reiniciar
    
    // -------------------------------------------------------------
    // Passo 0: Inicialização
    // -------------------------------------------------------------
    r0 = b - A * x0
    beta = norma_euclidiana(r0)
    
    Se beta < tol Então
        Retornar x0 // O palpite inicial já é a solução
    Fim Se
    
    // Inicializa a base de Krylov V e o vetor g do lado direito projetado
    v = r0 / beta
    g = vetor_zerado(m_max + 1)
    g[1] = beta
    
    // Inicializa vetores para guardar os senos e cossenos das rotações de Givens
    c = vetor_zerado(m_max)
    s = vetor_zerado(m_max)
    
    // Aloca espaço para a Matriz de Hessenberg Superior H (m_max+1 x m_max)
    H = matriz_zerada(m_max + 1, m_max)
    
    // -------------------------------------------------------------
    // Loop Iterativo (Processo de Arnoldi + Minimização)
    // -------------------------------------------------------------
    Para j = 1 Até m_max Faça
        
        // 1. Passo de Arnoldi: Multiplicação
        w = A * v[j]
        
        // 2. Ortogonalização de Gram-Schmidt Modificada
        Para i = 1 Até j Faça
            H[i, j] = produto_escalar(w, v[i])
            w = w - H[i, j] * v[i]
        Fim Para
        
        H[j+1, j] = norma_euclidiana(w)
        
        // 3. Aplica rotações de Givens anteriores à nova coluna de H
        Para i = 1 Até j-1 Faça
            temp      =  c[i] * H[i, j] + s[i] * H[i+1, j]
            H[i+1, j] = -s[i] * H[i, j] + c[i] * H[i+1, j]
            H[i, j]   = temp
        Fim Para
        
        // 4. Calcula e aplica a NOVA rotação de Givens para zerar H[j+1, j]
        a = H[j, j]
        b = H[j+1, j]
        
        Se b == 0 Então
            c[j] = 1
            s[j] = 0
        Senão Se modulo(b) > modulo(a) Então
            tau = a / b
            s[j] = 1 / raiz_quadrada(1 + tau^2)
            c[j] = s[j] * tau
        Senão
            tau = b / a
            c[j] = 1 / raiz_quadrada(1 + tau^2)
            s[j] = c[j] * tau
        Fim Se
        
        // Elimina o elemento subdiagonal em H
        H[j, j]   = c[j] * a + s[j] * b
        H[j+1, j] = 0
        
        // Aplica a nova rotação ao vetor do lado direito g
        g[j+1] = -s[j] * g[j]
        g[j]   =  c[j] * g[j]
        
        // 5. Critério de Parada (O resíduo atualizado é o último elemento de g)
        residuo_atual = modulo(g[j+1])
        
        Se (residuo_atual / beta) < tol Então
            m_atual = j // Guarda em qual iteração convergiu
            Quebrar Loop
        Fim Se
        
        // Se não convergiu, define o próximo vetor da base
        v[j+1] = w / H[j+1, j]
        m_atual = j
    Fim Para
    
    // -------------------------------------------------------------
    // Passo Final: Reconstrução da Solução
    // -------------------------------------------------------------
    // Resolve o sistema triangular superior R * y = g usando a matriz H modificada
    // H (de 1 até m_atual, de 1 até m_atual) agora contém a matriz R triangular
    y = vetor_zerado(m_atual)
    
    Para i = m_atual Decrescendo Até 1 Faça
        soma = 0
        Para k = i+1 Até m_atual Faça
            soma = soma + H[i, k] * y[k]
        Fim Para
        y[i] = (g[i] - soma) / H[i, i]
    Fim Para
    
    // Monta a solução final no espaço original de dimensão n
    x = x0
    Para i = 1 Até m_atual Faça
        x = x + v[i] * y[i]
    Fim Para
    
    Retornar x
FIM ALGORITMO
```

---

## 📌 Detalhes de Implementação

1. **Gram-Schmidt Modificado:** Implementado no loop interno de ortogonalização. Atualizar `w` a cada passo reduz drasticamente a perda de ortogonalidade numérica causada por erros de arredondamento em precisão finita.
2. **Cálculo Estável de Givens:** A escolha do cálculo dos parâmetros baseando-se na razão `tau` (dependendo de qual valor absoluto é maior entre `a` e `b`) previne problemas de *overflow* aritmético.
3. **Monitoramento do Resíduo:** O valor `modulo(g[j+1])` fornece o resíduo exato da iteração atual de forma síncrona, permitindo a interrupção prematura do laço sem custos adicionais de reconstrução de `x` ou multiplicação de matrizes de ordem $n$.
