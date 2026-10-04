# Simulado: Métodos Numéricos para Resolução de Sistemas Lineares

**Instruções:**

* Responda às 30 questões de múltipla escolha (A, B, C, D ou E).
* Avalie com atenção os aspectos teóricos, algébricos, operacionais e as pegadinhas de convergência.
* Ao final de cada questão, consulte o gabarito comentado para consolidar os conceitos.

---

### Questão 1 (Fácil)

Em relação aos métodos de resolução de sistemas lineares $Ax = b$, qual é a principal diferença conceitual entre os **Métodos Diretos** e os **Métodos Iterativos**?

A) Métodos diretos encontram soluções aproximadas por refinamento sucessivo, enquanto métodos iterativos encontram a solução exata em um número infinito de passos.

B) Métodos diretos obtêm a solução exata (a menos de erros de arredondamento) em um número finito de operações aritméticas, enquanto métodos iterativos geram uma sequência de aproximações que convergem para a solução.

C) Métodos diretos só podem ser aplicados a matrizes simétricas e definidas positivas, enquanto métodos iterativos aplicam-se a qualquer matriz retangular.

D) Métodos iterativos exigem o cálculo explícito da matriz inversa $A^{-1}$, enquanto métodos diretos dispensam inversão.

E) Métodos diretos têm complexidade computacional $O(n)$, enquanto métodos iterativos têm complexidade $O(n!)$.

**Resposta Correta: B**

**Comentário:** Os métodos diretos (como a Eliminação de Gauss e Fatoração LU) chegam ao resultado exato em um número fixo/finito de passos operacionais, sofrendo apenas com erros de arredondamento inerentes à precisão finita do computador. Já os métodos iterativos (como Gauss-Jacobi e Gauss-Seidel) partem de um chute inicial $x^{(0)}$ e geram uma sequência de vetores $x^{(k)}$ que se aproximam da solução teórica conforme $k \to \infty$.

---

### Questão 2 (Médio - *Pegadinha*)

Ao aplicar o algoritmo de **Eliminação de Gauss sem pivoteamento** no sistema abaixo, qual problema computacional é encontrado no primeiro passo de eliminação?

```
| 0 2  1 | x_1 |   3 
| 1 4 -2 | x_2 | = 3 
| 2 1  1 | x_3 |   4
```

$$
\begin{bmatrix}
0 & 2 & 1 \\
1 & 4 & -2 \\
2 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
$$

=

$$
\begin{bmatrix}
3 \\
3 \\
4
\end{bmatrix}
$$

A) O determinante da matriz é igual a zero, tornando o sistema impossível.

B) O primeiro pivô é nulo ($a_{11} = 0$), impedindo a divisão para o cálculo dos multiplicadores $m_{i1}$, embora o sistema seja possível e determinado.

C) O sistema entra em um loop infinito de trocas de linhas.

D) A matriz é estritamente diagonal dominante, o que anula a Eliminação de Gauss.

E) O método resulta imediatamente em um estouro de memória (*overflow*).

**Resposta Correta: B**

**Comentário:** *Pegadinha comum!* O determinante da matriz é $\det(A) = 0 \cdot (4 - (-2)) - 2 \cdot (1 - (-4)) + 1 \cdot (1 - 8) = -10 - 7 = -17 \neq 0$, o que significa que o sistema é perfeitamente possível e possui solução única. No entanto, o algoritmo de Eliminação de Gauss **sem pivoteamento** falha categoricamente porque o multiplicador é $m_{i1} = a_{i1}/a_{11}$, gerando uma divisão por zero ($a_{11} = 0$). Isso demonstra a necessidade do pivoteamento parcial (troca de linhas).

---

### Questão 3 (Difícil)

Na **Fatoração LU** de uma matriz quadrada $A$ de ordem $n$, decompõe-se $A = L \cdot U$, onde $L$ é triangular inferior e $U$ é triangular superior. Se adotarmos a convenção de **Doolittle** (onde os elementos da diagonal principal de $L$ são iguais a 1, ou seja, $l_{ii} = 1$), quantos cálculos de multiplicadores da Eliminação de Gauss são armazenados na matriz $L$?

A) $n^2$

B) $\frac{n(n-1)}{2}$

C) $n$

D) $n(n+1)$

E) $\frac{n(n+1)}{2}$

**Resposta Correta: B**

**Comentário:** Em uma matriz $n \times n$, os elementos estritamente abaixo da diagonal principal correspondem ao número de multiplicadores $m_{ij}$ gerados durante a eliminação gaussiana. A quantidade de elementos abaixo da diagonal é dada por $\frac{n^2 - n}{2} = \frac{n(n-1)}{2}$. Como a diagonal principal de $L$ é fixada em $1$ (decomposição de Doolittle), basta armazenar esses $\frac{n(n-1)}{2}$ multiplicadores abaixo da diagonal.

---

### Questão 4 (Médio)

A **Decomposição de Cholesky** é uma variação extremamente eficiente da fatoração $LU$ aplicável apenas a um classe específica de matrizes. Quais são as condições **necessárias e suficientes** sobre a matriz real $A$ para garantir a existência e unicidade da decomposição $A = R^T R$ (onde $R$ é uma matriz triangular superior com diagonal estritamente positiva)?

