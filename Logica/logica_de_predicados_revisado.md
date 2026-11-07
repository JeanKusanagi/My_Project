# II - Lógica de Predicados

A Lógica de Predicados, também denominada Lógica de Primeira Ordem (LPO) ou cálculo de predicados, constitui uma extensão da lógica proposicional que permite representar não apenas proposições inteiras, mas também objetos, propriedades, relações e quantificações sobre indivíduos de um domínio. Ela é um dos principais formalismos utilizados em Inteligência Artificial para representação de conhecimento e realização de inferências, pois permite expressar informações de maneira mais estruturada e geral. Além da IA, conceitos da lógica de primeira ordem são amplamente empregados na especificação e verificação formal de sistemas, na demonstração automática de teoremas e na fundamentação de aspectos da semântica de linguagens de programação e de bancos de dados.

Na lógica proposicional, uma sentença como "Sócrates é humano" pode ser representada por uma proposição simples, digamos P. Entretanto, esse formalismo não permite explicitar os elementos que compõem a sentença. Na lógica de predicados, podemos representá-la por Humano(Sócrates), em que Humano é um predicado e Sócrates é uma constante que representa um indivíduo. Diferente da lógica proposicional, que trata apenas de sentenças completas como verdadeiras ou falsas, a LPO permite representar propriedades dos objetos e relações entre diferentes entidades. Por exemplo, "João ama Maria" pode ser escrito como Ama(João, Maria), em que Ama é um predicado de dois argumentos (uma relação binária), e "O pai de João é professor" como Professor(pai(João)), em que pai é uma função.

## 1. A linguagem da lógica de predicados

A linguagem da lógica de predicados é composta principalmente por constantes, variáveis, predicados, funções, conectivos lógicos e quantificadores. As constantes representam indivíduos específicos, as variáveis representam elementos genéricos do domínio e os predicados representam propriedades ou relações entre indivíduos. As funções representam operações que associam elementos do domínio a outros elementos, permitindo representar objetos obtidos a partir de outros objetos.

Uma distinção importante: constantes, variáveis e funções aplicadas a termos formam **termos** (que denotam objetos), enquanto predicados aplicados a termos formam **fórmulas atômicas** (que têm valor de verdade). Assim, pai(João) é um termo (denota uma pessoa), ao passo que Professor(pai(João)) é uma fórmula atômica (é verdadeira ou falsa).

Os conectivos, como negação (¬), conjunção (∧), disjunção (∨), implicação (→), bicondicional (↔) e disjunção exclusiva (⊕), permitem combinar fórmulas. Em particular, a negação atua sobre uma única fórmula (não combina duas). Já os quantificadores, universal (∀) e existencial (∃), permitem expressar afirmações sobre todos os indivíduos do domínio ou sobre a existência de indivíduos com determinada propriedade.

O quantificador universal (∀) indica que uma propriedade é verdadeira para todos os elementos de determinado domínio, enquanto o quantificador existencial (∃) indica a existência de pelo menos um elemento que satisfaz determinada propriedade. Por exemplo, a afirmação "Todo ser humano é mortal" pode ser representada por:

∀x (Humano(x) → Mortal(x))

Já "Existe pelo menos um ser humano" pode ser representada por:

∃x Humano(x)

Note o padrão de uso: o quantificador universal é, em geral, combinado com a **implicação**, e o existencial com a **conjunção**. Assim:

- "Todo pássaro voa": ∀x (Pássaro(x) → Voa(x))
- "Algum pássaro voa": ∃x (Pássaro(x) ∧ Voa(x))

Escrever ∀x (Pássaro(x) ∧ Voa(x)) diria que *tudo* é pássaro e voa, e escrever ∃x (Pássaro(x) → Voa(x)) seria verdadeiro mesmo que existisse apenas um objeto que não é pássaro, pois a implicação é vacuamente verdadeira. Ambos são erros comuns de formalização.

A **ordem** dos quantificadores também importa quando são de tipos diferentes. Com o predicado Ama(x, y):

