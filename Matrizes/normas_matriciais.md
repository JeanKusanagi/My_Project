# Normas Matriciais: Definições e Exemplos Práticos

Este documento apresenta a definição matemática de norma de uma matriz, suas propriedades fundamentais e o cálculo passo a passo das principais normas utilizando uma matriz de exemplo.

---

## 1. O que é a Norma de uma Matriz?

A **norma de uma matriz** é uma função que associa um número real não-negativo a uma matriz, medindo o seu "tamanho" ou magnitude. É uma extensão natural do conceito de comprimento (norma) de vetores para o espaço das matrizes.

### Propriedades Fundamentais

Para que uma função $\|A\|$ seja considerada uma norma matricial, ela deve satisfazer quatro propriedades para quaisquer matrizes $A$ e $B$ e qualquer escalar $\alpha$:

1. **Não-negatividade:** $\|A\| \ge 0$, sendo $\|A\| = 0$ se e somente se $A = 0$ (matriz nula).
2. **Homogeneidade:** $\|\alpha A\| = |\alpha| \cdot \|A\|$.
3. **Desigualdade Triangular:** $\|A + B\| \le \|A\| + \|B\|$.
4. **Submultiplicatividade:** $\|AB\| \le \|A\| \cdot \|B\|$ (requerida na maioria das normas matriciais).

---

## 2. Matriz Utilizada nos Exemplos

Para demonstrar o cálculo de cada norma, utilizaremos a seguinte matriz $A$ de dimensão $2 \times 3$:

$$A = \begin{pmatrix} 2 & -3 & 1 \\ 4 & 0 & -2 \end{pmatrix}$$

---

## 3. Principais Tipos de Normas e Exemplos

### 3.1 Norma 1 (Soma Máxima das Colunas)
A Norma 1 mapeia o maior valor obtido ao somar os módulos dos elementos de cada coluna individualmente.

$$\|A\|_1 = \max_{1 \le j \le n} \sum_{i=1}^{m} |a_{ij}|$$

**Cálculo passo a passo:**
* **Coluna 1:** $|2| + |4| = 2 + 4 = 6$
* **Coluna 2:** $|-3| + |0| = 3 + 0 = 3$
* **Coluna 3:** $|1| + |-2| = 1 + 2 = 3$

$$\|A\|_1 = \max(6, 3, 3) = \mathbf{6}$$

---

### 3.2 Norma $\infty$ (Soma Máxima das Linhas)
A Norma Infinito mapeia o maior valor obtido ao somar os módulos dos elementos de cada linha individualmente.

$$\s\|A\|_\infty = \max_{1 \le i \le m} \sum_{j=1}^{n} |a_{ij}|$$

**Cálculo passo a passo:**
* **Linha 1:** $|2| + |-3| + |1| = 2 + 3 + 1 = 6$
* **Linha 2:** $|4| + |0| + |-2| = 4 + 0 + 2 = 6$

$$\|A\|_\infty = \max(6, 6) = \mathbf{6}$$

---

### 3.3 Norma de Frobenius (Norma Euclidiana)
A Norma de Frobenius calcula a raiz quadrada da soma dos quadrados de absolutamente todos os elementos da matriz.

$$\|A\|_F = \sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n} |a_{ij}|^2}$$

**Cálculo passo a passo:**
$$\|A\|_F = \sqrt{2^2 + (-3)^2 + 1^2 + 4^2 + 0^2 + (-2)^2}$$
$$\|A\|_F = \sqrt{4 + 9 + 1 + 16 + 0 + 4}$$
$$\|A\|_F = \sqrt{34} \approx \mathbf{5{,}83}$$

---

### 3.4 Norma 2 ou Norma Espectral
A Norma 2 é igual ao maior valor singular da matriz, o que equivale à raiz quadrada do maior autovalor ($\lambda_{\max}$) da matriz quadrada obtida por $A A^T$ (ou $A^T A$).

$$\|A\|_2 = \sqrt{\lambda_{\max}(A A^T)}$$

**Cálculo passo a passo:**

1. **Multiplicação $A A^T$:**
   $$A A^T = \begin{pmatrix} 2 & -3 & 1 \\ 4 & 0 & -2 \end{pmatrix} \begin{pmatrix} 2 & 4 \\ -3 & 0 \\ 1 & -2 \end{pmatrix} = \begin{pmatrix} 14 & 6 \\ 6 & 20 \end{pmatrix}$$

2. **Cálculo dos autovalores ($\|A A^T - \lambda I\| = 0$):**
   $$\det \begin{pmatrix} 14 - \lambda & 6 \\ 6 & 20 - \lambda \end{pmatrix} = 0$$
   $$(14 - \lambda)(20 - \lambda) - 36 = 0$$
   $$\lambda^2 - 34\lambda + 244 = 0$$

3. **Resolução da equação quadrática:**
   $$\lambda = \frac{34 \pm \sqrt{(-34)^2 - 4(1)(244)}}{2} = \frac{34 \pm \sqrt{180}}{2}$$
   * $\lambda_1 = \frac{34 + 13{,}416}{2} \approx 23{,}708$ (Maior autovalor)
   * $\lambda_2 = \frac{34 - 13{,}416}{2} \approx 10{,}292$

4. **Extração da raiz quadrada:**
   $$\|A\|_2 = \sqrt{23{,}708} \approx \mathbf{4{,}87}$$

---

## 4. Resumo Comparativo das Normas

| Tipo de Norma | Fórmula Simplificada | Resultado Prático |
| :--- | :--- | :--- |
| **Norma 1** | Maior soma absoluta das colunas | **6,00** |
| **Norma $\infty$** | Maior soma absoluta das linhas | **6,00** |
| **Norma de Frobenius** | Raiz da soma de todos os quadrados | **5,83** |
| **Norma 2 (Espectral)** | Raiz quadrada do maior autovalor de $A A^T$ | **4,87** |