A) A matriz $A$ deve ser simétrica e singular.

B) A matriz $A$ deve ser simétrica e definida positiva.

C) A matriz $A$ precisa apenas ser tridiagonal e ter determinante nulo.

D) A matriz $A$ deve ser antissimétrica e ter norma infinita menor que 1.

E) A matriz $A$ precisa ser estritamente triangular inferior.

**Resposta Correta: B**

**Comentário:** O **Teorema de Cholesky** estabelece que uma matriz real $A$ admite uma decomposição única da forma $A = R^T R$ (com $R$ triangular superior de diagonal positiva) se, e somente se, $A$ for **simétrica** ($A = A^T$) e **definida positiva** ($x^T A x > 0$ para todo $x \neq 0$, o que também equivale a dizer que todos os seus autovalores e menores principais são estritamente positivos).

---

### Questão 5 (Fácil)

Qual é a complexidade de tempo assintótica (em termos de operações de ponto flutuante - FLOPs) para resolver um sistema linear $Ax = b$ de ordem $n$ utilizando a **Eliminação de Gauss** tradicional?

A) $O(n)$

B) $O(n \log n)$

C) $O(n^2)$

D) $O(n^3)$

E) $O(2^n)$

**Resposta Correta: D**

**Comentário:** A fase de eliminação (triangularização) da Eliminação de Gauss requer aproximadamente $\frac{2}{3}n^3$ operações aritméticas (multiplicações e subtrações). A fase de substituição regressiva requer $O(n^2)$ operações. Portanto, o comportamento assintótico dominante do método é $O(n^3)$.

---

### Questão 6 (Difícil - *Pegadinha*)

Considere o **Critério das Linhas** (Sassenfeld / Diagonal Dominante) para o método iterativo de **Gauss-Jacobi**. Dada a matriz $A$:

$$
A = \begin{bmatrix}
5 & 2 & 1 \\
1 & 4 & 2 \\
2 & -3 & 6
\end{bmatrix}
$$

A matriz $A$ satisfaz o Critério das Linhas para garantir a convergência do método de Gauss-Jacobi para qualquer chute inicial?

A) Não, porque $5 < 2 + 1 + 4$.

B) Sim, pois para cada linha $i$, tem-se $|a_{ii}| > \sum_{j \neq i} |a_{ij}|$.

C) Não, pois o elemento $a_{32} = -3$ é negativo e anula a convergência.

D) Sim, mas apenas se o vetor inicial $x^{(0)}$ for o vetor nulo.

E) Não, pois o determinante de $A$ é negativo.

**Resposta Correta: B**

**Comentário:** *Pegadinha de checagem linha a linha!* Vamos verificar o critério da matriz estritamente diagonal dominante por linhas:
- Linha 1: $|a_{11}| = |5| = 5$. Soma dos outros: $|2| + |1| = 3$. Como $5 > 3$, ok.
- Linha 2: $|a_{22}| = |4| = 4$. Soma dos outros: $|1| + |2| = 3$. Como $4 > 3$, ok.
- Linha 3: $|a_{33}| = |6| = 6$. Soma dos outros: $|2| + |-3| = 5$. Como $6 > 5$, ok.
Como $|a_{ii}| > \sum_{j \neq i} |a_{ij}|$ para **todas** as linhas $i=1,2,3$, a matriz é estritamente diagonal dominante por linhas, o que é condição **suficiente** para garantir a convergência do Método de Gauss-Jacobi (e também do Gauss-Seidel).

---

### Questão 7 (Médio)

Qual é a principal diferença entre a atualização das variáveis no **Método de Gauss-Jacobi** e no **Método de Gauss-Seidel** durante uma iteração $k+1$?

A) O método de Gauss-Jacobi usa derivadas parciais, enquanto Gauss-Seidel usa aproximações por diferenças finitas.

B) No método de Gauss-Jacobi, todos os componentes do novo vetor $x^{(k+1)}$ são calculados usando estritamente os valores do vetor anterior $x^{(k)}$; no método de Gauss-Seidel, os valores $x_i^{(k+1)}$ recém-calculados na mesma iteração são imediatamente utilizados para calcular os componentes seguintes $x_j^{(k+1)}$ ($j > i$).

C) Gauss-Jacobi só funciona para matrizes simétricas, enquanto Gauss-Seidel aplica-se apenas a matrizes não-quadradas.

D) Gauss-Seidel requer duas inversões matriciais por iteração, enquanto Gauss-Jacobi requer três.

E) Não há diferença prática; ambos geram rigorosamente os mesmos valores em todas as iterações intermediárias.

**Resposta Correta: B**

**Comentário:** No método de Gauss-Jacobi, a atualização é em "bloco paralelizável": $x_i^{(k+1)}$ depende exclusivamente de $x^{(k)}$. No Método de Gauss-Seidel, adota-se a estratégia de "substituição sucessiva imediata": para calcular $x_i^{(k+1)}$, utilizam-se os valores já atualizados $x_1^{(k+1)}, x_2^{(k+1)}, \dots, x_{i-1}^{(k+1)}$ da iteração corrente, o que em geral acelera a velocidade de convergência.

