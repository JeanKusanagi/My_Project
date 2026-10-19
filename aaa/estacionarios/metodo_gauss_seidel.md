# Exemplo Prático: Método de Gauss-Seidel

O **Método de Gauss-Seidel** é um algoritmo iterativo utilizado para resolver sistemas de equações lineares. Diferente do Método de Jacobi, ele utiliza os valores recém-calculados na mesma iteração assim que eles ficam disponíveis, o que geralmente acelera a convergência.

---

## Sistema Linear Proposto

Consideremos o seguinte sistema de equações lineares de ordem $3 \times 3$:

$$
\begin{cases} 
10x_1 + x_2 + 2x_3 = 6 \\ 
x_1 + 10x_2 + 3x_3 = 7 \\ 
2x_1 + 3x_2 + 10x_3 = 8 
\end{cases}
$$

Este sistema atende ao **Critério das Linhas (Diagonal Dominante)**, garantindo a convergência do método.

---

## Passo 1: Isolar as Variáveis com Atualização Imediata

Isolamos cada variável na sua respectiva linha, aplicando os índices de iteração imediata $(k+1)$:

$$x_1^{(k+1)} = \frac{6 - x_2^{(k)} - 2x_3^{(k)}}{10}$$

$$x_2^{(k+1)} = \frac{7 - x_1^{(k+1)} - 3x_3^{(k)}}{10}$$

$$x_3^{(k+1)} = \frac{8 - 2x_1^{(k+1)} - 3x_2^{(k+1)}}{10}$$

---

## Passo 2: Vetor Inicial ($k=0$)

Adotamos a aproximação inicial nula:
$$x_1^{(0)} = 0, \quad x_2^{(0)} = 0, \quad x_3^{(0)} = 0$$

---

## Passo 3: Iterações Calculadas

### Primeira Iteração ($k=1$)

1. **Calcular $x_1^{(1)}$:**
   $$x_1^{(1)} = \frac{6 - 0 - 2(0)}{10} = 0.6$$

2. **Calcular $x_2^{(1)}$:** (Usa o novo $x_1^{(1)} = 0.6$)
   $$x_2^{(1)} = \frac{7 - 0.6 - 3(0)}{10} = 0.64$$

3. **Calcular $x_3^{(1)}$:** (Usa os novos $x_1^{(1)} = 0.6$ e $x_2^{(1)} = 0.64$)
   $$x_3^{(1)} = \frac{8 - 2(0.6) - 3(0.64)}{10} = \frac{8 - 1.2 - 1.92}{10} = 0.488$$

Vetor resultante da iteração 1: $(0.6, \, 0.64, \, 0.488)$

### Segunda Iteração ($k=2$)

1. **Calcular $x_1^{(2)}$:**
   $$x_1^{(2)} = \frac{6 - 0.64 - 2(0.488)}{10} = \frac{6 - 0.64 - 0.976}{10} = 0.4384$$

2. **Calcular $x_2^{(2)}$:** (Usa o novo $x_1^{(2)} = 0.4384$)
   $$x_2^{(2)} = \frac{7 - 0.4384 - 3(0.488)}{10} = \frac{7 - 0.4384 - 1.464}{10} = 0.50976$$

3. **Calcular $x_3^{(2)}$:** (Usa os novos $x_1^{(2)} = 0.4384$ e $x_2^{(2)} = 0.50976$)
   $$x_3^{(2)} = \frac{8 - 2(0.4384) - 3(0.50976)}{10} = \frac{8 - 0.8768 - 1.52928}{10} = 0.559392$$

Vetor resultante da iteração 2: $(0.4384, \, 0.50976, \, 0.559392)$

---

## Comparação de Desempenho (Solução Exata $\approx [0.473, \, 0.518, \, 0.550]$)

| Método | Iteração 1 | Iteração 2 |
| :--- | :--- | :--- |
| **Jacobi** | $(0.6, \, 0.7, \, 0.8)$ | $(0.37, \, 0.40, \, 0.47)$ |
| **Gauss-Seidel** | $(0.6, \, 0.64, \, 0.488)$ | $(0.4384, \, 0.50976, \, 0.559392)$ |