- ∀x ∃y Ama(x, y): "todo mundo ama alguém" (a pessoa amada pode variar com x);
- ∃y ∀x Ama(x, y): "existe alguém que é amado por todos" (a mesma pessoa para todo x).

A segunda fórmula implica a primeira, mas não o contrário.

Uma variável é dita **ligada** quando ocorre no escopo de um quantificador que a governa e **livre** caso contrário. Em ∀x (P(x, y)), a variável x é ligada e y é livre; já em ∀x P(x) → Q(x), o x de Q(x) está fora do escopo do quantificador e, portanto, é livre. Uma fórmula que não possui variáveis livres é denominada **sentença** ou **fórmula fechada**; ∀x ∃y Ama(x, y) é uma sentença, mas Ama(x, y) não é.

Uma sentença possui um valor de verdade determinado por uma interpretação, enquanto o valor de verdade de uma fórmula com variáveis livres depende, além da interpretação, da atribuição de elementos do domínio a essas variáveis. Uma sentença é dita verdadeira em uma interpretação quando é satisfeita por qualquer atribuição de variáveis nessa interpretação. Uma fórmula é **válida** (ou tautologia) quando é verdadeira em toda interpretação possível, **satisfazível** quando é verdadeira em pelo menos uma, e **contradição** (ou insatisfatível) quando é falsa em todas. Uma **contingência** (ou fórmula contingente) é satisfazível, mas não válida: é verdadeira em algumas interpretações e falsa em outras (na lógica proposicional, isso corresponde a uma tabela-verdade com valores V e F misturados). Por exemplo, ∀x P(x) → P(a) é válida; P(a) ∧ ¬P(a) é uma contradição; e ∃x P(x) é contingente.

## 2. Sintaxe e semântica

A sintaxe determina quais expressões são construídas corretamente de acordo com as regras formais da lógica. A semântica determina o significado dessas expressões em uma determinada interpretação. Assim, o valor de verdade de uma fórmula depende da interpretação atribuída aos símbolos que a compõem. Além disso, toda fórmula de primeira ordem é interpretada em relação a um domínio não vazio, que faz parte da interpretação.

Por exemplo, considere o domínio D = {a, b}, a constante Sócrates interpretada como a, e o predicado Humano interpretado como o conjunto {a}. Nessa interpretação:

- Humano(Sócrates) é verdadeira (pois a ∈ {a});
- ∃x Humano(x) é verdadeira (x = a satisfaz);
- ∀x Humano(x) é falsa (x = b não satisfaz).

Com outra interpretação (por exemplo, Humano = {a, b}), a terceira fórmula passaria a ser verdadeira. Isso mostra que o valor de verdade depende da interpretação.

## 3. Fórmulas bem formadas

Uma fórmula bem formada (fbf) na lógica de predicados é uma expressão construída de acordo com as regras sintáticas da linguagem. Sua construção pode ser descrita da seguinte forma:

- **Termos:** representam elementos do domínio e podem ser constantes (ex.: João), variáveis (ex.: x) ou funções aplicadas a termos (ex.: pai(João)).
- **Fórmulas atômicas:** é a fórmula mais simples possível e é obtida pela aplicação de um predicado a um ou mais termos, como Ama(João, Maria).
- **Fórmulas compostas:** são formadas a partir de outras fórmulas por meio dos conectivos lógicos ¬, ∧, ∨, → e ↔.
- **Fórmulas quantificadas:** são obtidas pela aplicação dos quantificadores universal (∀) ou existencial (∃) a uma variável e a uma fórmula, como ∀x (Pássaro(x) → Voa(x)).

Assim, as fórmulas bem formadas são construídas recursivamente, partindo das fórmulas atômicas e aplicando as regras de formação por meio dos conectivos lógicos e quantificadores. Por exemplo, a fórmula ∀x (Pássaro(x) → ¬Ama(x, pai(x))) é bem formada, pois Pássaro(x) e Ama(x, pai(x)) são atômicas, ¬Ama(x, pai(x)) é composta, a implicação é composta e, por fim, a quantificação universal é aplicada. Já expressões como Humano(Ama) ou ∀ Humano(x) → não são fbfs. Uma das principais vantagens da LPO é justamente a capacidade de generalizar sobre indivíduos, possibilitada pelos quantificadores.

