# Resumo Prático: Métodos Lineares de Resolução de Sistemas

Este documento reúne o passo a passo prático e os conceitos fundamentais dos três principais métodos diretos para resolução de sistemas lineares de equações: **Gauss-Jordan**, **Eliminação Gaussiana** e **Fatoração LU**.

---

## 1. Método de Gauss-Jordan
O objective do método de Gauss-Jordan é transformar a matriz aumentada do sistema até que o lado esquerdo (matriz dos coeficientes) vire uma **Matriz Identidade**. Quando o sistema possui uma **solução única**, esse resultado é sempre alcançado.

### Exemplo Prático ($2 \times 2$)
Sistema original:
$$
\begin{cases} 2x + y = 5 \\ x - 3y = -1 \end{cases}
$$

1. **Matriz Aumentada Inicial:**
   $$ \begin{bmatrix} 2 & 1 & \bigm\vert{} & 5 \\ 1 & -3 & \bigm\vert{} & -1 \end{bmatrix} $$

2. **Troca de Linhas ($L_1 \leftrightarrow L_2$) para obter o primeiro pivô:**
   $$ \begin{bmatrix} \mathbf{1} & -3 & \bigm\vert{} & -1 \\ 2 & 1 & \bigm\vert{} & 5 \end{bmatrix} $$

3. **Zerar abaixo do pivô ($L_2 \leftarrow L_2 - 2L_1$):**
   $$ \begin{bmatrix} 1 & -3 & \bigm\vert{} & -1 \\ \mathbf{0} & 7 & \bigm\vert{} & 7 \end{bmatrix} $$

4. **Criar o segundo pivô ($L_2 \leftarrow \frac{1}{7}L_2$):**
   $$ \begin{bmatrix} 1 & -3 & \bigm\vert{} & -1 \\ 0 & \mathbf{1} & \bigm\vert{} & 1 \end{bmatrix} $$

5. **Zerar acima do segundo pivô ($L_1 \leftarrow L_1 + 3L_2$):**
   $$ \begin{bmatrix} \mathbf{1} & \mathbf{0} & \bigm\vert{} & 2 \\ \mathbf{0} & \mathbf{1} & \bigm\vert{} & 1 \end{bmatrix} $$

**Solução Direta:** $x = 2$, $y = 1$.

---

## 2. Eliminação Gaussiana (Gauss Simples)
Diferente de Gauss-Jordan, a Eliminação Gaussiana para assim que a matriz atinge o formato **Triangular Superior** (zeros apenas abaixo da diagonal principal). A partir daí, resolve-se o sistema de baixo para cima usando substituição regressiva.

### Exemplo Prático ($3 \times 3$)
Sistema original:
$$
\begin{cases} x + 2y + z = 8 \\ 2x + y - z = 1 \\ -x + y - 2z = -7 \end{cases}
$$

1. **Matriz Aumentada Inicial:**
   $$ \begin{bmatrix} 1 & 2 & 1 & \bigm\vert{} & 8 \\ 2 & 1 & -1 & \bigm\vert{} & 1 \\ -1 & 1 & -2 & \bigm\vert{} & -7 \end{bmatrix} $$

2. **Zerar a Coluna 1 ($L_2 \leftarrow L_2 - 2L_1$ e $L_3 \leftarrow L_3 + L_1$):**
   $$ \begin{bmatrix} 1 & 2 & 1 & \bigm\vert{} & 8 \\ \mathbf{0} & -3 & -3 & \bigm\vert{} & -15 \\ \mathbf{0} & 3 & -1 & \bigm\vert{} & 1 \end{bmatrix} $$

3. **Zerar a Coluna 2 abaixo do pivô ($L_3 \leftarrow L_3 + L_2$):**
   $$ \begin{bmatrix} 1 & 2 & 1 & \bigm\vert{} & 8 \\ 0 & -3 & -3 & \bigm\vert{} & -15 \\ \mathbf{0} & \mathbf{0} & -4 & \bigm\vert{} & -14 \end{bmatrix} $$

4. **Substituição de Baixo para Cima:**
   * Linha 3: $-4z = -14 \implies \mathbf{z = 3.5}$
   * Linha 2: $-3y - 3(3.5) = -15 \implies \mathbf{y = 1.5}$
   * Linha 1: $x + 2(1.5) + 3.5 = 8 \implies \mathbf{x = 1.5}$

