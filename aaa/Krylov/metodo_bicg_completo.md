# O Método dos Gradientes Biconjugados (BiCG)

O **método BiCG** (*Biconjugate Gradients*) é um algoritmo iterativo do subespaço de Krylov projetado para resolver sistemas de equações lineares **não simétricos** da forma:

$$Ax = b$$

Diferente do método dos Gradientes Conjugados (CG) tradicional, que exige que a matriz $A$ seja simétrica e definida positiva, o BiCG estende essa capacidade para matrizes gerais através da introdução de um sistema "sombra" ou adjunto baseado na transposta da matriz ($A^T$).

---

## 1. Características Principais

* **Sequências Biorgtonais:** O método gera duas sequências de resíduos ($r_k$ e $\hat{r}_k$) e duas sequências de direções de busca ($p_k$ e $\hat{p}_k$) que satisfazem condições de biortogonalidade e biconjugação:
  $$\langle \hat{r}_i, r_j \rangle = 0 \quad \text{para } i \neq j$$
  $$\langle \hat{p}_i, A p_j \rangle = 0 \quad \text{para } i \neq j$$
* **Custo Computacional:** Cada iteração requer duas multiplicações de matriz por vetor: uma por $A$ e outra por $A^T$. Isso dobra o esforço computacional por passo em comparação ao CG.
* **Instabilidade Numérica (Breakdown):** O método não garante a minimização do resíduo a cada iteração (diferente do GMRES). Ele pode sofrer interrupções abruptas por divisão por zero se os produtos escalares $\langle \hat{r}_k, r_k \rangle$ ou $\langle \hat{p}_k, A p_k \rangle$ se anularem sem que o sistema tenha convergido.

---

## 2. O Algoritmo BiCG Base

Dado um palpite inicial $x_0$, a matriz $A$ e o vetor de carga $b$:

1. Calcular o resíduo inicial: $r_0 = b - A x_0$
2. Escolher um resíduo sombra inicial arbitrário $\hat{r}_0$ (frequentemente $\hat{r}_0 = r_0$)
3. Definir direções de busca iniciais: $p_0 = r_0$ e $\hat{p}_0 = \hat{r}_0$
4. Para cada iteração $k = 0, 1, 2, \dots$:
   $$\alpha_k = \frac{\langle \hat{r}_k, r_k \rangle}{\langle \hat{p}_k, A p_k \rangle}$$
   $$x_{k+1} = x_k + \alpha_k p_k$$
   $$r_{k+1} = r_k - \alpha_k A p_k$$
   $$\hat{r}_{k+1} = \hat{r}_k - \alpha_k A^T \hat{p}_k$$
   $$\beta_k = \frac{\langle \hat{r}_{k+1}, r_{k+1} \rangle}{\langle \hat{r}_k, r_k \rangle}$$
   $$p_{k+1} = r_{k+1} + \beta_k p_k$$
   $$\hat{p}_{k+1} = \hat{r}_{k+1} + \beta_k \hat{p}_k$$

---

## 3. BiCG Pré-Condicionado (PBiCG)

Para melhorar a taxa de convergência e mitigar instabilidades numéricas, introduz-se uma matriz de pré-condicionamento $M \approx A$ tal que sistemas do tipo $M z = r$ sejam fáceis de resolver. O algoritmo com pré-condicionamento à esquerda/direita (*split*) altera o cálculo dos passos usando os vetores transformados $z_k$ e $\hat{z}_k$.

### Algoritmo PBiCG

1. Inicializar $x_0$, calcular $r_0 = b - A x_0$. Escolher $\hat{r}_0 = r_0$.
2. Para cada iteração $k = 0, 1, 2, \dots$:
   * Resolver $M z_k = r_k$
   * Resolver $M^T \hat{z}_k = \hat{r}_k$
   * $\rho_k = \langle \hat{z}_k, r_k \rangle$
   * Se $k = 0$:
     * $p_0 = z_0$ e $\hat{p}_0 = \hat{z}_0$
   * Senão:
     * $\beta_{k-1} = \rho_k / \rho_{k-1}$
     * $p_k = z_k + \beta_{k-1} p_{k-1}$
     * $\hat{p}_k = \hat{z}_k + \beta_{k-1} \hat{p}_{k-1}$
   * Calcular $\alpha_k = \frac{\rho_k}{\langle \hat{p}_k, A p_k \rangle}$
   * Atualizar:
     * $x_{k+1} = x_k + \alpha_k p_k$
     * $r_{k+1} = r_k - \alpha_k A p_k$
     * $\hat{r}_{k+1} = \hat{r}_k - \alpha_k A^T \hat{p}_k$

---

## 4. Implementação Completa em Python

O código abaixo implementa a versão pré-condicionada pura utilizando `numpy`. Se nenhuma matriz `M` for fornecida, ele assume a identidade (BiCG padrão).

```python
import numpy as np

def preconditioned_biconjugate_gradient(A, b, M=None, x0=None, tol=1e-5, max_iter=1000):
    n = len(b)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    b = np.array(b, dtype=float)
    A = np.array(A, dtype=float)
    
    if M is None:
        M = np.eye(n)
    else:
        M = np.array(M, dtype=float)
        
    r = b - np.dot(A, x)
    r_shadow = r.copy()
    
    if np.linalg.norm(r) < tol:
        return x, 0
        
    rho_old = 1.0
    
    for k in range(max_iter):
        # Resolver o pré-condicionador
        z = np.linalg.solve(M, r)
        z_shadow = np.linalg.solve(M.T, r_shadow)
        
        rho_new = np.dot(z_shadow, r)
        
        if abs(rho_new) < 1e-12:
            print("Breakdown nos resíduos (divisão por zero).")
            break
            
        if k == 0:
            p = z.copy()
            p_shadow = z_shadow.copy()
        else:
            beta = rho_new / rho_old
            p = z + beta * p
            p_shadow = z_shadow + beta * p_shadow
            
        Ap = np.dot(A, p)
        denominator = np.dot(p_shadow, Ap)
        
        if abs(denominator) < 1e-12:
            print(f"Breakdown nas direções de busca na iteração {k}.")
            break
            
        alpha = rho_new / denominator
        
        x = x + alpha * p
        r = r - alpha * Ap
        
        if np.linalg.norm(r) < tol:
            return x, k + 1
            
        r_shadow = r_shadow - alpha * np.dot(A.T, p_shadow)
        rho_old = rho_new
        
    return x, max_iter

# Exemplo de teste (Pré-condicionador de Jacobi)
if __name__ == "__main__":
    A = np.array([[100.0, 1.0, -2.0], [3.0, 200.0, 6.0], [1.0, -1.0, 300.0]])
    b = np.array([99.0, 209.0, 300.0])
    M_jacobi = np.diag(np.diag(A))
    
    sol, iters = preconditioned_biconjugate_gradient(A, b, M=M_jacobi, tol=1e-7)
    print(f"Solução: {sol} obtida em {iters} iterações.")
```
