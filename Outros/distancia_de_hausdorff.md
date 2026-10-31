# Distância de Hausdorff

## 1. Definição

A **distância de Hausdorff** mede a diferença entre dois conjuntos não vazios de pontos em um espaço métrico. É utilizada, por exemplo, em geometria, processamento de imagens e visão computacional.

Sejam \(A\) e \(B\) dois conjuntos não vazios. A distância de Hausdorff é definida por:

$$
\[
H(A,B)=\max\{h(A,B),h(B,A)\}
\]
$$

em que:

$$
\[
h(A,B)=\sup_{a\in A}\inf_{b\in B}d(a,b)
\]
$$

e

$$
\[
h(B,A)=\sup_{b\in B}\inf_{a\in A}d(b,a).
\]
$$

### Significado dos termos

- $\(d(a,b)\)$: distância entre os pontos \(a\) e \(b\).
- $\(\inf\)$: ínfimo das distâncias — a maior cota inferior, que corresponde à menor distância quando ela é atingida.
- $\(\sup\)$: supremo das distâncias — a menor cota superior, que corresponde ao maior valor quando ele é atingido.
- $\(h(A,B)\)$: maior distância mínima dos pontos de \(A\) até o conjunto \(B\).
- $\(h(B,A)\)$: maior distância mínima dos pontos de \(B\) até o conjunto \(A\).

A distância de Hausdorff considera as duas direções para que nenhum dos conjuntos seja ignorado na comparação.

## 2. Exemplo passo a passo

Considere os conjuntos de pontos na reta real:

$$
\[
A=\{1,2,3\}
\]
$$

$$
\[
B=\{2,3,4\}
\]
$$

### Passo 1 — Calcular \(h(A,B)\)

Para cada ponto de \(A\), calcula-se a menor distância até algum ponto de \(B\):

- Ponto \(1\): distância mínima igual a \(1\).
- Ponto \(2\): distância mínima igual a \(0\).
- Ponto \(3\): distância mínima igual a \(0\).

Logo:

$$
\[
h(A,B)=\max\{1,0,0\}=1
\]
$$

### Passo 2 — Calcular \(h(B,A)\)

Para cada ponto de \(B\), calcula-se a menor distância até algum ponto de \(A\):

- Ponto \(2\): distância mínima igual a \(0\).
- Ponto \(3\): distância mínima igual a \(0\).
- Ponto \(4\): distância mínima igual a \(1\).

Logo:

$$
\[
h(B,A)=\max\{0,0,1\}=1
\]
$$

### Passo 3 — Calcular a distância de Hausdorff

$$
\[
H(A,B)=\max\{h(A,B),h(B,A)\}
\]
$$

Substituindo os valores:

$$
\[
H(A,B)=\max\{1,1\}
\]
$$

Portanto:

$$
\[
\boxed{H(A,B)=1}
\]
$$

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

## 4. Resumo

**Em síntese:** a distância de Hausdorff mede a maior distância mínima entre os pontos de dois conjuntos, considerando ambas as direções.

A definição pressupõe uma distância \(d\) no espaço considerado. Para conjuntos finitos, o supremo e o ínfimo das fórmulas correspondem, respectivamente, ao máximo e ao mínimo.





## 5. Distância de Hausdorff

A **distância de Hausdorff** ($d_H$) mede o quão distantes dois subconjuntos de um espaço métrico estão um do outro. Ela é amplamente utilizada em visão computacional, processamento de imagens e geometria computacional para comparar formas e conjuntos de pontos.

### Fórmula Geral

Para dois subconjuntos não vazios $A$ e $B$ de um espaço métrico, a distância de Hausdorff é definida como:

$$d_H(A, B) = \max \left( \sup_{a \in A} \inf_{b \in B} d(a, b), \, \sup_{b \in B} \inf_{a \in A} d(a, b) \right)$$

Onde:
* $d(a, b)$ representa a distância métrica básica (como a distância euclidiana) entre os pontos $a$ e $b$.
* $\inf_{b \in B} d(a, b)$ é a menor distância do ponto $a$ até o conjunto $B$.
* $\sup_{a \in A}$ encontra o ponto dentro de $A$ que maximiza essa distância mínima em relação a $B$.
* O cálculo é feito de forma simétrica ($A$ para $B$ e $B$ para $A$), selecionando o maior valor resultante.

### Fórmula para Conjuntos Compactos

Se os conjuntos forem compactos (como formas geométricas fechadas e limitadas no plano), os operadores de ínfimo e supremo coincidem com o mínimo e o máximo:

$$d_H(A, B) = \max \left( \max_{a \in A} \min_{b \in B} d(a, b), \, \max_{b \in B} \min_{a \in A} d(a, b) \right)$$
