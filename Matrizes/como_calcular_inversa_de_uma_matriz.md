# Como calcular a inversa de uma matriz?

A **inversa de uma matriz** é uma matriz que, quando multiplicada pela matriz original, resulta na matriz identidade. Seu cálculo é importante na Álgebra Linear, especialmente na resolução de sistemas de equações lineares.

Uma matriz quadrada \(A\) possui inversa, denotada por \(A^{-1}\), se, e somente se, for **invertível**, o que equivale a dizer que seu determinante é diferente de zero.

$
\[
AA^{-1}=A^{-1}A=I
\]
$

Em que \(I\) é a matriz identidade.

Existem diferentes métodos para calcular a inversa, como a fórmula para matrizes \(2\times2\), o método de Gauss-Jordan e a decomposição LU.

## 1. Inversa de uma matriz \(2\times2\)

Para uma matriz quadrada de ordem 2,

$
\[
A=\begin{bmatrix}a&b\\c&d\end{bmatrix}
\]
$

sua inversa é dada por:

\[
A^{-1}=\frac{1}{ad-bc}
\begin{bmatrix}d&-b\\-c&a\end{bmatrix}
\]

Essa fórmula só pode ser aplicada quando o determinante é diferente de zero:

$
\[
\det(A)=ad-bc\ne0
\]
$

### Exemplo

Considere a matriz:

$
\[
A=\begin{bmatrix}2&1\\3&2\end{bmatrix}
\]
$

**Passo 1 — Calcular o determinante.**

$
\[
\det(A)=2\cdot2-1\cdot3=4-3=1
\]
$

Como o determinante é diferente de zero, a matriz possui inversa.

**Passo 2 — Aplicar a fórmula.**

$
\[
A^{-1}=\frac{1}{1}
\begin{bmatrix}2&-1\\-3&2\end{bmatrix}
\]
$

Portanto,

$
\[
\boxed{A^{-1}=\begin{bmatrix}2&-1\\-3&2\end{bmatrix}}
\]
$

**Passo 3 — Verificar o resultado.**

$
\[
AA^{-1}=
\begin{bmatrix}2&1\\3&2\end{bmatrix}
\begin{bmatrix}2&-1\\-3&2\end{bmatrix}
=
\begin{bmatrix}1&0\\0&1\end{bmatrix}=I
\]
$

Como o resultado é a matriz identidade, a inversa está correta.

## 2. Método de Gauss-Jordan

O método de Gauss-Jordan permite calcular a inversa de matrizes quadradas de ordem superior a 2.

A ideia é construir uma matriz aumentada contendo a matriz original \(A\) à esquerda e a identidade \(I\) à direita:

$
\[
[A\mid I]
\]
$

Em seguida, aplicam-se operações elementares nas linhas até transformar a parte esquerda em \(I\). Se isso for possível, a parte direita se transforma em \(A^{-1}\):

$
\[
[A\mid I]\longrightarrow[I\mid A^{-1}]
\]
$

As operações elementares permitidas são:

- Trocar duas linhas.
- Multiplicar uma linha por um escalar não nulo.
- Somar a uma linha um múltiplo de outra linha.

### Exemplo

Considere novamente:

$
\[
A=\begin{bmatrix}2&1\\3&2\end{bmatrix}
\]
$

Construímos a matriz aumentada:

$
\[
\left[\begin{array}{cc|cc}
2&1&1&0\\
3&2&0&1
\end{array}\right]
\]
$

**Passo 1 — Transformar o primeiro elemento da primeira linha em 1.**

Dividimos a primeira linha por 2:

$
\[
L_1\leftarrow \frac{L_1}{2}
\]
$

$
\[
\left[\begin{array}{cc|cc}
1&1/2&1/2&0\\
3&2&0&1
\end{array}\right]
\]
$

**Passo 2 — Zerar o elemento abaixo do primeiro pivô.**

Subtraímos três vezes a primeira linha da segunda:

$
\[
L_2\leftarrow L_2-3L_1
\]
$

$
\[
\left[\begin{array}{cc|cc}
1&1/2&1/2&0\\
0&1/2&-3/2&1
\end{array}\right]
\]
$

**Passo 3 — Transformar o segundo pivô em 1.**

Multiplicamos a segunda linha por 2:

$
\[
L_2\leftarrow2L_2
\]
$

$
\[
\left[\begin{array}{cc|cc}
1&1/2&1/2&0\\
0&1&-3&2
\end{array}\right]
\]
$

**Passo 4 — Zerar o elemento acima do segundo pivô.**

Subtraímos metade da segunda linha da primeira:

$
\[
L_1\leftarrow L_1-\frac{1}{2}L_2
\]
$

$
\[
\left[\begin{array}{cc|cc}
1&0&2&-1\\
0&1&-3&2
\end{array}\right]
\]
$

A parte esquerda é agora a matriz identidade. A parte direita corresponde à inversa:

\[
\boxed{A^{-1}=\begin{bmatrix}2&-1\\-3&2\end{bmatrix}}
\]

O resultado é o mesmo obtido pela fórmula para matrizes \(2\times2\).

## 3. Quando uma matriz não possui inversa?

Uma matriz quadrada não possui inversa quando seu determinante é zero. Nesse caso, ela é chamada de **matriz singular**.

Por exemplo:

$
\[
B=\begin{bmatrix}1&2\\2&4\end{bmatrix}
\]
$

Seu determinante é:

$
\[
\det(B)=1\cdot4-2\cdot2=0
\]
$

Portanto, \(B\) não possui inversa.

Isso ocorre porque a segunda linha é o dobro da primeira. Assim, as linhas são linearmente dependentes e a matriz não possui posto completo.

Em geral, para uma matriz quadrada \(A\) de ordem \(n\), as seguintes condições são equivalentes:

- \(A\) possui inversa.
- \(\det(A)\ne0\).
- O posto de \(A\) é \(n\).
- As colunas de \(A\) são linearmente independentes.
- O sistema \(Ax=b\) possui solução única para todo vetor \(b\).

## 4. Relação com a resolução de sistemas lineares

Considere um sistema linear:

\[
Ax=b
\]

Se \(A\) for invertível, podemos multiplicar os dois lados pela inversa de \(A\):

\[
A^{-1}Ax=A^{-1}b
\]

Como \(A^{-1}A=I\), obtemos:

\[
Ix=A^{-1}b
\]

Portanto,

\[
\boxed{x=A^{-1}b}
\]

Essa expressão demonstra a relação entre a inversa e a solução de sistemas lineares.

Entretanto, **na prática computacional, geralmente não se calcula a inversa explicitamente apenas para resolver \(Ax=b\)**. Métodos como eliminação de Gauss, decomposição LU e métodos iterativos costumam ser mais eficientes e numericamente adequados.

## 5. Resumo para prova

| Método | Característica |
|---|---|
| Fórmula para matriz \(2\times2\) | Usa o determinante e uma fórmula direta. |
| Gauss-Jordan | Transforma a matriz aumentada \([A\mid I]\) em \([I\mid A^{-1}]\). |
| Decomposição LU | Decompõe \(A\) em matrizes triangulares e permite calcular a inversa resolvendo sistemas lineares. |
| SVD | Permite analisar a invertibilidade e calcular a pseudoinversa, inclusive para matrizes singulares ou retangulares. |

**Ideia central:** uma matriz quadrada é invertível quando seu determinante é diferente de zero. A inversa pode ser calculada por fórmulas diretas, para matrizes pequenas, ou por métodos algébricos como Gauss-Jordan, para matrizes de ordem maior.
