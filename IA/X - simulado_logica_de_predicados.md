# Simulado: Lógica de Predicados (Lógica de Primeira Ordem)

**Instruções:**
* Responda às 30 questões de múltipla escolha (A, B, C, D ou E).
* Preste atenção às propriedades dos quantificadores, escopos, negações e equivalências lógicas.
* Ao final de cada questão, leia o gabarito comentado para validar a fundamentação teórica.

---

### Questão 1 (Fácil)

Na Lógica de Primeira Ordem, como se traduz formalmente a sentença: *"Todos os filósofos são pensadores"*?

*(Considere $F(x)$: "$x$ é filósofo" e $P(x)$: "$x$ é pensador")*

A) $\exists x (F(x) \land P(x))$

B) $\forall x (F(x) \rightarrow P(x))$

C) $\forall x (F(x) \land P(x))$

D) $\exists x (F(x) \rightarrow P(x))$

E) $\forall x (P(x) \rightarrow F(x))$

**Resposta Correta: B**

**Comentário:** A declaração universal afirmativa ("Todo A é B") é padronizada na lógica de predicados através do quantificador universal $\forall$ combinado com o conectivo condicional $\rightarrow$. A forma $\forall x (F(x) \rightarrow P(x))$ lê-se "Para todo $x$, se $x$ é filósofo, então $x$ é pensador". O uso da conjunção $\land$ com $\forall$ (como na alternativa C) significaria erroneamente que *todos os objetos do universo* são ao mesmo tempo filósofos e pensadores.

---

### Questão 2 (Médio - *Pegadinha*)

Qual é a negação lógica correta da proposição quantificada $\forall x (P(x) \rightarrow Q(x))$?

A) $\exists x (P(x) \rightarrow \neg Q(x))$

B) $\forall x (P(x) \land \neg Q(x))$

C) $\exists x (P(x) \land \neg Q(x))$

D) $\exists x (\neg P(x) \lor Q(x))$

E) $\forall x (\neg P(x) \rightarrow \neg Q(x))$

**Resposta Correta: C**

**Comentário:** *Pegadinha clássica!* Para negar uma sentença com quantificador universal, nega-se a proposição interna e troca-se o quantificador: $\neg \forall x A(x) \equiv \exists x \neg A(x)$. Aplicando isso à condicional $P(x) \rightarrow Q(x)$: sabendo que a negação da condicional $\neg (A \rightarrow B)$ é $A \land \neg B$, obtemos $\exists x \neg (P(x) \rightarrow Q(x)) \equiv \exists x (P(x) \land \neg Q(x))$. Muitos erram ao achar que a negação de uma condicional gera outra condicional (como nas alternativas A ou E).

---

### Questão 3 (Difícil)

Considere a fórmula $\forall x \exists y R(x, y)$ definida sobre o domínio dos números inteiros $\mathbb{Z}$, onde $R(x, y)$ significa "$x < y$". O que ocorre se invertermos a ordem dos quantificadores para $\exists y \forall x R(x, y)$ no mesmo domínio?

A) O valor lógico permanece Verdadeiro, pois os quantificadores comutam livremente.

B) A fórmula passa de Verdadeira para Falsa.

C) A fórmula passa de Falsa para Verdadeira.

D) A fórmula torna-se sintaticamente inválida na Lógica de Primeira Ordem.

E) O valor lógico permanece Falso em ambas as formulações.

**Resposta Correta: B**

**Comentário:** A ordem dos quantificadores importa criticamente quando eles são diferentes! 
1. $\forall x \exists y (x < y)$: "Para todo inteiro $x$, existe um inteiro $y$ maior que ele". Isso é **Verdadeiro** (basta escolher $y = x + 1$).
2. $\exists y \forall x (x < y)$: "Existe um inteiro $y$ fixo que é estritamente maior que todos os inteiros $x$ do universo". Isso é **Falso**, pois não existe um número inteiro máximo.

---

### Questão 4 (Fácil)

Em Lógica de Predicados, uma variável em uma fórmula é dita **ligada** (*bound*) se ela está sob o escopo de:

A) Uma constante individual.

B) Um conectivo lógico de condicional ($\rightarrow$).

C) Um quantificador (universal $\forall$ ou existencial $\exists$).

D) Um símbolo de função unária.

