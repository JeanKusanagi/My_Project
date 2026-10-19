# O Princípio da Compressão de Imagens via SVD

A compressão de imagens utilizando a **Decomposição em Valores Singulares (SVD)** baseia-se no conceito matemático de **Aproximação de Baixo Posto** (*Low-Rank Approximation*). 

Uma imagem digital em tons de cinza pode ser representada como uma matriz $A$ de dimensões $m \times n$, onde cada elemento corresponde à intensidade de um pixel.

---

## 1. A Fórmula de Decomposição

A SVD fatora a matriz $A$ no produto de três matrizes:
$$A = U \Sigma V^T$$

Isso pode ser reescrito de forma equivalente como uma **soma de produtos externos** dos vetores das matrizes $U$ (colunas $u_i$) e $V^T$ (linhas $v_i^T$):

$$A = \sigma_1 (u_1 v_1^T) + \sigma_2 (u_2 v_2^T) + \sigma_3 (u_3 v_3^T) + \dots + \sigma_r (u_r v_r^T)$$

Onde:
* $\sigma_i$ são os **valores singulares**, organizados em ordem decrescente ($\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$).
* Cada termo $(u_i v_i^T)$ forma uma matriz de posto 1 com o mesmo tamanho da imagem original.

---

## 2. Como Funciona a Compressão?

Os primeiros termos da soma (associados aos maiores valores singulares $\sigma$) concentram a maior parte da energia e variância dos dados. Eles representam as **estruturas principais, formas e contornos globais** da imagem. 

Os termos posteriores (associados a valores singulares muito pequenos) representam apenas **detalhes finos, texturas sutis ou ruídos**.

Para comprimir a imagem, escolhemos um número truncado $k$ (onde $k < r$) e **descartamos** todos os componentes a partir dali. A aproximação da imagem comprimida $A_k$ passa a ser:

$$A_k \approx \sum_{i=1}^{k} \sigma_i u_i v_i^T$$

---

## 3. Economia de Espaço (Exemplo Prático)

Considere uma imagem de resolução $500 \times 500$ pixels:
* **Sem compressão (Original):** É necessário armazenar os $500 \times 500 = 250.000$ pixels.
* **Com compressão SVD (truncada em $k = 20$):**
  * $20$ colunas de $U$: $500 \times 20 = 10.000$ valores
  * $20$ valores singulares de $\Sigma$: $20$ valores
  * $20$ linhas de $V^T$: $20 \times 500 = 10.000$ valores
  * **Total armazenado:** $10.000 + 20 + 10.000 = 20.020$ valores.

Neste cenário, mantemos apenas **~8% dos dados originais**, obtendo uma redução drástica de espaço de armazenamento enquanto a imagem reconstruída retém suas características visuais mais importantes de forma perfeitamente reconhecível.


## 4. Implementação da Comprensão SVD em Python (NumPy)

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
