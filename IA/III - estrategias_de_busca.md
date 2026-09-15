# Estratégias de Busca em IA
## Busca sem Informação (Cega) e Busca Informada (Heurística) — Material de Estudo

---

## 1. Conceito Central

**Busca** é a técnica fundamental de IA para resolver problemas que podem ser formulados como a exploração de um **espaço de estados**, buscando um caminho de um **estado inicial** até um **estado objetivo**.

> **Definição de prova:** "Um problema de busca é definido pela tupla (Estado inicial, Ações, Modelo de transição, Teste de objetivo, Custo de caminho). O algoritmo de busca explora esse espaço, expandindo nós até encontrar (ou provar que não existe) uma solução."

**Duas grandes famílias:**
| Família | O que usa para decidir qual nó expandir | Exemplos |
|---|---|---|
| **Busca sem informação (cega/blind)** | Apenas a estrutura do problema — não sabe "a que distância" está do objetivo | BFS, DFS, Custo Uniforme, Aprofundamento Iterativo |
| **Busca informada (heurística)** | Uma **função heurística** h(n) que estima o custo até o objetivo | Gulosa (Greedy), A*, IDA* |

⚠️ **Pegadinha clássica de prova:** "sem informação" **não significa** que o algoritmo não sabe nada sobre o problema — ele conhece as ações e transições possíveis; o que falta é **qualquer estimativa de quão perto está do objetivo**.

---

## 2. Vocabulário Fundamental

| Termo | Definição |
|---|---|
| **Estado** | Uma configuração/situação possível do problema |
| **Nó (node)** | Estrutura de dados que representa um estado na árvore de busca (contém estado, nó-pai, ação, custo do caminho, profundidade) |
| **Fronteira (frontier / open list)** | Conjunto de nós gerados, mas ainda não expandidos |
| **Conjunto explorado (explored set / closed list)** | Nós já expandidos, usados para evitar reexpansão (busca em grafo) |
| **Fator de ramificação (b)** | Número médio de sucessores de cada nó |
| **Profundidade da solução (d)** | Número de passos do estado inicial até o objetivo mais raso |
| **Custo de caminho g(n)** | Custo acumulado do estado inicial até o nó n |

⚠️ **Pegadinha:** confundir **árvore de busca** com **espaço de estados**. O espaço de estados pode ter ciclos/repetições; a árvore de busca é a estrutura gerada pelo algoritmo ao explorar esse espaço (podendo gerar o mesmo estado várias vezes se não houver controle de repetição — daí a diferença entre **busca em árvore** e **busca em grafo**).

---

## 3. Propriedades de Avaliação de Algoritmos de Busca

Toda prova pede para classificar um algoritmo segundo essas 4 propriedades:

| Propriedade | Pergunta que responde |
|---|---|
| **Completude** | O algoritmo **garante encontrar uma solução**, se ela existir? |
| **Otimalidade** | O algoritmo encontra a **solução de menor custo**? |
| **Complexidade de tempo** | Quantos nós são gerados/expandidos, no pior caso? |
| **Complexidade de espaço** | Quantos nós precisam ser mantidos em memória, no pior caso? |

⚠️ **Pegadinha:** **completo ≠ ótimo**. Um algoritmo pode ser completo (sempre acha *uma* solução) mas não ótimo (não garante que seja a *melhor* solução) — é exatamente o caso da Busca em Largura (BFS) em problemas com custos de passo diferentes.

---

## 4. Busca Sem Informação (Cega)

### 4.1 Busca em Largura — BFS (Breadth-First Search)
- Expande os nós **nível a nível** (mais rasos primeiro), usando uma **fila FIFO** como fronteira.
- **Completa:** sim (se b for finito).
- **Ótima:** sim, **somente se todos os custos de passo forem iguais** (senão, encontra o caminho com menos passos, não o de menor custo).
- **Complexidade de tempo e espaço:** O(b^d) — cresce exponencialmente, e o **espaço é o maior problema prático** do BFS (guarda toda a fronteira, que cresce exponencialmente).

⚠️ **Pegadinha número 1 (muito cobrada):** achar que BFS sempre encontra o **caminho de menor custo**. Isso só é verdade se **todos os custos de aresta forem iguais** (ex.: 1 por passo). Se os custos variarem, BFS pode retornar um caminho com menos passos, mas custo total maior.

