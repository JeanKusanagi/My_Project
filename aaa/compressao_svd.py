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