---

### Questão 8 (Difícil - *Pegadinha*)

Considere o número de condicionamento de uma matriz não-singular $A$, definido por $\text{cond}(A) = \|A\| \cdot \|A^{-1}\|$. Assinale a afirmativa **CORRETA** sobre sistemas mal condicionados:

A) Se $\text{cond}(A)$ for muito próximo de 1, o sistema é considerado mal condicionado e pequenas perturbações em $b$ causam erros gigantescos em $x$.

B) Se $\text{cond}(A) \gg 1$ (muito grande), o sistema é mal condicionado, significando que pequenas variações ou erros de arredondamento nos dados de entrada podem provocar grandes variações na solução $x$.

C) O menor valor possível para o número de condicionamento em qualquer norma induzida é $0$.

D) Se $\text{cond}(A)$ for elevado, a Eliminação de Gauss garante precisão absoluta sem propagação de erros de arredondamento.

E) O número de condicionamento de uma matriz identidade $I$ é infinito.

**Resposta Correta: B**

**Comentário:** *Pegadinha sobre os valores de cond(A)!* Para qualquer norma matricial induzida, o menor valor teórico possível para $\text{cond}(A)$ é **1** (alcançado pela matriz identidade $I$, pois $\|I\| \cdot \|I^{-1}\| = 1 \cdot 1 = 1$). Um valor $\text{cond}(A) \approx 1$ indica um sistema **bem condicionado** (estável). Quando $\text{cond}(A)$ é imenso ($\gg 1$), o sistema é **mal condicionado**, e os erros relativos nos dados/arredondamentos podem ser amplificados por um fator proporcional a $\text{cond}(A)$.

---

### Questão 9 (Médio)

Seja um sistema linear $Ax = b$ de ordem 3. Suponha que, após aplicar a Eliminação de Gauss com pivoteamento, obtemos a decomposição $P A = L U$, onde $P$ é a matriz de permutação. Como a solução final $x$ deve ser computada eficientemente através de duas substituições?

A) Resolver $L y = P b$ por substituição progressiva e, em seguida, resolver $U x = y$ por substituição regressiva.

B) Resolver $U y = b$ por substituição regressiva e $L x = P y$ por substituição progressiva.

C) Multiplicar $x = U^{-1} L^{-1} P b$ diretamente via produto matricial denso.

D) Resolver $P y = b$ e depois $L U x = P$.

E) Inverter $P$ e calcular $x = L U b$.

**Resposta Correta: A**

**Comentário:** A partir de $P A x = P b$ e sabendo que $P A = L U$, temos $L (U x) = P b$.
1. Fazemos a substituição de variável $y = U x$.
2. Resolvemos o sistema triangular inferior $L y = P b$ para obter $y$ (Substituição Progressiva - *Forward Substitution*).
3. Resolvemos o sistema triangular superior $U x = y$ para obter $x$ (Substituição Regressiva - *Backward Substitution*).
Isso custa apenas $O(n^2)$ operações, preservando a eficiência da fatoração.

---

### Questão 10 (Fácil)

Em um método iterativo para solução de sistemas lineares, qual das opções a seguir representa o **Vetor Resíduo** $r^{(k)}$ na $k$-ésima iteração, associado à aproximação $x^{(k)}$?

A) $r^{(k)} = x^{(k)} - x^{(k-1)}$

B) $r^{(k)} = b - A x^{(k)}$

C) $r^{(k)} = A^{-1} b$

D) $r^{(k)} = \frac{\|x^{(k)}\|}{\|b\|}$

E) $r^{(k)} = \det(A) \cdot x^{(k)}$

**Resposta Correta: B**

**Comentário:** O vetor resíduo mede o "desconto" ou o quanto a aproximação atual $x^{(k)}$ falha em satisfazer a equação exata $Ax = b$. Ele é definido por $r^{(k)} = b - A x^{(k)}$. Conforme a aproximação $x^{(k)}$ se aproxima da solução exata $x^*$, o vetor resíduo $r^{(k)}$ tende ao vetor nulo.

---

### Questão 11 (Difícil - *Pegadinha*)

O **Critério de Sassenfeld** é uma condição suficiente para garantir a convergência de qual método iterativo, oferecendo uma condição frequentemente mais fraca (mais fácil de satisfazer) do que o critério das linhas simples?

A) Método de Eliminação de Gauss com Pivoteamento Total

B) Método de Cholesky

C) Método de Gauss-Seidel

D) Método de Gauss-Jordan

E) Regra de Cramer

**Resposta Correta: C**

**Comentário:** O **Critério de Sassenfeld** calcula fatores $\beta_i$ que levam em consideração que o Método de **Gauss-Seidel** utiliza os valores já atualizados dentro da própria iteração. Se $\max_i (\beta_i) < 1$, o método de Gauss-Seidel converge para qualquer vetor inicial. O critério das linhas simples garante a convergência tanto de Jacobi quanto de Gauss-Seidel, mas o Critério de Sassenfeld é específico para provar a convergência do Gauss-Seidel mesmo quando o critério das linhas simples falha.

---

### Questão 12 (Médio)

Considere a matriz $A$ triangular inferior:

$$
A = \begin{bmatrix}
2 & 0 & 0 \\
3 & 4 & 0 \\
1 & -2 & 5
\end{bmatrix}
$$

Ao resolver o sistema $A x = b$ com $b = [4, 10, 3]^T$ por **substituição progressiva** (*forward substitution*), qual é o valor do vetor solução $x = [x_1, x_2, x_3]^T$?

A) $x = [2, 1, 0.6]^T$

B) $x = [2, 1, 0.6]^T$

C) $x = [2, 1, 0]^T$

D) $x = [2, 1, 0.6]^T$

E) $x = [2, 1, 0.6]^T$

*(Ajustando as opções de cálculo:)*
- $2 x_1 = 4 \implies x_1 = 2$.
- $3(2) + 4 x_2 = 10 \implies 6 + 4 x_2 = 10 \implies 4 x_2 = 4 \implies x_2 = 1$.
- $1(2) - 2(1) + 5 x_3 = 3 \implies 2 - 2 + 5 x_3 = 3 \implies 5 x_3 = 3 \implies x_3 = 0.6$.

A) $x = [2, 1, 0.6]^T$

B) $x = [1, 2, 0.5]^T$

C) $x = [2, -1, 1]^T$

D) $x = [4, 10, 3]^T$

E) $x = [0, 1, 2]^T$

**Resposta Correta: A**

**Comentário:** 
1. $2 x_1 = 4 \implies x_1 = 2$.
2. $3 x_1 + 4 x_2 = 10 \implies 3(2) + 4 x_2 = 10 \implies 6 + 4 x_2 = 10 \implies 4 x_2 = 4 \implies x_2 = 1$.
3. $x_1 - 2 x_2 + 5 x_3 = 3 \implies 2 - 2(1) + 5 x_3 = 3 \implies 0 + 5 x_3 = 3 \implies x_3 = 3/5 = 0.6$.
Portanto, $x = [2, 1, 0.6]^T$.

---

### Questão 13 (Difícil)

Para analisar a convergência de um método iterativo genérico da forma $x^{(k+1)} = C x^{(k)} + g$ (onde $C$ é a matriz de iteração), qual é a condição **necessária e suficiente** para que o método converja para a solução única a partir de qualquer chute inicial $x^{(0)}$?

A) O determinante da matriz de iteração $C$ deve ser exatamente 1.

B) O raio espectral da matriz de iteração, denotado por $\rho(C) = \max_i |\lambda_i(C)|$, deve ser estritamente menor que 1 ($\rho(C) < 1$).

C) A matriz $C$ deve ser simétrica e ter trace igual a zero.

D) O raio espectral da matriz $C$ deve ser maior que o número de condicionamento de $A$.

E) Todos os autovalores de $C$ devem ser números reais estritamente negativos.

**Resposta Correta: B**

**Comentário:** O teorema fundamental da convergência de métodos iterativos estatísticos afirma que a sequência de erros $e^{(k)} = C^k e^{(0)}$ tende a zero para qualquer $e^{(0)}$ se, e somente se, $\lim_{k \to \infty} C^k = 0$, o que equivale matematicamente a dizer que o **raio espectral** $\rho(C) < 1$ (o maior módulo dentre todos os autovalores da matriz de iteração $C$ é estritamente menor que 1).

---

### Questão 14 (Médio - *Pegadinha*)

Por que a **Regra de Cramer** é praticamente descartada na prática computacional para resolver sistemas lineares $Ax = b$ de grande porte (ex: $n \ge 20$), apesar de fornecer uma fórmula analítica exata?

A) Porque a Regra de Cramer exige que a matriz $A$ seja triangular superior.

B) Porque o custo computacional da Regra de Cramer usando cálculo clássico de determinantes cresce na ordem de $O((n+1)!)$, tornando o tempo de processamento astronomicamente inviável.

C) Porque a Regra de Cramer só funciona se o vetor $b$ for composto inteiramente por números inteiros.

D) Porque a Regra de Cramer gera soluções imaginárias para matrizes reais.

E) Porque ela introduz erros de truncamento em sistemas pequenos de ordem $n=2$.

**Resposta Correta: B**

**Comentário:** *Pegadinha sobre complexidade!* A Regra de Cramer calcula $n+1$ determinantes de ordem $n$. Se os determinantes forem calculados pela expansão por cofatores (definição direta), a complexidade é da ordem de $O((n+1)!)$. Para $n=20$, $(21)! \approx 5.1 \times 10^{19}$ operações, o que levaria séculos no supercomputador mais rápido do mundo, enquanto a Eliminação de Gauss ($O(n^3)$) resolve em uma fração de segundo.

---

### Questão 15 (Fácil)

Qual é o objetivo principal da estratégia de **Pivoteamento Parcial** na Eliminação de Gauss?

A) Garantir que a matriz final seja diagonal.

B) Evitar divisões por zero ou por números muito próximos de zero em módulo, trocando linhas para colocar o elemento de maior valor absoluto na posição do pivô, reduzindo a amplificação de erros de arredondamento.

C) Reduzir a dimensão da matriz pela metade a cada iteração.