---

## 3. Fatoração LU
Consiste em decompor a matriz de coeficientes $A$ no produto de duas matrizes triangulares: $A = L \cdot U$. 
* $L$ (Lower): Triangular Inferior com $1$ na diagonal principal (armazena os multiplicadores).
* $U$ (Upper): Triangular Superior (resultado final do escalonamento).

Utilizando a mesma matriz $A$ do exemplo anterior:
$$ A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 1 & -1 \\ -1 & 1 & -2 \end{bmatrix} $$

### Obtenção das Matrizes:
Ao realizar o escalonamento clássico, guardamos os fatores utilizados para zerar as posições:
* Para zerar a posição (2,1), o multiplicador foi **2**.
* Para zerar a posição (3,1), o multiplicador foi **-1**.
* Para zerar a posição (3,2), o multiplicador foi **-1**.

### Matrizes Finais:
$$ L = \begin{bmatrix} 1 & 0 & 0 \\ \mathbf{2} & 1 & 0 \\ \mathbf{-1} & \mathbf{-1} & 1 \end{bmatrix} \qquad U = \begin{bmatrix} 1 & 2 & 1 \\ 0 & -3 & -3 \\ 0 & 0 & -4 \end{bmatrix} $$

### Resolução em Duas Etapas ($A \cdot x = b$):
1. **Resolver $L \cdot y = b$** (Substituição Direta): Encontra-se o vetor auxiliar $y = [8, -15, -14]^T$.
2. **Resolver $U \cdot x = y$** (Substituição Regressiva): Encontra-se a solução final $x = [1.5, 1.5, 3.5]^T$.

---

## 4. Tabela Comparativa dos Métodos

| Método | Formato Final da Matriz | Vantagem Principal | Desvantagem Principal | Cenário Ideal |
| :--- | :--- | :--- | :--- | :--- |
| **Eliminação Gaussiana** | Triangular Superior | Menos operações aritméticas que Gauss-Jordan. | Exige esforço de substituição manual no final. | Sistemas gerais calculados manualmente ou algoritmos simples. |
| **Gauss-Jordan** | Matriz Identidade | Dá a resposta diretamente na última coluna, sem substituição. | Custo computacional mais elevado (mais operações por linha). | Encontrar a Matriz Inversa ou resolver sistemas pequenos de forma direta. |
| **Fatoração LU** | Duas Matrizes ($L$ e $U$) | Extremamente rápido quando o vetor de respostas ($b$) muda frequentemente. | A decomposição inicial exige atenção com os multiplicadores. | Sistemas de engenharia/física com cargas dinâmicas (mesma estrutura, respostas variadas). |
| **Fatoração de Cholesky** | Duas Matrizes ($L$ e $L^T$) | Duas vezes mais rápido que o método LU tradicional. | Restrito apenas a matrizes simétricas e definidas positivas. | Simulações de Monte Carlo, Machine Learning e filtragem de Kalman. |
| **Algoritmo de Thomas** | Vetores modificados ($c'$ e $d'$) | Reduz drasticamente o custo computacional para complexidade linear $O(n)$. | Aplica-se exclusivamente a matrizes tridiagonais. | Resolução de Equações Diferenciais Parciais por Diferenças Finitas. |
| **Fatoração QR** | Duas Matrizes ($Q$ ortogonal e $R$ triangular) | Altamente estável numericamente e dispensa pivoteamento. | Custo computacional elevado em comparação com o método LU. | Problemas de Mínimos Quadrados, regressões lineares e cálculo de autovalores. |
| **SVD (Valores Singulares)** | Três Matrizes ($U$ ortogonal, $\Sigma$ diagonal e $V^T$ ortogonal) | Aplica-se a **qualquer matriz** (mesmo retangular ou singular) e extrai propriedades geométricas puras. | Custo computacional muito elevado para grandes volumes de dados. | **Redução de dimensionalidade (PCA)**, compressão de dados/imagens e sistemas mal condicionados. |

---
*Documento gerado para consolidação de estudos em álgebra linear computacional.*