E) Uma tautologia cartesiana.

**Resposta Correta: C**

**Comentário:** Uma variável é considerada *ligada* quando ela aparece associada a um quantificador (seja $\forall x$ ou $\exists x$) que delimita seu escopo. Caso contrário, se a variável não estiver sob o escopo de nenhum quantificador para aquela variável, ela é chamada de variável *livre* (*free variable*).

---

### Questão 5 (Médio)

Dada a sentença do português: *"Existe pelo menos um estudante que não gosta de nenhuma disciplina"*, assinale a tradução formal correta sobre o domínio de pessoas e disciplinas.

*(Considere $E(x)$: "$x$ é estudante", $D(y)$: "$y$ é disciplina", $G(x, y)$: "$x$ gosta de $y$")*

A) $\exists x (E(x) \land \forall y (D(y) \rightarrow \neg G(x, y)))$

B) $\exists x (E(x) \rightarrow \forall y (D(y) \land \neg G(x, y)))$

C) $\forall x (E(x) \land \exists y (D(y) \land \neg G(x, y)))$

D) $\exists x \exists y (E(x) \land D(y) \land \neg G(x, y))$

E) $\forall x \forall y ((E(x) \land D(y)) \rightarrow \neg G(x, y))$

**Resposta Correta: A**

**Comentário:** A estrutura é: "Existe um $x$ tal que $x$ é estudante AND para toda disciplina $y$, $x$ não gosta de $y$". 
O uso de $\land$ conecta o fato de $x$ ser estudante com a propriedade universal relativa às disciplinas ($\forall y (D(y) \rightarrow \neg G(x, y))$). A alternativa D está errada pois afirma apenas que existe *uma* disciplina que ele não gosta, e não *nenhuma* (todas).

---

### Questão 6 (Difícil - *Pegadinha*)

Considere a fórmula em Lógica de Primeira Ordem: $\phi = (\forall x P(x)) \rightarrow (\exists x Q(x))$. Qual das seguintes opções é uma forma logicamente equivalente a $\phi$?

A) $\forall x (P(x) \rightarrow Q(x))$

B) $\exists x (P(x) \rightarrow Q(x))$

C) $\exists x \forall y (P(x) \rightarrow Q(y))$

D) $\exists x \exists y (P(x) \rightarrow Q(y))$

E) $\forall x \exists y (P(x) \land Q(y))$

**Resposta Correta: D**

**Comentário:** *Pegadinha de reescrita de escopo (Forma Normal Prenex)!*
Vamos renomear variáveis e mover quantificadores:
$\phi = (\forall x P(x)) \rightarrow (\exists y Q(y))$.
Pela regra da negação da condicional/equivalência da condicional $A \rightarrow B \equiv \neg A \lor B$:
$\phi \equiv \neg (\forall x P(x)) \lor (\exists y Q(y)) \equiv (\exists x \neg P(x)) \lor (\exists y Q(y))$.
Como o quantificador existencial pode ser colocado para fora da disjunção:
$\phi \equiv \exists x \exists y (\neg P(x) \lor Q(y)) \equiv \exists x \exists y (P(x) \rightarrow Q(y))$.
Muitos tentam juntar direto em $\forall x (P(x) \rightarrow Q(x))$, o que é um erro clássico de escopo.

---

### Questão 7 (Médio)

Qual é o valor de verdade da proposição $\forall x (x^2 \ge 0)$ se o universo do discurso for o conjunto dos números complexos $\mathbb{C}$?

A) Verdadeiro, pois qualquer número elevado ao quadrado resulta em um valor não negativo.

B) Falso, pois para números imaginários puros como $i$, temos $i^2 = -1 < 0$.

C) Indeterminado, pois o quantificador universal não pode ser aplicado ao conjunto $\mathbb{C}$.

D) Verdadeiro, pela propriedade distributiva da multiplicação sobre somas no campo complexo.

E) Falso, pois $0^2 = 0$ não é estritamente maior que zero.

**Resposta Correta: B**

**Comentário:** A validade de uma fórmula quantificada depende crucialmente do **Universo do Discurso (Domínio)**. Enquanto em $\mathbb{R}$ a sentença é Verdadeira, em $\mathbb{C}$ temos o contraexemplo da unidade imaginária $i$, onde $i^2 = -1$. Como $-1 < 0$, o quantificador universal falha e a proposição é Falsa.

