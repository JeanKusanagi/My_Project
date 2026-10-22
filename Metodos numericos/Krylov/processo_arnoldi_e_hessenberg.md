# Estudo de Caso: Álgebra Linear Numérica e Aplicações

Este documento reúne os conceitos abordados sobre o **Processo de Arnoldi**, **Matrizes de Hessenberg**, o **Algoritmo QR** (incluindo o tratamento de autovalores complexos) e o método iterativo **GMRES** aplicado à resolução de Equações Diferenciais Parciais (EDPs).

---

## 1. O Processo de Arnoldi

O **processo de Arnoldi** (ou iteração de Arnoldi) é um algoritmo iterativo da álgebra linear numérica usado para encontrar aproximações dos autovalores e autovetores de matrizes de grande porte e não-hermitianas.

### Como funciona
*   **Subespaço de Krylov:** O método constrói gradualmente uma base ortonormal para o subespaço de Krylov gerado por uma matriz $A$ e um vetor inicial $v$.
*   **Ortogonalização:** Utiliza um processo semelhante ao de Gram-Schmidt para garantir que os vetores da base sejam ortonormais.
*   **Matriz de Hessenberg:** Transforma a matriz original em uma matriz Hessenberg superior (ou tridiagonal, no caso de matrizes hermitianas), que possui menor complexidade computacional para o cálculo de autovalores.

### Principais Aplicações
*   **Grandes matrizes esparsas:** É altamente eficiente quando a matriz é muito grande e possui muitos elementos iguais a zero, onde métodos diretos seriam inviáveis.
*   **Resultados parciais:** Permite obter boas aproximações após um número reduzido de iterações, sem a necessidade de concluir o processo completo.
*   **Sistemas lineares:** Serve de base para outros algoritmos importantes, como o método **GMRES** (*Generalized Minimal Residual Method*).

---

## 2. A Matriz de Hessenberg

Uma **matriz de Hessenberg** é um tipo especial de matriz quadrada que é "quase" triangular. Ela serve como um passo intermediário crucial em álgebra linear numérica porque simplifica drasticamente o cálculo de autovalores e autovetores.

Existem dois tipos, sendo o superior o mais comum:
*   **Hessenberg Superior:** Todos os elementos **abaixo da primeira subdiagonal são zero**. Ou seja, deve obedecer a $A_{ij} = 0$ sempre que $i > j + 1$.
*   **Hessenberg Inferior:** Todos os elementos **acima da primeira superdiagonal são zero**. Ou seja, $A_{ij} = 0$ sempre que $j > i + 1$.

### Exemplo Visual (Hessenberg Superior $4 	imes 4$)
$$
\begin{pmatrix}
* & * & * & * \\
* & * & * & * \\
0 & * & * & * \\
0 & 0 & * & *
\end{pmatrix}
$$
*Nota: Os asteriscos ($*$) representam elementos que podem ser zero ou não.*

### Exemplo Numérico de Transformação
Dada uma matriz original $A$, queremos zerar o elemento inferior esquerdo ($A_{31} = 4$):
$$
A = \begin{pmatrix} 1 & 5 & 7 \\ 3 & 0 & 6 \\ 4 & 3 & 2 \end{pmatrix}
$$

Utilizando uma **Reflexão de Householder** ($P$) para zerar a posição desejada:
$$
P = \begin{pmatrix} 1.0 & 0.0 & 0.0 \\ 0.0 & -0.6 & -0.8 \\ 0.0 & -0.8 & 0.6 \end{pmatrix}
$$

Aplicando a transformação de similaridade ($H = P \cdot A \cdot P$), obtemos a matriz de Hessenberg Superior:
$$
H = \begin{pmatrix} 1.0 & -8.6 & 0.2 \\ -5.0 & 5.6 & -1.2 \\ 0.0 & 1.8 & -3.6 \end{pmatrix}
$$

---

## 3. Extração de Autovalores: Algoritmo QR e o Desafio Complexo

Para extrair os autovalores de $H$, aplica-se de forma iterativa o **Algoritmo QR com Deslocamento (Shifted QR Algorithm)**.

