# Estruturas de Dados
## Vetor, Matriz, Pilha, Fila, Listas, Heap, Árvores e Tabela Hash — Material de Estudo

---

## 1. Conceito Central

**Estrutura de dados** é uma forma organizada de armazenar e acessar dados, escolhida de acordo com as **operações mais frequentes** que o problema exige (busca, inserção, remoção, ordenação, acesso por posição).

> **Definição de prova:** "Não existe 'a melhor estrutura de dados' de forma absoluta — existe a estrutura mais adequada para o **padrão de uso** do problema. A escolha errada de estrutura pode transformar um algoritmo O(n log n) em O(n²) na prática, mesmo mantendo a lógica do algoritmo idêntica."

⚠️ **Pegadinha clássica de prova:** achar que a complexidade de uma estrutura de dados é uma propriedade **fixa e única**. Quase toda estrutura tem complexidades **diferentes para operações diferentes** (acesso, busca, inserção, remoção) e, em muitos casos, **diferentes no melhor, médio e pior caso** — a resposta correta em prova quase sempre depende de **qual operação** e **qual cenário** estão sendo perguntados.

---

## 2. Vetor / Array

### 2.1 Características
- Estrutura de **memória contígua**, com acesso direto por índice.
- **Array estático:** tamanho fixo definido na criação.
- **Array dinâmico** (ex.: `ArrayList` em Java, `list` em Python, `vector` em C++): cresce automaticamente, geralmente **dobrando de tamanho** quando a capacidade é excedida.

### 2.2 Complexidades
| Operação | Complexidade | Observação |
|---|---|---|
| Acesso por índice | O(1) | Acesso direto via endereço de memória |
| Busca (valor desconhecido a posição) | O(n) | Busca linear, sem informação de ordem |
| Inserção/remoção no **final** | O(1) amortizado (array dinâmico) | Ver seção 2.3 |
| Inserção/remoção no **início/meio** | O(n) | Exige deslocar todos os elementos seguintes |

### 2.3 Complexidade amortizada do array dinâmico
- Quando o array dinâmico atinge sua capacidade, ele **realoca um novo array maior** (geralmente o dobro) e copia todos os elementos — uma operação O(n) isolada.

⚠️ **Pegadinha número 1 (muito cobrada):** achar que **toda inserção no final** de um array dinâmico é O(1). Na verdade, é O(1) **amortizado**: a maioria das inserções é O(1), mas ocasionalmente ocorre uma realocação O(n). A **estratégia de dobrar a capacidade** (em vez de crescer um espaço fixo por vez) é justamente o que garante que o **custo médio por operação**, ao longo de muitas inserções, permaneça O(1).

---

## 3. Matriz (Array Multidimensional)

- Extensão do array para múltiplas dimensões; internamente, ainda é armazenada em um bloco de memória contígua (na maioria das linguagens), seguindo uma ordem: **row-major** (linha por linha — C, Python/NumPy) ou **column-major** (coluna por coluna — Fortran, MATLAB).

⚠️ **Pegadinha:** percorrer uma matriz na **ordem errada** em relação à forma como ela é armazenada na memória (ex.: percorrer por colunas em uma linguagem row-major) causa **acessos de memória não-sequenciais**, prejudicando o desempenho por má utilização do cache — mesmo que a complexidade assintótica O(n²) permaneça a mesma, o desempenho real pode ser significativamente pior.

- **Matrizes esparsas** (majoritariamente zeros) são frequentemente representadas com estruturas especializadas (listas de coordenadas, CSR/CSC), evitando desperdiçar memória com os zeros — relevante em sistemas lineares esparsos (ver material de Métodos Numéricos).

---

## 4. Pilha (Stack) — LIFO

### 4.1 Definição
- **LIFO (Last In, First Out):** o último elemento inserido é o primeiro a ser removido.
- Operações principais: **push** (inserir no topo), **pop** (remover do topo), **peek/top** (consultar o topo sem remover).

### 4.2 Complexidades
| Operação | Complexidade |
|---|---|
| push | O(1) |
| pop | O(1) |
| peek | O(1) |
| busca por valor | O(n) |

