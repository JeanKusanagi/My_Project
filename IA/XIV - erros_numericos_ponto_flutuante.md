# Erros Numéricos, Aritmética de Ponto Flutuante e Análise de Erros
## Conceitos Fundamentais de Cálculo Numérico — Material de Estudo

---

## 1. Conceito Central

Todo cálculo numérico realizado em um computador está sujeito a **erros inevitáveis**, porque computadores representam números reais com **precisão finita** e porque muitos métodos numéricos são, por natureza, **aproximações** de processos matemáticos ideais (infinitos ou contínuos).

> **Definição de prova:** "Análise de erros é o estudo sistemático de **quanto**, **por que** e **como** os erros surgem e se propagam ao longo de um cálculo numérico, com o objetivo de garantir que o resultado final seja **confiável dentro de uma margem conhecida**."

⚠️ **Pegadinha clássica de prova:** achar que "erro numérico" é sinônimo de "erro de programação" (bug). Erros numéricos são **inerentes** ao processo de representar números reais em máquinas com memória finita e de aproximar processos matemáticos — eles existem **mesmo em um programa perfeitamente correto**.

---

## 2. Fontes de Erro (classificação fundamental)

| Tipo de erro | Definição | Exemplo |
|---|---|---|
| **Erro de modelagem** | Diferença entre o modelo matemático usado e a realidade física/fenômeno modelado | Simplificar um sistema físico ignorando o atrito |
| **Erro de truncamento** | Vem de **aproximar um processo infinito/contínuo por um processo finito** | Usar apenas os primeiros termos de uma série de Taylor infinita; aproximar uma derivada por diferenças finitas |
| **Erro de arredondamento (round-off)** | Vem da **representação finita** de números reais na memória do computador (ponto flutuante) | 0.1 não pode ser representado exatamente em binário |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a unidade):** confundir **erro de truncamento** com **erro de arredondamento**.
- O **erro de truncamento** é um erro **do método matemático/algoritmo escolhido** — existiria mesmo em uma máquina hipotética com precisão infinita, porque a aproximação em si (ex.: parar uma série infinita em um número finito de termos) já introduz erro.
- O **erro de arredondamento** é um erro **da representação numérica no hardware** — existe mesmo que o método matemático usado seja exato, simplesmente porque o computador não consegue armazenar infinitas casas decimais/binárias.

⚠️ **Pegadinha número 2:** achar que aumentar a precisão da máquina (ex.: usar `double` em vez de `float`) **resolve todos os problemas numéricos**. Isso reduz o erro de **arredondamento**, mas **não tem nenhum efeito sobre o erro de truncamento** (que depende do método escolhido, ex.: quantos termos de uma série são usados) nem sobre problemas de **mal condicionamento** (ver seção 7).

---

## 3. Erro Absoluto e Erro Relativo

| Tipo | Fórmula | Quando é mais informativo |
|---|---|---|
| **Erro absoluto** | \|valor exato − valor aproximado\| | Quando a escala/magnitude da grandeza é conhecida e fixa |
| **Erro relativo** | Erro absoluto / \|valor exato\| | Quando se quer comparar a "qualidade" do erro **independente da escala** da grandeza |

⚠️ **Pegadinha número 1 (muito cobrada):** um **erro absoluto pequeno não implica necessariamente boa precisão**, e vice-versa. Um erro absoluto de 1 é **irrelevante** ao medir a distância entre cidades (em km), mas é **catastrófico** ao medir a dosagem de um medicamento (em mg). Por isso, o **erro relativo** costuma ser a métrica mais significativa para comparar a qualidade de aproximações entre contextos diferentes.

---

## 4. Representação de Ponto Flutuante (Padrão IEEE 754)

### 4.1 Estrutura básica
- Um número em ponto flutuante é representado, de forma simplificada, como: **±(1.mantissa) × 2^expoente**
- Composto por três partes: **bit de sinal**, **expoente** (deslocado por um viés/bias) e **mantissa** (também chamada de significando).

| Formato | Bits totais | Bits de mantissa | Precisão decimal aproximada |
|---|---|---|---|
| **Precisão simples (float, 32 bits)** | 32 | 23 | ~7 dígitos decimais |
| **Precisão dupla (double, 64 bits)** | 64 | 52 | ~15-16 dígitos decimais |

### 4.2 Por que nem todo número decimal é representável exatamente
- Assim como 1/3 não tem representação decimal finita exata, muitos números que têm representação decimal **finita e simples** (como 0,1) **não têm representação binária finita exata** — porque 0,1 em binário é uma **dízima periódica**.

⚠️ **Pegadinha número 1 (o exemplo mais clássico de toda a disciplina):** o famoso caso de **0.1 + 0.2 ≠ 0.3** exatamente, ao testar em ponto flutuante em qualquer linguagem de programação. Isso **não é um bug** da linguagem — é uma consequência direta e esperada da representação binária de ponto flutuante, que **não consegue armazenar 0.1 e 0.2 de forma exata**, apenas aproximações muito próximas.

