# Inversa de uma Matriz por Gauss-Jordan

O método de **Gauss-Jordan** é uma das formas mais eficientes e estruturadas para calcular a matriz inversa ($A^{-1}$) de uma matriz quadrada invertível $A$.

---

## O Conceito Fundamental

Para encontrar a inversa, nós construímos uma **matriz aumentada** colocando a matriz original $A$ ao lado da **matriz identidade** $I$ de mesma ordem:

$$[A \mid I]$$

Aplicamos as **operações elementares de linha** de forma simultânea em ambos os lados. O objetivo é transformar o lado esquerdo (onde está a matriz $A$) na matriz identidade $I$. Quando alcançamos esse objetivo, o lado direito se transforma automaticamente na matriz inversa $A^{-1}$:

$$[I \mid A^{-1}]$$

Se, durante o processo, uma linha inteira do lado esquerdo se tornar zero, a matriz **não possui inversa** (é uma matriz singular).

---

## Exemplo Passo a Passo

Vamos calcular a inversa da seguinte matriz $2 \times 2$:

$$A = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}$$

### Passo 1: Construir a Matriz Aumentada $[A \mid I]$

$$\left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 4 & 3 & 0 & 1 \end{array}\right)$$

### Passo 2: Criar o pivô 1 na primeira linha ($L_1$)
Dividimos a primeira linha ($L_1$) por $2$:

$$L_1 \leftarrow \frac{1}{2} L_1$$

$$\left(\begin{array}{cc|cc} 1 & 0.5 & 0.5 & 0 \\ 4 & 3 & 0 & 1 \end{array}\right)$$

### Passo 3: Zerar o elemento abaixo do pivô na coluna 1 ($L_2$)
Subtraímos $4$ vezes a primeira linha da segunda linha ($L_2$):

$$
L_2 \leftarrow L_2 - 4L_1
$$

*Cálculo auxiliar para $L_2$:*
* $4 - 4(1) = 0$
* $3 - 4(0.5) = 1$
* $0 - 4(0.5) = -2$
* $1 - 4(0) = 1$

$$\left(\begin{array}{cc|cc} 1 & 0.5 & 0.5 & 0 \\ 0 & 1 & -2 & 1 \end{array}\right)$$

*(Note que o elemento da diagonal na segunda linha já virou $1$ de forma natural neste exemplo!).*

### Passo 4: Zerar o elemento acima do pivô na coluna 2 ($L_1$)
Subtraímos $0.5$ vezes a segunda linha da primeira linha ($L_1$):

$$L_1 \leftarrow L_1 - 0.5L_2$$

*Cálculo auxiliar para $L_1$:*
* $1 - 0.5(0) = 1$
* $0.5 - 0.5(1) = 0$
* $0.5 - 0.5(-2) = 0.5 + 1 = 1.5$
* $0 - 0.5(1) = -0.5$

$$\left(\begin{array}{cc|cc} 
1 & 0 & 1.5 & -0.5 \\
0 & 1 & -2 & 1 
\end{array}\right)$$

---

## Resultado Final

Como o lado esquerdo se tornou a matriz identidade, o lado direito é a nossa matriz inversa:

$$A^{-1} = \begin{pmatrix} 1.5 & -0.5 \\ -2 & 1 \end{pmatrix}$$

### Verificação ($A \times A^{-1} = I$)

$$\begin{pmatrix} 
2 & 1 \\
4 & 3 
\end{pmatrix}
\begin{pmatrix} 
1.5 & -0.5 \\
-2 & 1 
\end{pmatrix} = 
\begin{pmatrix}
2(1.5)+1(-2) & 2(-0.5)+1(1) \\
4(1.5)+3(-2) & 4(-0.5)+3(1) 
\end{pmatrix} = 
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}$$

A verificação confirma que o cálculo está **correto**!