## 4. Equivalências lógicas

Da mesma forma que os conectivos da lógica proposicional possuem equivalências úteis (como as Leis de De Morgan ¬(A ∧ B) ≡ ¬A ∨ ¬B e ¬(A ∨ B) ≡ ¬A ∧ ¬B), os quantificadores também obedecem a leis próprias de transformação. Entre elas, destacam-se as Leis de De Morgan para quantificadores, que permitem passar a negação por um quantificador, trocando ∀ por ∃ e vice-versa:

¬∀x P(x) ≡ ∃x ¬P(x)

¬∃x P(x) ≡ ∀x ¬P(x)

Em linguagem natural, "Nem todos os alunos foram aprovados" é equivalente a "Existe pelo menos um aluno que não foi aprovado". Formalmente:

¬∀x (Aluno(x) → Aprovado(x)) ≡ ∃x ¬(Aluno(x) → Aprovado(x)) ≡ ∃x (Aluno(x) ∧ ¬Aprovado(x))

O último passo usa a negação da implicação, ¬(P → Q) ≡ P ∧ ¬Q. Observe que o resultado **não** é ∃x (Aluno(x) → ¬Aprovado(x)): a troca de quantificadores deve ser acompanhada da negação de todo o corpo da fórmula, e a implicação exige cuidado especial. Analogamente, "Nenhum aluno foi aprovado" é:

¬∃x (Aluno(x) ∧ Aprovado(x)) ≡ ∀x ¬(Aluno(x) ∧ Aprovado(x)) ≡ ∀x (Aluno(x) → ¬Aprovado(x))

Outras equivalências úteis envolvem a distribuição e a troca de quantificadores:

- ∀x (P(x) ∧ Q(x)) ≡ ∀x P(x) ∧ ∀x Q(x)
- ∃x (P(x) ∨ Q(x)) ≡ ∃x P(x) ∨ ∃x Q(x)
- ∀x ∀y P(x, y) ≡ ∀y ∀x P(x, y) e ∃x ∃y P(x, y) ≡ ∃y ∃x P(x, y)
- Se x não ocorre livre em Q: ∀x (P(x) → Q) ≡ (∃x P(x)) → Q e ∃x (P(x) → Q) ≡ (∀x P(x)) → Q

Atenção: ∀x (P(x) ∨ Q(x)) **não** é equivalente a ∀x P(x) ∨ ∀x Q(x), nem ∃x (P(x) ∧ Q(x)) a ∃x P(x) ∧ ∃x Q(x). E, como visto, quantificadores de tipos diferentes não comutam (∀x ∃y ≢ ∃y ∀x). A última equivalência da lista, em particular, será usada na conversão para a forma prenex.

## 5. Inferência: dedução natural

Essa capacidade de representar conhecimento de maneira geral constitui uma importante vantagem da lógica de predicados em relação à lógica proposicional. A partir de fatos e regras, um sistema pode realizar inferências, derivando novas informações que não estavam explicitamente armazenadas na base de conhecimento. Por exemplo, considerando que Sócrates é humano e que todo humano é mortal, é possível inferir que Sócrates é mortal.

O sistema de dedução natural organiza as regras de inferência em regras de introdução e eliminação para cada conectivo lógico e para os quantificadores, permitindo construir demonstrações formais a partir de hipóteses e premissas. As principais regras envolvendo quantificadores e o Modus Ponens estão resumidas na tabela a seguir:

| Regra | Descrição | Exemplo |
|---|---|---|
| Instanciação Universal (UI) | De ∀x P(x), pode-se inferir P(a) para qualquer constante a do domínio. | ∀x (Humano(x) → Mortal(x)) ⟹ Humano(Sócrates) → Mortal(Sócrates) |
| Generalização Universal (UG) | Se P(a) é verdadeiro para um elemento arbitrário a (sobre o qual nenhuma premissa específica foi assumida), pode-se inferir ∀x P(x). | P(a) válido para a arbitrário ⟹ ∀x P(x) |
| Instanciação Existencial (EI) | De ∃x P(x), pode-se inferir P(c) para uma nova constante c (ainda não usada). | ∃x Primo(x) ⟹ Primo(c), c nova |
| Generalização Existencial (EG) | De P(a) para uma constante específica a, pode-se inferir ∃x P(x). | Primo(7) ⟹ ∃x Primo(x) |
| Modus Ponens (MP) | De P e P → Q, pode-se inferir Q (aplicado a fórmulas com predicados). | Humano(Sócrates), Humano(Sócrates) → Mortal(Sócrates) ⟹ Mortal(Sócrates) |
| Modus Tollens (MT) | De P → Q e ¬Q, pode-se inferir ¬P. | Humano(Zeus) → Mortal(Zeus), ¬Mortal(Zeus) ⟹ ¬Humano(Zeus) |

Essas regras podem ser combinadas para construir provas formais, nas quais cada nova fórmula é obtida a partir de premissas ou de fórmulas anteriormente demonstradas. Um exemplo clássico de prova formal é o Silogismo de Sócrates:

1. ∀x (Humano(x) → Mortal(x)) — premissa
2. Humano(Sócrates) — premissa
3. Humano(Sócrates) → Mortal(Sócrates) — por UI em (1)
4. Mortal(Sócrates) — por Modus Ponens em (2) e (3)

O exemplo mostra como uma regra geral, representada por um quantificador universal, pode ser aplicada a um indivíduo específico para produzir uma nova conclusão. O mesmo princípio pode ser utilizado em situações mais complexas de representação de conhecimento, nas quais fatos e relações entre indivíduos são combinados para produzir novas informações.

Considere, por exemplo, o seguinte conhecimento:

- Todo pesquisador que publica algum artigo possui produção científica.
- Ana é pesquisadora.
- Ana publicou o artigo a1.

Podemos representar:

∀x ∀y (Pesquisador(x) ∧ Artigo(y) ∧ Publica(x, y) → ProducaoCientifica(x))

e os fatos:

Pesquisador(Ana), Artigo(a1), Publica(Ana, a1)

Observe que "publica algum artigo" aparece no antecedente da implicação; por isso o quantificador existencial ∃y (Artigo(y) ∧ Publica(x, y)) → ProducaoCientifica(x) vira, pela última equivalência da seção 4, um ∀y sobre toda a implicação. Instanciando x = Ana e y = a1 (duas aplicações de UI):

Pesquisador(Ana) ∧ Artigo(a1) ∧ Publica(Ana, a1) → ProducaoCientifica(Ana)

Como o antecedente é verdadeiro (os três fatos são premissas), o Modus Ponens permite concluir ProducaoCientifica(Ana).

## 6. Inferência automática: unificação e resolução

A dedução natural é adequada para demonstrações feitas por humanos, mas é difícil de automatizar. Para a prova automática, utiliza-se um mecanismo mais mecânico, baseado em dois conceitos: a unificação e a resolução.

A **unificação** é responsável por determinar substituições que tornam expressões lógicas compatíveis, e é fundamental para os algoritmos de inferência em lógica de primeira ordem. Exemplos:

- P(x, f(y)) e P(a, f(b)) unificam com a substituição {x/a, y/b};
- P(x, x) e P(a, b) **não** unificam, pois x não pode ser ao mesmo tempo a e b;
- x e f(x) não unificam (falha na verificação de ocorrência, *occurs check*), pois levariam a um termo infinito.

Associada à unificação, destaca-se a **resolução**, um método de prova que pode ser utilizado para demonstrar que uma determinada conclusão decorre logicamente de um conjunto de premissas. Ela funciona por **refutação**: em vez de derivar a conclusão diretamente, adiciona-se sua negação às premissas e busca-se uma contradição. A resolução é correta e completa para refutação, isto é, ela chega à cláusula vazia se, e somente se, o conjunto de cláusulas for insatisfatível.

