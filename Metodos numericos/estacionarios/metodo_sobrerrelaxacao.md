# Método da Sobrerrelaxação Sucessiva (SOR)

O método da **Sobrerrelaxação Sucessiva** (SOR - *Successive Over-Relaxation*) é uma variante e otimização do Método de Gauss-Seidel. Ele introduz um fator de relaxação $\omega$ (ômega) para acelerar a convergência do sistema linear.

---

## Sistema Linear Utilizado

Utilizamos o mesmo sistema de equações lineares de ordem $3 \times 3$:

$$
\begin{cases} 
10x_1 + x_2 + 2x_3 = 6 \\ 
x_1 + 10x_2 + 3x_3 = 7 \\ 
2x_1 + 3x_2 + 10x_3 = 8 
\end{cases}
$$

A solução exata aproximada deste sistema é $x_1 \approx 0.473$, $x_2 \approx 0.518$ e $x_3 \approx 0.550$.

---

## Fórmula de Recorrência

O método calcula uma solução intermediária pelo método de Gauss-Seidel ($\ ext{GS}$) e depois faz uma média ponderada com o valor da iteração anterior utilizando o fator $\omega$:

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega \cdot x_i^{(\text{GS})}$$

Para este exemplo, escolheremos um fator de sobrerrelaxação **$\omega = 1.15$**.

As equações de iteração ficam:

$$x_1^{(k+1)} = (1 - 1.15)x_1^{(k)} + 1.15 \cdot \left( \frac{6 - x_2^{(k)} - 2x_3^{(k)}}{10} \right)$$

$$x_2^{(k+1)} = (1 - 1.15)x_2^{(k)} + 1.15 \cdot \left( \frac{7 - x_1^{(k+1)} - 3x_3^{(k)}}{10} \right)$$

$$x_3^{(k+1)} = (1 - 1.15)x_3^{(k)} + 1.15 \cdot \left( \frac{8 - 2x_1^{(k+1)} - 3x_2^{(k+1)}}{10} \right)$$

---

## Iterações (Chute Inicial $x^{(0)} = [0, 0, 0]$)

### **Primeira Iteração ($k=1$)**

* **Calcular $x_1^{(1)}$:**
  $$x_1^{(1)} = -0.15(0) + 1.15 \cdot \left( \frac{6 - 0 - 2(0)}{10} \right) = 1.15 \cdot 0.6 = \mathbf{0.69}$$

* **Calcular $x_2^{(1)}$:** (usa o novo $x_1^{(1)} = 0.69$)
  $$x_2^{(1)} = -0.15(0) + 1.15 \cdot \left( \frac{7 - 0.69 - 3(0)}{10} \right) = 1.15 \cdot 0.631 = \mathbf{0.72565}$$

* **Calcular $x_3^{(1)}$:** (usa os novos $x_1^{(1)} = 0.69$ e $x_2^{(1)} = 0.72565$)
  $$x_3^{(1)} = -0.15(0) + 1.15 \cdot \left( \frac{8 - 2(0.69) - 3(0.72565)}{10} \right) = 1.15 \cdot \left( \frac{8 - 1.38 - 2.17695}{10} \right) = 1.15 \cdot 0.444305 = \mathbf{0.51095075}$$

Vetor após a primeira iteração: $[0.69, \, 0.72565, \, 0.51095075]$.

---

## Comparação de Convergência (Iteração 1)

| Método | Componente $x_1$ | Componente $x_2$ | Componente $x_3$ |
| :--- | :--- | :--- | :--- |
| **Jacobi** | $0.6000$ | $0.7000$ | $0.8000$ |
| **Gauss-Seidel** | $0.6000$ | $0.6400$ | $0.4880$ |
| **SOR ($\omega = 1.15$)** | $\mathbf{0.6900}$ | $\mathbf{0.7256}$ | $\mathbf{0.5110}$ |