### 4.3 Aplicações clássicas
- **Pilha de chamadas (call stack)** em recursão.
- **Desfazer/refazer (undo/redo)** em editores.
- **Avaliação de expressões** (conversão infixa → pós-fixa, verificação de parênteses balanceados).
- **Backtracking** (busca em profundidade usa implicitamente uma pilha, seja via recursão ou explicitamente).

⚠️ **Pegadinha:** a **recursão** é, na prática, uma pilha implícita gerenciada pelo próprio ambiente de execução — por isso, recursões muito profundas podem causar **estouro de pilha (stack overflow)**, um problema diretamente relacionado à estrutura de dados pilha, não apenas um "erro de lógica" do código.

---

## 5. Fila (Queue) — FIFO

### 5.1 Definição
- **FIFO (First In, First Out):** o primeiro elemento inserido é o primeiro a ser removido.
- Operações principais: **enqueue** (inserir no final), **dequeue** (remover do início).

### 5.2 Complexidades (e a pegadinha central desta seção)
| Implementação | enqueue | dequeue |
|---|---|---|
| Array simples (sem controle circular) | O(1) | **O(n)** — exige deslocar todos os elementos restantes |
| Buffer circular (circular array) | O(1) | O(1) |
| Lista encadeada (com ponteiro para início e fim) | O(1) | O(1) |

⚠️ **Pegadinha número 1 (muito cobrada):** achar que **toda implementação de fila** tem dequeue O(1). Se a fila for implementada de forma ingênua sobre um array (removendo o primeiro elemento e deslocando todos os demais uma posição para trás), o dequeue é **O(n)**. Implementações eficientes usam **buffer circular** ou **lista encadeada** para garantir O(1) em ambas as operações.

### 5.3 Variações
- **Deque (double-ended queue):** permite inserção/remoção em **ambas as extremidades**, em O(1).
- **Fila de prioridade (priority queue):** cada elemento tem uma prioridade, e a remoção sempre retorna o elemento de **maior (ou menor) prioridade**, não necessariamente o mais antigo — geralmente implementada com um **heap** (ver seção 7).

⚠️ **Pegadinha:** fila de prioridade **não é FIFO** — é fácil confundir pelo nome "fila", mas sua ordem de saída depende da **prioridade**, não da ordem de chegada.

### 5.4 Aplicação clássica
- **Busca em Largura (BFS)** em grafos/árvores usa fila; **Busca em Profundidade (DFS)** usa pilha (ver material de Estratégias de Busca).

---

## 6. Listas Encadeadas (Linked Lists)

### 6.1 Tipos
| Tipo | Estrutura |
|---|---|
| **Lista simplesmente encadeada** | Cada nó aponta apenas para o **próximo** |
| **Lista duplamente encadeada** | Cada nó aponta para o **próximo e o anterior** |
| **Lista circular** | O último nó aponta de volta para o primeiro |

### 6.2 Complexidades
| Operação | Complexidade |
|---|---|
| Acesso por índice/posição | O(n) — precisa percorrer a partir do início |
| Busca por valor | O(n) |
| Inserção/remoção **no início** | O(1) |
| Inserção/remoção **em posição conhecida** (com ponteiro já em mãos) | O(1) |
| Inserção/remoção **em posição arbitrária (por índice, sem ponteiro)** | O(n) — precisa percorrer até a posição |

⚠️ **Pegadinha número 1 (a mais cobrada desta seção):** comparar lista encadeada com array afirmando genericamente que "lista encadeada é sempre melhor para inserção/remoção". Isso só é verdade quando **já se tem o ponteiro/referência para a posição de inserção** — se for preciso **primeiro encontrar** a posição (por índice ou valor), o custo de busca O(n) da lista **anula** a vantagem, tornando o custo total comparável (ou pior) ao de um array.

⚠️ **Pegadinha número 2:** diferente do array, a lista encadeada **não tem acesso aleatório O(1)** — acessar o elemento na posição k sempre exige percorrer os k nós anteriores, mesmo em uma lista duplamente encadeada (a menos que se comece a busca a partir do fim, quando k está mais próximo do final).