---

### Questão 8 (Fácil)

A regra de inferência que permite deduzir $P(c)$ para qualquer constante $c$ pertencente ao domínio, a partir da premissa $\forall x P(x)$, é chamada de:

A) Generalização Universal

B) Instanciação Universal (ou Especificação Universal)

C) Instanciação Existencial

D) Generalização Existencial

E) Modus Tollens Predicativo

**Resposta Correta: B**

**Comentário:** A **Instanciação Universal** (Universal Instantiation) é a regra de inferência básica que nos permite deduzir que, se uma propriedade vale para *todos* os elementos do domínio ($\forall x P(x)$), então ela vale para qualquer elemento arbitrário específico $c$ desse domínio ($P(c)$).

---

### Questão 9 (Difícil)

A **Skolemização** é um passo essencial no processo de conversão de fórmulas de primeira ordem para a Forma Normal Clausal (usada na Resolução). Como se elimina um quantificador existencial que está dentro do escopo de um quantificador universal, como em $\forall x \exists y R(x, y)$?

A) Substitui-se $y$ por uma constante de Skolem $c$, resultando em $\forall x R(x, c)$.

B) Elimina-se simplesmente o quantificador $\exists y$, resultando em $\forall x R(x, y)$.

C) Substitui-se $y$ por uma **função de Skolem** $f(x)$ dependente de $x$, resultando em $\forall x R(x, f(x))$.

D) Inverte-se a posição para $\exists y \forall x R(x, y)$ e depois substitui-se por uma variável livre.

E) Substitui-se o conectivo por uma implicação lógica entre $x$ e $y$.

**Resposta Correta: C**

**Comentário:** Quando um quantificador existencial $\exists y$ ocorre dentro do escopo de um quantificador universal $\forall x$, o valor de $y$ depende do valor escolhido para $x$. Por isso, não podemos usar uma constante simples; devemos substituir $y$ por uma **função de Skolem** $f(x)$. Se $\exists y$ não estivesse no escopo de nenhum $\forall$, aí sim usaríamos uma *constante de Skolem*.

---

### Questão 10 (Médio - *Pegadinha*)

Considere a expressão $P(x) \land \exists x Q(x)$. Qual das opções descreve corretamente o status das ocorrências da variável $x$?

A) Ambas as ocorrências de $x$ estão ligadas pelo quantificador existencial.

B) A primeira ocorrência de $x$ (em $P(x)$) é livre, enquanto a segunda ocorrência de $x$ (em $Q(x)$) é ligada.

C) Ambas as ocorrências de $x$ são variáveis livres.

D) A expressão é sintaticamente inválida, pois não se pode reutilizar o mesmo nome de variável.

E) A primeira ocorrência é ligada e a segunda é livre.

**Resposta Correta: B**

**Comentário:** *Pegadinha de escopo de quantificador!* O escopo de $\exists x$ abrange apenas a fórmula imediatamente subsequente, ou seja, $Q(x)$. O $x$ em $P(x)$ está fora desse escopo. Portanto, o $x$ em $P(x)$ é uma **variável livre**, enquanto o $x$ em $Q(x)$ é uma **variável ligada**. É uma boa prática reescrever isso como $P(x) \land \exists y Q(y)$ para evitar confusões.

---

### Questão 11 (Fácil)

Qual das alternativas a seguir expressa a equivalência lógica correta da negação de um quantificador existencial, isto é, $\neg \exists x P(x)$?

A) $\exists x \neg P(x)$

B) $\forall x P(x)$

C) $\forall x \neg P(x)$

D) $\neg \forall x P(x)$

E) $\forall x \neg (\neg P(x))$

**Resposta Correta: C**

**Comentário:** Dizer que "Não existe nenhum $x$ que possui a propriedade $P$" ($\neg \exists x P(x)$) é logicamente equivalente a dizer que "Para todos os $x$, $x$ NÃO possui a propriedade $P$" ($\forall x \neg P(x)$). Esta é uma das leis de De Morgan para quantificadores.

---

### Questão 12 (Médio)

Considere a interpretação em que o domínio é o conjunto dos seres humanos, $P(x, y)$ significa "$x$ é pai de $y$". Como pode ser traduzida a fórmula $\exists x \forall y P(x, y)$?

