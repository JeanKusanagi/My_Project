# SIMULADO — Lógica de Predicados
### Predicados, quantificadores, variáveis livres e ligadas, tradução para FOL, equivalências e validade

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas conceituais clássicas de lógica de predicados.

---

**1.** Na lógica de predicados (ou lógica de primeira ordem), um predicado pode ser entendido como:

a) Uma proposição sempre falsa
b) Uma função que associa a um ou mais indivíduos de um domínio um valor verdade (verdadeiro ou falso), a depender dos argumentos
c) Um conectivo lógico, como ∧ ou ∨
d) Um símbolo exclusivo da lógica proposicional

> **Gabarito: b.** Um predicado, como P(x) ou "É primo(x)", só assume um valor de verdade quando aplicado a indivíduos específicos do domínio — diferente de uma proposição fechada, que já tem valor de verdade definido.

---

**2.** **(Pegadinha)** A fórmula `P(x)`, isoladamente (sem quantificador e sem atribuição de valor a x), é:

a) Sempre verdadeira
b) Sempre falsa
c) Uma fórmula aberta, cujo valor de verdade depende do valor atribuído à variável livre x
d) Uma contradição lógica

> **Gabarito: c.** Pegadinha: `P(x)` sem quantificador nem interpretação para x não é nem verdadeira nem falsa em si — é uma fórmula aberta (com variável livre), diferente de uma proposição fechada.

---

**3.** O quantificador universal ∀ é lido como:

a) "Existe pelo menos um"
b) "Para todo" ou "qualquer que seja"
c) "Não existe nenhum"
d) "Exatamente um"

> **Gabarito: b.** ∀x significa "para todo x" — afirma algo sobre todos os elementos do domínio considerado.

---

**4.** O quantificador existencial ∃ é lido como:

a) "Para todo"
b) "Nenhum"
c) "Existe pelo menos um" (ou "existe algum")
d) "Sempre"

> **Gabarito: c.** ∃x afirma que pelo menos um elemento do domínio satisfaz a condição descrita.

---

**5.** **(Pegadinha)** Considere a sentença "Todo gato é um mamífero". A tradução correta em lógica de predicados, usando Gato(x) e Mamifero(x), é:

a) ∀x (Gato(x) ∧ Mamifero(x))
b) ∀x (Gato(x) → Mamifero(x))
c) ∃x (Gato(x) → Mamifero(x))
d) ∀x (Mamifero(x) → Gato(x))

> **Gabarito: b.** Pegadinha clássica: sentenças do tipo "Todo A é B" usam ∀ com **implicação** (→), não conjunção (∧). Usar ∧ com ∀ (alternativa a) tornaria a fórmula falsa em qualquer domínio com elementos que não sejam gatos, pois exigiria que TUDO no domínio fosse gato e mamífero.

---

**6.** **(Pegadinha)** Considere a sentença "Existe um gato que é preto". A tradução correta, usando Gato(x) e Preto(x), é:

a) ∃x (Gato(x) → Preto(x))
b) ∃x (Gato(x) ∧ Preto(x))
c) ∀x (Gato(x) ∧ Preto(x))
d) ∀x (Gato(x) → Preto(x))

> **Gabarito: b.** Pegadinha inversa da anterior: sentenças do tipo "Existe um A que é B" usam ∃ com **conjunção** (∧), não implicação. Usar → com ∃ (alternativa a) tornaria a fórmula trivialmente verdadeira até em domínios sem nenhum gato, bastando um único indivíduo não-gato para satisfazer o condicional.

---

**7.** Em uma variável **ligada** (bound variable), o que ocorre?

a) A variável está livre para receber qualquer valor sem influência de quantificadores
b) A variável está no escopo de um quantificador (∀ ou ∃) que a governa, deixando de ser livre
c) A variável nunca aparece em uma fórmula bem formada
d) A variável só pode aparecer em lógica proposicional, não em lógica de predicados

> **Gabarito: b.** Uma variável é dita ligada quando está sob o escopo de um quantificador que a captura; caso contrário, é livre.

---

**8.** **(Pegadinha)** Na fórmula `∀x P(x,y)`, a variável y é:

a) Ligada pelo quantificador ∀
b) Livre, pois o quantificador ∀x liga apenas a ocorrência de x, não de y
c) Indefinida e torna a fórmula malformada
d) Automaticamente igual a x

> **Gabarito: b.** Pegadinha: um quantificador liga apenas a variável explicitamente indicada (aqui, x). A variável y permanece livre, o que significa que o valor de verdade da fórmula ainda depende de uma atribuição para y.

---

**9.** Qual das alternativas expressa corretamente a negação de `∀x P(x)`?

a) ∀x ¬P(x)
b) ∃x ¬P(x)
c) ¬∃x P(x)
d) ∃x P(x)

> **Gabarito: b.** Uma das equivalências fundamentais (análogas às Leis de De Morgan para quantificadores): ¬∀x P(x) ≡ ∃x ¬P(x). Negar "para todo x, P(x)" equivale a afirmar "existe x tal que não-P(x)".

---

**10.** **(Pegadinha)** Qual das alternativas expressa corretamente a negação de `∃x P(x)`?

a) ∃x ¬P(x)
b) ∀x P(x)
c) ∀x ¬P(x)
d) ¬P(x), sem quantificador

> **Gabarito: c.** Pegadinha: muitos confundem com a alternativa "a". A equivalência correta é ¬∃x P(x) ≡ ∀x ¬P(x): negar "existe x tal que P(x)" equivale a afirmar "para todo x, não-P(x)" (ou seja, nenhum elemento satisfaz P).

---

**11.** **(Pegadinha)** Ao negar `∀x ∃y R(x,y)`, qual é o resultado correto, aplicando as regras de negação de quantificadores passo a passo?

a) ∃x ∀y ¬R(x,y)
b) ∀x ∃y ¬R(x,y)
c) ∃x ∀y R(x,y)
d) ∀x ∀y ¬R(x,y)

> **Gabarito: a.** Aplicando a regra duas vezes: ¬∀x ∃y R(x,y) ≡ ∃x ¬∃y R(x,y) ≡ ∃x ∀y ¬R(x,y). Pegadinha: é comum o aluno trocar apenas um quantificador e esquecer de inverter o segundo, ou de negar o predicado interno.

---

**12.** **(Pegadinha)** Considere as fórmulas `∀x ∃y Ama(x,y)` e `∃y ∀x Ama(x,y)`, com o domínio de pessoas e Ama(x,y) significando "x ama y". É correto afirmar que:

a) As duas fórmulas são logicamente equivalentes, podendo trocar livremente a ordem dos quantificadores
b) A primeira significa "toda pessoa ama alguém (possivelmente pessoas diferentes)", enquanto a segunda significa "existe uma pessoa específica que é amada por todo mundo" — são afirmações distintas, e a ordem dos quantificadores importa
c) As duas fórmulas são sempre falsas
d) A ordem de ∀ e ∃ nunca afeta o significado de uma fórmula

> **Gabarito: b.** Pegadinha central em lógica de predicados: a ordem entre um quantificador universal e um existencial **importa** — trocar ∀x∃y por ∃y∀x altera radicalmente o significado (de "cada um tem o seu" para "existe um único elemento que serve para todos").

---

**13.** A fórmula `∀x∀y R(x,y)` é logicamente equivalente a:

a) `∃y∃x R(x,y)`
b) `∀y∀x R(x,y)` — a ordem entre dois quantificadores do mesmo tipo (ambos universais) pode ser trocada sem alterar o significado
c) `∃x∀y R(x,y)`
d) `∀x∃y R(x,y)`

> **Gabarito: b.** Diferente do caso ∀/∃, quando os quantificadores são do mesmo tipo (ambos ∀ ou ambos ∃), a ordem pode ser trocada livremente sem alterar o valor de verdade da fórmula.

---

**14.** Qual é a diferença fundamental entre lógica proposicional e lógica de predicados?

a) A lógica de predicados não usa conectivos como ∧, ∨ e ¬
b) A lógica de predicados permite expressar a estrutura interna das proposições, com predicados, termos, variáveis e quantificadores, algo que a lógica proposicional (que trata proposições como blocos indivisíveis) não permite
c) A lógica proposicional é mais expressiva que a lógica de predicados
d) Não há diferença relevante entre elas

