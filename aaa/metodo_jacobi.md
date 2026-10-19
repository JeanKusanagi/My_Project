# Exemplo Prático: Método de Jacobi

Este documento apresenta a resolução passo a passo de um sistema de equações lineares utilizando o **Método Iterativo de Jacobi**.

---

## 1. O Sistema Linear

Consideramos o seguinte sistema de ordem $3 \times 3$:

$$
\begin{cases} 
10x_1 + x_2 + 2x_3 = 6 \\ 
x_1 + 10x_2 + 3x_3 = 7 \\ 
2x_1 + 3x_2 + 10x_3 = 8 
\end{cases}
$$

### Critério de Convergência (Linhas)
Antes de iniciar, verificamos se a matriz é **estritamente diagonal dominante**:
- Linha 1: $|10| > |1| + |2| \implies 10 > 3$ (OK)
- Linha 2: $|10| > |1| + |3| \implies 10 > 4$ (OK)
- Linha 3: $|10| > |2| + |3| \implies 10 > 5$ (OK)

Como o critério das linhas é atendido, o método possui convergência garantida.

---

## 2. Fórmulas de Iteração

Isolando cada variável da diagonal principal no lado esquerdo, obtemos as equações de recorrência para o passo $(k+1)$ baseado no passo $(k)$:

$$x_1^{(k+1)} = \frac{6 - x_2^{(k)} - 2x_3^{(k)}}{10}$$

$$x_2^{(k+1)} = \frac{7 - x_1^{(k)} - 3x_3^{(k)}}{10}$$

$$x_3^{(k+1)} = \frac{8 - 2x_1^{(k)} - 3x_2^{(k)}}{10}$$

---

## 3. Processo de Resolução

### Aproximação Inicial ($k=0$)
Adotamos o vetor nulo como ponto de partida:
$$x_1^{(0)} = 0, \quad x_2^{(0)} = 0, \quad x_3^{(0)} = 0$$

### Primeira Iteração ($k=1$)
Substituindo os valores iniciais ($k=0$) nas fórmulas:
- $x_1^{(1)} = \frac{6 - 0 - 2(0)}{10} = \mathbf{0.6}$
- $x_2^{(1)} = \frac{7 - 0 - 3(0)}{10} = \mathbf{0.7}$
- $x_3^{(1)} = \frac{8 - 2(0) - 3(0)}{10} = \mathbf{0.8}$

**Vetor resultante:** $(0.6, \, 0.7, \, 0.8)$

### Segunda Iteração ($k=2$)
Substituindo os valores obtidos na primeira iteração de forma simultânea:
- $x_1^{(2)} = \frac{6 - (0.7) - 2(0.8)}{10} = \frac{6 - 0.7 - 1.6}{10} = \mathbf{0.37}$
- $x_2^{(2)} = \frac{7 - (0.6) - 3(0.8)}{10} = \frac{7 - 0.6 - 2.4}{10} = \mathbf{0.40}$
- $x_3^{(2)} = \frac{8 - 2(0.6) - 3(0.7)}{10} = \frac{8 - 1.2 - 2.1}{10} = \mathbf{0.47}$

**Vetor resultante:** $(0.37, \, 0.40, \, 0.47)$

---

## 4. Conclusão
O algoritmo continua executando as iterações de forma análoga até atingir o critério de parada estabelecido pelo erro limite. A solução exata deste sistema converge para os valores aproximados:
- $x_1 \approx 0.473$
- $x_2 \approx 0.518$
- $x_3 \approx 0.550$