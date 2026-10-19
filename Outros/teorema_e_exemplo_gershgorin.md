# Teorema dos Discos de Gershgorin

O **Teorema dos Discos de Gershgorin** (ou Teorema do Círculo de Gershgorin) é um resultado fundamental da álgebra linear numérica usado para estimar e delimitar a localização dos **autovalores** de uma matriz quadrada no plano complexo sem a necessidade de calculá-los explicitamente.

---

## 1. Definição Teórica

Dada uma matriz quadrada $A = [a_{ij}]$ de tamanho $n \times n$ com entradas reais ou complexas, todos os autovalores $\lambda$ de $A$ estão contidos na união de $n$ discos fechados no plano complexo, chamados **Discos de Gershgorin**.

Cada disco $D_i$ associado à linha $i$ é definido por:

* **Centro ($c_i$):** O elemento da diagonal principal da linha $i$:
  $$c_i = a_{ii}$$
* **Raio ($R_i$):** A soma dos módulos de todos os outros elementos da mesma linha $i$:
  $$R_i = \sum_{j \neq i} |a_{ij}|$$

Matematicamente, o disco é o conjunto de pontos $z$ no plano complexo que satisfazem:
$$D_i = \{ z \in \mathbb{C} : |z - a_{ii}| \leq R_i \}$$

O espectro da matriz, $\sigma(A)$, cumpre a seguinte inclusão:
$$\sigma(A) \subset \bigcup_{i=1}^{n} D_i$$

### Propriedades Importantes
1. **Versão por Colunas:** O teorema também é válido se os raios forem calculados somando os elementos das colunas (excluindo a diagonal). Portanto, os autovalores estão contidos na interseção da união dos discos por linhas com a união dos discos por colunas.
2. **Componentes Conexas:** Se a união de $k$ discos for disjunta (completamente separada) dos outros $n-k$ discos, então essa união isolada contém exatamente $k$ autovalores da matriz (contando suas multiplicidades algébricas).
3. **Invertibilidade:** Se nenhum dos discos contiver a origem $(0,0)$, a matriz é *estritamente diagonalmente dominante* e, consequentemente, é **invertível** (pois zero não pode ser um autovalor).

---

## 2. Exemplo Prático de Cálculo

Considere a seguinte matriz real $A$ de tamanho $3 \times 3$:

$$A = \begin{pmatrix} 4 & 1 & 1 \\ 0.5 & 8 & 0.5 \\ 1 & -0.5 & 12 \end{pmatrix}$$

Vamos calcular o centro e o raio de cada um dos três discos correspondentes às linhas da matriz:

### Disco 1 (Linha 1)
* **Centro ($c_1$):** $a_{11} = 4$
* **Raio ($R_1$):** $|a_{12}| + |a_{13}| = |1| + |1| = 2$
* **Equação:** $|z - 4| \leq 2$
* **Intervalo no eixo real:** $[2, 6]$

### Disco 2 (Linha 2)
* **Centro ($c_2$):** $a_{22} = 8$
* **Raio ($R_2$):** $|a_{21}| + |a_{23}| = |0.5| + |0.5| = 1$
* **Equação:** $|z - 8| \leq 1$
* **Intervalo no eixo real:** $[7, 9]$

### Disco 3 (Linha 3)
* **Centro ($c_3$):** $a_{33} = 12$
* **Raio ($R_3$):** $|a_{31}| + |a_{32}| = |1| + |-0.5| = 1 + 0.5 = 1.5$
* **Equação:** $|z - 12| \leq 1.5$
* **Intervalo no eixo real:** $[10.5, 13.5]$

---

## 3. Análise dos Resultados

A união dos três discos define a região onde todos os autovalores de $A$ obrigatoriamente se encontram:

$$\text{Região} = D_1 \cup D_2 \cup D_3$$

Ao analisar os intervalos gerados no eixo real, podemos observar:
* $D_1 \rightarrow [2, 6]$
* $D_2 \rightarrow [7, 9]$
* $D_3 \rightarrow [10.5, 13.5]$

### Conclusões:
1. **Discos Disjuntos:** Como os intervalos não se sobrepõem ($[2,6] \cap [7,9] = \emptyset$, etc.), os três discos são completamente disjuntos. Pela propriedade das componentes conexas, isto garante que **existe exatamente um autovalor em cada disco**.
2. **Invertibilidade:** A origem $z = 0$ não pertence a nenhum dos discos (o menor valor coberto é $2$). Portanto, a matriz $A$ é estritamente diagonalmente dominante e **invertível**.
