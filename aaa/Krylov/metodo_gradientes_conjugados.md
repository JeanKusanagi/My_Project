# Método dos Gradientes Conjugados e Variantes

O **método do gradiente conjugado (CG)** é um algoritmo iterativo utilizado para resolver sistemas de equações lineares do tipo $Ax = b$, especialmente quando a matriz $A$ é grande, simétrica e definida positiva.

Proposto por Hestenes e Stiefel em 1952, CG é particularmente adequado à resolução de sistemas lineares cuja matriz (A) é simétrica definida positiva (SPD). Em aritmética exata, para uma matriz de dimensão (n), o método converge para a solução em no máximo (n) iterações. Na prática, devido à estrutura espectral da matriz e aos efeitos da aritmética de ponto flutuante, a convergência pode ocorrer em um número significativamente menor de iterações, geralmente, quando um critério de tolerância é atingido. A velocidade de convergência depende, entre outros fatores, do condicionamento e da distribuição dos autovalores de (A), sendo comum o emprego de técnicas de pré-condicionamento para melhorar esse comportamento. Sistemas bem condicionados tendem a apresentar convergência mais rápida, enquanto sistemas mal condicionados podem exigir técnicas adicionais.

Diferentemente dos métodos diretos baseados em fatoração, o CG gera iterativamente uma sequência de direções conjugadas em relação à matriz (A) e busca a solução do sistema por meio da minimização da função quadrática

$$
f(x)=(½) xᵀAx − bᵀx.
$$

A solução do sistema Ax=b corresponde ao ponto de mínimo desta função). Isso permite que as informações obtidas nas iterações anteriores sejam aproveitadas de maneira mais eficiente, em vez de seguir simplesmente a direção do gradiente, como ocorre no método do gradiente descendente.

Como a matriz (A) é SPD, essa função é estritamente convexa e possui um único ponto de mínimo, que satisfaz

$$
∇f(x)=Ax−b=0.
$$

Ou seja, esse ponto de mínimo é exatamente a solução do sistema linear Ax=b.

O pré-condicionamento consiste em transformar um sistema linear em outro equivalente, mas com propriedades que favoreçam a convergência de um método iterativo, tornando o número de condição menor e fazendo com a solução seja encontrada por um método iterativo com uma quantidade muito menor de iterações. Em vez de resolver diretamente o sistema Ax = b, pode-se, por exemplo, aplicar um pré-condicionamento e resolver o sistema M⁻¹A x = M⁻¹b, em que M é uma matriz pré-condicionadora escolhida de modo que seja mais fácil aplicar M⁻¹ do que resolver diretamente o sistema original.

Em termos intuitivos, o pré-condicionador procura "melhorar" o sistema antes da aplicação do método iterativo. Idealmente, o sistema pré-condicionado apresenta propriedades espectrais mais favoráveis, como um melhor agrupamento dos autovalores, o que pode reduzir significativamente o número de iterações necessárias para atingir a convergência. Assim, um bom pré-condicionador deve estabelecer um equilíbrio entre a melhoria da convergência e o custo computacional de sua aplicação a cada iteração. Um bom pré-condicionador deve aproximar adequadamente A e, ao mesmo tempo, ser barato de aplicar. Pré-condicionadores comuns incluem a fatoração LU incompleta (ILU), a fatoração de Cholesky incompleta (IC), o pré-condicionamento diagonal (Jacobi) e os métodos multigrade (multigrid), este último particularmente eficaz para equações diferenciais parciais discretizadas. O pré-condicionamento é particularmente importante em sistemas provenientes de discretizações de equações diferenciais parciais.

---

## 1. Características Principais

* **Natureza iterativa**: Ele aproxima a solução passo a passo, sendo ideal para sistemas esparsos grandes demais para métodos diretos (como a decomposição de Cholesky).
* **Direções conjugadas**: Diferente do método do gradiente descendente tradicional (que faz movimentos em "zigue-zague" repetindo direções), o gradiente conjugado utiliza direções ortogonais (conjugadas) em relação à matriz $A$.
* **Convergência rápida**: Para um sistema de dimensão $n$, o método garante a convergência teórica em no máximo $n$ passos (na ausência de erros de arredondamento).
* **Otimização**: Resolver $Ax = b$ com $A$ simétrica e definida positiva equivale a encontrar o ponto de mínimo de uma função quadrática associada.

---

## 2. Exemplo Numérico Prático

Considere o sistema linear bidimensional ($n = 2$):

$$A = 
\begin{pmatrix} 4 & 1 \\
1 & 3
\end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

A solução exata é 

$$
x =
\begin{pmatrix} 
0.0909 \\
0.6364 
\end{pmatrix}
$$.

Partindo de uma estimativa inicial

$$
x_0 = 
\begin{pmatrix}
0 \\
0
\end{pmatrix}:
$$

### Passo 0: Inicialização
1. **Resíduo inicial ($r_0$)**: $r_0 = b - Ax_0 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$
2. **Direção inicial ($p_0$)**: $p_0 = r_0 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

### Iteração 1
1. **Tamanho do passo ($\alpha_0$)**:
   * $Ap_0 = \begin{pmatrix} 6 \\ 7 \end{pmatrix}$
   * $\alpha_0 = \frac{r_0^T r_0}{p_0^T A p_0} = \frac{5}{20} = 0.25$
