# Métodos Numéricos para Resolução de Sistemas Lineares
## Métodos Diretos, Iterativos e Análise de Convergência — Material de Estudo

---

## 1. Conceito Central

Um **sistema linear** Ax = b, onde A é uma matriz n×n, x é o vetor de incógnitas e b é o vetor de termos independentes, aparece constantemente em engenharia, ciência de dados, simulações físicas e otimização. **Métodos numéricos** são necessários porque, para sistemas de porte real (centenas, milhares ou milhões de equações), soluções puramente "algébricas" (como a Regra de Cramer) são **computacionalmente inviáveis**.

> **Definição de prova:** "Métodos numéricos para sistemas lineares se dividem em duas grandes famílias: **métodos diretos**, que obtêm a solução exata (a menos de erros de arredondamento) em um número finito e predeterminado de operações; e **métodos iterativos**, que geram uma sequência de aproximações que **converge** para a solução, sem garantia de terminar em um número fixo de passos."

⚠️ **Pegadinha clássica de prova:** achar que a **Regra de Cramer** (usar determinantes) é um método numérico prático para resolver sistemas grandes. Seu custo computacional é da ordem de **O(n!)** (calculando n+1 determinantes via expansão de cofatores) — **proibitivo** mesmo para n moderado (ex.: n=20 já é inviável). Na prática, usa-se **Eliminação de Gauss**, com custo **O(n³)**, drasticamente mais eficiente.

---

## 2. Métodos Diretos

### 2.1 Eliminação de Gauss (Gaussian Elimination)
- Transforma o sistema Ax = b em um sistema **triangular superior equivalente**, através de operações elementares sobre as linhas (combinações lineares entre equações), e depois resolve por **substituição regressiva (backward substitution)**.
- **Complexidade:** O(n³) para a eliminação, O(n²) para a substituição — a eliminação domina o custo total.

### 2.2 Pivoteamento (Pivoting)
- Durante a eliminação, se o **elemento pivô** (na diagonal) for **zero ou muito pequeno**, o processo falha ou se torna numericamente instável.
- **Pivoteamento parcial:** troca linhas para colocar, em cada etapa, o **maior elemento em módulo da coluna** na posição de pivô.
- **Pivoteamento total:** troca linhas **e colunas**, buscando o maior elemento em módulo em toda a submatriz restante (mais custoso, raramente necessário na prática).

⚠️ **Pegadinha número 1 (muito cobrada):** achar que o pivoteamento só é necessário quando o pivô é **exatamente zero**. Na prática, pivôs **muito pequenos** (mesmo que não nulos) causam **amplificação de erros de arredondamento** (divisão por número próximo de zero gera valores muito grandes, propagando erro numérico) — por isso o pivoteamento parcial é **prática padrão recomendada**, não apenas uma correção emergencial.