### 6.3 Trade-off central Array vs. Lista Encadeada
| Critério | Array | Lista Encadeada |
|---|---|---|
| Acesso por índice | O(1) | O(n) |
| Inserção/remoção no meio (posição conhecida) | O(n) (desloca elementos) | O(1) |
| Uso de memória | Contígua, sem overhead de ponteiros | Overhead extra de ponteiros por nó |
| Localidade de cache | Melhor (dados contíguos) | Pior (nós espalhados na memória) |

---

## 7. Heap (Min-Heap / Max-Heap)

### 7.1 Definição
- **Árvore binária completa** (todos os níveis preenchidos, exceto possivelmente o último, preenchido da esquerda para a direita) que satisfaz a **propriedade de heap**:
  - **Min-heap:** todo nó pai é **menor ou igual** a seus filhos.
  - **Max-heap:** todo nó pai é **maior ou igual** a seus filhos.
- Geralmente implementado sobre um **array** (sem necessidade de ponteiros), usando aritmética de índices para navegar entre pai e filhos.

### 7.2 Complexidades
| Operação | Complexidade |
|---|---|
| Consultar o mínimo/máximo (topo) | O(1) |
| Inserir elemento | O(log n) |
| Remover o topo (extract-min/max) | O(log n) |
| Construir heap a partir de n elementos (build-heap) | O(n) — não O(n log n)! |
| **Busca por um valor arbitrário** | O(n) |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a seção de heap):** achar que um **heap é uma árvore de busca binária (BST)** e que, portanto, buscar um valor arbitrário nele é O(log n). **Isso é falso.** O heap garante **apenas a relação entre pai e filho** (pai ≤ filhos, no min-heap) — não existe garantia de ordem entre **irmãos** ou entre **subárvores diferentes**. Por isso, buscar um valor qualquer (que não seja o topo) exige, no pior caso, **percorrer toda a estrutura: O(n)**.

⚠️ **Pegadinha número 2:** a construção de um heap a partir de n elementos desordenados (**build-heap**, usando o algoritmo bottom-up de "heapify") tem complexidade **O(n)**, e não O(n log n) como uma análise ingênua (n inserções de O(log n) cada) sugeriria — esse é um resultado clássico de análise amortizada, muito cobrado em prova.

### 7.3 Aplicações
- Implementação de **fila de prioridade**.
- **Heap Sort** (algoritmo de ordenação O(n log n), in-place).
- Algoritmos de grafos como **Dijkstra** (menor caminho) e **Prim** (árvore geradora mínima), que usam fila de prioridade internamente.

---

## 8. Árvores

### 8.1 Árvore Binária de Busca (BST — Binary Search Tree)
- Estrutura em que, para cada nó, **todos os valores da subárvore esquerda são menores**, e **todos os valores da subárvore direita são maiores** (assumindo valores únicos).

### 8.2 Complexidades — a pegadinha central da seção
| Operação | Caso médio (árvore balanceada) | Pior caso (árvore degenerada) |
|---|---|---|
| Busca | O(log n) | **O(n)** |
| Inserção | O(log n) | **O(n)** |
| Remoção | O(log n) | **O(n)** |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a unidade de estruturas de dados):** afirmar categoricamente que uma **BST tem complexidade O(log n)**. Isso só é verdade se a árvore estiver **razoavelmente balanceada**. Se os elementos forem inseridos em **ordem crescente (ou decrescente)** em uma BST comum (sem balanceamento automático), a árvore **degenera em uma lista encadeada disfarçada**, e todas as operações passam a ser **O(n)** no pior caso.

### 8.3 Árvores Balanceadas (AVL, Red-Black) — a solução para o problema acima
- **Árvores auto-balanceadas** aplicam **rotações** durante inserção/remoção para manter a altura da árvore em **O(log n)**, garantindo essa complexidade mesmo no **pior caso**.

| Tipo | Característica | Trade-off |
|---|---|---|
| **AVL** | Balanceamento **mais rígido** (diferença de altura entre subárvores ≤ 1) | Buscas mais rápidas (árvore mais "baixa"), porém **mais rotações** em inserção/remoção |
| **Red-Black (Rubro-Negra)** | Balanceamento **mais relaxado** (regras de coloração garantem altura no máximo ~2× a ideal) | Menos rotações em inserção/remoção (melhor para cargas de escrita frequente), busca um pouco menos otimizada que AVL |

