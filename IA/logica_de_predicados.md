# Lógica de Predicados
## Conceitos, Definições e Aplicações — Material de Estudo

---

## 1. Conceito Central

**Lógica de predicados** (ou **lógica de primeira ordem**) é uma extensão da **lógica proposicional** que permite expressar afirmações sobre **objetos, suas propriedades e relações entre eles**, usando **variáveis, predicados e quantificadores** — algo que a lógica proposicional, sozinha, não consegue fazer.

> **Definição de prova:** "Enquanto a lógica proposicional trata proposições como blocos indivisíveis (ex.: 'p = Sócrates é mortal'), a lógica de predicados **decompõe** a proposição em um **predicado** aplicado a **argumentos** (ex.: Mortal(Sócrates)), permitindo generalizar afirmações sobre um conjunto de objetos."

⚠️ **Pegadinha clássica de prova:** a lógica proposicional **não consegue representar** o clássico silogismo "Todo homem é mortal; Sócrates é homem; logo, Sócrates é mortal" de forma que a validade seja capturada estruturalmente — é justamente essa limitação que motiva a lógica de predicados.

---

## 2. Elementos Sintáticos Básicos

| Elemento | Definição | Exemplo |
|---|---|---|
| **Constante** | Nome de um objeto específico do domínio | `sócrates`, `3`, `brasil` |
| **Variável** | Representa um objeto genérico/não especificado | `x`, `y`, `z` |
| **Predicado** | Propriedade ou relação aplicada a um ou mais argumentos | `Mortal(x)`, `Amigo(x, y)` |
| **Função** | Mapeia objetos em outros objetos (não é verdadeiro/falso) | `mãe(x)`, `soma(x, y)` |
| **Termo** | Constante, variável, ou função aplicada a termos | `x`, `sócrates`, `mãe(maria)` |
| **Quantificador** | Indica "para quantos" objetos a afirmação vale | `∀` (universal), `∃` (existencial) |
| **Conectivos lógicos** | Mesmos da lógica proposicional | `¬, ∧, ∨, →, ↔` |

⚠️ **Pegadinha:** confundir **predicado** com **função**. Um predicado sempre retorna **verdadeiro ou falso** (ex.: `Mortal(x)`); uma função retorna **um objeto** do domínio (ex.: `mãe(x)` retorna uma pessoa, não um valor lógico).

---

## 3. Quantificadores

### 3.1 Quantificador Universal (∀)
- **∀x P(x)** — "Para todo x, P(x) é verdadeiro."
- É **verdadeiro** se P(x) vale para **todos** os elementos do domínio.

### 3.2 Quantificador Existencial (∃)
- **∃x P(x)** — "Existe pelo menos um x tal que P(x) é verdadeiro."
- É **verdadeiro** se P(x) vale para **pelo menos um** elemento do domínio.

⚠️ **Pegadinha número 1 (muito cobrada):** a **combinação típica** de quantificador com conectivo:
- **∀x (P(x) → Q(x))** — usa-se **implicação (→)** com o universal. Ex.: "Todo cachorro é mamífero" = ∀x (Cachorro(x) → Mamífero(x)).
- **∃x (P(x) ∧ Q(x))** — usa-se **conjunção (∧)** com o existencial. Ex.: "Existe um cachorro que é branco" = ∃x (Cachorro(x) ∧ Branco(x)).

**Por que essa troca é um erro clássico:** se você escrever **∀x (Cachorro(x) ∧ Branco(x))**, estaria afirmando que **todo objeto do domínio é cachorro E é branco** (falso, quase sempre) — completamente diferente da intenção original. E se escrever **∃x (Cachorro(x) → Branco(x))**, a fórmula fica **trivialmente verdadeira** até em domínios sem nenhum cachorro (basta existir algo que não seja cachorro, e a implicação já é verdadeira por vacuidade).

### 3.3 Domínio de Discurso
- Todo quantificador opera sobre um **domínio** (universo de discurso) — o conjunto de todos os objetos possíveis que a variável pode assumir.
- **A mesma fórmula pode ser verdadeira ou falsa dependendo do domínio escolhido.**

⚠️ **Pegadinha:** esquecer de definir/considerar o domínio. Ex.: "∀x (x² ≥ 0)" é verdadeiro se o domínio for os **reais**, mas a interpretação muda completamente se o domínio for os **números complexos**.

---

## 4. Escopo, Variáveis Livres e Ligadas (Bound vs. Free)

- **Variável ligada (bound):** está dentro do escopo de um quantificador que a "captura". Ex.: em `∀x P(x)`, x é ligada.
- **Variável livre (free):** não está sob o escopo de nenhum quantificador — seu valor depende de uma interpretação externa. Ex.: em `P(x) ∧ ∀y Q(y)`, x é livre, y é ligada.
- Uma fórmula **sem variáveis livres** é chamada de **sentença (sentence)** — só sentenças têm valor-verdade bem definido de forma independente.

