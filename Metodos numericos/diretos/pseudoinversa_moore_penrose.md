# Resumo Completo: Inversa de Moore–Penrose e suas Aplicações

Este documento reúne todas as explicações, exemplos numéricos e aplicações práticas em Machine Learning discutidos ao longo da consulta sobre a pseudoinversa de Moore-Penrose.

---

## 1. O que é a Inversa de Moore–Penrose?

A **inversa de Moore-Penrose** (frequentemente chamada de **pseudoinversa** e denotada por $A^\dagger$ ou $A^+$) é a generalização mais conhecida da matriz inversa tradicional na álgebra linear. 

Ela foi descrita de forma independente por E. H. Moore (1920), Arne Bjerhammar (1951) e Roger Penrose (1955) para resolver as limitações da inversa comum.

### Principais Características:
* **Matrizes Não Quadradas:** Enquanto a inversa comum exige que a matriz seja quadrada ($m = n$) e não singular, a pseudoinversa funciona para qualquer matriz real ou complexa de tamanho $m \times n$.
* **Mínimos Quadrados:** Quando um sistema $Ax = b$ não possui solução exata (sistema sobredeterminado) ou possui infinitas soluções (sistema subdeterminado), a pseudoinversa encontra o vetor $x$ que minimiza o erro euclidiano $\Vert Ax - b \Vert_2$.

### Métodos de Cálculo:
A forma mais estável e universal de computar a pseudoinversa é através da **Decomposição em Valores Singulares (SVD)**:
1. Decompõe-se a matriz em $A = U \Sigma V^T$.
2. Inverte-se cada elemento não nulo da matriz diagonal $\Sigma$ (transpondo-a para $\Sigma^+$).
3. Calcula-se $A^\dagger = V \Sigma^+ U^T$.

Para matrizes com posto completo, existem atalhos algébricos:
* **Posto de coluna completo** ($A^T A$ é invertível): $A^\dagger = (A^T A)^{-1} A^T$ (Inversa à esquerda).
* **Posto de linha completo** ($A A^T$ é invertível): $A^\dagger = A^T (A A^T)^{-1}$ (Inversa à direita).

---

## 2. Exemplo Numérico Prático

Vamos calcular a pseudoinversa de uma matriz retangular simples $3 \times 2$ utilizando a fórmula de posto de coluna completo.

Dado:
$$A = \begin{bmatrix} 1 & 2 \\ 1 & 1 \\ 2 & 3 \end{bmatrix}$$

### Passo 1: Calcular $A^T A$
Multiplicamos a transposta de $A$ por ela mesma:
$$A^T A = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 1 & 1 \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} (1+1+4) & (2+1+6) \\ (2+1+6) & (4+1+9) \end{bmatrix} = \begin{bmatrix} 6 & 9 \\ 9 & 14 \end{bmatrix}$$

### Passo 2: Calcular a inversa de $(A^T A)$
Para uma matriz $2 \times 2$, a inversa é calculada usando o determinante:
* **Determinante:** $(6 \times 14) - (9 \times 9) = 84 - 81 = 3$
* **Inversa:**
$$(A^T A)^{-1} = \frac{1}{3} \begin{bmatrix} 14 & -9 \\ -9 & 6 \end{bmatrix} = \begin{bmatrix} \frac{14}{3} & -3 \\ -3 & 2 \end{bmatrix}$$

### Passo 3: Multiplicar por $A^T$ para obter $A^\dagger$
$$A^\dagger = (A^T A)^{-1} A^T = \begin{bmatrix} \frac{14}{3} & -3 \\ -3 & 2 \end{bmatrix} \begin{bmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \end{bmatrix} = \begin{bmatrix} -\frac{4}{3} & \frac{5}{3} & \frac{1}{3} \\ 1 & -1 & 0 \end{bmatrix}$$

---

## 3. Resolução de um Sistema sem Solução Exata

Utilizando a matriz $A$ anterior, vamos aproximar a solução do seguinte sistema impossível:
$$\begin{cases} 1x + 2y = 1 \\ 1x + 1y = 2 \\ 2x + 3y = 4 \end{cases} \implies A \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 4 \end{bmatrix}$$

A melhor aproximação de mínimos quadrados ($\hat{x}$) é dada por:
$$\hat{x} = A^\dagger b$$

$$\hat{x} = \begin{bmatrix} -\frac{4}{3} & \frac{5}{3} & \frac{1}{3} \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 4 \end{bmatrix} = \begin{bmatrix} \frac{10}{3} \\ -1 \end{bmatrix}$$

* **Solução ótima:** $x \approx 3.33$, $y = -1$

### Verificação do Erro:
Ao substituir os valores de volta em $Ax$, temos:
1. $1(3.33) + 2(-1) = 1.33$ *(esperado: 1)*
2. $1(3.33) + 1(-1) = 2.33$ *(esperado: 2)*
3. $2(3.33) + 3(-1) = 3.66$ *(esperado: 4)*

Essas coordenadas representam o ponto geométrico que minimiza a distância global para as três equações retas concorrentes.

---

## 4. Aplicação em Machine Learning (Regressão Linear)

Na Inteligência Artificial, a matriz de dados $X$ (características) e o vetor $y$ (alvo) geram um modelo preditivo definido por $y = Xw$. Encontrar os pesos ideais $w$ que minimizam o erro quadrático é equivalente a aplicar a pseudoinversa:
$$w = X^\dagger y$$

### Vantagens sobre a Inversa Comum:
1. **Multicolinearidade:** Se existirem colunas redundantes (dados correlacionados), a inversa padrão quebra porque o determinante de $X^T X$ zera. A pseudoinversa (via SVD) contorna isso e calcula os pesos normalmente.
2. **Mais Variáveis que Amostras ($n > m$):** Evita falhas por indefinição de sistemas subdeterminados, escolhendo a solução com a menor norma euclidiana (evitando *overfitting*).

### Códigos Práticos em Python

#### Abordagem Pura com NumPy:
```python
import numpy as np

# Características: [Idade, Renda Mensal]
X = np.array([[25, 3.5], [30, 5.0], [45, 8.2], [22, 2.8]])
# Adicionando viés (Bias)
X_b = np.c_[np.ones((X.shape[0], 1)), X] 
# Gasto real no cartão de crédito
y = np.array([1.2, 1.8, 3.5, 0.9])

# Treinamento via Pseudoinversa
X_pseudo = np.linalg.pinv(X_b)
w = X_pseudo.dot(y)
print("Pesos calculados (w):", w)
```

#### Abordagem de Mercado com Scikit-Learn:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[25, 3.5], [30, 5.0], [45, 8.2], [22, 2.8]])
y = np.array([1.2, 1.8, 3.5, 0.9])

modelo = LinearRegression()
modelo.fit(X, y)

print(f"Bias (Intercepto): {modelo.intercept_}")
print(f"Pesos das variáveis: {modelo.coef_}")
```