### 4.3 Épsilon de Máquina (Machine Epsilon)
- É o **menor número positivo ε** tal que, em aritmética de ponto flutuante, **1 + ε ≠ 1** (ou seja, a menor "diferença perceptível" que a máquina consegue distinguir ao redor de 1.0).
- Serve como referência para o **limite de precisão relativa** da representação de ponto flutuante.

⚠️ **Pegadinha número 1 (muito cobrada):** confundir o **épsilon de máquina** com o **menor número positivo representável** pela máquina (que está relacionado ao limite de **underflow**, não ao épsilon). São conceitos **diferentes**:
- **Épsilon de máquina:** mede a **resolução/precisão relativa** perto de 1.0 (relacionado ao número de bits da mantissa).
- **Menor número positivo representável:** mede o **menor valor em módulo** que a máquina consegue representar antes de o resultado ser tratado como zero (underflow) — relacionado ao número de bits do **expoente**.

### 4.4 Overflow e Underflow
- **Overflow:** ocorre quando um número calculado é **maior** do que o maior valor representável no formato usado — geralmente resulta em "infinito" (±∞) ou erro.
- **Underflow:** ocorre quando um número calculado é **menor em módulo** do que o menor valor positivo representável — geralmente é arredondado para **zero**.

---

## 5. Cancelamento Catastrófico (Catastrophic Cancellation)

### 5.1 Definição
- Ocorre quando se **subtraem dois números muito próximos em valor**, resultando em uma **perda significativa de dígitos significativos** — o resultado pode ter muito menos precisão do que os operandos originais sugeririam.

> **Definição de prova:** "Se dois números têm, cada um, boa precisão relativa, mas são muito próximos entre si, a subtração entre eles amplifica o erro relativo do resultado, porque os dígitos significativos que 'coincidem' se cancelam, sobrando principalmente os dígitos onde já havia incerteza."

### 5.2 Exemplo clássico: fórmula de Bhaskara (equação quadrática)
- Na fórmula x = (−b ± √(b² − 4ac)) / 2a, quando **b² é muito maior que 4ac**, o termo √(b² − 4ac) fica **muito próximo de \|b\|**.
- Se o sinal escolhido na fórmula (+ ou −) faz com que se **subtraiam dois números muito próximos** (ex.: −b e √(b²−4ac) quando ambos têm o mesmo sinal e magnitude parecida), ocorre cancelamento catastrófico, perdendo precisão na raiz calculada.
- **Solução numérica padrão:** usar uma forma alternativa e matematicamente equivalente da fórmula (multiplicando pelo "conjugado") para uma das raízes, evitando a subtração de valores próximos.

⚠️ **Pegadinha número 1 (a mais cobrada desta seção):** achar que o cancelamento catastrófico é causado por **erro no método matemático**. Na verdade, as duas formas da fórmula de Bhaskara são **matematicamente equivalentes** (dão o mesmo resultado exato) — o problema é **puramente numérico**, causado pela forma como a subtração amplifica o erro de arredondamento já presente nos operandos.

### 5.3 Outro exemplo clássico: derivada numérica
- Ao aproximar uma derivada por diferenças finitas: f'(x) ≈ [f(x+h) − f(x)] / h, escolher **h muito pequeno** parece intuitivamente "mais preciso" (menor erro de truncamento), mas gera f(x+h) muito próximo de f(x), causando **cancelamento catastrófico** na subtração e **aumentando o erro de arredondamento**.

⚠️ **Pegadinha número 2:** esse é o exemplo clássico do **trade-off entre erro de truncamento e erro de arredondamento** — diminuir h reduz o erro de truncamento, mas **aumenta** o erro de arredondamento (por cancelamento catastrófico); existe um **h ótimo intermediário** que minimiza o erro total, não o menor h possível.

---

## 6. Propagação de Erros

- Em uma sequência de operações aritméticas, o erro presente em um valor **se propaga** (e pode se amplificar ou se atenuar) através de cada operação subsequente.
- Operações de **multiplicação e divisão** tendem a propagar o **erro relativo** de forma relativamente controlada (soma-se aproximadamente os erros relativos).
- Operações de **subtração entre números próximos** são as que mais amplificam o erro relativo (ver cancelamento catastrófico).

⚠️ **Pegadinha:** em uma sequência longa de cálculos, o erro de arredondamento de cada operação individual pode ser pequeno, mas a **soma acumulada** desses pequenos erros ao longo de milhares/milhões de operações pode se tornar **significativa** — especialmente relevante em simulações numéricas de longa duração.

---

## 7. Estabilidade do Algoritmo vs. Condicionamento do Problema (distinção crucial, muito cobrada)

Esses dois conceitos são frequentemente confundidos, mas são **independentes**:

| Conceito | O que descreve | Depende de... |
|---|---|---|
| **Condicionamento do problema** | O quanto a **solução exata** de um problema é sensível a pequenas perturbações nos **dados de entrada** | Da natureza matemática do próprio problema (ex.: número de condição de uma matriz — ver material de Sistemas Lineares) |
| **Estabilidade do algoritmo** | O quanto os **erros de arredondamento introduzidos durante a execução** do algoritmo são amplificados ao longo do cálculo | Da forma como o algoritmo é implementado/estruturado |

⚠️ **Pegadinha número 1 (a mais cobrada desta seção, e da unidade inteira):** tratar "problema mal condicionado" e "algoritmo instável" como a mesma coisa. É possível ter:
- Um **problema bem condicionado**, resolvido por um **algoritmo numericamente instável**, gerando um resultado ruim (nesse caso, **trocar o algoritmo** resolve o problema).
- Um **problema mal condicionado**, resolvido pelo **melhor algoritmo estável possível**, ainda gerando resultado sensível a pequenas perturbações (nesse caso, **nenhum algoritmo resolve** — a sensibilidade é inerente ao problema, não ao método).

⚠️ **Pegadinha número 2:** por isso, ao observar um resultado numérico ruim, é essencial **diagnosticar a causa correta** antes de "trocar de algoritmo" — se o problema for de condicionamento, trocar o algoritmo **não ajuda**; é preciso reformular o problema ou aceitar a sensibilidade inerente.

---

## 8. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Erro por aproximar série infinita/processo contínuo | Erro de truncamento (do método) |
| Erro por representação finita de números no computador | Erro de arredondamento (do hardware) |
| Aumentar precisão (float → double) resolve tudo? | Não — reduz arredondamento, mas não afeta truncamento nem mal condicionamento |
| 0.1 + 0.2 ≠ 0.3 em ponto flutuante | Representação binária finita não armazena 0.1 exatamente — não é bug |
| Menor ε tal que 1+ε ≠ 1 | Épsilon de máquina (não confundir com menor número representável) |
| Resultado maior que o representável | Overflow |
| Resultado menor em módulo que o representável | Underflow (arredondado para zero) |
| Subtrair dois números muito próximos | Cancelamento catastrófico — perde dígitos significativos |
| h muito pequeno em derivada numérica | Reduz truncamento, mas aumenta arredondamento (cancelamento catastrófico) — existe h ótimo |
| Resultado ruim: problema do algoritmo ou do problema em si? | Verificar separadamente: estabilidade do algoritmo x condicionamento do problema |
| Problema mal condicionado + algoritmo estável | Resultado ainda pode ser ruim — sensibilidade é inerente ao problema |
| Erro absoluto pequeno = boa precisão? | Não necessariamente — depende da escala; erro relativo é mais informativo |

---

## 9. Aplicação Profissional

- **Engenharia e simulações científicas:** escolha cuidadosa de algoritmos numericamente estáveis é essencial em simulações de longa duração (ex.: previsão do tempo, dinâmica de fluidos), onde pequenos erros acumulados podem invalidar completamente o resultado.
- **Sistemas financeiros:** cálculos monetários geralmente **evitam ponto flutuante binário** (usando tipos de dados decimais/inteiros em centavos) justamente para evitar erros de arredondamento como o de 0.1 + 0.2, que seriam inaceitáveis em transações financeiras.
- **Machine Learning:** operações em lote (batch) com muitas somas/multiplicações (ex.: em redes neurais profundas) podem acumular erro de arredondamento; técnicas como **treinamento de precisão mista (mixed precision)** equilibram desempenho computacional e estabilidade numérica.
- **Bibliotecas numéricas profissionais** (LAPACK, BLAS, NumPy) já implementam versões numericamente estáveis de algoritmos clássicos (ex.: cálculo de variância, resolução de sistemas lineares) justamente para evitar armadilhas como cancelamento catastrófico — reimplementar "na unha" fórmulas matemáticas de livro-texto sem cuidado numérico é uma fonte comum de bugs sutis em produção.
- Na prática profissional, **debugar um resultado numérico "estranho"** exige primeiro diagnosticar se a causa é erro de implementação, instabilidade do algoritmo ou mal condicionamento do problema — tratar todos os casos como "bug de código" é um erro recorrente de quem não teve formação em análise numérica.

---

## 10. Perguntas típicas de prova (para se testar)

1. Qual a diferença entre erro de truncamento e erro de arredondamento? Dê um exemplo de cada.
2. Por que 0.1 + 0.2 não resulta exatamente em 0.3 quando calculado em ponto flutuante? Isso é um bug da linguagem de programação?
3. O que é cancelamento catastrófico? Explique com o exemplo da fórmula de Bhaskara ou da derivada numérica por diferenças finitas.
4. Qual a diferença entre épsilon de máquina e o menor número positivo representável por um sistema de ponto flutuante?
5. Explique a diferença entre "condicionamento do problema" e "estabilidade do algoritmo". Por que um problema mal condicionado pode gerar erro grande mesmo com o melhor algoritmo possível?
6. Por que, ao aproximar uma derivada numericamente, diminuir o valor de h não leva a uma precisão cada vez melhor de forma indefinida?
