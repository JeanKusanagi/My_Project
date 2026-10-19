# Decomposição em Valores Singulares (SVD)

Para ilustrar o funcionamento da **SVD**, vamos resolver um exemplo numérico simples e, em seguida, ver como aplicar o cálculo diretamente em **Python**.

---

## 1. Exemplo Numérico Prático

Vamos calcular a SVD de uma matriz real $A$ de dimensão $2 	imes 2$:

$$
A = \begin{pmatrix}
3 & 0 \\
4 & 5 
\end{pmatrix}
$$

O objetivo é encontrar $A = U \Sigma V^T$.

### Passo 1: Encontrar os Valores Singulares ($\Sigma$) e os Vetores Singulares à Direita ($V$)
Os valores singulares ao quadrado são os autovalores da matriz $A^T A$. Vamos calcular esse produto:

$$A^T A = \begin{pmatrix} 
3 & 4 \\
0 & 5 
\end{pmatrix}
\begin{pmatrix} 
3 & 0 \\
4 & 5 
\end{pmatrix} = 
\begin{pmatrix} 
25 & 20 \\
20 & 25
\end{pmatrix}$$

Os autovalores ($\lambda$) de $A^T A$ são encontrados resolvendo o determinante $\det(A^T A - \lambda I) = 0$:

$$\det \begin{pmatrix}
25 - \lambda & 20 \\
20 & 25 - \lambda
\end{pmatrix} = 0 \implies (25 - \lambda)^2 - 400 = 0$$
$$\lambda_1 = 45, \quad \lambda_2 = 5$$

Os **valores singulares** ($\sigma$) são as raízes quadradas positivas dos autovalores:
* $\sigma_1 = \sqrt{45} = 3\sqrt{5} \approx 6.708$
* $\sigma_2 = \sqrt{5} \approx 2.236$

Portanto, a matriz diagonal $\Sigma$ é:
$$\Sigma = \begin{pmatrix} 
3\sqrt{5} & 0 \\
0 & \sqrt{5}
\end{pmatrix}$$

Os autovetores normalizados de $A^T A$ formam as colunas de $V$. Resolvendo o sistema para cada $\lambda$, obtemos:

$$V = \begin{pmatrix}
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{pmatrix}$$

### Passo 2: Encontrar os Vetores Singulares à Esquerda ($U$)
As colunas de $U$ podem ser encontradas usando a relação $u_i = \frac{1}{\sigma_i} A v_i$:

* Para $u_1$:

$$A v_1 =
\begin{pmatrix}
3 & 0 \\
4 & 5 \end{pmatrix}
\begin{pmatrix}
\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}}
\end{pmatrix} = \begin{pmatrix}
\frac{3}{\sqrt{2}} \\
\frac{9}{\sqrt{2}}
\end{pmatrix} \implies u_1 = \frac{1}{3\sqrt{5}}
\begin{pmatrix} 
\frac{3}{\sqrt{2}} \\
\frac{9}{\sqrt{2}}
\end{pmatrix} =
\begin{pmatrix}
\frac{1}{\sqrt{10}} \\
\frac{3}{\sqrt{10}}
\end{pmatrix}
$$

* Para $u_2$: Seguindo o mesmo processo com $v_2$ e $\sigma_2$, obtemos a segunda coluna.

A matriz $U$ resultante será:

$$U = \begin{pmatrix}
\frac{1}{\sqrt{10}} & -\frac{3}{\sqrt{10}} \\
\frac{3}{\sqrt{10}} & \frac{1}{\sqrt{10}}
\end{pmatrix}$$

Ao multiplicar $U \Sigma V^T$, você retornará exatamente para a matriz original $A$.

---

## 2. Implementação em Python (NumPy)

Em ambientes reais, você não precisa fazer esses cálculos à mão. A biblioteca **NumPy** resolve isso com apenas uma linha de código usando a função `np.linalg.svd`.

```python
import numpy as np

# 1. Definindo a matriz do exemplo anterior
A = np.array([[3.0, 0.0],
              [4.0, 5.0]])

# 2. Calculando a SVD
# Nota: O NumPy retorna V transposto (Vt) diretamente
U, S, Vt = np.linalg.svd(A)

print("Matriz U (Vetores à esquerda):")
print(U)

print("\nValores Singulares (S):")
print(S)  # Retorna como um array unidimensional

print("\nMatriz V^T (Transposta dos vetores à direita):")
print(Vt)

# 3. Reconstruindo a matriz original para verificar o resultado
# Criamos a matriz Sigma diagonal a partir do vetor S
Sigma = np.diag(S)
A_reconstruida = U @ Sigma @ Vt

print("\nMatriz Reconstruída:")
print(A_reconstruida)
```

## 3. Implementação da Comprensão SVD em Python (NumPy)

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Criando uma matriz de exemplo (simulando uma imagem 100x100)
# Criamos um padrão quadrado no centro para simular um objeto
imagem_original = np.zeros((100, 100))
imagem_original[30:70, 30:70] = 1.0  # Um quadrado branco no centro

# Adicionamos um pouco de ruído aleatório
np.random.seed(42)
imagem_original += np.random.normal(0, 0.2, (100, 100))

# 2. Aplicando a SVD usando a biblioteca NumPy
# np.linalg.svd retorna U, os valores singulares em um vetor S, e V transposta (Vt)
U, S, Vt = np.linalg.svd(imagem_original)

# 3. Definindo quantos valores singulares vamos manter (k)
# Modifique este valor para ver o efeito da compressão e filtragem de ruído!
k = 5 

# Reconstruindo a imagem truncada (usando apenas os k primeiros componentes)
S_k = np.diag(S[:k])
U_k = U[:, :k]
Vt_k = Vt[:k, :]
imagem_comprimida = U_k @ S_k @ Vt_k

# 4. Exibindo o resultado visualmente com Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(imagem_original, cmap='gray')
axes[0].set_title("Imagem Original (Com Ruído)")
axes[0].axis('off')

axes[1].imshow(imagem_comprimida, cmap='gray')
axes[1].set_title(f"Imagem Comprimida (k = {k})")
axes[1].axis('off')

print("Exibindo o gráfico... Feche a janela do gráfico para encerrar o script.")
plt.show()
```
