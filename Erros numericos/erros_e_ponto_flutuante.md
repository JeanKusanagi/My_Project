# Guia Completo: Erros Numéricos, de Arredondamento e Ponto Flutuante

Este documento reúne de forma estruturada os conceitos fundamentais sobre erros absolutos, relativos, propagação de erros e a representação de ponto flutuante em computadores.

---

## 1. Erro Absoluto e Erro de Arredondamento

### Erro Absoluto
O **erro absoluto** é a distância ou a diferença em módulo entre o valor exato ($x$) e o seu valor aproximado ($\bar{x}$):

$$\text{Erro Absoluto} = \vert{}x - \bar{x}\vert{}$$

* **Sinal:** É sempre um número maior ou igual a zero devido ao módulo.
* **Unidade:** Possui a **mesma unidade de medida** da grandeza original (metros, gramas, segundos, etc.).
* **Limitação:** Mede o "tamanho bruto" do desvio, mas sozinho não diz se o erro é grave. Um erro de $1\text{ cm}$ é enorme para um parafuso, mas irrelevante para a distância entre duas cidades.

### Erro de Arredondamento
É um erro computacional ou numérico que ocorre quando representamos um número real com uma **quantidade finita de casas decimais** ou de algarismos significativos. É inerente ao uso de calculadoras e computadores, que precisam truncar ou arredondar valores para caber na memória.

#### Exemplo Prático com o Número $\pi$:
* **Valor exato ($x$):** $\pi \approx 3,14159265...$
* **Valor aproximado ($\bar{x}$):** $3,14$ (arredondado para duas casas decimais)
* **Erro Absoluto:** $\vert{}3,14159... - 3,14\vert{} = 0,00159...$

---

## 2. Erro Relativo

O **erro relativo** é a razão entre o erro absoluto e o valor exato (ou aproximado, por convenção). Ele serve para medir a **gravidade ou o impacto** do erro em relação ao tamanho do objeto analisado.

$$\text{Erro Relativo} = \frac{\text{Erro Absoluto}}{\vert{}x\vert{}} = \frac{\vert{}x - \bar{x}\vert{}}{\vert{}x\vert{}}$$

* **Unidade:** Não possui unidade de medida (é um número puro), sendo frequentemente expresso em **porcentagem**.
* **Utilidade:** Permite comparar a precisão de medições de escalas diferentes.

### Comparativo de Impacto (Erro Absoluto vs. Erro Relativo)

| Objeto Medido | Valor Exato ($x$) | Valor Aproximado ($\bar{x}$) | Erro Absoluto | Erro Relativo | Impacto Real |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Parafuso** | $5\text{ cm}$ | $6\text{ cm}$ | **$1\text{ cm}$** | $\frac{1}{5} = 20\%$ | **Gravíssimo** |
| **Prédio** | $5.000\text{ cm}$ | $5.001\text{ cm}$ | **$1\text{ cm}$** | $\frac{1}{5000} = 0,02\%$ | **Irrelevante** |

---

## 3. Limite de Erro em Operações (Propagação de Erros)

Quando realizamos operações matemáticas com valores que já contêm erros (como dados experimentais ou números arredondados), esses erros se propagam pelo cálculo.

### 1. Na Soma (e Subtração)
O limite do erro absoluto do resultado é a **soma dos erros absolutos** de cada termo individual.

* **Barra A:** $10\text{ cm} \pm 0,1\text{ cm}$ (Erro de A = $0,1$)
* **Barra B:** $15\text{ cm} \pm 0,2\text{ cm}$ (Erro de B = $0,2$)
* **Comprimento Total:** $10 + 15 = 25\text{ cm}$
* **Erro Absoluto Máximo:** $\Delta(A + B) = 0,1 + 0,2 = \mathbf{0,3\text{ cm}}$
* **Resultado Final:** $25\text{ cm} \pm 0,3\text{ cm}$

### 2. Na Multiplicação (e Divisão)
Na multiplicação, o **erro relativo** do resultado final é aproximadamente igual à **soma dos erros relativos** de cada termo.