A) Toda pessoa tem um pai.

B) Existe alguém que é pai de todos (inclusive de si mesmo).

C) Ninguém é pai de todo mundo.

D) Toda pessoa é pai de alguma pessoa.

E) Existem duas pessoas que têm o mesmo pai.

**Resposta Correta: B**

**Comentário:**
A ordem $\exists x \forall y$ fixa primeiramente o indivíduo $x$: "Existe um indivíduo $x$ tal que, para qualquer pessoa $y$, $x$ é pai de $y$". Ou seja, $x$ é o pai universal de todas as pessoas. 
(Se a frase fosse "Toda pessoa tem um pai", a formalização correta seria $\forall y \exists x P(x, y)$).

---

### Questão 13 (Difícil - *Pegadinha*)

Seja $\Sigma$ um conjunto de sentenças em Lógica de Primeira Ordem. Pelo **Teorema da Compacidade** (*Compactness Theorem*), $\Sigma$ tem um modelo (é satisfazível) se e somente se:

A) $\Sigma$ for um conjunto finito de sentenças.

B) Todo subconjunto finito de $\Sigma$ tiver um modelo.

C) Nenhuma variável em $\Sigma$ for livre.

D) A negação de $\Sigma$ for uma contradição computável em tempo polinomial.

E) $\Sigma$ puder ser provado usando unicamente a regra de Modus Ponens sem quantificadores.

**Resposta Correta: B**

**Comentário:** O **Teorema da Compacidade** para a Lógica de Primeira Ordem afirma que um conjunto infinito de fórmulas $\Sigma$ possui um modelo (é satisfazível) se, e somente se, **todo subconjunto finito de $\Sigma$ for satisfazível**. A pegadinha na alternativa A é sugerir que $\Sigma$ precisa ser finito, quando na verdade o teorema trata justamente da relação entre conjuntos infinitos e seus subconjuntos finitos.

---

### Questão 14 (Médio)

Na Lógica de Primeira Ordem, qual é a diferença fundamental entre um símbolo de **Predicado** e um símbolo de **Função**?

A) Predicados retornam valores numéricos; Funções retornam valores booleanos (Verdadeiro/Falso).

B) Predicados mapeiam elementos do domínio em valores de verdade (Verdadeiro/Falso); Funções mapeiam elementos do domínio em outros elementos do próprio domínio.

C) Funções podem ser quantificadas por $\forall$; Predicados não podem ser quantificados.

D) Predicados aplicam-se apenas a variáveis ligadas; Funções aplicam-se apenas a constantes.

E) Não há diferença; são apenas sinônimos sintáticos.

**Resposta Correta: B**

**Comentário:** 
- Um **Predicado** de aridade $n$ avalia uma $n$-tupla de objetos e produz um valor lógico (booleano): $P: D^n \rightarrow \{V, F\}$. 
- Uma **Função** de aridade $n$ recebe uma $n$-tupla de objetos do domínio e retorna outro objeto do próprio domínio: $f: D^n \rightarrow D$. (Exemplo: $pai\_de(x)$ retorna uma pessoa, enquanto $EhPai(x)$ retorna Verdadeiro ou Falso).

---

### Questão 15 (Fácil)

Qual é a representação formal correta para a sentença: *"Alguns gatos não são pretos"*?

*(Considere $G(x)$: "$x$ é gato" e $P(x)$: "$x$ é preto")*

A) $\exists x (G(x) \land \neg P(x))$

B) $\exists x (G(x) \rightarrow \neg P(x))$

C) $\forall x (G(x) \land \neg P(x))$

D) $\neg \exists x (G(x) \land P(x))$

E) $\exists x (\neg G(x) \land P(x))$

**Resposta Correta: A**

**Comentário:** A declaração particular negativa ("Algum A não é B") é formalizada usando o quantificador existencial $\exists$ combinado com o conectivo de conjunção $\land$ e a negação no predicado secundário: $\exists x (G(x) \land \neg P(x))$. Lembramos que usar $\rightarrow$ com $\exists$ (Alternativa B) é quase sempre um erro, pois tornaria a sentença verdadeira trivialmente se existisse qualquer objeto no universo que não fosse gato.

---

