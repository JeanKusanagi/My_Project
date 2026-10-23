# Estruturas de Dados e Suas Complexidades

Um guia de referência rápida sobre as principais estruturas de dados utilizadas na computação, cobrindo suas definições, características, funcionamento de colisões, redimensionamento e balanceamento.

---

## 1. Tabela Resumo de Complexidade (Notação Big-O)

| Estrutura de Dados | Acesso / Busca (Médio) | Inserção (Médio) | Remoção (Médio) | Pior Caso (Geral) |
| :--- | :--- | :--- | :--- | :--- |
| **Vetor (Array)** | $O(1)$ / $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Matriz** | $O(1)$ / $O(n \times m)$ | $O(n \times m)$ | $O(n \times m)$ | $O(n \times m)$ |
| **Pilha (Stack)** | $O(1)$ / $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ (Busca) |
| **Fila (Queue)** | $O(1)$ / $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ (Busca) |
| **Lista Encadeada** | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ (Busca) |
| **Heap Binário** | $O(1)$ (Topo) / $O(n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| **Árvore de Busca (BST)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ (Desbalanceada) |
| **Árvore Balanceada (AVL/RB)**| $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| **Tabela Hash** | $O(1)$ | $O(1)$ | $O(1)$ | $O(n)$ (Colisões totais) |

---

## 2. Visão Geral das Estruturas

### Vetor e Matriz
* **Vetor:** Elementos contíguos na memória. Acesso instantâneo por índice $O(1)$, mas inserções/remoções no início ou meio exigem o deslocamento de elementos $O(n)$. Principais Aplicações: Buffers de dados, tabelas de consulta rápida (lookup tables), armazenamento de sequências fixas ou variáveis de tamanho previsível.
* **Matriz:** Extensão bidimensional ($m \times n$) ou multidimensional. Mantém propriedades similares de acesso direto na memória física linearizada. Principais Aplicações: Processamento de imagens e pixels, tabuleiros de jogos (xadrez, batalha naval), representação de grafos via matriz de adjacência e cálculos de álgebra linear.

### Pilha (LIFO) e Fila (FIFO)
* **Pilha (Last In, First Out):** Operações concentradas no topo (*Push*, *Pop*, *Peek*). Todas executadas em $O(1)$. Principais Aplicações:
    * Gerenciamento de chamadas de funções (Call Stack) em compiladores e sistemas operacionais.
    * Desfazer/refazer (Undo/Redo) em editores de texto.
    * Verificação de sintaxe e balanceamento de parênteses/chaves em código.
    * Algoritmos de busca em profundidade (DFS) e conversão de expressões matemáticas.
* **Fila (First In, First Out):** Elementos entram pelo fim (*Enqueue*) e saem pelo início (*Dequeue*). Operações gerenciadas eficientemente com ponteiros em $O(1)$. Principais Aplicações:
    * Gerenciamento de filas de impressão em sistemas operacionais.
    * Processamento de requisições em servidores e filas de mensagens (message brokers).
    * Algoritmos de busca em largura (BFS - Breadth-First Search).
    * Escalonamento de processos (scheduling) na CPU.

### Listas Encadeadas
* Elementos espalhados pela memória conectados por ponteiros (referências). Perdem o acesso indexado rápido $O(n)$, mas ganham em inserções dinâmicas $O(1)$ caso o ponto de inserção já seja conhecido. Principais Aplicações:• Implementação dinâmica de pilhas e filas onde o tamanho varia constantemente.
    * Gerenciamento de memória livre por sistemas operacionais.
    * Navegador web histórico (botões "avançar" e "voltar" em listas duplamente encadeadas).

### Heap
* Árvore binária completa usada para filas de prioridade. Garante que o maior (Max-Heap) ou menor (Min-Heap) elemento esteja sempre na raiz $O(1)$. Modificações estruturais tomam $O(\log n)$. Principais Aplicações:
    * Filas de prioridade (atendimento de urgências, escalonador de tarefas com pesos).
    * Algoritmo de Dijkstra para caminho mais curto em grafos.
    * Ordenação eficiente (HeapSort).

---

## 3. Tabelas Hash: Colisões e Redimensionamento (Rehashing)

Uma **colisão** ocorre quando duas chaves diferentes resultam no mesmo índice após passarem pela função hash.

### Estratégias de Resolução
1. **Encadeamento Externo (Separate Chaining):** Cada posição do vetor aponta para uma lista encadeada. Se houver colisão, o elemento é inserido no final ou início da lista.
2. **Endereçamento Aberto (Open Addressing):** Todos os dados ficam no próprio vetor principal:
   * *Sondagem Linear:* Procura a próxima vaga sequencialmente ($h + 1, h + 2, \dots$). Causa agrupamento primário.
   * *Sondagem Quadrática:* Procura vagas usando saltos ao quadrado ($h + 1^2, h + 2^2, \dots$).
   * *Hash Duplo:* Utiliza uma segunda função hash para calcular a distância do salto, distribuindo melhor os elementos.

### Redimensionamento (Rehashing)
* **Gatilho:** Ativado pelo Fator de Carga $\alpha = n/m$. Normalmente disparado quando a ocupação atinge **75% ($\alpha = 0.75$)**.
* **Como funciona:** Um novo vetor de tamanho maior (geralmente o dobro) é alocado. Como o tamanho mudou, a operação `hash(chave) % tamanho` é recalculada para **todos** os elementos antigos, espalhando-os e eliminando colisões acumuladas.
* **Complexidade:** A operação isolada custa $O(n)$, mas seu impacto diluído mantém o custo de inserção em **$O(1)$ amortizado**.

Principais Aplicações:• 
   * Dicionários e objetos em linguagens de programação (JSON, Maps).
   * Cache de dados e memorização (Memoization em programação dinâmica).
   * Bancos de dados NoSQL baseados em chave-valor e verificação rápida de duplicatas.

---

## 4. Balanceamento de Árvores

Árvores de Busca Binária (BST) puras podem sofrer degeneração se receberem dados ordenados, transformando-se em listas lineares de pior caso $O(n)$. O balanceamento reorganiza a árvore para manter sua altura restrita a $O(\log n)$.

### Mecanismo: Rotações
Modificam a estrutura dos ponteiros sem violar a regra básica da BST (filhos esquerdos menores, filhos direitos maiores).
* **Simples (Esquerda / Direita):** Corrigem desbalanceamentos em linha reta (ex: sequências estritamente crescentes ou decrescentes).
* **Duplas (Esquerda-Direita / Direita-Esquerda):** Corrigem estruturas em "zigue-zague" ou joelho antes de aplicar a rotação principal.

### Modelos de Árvores Auto-Balanceáveis
* **Árvore AVL:** Rigorosa. O fator de balanceamento (diferença de altura entre subárvores) de qualquer nó nunca pode passar de $\pm 1$. Excelente para cenários de alta frequência de leitura e busca.
* **Árvore Rubro-Negra (Red-Black):** Mais flexível. Utiliza regras de coloração de nós (Vermelho/Preto). Permite que o maior caminho seja até o dobro do menor caminho. Exige menos rotações, sendo ideal para sistemas com inserções e remoções frequentes (base do `std::map` do C++ e `TreeMap` do Java).
 

## Árvores (Árvore de Busca Binária - BST, AVL, Vermelho-Preta, Árvore B)

• O que é: Estrutura não linear hierárquica composta por nós conectados em ramificações (raiz, ramos e folhas).

• Principais Aplicações:
  * Bancos de dados e sistemas de arquivos (Árvores B e B+ para indexação rápida em disco).
  * Hierarquias de diretórios e representação de expressões/AST (Abstract Syntax Trees).
  * Árvores balanceadas (AVL / Vermelho-Preta) para manter buscas rápidas ordenadas dinamicamente.

• Complexidade (Árvore de Busca Binária / Balanceada no Caso Médio):• Busca / Inserção / Remoção: $\(O(\log n)\)$.
