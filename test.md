### Questão 25 (Médio - *Pegadinha*)

Seja a matriz 

$$
A = \begin{bmatrix} 
1 & 1000 \\ 
0 & 1 
\end{bmatrix}.
$$

Calcule $\|A\|_\infty$ 

e $\|A^{-1}\|_\infty$ 

e determine o número de condicionamento $\text{cond}_\infty(A)$.

A) $\text{cond}_\infty(A) = 1$

B) $\text{cond}_\infty(A) = 1001^2 = 1.002.001$

C) $\text{cond}_\infty(A) = 1000$

D) $\text{cond}_\infty(A) = 2002$

E) $\text{cond}_\infty(A) = 0$

**Resposta Correta: B**

**Comentário:** *Pegadinha do cálculo da matriz inversa e norma!*
1. $\|A\|_\infty = \max(|1| + |1000|, |0| + |1|) = \max(1001, 1) = 1001 $.
2. Inversa de $A$: Para

$$
A = \begin{bmatrix} 
1 & 1000 \\ 
0 & 1 
\end{bmatrix}$$
$$

a inversa é

$$
A^{-1} = \begin{bmatrix} 
1 & -1000 \\ 
0 & 1 
\end{bmatrix}
$$
   
3. $\|A^{-1}\|_\infty = \max(|1| + |-1000|, |0| + |1|) = \max(1001, 1) = 1001 $.

4.
$$\text{cond}_\infty(A) = \|A\|_\infty \cdot \|A^{-1}\|_\infty = 1001 \times 1001 = 1.002.001 $$

Apesar do determinante ser $1$, a presença do elemento $1000$ fora da diagonal torna a matriz mal condicionada!