D) Converter uma matriz não-simétrica em uma matriz simétrica definida positiva.

E) Eliminar a necessidade de realizar a substituição regressiva.

**Resposta Correta: B**

**Comentário:** Se o pivô $a_{kk}^{(k)}$ for muito pequeno em módulo, o multiplicador $m_{ik} = \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}$ será imenso em módulo. Ao multiplicar a linha do pivô por um número gigante e subtraí-la de outra linha, os erros de arredondamento da máquina são drasticamente amplificados (perda de precisão). O pivoteamento parcial troca a linha atual por outra linha abaixo que contenha o maior $|a_{ik}|$, garantindo que $|m_{ik}| \le 1$.

---

### Questão 16 (Difícil)

Em um método iterativo para $Ax = b$, escreve-se a matriz $A$ como $A = M - N$, onde $M$ é uma matriz não-singular de fácil inversão. A equação de iteração é $M x^{(k+1)} = N x^{(k)} + b$. Para o **Método de Gauss-Jacobi**, como a matriz $A$ é decomposta em termos de sua parte diagonal ($D$), triangular inferior estrita ($-L$) e triangular superior estrita ($-U$), de modo que $A = D - L - U$?

A) $M = D$ e $N = L + U$

B) $M = D - L$ e $N = U$

C) $M = L$ e $N = D + U$

D) $M = D - U$ e $N = L$

E) $M = D + L + U$ e $N = 0$

**Resposta Correta: A**

**Comentário:**
Se dividirmos $A = D - L - U$, onde $D$ é a diagonal principal, $-L$ é a parte estritamente inferior e $-U$ é a parte estritamente superior:
- **Gauss-Jacobi:** Toma $M = D$ e $N = L + U$. Assim, $D x^{(k+1)} = (L + U) x^{(k)} + b \implies x^{(k+1)} = D^{-1}(L + U) x^{(k)} + D^{-1}b$. A matriz de iteração é $C_J = D^{-1}(L + U)$.
- **Gauss-Seidel:** Toma $M = D - L$ e $N = U$. Assim, $(D - L) x^{(k+1)} = U x^{(k)} + b$. A matriz de iteração é $C_{GS} = (D - L)^{-1} U$.

---

### Questão 17 (Médio - *Pegadinha*)

Dada a norma do infinito de um vetor $x \in \mathbb{R}^n$, definida por $\|x\|_\infty = \max_{1 \le i \le n} |x_i|$. Qual é a **norma matricial do infinito** $\|A\|_\infty$ induzida para uma matriz $A_{n \times n}$?

A) A maior soma dos valores absolutos dos elementos de uma coluna (Soma Máxima por Coluna).

B) A maior soma dos valores absolutos dos elementos de uma linha (Soma Máxima por Linha): $\max_{1 \le i \le n} \sum_{j=1}^n |a_{ij}|$.

C) A soma de todos os elementos da matriz elevados ao quadrado.

D) O valor absoluto do determinante de $A$.

E) O maior autovalor de $A$ em módulo.

**Resposta Correta: B**

**Comentário:** *Pegadinha entre norma de linha e norma de coluna!*
- Norma do Infinito $\|A\|_\infty$: É a **Soma Máxima Absoluta por Linha** $\max_i \sum_j |a_{ij}|$.
- Norma 1 $\|A\|_1$: É a **Soma Máxima Absoluta por Coluna** $\max_j \sum_i |a_{ij}|$.
Lembrar dessa distinção é fundamental para o cálculo de números de condicionamento em prova.

---

### Questão 18 (Médio)

Considere o sistema linear de 2 equações e 2 incógnitas:

$$
\begin{aligned}
2 x_1 + x_2 &= 5 \\
x_1 + 2 x_2 &= 4
\end{aligned}
$$

Partindo do vetor inicial $x^{(0)} = [0, 0]^T$, calcule a primeira aproximação $x^{(1)} = [x_1^{(1)}, x_2^{(1)}]^T$ obtida pelo **Método de Gauss-Jacobi**.

A) $x^{(1)} = [2.5, 2.0]^T$

B) $x^{(1)} = [2.5, 0.75]^T$

C) $x^{(1)} = [5.0, 4.0]^T$

D) $x^{(1)} = [0.0, 0.0]^T$

E) $x^{(1)} = [1.0, 1.0]^T$

**Resposta Correta: A**

**Comentário:** Isolando as variáveis na diagonal principal:
- $x_1^{(k+1)} = \frac{5 - x_2^{(k)}}{2}$
- $x_2^{(k+1)} = \frac{4 - x_1^{(k)}}{2}$

Para $k=0$, usando $x^{(0)} = [0, 0]^T$:
- $x_1^{(1)} = \frac{5 - 0}{2} = 2.5$
- $x_2^{(1)} = \frac{4 - 0}{2} = 2.0$

Portanto, $x^{(1)} = [2.5, 2.0]^T$.

---

### Questão 19 (Difícil - *Pegadinha*)

Usando o **mesmo** sistema da questão anterior:

$$
\begin{aligned}
2 x_1 + x_2 &= 5 \\
x_1 + 2 x_2 &= 4
\end{aligned}
$$