### Fluxo de Convergência
1.  **Escolha do Deslocamento ($\mu$):** Isola frequências numéricas usando, por exemplo, o elemento inferior direito ($\mu = H_{nn}$).
2.  **Fatoração QR:** Decompõe a matriz deslocada: $(H - \mu I) = Q \cdot R$.
3.  **Recombinação:** Cria a nova matriz do passo: $H_{novo} = (R \cdot Q) + \mu I$.

A matriz mantém a forma de Hessenberg e os mesmos autovalores, mas os elementos abaixo da diagonal convergem para zero, restando os autovalores diretamente na diagonal principal.

### O Desafio dos Autovalores Complexos (Passo Duplo de Francis)
Quando uma matriz real possui autovalores complexos conjugados, o algoritmo padrão pode estagnar ou exigir aritmética complexa (o que duplica o custo computacional). Para resolver isso, usa-se o **Passo Duplo de Francis** (*Implicit Double-Shift QR*).

Em vez de um deslocamento unitário, realizam-se dois deslocamentos simultâneos usando o par conjugado $\mu_1$ e $\mu_2 = \bar{\mu}_1$:
$$
M = (H - \mu_1 I)(H - \mu_2 I) = H^2 - (\mu_1 + \mu_2)H + (\mu_1\mu_2)I
$$
Como $(\mu_1 + \mu_2)$ e $(\mu_1\mu_2)$ são números estritamente **reais**, toda a computação permanece no domínio real. O algoritmo usa uma técnica de perseguição de protuberância (*bulge chasing*) para restaurar a forma de Hessenberg ao fim do passo, isolando os autovalores complexos em subblocos diagonais de tamanho $2 \times 2$.

---

## 4. O Método GMRES

O **GMRES** (*Generalized Minimal Residual Method*) resolve sistemas lineares $Ax = b$ onde $A$ é grande, esparsa e não-simétrica. Ele projeta o problema em um espaço menor usando o Processo de Arnoldi.

### Algoritmo Simplificado
1.  **Arnoldi:** Constrói uma base ortonormal $Q_n$ para o subespaço de Krylov e uma matriz de Hessenberg pequena $H_n$ de tamanho $(n+1) \times n$, respeitando a relação $A Q_n = Q_{n+1} H_n$.
2.  **Minimização:** O problema gigante de resíduo mínimo transforma-se em um problema de mínimos quadrados minúsculo:
    $$
    \min_{y} \Vert \beta e_1 - H_n y \Vert_2
    $$
3.  **Atualização:** A solução aproximada é calculada por $x_n = x_0 + Q_n y$.

---

## 5. Exemplo Prático: Equação de Convecção-Difusão

Abaixo está o exemplo prático de aplicação em uma Equação Diferencial Parcial Discretizada por Diferenças Finitas. O termo de convecção quebra a simetria da matriz, inviabilizando métodos como o de Gradientes Conjugados e justificando o uso do GMRES.

```python
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# 1. Parâmetros do problema
N = 1000          # Número de pontos internos no grid
L = 1.0
h = L / (N + 1)
kappa = 0.01      # Difusão
v = 1.0           # Convecção (velocidade)

# 2. Montagem dos coeficientes da matriz esparsa
c_esquerdo = -kappa / h**2 - v / h
c_central  = 2*kappa / h**2 + v / h
c_direito  = -kappa / h**2

# Criando as diagonais da matriz A
diagonais = [
    np.full(N - 1, c_esquerdo),  # Subdiagonal
    np.full(N, c_central),       # Diagonal principal
    np.full(N - 1, c_direito)    # Superdiagonal
]
A = sp.diags(diagonais, [-1, 0, 1], format='csr')

# 3. Vetor força/fonte f(x) = 1
b = np.ones(N)

# 4. Resolvendo o sistema usando GMRES
solucao, info = spla.gmres(A, b, tol=1e-8)

if info == 0:
    print("GMRES convergiu com sucesso!")
    print(f"Temperatura máxima calculada no canal: {max(solucao):.4f}")
else:
    print("O GMRES falhou em convergir.")
```