### 4.2 Busca em Profundidade — DFS (Depth-First Search)
- Expande sempre o **nó mais profundo** primeiro, usando uma **pilha LIFO** (ou recursão) como fronteira.
- **Completa:** **não**, em espaços de estados infinitos ou com ciclos (pode ficar "preso" descendo um ramo infinito) — **é completa em espaços finitos com controle de repetição de estados**.
- **Ótima:** não.
- **Complexidade de tempo:** O(b^m), onde m é a profundidade máxima (pode ser muito pior que BFS se m >> d).
- **Complexidade de espaço:** O(b·m) — **grande vantagem sobre BFS**, pois só guarda um caminho por vez (linear, não exponencial).

⚠️ **Pegadinha número 1:** a vantagem clássica do DFS sobre o BFS é justamente a **economia de memória** (espaço linear vs. exponencial) — mas isso vem ao custo de **perder completude e otimalidade** em muitos cenários.

### 4.3 Busca de Custo Uniforme — UCS (Uniform Cost Search)
- Expande sempre o nó com **menor custo de caminho acumulado g(n)**, usando uma **fila de prioridade**.
- Equivalente ao **algoritmo de Dijkstra** aplicado à busca.
- **Completa:** sim (se os custos forem ≥ um valor positivo ε).
- **Ótima:** sim, sempre (mesmo com custos de passo diferentes) — essa é a principal vantagem sobre o BFS.
- **Complexidade:** depende do custo da solução ótima C* e do menor custo de aresta ε: O(b^(C*/ε)).

⚠️ **Pegadinha:** UCS **generaliza** o BFS — quando todos os custos são iguais a 1, UCS se comporta exatamente como BFS. Isso costuma ser cobrado como pergunta de "qual a relação entre BFS e UCS?".

### 4.4 Busca em Profundidade Limitada (Depth-Limited Search)
- Igual ao DFS, mas com um **limite de profundidade L** — nós além de L não são expandidos.
- Resolve o problema de "ficar preso" em ramos infinitos, mas **introduz incompletude** se L for menor que a profundidade real da solução.

### 4.5 Aprofundamento Iterativo — IDS (Iterative Deepening Search)
- Executa **DFS com limite de profundidade crescente** (L = 0, 1, 2, 3, ...), repetindo a busca a cada iteração até encontrar a solução.
- **Combina o melhor dos dois mundos:** a eficiência de memória do DFS (O(b·d)) com a completude e otimalidade do BFS (quando custos são uniformes).
- **Complexidade de tempo:** O(b^d) — parece haver desperdício por reexpandir os nós superiores repetidamente, mas o custo extra é **assintoticamente pequeno**, pois a maior parte dos nós está nas camadas mais profundas.

⚠️ **Pegadinha número 1 (super cobrada):** alunos acham que reexpandir os níveis superiores repetidamente torna o IDS **ineficiente**. Na prática, o custo adicional é **desprezível** — a maioria dos nós de uma árvore de fator de ramificação b está concentrada nas camadas mais profundas, então repetir as camadas rasas tem baixo impacto no total.

⚠️ **Pegadinha número 2:** o IDS é frequentemente citado como a **estratégia sem informação preferida** quando o espaço de busca é grande e a profundidade da solução é desconhecida — por unir baixa exigência de memória com garantias de completude/otimalidade.

### 4.6 Busca Bidirecional
- Executa **duas buscas simultâneas**: uma a partir do estado inicial (para frente) e outra a partir do objetivo (para trás), parando quando as duas fronteiras se encontram.
- Pode reduzir drasticamente a complexidade de tempo: de O(b^d) para **O(b^(d/2))**.

⚠️ **Pegadinha:** busca bidirecional exige que a busca "de trás para frente" seja possível — ou seja, que se consiga **gerar predecessores** a partir do objetivo, o que nem sempre é trivial ou até possível (ex.: quando há múltiplos objetivos ou o objetivo não é único e explícito).

---

## 5. Quadro Comparativo — Busca Sem Informação

| Algoritmo | Completa? | Ótima? | Tempo | Espaço |
|---|---|---|---|---|
| **BFS** | Sim | Só com custos uniformes | O(b^d) | O(b^d) |
| **DFS** | Não (espaços infinitos) | Não | O(b^m) | O(b·m) |
| **Custo Uniforme (UCS)** | Sim | Sim | O(b^(C*/ε)) | O(b^(C*/ε)) |
| **Profundidade Limitada** | Não (se L < d) | Não | O(b^L) | O(b·L) |
| **Aprofundamento Iterativo (IDS)** | Sim | Só com custos uniformes | O(b^d) | O(b·d) |
| **Bidirecional** | Sim | Sim (em condições específicas) | O(b^(d/2)) | O(b^(d/2)) |

