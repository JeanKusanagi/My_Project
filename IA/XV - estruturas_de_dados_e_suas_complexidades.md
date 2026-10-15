# Guia Definitivo: Estruturas de Dados e Suas Complexidades (Big-O)

Este documento apresenta uma análise detalhada das principais estruturas de dados utilizadas na ciência da computação, abordando seu funcionamento, casos de uso e a complexidade temporal e espacial das operações fundamentais.

---

## 1. Tabela Resumo de Complexidade (Big-O)

| Estrutura de Dados | Acesso (Médio / Pior) | Busca (Médio / Pior) | Inserção (Médio / Pior) | Remoção (Médio / Pior) | Espaço (Pior Caso) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Vetor (Array)** | $O(1) / O(1)$ | $O(n) / O(n)$ | $O(n) / O(n)$ | $O(n) / O(n)$ | $O(n)$ |
| **Vetor Dinâmico** | $O(1) / O(1)$ | $O(n) / O(n)$ | $O(1)^1 / O(n)$ | $O(n) / O(n)$ | $O(n)$ |
| **Matriz ($m \times n$)** | $O(1) / O(1)$ | $O(m \cdot n)$ | $O(m \cdot n)^2$ | $O(m \cdot n)^2$ | $O(m \cdot n)$ |
| **Pilha (Stack)** | $O(n) / O(n)$ | $O(n) / O(n)$ | $O(1) / O(1)$ | $O(1) / O(1)$ | $O(n)$ |
| **Fila (Queue)** | $O(n) / O(n)$ | $O(n) / O(n)$ | $O(1) / O(1)$ | $O(1) / O(1)$ | $O(n)$ |
| **Lista Simplesmente Encadeada** | $O(n) / O(n)$ | $O(n) / O(n)$ | $O(1)^3 / O(1)^3$ | $O(1)^3 / O(1)^3$ | $O(n)$ |
| **Lista Duplamente Encadeada** | $O(n) / O(n)$ | $O(n) / O(n)$ | $O(1)^3 / O(1)^3$ | $O(1)^3 / O(1)^3$ | $O(n)$ |
| **Tabela Hash (Hash Map)** | $N/A$ | $O(1) / O(n)$ | $O(1) / O(n)$ | $O(1) / O(n)$ | $O(n)$ |
| **Heap (Min/Max)** | $O(1)^4 / O(1)^4$ | $O(n) / O(n)$ | $O(\log n) / O(\log n)$ | $O(\log n) / O(\log n)$ | $O(n)$ |
| **Árvore Binária de Busca (BST)** | $O(\log n) / O(n)^5$ | $O(\log n) / O(n)^5$ | $O(\log n) / O(n)^5$ | $O(\log n) / O(n)^5$ | $O(n)$ |
| **Árvore Balanceada (AVL / Red-Black)**| $O(\log n) / O(\log n)$ | $O(\log n) / O(\log n)$ | $O(\log n) / O(\log n)$ | $O(\log n) / O(\log n)$ | $O(n)$ |

> **Notas de Rodapé:**
> 1. Inserção amortecida $O(1)$. No pior caso (redimensionamento do array), é $O(n)$.
> 2. Redimensionamento ou deslocamento de linhas/colunas. Alterar um elemento existente é $O(1)$.
> 3. Considera inserção/remoção nas extremidades (cabeça/cauda) ou quando se já tem o ponteiro para o nó. Se for necessário buscar a posição primeiro, o tempo total inclui a busca $O(n)$.
> 4. Refere-se ao acesso do elemento do topo (mínimo ou máximo).
> 5. Uma BST não balanceada pode degenerar em uma lista encadeada no pior caso.

---

## 2. Detalhamento por Estrutura de Dados

### 2.1. Vetor (Array) e Vetor Dinâmico
* **O que é:** Bloco contíguo de memória reservado para armazenar elementos do mesmo tipo. No vetor estático, o tamanho é fixado na compilação/alocação. No vetor dinâmico (`ArrayList` em Java, `std::vector` em C++, `list` em Python), o tamanho cresce automaticamente conforme necessário.
* **Mecânica interna:** Para vetores dinâmicos, quando a capacidade máxima é atingida, aloca-se um novo bloco de memória com o dobro da capacidade e todos os elementos antigos são copiados ($O(n)$ pontual, porém $O(1)$ amortizado).
* **Vantagens:**
  * Acesso aleatório extremamente rápido $O(1)$ via índice (cálculo de deslocamento na memória: `endereço_base + índice * tamanho_do_tipo`).
  * Excelente localidade de referência (ótimo aproveitamento de *cache* do processador).
* **Desvantagens:**
  * Inserção e remoção no meio ou início exigem o deslocamento (*shift*) de todos os elementos subsequentes ($O(n)$).
* **Casos de Uso:**
  * Armazenamento de dados com tamanho fixo conhecido previamente.
  * Coleções onde a operação mais frequente é a leitura e iteração contínua.

---

