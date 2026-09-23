# SIMULADO — Erros Numéricos, Aritmética de Ponto Flutuante e Análise de Erros
### Erro absoluto e relativo, truncamento e arredondamento, representação IEEE 754, cancelamento catastrófico, propagação de erros, estabilidade e condicionamento

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas clássicas de análise numérica.

---

**1.** O **erro absoluto** de uma aproximação x̃ em relação ao valor exato x é definido como:

a) |x̃ / x|<br>
b) |x − x̃|<br>
c) x + x̃<br>
d) (x − x̃) / x̃, sempre multiplicado por 100

> **Gabarito: b.** O erro absoluto é simplesmente a diferença, em módulo, entre o valor exato e o valor aproximado: Ea = |x − x̃|.

---

**2.** O **erro relativo** de uma aproximação x̃ em relação ao valor exato x (com x ≠ 0) é definido como:

a) |x − x̃|<br>
b) |x − x̃| / |x|<br>
c) x · x̃<br>
d) |x| + |x̃|

> **Gabarito: b.** O erro relativo normaliza o erro absoluto pela magnitude do valor exato, permitindo comparar a qualidade de aproximações em escalas diferentes — algo que o erro absoluto isolado não permite.

---

**3.** **(Pegadinha)** Considere duas aproximações: x = 1000 aproximado por x̃ = 999 (erro absoluto = 1), e y = 2 aproximado por ỹ = 1 (erro absoluto = 1). Sobre a qualidade dessas duas aproximações, é correto afirmar que:

a) As duas aproximações têm exatamente a mesma qualidade, pois possuem o mesmo erro absoluto<br>
b) Apesar de terem o mesmo erro absoluto, a aproximação de x é consideravelmente melhor em termos relativos (erro relativo de 0,1%) do que a aproximação de y (erro relativo de 50%) — o erro absoluto isolado pode enganar sobre a real qualidade de uma aproximação<br>
c) A aproximação de y é sempre melhor, pois o número é menor<br>
d) Erro absoluto e erro relativo são sempre proporcionais entre si, então o resultado seria o mesmo

> **Gabarito: b.** Pegadinha clássica: comparar apenas erros absolutos pode ser enganoso — é o erro relativo que revela o real impacto proporcional do erro em relação à grandeza do valor.

---

**4.** O **erro de truncamento** (ou erro de discretização) em métodos numéricos surge principalmente de:

a) Limitações da representação finita de números em ponto flutuante no computador<br>
b) Aproximar um processo matemático infinito (ou contínuo) por um processo finito (ou discreto) — por exemplo, truncar uma série infinita após um número finito de termos, ou aproximar uma derivada por diferenças finitas<br>
c) Erros de digitação do programador<br>
d) Falhas de hardware do processador

> **Gabarito: b.** O erro de truncamento é inerente ao método matemático empregado (não ao computador), surgindo da substituição de um processo exato/infinito por uma aproximação finita — como truncar a série de Taylor em um número finito de termos.

---

**5.** **(Pegadinha)** O **erro de arredondamento** (rounding error), diferente do erro de truncamento, é causado principalmente por:

a) A escolha de um método numérico inadequado para o problema<br>
b) A representação finita de números reais em um sistema de ponto flutuante com precisão limitada, o que obriga a arredondar (ou truncar) valores que não podem ser representados exatamente com o número finito de bits disponível<br>
c) A aproximação de uma função contínua por uma discreta<br>
d) A escolha de um passo de discretização muito grande

> **Gabarito: b.** Pegadinha: é comum confundir erro de truncamento (do método matemático) com erro de arredondamento (da representação finita em máquina) — este último surge da própria limitação de bits do sistema de ponto flutuante, independentemente do método numérico escolhido.

---

**6.** No padrão **IEEE 754** de ponto flutuante, um número é tipicamente representado por três componentes principais:

