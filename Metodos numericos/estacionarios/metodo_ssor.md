# Método da Sobrerrelaxação Sucessiva Simétrica (SSOR)

O método **SSOR (Symmetric Successive Over-Relaxation)** é uma variante do método SOR (Sobrerrelaxação Sucessiva) projetada para que a matriz de iteração seja simétrica se a matriz original do sistema for simétrica. Ele consiste em duas meias-etapas por iteração: uma etapa do SOR convencional (passo progressivo) seguida imediatamente por uma etapa do SOR aplicada na ordem inversa das equações (passo regressivo).

---

## O Sistema Linear Exemplo

Utilizaremos o mesmo sistema linear das etapas anteriores:

$$
\begin{cases} 
10x_1 + x_2 + 2x_3 = 6 \\ 
x_1 + 10x_2 + 3x_3 = 7 \\ 
2x_1 + 3x_2 + 10x_3 = 8 
\end{cases}
$$

Adotaremos o fator de relaxação $\omega = 1.15$ e o chute inicial nulo $x^{(0)} = [0, 0, 0]^T$.

---

## Primeira Iteração ($k=1$)

### Passo 1: Passo Progressivo (Forward SOR)
É idêntico ao método SOR tradicional aplicado de $1$ até $n$:

1. **Calcular $\tilde{x}_1^{(1/2)}$ (Jacobi):**
   $$ \tilde{x}_1 = \frac{6 - 0 - 2(0)}{10} = 0.6 $$
   $$ x_1^{(1/2)} = (1 - 1.15)(0) + 1.15(0.6) = \mathbf{0.69} $$

2. **Calcular $\tilde{x}_2^{(1/2)}$ (Jacobi com atualização de $x_1$):**
   $$ \tilde{x}_2 = \frac{7 - 0.69 - 3(0)}{10} = 0.631 $$
   $$ x_2^{(1/2)} = (1 - 1.15)(0) + 1.15(0.631) = \mathbf{0.72565} $$

3. **Calcular $\tilde{x}_3^{(1/2)}$ (Jacobi com atualização de $x_1$ e $x_2$):**
   $$ \tilde{x}_3 = \frac{8 - 2(0.69) - 3(0.72565)}{10} = \frac{8 - 1.38 - 2.17695}{10} = 0.444305 $$
   $$ x_3^{(1/2)} = (1 - 1.15)(0) + 1.15(0.444305) = \mathbf{0.51095075} $$

### Passo 2: Passo Regressivo (Backward SOR)
Agora aplicamos o SOR na ordem reversa (de $n$ até $1$), partindo dos valores intermediários $x^{(1/2)}$:

1. **Calcular $x_3^{(1)}$:** Como começamos o passo regressivo por $x_3$, o valor não se altera nesta subetapa em relação ao intermediário:
   $$ x_3^{(1)} = x_3^{(1/2)} = \mathbf{0.51095075} $$

2. **Calcular $x_2^{(1)}$ (Regressivo):** Isolando $x_2$ usando o novo $x_3^{(1)}$ e o $x_1^{(1/2)}$ anterior:
   $$ \tilde{x}_2 = \frac{7 - 0.69 - 3(0.51095075)}{10} = \frac{7 - 0.69 - 1.53285225}{10} = 0.477714775 $$
   $$ x_2^{(1)} = (1 - 1.15)(0.72565) + 1.15(0.477714775) = -0.1088475 + 0.549371991 = \mathbf{0.44052449} $$

3. **Calcular $x_1^{(1)}$ (Regressivo):** Isolando $x_1$ usando os novos valores de $x_2^{(1)}$ e $x_3^{(1)}$:
   $$ \tilde{x}_1 = \frac{6 - 0.44052449 - 2(0.51095075)}{10} = \frac{6 - 0.44052449 - 1.0219015}{10} = 0.453757401 $$
   $$ x_1^{(1)} = (1 - 1.15)(0.69) + 1.15(0.453757401) = -0.1035 + 0.521821011 = \mathbf{0.41832101} $$

Vetor resultante após a primeira iteração completa do SSOR:
$$ x^{(1)} \approx [0.4183, 0.4405, 0.5110]^T $$
