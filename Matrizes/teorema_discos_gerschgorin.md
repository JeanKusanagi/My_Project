# Teorema dos Discos de Gerschgorin

O **Teorema dos Discos de Gerschgorin** (também grafado *Gershgorin*) é um resultado da Álgebra Linear Numérica que permite **estimar a localização dos autovalores de uma matriz quadrada no plano complexo**, sem precisar calculá-los diretamente.

O teorema é útil na análise de convergência de métodos numéricos, no estudo de sistemas lineares e na análise de propriedades espectrais de matrizes.

## 1. Definição do teorema

Seja \(A\) uma matriz quadrada de ordem \(n\), com elementos \(a_{ij}\). O teorema estabelece que todos os autovalores de \(A\) estão contidos na união de \(n\) discos fechados no plano complexo, chamados **discos de Gerschgorin**.

Cada disco é definido por:

\[
D_i=\left\{z\in\mathbb{C}:|z-a_{ii}|\leq R_i\right\}
\]

Em que:

- \(a_{ii}\): elemento da diagonal principal da matriz \(A\); corresponde ao centro do disco.
- \(R_i\): raio do disco, calculado pela soma dos valores absolutos dos elementos da linha \(i\), excluindo o elemento da diagonal principal.

O raio é dado por:

\[
R_i=\sum_{\substack{j=1\\j\neq i}}^n |a_{ij}|
\]

Portanto, cada disco tem como centro o elemento diagonal \(a_{ii}\) e como raio a soma dos módulos dos demais elementos da mesma linha.

O teorema garante que:

\[
\sigma(A)\subseteq\bigcup_{i=1}^{n}D_i
\]

Aqui, \(\sigma(A)\) representa o conjunto dos autovalores da matriz \(A\).

**Interpretação:** todos os autovalores da matriz devem estar dentro de pelo menos um dos discos definidos pelas linhas da matriz.

## 2. Exemplo de aplicação

Considere a matriz:

\[
A=
\begin{bmatrix}
4&1&0\\
2&5&1\\
0&1&3
\end{bmatrix}
\]

Vamos determinar os discos de Gerschgorin associados às suas três linhas.

### Passo 1 — Primeiro disco

A primeira linha é \([4,\ 1,\ 0]\).

O centro é:

\[
c_1=a_{11}=4
\]

O raio é:

\[
R_1=|1|+|0|=1
\]

Logo:

\[
D_1=\{z\in\mathbb{C}:|z-4|\leq1\}
\]

Esse disco tem centro em \(4\) e raio \(1\).

### Passo 2 — Segundo disco

A segunda linha é \([2,\ 5,\ 1]\).

O centro é:

\[
c_2=a_{22}=5
\]

O raio é:

\[
R_2=|2|+|1|=3
\]

Portanto:

\[
D_2=\{z\in\mathbb{C}:|z-5|\leq3\}
\]

O segundo disco tem centro em \(5\) e raio \(3\).

### Passo 3 — Terceiro disco

A terceira linha é \([0,\ 1,\ 3]\).

O centro é:

\[
c_3=a_{33}=3
\]

O raio é:

\[
R_3=|0|+|1|=1
\]

Assim:

\[
D_3=\{z\in\mathbb{C}:|z-3|\leq1\}
\]

O terceiro disco tem centro em \(3\) e raio \(1\).

### Passo 4 — Interpretar os resultados

| Disco | Centro | Raio | Intervalo correspondente no eixo real |
|---|---:|---:|---|
| \(D_1\) | 4 | 1 | De 3 a 5 |
| \(D_2\) | 5 | 3 | De 2 a 8 |
| \(D_3\) | 3 | 1 | De 2 a 4 |

Como os centros são reais, os discos se estendem ao redor desses centros no plano complexo. Neste exemplo, o disco de centro \(5\) e raio \(3\) engloba os outros dois. Logo, todos os autovalores pertencem a esse disco e satisfazem:

\[
2\leq\operatorname{Re}(\lambda)\leq8
\]

e

\[
|\operatorname{Im}(\lambda)|\leq3
\]

Essas desigualdades delimitam uma região que contém os autovalores; não significam que eles assumam necessariamente esses valores extremos.

## 3. Relação com a convergência de métodos iterativos

O teorema também pode auxiliar na análise de métodos numéricos para resolução de sistemas lineares, como Jacobi e Gauss-Seidel.

Uma propriedade importante é a **dominância diagonal estrita por linhas**, definida por:

\[
|a_{ii}|>\sum_{j\neq i}|a_{ij}|,\qquad i=1,\ldots,n
\]

Essa condição significa que, em cada linha, o módulo do elemento diagonal é maior que a soma dos módulos dos demais elementos.

Geometricamente, cada disco de Gerschgorin tem raio menor que a distância de seu centro à origem.

A dominância diagonal estrita por linhas é uma condição suficiente para garantir a convergência dos métodos de Jacobi e Gauss-Seidel para sistemas lineares com matriz de coeficientes não singular.

**Atenção:** o teorema de Gerschgorin, isoladamente, não garante a convergência desses métodos. Ele fornece limites para a localização dos autovalores; a convergência depende das propriedades da matriz de iteração associada ao método.

## 4. Principais aplicações

O Teorema dos Discos de Gerschgorin pode ser utilizado para:

- **Estimar os autovalores:** delimitar regiões onde os autovalores podem estar localizados.
- **Analisar estabilidade:** obter informações sobre a localização do espectro de uma matriz.
- **Estudar métodos iterativos:** auxiliar na análise de propriedades espectrais relacionadas à convergência.
- **Verificar propriedades de matrizes:** obter informações sobre a localização dos autovalores sem resolver explicitamente o polinômio característico.

## Resumo para prova escrita

O Teorema dos Discos de Gerschgorin estabelece que os autovalores de uma matriz quadrada pertencem à união de discos no plano complexo. Cada disco tem centro no elemento da diagonal principal de uma linha e raio igual à soma dos módulos dos elementos restantes dessa linha. O teorema permite estimar a localização dos autovalores com baixo custo computacional, sendo útil na análise espectral de matrizes, na investigação da estabilidade de sistemas e no estudo de métodos iterativos para resolução de sistemas lineares.