⚠️ **Pegadinha número 2:** achar que AVL é "estritamente melhor" que Red-Black (ou vice-versa). É um **trade-off**: AVL favorece cenários com **muitas buscas e poucas inserções/remoções** (árvore mais baixa = busca mais rápida); Red-Black favorece cenários com **inserções/remoções frequentes** (menos rotações = menor custo de manutenção). Muitas bibliotecas padrão (ex.: `TreeMap` em Java, `map`/`set` em C++) usam árvores Red-Black internamente.

### 8.4 Percursos em Árvores (Tree Traversals)
| Percurso | Ordem | Uso típico |
|---|---|---|
| **Pré-ordem (pre-order)** | Raiz → Esquerda → Direita | Copiar/serializar a estrutura da árvore |
| **Em-ordem (in-order)** | Esquerda → Raiz → Direita | Em uma BST, retorna os elementos **em ordem crescente** |
| **Pós-ordem (post-order)** | Esquerda → Direita → Raiz | Deletar a árvore com segurança (filhos antes do pai) |
| **Em nível (level-order / BFS)** | Nível por nível | Usa fila; útil para encontrar o nó mais próximo da raiz |

⚠️ **Pegadinha:** o percurso **em-ordem em uma BST** sempre retorna os elementos em **ordem crescente** — essa propriedade é frequentemente usada em prova para "provar" que uma árvore é uma BST válida, ou para extrair os elementos ordenados sem precisar de um algoritmo de ordenação separado.

---

## 9. Tabela Hash (Hash Table / Hash Map)

### 9.1 Definição
- Estrutura que mapeia **chaves para valores**, usando uma **função hash** para calcular o índice de um array interno onde o valor deve ser armazenado, permitindo acesso muito rápido em média.

### 9.2 Tratamento de Colisões
| Estratégia | Como funciona |
|---|---|
| **Encadeamento (chaining)** | Cada posição do array guarda uma **lista** de todos os elementos que colidiram naquele índice |
| **Endereçamento aberto (open addressing)** | Ao colidir, procura-se **outra posição livre** no próprio array, seguindo uma regra (linear probing, quadratic probing, double hashing) |

### 9.3 Complexidades — a pegadinha central desta seção
| Operação | Caso médio | Pior caso |
|---|---|---|
| Inserção | O(1) | **O(n)** |
| Busca | O(1) | **O(n)** |
| Remoção | O(1) | **O(n)** |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a seção de tabela hash):** afirmar que tabela hash é **"sempre O(1)"**. O O(1) é o **caso médio**, assumindo uma **boa função hash** e um **fator de carga controlado** (poucas colisões). No **pior caso** (função hash ruim, muitas colisões, ou um ataque adversarial deliberadamente escolhendo chaves que colidem), a estrutura pode **degenerar** — no encadeamento, todos os elementos caem no mesmo balde, tornando busca/inserção O(n) (equivalente a percorrer uma lista encadeada única).

### 9.4 Fator de Carga (Load Factor) e Rehashing
- **Fator de carga** = número de elementos / número de posições (buckets) do array interno.
- Quando o fator de carga ultrapassa um limite (ex.: 0.75), a tabela realiza **rehashing**: cria um array maior e redistribui todos os elementos — operação O(n), mas que, como no array dinâmico, tem **custo amortizado O(1) por inserção** ao longo do tempo.

⚠️ **Pegadinha:** uma **boa função hash** deve distribuir as chaves **uniformemente** pelos buckets — uma função hash mal projetada (ex.: que gera muitos valores concentrados em poucos índices) pode causar degradação de performance **mesmo com fator de carga baixo**.

---

## 10. Quadro Comparativo Geral de Complexidades