> **Gabarito: b.** A lógica de predicados analisa a estrutura interna das sentenças (sujeitos, predicados, quantificação), enquanto a proposicional trata cada proposição como uma unidade atômica.

---

**15.** **(Pegadinha)** Sobre a sentença "Nenhum peixe é mamífero", traduzida com Peixe(x) e Mamifero(x), qual fórmula está correta?

a) ∃x (Peixe(x) ∧ Mamifero(x))
b) ∀x (Peixe(x) → ¬Mamifero(x))
c) ∀x (Peixe(x) ∧ ¬Mamifero(x))
d) ∃x (Peixe(x) → ¬Mamifero(x))

> **Gabarito: b.** Pegadinha: "Nenhum A é B" equivale a "Todo A não é B", ou seja, ∀x(A(x) → ¬B(x)). Usar ∧ (alternativa c) exigiria que TUDO no domínio fosse peixe e não-mamífero, o que está errado.

---

**16.** Em lógica de predicados, o **domínio de discurso** (ou universo) é:

a) O conjunto de conectivos lógicos disponíveis
b) O conjunto de todos os indivíduos sobre os quais os quantificadores e predicados da fórmula se referem numa dada interpretação
c) Um sinônimo de "variável livre"
d) Exclusivo de fórmulas com quantificador existencial

> **Gabarito: b.** O domínio de discurso define o "universo" de objetos considerados na interpretação de uma fórmula — sem especificá-lo, o valor de verdade de fórmulas quantificadas fica indeterminado.

---

**17.** **(Pegadinha)** Se o domínio de discurso for o conjunto vazio (∅), o valor de verdade de `∀x P(x)` é:

a) Sempre falso, pois não há elementos para verificar
b) Verdadeiro (vacuamente verdadeiro), pois não existe nenhum contraexemplo possível em um domínio vazio
c) Indefinido, pois a lógica de predicados proíbe domínios vazios
d) Depende do predicado P, podendo variar livremente

> **Gabarito: b.** Pegadinha comum: no domínio vazio, `∀x P(x)` é considerado "vacuamente verdadeiro" (não há nenhum elemento que viole a condição). Já `∃x P(x)` seria falso nesse mesmo domínio, pois não há nenhum elemento que a satisfaça.

---

**18.** Considerando o mesmo cenário da questão anterior (domínio vazio), o valor de verdade de `∃x P(x)` é:

a) Verdadeiro, pelo mesmo motivo do caso anterior
b) Falso, pois não existe nenhum elemento no domínio que possa satisfazer P(x)
c) Indefinido
d) Depende apenas do predicado P, independentemente do domínio

> **Gabarito: b.** Em domínio vazio, uma afirmação existencial é sempre falsa, já que não há nenhum objeto para testemunhar a existência.

---

**19.** Uma fórmula é dita **válida** (ou tautológica) em lógica de predicados quando:

a) É verdadeira em pelo menos uma interpretação
b) É verdadeira em todas as interpretações possíveis, independentemente do domínio ou da atribuição de valores aos predicados
c) É falsa em todas as interpretações
d) Depende exclusivamente da opinião do avaliador

> **Gabarito: b.** Validade em lógica significa verdade em toda e qualquer interpretação (modelo) possível — não apenas em um caso particular.

---

**20.** **(Pegadinha)** Uma fórmula é dita **satisfatível** quando:

a) É verdadeira em todas as interpretações possíveis
b) Existe pelo menos uma interpretação (um modelo) na qual a fórmula é verdadeira
c) É sempre falsa, em qualquer interpretação
d) É sinônimo exato de "válida"

> **Gabarito: b.** Pegadinha: satisfatibilidade (existir ao menos um modelo que a torne verdadeira) é mais fraca que validade (ser verdadeira em TODOS os modelos) — toda fórmula válida é satisfatível, mas nem toda satisfatível é válida.

---

**21.** No que diz respeito à decidibilidade, é correto afirmar que:

