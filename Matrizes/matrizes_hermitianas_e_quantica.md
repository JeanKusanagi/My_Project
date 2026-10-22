# Matrizes Complexas Hermitianas e suas Aplicações na Física Quântica

Uma **matriz hermitiana** (ou autoajunta) é uma matriz quadrada com entradas complexas que é igual à sua própria transposta conjugada, ou seja, $A = A^{\mathsf{H}}$ (onde $A^{\mathsf{H}} = (\overline{A})^{\mathsf{T}}$). Elas são consideradas a generalização complexa das matrizes reais simétricas.

---

## 1. Principais Propriedades

* **Diagonal principal:** Todos os elementos da diagonal principal de uma matriz hermitiana são obrigatoriamente **números reais**.
* **Autovalores:** Todos os autovalores de uma matriz hermitiana são **sempre reais**.
* **Autovetores:** Autovetores associados a autovalores distintos são **ortogonais** entre si, e a matriz é unitariamente diagonalizável.
* **Soma e Produto:** A soma de duas matrizes hermitianas é hermitiana. O produto $AB$ é hermitiano se, e somente se, as matrizes comutam ($AB = BA$).

### Exemplo Prático de Estrutura
Uma matriz $2 \times 2$ hermitiana tem a seguinte forma geral:
$$A = \begin{pmatrix} a & b + ci \\ b - ci & d \end{pmatrix}$$
Onde $a, d \in \mathbb{R}$ (números reais na diagonal) e $b + ci$ é o conjugado complexo de $b - ci$. Um exemplo numérico clássico é a **Matriz de Pauli $\sigma_x$**:
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

---

## 2. Exemplo de Cálculo de Autovalores e Autovetores

Vamos analisar a seguinte matriz hermitiana $A$:
$$A = \begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix}$$

### Passo 1: Encontrar os Autovalores
Usamos a equação característica $\det(A - \lambda I) = 0$:
$$\det \begin{pmatrix} 2 - \lambda & 1 + i \\ 1 - i & 3 - \lambda \end{pmatrix} = 0$$

$$\det(A - \lambda I) = (2 - \lambda)(3 - \lambda) - (1 + i)(1 - i)$$
$$\det(A - \lambda I) = (\lambda^2 - 5\lambda + 6) - (1^2 - i^2)$$
$$\det(A - \lambda I) = \lambda^2 - 5\lambda + 6 - 2 = \lambda^2 - 5\lambda + 4$$

Resolvendo a equação quadrática $\lambda^2 - 5\lambda + 4 = 0$, encontramos:
* **$\lambda_1 = 1$**
* **$\lambda_2 = 4$**

*(Como previsto, todos os autovalores calculados são números puramente reais).*

### Passo 2: Encontrar os Autovetores
Substituindo cada $\lambda$ na equação $(A - \lambda I)v = 0$:

1. **Para $\lambda_1 = 1$:**
   $$\begin{pmatrix} 1 & 1 + i \\ 1 - i & 2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x + (1 + i)y = 0 \implies x = -(1 + i)y$$
   Escolhendo $y = 1$, temos $v_1 = \begin{pmatrix} -1 - i \\ 1 \end{pmatrix}$.

2. **Para $\lambda_2 = 4$:**
   $$\begin{pmatrix} -2 & 1 + i \\ 1 - i & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies (1 - i)x - y = 0 \implies y = (1 - i)x$$
   Escolhendo $x = 1$, temos $v_2 = \begin{pmatrix} 1 \\ 1 - i \end{pmatrix}$.

### Passo 3: Verificação de Ortogonalidade
No espaço complexo, calculamos o produto interno usando o transposto conjugado $v_1^{\mathsf{H}}$:
$$\langle v_1, v_2 \rangle = v_1^{\mathsf{H}} v_2 = \begin{pmatrix} -1 + i & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 - i \end{pmatrix}$$
$$\langle v_1, v_2 \rangle = (-1 + i)(1) + (1)(1 - i) = -1 + i + 1 - i = 0$$
Como o resultado é **zero**, os autovetores são estritamente **ortogonais**.

---

## 3. Diagonalização Unitária

Para realizar a diagonalização unitária, normalizamos os autovetores dividindo-os por suas respectivas normas (ambos possuem norma igual a $\sqrt{3}$):
$$\hat{v}_1 = \frac{1}{\sqrt{3}} \begin{pmatrix} -1 - i \\ 1 \end{pmatrix}, \quad \hat{v}_2 = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 1 - i \end{pmatrix}$$

Construímos a matriz unitária de transição $P$:
$$P = \frac{1}{\sqrt{3}} \begin{pmatrix} -1 - i & 1 \\ 1 & 1 - i \end{pmatrix}$$

A diagonalização é dada por $P^{\mathsf{H}} A P = D$, resultando na matriz diagonal dos autovalores:
$$D = \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix}$$

---

## 4. A Equação de Schrödinger e Sistemas Quânticos

Na mecânica quântica, as propriedades físicas observáveis são representadas por operadores ou matrizes hermitianas. A **Equação de Schrödinger Dependente do Tempo** é dada por:
$$i\hbar \frac{\partial}{\partial t} \vert{}\Psi(t)\rangle = \hat{H} \vert{}\Psi(t)\rangle$$

Onde $\hat{H}$ é o operador **Hamiltoniano** (energia total). Ele **deve ser hermitiano** para assegurar que:
1. Os valores de energia medidos (autovalores de $\hat{H}$) sejam estritamente reais.
2. A evolução temporal conserve a probabilidade total do sistema (evolução unitária).

### Exemplo de um Qubit (Hamiltoniano Simples)
Considere um sistema de dois níveis com o Hamiltoniano:
$$\hat{H} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$
Resolvendo $\det(\hat{H} - E \cdot I) = 0$, obtemos os níveis de energia **$E_1 = 1$** e **$E_2 = -1$**. Seus respectivos estados estacionários normalizados são:
$$\vert{}\psi_1\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} -i \\ 1 \end{pmatrix}, \quad \vert{}\psi_2\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} i \\ 1 \end{pmatrix}$$

---

## 5. Portas Lógicas na Computação Quântica

Enquanto os observáveis de um sistema são hermitianos, as **portas lógicas quânticas são representadas por matrizes unitárias ($U^{\mathsf{H}}U = I$)**, as quais descrevem transformações e rotações puras que preservam a probabilidade total dos estados quânticos.

As portas lógicas mais comuns para um único qubit são:

* **Porta X (NOT):** $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ — Inverte o estado do qubit (transforma $\vert{}0\rangle$ em $\vert{}1\rangle$).
* **Porta Z:** $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ — Inverte a fase do estado $\vert{}1\rangle$.
* **Porta H (Hadamard):** $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ — Coloca o qubit em um estado de superposição perfeita.

### Resumo de Diferenças e Conexões

| Característica | Matriz Hermitiana ($A$) | Matriz Unitária ($U$) |
| :--- | :--- | :--- |
| **Definição** | $A^{\mathsf{H}} = A$ | $U^{\mathsf{H}} = U^{-1}$ |
| **Autovalores** | Números Reais ($\lambda \in \mathbb{R}$) | Módulo igual a 1 ($e^{i\theta}$) |
| **Ação Física** | Representa uma medição/observável | Representa evolução ou porta lógica |

**Ponte Matemática:** Uma matriz hermitiana $A$ gera uma matriz unitária através da exponencial complexa: $U = e^{iA}$. Matrizes especiais como as de Pauli e a de Hadamard atendem a ambos os critérios simultaneamente ($A = A^{\mathsf{H}} = A^{-1}$), sendo chamadas de involutivas.