---

## 6. Busca Informada (Heurística)

### 6.1 Função Heurística h(n)
- **h(n)** estima o **custo do caminho mais barato de n até o objetivo**.
- Deve ser calculada de forma **barata computacionalmente** (senão perde-se a vantagem de usá-la).
- **h(objetivo) = 0** sempre.

**Exemplo clássico:** no problema do 8-puzzle, heurísticas comuns são:
- **h1** = número de peças fora do lugar.
- **h2** = soma das distâncias Manhattan de cada peça até sua posição correta.

⚠️ **Pegadinha:** entre h1 e h2 acima, **h2 domina h1** (h2(n) ≥ h1(n) para todo n) — ou seja, h2 é uma heurística **mais informada**, o que geralmente leva a menos nós expandidos pelo A*, mesmo que cada cálculo de h2 seja um pouco mais custoso.

### 6.2 Busca Gulosa — Greedy Best-First Search
- Expande sempre o nó que **parece mais próximo do objetivo**, usando apenas f(n) = h(n) (ignora o custo já percorrido).
- **Completa:** não, em geral (pode entrar em loop em espaços com ciclos, ou ficar presa em ramos infinitos).
- **Ótima:** **não** — pode ser "enganada" pela heurística e seguir um caminho que parece bom localmente, mas é caro globalmente.
- **Complexidade:** O(b^m) no pior caso, mas uma boa heurística pode reduzir drasticamente na prática.

⚠️ **Pegadinha:** Busca Gulosa é **míope** — ela só olha "quão perto parece estar do objetivo" (h(n)), **ignorando completamente o custo já gasto** (g(n)) para chegar até ali. Isso é o que a diferencia do A* e é a causa raiz de sua não-otimalidade.

### 6.3 A* (A-estrela)
- Combina **g(n)** (custo já percorrido) e **h(n)** (estimativa até o objetivo): **f(n) = g(n) + h(n)**.
- Expande sempre o nó com **menor f(n)**.
- É o algoritmo de busca informada mais importante e mais cobrado em prova.

**Condições de otimalidade (a parte mais cobrada de toda a matéria de busca):**