Para sua aplicação, as fórmulas normalmente são convertidas para uma forma adequada, como a Forma Normal Conjuntiva (FNC). A partir dessa representação, a fórmula pode ser organizada como um conjunto de cláusulas, denominado forma clausal, que constitui a representação utilizada pelo procedimento de resolução. Esse processo envolve uma sequência padronizada de transformações que preservam a satisfatibilidade da fórmula (a fórmula original e sua forma clausal são equissatisfatíveis, embora nem sempre equivalentes) e a tornam adequada aos procedimentos de inferência.

Inicialmente, eliminam-se os bicondicionais e as implicações, substituindo-os por equivalências lógicas. Em seguida, aplicam-se as Leis de De Morgan e as demais equivalências necessárias para que todas as negações sejam posicionadas diretamente sobre os átomos. As variáveis também podem ser renomeadas para evitar conflitos de escopo e garantir que variáveis provenientes de diferentes quantificadores sejam tratadas de maneira independente. As equivalências mais usadas nessa etapa são:

- P → Q ≡ ¬P ∨ Q (e, portanto, a negação ¬(P → Q) ≡ P ∧ ¬Q)
- P ↔ Q ≡ (P → Q) ∧ (Q → P)
- P → Q ≡ ¬Q → ¬P (contrapositiva, útil na leitura de regras, mas não necessária para a conversão)
- ¬(A ∧ B) ≡ ¬A ∨ ¬B
- ¬(A ∨ B) ≡ ¬A ∧ ¬B
- ¬¬A ≡ A
- ¬∀x P(x) ≡ ∃x ¬P(x) e ¬∃x P(x) ≡ ∀x ¬P(x)

Em seguida, movem-se os quantificadores para o início da fórmula, obtendo-se a **Forma Normal Prenex (FNP)**: uma forma padronizada de escrever fórmulas da Lógica de Predicados na qual todos os quantificadores aparecem no início da fórmula, formando o chamado prefixo de quantificadores. O restante da fórmula, chamado matriz, não contém quantificadores. Por exemplo:

∀x P(x) → ∃y Q(y)
≡ ¬∀x P(x) ∨ ∃y Q(y)  (eliminação da implicação)
≡ ∃x ¬P(x) ∨ ∃y Q(y)  (De Morgan para quantificadores)
≡ ∃x ∃y (¬P(x) ∨ Q(y))  (prenex; prefixo ∃x ∃y, matriz ¬P(x) ∨ Q(y))

Quando a mesma variável é usada em quantificadores distintos, como em (∀x P(x)) ∧ (∃x Q(x)), é preciso renomeá-la antes de mover os quantificadores, obtendo ∀x ∃y (P(x) ∧ Q(y)).

Posteriormente, realiza-se a **Skolemização**, que elimina os quantificadores existenciais por meio da introdução de constantes ou funções de Skolem. Uma variável existencial que não esteja sob o escopo de nenhum quantificador universal pode ser substituída por uma constante de Skolem. Quando está sob o escopo de uma ou mais variáveis universais, é substituída por uma função de Skolem que recebe essas variáveis como argumentos.

Por exemplo, a fórmula

∀x ∃y P(x, y)

pode ser skolemizada substituindo-se a variável existencialmente quantificada y por uma função de Skolem f(x), que depende de x (já que y está no escopo de ∀x). Isso resulta em:

∀x P(x, f(x))

Já em ∃x ∀y P(x, y), a variável x não está sob nenhum ∀, e é substituída por uma constante de Skolem a, resultando em ∀y P(a, y). A diferença entre os dois casos reflete exatamente a diferença de significado entre as ordens dos quantificadores vista na seção 1.

Como, na forma clausal, os quantificadores universais são implícitos (toda variável livre é considerada universalmente quantificada), o quantificador ∀x pode ser omitido, produzindo a cláusula final:

P(x, f(x))

Após a Skolemização, realiza-se a conversão para FNC, aplicando-se, entre outras, a propriedade distributiva da disjunção sobre a conjunção:

P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)