### 2.3 Fatoração LU (Decomposição LU)
- Decompõe a matriz A em um **produto de duas matrizes triangulares**: A = LU, onde L é triangular inferior (com 1's na diagonal, na forma mais comum) e U é triangular superior.
- Depois, resolve-se o sistema original em **duas etapas mais baratas**: Ly = b (substituição direta/forward substitution) e Ux = y (substituição regressiva).

**Grande vantagem prática da fatoração LU (muito cobrada):** quando é preciso resolver **Ax = b para vários vetores b diferentes**, com a **mesma matriz A**, a fatoração LU é feita **uma única vez** (custo O(n³)), e cada novo sistema é resolvido apenas com as substituições triangulares (custo O(n²) cada) — muito mais eficiente do que repetir a eliminação de Gauss completa para cada b.

⚠️ **Pegadinha:** confundir a fatoração LU com "só mais uma forma de fazer eliminação de Gauss sem vantagem prática". A vantagem central é justamente a **reutilização da fatoração** quando b muda mas A permanece o mesmo — cenário comum em simulações iterativas e otimização.

### 2.4 Fatoração de Cholesky
- Aplicável **apenas quando A é simétrica e positiva definida** — decompõe A = L·Lᵀ, onde L é triangular inferior.
- É aproximadamente **duas vezes mais eficiente** que a fatoração LU genérica, pois explora a simetria da matriz (calcula e armazena aproximadamente metade dos elementos).

⚠️ **Pegadinha:** tentar aplicar Cholesky em uma matriz que **não é simétrica e positiva definida** — o método falha (a decomposição não existe nesse caso, geralmente detectado por uma raiz quadrada de número negativo durante o cálculo). Provas gostam de pedir para verificar essas condições antes de escolher o método.

---

## 3. Métodos Iterativos

### 3.1 Ideia Central
- Em vez de calcular a solução exata em um número fixo de operações, métodos iterativos partem de uma **estimativa inicial x⁽⁰⁾** e geram uma sequência x⁽¹⁾, x⁽²⁾, ... que, sob certas condições, **converge** para a solução real.

**Quando preferir métodos iterativos a diretos (muito cobrado):**
- Sistemas **grandes e esparsos** (muitos zeros), onde métodos diretos desperdiçariam memória e tempo processando/armazenando zeros.
- Quando **apenas uma solução aproximada** é necessária, e não a solução exata.

⚠️ **Pegadinha número 1 (muito cobrada):** achar que métodos diretos são **sempre superiores** por serem "exatos". Para sistemas muito grandes e esparsos (comuns em simulações de elementos finitos, por exemplo), métodos iterativos podem ser **muito mais eficientes em memória e tempo**, pois exploram a esparsidade (não armazenam nem operam sobre os zeros), algo que a eliminação de Gauss tende a destruir (fenômeno de **preenchimento/fill-in**, em que zeros da matriz original se tornam não-zeros durante a eliminação).

### 3.2 Método de Jacobi
- Em cada iteração, calcula **todos os novos valores** x⁽ᵏ⁺¹⁾ usando **apenas os valores da iteração anterior** x⁽ᵏ⁾ — os novos valores só são "publicados" ao final de cada iteração completa.

### 3.3 Método de Gauss-Seidel
- Muito parecido com Jacobi, mas usa os valores **já atualizados na mesma iteração**, assim que disponíveis, em vez de esperar a iteração terminar.

⚠️ **Pegadinha número 1 (a mais cobrada desta seção):** confundir Jacobi com Gauss-Seidel.
- **Jacobi:** só usa valores da **iteração anterior completa**; permite paralelização mais simples (todos os cálculos de uma iteração são independentes entre si).
- **Gauss-Seidel:** usa valores **já atualizados dentro da mesma iteração**, o que geralmente acelera a convergência (usa informação "mais fresca"), mas **dificulta a paralelização** (cada cálculo depende do anterior na mesma iteração).

**Regra prática cobrada em prova:** Gauss-Seidel **geralmente converge mais rápido** que Jacobi (quando ambos convergem), mas isso **não é uma garantia absoluta em todos os casos** — existem sistemas específicos em que Jacobi converge e Gauss-Seidel não, ou vice-versa.

### 3.4 SOR (Successive Over-Relaxation)
- Generaliza o Gauss-Seidel introduzindo um **fator de relaxação ω**, que pondera entre o valor anterior e o novo valor calculado, podendo **acelerar a convergência** quando ω é bem escolhido (0 < ω < 2).
- ω = 1 reduz o SOR exatamente ao Gauss-Seidel.

---

## 4. Critérios de Convergência (o ponto mais cobrado de toda a unidade)

### 4.1 Condição necessária e suficiente
- A convergência dos métodos de Jacobi e Gauss-Seidel é garantida **se e somente se** o **raio espectral** da matriz de iteração for menor que 1 (ρ < 1) — o raio espectral é o maior valor absoluto entre os autovalores da matriz de iteração.

### 4.2 Condição suficiente (mas não necessária) — a mais cobrada na prática
- Se a matriz A é **estritamente diagonalmente dominante** (o valor absoluto do elemento da diagonal, em cada linha, é maior que a soma dos valores absolutos dos demais elementos da linha), então **tanto Jacobi quanto Gauss-Seidel convergem**, para qualquer estimativa inicial.

⚠️ **Pegadinha número 1 (a mais cobrada de toda a unidade de sistemas lineares):** tratar a **dominância diagonal estrita** como condição **necessária** para convergência. Ela é apenas **suficiente**: existem sistemas em que a matriz **não** é diagonalmente dominante, e os métodos **ainda assim convergem** (a condição real, necessária e suficiente, é o raio espectral < 1, que é mais difícil de verificar na prática). Provas adoram pegar quem generaliza "se não é diagonalmente dominante, não converge" — isso é **falso**.

⚠️ **Pegadinha número 2:** confundir dominância diagonal com **matriz simétrica positiva definida** — são propriedades **diferentes**, embora ambas sejam frequentemente usadas como condições facilitadoras de convergência/aplicabilidade de métodos distintos (dominância diagonal → convergência de Jacobi/Gauss-Seidel; simetria positiva definida → aplicabilidade de Cholesky, e também garante convergência de Gauss-Seidel).

### 4.3 Critérios de parada práticos
- **Erro absoluto/relativo entre iterações sucessivas:** ‖x⁽ᵏ⁺¹⁾ − x⁽ᵏ⁾‖ < tolerância.
- **Resíduo:** ‖b − Ax⁽ᵏ⁾‖ < tolerância (mede o quão bem a aproximação atual satisfaz o sistema original).
- **Número máximo de iterações:** critério de segurança para evitar loop infinito em caso de não-convergência.

---

## 5. Número de Condição e Mal Condicionamento (tópico transversal, muito cobrado)

- O **número de condição** de uma matriz, κ(A), mede o quanto **pequenas perturbações** nos dados de entrada (b, ou até erros de arredondamento em A) podem gerar **grandes variações** na solução x.
- Um número de condição **alto** (matriz **mal condicionada**) significa que o sistema é **intrinsecamente sensível** — mesmo com um método numérico perfeito e sem erros de arredondamento no algoritmo, pequenas imprecisões nos dados de entrada podem gerar soluções muito diferentes.

⚠️ **Pegadinha número 1 (muito cobrada):** achar que erro numérico grande sempre indica **falha do método** (Gauss, LU, Jacobi etc.). Se a matriz A é **mal condicionada**, o problema é **do próprio sistema** (sensibilidade inerente), não necessariamente do algoritmo escolhido — trocar de método direto para iterativo (ou vice-versa) **não resolve** um problema de mal condicionamento.

⚠️ **Pegadinha número 2:** confundir **matriz singular** (não invertível, determinante = 0, sistema sem solução única) com **matriz mal condicionada** (invertível, mas numericamente sensível, número de condição alto). São conceitos relacionados, mas distintos — uma matriz mal condicionada ainda tem solução única, só que numericamente instável de se obter.

---

## 6. Quadro Comparativo — Métodos Diretos vs. Iterativos

| Critério | Métodos Diretos (Gauss, LU, Cholesky) | Métodos Iterativos (Jacobi, Gauss-Seidel, SOR) |
|---|---|---|
| **Tipo de resultado** | Solução exata (a menos de erro de arredondamento), em número fixo de operações | Sequência de aproximações que converge (ou não) |
| **Custo computacional** | O(n³) | O(n²) por iteração (matriz densa); pode ser muito menor com esparsidade |
| **Melhor cenário de uso** | Sistemas pequenos/médios, densos, ou quando A é reutilizada com vários b (via LU) | Sistemas grandes e esparsos |
| **Garantia de solução** | Sempre obtém solução (se A for não-singular) | Depende de condições de convergência (raio espectral < 1) |
| **Uso de memória** | Pode ser alto (fenômeno de fill-in em matrizes esparsas) | Geralmente menor, especialmente aproveitando esparsidade |

---

## 7. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Método "teoricamente correto" mas inviável na prática | Regra de Cramer — O(n!), proibitivo |
| Resolver Ax=b para vários b's, mesmo A | Fatoração LU — fatorar uma vez, resolver várias vezes |
| Método aplicável só a matrizes simétricas positivas definidas | Fatoração de Cholesky |
| Pivô pequeno mas não-zero | Ainda exige pivoteamento — evita amplificação de erro |
| Usa só valores da iteração anterior | Jacobi |
| Usa valores já atualizados na mesma iteração | Gauss-Seidel (geralmente converge mais rápido) |
| Fator de relaxação ω para acelerar convergência | SOR (ω=1 vira Gauss-Seidel) |
| Condição necessária e suficiente de convergência | Raio espectral da matriz de iteração < 1 |
| Condição só suficiente, não necessária | Dominância diagonal estrita |
| "Se não é diagonalmente dominante, não converge" | FALSO — pode convergir mesmo assim |
| Pequenas mudanças em b geram grandes mudanças em x | Matriz mal condicionada (número de condição alto) |
| Sistema sem solução única, determinante = 0 | Matriz singular (diferente de mal condicionada) |
| Sistema grande e esparso | Preferir métodos iterativos |

---

## 8. Aplicação Profissional

- **Simulações de engenharia (elementos finitos, fluidodinâmica):** geram sistemas lineares muito grandes e esparsos — métodos iterativos (e variantes mais avançadas, como Gradiente Conjugado e GMRES) são padrão nesse contexto.
- **Otimização e Machine Learning:** métodos como regressão linear (mínimos quadrados) e treinamento de certos modelos recaem em sistemas lineares; a fatoração LU/Cholesky é usada internamente em várias bibliotecas numéricas (NumPy, SciPy, LAPACK).
- **Computação gráfica e simulação física em jogos:** sistemas lineares para simulação de física (colisões, dinâmica de corpos rígidos), frequentemente resolvidos com métodos iterativos por questões de desempenho em tempo real.
- **Análise de circuitos elétricos:** leis de Kirchhoff geram sistemas lineares esparsos, resolvidos numericamente em softwares de simulação (SPICE e similares).
- Na prática profissional, a escolha entre método direto e iterativo raramente é feita "na mão" — bibliotecas numéricas (LAPACK, SciPy, Eigen) já implementam essas rotinas de forma altamente otimizada; o papel do profissional costuma ser **escolher a rotina/parâmetro certo** (ex.: tolerância de convergência, se a matriz é esparsa o suficiente para justificar um solver iterativo) mais do que implementar o algoritmo do zero.

---

## 9. Perguntas típicas de prova (para se testar)

1. Por que a Regra de Cramer, apesar de matematicamente correta, não é usada na prática para resolver sistemas lineares de porte real?
2. Explique a vantagem da fatoração LU em relação à eliminação de Gauss quando é necessário resolver Ax=b para múltiplos vetores b, com a mesma matriz A.
3. Qual a diferença entre o método de Jacobi e o método de Gauss-Seidel? Por que Gauss-Seidel costuma convergir mais rápido?
4. A dominância diagonal estrita é condição necessária ou apenas suficiente para a convergência de Jacobi/Gauss-Seidel? Justifique.
5. Qual a diferença entre uma matriz singular e uma matriz mal condicionada? Por que um sistema mal condicionado pode gerar erros grandes mesmo com um algoritmo numericamente correto?
6. Em que cenários métodos iterativos são preferíveis a métodos diretos, e por quê?