### 2.2. Matriz
* **O que é:** Estrutura bidimensional (ou multidimensional) organizada em linhas e colunas.
* **Mecânica interna:** Em memória, a matriz pode ser mapeada em ordem de linha (*Row-Major Order*, usada em C/C++) ou ordem de coluna (*Column-Major Order*, usada em Fortran).
* **Vantagens:**
  * Representação natural de dados bidimensionais como imagens, mapas e sistemas de equações.
  * Acesso a qualquer posição $(i, j)$ em $O(1)$.
* **Desvantagens:**
  * Dificuldade de redimensionamento dinâmico.
  * Ineficiente no uso de memória se a matriz for esparsa (maioria dos elementos são zero ou nulos) — para esses casos, utilizam-se matrizes esparsas (*CSR*, *COO*).
* **Casos de Uso:**
  * Computação gráfica e processamento de imagens (matrizes de pixels).
  * Álgebra linear, inteligência artificial e aprendizado de máquina (tensores/matrizes de pesos).
  * Algoritmos de programação dinâmica e grafos (matriz de adjacência).

---

### 2.3. Pilha (Stack)
* **O que é:** Estrutura linear do tipo **LIFO** (*Last-In, First-Out* — O último a entrar é o primeiro a sair).
* **Principais Operações:**
  * `push(x)`: Insere no topo ($O(1)$).
  * `pop()`: Remove do topo ($O(1)$).
  * `peek()` / `top()`: Consulta o elemento do topo sem remover ($O(1)$).
* **Vantagens:**
  * Simplicidade de implementação.
  * Garantia de controle de ordem reversa e contexto de execução.
* **Desvantagens:**
  * Acesso restrito apenas ao topo (não permite busca ou acesso aleatório eficiente).
* **Casos de Uso:**
  * Pilha de chamadas de funções em linguagens de programação (*Call Stack*).
  * Mecanismo de Desfazer/Refazer (*Undo/Redo*) em editores de texto.
  * Validação de parênteses e sintaxe em compiladores.
  * Algoritmos de navegação (botão "Voltar" do navegador).

---

### 2.4. Fila (Queue)
* **O que é:** Estrutura linear do tipo **FIFO** (*First-In, First-Out* — O primeiro a entrar é o primeiro a sair).
* **Principais Operações:**
  * `enqueue(x)`: Insere no fim/cauda ($O(1)$).
  * `dequeue()`: Remove do início/cabeça ($O(1)$).
  * `front()`: Consulta o primeiro da fila ($O(1)$).
* **Variantes:**
  * **Deque (Double-ended Queue):** Inserção e remoção permitidas em ambas as extremidades em $O(1)$.
  * **Fila de Prioridade (Priority Queue):** Os elementos são removidos com base em prioridade, não na ordem de chegada (geralmente implementada com *Heap*).
* **Casos de Uso:**
  * Escalonamento de processos no sistema operacional (*CPU Scheduling*).
  * Filas de impressão e envio de e-mails em lote.
  * Algoritmos de busca em largura (*BFS - Breadth-First Search*) em grafos e árvores.

---

### 2.5. Listas Encadeadas (Linked Lists)
* **O que é:** Estrutura linear na qual os elementos (nós) não estão em posições contíguas de memória. Cada nó contém o seu valor e um ponteiro (ou referência) para o próximo nó.

#### Tipos:
1. **Simplesmente Encadeada:** Cada nó aponta para o próximo (`node -> next`).
2. **Duplamente Encadeada:** Cada nó aponta para o próximo e para o anterior (`prev <- node -> next`).
3. **Circular:** O último nó aponta para o primeiro nó da lista.

* **Vantagens:**
  * Tamanho dinâmico (não precisa de pré-alocação de espaço contíguo).
  * Inserções e remoções rápidas em $O(1)$ se a posição (ponteiro) já for conhecida.
* **Desvantagens:**
  * Acesso aleatório lento ($O(n)$) — é necessário percorrer nó a nó a partir da cabeça (*Head*).
  * Maior consumo de memória devido ao armazenamento dos ponteiros adicionais.
  * Baixa performance com relação à *cache* do processador.
* **Casos de Uso:**
  * Implementação de Pilhas, Filas e Tabelas Hash (resolução de colisões por encadeamento).
  * Alocação dinâmica de memória no sistema operacional.

---

### 2.6. Tabela Hash (Hash Map / Hash Table)
* **O que é:** Estrutura de dados que mapeia chaves a valores utilizando uma **Função Hash** (*Hash Function*) para calcular o índice em um vetor subjacente onde o valor deve ser armazenado.
* **Colisões:** Ocorrem quando duas chaves diferentes geram o mesmo índice na função hash.
  * **Tratamento por Encadeamento (*Chaining*):** Cada posição do vetor armazena uma Lista Encadeada com os elementos colididos.
  * **Tratamento por Endereçamento Aberto (*Open Addressing*):** Procura a próxima posição livre no vetor (ex: *Linear Probing*, *Quadratic Probing*, *Double Hashing*).