Em seguida, a fórmula pode ser representada como um conjunto de cláusulas, em que cada cláusula corresponde a uma disjunção de literais. A título de ilustração, a regra "Todo aluno tem um orientador" passa por estas etapas:

∀x (Aluno(x) → ∃y Orienta(y, x))
→ ∀x (¬Aluno(x) ∨ ∃y Orienta(y, x))  (eliminação da implicação)
→ ∀x ∃y (¬Aluno(x) ∨ Orienta(y, x))  (prenex)
→ ∀x (¬Aluno(x) ∨ Orienta(f(x), x))  (Skolemização, y ↦ f(x))
→ ¬Aluno(x) ∨ Orienta(f(x), x)  (cláusula, com ∀ implícito)

A partir dessa representação, a regra de resolução pode ser aplicada iterativamente. Dadas duas cláusulas contendo literais complementares (p e ¬p), possivelmente após uma unificação, esses literais são eliminados e os demais literais das duas cláusulas são combinados para gerar uma nova cláusula (o resolvente). Por fim, quando se utiliza o método de resolução para provar uma conclusão, a sequência típica é:

1. Formalização → 2. Negação da conclusão → 3. Eliminação de → e ↔ e movimentação das negações → 4. Forma prenex → 5. Skolemização → 6. Forma Normal Conjuntiva (FNC) → 7. Conjunto de cláusulas → 8. Resolução → 9. Cláusula vazia

Em mais detalhes:

1. Formalizar as premissas e a conclusão em lógica de predicados.
2. Adicionar a negação da conclusão às premissas: P1 ∧ P2 ∧ ⋯ ∧ Pn ∧ ¬C.
3. Eliminar implicações e equivalências, quando presentes, e mover as negações para junto dos átomos (Leis de De Morgan).
4. Renomear variáveis para evitar conflitos e colocar as fórmulas em forma prenex, quando necessário.
5. Skolemizar as variáveis existenciais, substituindo-as por constantes ou funções de Skolem, e omitir os quantificadores universais.
6. Converter para FNC, utilizando equivalências lógicas, incluindo a distributividade: P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R).
7. Separar a FNC em cláusulas, obtendo um conjunto de cláusulas.
8. Aplicar a regra de resolução, unificando literais complementares. Por exemplo, de (P(x) ∨ Q(x)) e (¬P(a) ∨ R(a)), obtém-se, após a unificação x/a: Q(a) ∨ R(a).
9. Continuar aplicando resolução até obter a cláusula vazia (□).

A obtenção de □ demonstra que o conjunto formado pelas premissas + negação da conclusão é inconsistente. Portanto, a conclusão é consequência lógica das premissas.

**Exemplo 1 (silogismo de Sócrates por resolução).** Premissas: ∀x (Humano(x) → Mortal(x)) e Humano(Sócrates). Conclusão: Mortal(Sócrates). Negando a conclusão e convertendo para cláusulas:

1. ¬Humano(x) ∨ Mortal(x)  (premissa 1)
2. Humano(Sócrates)  (premissa 2)
3. ¬Mortal(Sócrates)  (negação da conclusão)
4. ¬Humano(Sócrates)  (resolução de 1 e 3, com x/Sócrates)
5. □  (resolução de 2 e 4)

**Exemplo 2 (com Skolemização).** Premissas: ∀x (Aluno(x) → ∃y Orienta(y, x)) e Aluno(Ana). Conclusão: ∃y Orienta(y, Ana). A negação da conclusão é ¬∃y Orienta(y, Ana) ≡ ∀y ¬Orienta(y, Ana). Cláusulas:

1. ¬Aluno(x) ∨ Orienta(f(x), x)  (premissa 1 skolemizada)
2. Aluno(Ana)  (premissa 2)
3. ¬Orienta(y, Ana)  (negação da conclusão)
4. Orienta(f(Ana), Ana)  (resolução de 1 e 2, com x/Ana)
5. □  (resolução de 3 e 4, com y/f(Ana))

## 7. Lógica de predicados e programação lógica