2. **Atualização da solução ($x_1$)**: $x_1 = x_0 + \alpha_0 p_0 = \begin{pmatrix} 0.25 \\ 0.50 \end{pmatrix}$
3. **Atualização do resíduo ($r_1$)**: $r_1 = r_0 - \alpha_0 A p_0 = \begin{pmatrix} -0.50 \\ 0.25 \end{pmatrix}$
4. **Fator de correção ($\beta_0$)**: $\beta_0 = \frac{r_1^T r_1}{r_0^T r_0} = \frac{0.3125}{5} = 0.0625$
5. **Nova direção ($p_1$)**: $p_1 = r_1 + \beta_0 p_0 = \begin{pmatrix} -0.4375 \\ 0.3750 \end{pmatrix}$

### Iteração 2
1. **Tamanho do passo ($\alpha_1$)**:
   * $Ap_1 = \begin{pmatrix} -1.375 \\ 0.6875 \end{pmatrix}$
   * $\alpha_1 = \frac{r_1^T r_1}{p_1^T A p_1} = \frac{0.3125}{0.859375} \approx 0.363636$
2. **Atualização da solução ($x_2$)**: $x_2 = x_1 + \alpha_1 p_1 = \begin{pmatrix} 0.090909 \\ 0.636364 \end{pmatrix}$
3. **Atualização do resíduo ($r_2$)**: $r_2 = r_1 - \alpha_1 A p_1 = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$

Como o resíduo zerou, a convergência exata foi atingida em exatamente 2 iterações.

---

## 3. Os Pré-condicionadores

Os pré-condicionadores modificam o sistema original para reduzir o seu **número de condicionamento** ($\kappa$). O sistema original $Ax=b$ é transformado em $M^{-1}Ax = M^{-1}b$, onde $M$ é uma aproximação de $A$ de fácil inversão.
Visualmente, o pré-condicionador deforma curvas de nível elípticas e alongadas ("charutos") para torná-las o mais próximas possível de círculos perfeitos, acelerando drasticamente o algoritmo.

### Principais Tipos:
* **Jacobi (Diagonal)**: $M = \text{diag}(A)$. Extremamente barato, ideal para matrizes diagonalmente dominantes.
* **Cholesky Incompleto (ILU)**: Fatoração esparsa eliminando termos irrelevantes. Muito poderoso para problemas físicos estruturados.

---

## 4. Implementação Completa em Python (Matrizes Esparsas + Gráfico)

Abaixo está o código integrado que implementa o Gradiente Conjugado Pré-condicionado (PCG) com suporte a matrizes esparsas do tipo **CSR (Compressed Sparse Row)** e gera o histórico para monitoramento gráfico.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, csr_matrix

def pcg_esparso_historico(A, b, tol=1e-10, max_iter=2000, usar_jacobi=True):
    A = csr_matrix(A)
    b = np.array(b, dtype=float).reshape(-1, 1)
    x = np.zeros_like(b)
    
    r = b - A.dot(x)
    historico_residuos = [np.linalg.norm(r)]
    
    if usar_jacobi:
        diag_A = A.diagonal()
        if np.any(diag_A == 0):
            raise ValueError("A diagonal contém zeros. Jacobi falhou.")
        M_inv = diags(1.0 / diag_A)
        z = M_inv.dot(r)
    else:
        z = r.copy()
        
    p = z.copy()
    
    for i in range(max_iter):
        Ap = A.dot(p)
        r_t_z = np.dot(r.T, z)
        
        if np.linalg.norm(r) < tol:
            break
            
        alpha = r_t_z / np.dot(p.T, Ap)
        x = x + alpha * p
        r_novo = r - alpha * Ap
        
        if usar_jacobi:
            z_novo = M_inv.dot(r_novo)
        else:
            z_novo = r_novo.copy()
            
        beta = np.dot(r_novo.T, z_novo) / r_t_z
        p = z_novo + beta * p
        
        r = r_novo
        z = z_novo
        historico_residuos.append(np.linalg.norm(r))
        
    return x, historico_residuos

# Exemplo de Teste de Grande Porte
dim = 500
diag_principal = np.ones(dim) * 2.1
diag_principal[::10] = 500.0  # Adiciona mal condicionamento
diag_secundaria = np.ones(dim - 1) * -1.0
A_esparsa = diags([diag_secundaria, diag_principal, diag_secundaria], [-1, 0, 1], format='csr')
b_real = np.ones(dim)

_, erro_sem_pc = pcg_esparso_historico(A_esparsa, b_real, tol=1e-7, usar_jacobi=False)
_, erro_com_jacobi = pcg_esparso_historico(A_esparsa, b_real, tol=1e-7, usar_jacobi=True)

# Plotando os Gráficos de Convergência
plt.figure(figsize=(9, 5))
plt.plot(erro_sem_pc, label='Gradiente Conjugado Padrão', color='red')
plt.plot(erro_com_jacobi, label='Gradiente Conjugado + Jacobi', color='blue')
plt.yscale('log')
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.xlabel('Número de Iterações')
plt.ylabel('Norma do Resíduo (Escala Log)')
plt.legend()
plt.show()
```

---

## 5. Carregando Matrizes de Arquivos de Engenharia

Para matrizes reais obtidas de softwares de modelagem ou simuladores:

### Arquivos Matrix Market (`.mtx`)
```python
from scipy.io import mmread
A_esparsa = mmread('malha_engenharia.mtx').tocsr()
```

### Arquivos MATLAB (`.mat`)
```python
import scipy.io as sio
dados_matlab = sio.loadmat('dados_sistema.mat')
A_esparsa = dados_matlab['A'].tocsr()
b = dados_matlab['b']
```
