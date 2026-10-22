# Transposta Conjugada (Matriz Hermitiana)

O **transposto conjugado** (também conhecido como transposta hermitiana ou adjunta) de uma matriz complexa é a matriz obtida pela troca de suas linhas por colunas e pela substituição de cada elemento pelo seu respectivo conjugado complexo.

## Notações e Definição
* **Símbolos mais comuns:** $A^H$, $A^*$, $A'$ ou $A^\dagger$ (geralmente usado em física quântica).
* **Fórmula:** $(A^H)_{ij} = \overline{A_{ji}}$
* Se uma matriz $A$ possui dimensão $m \times n$, o seu transposto conjugado $A^H$ terá dimensão $n \times m$.
* Para matrizes com **entradas estritamente reais**, o transposto conjugado é exatamente igual à transposta convencional ($A^H = A^T$).

## Propriedades Principais
1. **Involução:** $(A^H)^H = A$
2. **Soma:** $(A + B)^H = A^H + B^H$
3. **Produto escalar:** $(\alpha A)^H = \overline{\alpha} A^H$ (onde $\alpha$ é um número complexo)
4. **Produto matricial:** $(AB)^H = B^H A^H$ (a ordem dos fatores é invertida)
5. **Autovalores:** Os autovalores de uma matriz que é igual à sua transposta conjugada ($A = A^H$, dita Hermitiana) são sempre números reais.

---

## Exemplo Prático Passo a Passo

Dada a matriz $A$ de ordem $2 \times 3$:

$$A = \begin{pmatrix} 1 + i & 5 & -2i \\ 3 & 2 - 4i & i \end{pmatrix}$$

Para encontrar a transposta conjugada ($A^H$), realizamos o processo em dois passos:

### Passo 1: Calcular o Conjugado Complexo ($\overline{A}$)
Invertemos o sinal da parte imaginária de cada um dos elementos da matriz (trocando $+i$ por $-i$ e vice-versa):

$$\overline{A} = \begin{pmatrix} 1 - i & 5 & 2i \\ 3 & 2 + 4i & -i \end{pmatrix}$$

### Passo 2: Transpor a Matriz ($A^H = (\overline{A})^T$)
Permutamos as linhas pelas colunas. A matriz resultante passa a ter a ordem $3 \times 2$:

$$A^H = \begin{pmatrix} 1 - i & 3 \\ 5 & 2 + 4i \\ 2i & -i \end{pmatrix}$$

---

### Mapeamento dos Elementos

| Elemento Original ($A_{ij}$) | Elemento Transposto Conjugado ($A^H_{ji}$) |
| :--- | :--- |
| **$1 + i$** (linha 1, col 1) | **$1 - i$** (linha 1, col 1) |
| **$5$** (linha 1, col 2) | **$5$** (linha 2, col 1) |
| **$-2i$** (linha 1, col 3) | **$2i$** (linha 3, col 1) |
| **$3$** (linha 2, col 1) | **$3$** (linha 1, col 2) |
| **$2 - 4i$** (linha 2, col 2) | **$2 + 4i$** (linha 2, col 2) |
| **$i$** (linha 2, col 3) | **$-i$** (linha 3, col 2) |