### Questão 16 (Difícil)

Dadas as regras de unificação na Resolução de Primeira Ordem, qual é o **Mais Geral Unificador (MGU)** entre os dois termos $L_1 = P(x, f(g(z)))$ e $L_2 = P(a, f(y))$?

*(onde $a$ é uma constante, e $x, y, z$ são variáveis)*

A) $\{ x/a, y/g(z) \}$

B) $\{ x/a, y/z \}$

C) $\{ x/a, z/y \}$

D) $\{ x/g(z), y/a \}$

E) Os termos não são unificáveis.

**Resposta Correta: A**

**Comentário:** Para unificar $L_1$ e $L_2$:
1. Igualamos os primeiros argumentos: $x$ com $a \Rightarrow$ Substituição $\{x/a\}$.
2. Igualamos os segundos argumentos: $f(g(z))$ com $f(y)$. Para que os argumentos internos da função $f$ sejam iguais, precisamos que $y = g(z) \Rightarrow$ Substituição $\{y/g(z)\}$.
O MGU completo resultante é a composição dessas substituições: $\{ x/a, y/g(z) \}$.

---

### Questão 17 (Médio - *Pegadinha*)

Qual é a relação de implicação lógica correta entre as sentenças $S_1 = \forall x P(x)$ e $S_2 = \exists x P(x)$, assumindo a convenção padrão da Lógica de Primeira Ordem clássica sobre domínios **não-vazios**?

A) $S_2 \models S_1$, mas $S_1 \not\models S_2$

B) $S_1 \models S_2$, mas $S_2 \not\models S_1$

C) $S_1 \equiv S_2$ (são logicamente equivalentes)

D) Nenhuma implica a outra em hipótese alguma.

E) $S_1 \models \neg S_2$

**Resposta Correta: B**

**Comentário:** *Pegadinha de pressuposição de domínio!* Na Lógica de Primeira Ordem clássica, assume-se rigorosamente que o universo do discurso é **não-vazio** (contém ao menos um elemento). Sob essa premissa, se uma propriedade vale para *todos* os elementos ($\forall x P(x)$), obrigatoriamente ela vale para *pelo menos um* elemento ($\exists x P(x)$). Logo, $S_1 \models S_2$. No entanto, a recíproca é falsa (só porque existe um elemento com a propriedade, não significa que todos a tenham).

---

### Questão 18 (Fácil)

Em Lógica de Primeira Ordem, uma sentença que não possui nenhuma variável livre é denominada:

A) Termo de Skolem

B) Cláusula de Horn

C) Sentença Fechada (ou Proposição)

D) Predicado Aberto

E) Literal Complementar

**Resposta Correta: C**

**Comentário:** Uma fórmula bem-formada que não contém variáveis livres (todas as suas variáveis estão devidamente ligadas por quantificadores) é chamada de **Sentença Fechada** ou simplesmente **Sentença**. Somente sentenças fechadas possuem um valor de verdade bem definido (Verdadeiro ou Falso) sob uma dada interpretação.

---

### Questão 19 (Difícil)

A **Lógica de Primeira Ordem (FOL)** difere da **Lógica de Segunda Ordem (SOL)** principalmente porque a FOL:

A) Não permite o uso de conectivos condicionais como $\rightarrow$.

B) Permite a quantificação apenas sobre indivíduos/objetos do domínio, mas **não** sobre predicados ou relações/funções.

C) Não possui regras de inferência sãs e completas.

D) Permite quantificar conjuntos infinitos de predicados simultaneamente numa mesma variável.

E) Opera apenas com valores de verdade probabilísticos.

**Resposta Correta: B**

**Comentário:** Na Lógica de Primeira Ordem (FOL), os quantificadores $\forall$ e $\exists$ só podem ser aplicados a **variáveis de objetos** (ex: $\forall x (P(x))$). Na Lógica de Segunda Ordem (SOL), é permitido quantificar diretamente sobre **predicados e relações** (ex: $\forall P (P(x) \rightarrow P(y))$ para definir a igualdade de Leibniz).

---

### Questão 20 (Médio - *Pegadinha*)

Seja a fórmula $\phi = \exists x P(x) \land \exists x Q(x)$. Qual das alternativas abaixo apresenta uma interpretação **correta** de $\phi$?

