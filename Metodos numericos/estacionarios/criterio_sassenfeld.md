# Critério de Sassenfeld

O **critério de Sassenfeld** é uma condição suficiente que garante a convergência do método iterativo de Gauss-Seidel para a resolução de sistemas de equações lineares, independentemente do vetor inicial $x^{(0)}$ escolhido.

---

## Como Funciona

Para aplicar o critério a um sistema de $n$ equações, calculam-se os fatores $\beta_i$ (chamados de constantes de Sassenfeld) para cada linha $i$ da matriz do sistema, de forma sequencial (de $i = 1$ até $n$):

* **Para a primeira linha ($i = 1$):**
  $$\beta_1 = \frac{\sum_{j=2}^{n} |a_{1j}|}{|a_{11}|}$$

* **Para as linhas seguintes ($i = 2, 3, \ldots, n$):**
  $$\beta_i = \frac{\sum_{j=1}^{i-1} |a_{ij}|\beta_j + \sum_{j=i+1}^{n} |a_{ij}|}{|a_{ii}|}$$

*(Onde $a_{ij}$ são os elementos da matriz dos coeficientes e $a_{ii}$ são os elementos da diagonal principal).*

---

## Regra de Convergência

1. Encontra-se o valor máximo entre todos os betas calculados: $\beta = \max(\beta_1, \beta_2, \ldots, \beta_n)$.
2. **Se $\beta < 1$**: o critério é satisfeito e a convergência pelo método de Gauss-Seidel é **garantida**.
3. Quanto **menor** for o valor de $\beta$, mais rápida será a convergência do método.
4. **Se $\beta \ge 1$**: o critério **não** garante a convergência (embora o método possa, em alguns casos específicos, convergir mesmo assim; trata-se de uma condição suficiente, mas não necessária).

---

## Exemplo Prático

Considere o seguinte sistema linear:

$$\begin{cases} 4x_1 + x_2 + x_3 = 6 \\ x_1 + 3x_2 + 2x_3 = 6 \\ x_1 + x_2 + 2x_3 = 4 \end{cases}$$

A matriz dos coeficientes $A$ deste sistema é:
$$A = \begin{pmatrix} \mathbf{4} & 1 & 1 \\ 1 & \mathbf{3} & 2 \\ 1 & 1 & \mathbf{2} \end{pmatrix}$$

### Passo a Passo do Cálculo

#### 1. Primeira Linha ($i = 1$)
Usamos apenas os elementos restantes da linha divididos pelo elemento da diagonal ($a_{11} = 4$):
$$\beta_1 = \frac{|a_{12}| + |a_{13}|}{|a_{11}|} = \frac{|1| + |1|}{|4|} = \frac{2}{4} = \mathbf{0.5}$$

#### 2. Segunda Linha ($i = 2$)
Para os elementos antes da diagonal, multiplicamos pelo $\beta$ correspondente (neste caso, $\beta_1$). O elemento da diagonal é $a_{22} = 3$:
$$\beta_2 = \frac{|a_{21}|\cdot\beta_1 + |a_{23}|}{|a_{22}|} = \frac{|1|\cdot(0.5) + |2|}{|3|} = \frac{0.5 + 2}{3} = \frac{2.5}{3} \approx \mathbf{0.833}$$

#### 3. Terceira Linha ($i = 3$)
Aqui, todos os elementos vêm antes da diagonal ($a_{33} = 2$), portanto multiplicamos ambos pelos seus respectivos $\beta$:
$$\beta_3 = \frac{|a_{31}|\cdot\beta_1 + |a_{32}|\cdot\beta_2}{|a_{33}|} = \frac{|1|\cdot(0.5) + |1|\cdot(0.833)}{|2|} = \frac{0.5 + 0.833}{2} = \frac{1.333}{2} \approx \mathbf{0.667}$$

### Conclusão do Exemplo

Agora, encontramos o maior valor de $\beta$:
$$\beta = \max(\beta_1, \beta_2, \beta_3) = \max(0.5, \, 0.833, \, 0.667) = \mathbf{0.833}$$

Como **$\beta < 1$**, o critério de Sassenfeld é satisfeito. Isso significa que o método de Gauss-Seidel **vai convergir** para a solução exata deste sistema, independentemente do chute inicial escolhido.
