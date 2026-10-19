# Método de Sobrerrelaxação Sucessiva (SOR)

O **Método de Sobrerrelaxação Sucessiva** (*Successive Over-Relaxation* ou **SOR**) é um método iterativo avançado da álgebra linear numérica utilizado para resolver sistemas de equações lineares da forma $Ax = b$. Ele constitui uma extensão e otimização direta do **Método de Gauss-Seidel**.

---

## 1. O Conceito e o Fator de Relaxação ($\omega$)

Enquanto o método de Gauss-Seidel adota imediatamente o último valor calculado para uma variável, o método SOR introduz um parâmetro de ajuste chamado **fator de relaxação ($\omega$)**. Este parâmetro realiza uma média ponderada entre o valor da iteração anterior e o valor que seria obtido por Gauss-Seidel, acelerando a velocidade de convergência.

O comportamento do algoritmo varia de acordo com o intervalo escolhido para $\omega$:

*   **$\omega = 1$:** O método reduz-se exatamente ao **Método de Gauss-Seidel**.
*   **$1 < \omega < 2$ (Sobrerrelaxação):** Utilizado para **acelerar a convergência** de sistemas que convergiriam lentamente por Gauss-Seidel. É o cenário ideal e mais utilizado na prática.
*   **$0 < \omega < 1$ (Subrelaxação):** Utilizado para amortecer oscilações e **garantir a convergência** em sistemas onde Gauss-Seidel diverge ou oscila agressivamente.
*   **$\omega \le 0$ ou $\omega \ge 2$:** O método **diverge** obrigatoriamente.

---

## 2. Formulação Matemática

Dada a equação geral para a $i$-ésima componente do vetor solução no método de Gauss-Seidel:

$$\tilde{x}_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)} \right)$$

A fórmula do método SOR aplica o fator $\omega$ combinando o estado anterior $x_i^{(k)}$ com o novo candidato $\tilde{x}_i^{(k+1)}$:

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega \tilde{x}_i^{(k+1)}$$

Agrupando em uma única equação computacional:

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)} \right)$$

---

## 3. Exemplo Prático Passo a Passo

Considerando o sistema linear diagonalmente dominante abaixo:

$$\begin{cases} 4x_1 + x_2 = 5 \\ x_1 + 3x_2 = 4 \end{cases}$$

Definimos:
*   **Vetor Inicial ($k=0$):** $x^{(0)} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
*   **Fator de Relaxação:** $\omega = 1.25$

### Isolando as Variáveis (Formulário Gauss-Seidel com fator $\omega$):
1.  $x_1^{(k+1)} = (1 - 1.25)x_1^{(k)} + \frac{1.25}{4}\left(5 - x_2^{(k)}\right)$
2.  $x_2^{(k+1)} = (1 - 1.25)x_2^{(k)} + \frac{1.25}{3}\left(4 - x_1^{(k+1)}\right)$

### Cálculo da Primeira Iteração ($k=1$):

*   **Para $x_1^{(1)}$:**
    $$x_1^{(1)} = (-0.25)(0) + \frac{1.25}{4}(5 - 0)$$
    $$x_1^{(1)} = 0 + 0.3125 \times 5 = \mathbf{1.5625}$$

*   **Para $x_2^{(1)}$ (utilizando imediatamente o $x_1^{(1)} = 1.5625$):**
    $$x_2^{(1)} = (-0.25)(0) + \frac{1.25}{3}(4 - 1.5625)$$
    $$x_2^{(1)} = 0 + \frac{1.25}{3}(2.4375)$$
    $$x_2^{(1)} = 0.416667 \times 2.4375 = \mathbf{1.015625}$$

**Resultado da iteração 1:** $x^{(1)} = \begin{bmatrix} 1.5625 \\ 1.015625 \end{bmatrix}$

---

## 4. Análise de Convergência Comparativa

| Critério / Aspecto | Método de Jacobi | Método de Gauss-Seidel | Método SOR |
| :--- | :--- | :--- | :--- |
| **Uso de dados** | Apenas iteração anterior ($k$) | Mistura dados de ($k$) e ($k+1$) | Mistura dados ponderados por $\omega$ |
| **Velocidade** | Lenta | Geralmente 2x mais rápido que Jacobi | **Altamente acelerada** com $\omega$ ótimo |
| **Requisito Base** | Diagonal Dominante / Sassenfeld | Diagonal Dominante / Sassenfeld | Matrizes Simétricas e Positivas Definidas |

---
*Nota: O maior desafio prático do método SOR consiste em determinar de forma analítica ou empírica o valor ótimo de $\omega$ para sistemas complexos.*