A lógica de predicados apresenta papel importante na representação de conhecimento em Inteligência Artificial, sendo utilizada em sistemas especialistas, agentes inteligentes, sistemas de diagnóstico e linguagens de programação lógica, como o Prolog. Em Prolog, fatos e regras são representados de maneira declarativa, enquanto mecanismos de unificação e busca são utilizados para responder às consultas. Embora a lógica de predicados seja mais abrangente, o Prolog utiliza principalmente um subconjunto denominado cláusulas de Horn, que possuem no máximo um literal positivo. Por exemplo, a cláusula ¬Humano(x) ∨ Mortal(x), que vimos na resolução, é uma cláusula de Horn e corresponde diretamente à regra Prolog mortal(X) :- humano(X).

Computacionalmente, o Prolog utiliza a unificação para determinar valores que tornam termos logicamente compatíveis e a resolução (na variante conhecida como resolução SLD) para derivar consequências a partir dos fatos e regras. A busca pelas soluções é tradicionalmente realizada em profundidade, com retrocesso (backtracking) quando uma alternativa não conduz a uma solução. Dessa forma, o Prolog estabelece uma conexão direta entre lógica formal e computação, permitindo representar conhecimento e realizar inferências de maneira declarativa. Essa abordagem encontra aplicações em áreas como sistemas especialistas, processamento de linguagem natural, representação de conhecimento e verificação formal.

Um programa, utilizando Prolog, pode representar fatos da seguinte forma:

```prolog
humano(socrates).
```

e regras:

```prolog
mortal(X) :- humano(X).
```

A consulta:

```prolog
?- mortal(socrates).
true.
```

Consultas com variáveis retornam as substituições que as satisfazem:

```prolog
?- mortal(X).
X = socrates.
```

O exemplo da pesquisadora, com a regra de duas condições e o fato adicional, fica:

```prolog
pesquisador(ana).
artigo(a1).
publica(ana, a1).
producao_cientifica(X) :- pesquisador(X), artigo(Y), publica(X, Y).

?- producao_cientifica(ana).
true.
```

Vale notar que o Prolog usa a negação como falha (se não é possível provar algo, considera-se falso), o que difere da negação clássica da lógica de primeira ordem.

## 8. Limitações e relevância atual

Apesar de seu poder expressivo, a lógica de primeira ordem possui limitações computacionais. Em particular, o problema geral de determinar se uma fórmula arbitrária é consequência lógica de um conjunto de premissas é indecidível; mais precisamente, é **semidecidível**. Isso significa que não existe um algoritmo que, para qualquer entrada, sempre termine e determine corretamente se a conclusão pode ser derivada: se a conclusão de fato decorre das premissas, um procedimento completo (como a resolução) acabará encontrando a prova, mas, se não decorre, o procedimento pode não terminar. Assim, sistemas práticos frequentemente utilizam subconjuntos da lógica (como as cláusulas de Horn) ou estratégias de inferência específicas para manter a complexidade computacional sob controle.

Embora as técnicas de deep learning e os modelos probabilísticos tenham assumido um papel central na IA moderna, a lógica de predicados continua relevante. Ela oferece vantagens particularmente importantes em situações que exigem representação explícita do conhecimento, raciocínio dedutivo, explicabilidade, verificação formal, consistência lógica, planejamento simbólico e raciocínio sobre relações entre entidades.

Por outro lado, sistemas puramente lógicos apresentam dificuldades para representar diretamente fenômenos como percepção visual, linguagem ambígua, incerteza e dados de alta dimensionalidade. Essa diferença ajuda a explicar a importância contemporânea das abordagens neuro-simbólicas, que procuram combinar a capacidade de aprendizagem estatística com a representação e o raciocínio simbólicos.

## Síntese

Em síntese, a Lógica de Predicados fornece um formalismo poderoso para representar conhecimento sobre indivíduos, propriedades e relações e para realizar inferências sobre esse conhecimento. Seus conceitos fundamentais (predicados, variáveis, constantes, funções, conectivos, quantificadores, unificação e resolução) formam uma base importante para a Inteligência Artificial simbólica e para a construção de sistemas capazes de raciocinar de maneira formal.
