# Guia Completo: Análise Discriminante Linear (LDA)

A **Análise Discriminante Linear (LDA)** é um método estatístico e de aprendizado de máquina supervisionado usado para **classificação** e **redução de dimensionalidade**.

---

## 1. Como Funciona

*   **Supervisionado:** Diferente da PCA (que é não supervisionada e busca apenas a maior variância geral), a LDA utiliza as informações das classes (rótulos) para encontrar uma combinação linear de características que melhor separa os grupos.
*   **Objetivo Matemático:** Maximiza a distância entre as médias das classes (dispersão entre classes) e, ao mesmo tempo, minimiza a dispersão (variância) dentro de cada classe.
*   **Projeção:** Transforma dados de alta dimensão em um espaço de menor dimensão (por exemplo, reduzir de N variáveis para C-1 dimensões, onde C é o número de classes).

### Principais Diferenças: LDA vs. PCA

| Característica | LDA (Análise Discriminante Linear) | PCA (Análise de Componentes Principais) |
| :--- | :--- | :--- |
| **Tipo de Aprendizado** | **Supervisionado** (usa os rótulos das classes) | **Não supervisionado** (ignora os rótulos) |
| **Objetivo Principal** | Maximizar a separação entre as classes | Maximizar a variância total dos dados |
| **Número máximo de eixos** | Limitado a C - 1 (onde C é o número de classes) | Limitado a $\min(N, \text{amostras})$ |

### Principais Premissas (Pressupostos)
Para ter um desempenho ideal, a LDA assume que:
1.  Os dados de cada classe seguem uma **distribuição normal (gaussiana)**.
2.  Todas as classes compartilham a **mesma matriz de covariância**.
3.  As variáveis preditoras são linearmente separáveis e não sofrem de multicolinearidade extrema.

*Nota: Quando as covariâncias diferem entre as classes, utiliza-se a variação **QDA** (Quadratic Discriminant Analysis).*

---

## 2. Exemplo Numérico Passo a Passo

Imagine um cenário simplificado com 2 dimensões e 2 classes, com 2 amostras cada:

*   **Classe 1 ($C_1$):** $x_1 = [1, 2]$, $x_2 = [2, 3]$
*   **Classe 2 ($C_2$):** $x_3 = [4, 5]$, $x_4 = [5, 6]$

### Passo 1: Calcular os vetores de média ($\mu_1$, $\mu_2$ e $\mu$ global)
*   $\mu_1 = \left[ \frac{1+2}{2}, \frac{2+3}{2} \right] = [1.5, 2.5]$
*   $\mu_2 = \left[ \frac{4+5}{2}, \frac{5+6}{2} \right] = [4.5, 5.5]$
*   $\mu = \left[ \frac{1+2+4+5}{4}, \frac{2+3+5+6}{4} \right] = [3.0, 4.0]$

### Passo 2: Matriz de Dispersão Dentro das Classes ($S_W$)
Mede a variação interna de cada grupo através da fórmula: $\sum (x - \mu)(x - \mu)^T$.

*   **Para $C_1$ ($S_1$):**
    *   Ponto 1: $[1, 2] - [1.5, 2.5] = [-0.5, -0.5] \rightarrow [-0.5, -0.5] \times [-0.5, -0.5]^T = \begin{bmatrix} 0.25 & 0.25 \\ 0.25 & 0.25 \end{bmatrix}$
    *   Ponto 2: $[2, 3] - [1.5, 2.5] = [0.5, 0.5] \rightarrow [0.5, 0.5] \times [0.5, 0.5]^T = \begin{bmatrix} 0.25 & 0.25 \\ 0.25 & 0.25 \end{bmatrix}$
    *   $S_1 = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix}$
*   **Para $C_2$ ($S_2$):** Resulta no mesmo devido à simetria: $S_2 = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix}$

$$S_W = S_1 + S_2 = \begin{bmatrix} 1.0 & 1.0 \\ 1.0 & 1.0 \end{bmatrix}$$

### Passo 3: Matriz de Dispersão Entre as Classes ($S_B$)
Mede a distância entre as médias das classes: $S_B = \sum N_i (\mu_i - \mu)(\mu_i - \mu)^T$.

*   **Classe 1:** $2 \times \left( ([1.5, 2.5] - [3, 4]) \times ([1.5, 2.5] - [3, 4])^T \right) = \begin{bmatrix} 4.5 & 4.5 \\ 4.5 & 4.5 \end{bmatrix}$
*   **Classe 2:** $2 \times \left( ([4.5, 5.5] - [3, 4]) \times ([4.5, 5.5] - [3, 4])^T \right) = \begin{bmatrix} 4.5 & 4.5 \\ 4.5 & 4.5 \end{bmatrix}$

$$S_B = \begin{bmatrix} 9.0 & 9.0 \\ 9.0 & 9.0 \end{bmatrix}$$

### Passo 4: Vetor de Projeção ($w$)
O objetivo é encontrar os autovetores de $S_W^{-1}S_B$, aproximado por:
$$w \propto S_W^{-1}(\mu_1 - \mu_2)$$

---

## 3. Implementação Prática em Python

### Scikit-Learn (Abordagem Padrão e Dataset Iris)

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np

# 1. Carregar o dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# 2. Divisão Treino/Teste com Estratificação
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Treinar Classificador LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# 4. Avaliação
y_pred = lda.predict(X_test)
print(f"Acurácia Geral: {accuracy_score(y_test, y_pred):.2%}")

# 5. Validação Cruzada (5-Fold)
cv_estrategia = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(lda, X, y, cv=cv_estrategia, scoring='accuracy')
print(f"Acurácia Média CV: {np.mean(scores):.2%} (± {np.std(scores):.2%})")

# 6. Salvar o Modelo
joblib.dump(lda, 'modelo_lda_iris.joblib')
```

### PyTorch (LDA do Zero com Aceleração por Hardware)

```python
import torch
from sklearn.datasets import load_iris

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
iris = load_iris()
X = torch.tensor(iris.data, dtype=torch.float32, device=device)
y = torch.tensor(iris.target, dtype=torch.long, device=device)

n_samples, n_features = X.shape
classes = torch.unique(y)
mean_total = torch.mean(X, dim=0)

Sw = torch.zeros((n_features, n_features), device=device)
Sb = torch.zeros((n_features, n_features), device=device)

for c in classes:
    X_c = X[y == c]
    mean_c = torch.mean(X_c, dim=0)
    
    deviation_w = X_c - mean_c
    Sw += torch.matmul(deviation_w.t(), deviation_w)
    
    n_c = X_c.shape[0]
    deviation_b = (mean_c - mean_total).unsqueeze(1)
    Sb += n_c * torch.matmul(deviation_b, deviation_b.t())

Sw += torch.eye(n_features, device=device) * 1e-5
A = torch.matmul(torch.linalg.inv(Sw), Sb)
eigenvalues, eigenvectors = torch.linalg.eig(A)

eigenvalues, eigenvectors = torch.real(eigenvalues), torch.real(eigenvectors)
idxs = torch.argsort(eigenvalues, descending=True)
W = eigenvectors[:, idxs[:, :len(classes)-1]]

X_lda = torch.matmul(X, W)
print("Dados projetados com sucesso via PyTorch!")
```