A) Existe pelo menos um mesmo indivíduo $x$ no domínio que satisfaz simultaneamente $P(x)$ e $Q(x)$.

B) Existe um indivíduo que satisfaz $P$ e (não necessariamente o mesmo) indivíduo que satisfaz $Q$.

C) A fórmula é equivalente a $\exists x (P(x) \land Q(x))$.

D) Para todos os indivíduos do domínio, ou $P(x)$ é verdadeiro ou $Q(x)$ é verdadeiro.

E) O quantificador existencial distribui-se perfeitamente sobre a conjunção mantendo a mesma variável.

**Resposta Correta: B**

**Comentário:** *Pegadinha crucial sobre distribuição de quantificadores!*
O quantificador existencial **NÃO se distribui** sobre a conjunção de forma simples: $\exists x (P(x) \land Q(x)) \not\equiv \exists x P(x) \land \exists x Q(x)$.
Na fórmula $\exists x P(x) \land \exists x Q(x)$, os dois quantificadores usam escopos totalmente independentes (é o mesmo que escrever $\exists x P(x) \land \exists y Q(y)$). Isso significa apenas que há alguém que é $P$ e há alguém que é $Q$, mas não garante que seja a **mesma** pessoa.

---

### Questão 21 (Fácil)

Seja a estrutura matemática onde o domínio é o conjunto dos números naturais $\mathbb{N} = \{0, 1, 2, 3, \dots\}$. Qual é o valor de verdade da sentença $\exists x (x + 5 = 2)$?

A) Verdadeiro, com $x = -3$.

B) Falso, pois $-3$ não pertence ao domínio dos números naturais $\mathbb{N}$.

C) Verdadeiro, pois a adição é uma função comutativa.

D) Indeterminado, pois depende da base numérica utilizada.

E) Verdadeiro, se utilizarmos a regra da Instanciação Existencial.

**Resposta Correta: B**

**Comentário:** A solução da equação $x + 5 = 2$ é $x = -3$. No entanto, como o domínio do discurso especificado é $\mathbb{N}$, e $-3 \notin \mathbb{N}$, não existe nenhum elemento no domínio que satisfaça o predicado. Logo, a sentença é **Falsa**.

---

### Questão 22 (Difícil)

O **Teorema da Indecidibilidade de Church-Turing** para a Lógica de Primeira Ordem estabelece que:

A) A Lógica de Primeira Ordem é decidível por algoritmos de tempo exponencial ($EXPTIME$).

B) Não existe um algoritmo geral que possa determinar, para qualquer fórmula arbitrária de Primeira Ordem, se ela é validamente consequência lógica de um conjunto de premissas (a FOL é semidecidível).

C) A Lógica de Primeira Ordem é inconsistente e gera paradoxos em todas as suas interpretações finitas.

D) Todas as fórmulas de Primeira Ordem podem ser reduzidas à Lógica Proposicional em tempo polinomial.

E) Nenhuma fórmula contendo quantificadores universais pode ser provada por computadores.

**Resposta Correta: B**

**Comentário:** Alonzo Church e Alan Turing provaram de forma independente em 1936 que a Lógica de Primeira Ordem é **semidecidível**. Isso significa que se uma fórmula for válida, existe um procedimento/algoritmo (como a Resolução) que eventualmente terminará e provará sua validade; porém, se a fórmula **não** for válida, o algoritmo pode rodar indefinidamente sem nunca parar.

---

### Questão 23 (Médio)

Considere a frase: *"Nenhum cão voa"*. Assinale a formalização correta utilizando $C(x)$: "$x$ é cão" e $V(x)$: "$x$ voa".

A) $\neg \forall x (C(x) \rightarrow V(x))$

B) $\forall x (C(x) \rightarrow \neg V(x))$

C) $\exists x (C(x) \land \neg V(x))$

D) $\forall x (\neg C(x) \rightarrow V(x))$

E) $\exists x (\neg C(x) \land V(x))$

**Resposta Correta: B**

**Comentário:** "Nenhum A é B" é uma declaração universal negativa ("Para todo $x$, se $x$ é cão, então $x$ NÃO voa"): $\forall x (C(x) \rightarrow \neg V(x))$.
Note que isso também é equivalente a dizer "Não existe nenhum $x$ que seja cão E voe": $\neg \exists x (C(x) \land V(x))$. A alternativa A está incorreta pois diz apenas que "nem todos os cães voam" (o que deixaria aberta a possibilidade de alguns voarem).