⚠️ **Pegadinha:** uma fórmula com variável livre **não tem valor-verdade fixo** até que a variável seja substituída ou quantificada — é comum a prova pedir para identificar se uma fórmula é uma sentença ou não.

---

## 5. Negação de Quantificadores (Leis de De Morgan para Predicados)

| Fórmula original | Negação equivalente |
|---|---|
| ¬∀x P(x) | ∃x ¬P(x) |
| ¬∃x P(x) | ∀x ¬P(x) |

> **Regra de prova:** "Negar um universal vira existencial da negação; negar um existencial vira universal da negação." (Análogo às Leis de De Morgan da lógica proposicional, onde ¬(A∧B) ≡ ¬A∨¬B.)

⚠️ **Pegadinha número 1 (extremamente cobrada):** negar **∀x (P(x) → Q(x))** de forma incorreta. A negação correta é:

¬∀x (P(x) → Q(x)) ≡ ∃x ¬(P(x) → Q(x)) ≡ **∃x (P(x) ∧ ¬Q(x))**

(usa-se que ¬(A→B) ≡ A∧¬B). Um erro muito comum é escrever ∃x(¬P(x) → ¬Q(x)) ou ∃x(¬P(x) ∧ ¬Q(x)) — ambos **errados**.

---

## 6. Quantificadores Aninhados (Nested Quantifiers)

Quando há mais de um quantificador na mesma fórmula, a **ordem importa muito**.

| Fórmula | Leitura | Significado |
|---|---|---|
| **∀x ∃y P(x,y)** | Para todo x, existe um y (que pode depender de x) | Cada x pode ter um y diferente |
| **∃y ∀x P(x,y)** | Existe um y (fixo) que serve para todo x | O mesmo y serve para todos os x |

⚠️ **Pegadinha número 1 (a mais clássica de todas em lógica de predicados):** trocar a ordem de `∀∃` por `∃∀` muda completamente o significado.

**Exemplo didático clássico:** "Toda pessoa tem uma mãe."
- ✅ Correto: **∀x ∃y Mãe(y, x)** — para cada pessoa x, existe uma mãe y (cada pessoa tem a sua própria mãe).
- ❌ Errado: **∃y ∀x Mãe(y, x)** — existe uma única pessoa y que é mãe de **todo mundo** (absurdo).

Essa é provavelmente a pegadinha **número 1** em qualquer prova de lógica de predicados — sempre que houver `∀` seguido de `∃`, o valor do existencial **pode variar** em função do universal anterior; se a ordem for invertida, o valor do existencial fica **fixo**.

---

## 7. Regras de Inferência

| Regra | Do que parte | Conclui |
|---|---|---|
| **Instanciação Universal (UI)** | ∀x P(x) | P(c), para qualquer constante c do domínio |
| **Generalização Universal (UG)** | P(c) vale para um c **arbitrário/genérico** | ∀x P(x) |
| **Instanciação Existencial (EI)** | ∃x P(x) | P(c), para **uma nova constante** c (ainda não usada antes) |
| **Generalização Existencial (EG)** | P(c), para algum c específico | ∃x P(x) |

⚠️ **Pegadinha:** na **Instanciação Existencial**, a constante introduzida deve ser **nova** (não usada anteriormente na prova) — se você reaproveitar uma constante já usada, pode introduzir uma conclusão inválida, assumindo implicitamente que dois objetos diferentes são o mesmo.

### 7.1 Exemplo clássico de prova formal (Silogismo de Sócrates)
1. ∀x (Homem(x) → Mortal(x)) — premissa
2. Homem(sócrates) — premissa
3. Homem(sócrates) → Mortal(sócrates) — por UI em (1)
4. Mortal(sócrates) — por Modus Ponens em (2) e (3)

---

## 8. Validade, Satisfatibilidade e Contradição

| Conceito | Definição |
|---|---|
| **Válida (tautologia)** | Verdadeira em **toda** interpretação possível |
| **Satisfatível** | Verdadeira em **pelo menos uma** interpretação |
| **Insatisfatível (contradição)** | Falsa em **toda** interpretação possível |

⚠️ **Pegadinha:** diferente da lógica proposicional (onde dá para checar validade com tabela-verdade finita), na **lógica de predicados de primeira ordem** o problema de validade é, em geral, **indecidível** — não existe um algoritmo garantido que sempre termina e decide se qualquer fórmula é válida ou não (é apenas **semi-decidível**: se for válida, um procedimento pode eventualmente provar isso, mas se não for, o procedimento pode nunca terminar).

---

