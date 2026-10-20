# Guia Completo do Método BiCGSTAB

O **BiCGSTAB** (*Biconjugate Gradient Stabilized*, ou Método Gradiente Biconjugado Estabilizado) é um método iterativo do **subespaço de Krylov** criado por H. A. van der Vorst para resolver sistemas de equações lineares não simétricos do tipo $Ax = b$.

---

## 1. Principais Características e Aplicações

* **Não simetria:** Diferente do método do Gradiente Conjugado (CG) tradicional — que exige que a matriz $A$ seja simétrica e definida positiva —, o BiCGSTAB funciona em **matrizes não simétricas**.
* **Convergência suave:** Ele foi desenvolvido para corrigir o comportamento irregular e as oscilações severas (em "dentes de serra") que ocorrem no método BiCG original e no CGS (*Conjugate Gradient Squared*).
* **Sem transposta:** Não exige a multiplicação pela matriz transposta $A^T$.
* **Custo computacional:** Cada iteração gasta duas multiplicações matriz-vetor, mas consome pouca memória porque não precisa armazenar uma base ortogonal grande (como faz o GMRES).

### Onde é utilizado:
* Resolução de grandes sistemas esparsos em **simulações de engenharia**, mecânica dos fluidos, aerodinâmica e computação científica.
* Disponível em bibliotecas numéricas padrão como `scipy.sparse.linalg.bicgstab`, MATLAB (`bicgstab`) e Eigen (`Eigen::BiCGSTAB`).

### Limitação:
* Por usar passos de minimização de ordem baixa (baseados no GMRES(1)), pode **estagnar** ou oscilar se o espectro da matriz for muito complexo, o que motivou o desenvolvimento de variantes de ordem superior como o **BiCGSTAB(l)**.

---

## 2. Algoritmo Passo a Passo (Sem Precondicionamento)

O algoritmo do **BiCGSTAB** atualiza iterativamente a solução aproximada $x_k$ e os resíduos. O processo busca minimizar o resíduo em direções ortogonais e aplica um passo de estabilização local a cada iteração.

### Inicialização
Antes de iniciar o laço principal, definimos os valores iniciais (para $k = 0$):

1. Escolha uma aproximação inicial $x_0$ (geralmente um vetor de zeros).
2. Calcule o resíduo inicial: $r_0 = b - A x_0$.
3. Escolha um vetor de sombra $r_0^*$ tal que o produto interno $\langle r_0^*, r_0 \rangle \neq 0$ (comumente escolhe-se $r_0^* = r_0$).
4. Defina as variáveis iniciais: $\rho_0 = \alpha = \omega_0 = 1$ e os vetores $v_0 = p_0 = 0$ (vetores nulos).

### Laço Iterativo (para $k = 1, 2, 3, \dots$)
Em cada iteração $k$, execute os seguintes passos ordenadamente:

1. $\rho_k = \langle r_0^*, r_{k-1} \rangle$
2. Se $\rho_k = 0$, o método falhou (quebra do método / *breakdown*).
3. $\beta = \left( \frac{\rho_k}{\rho_{k-1}} \right) \left( \frac{\alpha}{\omega_{k-1}} \right)$
4. $p_k = r_{k-1} + \beta (p_{k-1} - \omega_{k-1} v_{k-1})$
5. $v_k = A p_k$ *(Primeira multiplicação matriz-vetor)*
6. $\alpha = \frac{\rho_k}{\langle r_0^*, v_k \rangle}$
7. $s = r_{k-1} - \alpha v_k$
8. Se $\Vert{}s\Vert{}$ for menor que a tolerância estipulada, atualize a solução $x_k = x_{k-1} + \alpha p_k$ e pare (convergência prematura).
9. $t = A s$ *(Segunda multiplicação matriz-vetor)*
10. $\omega_k = \frac{\langle t, s \rangle}{\langle t, t \rangle}$
11. $x_k = x_{k-1} + \alpha p_k + \omega_k s$ *(Atualização da solução)*
12. $r_k = s - \omega_k t$ *(Atualização do resíduo)*
13. Se $\Vert{}r_k\Vert{}$ for menor que a tolerância, o método convergiu. Pare o laço.

---

## 3. Precondicionamento

O **precondicionamento** é uma técnica essencial para o BiCGSTAB na prática. Sistemas lineares reais frequentemente possuem matrizes mal-condicionadas, o que atrasa a convergência ou gera instabilidade numérica. O objetivo é transformar o sistema original $Ax = b$ em um sistema equivalente com propriedades numéricas melhores, injetando uma matriz precondicionadora $M$ que aproxima a inversa de A ($M \approx A^{-1}$).

### Versão Precondicionada à Direita
A abordagem mais comum para o BiCGSTAB é o **precondicionamento à direita**, transformando o sistema em $(AM^{-1})(Mx) = b$. Essa escolha é ideal porque avalia o resíduo verdadeiro diretamente.

#### Algoritmo Modificado (Passo a Passo)

**Inicialização:**
1. Escolha $x_0$. Calcule $r_0 = b - A x_0$.
2. Escolha $r_0^*$ (ex: $r_0^* = r_0$).
3. Defina $\rho_0 = \alpha = \omega_0 = 1$ e $v_0 = p_0 = 0$.