---

### Questão 24 (Difícil - *Pegadinha*)

Na tentativa de provar a validade do argumento:
1. $\exists x P(x)$
2. Portanto, $P(a)$ para uma constante específica $a$ previamente presente no contexto do problema.

Qual é a falha lógica cometida na aplicação da **Instanciação Existencial**?

A) A Instanciação Existencial só pode ser aplicada se a fórmula contiver também um quantificador universal.

B) Ao instanciar um quantificador existencial $\exists x P(x)$, deve-se introduzir um símbolo de constante **novo** (fresco) que não tenha sido utilizado anteriormente no discurso.

C) A Instanciação Existencial transforma automaticamente a proposição em uma contradição.

D) Não há falha lógica; a inferência é perfeitamente válida na Lógica de Primeira Ordem.

E) A regra exige que a constante $a$ seja substituída por uma função de duas variáveis.

**Resposta Correta: B**

**Comentário:** *Pegadinha de regra de inferência!* Saber que "Existe alguém que é $P$" ($\exists x P(x)$) nos permite dar um nome a essa pessoa (ex: $c$), mas deve ser um **nome/constante totalmente novo** que não traga pressupostos ou propriedades prévias. Se reutilizarmos uma constante $a$ existente sobre a qual já temos informações prévias, estaremos cometendo a falácia de assumir que o indivíduo que possui a propriedade $P$ é exatamente o indivíduo $a$.

---

### Questão 25 (Fácil)

Qual das alternativas descreve a **Forma Normal Prenex** de uma fórmula na Lógica de Primeira Ordem?

A) Uma fórmula composta apenas por conectivos $\land$ e $\lor$, sem nenhuma implicação.

B) Uma fórmula na qual todos os quantificadores aparecem no início da expressão, seguidos por uma parte sem quantificadores (chamada de matriz).

C) Uma fórmula que utiliza unicamente a regra de negação sobre predicados binários.

D) Uma fórmula em que todas as variáveis são livres.

E) Uma negação aplicada exclusivamente a constantes absolutas.

**Resposta Correta: B**

**Comentário:** Uma fórmula está na **Forma Normal Prenex** se ela for escrita na forma $Q_1 x_1 Q_2 x_2 \dots Q_n x_n M$, onde cada $Q_i$ é um quantificador ($\forall$ ou $\exists$) e $M$ é a matriz, uma fórmula que não contém nenhum quantificador.

---

### Questão 26 (Médio)

Considere o universo dos números reais $\mathbb{R}$. Qual é o valor de verdade da sentença $\forall x \forall y (x < y \rightarrow \exists z (x < z \land z < y))$?

A) Falso, pois não existem números reais entre $0$ e $1$.

B) Verdadeiro, pois o conjunto dos números reais é denso (sempre existe um real entre dois reais distintos).

C) Falso, pois se $x$ e $y$ forem inteiros, a propriedade falha.

D) Indeterminado, pois $z$ não está bem definido no escopo de $x$.

E) Verdadeiro apenas para números negativos.

**Resposta Correta: B**

**Comentário:** Esta propriedade expressa formalmente a **densidade** da reta real: dados quaisquer dois números reais $x$ e $y$ com $x < y$, sempre podemos encontrar pelo menos um número real $z$ estritamente entre eles (por exemplo, o ponto médio $z = \frac{x + y}{2}$). Como isso é válido para todo par de reais, a sentença é **Verdadeira**.

---

### Questão 27 (Difícil)

Qual é o resultado do teste de **Occur Check** (Verificação de Ocorrência) ao tentar unificar a variável $x$ com o termo $f(x)$ durante o algoritmo de unificação?

A) Sucesso absoluto, resultando na substituição $\{ x/f(x) \}$.

B) Falha na unificação, pois a variável $x$ ocorre dentro do próprio termo $f(x)$, o que geraria um termo infinito.

C) Sucesso parcial, criando uma constante de Skolem $c$.

D) O teste transforma o termo em uma função de grau $2$.

E) Depende do domínio ser finito ou infinito.

**Resposta Correta: B**