a) Numerador, denominador e resto<br>
b) Sinal, expoente (exponent) e mantissa (significando/fração)<br>
c) Base, altura e volume<br>
d) Real, imaginário e módulo

> **Gabarito: b.** A representação em ponto flutuante segundo o IEEE 754 organiza o número em um bit de sinal, um campo de expoente e um campo de mantissa (significando), de forma análoga à notação científica binária.

---

**7.** **(Pegadinha)** O número decimal 0,1 pode ser representado **exatamente** em ponto flutuante binário (double precision, IEEE 754)?

a) Sim, todo número decimal finito tem representação binária finita exata<br>
b) Não — 0,1 não possui representação binária finita exata (é uma dízima periódica em base 2), sendo armazenado apenas como uma aproximação, o que pode gerar resultados aparentemente "estranhos" em comparações de igualdade envolvendo esse valor<br>
c) Sim, pois 0,1 é um número racional simples<br>
d) Não, mas apenas porque 0,1 é um número negativo

> **Gabarito: b.** Pegadinha muito comum (e frequentemente motivo de "bugs" para iniciantes): frações decimais simples como 0,1 ou 0,3 não têm representação binária finita exata, o que explica por que comparações como `0.1 + 0.2 == 0.3` costumam retornar falso em linguagens de programação.

---

**8.** O **épsilon de máquina** (machine epsilon) é definido, de forma geral, como:

a) O maior número representável no sistema de ponto flutuante<br>
b) O menor número positivo ε tal que, na aritmética de ponto flutuante do sistema, 1 + ε é representado como um valor diferente de 1 (ou seja, uma medida da precisão/resolução relativa do sistema)<br>
c) O número zero, representado exatamente<br>
d) A quantidade total de bits usados na mantissa

> **Gabarito: b.** O épsilon de máquina caracteriza a menor diferença relativa "perceptível" pelo sistema de ponto flutuante — é uma medida fundamental da precisão da aritmética utilizada.

---

**9.** **(Pegadinha)** Sobre a associatividade da adição em aritmética de ponto flutuante, é correto afirmar que:

a) A adição de ponto flutuante é sempre associativa, exatamente como na aritmética real exata: (a + b) + c = a + (b + c) sempre, sem exceções<br>
b) A adição de ponto flutuante **não é**, em geral, associativa: devido a erros de arredondamento em cada operação, (a + b) + c pode produzir um resultado numericamente diferente de a + (b + c), especialmente quando os valores envolvidos têm magnitudes muito diferentes<br>
c) A associatividade só falha na subtração, nunca na adição<br>
d) A ordem das operações nunca afeta o resultado em ponto flutuante, desde que os números sejam positivos

> **Gabarito: b.** Pegadinha importante e prática: diferente da aritmética real, a aritmética de ponto flutuante **perde** propriedades como associatividade exata, devido ao arredondamento intermediário — isso tem implicações reais em computação numérica (ex.: paralelização de somas pode gerar resultados ligeiramente diferentes).

---

**10.** O fenômeno de **cancelamento catastrófico** (catastrophic cancellation) ocorre tipicamente quando:

a) Se somam dois números de magnitudes muito diferentes<br>
b) Se subtraem dois números muito próximos em valor (magnitude semelhante), resultando na perda de dígitos significativos, já que os erros de arredondamento presentes nos dois números passam a dominar proporcionalmente o resultado, muito menor em módulo<br>
c) Se multiplicam dois números muito grandes<br>
d) Se divide um número por zero

> **Gabarito: b.** Pegadinha frequente: cancelamento catastrófico ocorre na **subtração de números próximos**, não na soma — quando os valores são quase iguais, o resultado da subtração é pequeno, mas carrega proporcionalmente todo o erro de arredondamento já presente nos operandos originais, ampliando o erro relativo.

---

**11.** **(Pegadinha)** Um exemplo clássico de cancelamento catastrófico ocorre no cálculo das raízes de uma equação quadrática, ax² + bx + c = 0, pela fórmula de Bhaskara, quando:

a) O coeficiente a é igual a zero<br>
b) O valor de b² é muito maior, em módulo, que 4ac, de modo que √(b² − 4ac) fica muito próximo de |b|, fazendo com que, ao calcular −b + √(b²−4ac) (ou −b − √(b²−4ac), dependendo do sinal de b), ocorra subtração de valores próximos, perdendo precisão — nesses casos, utiliza-se uma forma alternativa da fórmula para evitar o problema<br>
c) O discriminante (b² − 4ac) é negativo, gerando raízes complexas<br>
d) Os coeficientes a, b e c são todos números inteiros

> **Gabarito: b.** Esse é um exemplo canônico ensinado em cursos de cálculo numérico: quando b é muito maior (em módulo) que 4ac, uma das duas formas da fórmula de Bhaskara sofre cancelamento catastrófico, exigindo o uso de uma forma algebricamente equivalente (multiplicando pelo conjugado) para preservar precisão.

---

**12.** O que caracteriza o fenômeno de **overflow** em aritmética de ponto flutuante?

a) O resultado de uma operação é menor, em módulo, que o menor número positivo representável, sendo aproximado para zero<br>
b) O resultado de uma operação excede, em módulo, o maior número representável no sistema de ponto flutuante, geralmente resultando em um valor especial como infinito (Inf) ou causando erro, dependendo da linguagem/sistema<br>
c) O resultado de uma operação é sempre exatamente igual a zero<br>
d) O overflow ocorre exclusivamente em operações de subtração

> **Gabarito: b.** Overflow ocorre quando a magnitude do resultado ultrapassa a capacidade de representação do sistema, geralmente gerando um valor especial (como +Inf ou -Inf no padrão IEEE 754) ou um erro, dependendo da implementação.

---

**13.** **(Pegadinha)** O que caracteriza o fenômeno de **underflow** em aritmética de ponto flutuante?

a) É sinônimo exato de overflow, apenas com nome diferente<br>
b) Ocorre quando o resultado de uma operação é diferente de zero, mas tão pequeno em módulo que não pode ser representado com precisão no sistema, podendo ser arredondado para zero ou para um número subnormal — o oposto do overflow, que trata de valores excessivamente grandes<br>
c) Ocorre apenas quando se divide um número por zero<br>
d) É um erro exclusivo de linguagens de programação antigas, já eliminado nos sistemas modernos

> **Gabarito: b.** Pegadinha: overflow (números grandes demais) e underflow (números pequenos demais, próximos de zero) são fenômenos opostos, ambos relacionados aos limites de representação do sistema de ponto flutuante — nenhum dos dois foi "eliminado" pelos sistemas modernos, apenas mitigado por representações mais amplas (como double precision) e números subnormais.

---

**14.** A **propagação de erros** em uma sequência de cálculos numéricos refere-se a:

a) O fato de que erros cometidos em etapas iniciais de um cálculo (por arredondamento ou truncamento) podem se acumular e/ou se amplificar ao longo das operações subsequentes, afetando o resultado final<br>
b) A eliminação automática de qualquer erro ao final de um cálculo longo<br>
c) Um fenômeno que ocorre apenas em cálculos manuais, nunca em cálculos computacionais<br>
d) A garantia de que erros sempre se cancelam mutuamente ao longo de uma sequência de operações

> **Gabarito: a.** A propagação de erros é uma preocupação central em análise numérica: erros iniciais (de entrada, arredondamento ou truncamento) podem se propagar — e, dependendo da natureza das operações, se amplificar — ao longo de um algoritmo, afetando significativamente o resultado final.

---

**15.** **(Pegadinha)** Um algoritmo é dito **numericamente instável** quando:

a) Ele é sempre lento em termos de tempo de execução<br>
b) Pequenos erros de arredondamento cometidos durante sua execução são amplificados de forma significativa ao longo dos cálculos, produzindo um resultado final com erro muito maior do que seria razoável esperar, mesmo quando o problema em si é bem condicionado<br>
c) Ele nunca converge para nenhum resultado<br>
d) Ele é sinônimo de "problema mal condicionado" — instabilidade do algoritmo e mau condicionamento do problema são exatamente a mesma coisa

> **Gabarito: b.** Pegadinha: instabilidade numérica é uma propriedade do **algoritmo** (como ele processa e propaga erros), diferente do condicionamento, que é uma propriedade do **problema** em si (quão sensível a solução exata é a perturbações nos dados) — um problema bem condicionado ainda pode ser resolvido de forma numericamente instável por um algoritmo mal projetado.

---

**16.** Sobre a diferença entre **estabilidade de um algoritmo** e **condicionamento de um problema**, é correto afirmar que:

a) São exatamente o mesmo conceito, usados como sinônimos<br>
b) O condicionamento é uma propriedade intrínseca do problema (independe de como ele é resolvido), enquanto a estabilidade é uma propriedade do algoritmo/método numérico utilizado para resolvê-lo — um problema bem condicionado pode ser resolvido de forma instável, e um algoritmo estável pode não "consertar" um problema intrinsecamente mal condicionado<br>
c) Todo problema mal condicionado é necessariamente resolvido por um algoritmo instável, em qualquer caso<br>
d) Estabilidade só se aplica a sistemas lineares, nunca a outros tipos de problemas numéricos

> **Gabarito: b.** Essa distinção conceitual (problema vs. método/algoritmo) é fundamental em análise numérica: condicionamento e estabilidade são independentes, ainda que relacionados — um bom algoritmo (estável) não transforma magicamente um problema mal condicionado em um bem condicionado.

---

**17.** **(Pegadinha)** Um sistema/problema bem condicionado, resolvido por um algoritmo numericamente instável, tende a produzir:

a) Sempre um resultado altamente preciso, pois o bom condicionamento do problema "compensa" qualquer instabilidade do algoritmo<br>
b) Possivelmente um resultado com erro maior do que o esperado, pois a instabilidade do algoritmo pode amplificar erros de arredondamento mesmo quando o problema, em si, não é sensível a pequenas perturbações nos dados de entrada<br>
c) Um resultado exato, pois problemas bem condicionados nunca sofrem qualquer tipo de erro numérico<br>
d) Um erro apenas se o problema também for mal condicionado simultaneamente

> **Gabarito: b.** Pegadinha: bom condicionamento do problema não "protege" contra um algoritmo mal projetado — a instabilidade do método pode, por si só, introduzir e amplificar erros significativos, mesmo em problemas teoricamente bem comportados.

---

**18.** Quantos **algarismos significativos** possui o número 0,003450, considerando as convenções usuais de algarismos significativos?

a) 7, contando todos os dígitos, incluindo os zeros à esquerda<br>
b) 4, considerando que os zeros à esquerda (antes do primeiro dígito não nulo) não são significativos, mas o zero à direita (após os demais dígitos significativos, indicando precisão até essa casa) é significativo — restando os algarismos 3, 4, 5 e 0<br>
c) 6, contando todos os dígitos após a vírgula, incluindo os zeros à esquerda<br>
d) 1, apenas o primeiro dígito não nulo

> **Gabarito: b.** Pegadinha comum em contagem de algarismos significativos: zeros à esquerda (0,00...) servem apenas para posicionar a vírgula decimal e não são significativos; já o zero à direita em 0,003450 é significativo, pois indica precisão até essa casa decimal — os algarismos significativos são 3, 4, 5 e 0, totalizando 4.

---

**19.** A **precisão dupla** (double precision) no padrão IEEE 754 utiliza, tipicamente:

a) 8 bits no total<br>
b) 32 bits no total<br>
c) 64 bits no total, distribuídos entre sinal, expoente (11 bits) e mantissa (52 bits)<br>
d) 128 bits no total, sempre