* **Lado A do terreno:** $10\text{ m}$ com erro relativo de $1\% = 0,01$
* **Lado B do terreno:** $20\text{ m}$ com erro relativo de $2\% = 0,02$
* **Área Nominal:** $10 \times 20 = 200\text{ m}^2$
* **Erro Relativo Máximo:** $1\% + 2\% = \mathbf{3\% \ (0,03)}$
* **Erro Absoluto da Área:** $200\text{ m}^2 \times 0,03 = \mathbf{6\text{ m}^2}$
* **Resultado Final:** $200\text{ m}^2 \pm 6\text{ m}^2$

---

## 4. O Sistema de Ponto Flutuante em Computadores

Os computadores modernos representam números reais usando o sistema de ponto flutuante, padronizado internacionalmente pela norma **IEEE 754**. 

O cerne do problema é que computadores calculam em **binário (base 2)**, enquanto nós pensamos em **decimal (base 10)**. Isso gera dízimas periódicas binárias para números simples, resultando em pequenas imprecisões na memória.

### O Caso Clássico: Por que `0.1 + 0.2` resulta em `0.30000000000000004`?
1. O número $0.1$ em decimal se transforma em uma dízima periódica em binário: $0.0001100110011..._2$.
2. Devido ao espaço finito na memória, o computador **arredonda** esse valor binário.
3. Ao somar $0.1$ e $0.2$ (ambos já ligeiramente modificados na memória), os erros absolutos se acumulam e se manifestam nas últimas casas decimais exibidas na tela.

### Arquitetura de Armazenamento (IEEE 754)
Qualquer número em ponto flutuante é dividido internamente em três partes:
* **Sinal:** Determina se o número é positivo ou negativo.
* **Mantissa (ou Fração):** Guarda os algarismos significativos e determina a precisão.
* **Expoente:** Define a magnitude do número (onde o ponto decimal vai "flutuar").

É o equivalente digital à notação científica padrão: $\mathbf{+1,234 \times 10^3}$.

### Tipos de Precisão

| Tipo de Precisão | Tamanho Total | Espaço da Mantissa | Casas Decimais Confiáveis |
| :--- | :--- | :--- | :--- |
| **Precisão Simples (`float`)** | 32 bits | 23 bits | Cerca de **7 casas** decimais |
| **Precisão Dupla (`double`)** | 64 bits | 52 bits | Cerca de **15 a 17 casas** decimais |

### O Épsilon da Máquina ($\epsilon$)
É o menor número positivo que, somado a 1, gera um resultado diferente de 1 na arquitetura do computador ($1 + \epsilon \neq 1$). Se você tentar somar um valor menor que o épsilon a um número muito grande, a mantissa perde a capacidade de registrar a diferença e o valor menor é ignorado. Esse fenômeno é conhecido como **erro de cancelamento**.

---

## 5. Boas Práticas de Programação

Para mitigar e evitar bugs causados por erros de arredondamento em sistemas práticos, siga estas diretrizes:

### 1. Nunca compare floats diretamente usando igualdade (`==`)
* ❌ **Incorreto:**
  ```python
  if (x + y == 0.3):
      # Pode falhar mesmo se logicamente devesse ser 0.3
  ```
*  **Correto:** Verifique se a diferença absoluta entre os valores é menor que uma margem de tolerância muito pequena:
  ```python
  if abs((x + y) - 0.3) < 0.00001:
      # Código seguro para ponto flutuante
  ```

### 2. Tratamento de Valores Financeiros (Dinheiro)
* 🛑 **Regra de Ouro:** **Nunca** use tipos flutuantes primitivos (`float` ou `double`) para processar dinheiro. Os erros acumulados causarão inconsistências em saldos e relatórios.
* **Soluções:**
  * Utilize tipos de precisão decimal arbitrária nativos da linguagem (como `Decimal` no Python/C# ou `BigDecimal` no Java).
  * Armazene e opere os valores monetários estritamente como números **inteiros**, representando a menor unidade fracionária (centavos). Por exemplo, um preço de R\$ 1,50 deve ser armazenado na memória e no banco de dados como o inteiro `150`.