## 9. Forma Normal Prenex e Skolemização (tópico avançado, comum em cursos de IA/lógica computacional)

- **Forma Normal Prenex:** reescreve a fórmula com **todos os quantificadores no início**, seguidos de uma fórmula sem quantificadores (matriz).
- **Skolemização:** técnica para **eliminar quantificadores existenciais**, substituindo a variável existencial por uma **função de Skolem** que depende das variáveis universais que a precedem (usada para preparar fórmulas para resolução automática, como em Prolog).

⚠️ **Pegadinha:** Skolemização **não preserva equivalência lógica**, apenas **equisatisfatibilidade** (a fórmula skolemizada é satisfatível se e somente se a original for) — isso é frequentemente cobrado como diferença conceitual em provas mais avançadas.

---

## 10. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Conectivo certo para usar com ∀ | Implicação (→) |
| Conectivo certo para usar com ∃ | Conjunção (∧) |
| Negar ∀x P(x) | ∃x ¬P(x) |
| Negar ∃x P(x) | ∀x ¬P(x) |
| Negar ∀x (P(x)→Q(x)) | ∃x (P(x) ∧ ¬Q(x)) |
| Ordem ∀x∃y vs ∃y∀x | No primeiro, y depende de x; no segundo, y é fixo para todos os x |
| Fórmula sem variável livre | Chamada de sentença; tem valor-verdade bem definido |
| Introduzir constante nova numa prova | Instanciação Existencial (constante deve ser nova) |
| Checar validade automaticamente | Em geral indecidível (apenas semi-decidível) em 1ª ordem |
| Eliminar quantificador existencial para automação | Skolemização (preserva equisatisfatibilidade, não equivalência) |

---

## 11. Aplicação Profissional (além da prova)

- **Bancos de dados e SQL:** cláusulas `EXISTS`, `NOT EXISTS`, `ALL`, `ANY` em SQL são, na prática, quantificadores existenciais e universais aplicados a conjuntos de tuplas.
- **Verificação formal de software/hardware:** especificação de propriedades de sistemas (ex.: "para todo estado alcançável, a variável x nunca é negativa") usa diretamente lógica de predicados.
- **Inteligência Artificial simbólica / Prolog:** a linguagem Prolog é baseada em um subconjunto da lógica de predicados (cláusulas de Horn), usando resolução como mecanismo de inferência.
- **Especificação de contratos e regras de negócio:** regras como "todo pedido acima de X precisa de aprovação de um gerente" são naturalmente formalizadas com quantificadores.
- Na prática profissional (ex.: engenharia de requisitos, testes formais), o erro mais comum é justamente o da seção 6 — **inverter a ordem de quantificadores** ao traduzir uma regra de negócio em lógica, gerando uma especificação que não captura a intenção real.

---

## 12. Perguntas típicas de prova (para se testar)

1. Traduza para lógica de predicados: "Todo estudante que estuda passa na prova." Depois traduza a negação dessa afirmação corretamente.

Seja o domínio o conjunto de estudantes, com predicados:
- **E(x)**: "x estuda"
- **P(x)**: "x passa na prova"

**Afirmação original:**

$$\forall x\, (E(x) \rightarrow P(x))$$

**Negação:**

Aplicando a negação de um quantificador universal (que vira existencial) e a negação de uma implicação (¬(A→B) ≡ A ∧ ¬B):

$$\neg \forall x\, (E(x) \rightarrow P(x)) \equiv \exists x\, (E(x) \wedge \neg P(x))$$

Ou seja: **"Existe pelo menos um estudante que estuda e não passa na prova."**

> ⚠️ Um erro comum é negar apenas o predicado interno, produzindo algo como `∀x(E(x) → ¬P(x))` ("todo estudante que estuda não passa"), o que está **incorreto** — essa não é a negação lógica da afirmação original.

---
   
2. Explique, com um exemplo, por que ∀x∃y P(x,y) e ∃y∀x P(x,y) não são logicamente equivalentes.

- **∀x∃y P(x,y)**: "Para todo x, existe (pelo menos um) y tal que P(x,y)" — o y pode **depender de x** (cada x pode ter seu próprio y).
- **∃y∀x P(x,y)**: "Existe um y tal que, para todo x, P(x,y)" — o **mesmo y** deve servir para todos os x.

### Exemplo

Seja `P(x,y)`: "y é maior que x", no domínio dos números naturais.

| Fórmula | Leitura | Valor-verdade |
|---|---|---|
| ∀x∃y P(x,y) | Para todo número x, existe um número y maior que ele | **Verdadeiro** (basta tomar y = x+1) |
| ∃y∀x P(x,y) | Existe um número y que é maior que todos os números x | **Falso** (não existe maior número natural) |