> **Gabarito: c.** O formato double precision do IEEE 754 usa 64 bits: 1 bit de sinal, 11 bits de expoente e 52 bits de mantissa/fração, oferecendo maior precisão e alcance do que o formato single precision (32 bits).

---

**20.** **(Pegadinha)** Sobre a diferença de precisão entre os formatos *single precision* (32 bits) e *double precision* (64 bits) do IEEE 754, é correto afirmar que:

a) Ambos oferecem exatamente a mesma precisão, diferindo apenas no espaço de armazenamento ocupado<br>
b) Double precision oferece maior precisão (mais bits de mantissa) e maior alcance (mais bits de expoente) do que single precision, à custa de maior consumo de memória e, potencialmente, maior custo computacional<br>
c) Single precision é sempre mais precisa que double precision, apesar de usar menos bits<br>
d) A escolha entre os dois formatos nunca afeta o resultado de cálculos numéricos

> **Gabarito: b.** Pegadinha: mais bits de mantissa e expoente significam maior precisão e alcance — a escolha entre os formatos é um trade-off real entre precisão numérica, uso de memória e desempenho computacional.

---

**21.** **(Pegadinha)** Comparar dois números de ponto flutuante usando o operador de igualdade exata (`==`), como em `a == b`, após uma sequência de operações aritméticas, é geralmente considerado:

a) Uma prática segura e recomendada em qualquer situação, pois computadores são precisos<br>
b) Uma prática arriscada, pois erros de arredondamento acumulados podem fazer com que dois valores matematicamente iguais (em teoria) não sejam representados de forma idêntica em ponto flutuante — recomenda-se, em vez disso, verificar se |a − b| é menor que uma tolerância pequena (epsilon)<br>
c) Irrelevante, pois ponto flutuante nunca introduz diferenças em comparações de igualdade<br>
d) Uma prática recomendada apenas para números inteiros representados em ponto flutuante, nunca para números fracionários

> **Gabarito: b.** Pegadinha prática muito comum em programação: comparar floats com igualdade exata é uma armadilha clássica, devido a erros de arredondamento acumulados — a prática recomendada é comparar a diferença absoluta (ou relativa) com uma tolerância adequada.

---

**22.** O que é um **número subnormal** (ou denormalizado) em ponto flutuante IEEE 754?

a) Um número maior que o maior valor representável no sistema<br>
b) Um número muito próximo de zero, representado com uma forma especial (expoente mínimo fixo e mantissa sem o "1 implícito"), que permite representar valores menores do que o menor número normal, embora com precisão reduzida — servindo como uma transição gradual até o zero, em vez de um "salto" abrupto (underflow abrupto)<br>
c) Um sinônimo exato de NaN (Not a Number)<br>
d) Um número exclusivo de sistemas de precisão simples, inexistente em precisão dupla

> **Gabarito: b.** Números subnormais preenchem a lacuna entre o menor número normal representável e o zero, permitindo um "underflow gradual" em vez de um salto abrupto direto para zero, embora com menor precisão relativa do que os números normais.

---

**23.** **(Pegadinha)** O valor especial **NaN** (Not a Number), previsto no padrão IEEE 754, surge tipicamente de operações como:

a) Qualquer soma entre dois números positivos<br>
b) Operações matematicamente indefinidas, como 0/0 ou ∞ − ∞, sendo usado para sinalizar que o resultado não é um número válido, propagando essa indefinição pelas operações subsequentes que o envolvam<br>
c) Divisão de qualquer número por 2<br>
d) Multiplicação de dois números negativos

> **Gabarito: b.** Pegadinha: NaN não representa "erro genérico" ou "infinito" — ele sinaliza especificamente resultados matematicamente indefinidos, como 0/0, ∞−∞ ou √(número negativo) em aritmética real, e tem a propriedade de que qualquer operação envolvendo NaN também resulta em NaN.

---

**24.** **(Pegadinha)** Sobre a comparação `NaN == NaN` em um sistema que segue o padrão IEEE 754, é correto afirmar que:

a) O resultado é sempre verdadeiro (True), pois NaN é igual a si mesmo, como qualquer outro valor<br>
b) O resultado é, por definição do padrão IEEE 754, falso (False) — NaN não é considerado igual a nenhum valor, nem mesmo a outro NaN, sendo essa uma peculiaridade proposital da especificação, usada inclusive como forma de detectar a presença de NaN em certos algoritmos<br>
c) O resultado gera obrigatoriamente um erro de compilação em qualquer linguagem<br>
d) O resultado depende exclusivamente do valor do bit de sinal do NaN

> **Gabarito: b.** Pegadinha bastante conhecida entre programadores: por definição do padrão IEEE 754, NaN nunca é considerado igual a nada, nem a si mesmo — esse comportamento incomum é, inclusive, aproveitado como teste padrão para detectar valores NaN em código (`x != x` sendo verdadeiro apenas para NaN).

---

**25.** Em relação ao erro de truncamento em séries infinitas (como a série de Taylor), ao aproximar uma função por um número finito de termos, é correto afirmar que:

a) O erro de truncamento é sempre zero, independentemente do número de termos utilizados<br>
b) O erro de truncamento tende a diminuir conforme se aumenta o número de termos considerados na aproximação (dentro da região de convergência da série), mas nunca é eliminado a menos que se use a série completa (infinita)<br>
c) O erro de truncamento aumenta sempre que se adicionam mais termos à aproximação<br>
d) O erro de truncamento é idêntico ao erro de arredondamento, sendo termos sinônimos

> **Gabarito: b.** Ao truncar uma série infinita convergente em um número finito de termos, o erro de truncamento tipicamente diminui à medida que mais termos são incluídos, mas subsiste enquanto a soma não for infinita — sendo, em geral, um erro diferente e de origem distinta do erro de arredondamento.

---

**26.** **(Pegadinha)** Um estudante afirma: "Quanto mais termos eu incluir em uma aproximação por série de Taylor, sempre menor será o erro total (considerando erro de truncamento e de arredondamento juntos), sem exceção." Essa afirmação está:

a) Correta, pois mais termos sempre significam mais precisão total, sem limite<br>
b) Incorreta — embora aumentar o número de termos geralmente reduza o erro de truncamento, adicionar mais termos também envolve mais operações aritméticas, o que pode aumentar o erro de arredondamento acumulado; em algum ponto, o erro total pode parar de diminuir ou até aumentar, havendo um número "ótimo" de termos além do qual a precisão não melhora (ou piora)<br>
c) Correta, mas apenas para funções polinomiais<br>
d) Incorreta, mas apenas porque a série de Taylor nunca converge na prática

> **Gabarito: b.** Pegadinha importante e prática: existe um trade-off entre erro de truncamento (que diminui com mais termos) e erro de arredondamento acumulado (que tende a aumentar com mais operações) — em algum ponto, adicionar mais termos deixa de compensar, podendo até piorar a precisão total do resultado.

---

**27.** **(Pegadinha)** Ao somar uma longa sequência de números de ponto flutuante, a ordem em que a soma é realizada:

a) Nunca afeta o resultado, pois adição é sempre comutativa e associativa em qualquer sistema numérico<br>
b) Pode afetar o resultado numérico final, devido a erros de arredondamento acumulados de forma diferente conforme a ordem das operações — por isso, técnicas como a soma de Kahan (compensated summation) foram desenvolvidas para reduzir esse tipo de erro em somas de muitos termos<br>
c) Só afeta o resultado quando todos os números são negativos<br>
d) É irrelevante, pois computadores sempre corrigem automaticamente qualquer erro de ordem de operações

> **Gabarito: b.** Pegadinha: assim como discutido na questão sobre associatividade, a ordem de soma em ponto flutuante pode alterar o resultado final devido ao arredondamento em cada etapa — motivando algoritmos especializados, como a soma de Kahan, para somas numericamente mais precisas de longas sequências.