a) A lógica proposicional e a lógica de predicados de primeira ordem são igualmente decidíveis, sempre existindo um algoritmo que determina em tempo finito se qualquer fórmula é válida
b) A lógica proposicional é decidível (por exemplo, via tabela-verdade), mas a lógica de predicados de primeira ordem é, em geral, indecidível — não existe algoritmo geral que sempre determine, em tempo finito, se uma fórmula qualquer é válida
c) Nenhuma das duas lógicas é decidível
d) A decidibilidade não é um conceito aplicável à lógica

> **Gabarito: b.** Resultado clássico (relacionado ao Teorema de Church-Turing sobre a indecidibilidade da lógica de primeira ordem): diferente da lógica proposicional, a validade em lógica de predicados não é, em geral, decidível por um algoritmo.

---

**22.** **(Pegadinha)** Considere a fórmula `∀x (P(x) → Q(x))` combinada com a premissa `P(a)`, sendo *a* um indivíduo específico do domínio. Qual conclusão pode ser validamente derivada por instanciação universal seguida de modus ponens?

a) `Q(a)`
b) `P(a) ∧ Q(a)` apenas se todos os elementos do domínio satisfizerem Q
c) `∀x Q(x)`, pois a regra vale para todo o domínio
d) Nenhuma conclusão pode ser derivada sem mais informações

> **Gabarito: a.** Pegadinha: instanciando `∀x(P(x)→Q(x))` para o indivíduo *a*, obtém-se `P(a)→Q(a)`; combinando com `P(a)` via modus ponens, conclui-se `Q(a)` — apenas para o indivíduo *a*, não para todo o domínio (erro comum é generalizar indevidamente para `∀x Q(x)`, alternativa c).

---

**23.** Em lógica de predicados, um **termo** pode ser:

a) Apenas uma constante
b) Uma variável, uma constante, ou o resultado da aplicação de uma função a outros termos
c) Exclusivamente um predicado
d) Um quantificador

> **Gabarito: b.** Termos são as expressões que denotam objetos do domínio: variáveis (x, y), constantes (a, b) ou aplicações de funções (f(x), soma(x,y)).

---

**24.** **(Pegadinha)** A fórmula `P(x) ∧ ∀x Q(x)`, na qual a primeira ocorrência de x está fora do escopo do quantificador ∀x, é um exemplo de:

a) Uma fórmula sem qualquer variável livre
b) Uma fórmula em que a primeira ocorrência de x é livre (fora do escopo do ∀x que aparece depois), enquanto a ocorrência de x dentro de Q(x) é ligada — ambas usam o mesmo símbolo "x", mas com papéis distintos
c) Uma fórmula malformada, proibida pela sintaxe da lógica de predicados
d) Uma contradição lógica

> **Gabarito: b.** Pegadinha sutil: é sintaticamente permitido reutilizar o símbolo x tanto livre quanto ligado na mesma fórmula (em subpartes distintas), mas isso pode gerar ambiguidade de leitura — por isso boas práticas de notação recomendam evitar essa reutilização, embora não seja tecnicamente malformada.

---

**25.** Qual é a tradução correta para "Todos os alunos que estudam passam na prova", usando Aluno(x), Estuda(x) e Passa(x)?

a) ∀x (Aluno(x) ∧ Estuda(x) ∧ Passa(x))
b) ∀x ((Aluno(x) ∧ Estuda(x)) → Passa(x))
c) ∃x ((Aluno(x) ∧ Estuda(x)) → Passa(x))
d) ∀x (Aluno(x) → (Estuda(x) ∧ Passa(x)))

> **Gabarito: b.** A estrutura "Todo A que é B é C" usa ∀ com a conjunção das condições no antecedente do condicional: ∀x((A(x)∧B(x)) → C(x)). A alternativa "d" erra ao transformar a condição "que estuda" em parte da conclusão, mudando o sentido da frase original.

---

**26.** **(Pegadinha)** A sentença "Só os alunos aprovados recebem certificado" pode ser corretamente traduzida, usando Aluno(x), Aprovado(x) e Certificado(x), como:

a) ∀x (Certificado(x) → (Aluno(x) ∧ Aprovado(x)))
b) ∀x ((Aluno(x) ∧ Aprovado(x)) → Certificado(x))
c) ∃x (Certificado(x) ∧ Aluno(x) ∧ Aprovado(x))
d) ∀x (Aluno(x) → Certificado(x))