Isso mostra que a **ordem dos quantificadores importa**: trocar ∀∃ por ∃∀ pode transformar uma afirmação verdadeira em falsa.

---
   
3. Qual conectivo lógico normalmente acompanha o quantificador universal e qual acompanha o existencial? Por que trocá-los produz fórmulas com significado indesejado?

- O **quantificador universal (∀)** normalmente acompanha o **condicional (→)**:
  `∀x (P(x) → Q(x))` — "para todo x, se P(x) então Q(x)".
- O **quantificador existencial (∃)** normalmente acompanha a **conjunção (∧)**:
  `∃x (P(x) ∧ Q(x))` — "existe x tal que P(x) e Q(x)".

### Por que trocá-los produz significado indesejado

- Usar `∀x (P(x) ∧ Q(x))` no lugar de "todo P é Q" exige que **todos os elementos do domínio** satisfaçam P e Q simultaneamente — não apenas os que satisfazem P. Isso é uma afirmação muito mais forte (e geralmente falsa).
- Usar `∃x (P(x) → Q(x))` no lugar de "existe x tal que P(x) e Q(x)" torna a fórmula **quase trivialmente verdadeira**: basta um x onde P(x) seja falso para a implicação ser verdadeira por vacuidade (F → qualquer coisa = V), mesmo sem relação real entre P e Q.

---

4. O que diferencia uma variável livre de uma variável ligada? Por que uma fórmula com variável livre não é considerada uma sentença?

- **Variável ligada**: está no escopo de um quantificador (∀ ou ∃) que a vincula.
  *Ex.:* em `∀x P(x,y)`, x é ligada.
- **Variável livre**: não está sob o escopo de nenhum quantificador.
  *Ex.:* em `∀x P(x,y)`, y é livre.

### Por que uma fórmula com variável livre não é uma sentença

Uma sentença (fórmula fechada) deve ter um **valor de verdade definido**, sem depender de interpretação externa. Uma fórmula com variável livre, como `P(x,y)` sem quantificação de y, não tem valor de verdade fixo: depende de **qual valor é atribuído a y**. Ela é uma *função proposicional* (um "molde" para sentenças), não uma proposição completa. Só se torna sentença quando todas as variáveis são ligadas por quantificadores ou substituídas por constantes específicas.

---
   
5. Por que o problema de validade na lógica de predicados de primeira ordem é indecidível (e não apenas "difícil")?

O problema é **indecidível** (não apenas difícil computacionalmente) porque, pelo **Teorema de Church-Turing (1936)**, não existe algoritmo que, para toda fórmula de primeira ordem, sempre termine e decida corretamente se ela é válida ou não.

**Motivo estrutural:** a lógica de primeira ordem é **semidecidível**:
- Se uma fórmula **é válida**, um procedimento de prova (como resolução) eventualmente a comprovará em tempo finito.
- Se a fórmula **não é válida**, não há garantia de que o procedimento pare; pode rodar indefinidamente sem nunca concluir "não é válida".

Isso decorre da capacidade da lógica de primeira ordem de codificar o **problema da parada** (halting problem) e a aritmética de Peano, ambos indecidíveis.

> Diferente de um problema "difícil" (como NP-completo, que é decidível mas com alto custo computacional), aqui **nenhum algoritmo, por mais tempo que rode, garante resposta em todos os casos**.

---
   
6. O que é uma constante de Skolem e por que a skolemização preserva apenas equisatisfatibilidade, não equivalência lógica?

Uma **constante de Skolem** (ou, de forma mais geral, **função de Skolem**) é um novo símbolo introduzido para **eliminar quantificadores existenciais** de uma fórmula, substituindo a variável existencialmente quantificada por um termo (constante ou função) que "testemunha" essa existência.

**Exemplo:**

`∀x∃y P(x,y)` é skolemizado para `∀x P(x, f(x))`, onde `f` é uma nova função de Skolem que, para cada x, fornece o y que satisfaz P.

### Por que preserva apenas equisatisfatibilidade, não equivalência lógica

A fórmula skolemizada **não é logicamente equivalente** à original, pois introduz um símbolo novo (`f` ou `c`) que não existia na linguagem original — as duas fórmulas nem sequer estão na mesma assinatura/linguagem.

O que se preserva é a **equisatisfatibilidade**: a fórmula original é satisfazível **se e somente se** a fórmula skolemizada é satisfazível. Isso é suficiente para fins práticos (prova automática de teoremas, resolução), pois o que importa é verificar se um conjunto de fórmulas é consistente — não preservar exatamente o mesmo conjunto de modelos. A skolemização "testemunha" a existência sem afirmar que a nova função é *a mesma* relação implícita no `∃y` original; apenas garante que, se existe alguma função que satisfaz a relação, podemos nomeá-la e trabalhar com ela.

