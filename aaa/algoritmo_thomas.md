# Algoritmo de Thomas (Matrizes Tridiagonais)

O **Algoritmo de Thomas** é uma simplificação da Eliminação Gaussiana otimizada para resolver sistemas de equações lineares tridiagonais. Ele reduz a complexidade computacional de $O(n^3)$ para apenas $O(n)$, sendo amplamente utilizado na resolução numérica de equações diferenciais (como o Método de Diferenças Finitas).

---

## 1. O Problema Tridiagonal

Um sistema tridiagonal possui coeficientes não nulos apenas na diagonal principal, na subdiagonal (abaixo) e na superdiagonal (acima). O sistema pode ser representado como:

$$
\begin{bmatrix} 
b_1 & c_1 & 0 & \dots & 0 \\ 
a_2 & b_2 & c_2 & \dots & 0 \\ 
0 & a_3 & b_3 & \dots & 0 \\ 
\vdots & \vdots & \ddots & \ddots & \vdots \\ 
0 & 0 & \dots & a_n & b_n 
\end{bmatrix} 
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_n \end{bmatrix} = 
\begin{bmatrix} d_1 \\ d_2 \\ d_3 \\ \vdots \\ d_n \end{bmatrix}
$$

Onde:
* $b_i$: Elementos da diagonal principal.
* $a_i$: Elementos da subdiagonal ($a_1 = 0$).
* $c_i$: Elementos da superdiagonal ($c_n = 0$).
* $d_i$: Vetor de termos independentes.

---

## 2. O Algoritmo

O método é dividido em duas etapas consecutivas:

### Fase 1: Varredura para a Frente (Eliminação)
Modificamos os coeficientes originais para eliminar a subdiagonal $a_i$, transformando a matriz em uma matriz triangular superior unitária com coeficientes ajustados $c'_i$ e $d'_i$.

1. Para a primeira linha ($i = 1$):
   $$c'_1 = \frac{c_1}{b_1} , \quad d'_1 = \frac{d_1}{b_1}$$

2. Para as linhas seguintes ($i = 2$ até $n$):
   $$c'_i = \frac{c_i}{b_i - a_i c'_{i-1}}$$
   $$d'_i = \frac{d_i - a_i d'_{i-1}}{b_i - a_i c'_{i-1}}$$
   *(Nota: Como $c_n = 0$, o cálculo de $c'_n$ não é necessário).*

### Fase 2: Varredura para Trás (Substituição)
Com a matriz escalonada, calculamos os valores das incógnitas $x_i$ começando do último elemento até o primeiro:

1. Para a última linha ($i = n$):
   $$x_n = d'_n$$

2. Para as linhas restantes (de $i = n-1$ até $1$):
   $$x_i = d'_i - c'_i x_{i+1}$$

---

## 3. Exemplo Numérico Passo a Passo

Vamos resolver o seguinte sistema $3 \times 3$:

$$
\begin{bmatrix} 
2 & 1 & 0 \\ 
1 & 2 & 1 \\ 
0 & 1 & 2 
\end{bmatrix} 
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = 
\begin{bmatrix} 4 \\ 8 \\ 8 \end{bmatrix}
$$

### Vetores de Entrada:
* $a = [0, 1, 1]$
* $b = [2, 2, 2]$
* $c = [1, 1, 0]$
* $d = [4, 8, 8]$

### Executando a Fase 1 (Varredura para frente):
* **Para $i = 1$:**
  $$c'_1 = \frac{1}{2} = 0.5$$
  $$d'_1 = \frac{4}{2} = 2.0$$

* **Para $i = 2$:**
  $$c'_2 = \frac{1}{2 - 1(0.5)} = \frac{1}{1.5} \approx 0.6667$$
  $$d'_2 = \frac{8 - 1(2.0)}{2 - 1(0.5)} = \frac{6}{1.5} = 4.0$$

* **Para $i = 3$:**
  $$d'_3 = \frac{8 - 1(4.0)}{2 - 1(0.6667)} = \frac{4}{1.3333} = 3.0$$

### Executando a Fase 2 (Varredura para trás):
* **Para $i = 3$:**
  $$x_3 = d'_3 = 3.0$$
* **Para $i = 2$:**
  $$x_2 = d'_2 - c'_2 x_3 = 4.0 - 0.6667(3.0) = 4.0 - 2.0 = 2.0$$
* **Para $i = 1$:**
  $$x_1 = d'_1 - c'_1 x_2 = 2.0 - 0.5(2.0) = 2.0 - 1.0 = 1.0$$

---

## 4. Solução Final

O vetor solução obtido de forma exata é:
$$x = \begin{bmatrix} 1.0 \\ 2.0 \\ 3.0 \end{bmatrix}$$