> **Gabarito: a.** Pegadinha: construções do tipo "Só A é B" (ou "Somente quem é A recebe B") invertem a direção intuitiva do condicional em relação a "Todo A é B" — aqui a condição necessária é "receber certificado implica ser aluno aprovado", e não o contrário (alternativa b, que erra o sentido lógico).

---

**27.** Sobre a diferença entre predicados **unários** e **binários**, é correto afirmar que:

a) Um predicado unário recebe dois argumentos, e um binário recebe apenas um
b) Um predicado unário recebe um único argumento (ex.: `Primo(x)`), enquanto um predicado binário recebe dois argumentos, geralmente expressando uma relação entre dois indivíduos (ex.: `Ama(x,y)`)
c) Predicados unários e binários são sinônimos
d) Só existem predicados unários em lógica de predicados

> **Gabarito: b.** A aridade de um predicado indica o número de argumentos que ele recebe; predicados binários (ou de aridade maior) expressam relações entre múltiplos indivíduos.

---

**28.** **(Pegadinha)** Considere a fórmula `∃x P(x) ∧ ∃x Q(x)`. É correto afirmar que essa fórmula garante que:

a) Existe um único indivíduo que satisfaz tanto P quanto Q simultaneamente
b) Existe algum indivíduo que satisfaz P e existe algum indivíduo (possivelmente diferente do primeiro) que satisfaz Q — mas não necessariamente o mesmo indivíduo para ambos
c) Todo o domínio satisfaz P e Q ao mesmo tempo
d) A fórmula é logicamente equivalente a `∃x (P(x) ∧ Q(x))`

> **Gabarito: b.** Pegadinha muito comum: `∃x P(x) ∧ ∃x Q(x)` **não é equivalente** a `∃x (P(x) ∧ Q(x))`. No primeiro caso, os "x" das duas partes são variáveis ligadas por quantificadores distintos (podem se referir a indivíduos diferentes); no segundo, exige-se que um único indivíduo satisfaça ambos os predicados simultaneamente.

---

**29.** Em relação à igualdade (`=`) na lógica de predicados com igualdade, a fórmula `∃x∃y (P(x) ∧ P(y) ∧ x ≠ y)` expressa corretamente:

a) Que existe exatamente um elemento que satisfaz P
b) Que existem pelo menos dois elementos distintos que satisfazem P
c) Que nenhum elemento satisfaz P
d) Que todo elemento do domínio satisfaz P

> **Gabarito: b.** A combinação de dois existenciais com a condição x ≠ y é a forma padrão de expressar "existem (pelo menos) dois indivíduos distintos" que satisfazem determinada propriedade — um recurso comum para expressar cardinalidade mínima em lógica de predicados com igualdade.

---

**30.** **(Pegadinha)** Um estudante afirma: "A lógica de predicados é apenas uma forma mais bonita de escrever a lógica proposicional, sem ganho real de poder expressivo." Essa afirmação está:

a) Correta, pois qualquer fórmula de lógica de predicados pode ser reescrita como uma fórmula proposicional equivalente, sem perda de informação
b) Incorreta — a lógica de predicados é estritamente mais expressiva que a proposicional, pois permite quantificar sobre indivíduos de um domínio (possivelmente infinito) e expressar relações internas entre eles, algo que a lógica proposicional, ao tratar sentenças como blocos atômicos, não consegue capturar
c) Correta, pois ambas as lógicas são indecidíveis
d) Incorreta, mas apenas porque a lógica de predicados usa símbolos diferentes, sem qualquer diferença de fundo

> **Gabarito: b.** Pegadinha conceitual final: a diferença entre as duas lógicas não é apenas notacional — a capacidade de quantificar sobre domínios (inclusive infinitos) e expressar a estrutura interna das proposições dá à lógica de predicados um poder expressivo genuinamente maior do que o da lógica proposicional.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Recomenda-se reforçar, na correção, os pares de pegadinhas mais recorrentes na prova: **"todo A é B" (∀ com →) vs. "existe A que é B" (∃ com ∧)** (questões 5 e 6), a **negação de quantificadores** (questões 9-11), e a **não comutatividade entre ∀ e ∃** (questão 12) — esses são os erros mais frequentes de alunos iniciantes em lógica de predicados.
