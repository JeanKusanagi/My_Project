# Guia Completo: Equação de Poisson, Resolução Analítica e Métodos Numéricos (MDF e SOR)

A **Equação de Poisson** é uma Equação Diferencial Parcial (EDP) de segunda ordem, classificada como elíptica, amplamente utilizada na física teórica e na engenharia para modelar fenômenos com termos fontes.

---

## 1. Definição Matemática

A forma geral da Equação de Poisson é expressa por:

$$\nabla^2 \varphi = f$$

Onde:
* **$\varphi$** é a função desconhecida (campo escalar a ser determinado).
* **$\nabla^2$** (ou $\Delta$) é o operador Laplaciano, que representa a divergência do gradiente.
* **$f$** é uma função conhecida chamada de **termo fonte**.

> **Nota:** Quando o termo fonte é nulo ($f = 0$), a equação transforma-se na **Equação de Laplace** ($\nabla^2 \varphi = 0$).

---

## 2. Exemplo Prático Unidimensional (1D)

Para demonstrar a aplicação física e matemática, analisamos o potencial elétrico entre duas placas condutoras paralelas e infinitas separadas por uma distância $L$. O espaço entre elas está preenchido com uma densidade de carga elétrica uniforme $\rho_0$.

A placa em $x = 0$ está aterrada ($V = 0$) e a placa em $x = L$ está submetida a um potencial de bateria $V_0$.

### Modelagem do Problema
Como o potencial varia apenas na direção $x$, a equação reduz-se a uma Equação Diferencial Ordinária (EDO):

$$\frac{d^2 V(x)}{dx^2} = -\frac{\rho_0}{\varepsilon_0}$$

Onde $\varepsilon_0$ é a permissividade elétrica do vácuo.

**Condições de Contorno:**
1. $V(0) = 0$
2. $V(L) = V_0$

---

## 3. Resolução Analítica Passo a Passo

### Passo 1: Primeira Integração
Integrando ambos os lados em relação a $x$ para reduzir a ordem da derivada:

$$\frac{dV(x)}{dx} = -\frac{\rho_0}{\varepsilon_0}x + C_1$$

### Passo 2: Segunda Integração
Integrando novamente para encontrar a função do potencial $V(x)$:

$$V(x) = -\frac{\rho_0}{2\varepsilon_0}x^2 + C_1x + C_2$$

### Passo 3: Aplicação das Condições de Contorno
* **Aplicando $V(0) = 0$:**
  $$V(0) = -\frac{\rho_0}{2\varepsilon_0}(0)^2 + C_1(0) + C_2 = 0 \implies C_2 = 0$$

* **Aplicando $V(L) = V_0$:**
  $$V(L) = -\frac{\rho_0}{2\varepsilon_0}L^2 + C_1L = V_0 \implies C_1 = \frac{V_0}{L} + \frac{\rho_0 L}{2\varepsilon_0}$$

### Solução Final do Potencial
Substituindo as constantes de volta na equação original e reorganizando os termos, obtemos a distribuição explícita do potencial:

$$V(x) = \frac{V_0}{L}x + \frac{\rho_0}{2\varepsilon_0}x(L - x)$$

---

## 4. Dedução do Campo Elétrico $E(x)$

Na eletrostática, o campo elétrico é o gradiente negativo do potencial elétrico ($E = -\nabla V$). No caso unidimensional:

$$E(x) = -\frac{dV(x)}{dx}$$

Derivando a solução analítica obtida para $V(x)$ em relação a $x$:

$$\frac{dV(x)}{dx} = \frac{V_0}{L} + \frac{\rho_0 L}{2\varepsilon_0} - \frac{\rho_0}{\varepsilon_0}x$$

Multiplicando por $-1$, chegamos à expressão final do Campo Elétrico:

$$E(x) = \frac{\rho_0}{\varepsilon_0}\left(x - \frac{L}{2}\right) - \frac{V_0}{L}$$

* **Análise Física:** O campo elétrico varia de maneira **linear** ao longo do espaço. O termo $-\frac{V_0}{L}$ representa o campo constante gerado pelas placas, enquanto o termo $\frac{\rho_0}{\varepsilon_0}(x - \frac{L}{2})$ representa a contribuição simétrica das cargas volumétricas internas.

---

## 5. Abordagem Numérica: Diferenças Finitas (MDF)

Para resolver o problema no computador, discretizamos o domínio contínuo em uma malha de $N$ intervalos de tamanho $\Delta x = \frac{L}{N}$. 

Aproximamos a segunda derivada pela **fórmula de diferença central de segunda ordem**:

$$\frac{d^2 V}{dx^2} \approx \frac{V_{i+1} - 2V_i + V_{i-1}}{(\Delta x)^2}$$

Substituindo na Equação de Poisson e isolando o ponto central $V_i$, obtemos a equação algébrica iterativa usada pelos algoritmos numéricos:

$$V_i = \frac{V_{i+1} + V_{i-1}}{2} + \frac{(\Delta x)^2 \cdot \rho_i}{2\varepsilon_0}$$

---

## 6. O Método de Sobrerrelaxação Sucessiva (SOR)

O **SOR** (*Successive Over-Relaxation*) acelera a convergência do método iterativo Gauss-Seidel introduzindo um fator de relaxação $\omega$ (onde $1 < \omega < 2$). A fórmula do algoritmo calcula uma média ponderada entre o valor atual e a nova estimativa calculada:

$$V_i^{\text{novo}} = (1 - \omega)V_i^{\text{atual}} + \omega \left[ \frac{V_{i+1}^{\text{atual}} + V_{i-1}^{\text{novo}}}{2} + \frac{(\Delta x)^2 \cdot \rho_i}{2\varepsilon_0} \right]$$

---

## 7. Implementação Completa em Python (SOR + Campo Elétrico)

O script abaixo utiliza o método SOR para encontrar o potencial elétrico e a função `np.gradient` para extrair o campo elétrico correspondente, plotando ambos em gráficos comparativos com a solução exata.

```python
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# 1. PARÂMETROS DO PROBLEMA & MALHA
# ==============================================================================
L = 1.0                # Distância entre as placas (m)
V0 = 10.0              # Potencial na placa direita (V)
rho0 = 1e-9            # Densidade de carga uniforme (C/m³)
epsilon0 = 8.854e-12    # Permissividade do vácuo (F/m)

N = 100                # Número de intervalos da malha
Nx = N + 1             # Número de nós
dx = L / N             # Tamanho do intervalo espacial (Delta x)
x = np.linspace(0, L, Nx)

# ==============================================================================
# 2. CONFIGURAÇÕES DO MÉTODO ITERATIVO (SOR)
# ==============================================================================
omega = 1.85           # Fator de aceleração/relaxação (1 < omega < 2)
tol = 1e-6             # Tolerância para o critério de parada
max_iter = 10000       # Limite máximo de iterações

V = np.zeros(Nx)       # Chute inicial zerado para o potencial
V = 0.0             # Condição de contorno: placa esquerda
V[N] = V0              # Condição de contorno: placa direita

# Termo fonte constante pré-calculado para os pontos internos
termo_fonte = (dx**2) * (rho0 / (2 * epsilon0))

# Loop de Iteração SOR
for iteracao in range(max_iter):
    V_velho = V.copy()
    
    # Atualização ponto a ponto dos nós internos
    for i in range(1, N):
        V_gs = 0.5 * (V[i+1] + V[i-1]) + termo_fonte
        V[i] = (1 - omega) * V[i] + omega * V_gs
        
    # Critério de convergência baseado na variação máxima absoluta
    erro = np.max(np.abs(V - V_velho))
    if erro < tol:
        print(f"O método SOR convergiu com sucesso em {iteracao} iterações.")
        break
else:
    print("Aviso: O limite máximo de iterações foi atingido.")

# ==============================================================================
# 3. EXTRAÇÃO DO CAMPO ELÉTRICO
# ==============================================================================
# Cálculo numérico do Campo através do gradiente negativo do potencial discreto
E_numerico = -np.gradient(V, dx)

# Soluções Analíticas Exatas para validação
V_analitico = (V0 / L) * x + (rho0 / (2 * epsilon0)) * x * (L - x)
E_analitico = (rho0 / epsilon0) * (x - L/2) - (V0 / L)

# ==============================================================================
# 4. VISUALIZAÇÃO DOS GRÁFICOS
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Potencial Elétrico
ax1.plot(x, V, 'mo', label=f'SOR Numérico ($\\omega$={omega})', markersize=4)
ax1.plot(x, V_analitico, 'k-', label='Analítico Exato')
ax1.set_title('Perfil de Potencial Elétrico V(x)')
ax1.set_xlabel('Posição x (m)')
ax1.set_ylabel('Potencial V (Volts)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend()

# Gráfico 2: Campo Elétrico
ax2.plot(x, E_numerico, 'go', label='Gradiente Numérico', markersize=4)
ax2.plot(x, E_analitico, 'k-', label='Analítico Exato')
ax2.set_title('Perfil do Campo Elétrico E(x)')
ax2.set_xlabel('Posição x (m)')
ax2.set_ylabel('Campo Elétrico E (V/m)')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend()

plt.tight_layout()
plt.show()
```