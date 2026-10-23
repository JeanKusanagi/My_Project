# Fatoração LU e Decomposição com Pivotamento Parcial

A **fatoração LU** (ou decomposição LU) é um método fundamental de álgebra linear e cálculo numérico que fatora uma matriz quadrada $A$ no produto de duas matrizes triangulares:
* **L (Lower / Triangular Inferior):** Possui elementos igual a $1$ na diagonal principal e os multiplicadores da eliminação nas posições abaixo dela.
* **U (Upper / Triangular Superior):** É a matriz resultante após a aplicação da eliminação de Gauss.

Quando não há trocas de linhas, a equação é dada por:
$$A = LU$$

Quando o pivotamento parcial é necessário para evitar divisões por zero ou reduzir erros numéricos, a equação assume a forma:
$$PA = LU$$
Onde **P** é uma matriz de permutação que registra a troca de linhas.

---

## Para que serve?

A principal aplicação da fatoração LU é a **resolução eficiente de sistemas lineares** da forma $Ax = b$. 

Em vez de aplicar a eliminação de Gauss inteira para cada novo vetor $b$, o sistema original é dividido em dois sistemas triangulares extremamente simples de resolver por substituição:
1. **$Ly = b$** (ou $Ly = Pb$ se houver pivotamento), resolvido por substituição progressiva para encontrar $y$.
2. **$Ux = y$**, resolvido por substituição retroativa para encontrar o vetor solução final $x$.

---

## 1. Exemplo Sem Pivotamento

Queremos resolver o sistema linear $Ax = b$, onde:
$$A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix}$$

### Passo 1.1: Encontrar as matrizes L e U
Começamos com $U$ sendo uma cópia de $A$ e $L$ como a matriz identidade:
$$L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} \mathbf{2} & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$$

* **Zerar a coluna 1 abaixo do pivô ($U_{11} = 2$):**
  * Para a Linha 2: O multiplicador é $m_{21} = \frac{4}{2} = \mathbf{2}$. Fazemos $L_2 \leftarrow L_2 - 2 \cdot L_1$.
  * Para a Linha 3: O multiplicador é $m_{31} = \frac{8}{2} = \mathbf{4}$. Fazemos $L_3 \leftarrow L_3 - 4 \cdot L_1$.
  * Guardamos $2$ e $4$ na primeira coluna de $L$.

$$L = \begin{pmatrix} 1 & 0 & 0 \\ \mathbf{2} & 1 & 0 \\ \mathbf{4} & 0 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & \mathbf{1} & 1 \\ 0 & 3 & 5 \end{pmatrix}$$

* **Zerar a coluna 2 abaixo do pivô ($U_{22} = 1$):**
  * Para a Linha 3: O multiplicador é $m_{32} = \frac{3}{1} = \mathbf{3}$. Fazemos $L_3 \leftarrow L_3 - 3 \cdot L_2$.
  * Guardamos $3$ na segunda coluna de $L$.

$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & \mathbf{3} & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$

### Passo 1.2: Resolver $Ly = b$ (Substituição Progressiva)
$$\begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix}$$
* **Linha 1:** $y_1 = \mathbf{1}$
* **Linha 2:** $2(1) + y_2 = 2 \implies y_2 = \mathbf{0}$
* **Linha 3:** $4(1) + 3(0) + y_3 = 5 \implies y_3 = \mathbf{1}$

Logo, $y = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$.

### Passo 1.3: Resolver $Ux = y$ (Substituição Retroativa)
$$\begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$
* **Linha 3:** $2x_3 = 1 \implies x_3 = \mathbf{\frac{1}{2}}$
* **Linha 2:** $x_2 + \frac{1}{2} = 0 \implies x_2 = \mathbf{-\frac{1}{2}}$
* **Linha 1:** $2x_1 - \frac{1}{2} + \frac{1}{2} = 1 \implies 2x_1 = 1 \implies x_1 = \mathbf{\frac{1}{2}}$

**Solução Final:** $x = \begin{pmatrix} 1/2 \\ -1/2 \\ 1/2 \end{pmatrix}$

---

## 2. Exemplo com Pivotamento Parcial ($PA = LU$)

O **pivotamento parcial** é necessário quando encontramos um pivô nulo ou muito próximo de zero. Vamos utilizar a seguinte matriz $A$ e o vetor $b$:
$$A = \begin{pmatrix} 0 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 4 \\ 3 \end{pmatrix}$$

### Passo 2.1: Fatoração com Troca de Linhas
Como $A_{11} = 0$, buscamos o maior elemento em módulo na primeira coluna, que é o **2** (na linha 2). Permutamos a Linha 1 com a Linha 2 em $U$ e na matriz de permutação $P$.

$$P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} \mathbf{2} & 4 & 2 \\ 0 & 2 & 1 \\ 1 & 2 & 3 \end{pmatrix}$$

* **Eliminação na Coluna 1:**
  * Linha 2 já possui zero ($m_{21} = 0$).
  * Linha 3: O multiplicador é $m_{31} = \frac{1}{2} = \mathbf{0.5}$. Fazemos $L_3 \leftarrow L_3 - 0.5 \cdot L_1$.

$$L = \begin{pmatrix} 1 & 0 & 0 \\ \mathbf{0} & 1 & 0 \\ \mathbf{0.5} & 0 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 4 & 2 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$

### Passo 2.2: Ajustar o vetor com $Pb$
Multiplicamos a matriz de permutação pelo vetor de termos independentes original:
$$Pb = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 4 \\ 3 \end{pmatrix} = \begin{pmatrix} \mathbf{4} \\ \mathbf{1} \\ \mathbf{3} \end{pmatrix}$$

### Passo 2.3: Resolver $Ly = Pb$ (Substituição Progressiva)
$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0.5 & 0 & 1 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 3 \end{pmatrix}$$
* **Linha 1:** $y_1 = \mathbf{4}$
* **Linha 2:** $y_2 = \mathbf{1}$
* **Linha 3:** $0.5(4) + y_3 = 3 \implies 2 + y_3 = 3 \implies y_3 = \mathbf{1}$

Logo, $y = \begin{pmatrix} 4 \\ 1 \\ 1 \end{pmatrix}$.

### Passo 2.4: Resolver $Ux = y$ (Substituição Retroativa)
$$\begin{pmatrix} 2 & 4 & 2 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 1 \end{pmatrix}$$
* **Linha 3:** $2x_3 = 1 \implies x_3 = \mathbf{\frac{1}{2}}$
* **Linha 2:** $2x_2 + \frac{1}{2} = 1 \implies 2x_2 = \frac{1}{2} \implies x_2 = \mathbf{\frac{1}{4}}$
* **Linha 1:** $2x_1 + 4\left(\frac{1}{4}\right) + 2\left(\frac{1}{2}\right) = 4 \implies 2x_1 + 1 + 1 = 4 \implies 2x_1 = 2 \implies x_1 = \mathbf{1}$

**Solução Final:** $x = \begin{pmatrix} 1 \\ 1/4 \\ 1/2 \end{pmatrix}$