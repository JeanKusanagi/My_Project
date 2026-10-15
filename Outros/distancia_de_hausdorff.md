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

## 3. Aplicações

A distância de Hausdorff é utilizada para:

- Comparar formas geométricas e contornos.
- Avaliar semelhanças e diferenças entre imagens.
- Comparar nuvens de pontos em visão computacional.
- Medir diferenças entre objetos representados por conjuntos de pontos.

## 4. Resumo

**Em síntese:** a distância de Hausdorff mede a maior distância mínima entre os pontos de dois conjuntos, considerando ambas as direções.

A definição pressupõe uma distância \(d\) no espaço considerado. Para conjuntos finitos, o supremo e o ínfimo das fórmulas correspondem, respectivamente, ao máximo e ao mínimo.