**Laço Iterativo (para $k = 1, 2, \dots$):**
1. $\rho_k = \langle r_0^*, r_{k-1} \rangle$
2. $\beta = \left( \frac{\rho_k}{\rho_{k-1}} \right) \left( \frac{\alpha}{\omega_{k-1}} \right)$
3. $p_k = r_{k-1} + \beta (p_{k-1} - \omega_{k-1} v_{k-1})$
4. **Resolva $M \hat{p} = p_k$** *(Passo do precondicionador)*
5. $v_k = A \hat{p}$
6. \alpha = \frac{\rho_k}{\langle r_0^*, v_k \rangle}
7. $s = r_{k-1} - \alpha v_k$
8. Se $\Vert{}s\Vert{} < \text{tol}$: $x_k = x_{k-1} + \alpha \hat{p}$ e pare.
9. **Resolva $M \hat{s} = s$** *(Passo do precondicionador)*
10. $t = A \hat{s}$
11. $\omega_k = \frac{\langle t, s \rangle}{\langle t, t \rangle}$
12. $x_k = x_{k-1} + \alpha \hat{p} + \omega_k \hat{s}$
13. $r_k = s - \omega_k t$
14. Se $\Vert{}r_k\Vert{} < \text{tol}$, convergiu. Pare.

> 💡 **Nota de Custo:** Além das 2 multiplicações matriz-vetor (passos 5 e 10), cada iteração exige **resolver 2 sistemas lineares com M** (passos 4 e 9). Portanto, $M$ precisa ser de fácil inversão.

---

## 4. Implementação Prática em Python

Abaixo está um script completo em Python utilizando o **SciPy** capaz de gerar um sistema sintético de teste ou carregar matrizes reais externas a partir de arquivos nos formatos **Matrix Market (`.mtx`)** ou binários do NumPy (`.npy`, `.npz`). O código compara o BiCGSTAB puro com o método precondicionado via **Fatoração LU Incompleta (ILU)**.

```python
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import scipy.io as sio

class IterationCounter:
    def __init__(self):
        self.count = 0
    def __call__(self, xk):
        self.count += 1

def carregar_ou_gerar_sistema(caminho_A=None, caminho_b=None):
    """Carrega matriz de arquivos externos ou gera um sistema sintético de teste."""
    if caminho_A is not None:
        ext_A = os.path.splitext(caminho_A).lower()
        if ext_A == '.mtx':
            print(f"Carregando matriz A (.mtx): {caminho_A}")
            A = sio.mmread(caminho_A).tocsr()
        elif ext_A == '.npy':
            print(f"Carregando matriz A (.npy): {caminho_A}")
            A = sp.csr_matrix(np.load(caminho_A))
        elif ext_A == '.npz':
            print(f"Carregando matriz A (.npz): {caminho_A}")
            A = sp.load_npz(caminho_A)
        else:
            raise ValueError("Formato de A inválido. Use .mtx, .npy ou .npz")
            
        if caminho_b is not None:
            ext_b = os.path.splitext(caminho_b).lower()
            if ext_b == '.mtx':
                b = sio.mmread(caminho_b).flatten()
            elif ext_b == '.npy':
                b = np.load(caminho_b).flatten()
            else:
                raise ValueError("Formato de b inválido. Use .mtx ou .npy")
        else:
            print("Gerando vetor b padrão (vetor de uns).")
            b = np.ones(A.shape[0])
    else:
        print("Gerando matriz sintética de teste (malha 50x50)...")
        n = 50
        size = n * n
        diags = [
            -1.5 * np.ones(size), -1.0 * np.ones(size),
             4.0 * np.ones(size),
            -1.2 * np.ones(size), -0.8 * np.ones(size)
        ]
        A = sp.diags(diags, [-n, -1, 0, 1, n], shape=(size, size), format='csr')
        b = A @ np.ones(size)
        
    return A, b

# --- Execução do Exemplo ---
# Para usar arquivos externos, mude para: A, b = carregar_ou_gerar_sistema("matriz.mtx", "vetor.npy")
A, b = carregar_ou_gerar_sistema()

print(f"Dimensões do sistema: {A.shape}")
print(f"Número de elementos não-zero (nnz): {A.nnz}\n")

# 1. Execução sem precondicionador
counter_puro = IterationCounter()
x_puro, info_puro = spla.bicgstab(A, b, tol=1e-6, maxiter=1000, callback=counter_puro)
print("=== BiCGSTAB Puro ===")
print(f"Status: {'Sucesso' if info_puro == 0 else 'Falha'}")
print(f"Iterações: {counter_puro.count}")

# 2. Execução com precondicionador ILU
print("\n=== BiCGSTAB + Precondicionador ILU ===")
ilu = spla.spilu(A, fill_factor=10.0)
M_linear_operator = spla.LinearOperator(A.shape, ilu.solve)

counter_pre = IterationCounter()
x_pre, info_pre = spla.bicgstab(A, b, tol=1e-6, maxiter=1000, M=M_linear_operator, callback=counter_pre)
print(f"Status: {'Sucesso' if info_pre == 0 else 'Falha'}")
print(f"Iterações: {counter_pre.count}")

# Erro relativo numérico
erro = np.linalg.norm(b - A @ x_pre) / np.linalg.norm(b)
print(f"\nResíduo relativo final (ILU): {erro:.2e}")
```