Partindo do vetor inicial $x^{(0)} = [0, 0]^T$, qual é a primeira aproximação $x^{(1)} = [x_1^{(1)}, x_2^{(1)}]^T$ obtida pelo **Método de Gauss-Seidel**?

A) $x^{(1)} = [2.5, 2.0]^T$

B) $x^{(1)} = [2.5, 0.75]^T$

C) $x^{(1)} = [1.5, 1.25]^T$

D) $x^{(1)} = [2.0, 1.0]^T$

E) $x^{(1)} = [0.0, 2.5]^T$

**Resposta Correta: B**

**Comentário:** *Pegadinha do uso imediato da variável recém-calculada!*
Formulas de atualização:
- $x_1^{(k+1)} = \frac{5 - x_2^{(k)}}{2}$
- $x_2^{(k+1)} = \frac{4 - x_1^{(k+1)}}{2}$  <-- Usa $x_1^{(1)}$ atualizado!

Para $k=0$, com $x^{(0)} = [0, 0]^T$:
1. $x_1^{(1)} = \frac{5 - 0}{2} = 2.5$.
2. $x_2^{(1)} = \frac{4 - x_1^{(1)}}{2} = \frac{4 - 2.5}{2} = \frac{1.5}{2} = 0.75$.

Portanto, no Gauss-Seidel $x^{(1)} = [2.5, 0.75]^T$ (diferente de Gauss-Jacobi que deu $[2.5, 2.0]^T$).

---

### Questão 20 (Fácil)

Em um contexto de computação científica, o que representa uma matriz **esparsa**?

A) Uma matriz que possui apenas elementos positivos em todas as posições.

B) Uma matriz retangular onde o número de colunas é estritamente maior que o número de linhas.

C) Uma matriz na qual a maioria esmagadora de seus elementos é igual a zero.

D) Uma matriz cujo determinante é infinito.

E) Uma matriz que possui autovalores complexos conjugados.

**Resposta Correta: C**

**Comentário:** Uma matriz é dita **esparsa** quando uma fração significativa de suas entradas é nula (zero). Para esse tipo de matriz (comum em discretização de equações diferenciais via elementos finitos/diferenças finitas), métodos iterativos ou métodos diretos estruturados são preferidos para economizar memória e tempo de processamento, armazenando apenas os elementos não-nulos.

---

### Questão 21 (Difícil)

O método **SOR** (*Successive Over-Relaxation*) é uma extrapolação do método de Gauss-Seidel que introduz um parâmetro de relaxamento $\omega$. Se o parâmetro for escolhido no intervalo $1 < \omega < 2$, o método é chamado de sobre-relaxamento. Qual é o papel principal da escolha ótima do fator $\omega$?

A) Converter a matriz $A$ em uma matriz diagonal.

B) Reduzir o raio espectral da matriz de iteração do método, acelerando significativamente a taxa de convergência em comparação ao Gauss-Seidel padrão.

C) Permitir a resolução de sistemas onde $\det(A) = 0$.

D) Eliminar a necessidade de armazenar o vetor de termos independentes $b$.

E) Garantir que todas as iterações tenham erro nulo a partir do passo $k=2$.

**Resposta Correta: B**

**Comentário:** O Método SOR modifica a atualização de Gauss-Seidel: $x_i^{(k+1)} = (1-\omega) x_i^{(k)} + \omega x_i^{GS}$. O parâmetro $\omega$ é projetado para diminuir o raio espectral $\rho(C_{SOR})$. Para problemas específicos (como equações elípticas), a escolha apropriada do $\omega_{ótimo} \in (1, 2)$ pode acelerar drasticamente a convergência, reduzindo o número de iterações necessárias de $O(n^2)$ para $O(n)$. Se $\omega = 1$, o SOR reduz-se ao Gauss-Seidel clássico.

---

### Questão 22 (Médio - *Pegadinha*)

Seja $A$ uma matriz de ordem $n$. Se o determinante de $A$ for muito pequeno (por exemplo, $\det(A) = 10^{-50}$), podemos afirmar categoricamente que o sistema $Ax = b$ é mal condicionado?

A) Sim, pois determinante próximo de zero sempre implica número de condicionamento gigantesco.

B) Não, pois o determinante pode ser tornado arbitrariamente pequeno apenas multiplicando a matriz por uma constante escalar $c < 1$ (uma vez que $\det(cA) = c^n \det(A)$), sem alterar o verdadeiro condicionamento do sistema.

C) Sim, porque o determinante é numericamente igual à norma da matriz inversa.

D) Não, porque determinantes pequenos só ocorrem em matrizes simétricas definidas positivas.

E) Sim, pois $\det(A)$ é o único indicador confiável de estabilidade numérica em sistemas lineares.

**Resposta Correta: B**

**Comentário:** *Pegadinha teórica clássica!* O determinante **NÃO** é uma medida confiável de condicionamento. Exemplo: considere a matriz identidade de ordem $100$ multiplicada por $0.1$, $A = 0.1 \times I_{100}$. O determinante é $\det(A) = (0.1)^{100} = 10^{-100}$ (extremamente pequeno). No entanto, $A^{-1} = 10 \times I_{100}$, e $\text{cond}(A) = \|A\| \cdot \|A^{-1}\| = 0.1 \times 10 = 1$. O sistema é perfeitamente bem condicionado! O determinante escala exponencialmente com a dimensão $n$, enquanto o número de condicionamento é invariante por escala.