* **Vantagens:**
  * Busca, inserção e remoção extremamente eficientes no caso médio: $O(1)$.
* **Desvantagens:**
  * No pior caso (todas as chaves colidem no mesmo bucket), a complexidade degenera para $O(n)$.
  * Os elementos não são armazenados de forma ordenada.
  * Requer bom redimensionamento e boa função hash para manter a taxa de carga (*Load Factor*) baixa.
* **Casos de Uso:**
  * Bancos de dados (índices Hash).
  * Sistemas de *Caching* (ex: Redis, Memcached).
  * Verificação de duplicatas e dicionários em linguagens (ex: `dict` em Python, `HashMap` em Java).

---

### 2.7. Heap (Binary Heap)
* **O que é:** Árvore binária completa na qual cada nó satisfaz a **Propriedade de Heap**:
  * **Min-Heap:** O valor do pai é menor ou igual ao valor dos filhos (a raiz é sempre o menor elemento).
  * **Max-Heap:** O valor do pai é maior ou igual ao valor dos filhos (a raiz é sempre o maior elemento).
* **Mecânica Interna:** Geralmente é implementada dentro de um **Vetor** comum (sem necessidade de ponteiros explicitos). Para um nó no índice $i$:
  * Filho Esquerdo: $2i + 1$
  * Filho Direito: $2i + 2$
  * Pai: $\lfloor(i - 1) / 2\rfloor$
* **Operações:**
  * `peek()`: $O(1)$
  * `insert()`: $O(\log n)$ — Adiciona no final e faz *bubble-up* (subida).
  * `extractMin()` / `extractMax()`: $O(\log n)$ — Remove a raiz, coloca o último elemento na raiz e faz *heapify-down* (descida).
* **Casos de Uso:**
  * Filas de Prioridade (*Priority Queue*).
  * Algoritmo de ordenação *Heapsort* ($O(n \log n)$ de tempo e $O(1)$ de espaço).
  * Algoritmo de Dijkstra para menor caminho em grafos.

---

### 2.8. Árvores (Trees)
* **O que é:** Estrutura hierárquica e não linear composta por Nós conectados por Arestas, sem ciclos. Contém um nó Raiz e zero ou mais subárvores filhas.

```
       ( Raiz )
        /    \
    ( No )  ( No )
     /  \
  (Folha)(Folha)
```

#### Variantes Importantes:

#### A. Árvore Binária de Busca (BST - Binary Search Tree)
* **Regra:** Para qualquer nó $X$, todos os nós da subárvore esquerda possuem valores menores que $X$, e todos os nós da subárvore direita possuem valores maiores que $X$.
* **Desempenho:**
  * Caso Médio: $O(\log n)$ para busca, inserção e remoção.
  * Pior Caso: $O(n)$ se a árvore for alimentada com dados ordenados, degenerando em uma lista encadeada.

#### B. Árvores Auto-Balanceadas (AVL e Red-Black)
* **AVL:** Árvore onde a diferença de altura entre a subárvore esquerda e direita de qualquer nó (Fator de Balanceamento) não pode ser maior que 1. Garante busca muito rápida devido ao balanceamento rigoroso, mas requer mais rotações em inserções/remoções.
* **Red-Black Tree:** Árvore balanceada por cores (Vermelho e Preto). É menos rigorosa no balanceamento que a AVL, exigindo menos reestruturações em inserções e remoções. É a base da biblioteca padrão de várias linguagens (`std::map` em C++, `TreeMap` em Java).
* **Desempenho:** Garantido de $O(\log n)$ em busca, inserção e remoção em qualquer cenário.

#### C. Árvore B / Árvore B+
* **O que é:** Árvores de busca multiway auto-balanceadas projetadas para funcionar eficientemente em sistemas de armazenamento secundário (discos rígidos, SSDs). Cada nó pode conter múltiplos elementos e múltiplos filhos.
* **Casos de Uso:**
  * Sistemas de arquivos (NTFS, ext4).
  * Bancos de dados relacionais (índices B-Tree do PostgreSQL, MySQL/InnoDB).

---

## 3. Resumo Prático de Tomada de Decisão

* Precisa de **acesso aleatório imediato por índice numérico**? $\rightarrow$ **Vetor / Array**.
* Precisa de **pesquisas por chave com acesso instantâneo $O(1)$**? $\rightarrow$ **Tabela Hash**.
* Precisa processar tarefas por **ordem de chegada**? $\rightarrow$ **Fila**.
* Precisa manter um **histórico de operações / rastreamento reverso**? $\rightarrow$ **Pilha**.
* Precisa acessar constantemente o **elemento de maior ou menor valor**? $\rightarrow$ **Heap**.
* Precisa manter os **dados sempre ordenados com inserção e busca logarítmica garantida**? $\rightarrow$ **Árvore Balanceada (AVL / Red-Black)**.
* Precisa armazenar **milhões de dados em disco com baixa I/O**? $\rightarrow$ **Árvore B / B+**.

```

O documento em formato Markdown está finalizado e organizado no editor ao lado.