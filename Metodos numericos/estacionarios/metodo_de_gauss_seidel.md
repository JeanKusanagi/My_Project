# Método de Gauss-Seidel

O **Método de Gauss-Seidel** é um algoritmo iterativo utilizado para resolver sistemas de equações lineares de grande porte. Ele é uma evolução direta do **Método de Jacobi**, projetado para convergir de forma mais rápida para a solução final.

---

## Como Funciona

Assim como no método de Jacobi, o processo começa isolando cada variável correspondente à diagonal principal da matriz. 

A grande diferença está no **momento de atualização das variáveis**:
1. **Aproveitamento imediato:** Assim que o valor de uma nova variável (por exemplo, $x_1$) é calculado na iteração atual, esse valor atualizado é **imediatamente utilizado** para calcular as próximas variáveis ($x_2, x_3, \dots$) da mesma iteração.
2. No método de Jacobi, todas as variáveis são calculadas usando apenas os valores da iteração estritamente anterior ($k$). Em Gauss-Seidel, usa-se o valor mais recente disponível.

### Formulação Matemática

Para um sistema linear $Ax = b$, a atualização de cada componente $x_i$ na iteração $k+1$ é dada por:

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)} \right)$$

---

## Critério de Convergência

O método de Gauss-Seidel possui critérios específicos que garantem que ele chegará à solução correta:

1. **Critério das Linhas (Matriz Diagonal Dominante):** Se a matriz for estritamente diagonal dominante por linhas, o método convergirará, independentemente do chute inicial.
2. **Critério de Sassenfeld:** É um critério mais poderoso e específico para Gauss-Seidel. Avalia-se o impacto das atualizações imediatas usando coeficientes $\beta_i$. Se o maior $\beta$ calculado for menor que 1, a convergência é garantida (muitas vezes convergindo onde Jacobi falharia).

---

## Exemplo Prático

Dado o sistema linear:

$$\begin{cases} 5x_1 + x_2 = 7 \\ x_1 + 4x_2 = 9 \end{cases}$$

### 1. Isolamento das Variáveis
$$x_1^{(k+1)} = \frac{7 - x_2^{(k)}}{5}$$
$$x_2^{(k+1)} = \frac{9 - x_1^{(k+1)}}{4} \quad \text{(Note o uso do } x_1 \text{ atualizado!)}$$

### 2. Iteração 1 (Chute Inicial $x^{(0)} = [0, 0]^T$)
* **Calcular $x_1^{(1)}$:**
  $$x_1^{(1)} = \frac{7 - 0}{5} = 1.4$$
* **Calcular $x_2^{(1)}$** (utilizando $x_1^{(1)} = 1.4$ imediatamente):
  $$x_2^{(1)} = \frac{9 - 1.4}{4} = \frac{7.6}{4} = 1.9$$

Vetor após a primeira iteração: $x^{(1)} = [1.4, 1.9]^T$.