| Estrutura | Acesso | Busca | Inserção | Remoção |
|---|---|---|---|---|
| **Array (dinâmico)** | O(1) | O(n) | O(1)* (fim) / O(n) (meio) | O(n) |
| **Lista encadeada** | O(n) | O(n) | O(1)** | O(1)** |
| **Pilha** | O(1) (topo) | O(n) | O(1) | O(1) |
| **Fila (bem implementada)** | O(1) (extremos) | O(n) | O(1) | O(1) |
| **Heap (binário)** | O(1) (topo) | O(n) | O(log n) | O(log n) |
| **BST balanceada (AVL/RB)** | — | O(log n) | O(log n) | O(log n) |
| **BST não-balanceada (pior caso)** | — | O(n) | O(n) | O(n) |
| **Tabela Hash** | — | O(1)* | O(1)* | O(1)* |

`*` = amortizado/caso médio; `**` = quando a posição já é conhecida (com ponteiro em mãos)

---

## 11. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Inserção no fim de array dinâmico | O(1) amortizado (não sempre O(1) estrito) |
| Fila implementada ingenuamente sobre array | Dequeue pode ser O(n) — usar buffer circular ou lista encadeada |
| "Lista encadeada é sempre melhor para inserir/remover" | Só se a posição já é conhecida; senão, busca O(n) anula a vantagem |
| Buscar valor arbitrário em um heap | O(n) — heap não é árvore de busca binária |
| Construir heap a partir de n elementos | O(n), não O(n log n) |
| "BST é sempre O(log n)" | Falso — pior caso O(n) se desbalanceada (ex.: inserção em ordem) |
| Garantir O(log n) mesmo no pior caso | Árvores balanceadas: AVL ou Red-Black |
| Muitas buscas, poucas escritas | AVL (mais balanceada, busca mais rápida) |
| Muitas inserções/remoções | Red-Black (menos rotações) |
| Percurso que retorna elementos ordenados em uma BST | Em-ordem (in-order) |
| "Tabela hash é sempre O(1)" | Falso — O(1) é caso médio; pior caso O(n) com muitas colisões |
| Estrutura por trás de fila de prioridade | Heap |
| Estrutura usada em BFS / DFS | Fila (BFS) / Pilha (DFS) |

---

## 12. Aplicação Profissional

- **Bancos de dados e índices:** árvores balanceadas (frequentemente B-trees, uma generalização de árvores balanceadas para disco) são a base de índices em bancos de dados relacionais.
- **Caches e dicionários:** tabelas hash são a estrutura padrão por trás de dicionários/mapas em praticamente todas as linguagens modernas (dict em Python, HashMap em Java, objetos em JavaScript).
- **Filas de tarefas e sistemas distribuídos:** filas (e variações como filas de prioridade) são centrais em sistemas de mensageria e escalonamento de tarefas.
- **Compiladores e parsers:** pilhas são usadas para análise sintática, verificação de balanceamento de símbolos, e a própria pilha de execução de chamadas de função.
- **Algoritmos de grafos em produção** (rotas, redes sociais): heaps (para Dijkstra) e filas (para BFS) são componentes centrais.
- Na prática profissional, a escolha errada de estrutura de dados é uma das causas mais comuns de **gargalos de performance silenciosos** — por exemplo, usar uma lista para buscas frequentes por chave (O(n)) quando um dicionário/tabela hash (O(1) médio) resolveria o mesmo problema de forma muito mais eficiente, sem exigir nenhuma mudança na lógica de negócio, apenas na estrutura de armazenamento.

---

## 13. Perguntas típicas de prova (para se testar)

1. Por que a inserção no final de um array dinâmico é chamada de "O(1) amortizado", e não simplesmente O(1)?
2. Explique por que uma fila implementada de forma ingênua sobre um array pode ter complexidade O(n) para a operação de dequeue, e como resolver esse problema.
3. Por que buscar um valor arbitrário em um heap binário é O(n), mesmo sendo uma estrutura baseada em árvore?
4. Em que cenário uma Árvore Binária de Busca (BST) comum degenera para complexidade O(n) em todas as operações? Como as árvores AVL e Red-Black resolvem esse problema?
5. Por que se diz que a complexidade O(1) de uma tabela hash é referente ao "caso médio", e não ao pior caso? O que pode causar a degradação para O(n)?
6. Compare o trade-off entre array e lista encadeada para as operações de acesso por índice e inserção/remoção no meio da estrutura.
