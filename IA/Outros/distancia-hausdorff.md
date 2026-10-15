# Distância de Hausdorff

## O que é

A **distância de Hausdorff** mede o quão distantes estão dois **conjuntos** de pontos em um espaço métrico. Enquanto a distância usual compara dois pontos, a de Hausdorff compara dois subconjuntos inteiros (curvas, formas, nuvens de pontos, contornos de imagens).

Ideia intuitiva: ela responde à pergunta *"no pior caso, qual é a maior distância que preciso percorrer para ir de um ponto de um conjunto até o conjunto mais próximo do outro?"*

## Definição formal

Seja $(X, d)$ um espaço métrico e $A, B \subseteq X$ não vazios.

**Distância direcionada** de $A$ para $B$:

$$h(A, B) = \sup_{a \in A} \; \inf_{b \in B} \; d(a, b)$$

**Distância de Hausdorff** (simétrica):

$$d_H(A, B) = \max\{\, h(A, B),\; h(B, A) \,\}$$

**Definição equivalente** (por vizinhanças): sendo $A_\varepsilon$ a união de todas as bolas de raio $\varepsilon$ centradas em pontos de $A$,

$$d_H(A, B) = \inf\{\, \varepsilon > 0 : A \subseteq B_\varepsilon \;\text{ e }\; B \subseteq A_\varepsilon \,\}$$

## Por que usar o máximo das duas direções?

A distância direcionada $h(A, B)$ **não é simétrica**. Exemplo: se $A$ é um único ponto dentro de uma região $B$ grande, $h(A, B) = 0$, mas $h(B, A)$ pode ser grande. Tomar o máximo garante que os dois conjuntos "cobrem" um ao outro.

## Propriedades

- $d_H(A, B) \ge 0$ e $d_H(A, B) = d_H(B, A)$.
- $d_H(A, B) = 0$ se e somente se $\overline{A} = \overline{B}$ (os fechos coincidem).
- Vale a desigualdade triangular: $d_H(A, C) \le d_H(A, B) + d_H(B, C)$.
- Sobre o conjunto dos subconjuntos **compactos não vazios** de $X$, $d_H$ é uma **métrica** (e, se $X$ é completo, esse espaço também é completo).
- É sensível a *outliers*: um único ponto muito distante domina o valor.

## Exemplo numérico

Sejam $A = \{(0,0),\ (1,0)\}$ e $B = \{(0,1),\ (3,0)\}$ no plano com distância euclidiana.

**Cálculo de $h(A, B)$:**

- Para $(0,0)$: distâncias a $B$ são $1$ e $3$ → mínimo $= 1$.
- Para $(1,0)$: distâncias a $B$ são $\sqrt{2}$ e $2$ → mínimo $= \sqrt{2}$.
- $h(A, B) = \max\{1, \sqrt{2}\} = \sqrt{2} \approx 1{,}41$.

**Cálculo de $h(B, A)$:**

- Para $(0,1)$: distâncias a $A$ são $1$ e $\sqrt{2}$ → mínimo $= 1$.
- Para $(3,0)$: distâncias a $A$ são $3$ e $2$ → mínimo $= 2$.
- $h(B, A) = \max\{1, 2\} = 2$.

**Resultado:** $d_H(A, B) = \max\{\sqrt{2},\ 2\} = 2$.

## Cálculo em Python

```python
import numpy as np
from scipy.spatial.distance import directed_hausdorff

A = np.array([[0, 0], [1, 0]])
B = np.array([[0, 1], [3, 0]])

h_ab = directed_hausdorff(A, B)[0]
h_ba = directed_hausdorff(B, A)[0]
d_h = max(h_ab, h_ba)

print(h_ab, h_ba, d_h)  # 1.414..., 2.0, 2.0
```

## Complexidade

- Algoritmo ingênuo para conjuntos finitos com $n$ e $m$ pontos: $O(nm)$.
- Em 2D, é possível obter $O((n + m)\log(n + m))$ usando diagramas de Voronoi.
- Há algoritmos práticos com *early break* e amostragem aleatória (Taha & Hanbury, 2015) que reduzem muito o tempo médio, e é esse tipo de abordagem que o SciPy usa.

## Variantes para lidar com outliers

| Variante | Ideia |
|---|---|
| **Hausdorff parcial** | Usa o $k$-ésimo maior valor (ou um quantil) em vez do supremo. |
| **HD95** | Usa o percentil 95 das distâncias; muito comum em segmentação médica. |
| **Hausdorff modificada (Dubuisson & Jain, 1994)** | Troca o supremo pela **média** das distâncias mínimas. |
| **Chamfer distance** | Soma ou média das distâncias ao ponto mais próximo; usada em nuvens de pontos 3D. |

## Aplicações

- **Visão computacional:** casamento de contornos e reconhecimento de objetos.
- **Imagens médicas:** avaliação de segmentações (comparar o contorno previsto com o de referência).
- **Computação gráfica e CAD:** comparação de malhas e superfícies, medindo erro de simplificação.
- **GIS:** similaridade entre geometrias e trajetórias.
- **Matemática:** topologia, análise e teoria de fractais (espaço de conjuntos compactos).

## Resumo

A distância de Hausdorff quantifica a **pior discrepância** entre dois conjuntos, considerando as duas direções. É uma métrica bem fundamentada, simples de interpretar e muito útil, mas sensível a ruído, motivo pelo qual variantes como HD95 e a versão modificada são comuns na prática.

## Referências

- Hausdorff, F. *Grundzüge der Mengenlehre* (1914).
- Huttenlocher, D. P.; Klanderman, G. A.; Rucklidge, W. J. "Comparing images using the Hausdorff distance", *IEEE TPAMI*, 1993.
- Dubuisson, M.-P.; Jain, A. K. "A modified Hausdorff distance for object matching", *ICPR*, 1994.
- Taha, A. A.; Hanbury, A. "An efficient algorithm for calculating the exact Hausdorff distance", *IEEE TPAMI*, 2015.