| Tipo de heurística | Definição | Garante otimalidade em... |
|---|---|---|
| **Admissível** | h(n) **nunca superestima** o custo real até o objetivo: h(n) ≤ h*(n) | Busca em **árvore** (tree search, sem closed list) |
| **Consistente (monotônica)** | Para todo nó n e sucessor n' via ação a: h(n) ≤ c(n,a,n') + h(n') | Busca em **grafo** (graph search, com closed list) |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a unidade de busca):** confundir **admissibilidade** com **consistência**.
- **Toda heurística consistente é admissível**, mas **nem toda heurística admissível é consistente**.
- Para a **busca em árvore**, basta que h(n) seja **admissível** para o A* ser ótimo.
- Para a **busca em grafo** (que evita reexpandir estados, usando conjunto explorado), é necessário que h(n) seja **consistente** — caso contrário, o A* pode descartar um caminho melhor para um estado já visitado e retornar uma solução subótima.

⚠️ **Pegadinha número 2:** heurística h(n) = 0 para todo n é **sempre admissível e consistente** (trivialmente) — nesse caso, **A* se reduz exatamente ao UCS** (Custo Uniforme). Essa é uma pergunta clássica de prova: "o que acontece com o A* se h(n) = 0?".

⚠️ **Pegadinha número 3:** uma heurística que **superestima** o custo real em algum nó (viola admissibilidade) pode fazer o A* encontrar uma solução **subótima** — mesmo que na maioria dos nós ela seja uma boa estimativa.

### 6.4 IDA* (Iterative Deepening A*)
- Aplica a ideia do **aprofundamento iterativo** ao A*: em vez de limitar por profundidade, limita por um **valor de corte em f(n)**, que aumenta a cada iteração.
- Vantagem: mantém a **otimalidade do A*** com a **eficiência de memória do DFS** (O(b·d) em vez de exponencial).
- Muito usado quando o espaço de busca é grande demais para caber a fronteira inteira do A* em memória.

⚠️ **Pegadinha:** o principal motivo de usar IDA* no lugar do A* é a **limitação de memória** do A* tradicional (que guarda todos os nós gerados na fronteira) — não uma questão de velocidade pura, mas de **viabilidade prática** em problemas grandes.

---

## 7. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Algoritmo sem informação ótimo e completo, com espaço exponencial | Busca em Largura (BFS) — só ótima se custos uniformes |
| Algoritmo sem informação com pouco uso de memória, mas incompleto | DFS |
| Une baixa memória do DFS + completude/otimalidade do BFS | Aprofundamento Iterativo (IDS) |
| Generalização do BFS para custos variados | Busca de Custo Uniforme (UCS) — equivale ao Dijkstra |
| Heurística que nunca superestima | Admissível → garante otimalidade em busca em árvore |
| Heurística com a condição do "triângulo" c(n,a,n') | Consistente → garante otimalidade em busca em grafo |
| A* com h(n) = 0 | Vira exatamente o UCS |
| Algoritmo guloso e míope, ignora custo já gasto | Greedy Best-First Search (usa só h(n)) |
| A* com pouca memória disponível | IDA* |
| Heurística h2 domina h1 | h2 é mais informada, A* expande menos nós com h2 |
| Reduzir complexidade de O(b^d) para O(b^(d/2)) | Busca Bidirecional |

---

## 8. Aplicação Profissional (além da prova)

- **Roteamento e GPS/mapas:** A* é amplamente usado para encontrar a rota mais curta/rápida, com heurística baseada em distância em linha reta (euclidiana) até o destino.
- **Jogos e pathfinding (games):** A* é o algoritmo padrão para movimentação de personagens/NPCs em grades e grafos de navegação.
- **Planejamento em robótica:** busca informada para planejamento de trajetórias, evitando obstáculos.
- **Redes de computadores:** UCS/Dijkstra é a base de protocolos de roteamento que buscam o caminho de menor custo (latência, número de saltos).
- **Resolução automática de quebra-cabeças** (8-puzzle, Rubik's Cube): A* e IDA* com heurísticas específicas do domínio (distância Manhattan, padrões de banco de dados/pattern databases).
- Na prática profissional, o maior desafio de projetar um sistema de busca informada é **desenhar uma boa heurística** — uma heurística fraca (pouco informada) faz o A* se comportar quase como o UCS (explorando muitos nós desnecessários), enquanto uma heurística mal projetada (não admissível) pode retornar soluções erradas sem nenhum aviso explícito.

---

## 9. Perguntas típicas de prova (para se testar)

1. Por que a Busca em Largura (BFS) não é ótima quando os custos das arestas são diferentes? Dê um contraexemplo.

   A BFS expande os nós em ordem de **profundidade** (número de arestas), não em ordem de **custo acumulado**. Ela encontra o caminho com **menor número de passos**, mas isso não é necessariamente o caminho de **menor custo total** quando as arestas têm pesos diferentes.

**Contraexemplo:**

```
        A
      /   \
   (1)     (10)
    /         \
   B           C
    \         /
   (10)     (1)
      \     /
        D
```

- Caminho A → C → D: 2 arestas, custo total = 10 + 1 = **11**
- Caminho A → B → D: 2 arestas, custo total = 1 + 10 = **11**

Agora, considere um caminho alternativo mais longo em número de arestas, mas mais barato:

```
A --(1)--> B --(1)--> E --(1)--> D
```

- Caminho A → B → E → D: 3 arestas, custo total = 1 + 1 + 1 = **3**

A BFS, por explorar por camadas (nível de profundidade), encontraria primeiro um caminho de **2 arestas** (A→C→D ou A→B→D, custo 11) e o retornaria como solução, **ignorando** o caminho de 3 arestas com custo total 3, que é o realmente ótimo. Isso prova que BFS otimiza número de passos, não custo — para isso seria necessário usar **Busca de Custo Uniforme (UCS)**.
   
2. Explique por que o Aprofundamento Iterativo (IDS) não é tão ineficiente quanto parece, apesar de reexpandir os nós das camadas superiores repetidamente.
5. Qual a diferença entre uma heurística admissível e uma heurística consistente? Por que a busca em grafo do A* exige consistência para garantir otimalidade?
6. O que acontece com o algoritmo A* se a heurística usada for h(n) = 0 para todo n?
7. Por que a Busca Gulosa (Greedy Best-First) não é ótima, mesmo usando uma heurística admissível?
8. Por que o IDA* é preferido ao A* tradicional em problemas com espaço de busca muito grande?