---

### Questão 23 (Fácil)

Ao utilizar o critério de parada baseado na norma da diferença entre duas iterações consecutivas $\|x^{(k+1)} - x^{(k)}\| < \epsilon$, qual cuidado adicional é recomendável tomar quando os valores do vetor solução $x$ possuem ordem de grandeza muito distante de 1 (muito grandes ou muito pequenos)?

A) Utilizar o erro relativo entre iterações: $\frac{\|x^{(k+1)} - x^{(k)}\|}{\|x^{(k+1)}\|} < \epsilon$.

B) Multiplicar a tolerância $\epsilon$ por $n!$.

C) Ignorar o critério de parada e parar sempre exatamente na iteração $k=1000$.

D) Trocar todos os elementos negativos por seus valores absolutos no vetor $b$.

E) Dividir o vetor $x^{(k)}$ por $\det(A)$ a cada passo.

**Resposta Correta: A**

**Comentário:** Se a solução do sistema tiver componentes da ordem de $10^6$, uma variação $\|x^{(k+1)} - x^{(k)}\| = 0.01$ representa um erro relativo minúsculo. Por outro lado, se a solução for da ordem de $10^{-5}$, essa mesma variação absoluta seria gigantesca. Portanto, o **erro relativo** $\frac{\|x^{(k+1)} - x^{(k)}\|}{\|x^{(k+1)}\|} < \epsilon$ é o critério robusto recomendado por evitar dependência da escala do problema.

---

### Questão 24 (Difícil)

Deseja-se resolver o sistema linear $Ax = b$ utilizando o **Método dos Gradientes Conjugados**. Qual conjunto de propriedades a matriz $A$ deve obrigatoriamente satisfazer para que a teoria clássica dos Gradientes Conjugados garanta convergência exata em no máximo $n$ passos (em aritmética exata)?

A) Matriz triangular e não-singular.

B) Matriz simétrica e definida positiva.

C) Matriz ortogonal e tridiagonal.

D) Matriz antissimétrica e densa.

E) Matriz estritamente diagonal dominante por colunas.

**Resposta Correta: B**

**Comentário:** O Método dos Gradientes Conjugados é um método de otimização/sistemas lineares extremamente poderoso para matrizes de grande porte que sejam **Simétricas e Definidas Positivas (SDP)**. Ele minimiza a função quadrática $f(x) = \frac{1}{2} x^T A x - b^T x$. Em aritmética exata, a ortogonalidade das direções de busca garante a convergência para a solução exata em no máximo $n$ iterações.

---

### Questão 25 (Médio - *Pegadinha*)

Seja a matriz $A = \begin{bmatrix} 1 & 1000 \\ 0 & 1 \end{bmatrix}$. Calcule $\|A\|_\infty$ e $\|A^{-1}\|_\infty$ e determine o número de condicionamento $\text{cond}_\infty(A)$.

A) $\text{cond}_\infty(A) = 1$

B) $\text{cond}_\infty(A) = 1001^2 = 1.002.001$

C) $\text{cond}_\infty(A) = 1000$

D) $\text{cond}_\infty(A) = 2002$

E) $\text{cond}_\infty(A) = 0$

**Resposta Correta: B**

**Comentário:** *Pegadinha do cálculo da matriz inversa e norma!*
1. $\|A\|_\infty = \max(|1| + |1000|, |0| + |1|) = \max(1001, 1) = 1001$.
2. Inversa de $A$: Para $A = \begin{bmatrix} 1 & 1000 \\ 0 & 1 \end{bmatrix}$, a inversa é $A^{-1} = \begin{bmatrix} 1 & -1000 \\ 0 & 1 \end{bmatrix}$.
3. $\|A^{-1}\|_\infty = \max(|1| + |-1000|, |0| + |1|) = \max(1001, 1) = 1001$.
4. $\text{cond}_\infty(A) = \|A\|_\infty \cdot \|A^{-1}\|_\infty = 1001 \times 1001 = 1.002.001$.
Apesar do determinante ser $1$, a presença do elemento $1000$ fora da diagonal torna a matriz mal condicionada!

---

### Questão 26 (Fácil)

Em uma matriz tridiagonal de ordem $n$, os únicos elementos não-nulos estão localizados na diagonal principal, na superdiagonal (acima da principal) e na subdiagonal (abaixo da principal). Qual algoritmo especializado executa a fatoração $LU$ para matrizes tridiagonais em tempo linear $O(n)$?

A) Algoritmo de Thomas (ou Tridiagonal Matrix Algorithm - TDMA)

B) Regra de Cramer Tridiagonal

C) Algoritmo de Strassen

D) Método do Gradiente Descendente sem Pré-condicionador

E) Decomposição em Valores Singulares (SVD)

**Resposta Correta: A**