---

**28.** Sobre a relação entre **erro relativo** e **algarismos significativos corretos** de uma aproximação, é correto afirmar, de forma geral, que:

a) Não existe relação alguma entre essas duas grandezas<br>
b) Quanto menor o erro relativo de uma aproximação, tipicamente maior é o número de algarismos significativos corretos que ela possui em relação ao valor exato — essa relação é frequentemente usada como critério prático de parada em métodos iterativos, ao se buscar determinado número de casas/algarismos corretos<br>
c) Erro relativo pequeno sempre implica erro absoluto pequeno, em qualquer escala<br>
d) O número de algarismos significativos independe totalmente da precisão da aproximação

> **Gabarito: b.** Existe uma relação prática (embora não exata em todos os casos) entre a magnitude do erro relativo e o número de algarismos significativos corretos — um erro relativo da ordem de 10⁻ⁿ costuma estar associado a aproximadamente n algarismos significativos corretos, servindo de guia para critérios de parada em métodos numéricos.

---

**29.** **(Pegadinha)** Um programador afirma: "Se meu algoritmo produz um resultado numérico razoável para um conjunto pequeno de dados de teste, posso concluir que ele é numericamente estável em qualquer cenário." Essa afirmação está:

a) Correta, pois testar com poucos dados já garante estabilidade numérica geral<br>
b) Incorreta — a estabilidade numérica de um algoritmo é uma propriedade que deve ser analisada teoricamente (ou testada em uma ampla variedade de cenários, incluindo casos extremos, mal condicionados ou com magnitudes muito diferentes entre si), pois um algoritmo pode se comportar bem em casos de teste simples e ainda assim amplificar erros de forma significativa em outros cenários<br>
c) Correta, desde que os dados de teste sejam números inteiros<br>
d) Incorreta, mas apenas porque testes numéricos nunca são úteis para avaliar algoritmos

> **Gabarito: b.** Pegadinha: um bom desempenho em casos de teste simples não garante estabilidade numérica geral — problemas de instabilidade costumam se manifestar justamente em cenários específicos (números de magnitudes muito diferentes, subtrações quase canceladas, muitas iterações), que podem não estar cobertos por testes simples.

---

**30.** **(Pegadinha)** Um estudante conclui: "Como os computadores modernos utilizam dupla precisão (64 bits) por padrão em muitas linguagens, os erros de arredondamento deixaram de ser uma preocupação relevante na prática." Essa afirmação está:

a) Correta, pois dupla precisão elimina totalmente qualquer erro de arredondamento<br>
b) Incorreta — mesmo com dupla precisão, erros de arredondamento continuam existindo (apenas com magnitude menor por operação) e podem se acumular significativamente em algoritmos com muitas operações, más condicionados, ou sujeitos a fenômenos como cancelamento catastrófico, permanecendo uma preocupação central em análise numérica<br>
c) Correta, pois qualquer sistema de 64 bits é matematicamente exato<br>
d) Incorreta, mas apenas porque dupla precisão foi abandonada pelos computadores modernos

> **Gabarito: b.** Pegadinha conceitual final: maior precisão (mais bits) reduz o erro por operação individual, mas não elimina o fenômeno de arredondamento — em algoritmos longos, mal condicionados ou sujeitos a cancelamento catastrófico, os erros ainda podem se acumular de forma significativa, por isso a análise de erros continua sendo uma disciplina relevante mesmo com hardware moderno.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Os pontos mais recorrentes de pegadinha nesta prova foram: a **diferença entre erro de truncamento e erro de arredondamento** (questões 4 e 5), o **cancelamento catastrófico** (questões 10 e 11), a **distinção entre estabilidade de algoritmo e condicionamento de problema** (questões 15 a 17), e as **peculiaridades de NaN e comparação de floats** (questões 21 e 24) — vale reforçar esses pontos na correção em sala.