**Comentário:** O **Occur Check** é um passo fundamental no algoritmo de unificação que verifica se a variável $x$ a ser substituída já aparece dentro do termo $T$ com o qual ela está sendo unificada. Se $x$ ocorre dentro de $T$ (como em $x$ e $f(x)$), a unificação deve **falhar**, pois caso contrário criaria uma substituição cíclica infinita ($x = f(f(f(\dots)))$).

---

### Questão 28 (Fácil)

Como se traduz a frase: *"Para todo número $x$, se $x$ é par, então $x+1$ é ímpar"*?

*(Considere $P(x)$: "$x$ é par", $I(x)$: "$x$ é ímpar", e $s(x)$ a função sucessor $x+1$)*

A) $\forall x (P(x) \land I(s(x)))$

B) $\forall x (P(x) \rightarrow I(s(x)))$

C) $\exists x (P(x) \rightarrow I(s(x)))$

D) $\forall x (I(s(x)) \rightarrow P(x))$

E) $\exists x (P(x) \land I(s(x)))$

**Resposta Correta: B**

**Comentário:**
- Quantificador universal para "Para todo número $x$": $\forall x$.
- Estrutura condicional "Se ... então ...": $P(x) \rightarrow I(s(x))$.
Unindo as partes: $\forall x (P(x) \rightarrow I(s(x)))$.

---

### Questão 29 (Médio - *Pegadinha*)

Considere a negação da frase: *"Todos os gatos gostam de leite ou todos os cães gostam de ossos"*. Qual é a formalização correta de sua negação?

*(Considere $G(x)$: "$x$ é gato", $L(x)$: "$x$ gosta de leite", $C(y)$: "$y$ é cão", $O(y)$: "$y$ gosta de ossos")*

A) Existe um gato que não gosta de leite E existe um cão que não gosta de ossos.

B) Nenhum gato gosta de leite E nenhum cão gosta de ossos.

C) Existe um gato que não gosta de leite OU existe um cão que não gosta de ossos.

D) Se um gato não gosta de leite, então nenhum cão gosta de ossos.

E) Todos os gatos não gostam de leite E todos os cães não gostam de ossos.

**Resposta Correta: A**

**Comentário:** *Pegadinha de De Morgan combinada com Quantificadores!*
A frase original é da forma $S_1 \lor S_2$, onde:
- $S_1 = \forall x (G(x) \rightarrow L(x))$
- $S_2 = \forall y (C(y) \rightarrow O(y))$

Negando a disjunção pela lei de De Morgan: $\neg (S_1 \lor S_2) \equiv \neg S_1 \land \neg S_2$.
- $\neg S_1 = \neg \forall x (G(x) \rightarrow L(x)) \equiv \exists x (G(x) \land \neg L(x))$ ("Existe um gato que não gosta de leite").
- $\neg S_2 = \neg \forall y (C(y) \rightarrow O(y)) \equiv \exists y (C(y) \land \neg O(y))$ ("Existe um cão que não gosta de ossos").

Logo, a negação é: $\exists x (G(x) \land \neg L(x)) \land \exists y (C(y) \land \neg O(y))$ (Alternativa A).
Muitos marcam a alternativa B ou C por erro de De Morgan na disjunção ou erro na negação do universal.

---

### Questão 30 (Difícil)

Diz-se que uma teoria de primeira ordem é **Completa** se:

A) Todos os seus modelos têm cardinalidade finita.

B) Para qualquer sentença fechada $\phi$ na linguagem da teoria, ou $\phi$ é demonstrável ($\vdash \phi$) ou sua negação é demonstrável ($\vdash \neg \phi$).

C) Ela não contém nenhum símbolo de função ou constante.

D) O algoritmo de resolução sempre termina em tempo $O(n^2)$.

E) Todas as variáveis livres podem ser eliminadas por skolemização.

**Resposta Correta: B**

**Comentário:** Uma teoria de primeira ordem $T$ é **Completa** se ela é suficientemente rica para decidir o valor de verdade de qualquer sentença fechada expressável em sua linguagem; isto é, para cada sentença $\phi$, $T \vdash \phi$ ou $T \vdash \neg \phi$. (Note: Isso difere da *Completude do Sistema Dedutivo*, que diz que toda fórmula semanticamente válida é dedutível).