**Comentário:** O **Algoritmo de Thomas** é uma versão simplificada e adaptada da Eliminação de Gauss projetada especificamente para matrizes tridiagonais. Como ele opera apenas com três diagonais, ele elimina as entradas não-nulas abaixo da diagonal em apenas $O(n)$ operações e exige apenas $O(n)$ de espaço de armazenamento, em comparação com os $O(n^3)$ da Eliminação de Gauss genérica.

---

### Questão 27 (Difícil)

Deseja-se resolver um sistema $Ax = b$ mal condicionado utilizando um método iterativo como os Gradientes Conjugados. Para acelerar a convergência e reduzir o número de condicionamento do sistema transformado, aplica-se uma técnica conhecida como **Pré-condicionamento**. A ideia central do pré-condicionamento consiste em:

A) Multiplicar o sistema por uma matriz pré-condicionadora $M^{-1}$ tal que $M^{-1} A \approx I$, fazendo com que o novo sistema $M^{-1} A x = M^{-1} b$ tenha um número de condicionamento muito mais próximo de 1.

B) Alterar o vetor $b$ substituindo suas entradas por zeros até que o determinante seja 1.

C) Arredondar todas as entradas da matriz $A$ para os números inteiros mais próximos.

D) Inverter a matriz $A$ usando cálculo simbólico exato antes das iterações.

E) Adicionar uma constante $\lambda \to \infty$ a todos os elementos fora da diagonal principal.

**Resposta Correta: A**

**Comentário:** O pré-condicionamento escolhe uma matriz $M$ de forma que $M \approx A$, mas $M$ seja fácil de inverter (ou resolver sistemas da forma $M y = r$). Ao resolver o sistema equivalente $M^{-1}A x = M^{-1} b$, o operador pré-condicionado $M^{-1}A$ possui autovalores muito mais agrupados e um número de condicionamento $\text{cond}(M^{-1}A) \approx 1$, acelerando dramaticamente a convergência do algoritmo iterativo.

---

### Questão 28 (Médio)

Considere o sistema de equações $Ax = b$ onde $A$ é uma matriz triangular superior não-singular. O método numérico exato indicado para resolver este sistema é:

A) Substituição Progressiva (*Forward Substitution*)

B) Substituição Regressiva (*Backward Substitution*)

C) Método de Gauss-Jacobi

D) Método do Gradiente Conjugado

E) Decomposição de Cholesky

**Resposta Correta: B**

**Comentário:** Para matrizes **triangulares superiores** (onde $a_{ij} = 0$ para $i > j$), a última equação contém apenas a incógnita $x_n$. Assim, resolve-se $x_n$ em primeiro lugar e "volta-se para trás" isolando $x_{n-1}, x_{n-2}, \dots, x_1$. Esse processo chama-se **Substituição Regressiva** (*Backward Substitution*). Para matrizes triangular inferiores, o processo inverso chama-se Substituição Progressiva.

---

### Questão 29 (Difícil - *Pegadinha*)

Seja o sistema linear $Ax = b$ de ordem $n$. Se soubermos previamente a Fatoração LU de $A$ ($A = L U$), qual é a complexidade computacional em número de FLOPs para resolver o sistema para um **novo vetor de termos independentes** $b_{novo}$?

A) $O(n^3)$

B) $O(n^2)$

C) $O(n \log n)$

D) $O(n)$

E) $O(2^n)$

**Resposta Correta: B**

**Comentário:** *Pegadinha de reuso da decomposição!* O custo pesado de $O(n^3)$ ocorre **apenas uma vez** durante o cálculo das matrizes $L$ e $U$ (fatoração). Uma vez que $L$ e $U$ já estão armazenadas na memória, resolver o sistema para qualquer novo lado direito $b$ envolve apenas uma substituição progressiva $L y = b$ (custo $\approx n^2$) e uma substituição regressiva $U x = y$ (custo $\approx n^2$). O custo total para novos vetores $b$ é de apenas $O(n^2)$, o que torna a Fatoração LU superior à Eliminação de Gauss quando temos múltiplos sistemas com a mesma matriz $A$.

---

### Questão 30 (Médio)

O **Teorema de Gerschgorin** (ou Círculos de Gerschgorin) é uma ferramenta poderosa na análise de matrizes de sistemas lineares. Ele permite:

A) Calcular analiticamente a matriz inversa sem realizar divisões.

B) Localizar e delimitar as regiões no plano complexo onde se encontram os autovalores de uma matriz, sem a necessidade de calcular o polinômio característico.

C) Garantir que todos os sistemas lineares possuem pelo menos duas soluções reais.

D) Determinar exatamente o tempo de execução do pivoteamento total em segundos.

E) Converter automaticamente um sistema denso em um sistema esparso tridiagonal.

**Resposta Correta: B**

**Comentário:** O **Teorema dos Discos de Gerschgorin** estabelece que todos os autovalores de uma matriz complexa $A_{n \times n}$ estão contidos na união de $n$ discos fechados $D_i$ no plano complexo, onde cada disco é centrado em um elemento da diagonal $a_{ii}$ e possui raio $R_i = \sum_{j \neq i} |a_{ij}|$ (a soma dos módulos das entradas fora da diagonal na linha $i$). Isso é extremamente útil para estimar o raio espectral $\rho(A)$ e analisar a convergência de métodos iterativos sem resolver o problema de autovalores.
