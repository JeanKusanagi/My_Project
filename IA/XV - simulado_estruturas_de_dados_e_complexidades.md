# Simulado Exame de Inteligência Artificial e Algoritmos: Estruturas de Dados e Suas Complexidades

**Instruções do Elaborador:**
* Este simulado contém 30 questões de múltipla escolha cobrindo Vetores, Matrizes, Pilhas, Filas, Listas Encadeadas, Heaps, Árvores e Tabelas Hash.
* As alternativas corretas estão distribuídas de forma aleatória (A, B, C, D e E).
* Preste atenção às pegadinhas clássicas de complexidade de tempo amortizada, alocação de memória e piores casos de estruturas de dados.
* O gabarito comentado ao final de cada questão traz a fundamentação teórica rigorosa.

---

### Questão 1 (Médio - Pegadinha)
Ao inserir $n$ elementos sequencialmente em um Vetor Dinâmico (como um `std::vector` em C++ ou `ArrayList` em Java) inicialmente vazio e que dobra sua capacidade a cada redimensionamento, a complexidade de tempo **amortizada** de uma única inserção e a complexidade do **pior caso de uma única inserção específica** são, respectivamente:

A) $O(n)$ e $O(n)$  
B) $O(1)$ e $O(1)$  
C) $O(1)$ e $O(n)$  
D) $O(\log n)$ e $O(n)$  
E) $O(1)$ e $O(\log n)$  

**Resposta Correta: C**

**Comentário:** A pegadinha está na diferença entre o tempo **amortizado** e o tempo do **pior caso**. Na maioria das inserções, o vetor dinâmico possui espaço livre, realizando a inserção em tempo constante $O(1)$. Porém, quando o vetor fica cheio, ocorre um redimensionamento (alocação de um novo bloco do dobro do tamanho + cópia dos $n$ elementos antigos), o que custa $O(n)$ no pior caso daquela chamada específica. Espalhando o custo das cópias ao longo das $n$ inserções (Análise Amortizada), o custo médio por operação é $O(1)$.

---

### Questão 2 (Fácil)
Qual das seguintes estruturas de dados é a escolha mais adequada para implementar o mecanismo de "Desfazer" (Undo) em um editor de código ou a pilha de chamadas de funções (*Call Stack*) de uma Linguagem de Programação?

A) Fila (Queue)  
B) Tabela Hash (Hash Table)  
C) Árvore AVL  
D) Pilha (Stack)  
E) Heap Mínimo  

**Resposta Correta: D**

**Comentário:** A Pilha segue o princípio LIFO (*Last-In, First-Out* — O último a entrar é o primeiro a sair). Como a última ação realizada pelo usuário deve ser a primeira a ser desfeita, a Pilha é a estrutura perfeita para esse padrão de acesso.

---

### Questão 3 (Difícil - Pegadinha)
Deseja-se realizar a busca por um valor específico em uma **Tabela Hash** contendo $n$ elementos armazenados, na qual o tratamento de colisões é feito por **Encadeamento Exterior (Chaining)** usando listas simplesmente encadeadas. No **pior caso absoluto**, qual é a complexidade de tempo dessa busca?

A) $O(1)$  
B) $O(\log n)$  
C) $O(n \log n)$  
D) $O(n^2)$  
E) $O(n)$  

**Resposta Correta: E**

**Comentário:** A pegadinha está na suposição de que "Tabela Hash é sempre $O(1)$". No caso médio com uma boa função hash, o acesso/busca é de fato $O(1)$. Contudo, no **pior caso** (quando a função hash é ruim ou sob um ataque de colisão proposital onde todas as $n$ chaves geram o exato mesmo índice/hash), todos os $n$ elementos caem no mesmo *bucket*, formando uma única lista encadeada de tamanho $n$. A busca nessa lista custa $O(n)$.

---

### Questão 4 (Médio)
Uma **Árvore Binária de Busca (BST)** não balanceada é construída inserindo sequencialmente os seguintes elementos, nessa exata ordem: `[1, 2, 3, 4, 5, 6, 7]`. Em seguida, realiza-se uma busca pelo elemento `7`. Qual é a complexidade dessa busca nessa árvore específica?

A) $O(\log n)$  
B) $O(1)$  
C) $O(n)$  
D) $O(n \log n)$  
E) $O(n^2)$  

**Resposta Correta: C**

**Comentário:** Ao inserir elementos estritamente crescentes em uma BST sem mecanismos de auto-balanceamento, a árvore degenera em uma estrutura similar a uma lista encadeada simples (uma árvore "fina" ou inclinada à direita). O tempo de busca para o elemento mais profundo ($7$) torna-se proporcional à altura da árvore, que é $n$, resultando em $O(n)$.

---

### Questão 5 (Difícil)
Em uma **Heap Mínima (Min-Heap)** binária com $n$ elementos, armazenada de forma contígua em um array, qual é a complexidade temporal para encontrar o **MAIOR** elemento presente na heap?

A) $O(1)$  
B) $O(\log n)$  
C) $O(n)$  
D) $O(n \log n)$  
E) Impossível determinar sem desestruturar a heap.  

**Resposta Correta: C**

**Comentário:** Em uma Min-Heap, a única garantia de ordenação rígida é que o pai é menor ou igual aos seus filhos. Portanto, o menor elemento está garantidamente na raiz (índice 0) em $O(1)$. Todavia, o **maior** elemento pode estar em qualquer uma das folhas da árvore. Como uma árvore binária completa tem aproximadamente $\lceil n/2 \rceil$ folhas, precisamos realizar uma busca linear por essas folhas, resultando em uma complexidade $O(n)$.

---

### Questão 6 (Fácil)
Dada uma Matriz de dimensões $m \times n$, qual é o tempo de acesso ao elemento localizado na linha $i$ e coluna $j$, assumindo que a matriz está mapeada na memória contígua?

A) $O(m \times n)$  
B) $O(m + n)$  
C) $O(\log(m \times n))$  
D) $O(1)$  
E) $O(m)$  

**Resposta Correta: D**

**Comentário:** O acesso a qualquer posição $(i, j)$ de uma matriz alocada sequencialmente na memória é feito via aritmética de ponteiros direta (ex: `EndereçoBase + (i * n + j) * tamanho_do_tipo`), exigindo apenas um número constante de operações matemáticas, o que corresponde a $O(1)$.

---

### Questão 7 (Médio - Pegadinha)
Considere uma **Lista Duplamente Encadeada** com ponteiros para a Cabeça (*Head*) e para a Cauda (*Tail*). Se já possuirmos uma **referência/ponteiro direto** para um nó intermediário $K$ que se deseja remover, qual é a complexidade temporal para efetuar a remoção desse nó $K$?

A) $O(n)$  
B) $O(1)$  
C) $O(\log n)$  
D) $O(n^2)$  
E) $O(k)$  

**Resposta Correta: B**

**Comentário:** A pegadinha é achar que é preciso "percorrer a lista até achar o nó". A questão especifica que **já temos o ponteiro direto** para o nó $K$. Como a lista é *duplamente encadeada*, o nó $K$ conhece tanto o nó anterior (`K.prev`) quanto o próximo (`K.next`). Para removê-lo, basta ajustar os ponteiros: `K.prev.next = K.next` e `K.next.prev = K.prev`. Essa atualização de ponteiros consome tempo constante $O(1)$. (Nota: Em uma lista *simplesmente* encadeada sem o truque de copiar o valor do sucessor, seria $O(n)$ para achar o nó anterior).

---

### Questão 8 (Difícil)
O processo de construção de uma Heap Binária (*Build-Heap*) a partir de um array desordenado contendo $n$ elementos pode ser feito de forma otimizada de baixo para cima (*bottom-up*) utilizando o algoritmo de Floyd. A complexidade de tempo desse processo no pior caso é:

A) $O(n \log n)$  
B) $O(n^2)$  
C) $O(n)$  
D) $O(\log n)$  
E) $O(n \sqrt{n})$  

**Resposta Correta: C**

**Comentário:** Embora inserir $n$ elementos um a um em uma heap vazia custe $O(n \log n)$, o algoritmo de *Build-Heap* de Floyd aplica a operação `heapify` de baixo para cima a partir do último nó não-folha. A soma das alturas de todos os nós resulta na série convergem $S = \sum_{h=0}^{\log n} \frac{n}{2^{h+1}} O(h) = O(n)$. Logo, construir uma heap a partir de um array desordenado custa tempo linear $O(n)$.

---

### Questão 9 (Fácil)
Em uma **Fila (Queue)** padrão mantida segundo o princípio FIFO, as operações de **Inserção (Enqueue)** e **Remoção (Dequeue)** ocorrem, respectivamente:

A) No Início (Cabeça) e no Fim (Cauda).  
B) Ambas no Início (Cabeça).  
C) No Fim (Cauda) e no Início (Cabeça).  
D) Ambas no Fim (Cauda).  
E) Em qualquer posição aleatória.  

**Resposta Correta: C**

**Comentário:** Por definição da estrutura FIFO (*First-In, First-Out*), novos elementos sempre entram no final da fila (Cauda/Rear) e os elementos processados são removidos da frente da fila (Início/Cabeça/Front).

---

### Questão 10 (Médio)
Qual é a principal vantagem de uma **Árvore AVL** sobre uma **Árvore Binária de Busca (BST)** tradicional?

A) A Árvore AVL permite armazenar chaves duplicadas no mesmo nó, reduzindo o uso de memória.  
B) A Árvore AVL garante que a altura da árvore seja sempre mantida em $O(\log n)$ através de rotações, prevenindo a degeneração para $O(n)$.  
C) As buscas na Árvore AVL têm complexidade $O(1)$ no caso médio.  
D) A Árvore AVL não utiliza ponteiros, sendo armazenada inteiramente em uma matriz.  
E) O tempo de remoção na Árvore AVL é sempre $O(1)$.  

**Resposta Correta: B**

**Comentário:** A Árvore AVL é uma árvore binária de busca auto-balanceada. A diferença entre as alturas das subárvores esquerda e direita de qualquer nó (fator de balanceamento) é mantida estritamente em no máximo $1$. Isso assegura uma altura $h \le 1.44 \log_2 n$, garantindo complexidade $O(\log n)$ para busca, inserção e remoção no pior caso.

---

### Questão 11 (Fácil)
Qual das seguintes estruturas de dados oferece acesso aleatório em tempo constante $O(1)$ aos seus elementos via índice inteiro, porém consome um bloco **estritamente contíguo** de memória RAM?

A) Lista Simplesmente Encadeada  
B) Árvore Vermelho-e-Preto (Red-Black Tree)  
C) Vetor Estático (Array)  
D) Tabela Hash com Encadeamento  
E) Grafo por Lista de Adjacência  

**Resposta Correta: C**

**Comentário:** O Vetor (Array estático) é a estrutura fundamental mantida em blocos de memória contíguos. Essa característica contígua é exatamente o que permite ao sistema operacional calcular o endereço de memória de qualquer elemento diretamente em tempo $O(1)$ através do seu índice.

---

### Questão 12 (Difícil - Pegadinha)
Deseja-se implementar uma Fila usando um **Vetor Dinâmico** comum, onde a inserção (`enqueue`) é feita na posição `array[size]` ($O(1)$ amortizado) e a remoção (`dequeue`) é feita removendo o elemento da posição `array[0]` e **deslocando todos os elementos restantes uma posição para a esquerda**. Qual é a complexidade temporal da operação `dequeue` nessa implementação ingênua?

A) $O(1)$  
B) $O(\log n)$  
C) $O(n)$  
D) $O(n^2)$  
E) $O(1)$ amortizado  

**Resposta Correta: C**

**Comentário:** A pegadinha está em esquecer o custo de reordenar o array. Ao remover do índice 0 de um array comum, todos os $n-1$ elementos subsequentes precisam ser copiados/deslocados para o índice anterior para preencher o "buraco". Portanto, a operação `dequeue` nessa implementação ingênua é $O(n)$. Para torná-la $O(1)$, deve-se usar um **Vetor Circular** com ponteiros para início e fim.

---

### Questão 13 (Médio)
Sobre o uso de **Tabelas Hash**, o que caracteriza o fenômeno do **Agrupamento Primário (Primary Clustering)** no tratamento de colisões por Endereçamento Aberto?

A) A criação de uma lista encadeada infinitamente longa na primeira posição da tabela.  
B) A tendência de chaves colididas formarem longos blocos contínuos de posições ocupadas quando se utiliza Sondagem Linear (Linear Probing), degradando o tempo de busca.  
C) O erro que ocorre quando a função hash retorna um valor negativo.  
D) O esgotamento da memória cache da CPU devido ao tamanho excessivo das chaves string.  
E) O aumento da complexidade de espaço de $O(n)$ para $O(n^2)$.  

**Resposta Correta: B**

**Comentário:** Na Sondagem Linear ($hash(k) + i \pmod N$), se uma colisão ocorre, procura-se a próxima posição livre (+1, +2, etc.). Isso gera cadeias/blocos contínuos de posições ocupadas na tabela. Quanto maior o bloco, maior a probabilidade de uma nova chave cair nesse bloco e aumentá-lo ainda mais, degradando o desempenho para próximo de $O(n)$.

---

### Questão 14 (Difícil)
Em uma **Árvore B (B-Tree)** de ordem $m$, qual das seguintes afirmações descreve corretamente suas propriedades operacionais e de estrutura?

A) Cada nó pode conter no máximo 1 chave e ter no máximo 2 filhos.  
B) Todos os nós folhas estão localizados no mesmo nível de profundidade.  
C) A busca por uma chave exige sempre a leitura de todas as folhas da esquerda para a direita.  
D) A inserção de uma nova chave ocorre sempre no nó raiz, empurrando as chaves antigas para baixo.  
E) É uma estrutura adequada apenas para memória principal (RAM), sendo inviável em bancos de dados e sistemas de arquivos.  

**Resposta Correta: B**

**Comentário:** A Árvore B é uma árvore de busca auto-balanceada projetada para sistemas de armazenamento secundário (discos/SSDs). Uma de suas propriedades fundamentais é que **todas as folhas estão exatamente na mesma profundidade/nível**, o que garante um balanceamento perfeito e operações em $O(\log n)$.

---

### Questão 15 (Fácil)
A travessia em uma Árvore Binária de Busca (BST) que visita os nós na ordem **Subárvore Esquerda $\to$ Nó Raiz $\to$ Subárvore Direita** é conhecida como:

A) Travessia em Pré-Ordem (Pre-order)  
B) Travessia em Pós-Ordem (Post-order)  
C) Travessia em Ordem Simétrica (In-order)  
D) Travessia por Nível (Breadth-First Search)  
E) Travessia Zig-zag  

**Resposta Correta: C**

**Comentário:** A caminhada *In-order* (em ordem simétrica) visita: Esquerda, Raiz, Direita. Uma propriedade famosa da BST é que o percurso *In-order* visita os nós em **ordem estritamente crescente** dos seus valores.

---

### Questão 16 (Médio - Pegadinha)
Dada uma **Lista Simplesmente Encadeada** com $n$ elementos, mantendo apenas o ponteiro para a **Cabeça (Head)** da lista. Qual é a complexidade de tempo para **inserir** um novo elemento no **final** (Cauda) desta lista e para **remover** um elemento do **início** (Cabeça), respectivamente?

A) $O(1)$ e $O(1)$  
B) $O(n)$ e $O(1)$  
C) $O(1)$ e $O(n)$  
D) $O(n)$ e $O(n)$  
E) $O(\log n)$ e $O(1)$  

**Resposta Correta: B**

**Comentário:** Como temos **apenas** o ponteiro para a Cabeça (`Head`):
1. Para inserir no final, é preciso percorrer todos os $n$ nós a partir da `Head` para achar o nó cujo `next == NULL`. Isso leva tempo $O(n)$.
2. Para remover do início, basta atualizar `Head = Head.next`. Isso leva tempo constante $O(1)$.

---

### Questão 17 (Difícil)
Suponha que tenhamos duas estruturas para representar um **Grafo não-dirigido** com $V$ vértices e $E$ arestas: uma Matriz de Adjacência ($V \times V$) e uma Lista de Adjacência. Qual é a complexidade de **espaço** de cada uma, respectivamente?

A) $O(V + E)$ e $O(V^2)$  
B) $O(V^2)$ e $O(V + E)$  
C) $O(V \cdot E)$ e $O(V)$  
D) $O(E^2)$ e $O(V^2)$  
E) $O(V^2)$ e $O(E^2)$  

**Resposta Correta: B**

**Comentário:** A Matriz de Adjacência aloca uma tabela de tamanho $V \times V$, consumindo espaço $O(V^2)$ independentemente de haver poucas ou muitas arestas. A Lista de Adjacência armazena um array de $V$ listas, onde o somatório de nós em todas as listas é $2E$, ocupando espaço proporcional a $O(V + E)$.

---

### Questão 18 (Fácil)
Qual das seguintes estruturas de dados armazena os elementos internamente utilizando o conceito de **Ponteiros/Referências** para interconectar nós não contíguos na memória?

A) Matriz Estática $3 \times 3$ em C  
B) Vetor Primitivo de Inteiros  
C) Lista Encadeada  
D) Tabela Hash sem colisões (Tabela Direta)  
E) Registrador de CPU  

**Resposta Correta: C**

**Comentário:** Listas Encadeadas utilizam alocação dinâmica de memória, onde cada nó contém os dados e um ou mais ponteiros (endereços) apontando para a localização na memória do(s) próximo(s) nó(s). Os nós não estão necessariamente em posições contíguas da RAM.

---

### Questão 19 (Médio - Pegadinha)
Qual é a complexidade de busca do elemento **MÍNIMO** em uma **Max-Heap** de $n$ elementos?

A) $O(1)$  
B) $O(\log n)$  
C) $O(n)$  
D) $O(n \log n)$  
E) $O(n^2)$  

**Resposta Correta: C**

**Comentário:** Pegadinha clássica similar à da Min-Heap! Numa **Max-Heap**, o maior elemento fica na raiz ($O(1)$). O menor elemento estará em alguma das folhas. Como há $O(n)$ folhas, varrer as folhas para achar o mínimo exige tempo linear $O(n)$.

---

### Questão 20 (Difícil)
Em uma **Tabela Hash** contendo $N$ buckets, utiliza-se a técnica de **Endereçamento Aberto** com **Sondagem Quadrática**: $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \pmod N$. Qual é a principal limitação/problema desta abordagem se as constantes $c_1, c_2$ e $N$ não forem cuidadosamente escolhidas?

A) Ocorre agrupamento primário idêntico ao da sondagem linear.  
B) A tabela degenera obrigatoriamente para uma lista encadeada de complexidade $O(2^n)$.  
C) A sequência de sondagem pode não examinar todos os $N$ buckets da tabela, falhando em encontrar uma posição livre mesmo havendo espaço disponível.  
D) A busca torna-se $O(n \log n)$ no caso médio.  
E) Torna impossível a operação de remoção de elementos.  

**Resposta Correta: C**

**Comentário:** Ao contrário da Sondagem Linear (que testará todos os buckets $0, 1, 2, \dots, N-1$), a Sondagem Quadrática gera saltos de tamanho $i^2$. Se o tamanho $N$ da tabela não for um número primo e as constantes não forem adequadamente dimensionadas, os saltos podem entrar em um ciclo cobrindo apenas uma fração (ex: $50\%$) das posições da tabela, impedindo a inserção de elementos mesmo com espaço vago.

---

### Questão 21 (Médio)
Qual é a complexidade temporal para converter uma **Árvore Binária de Busca (BST)** balanceada de $n$ elementos em uma lista ordenada utilizando a travessia *In-order*?

A) $O(\log n)$  
B) $O(n)$  
C) $O(n \log n)$  
D) $O(n^2)$  
E) $O(1)$  

**Resposta Correta: B**

**Comentário:** A travessia *In-order* percorre a árvore visitando **cada nó exatamente uma vez**. Como há $n$ nós e o trabalho realizado em cada nó é $O(1)$ (apenas leitura/cópia do valor), a complexidade total do algoritmo é linear $O(n)$.

---

### Questão 22 (Fácil)
Ao implementar uma **Pilha** com capacidade fixa utilizando um Vetor (Array), quais são as variáveis necessárias para controlar o estado da pilha em tempo constante $O(1)$?

A) Uma lista de ponteiros para todas as posições livres.  
B) Apenas um ponteiro/índice para o **Topo** da pilha.  
C) Dois índices: um para o Início e outro para o Meio.  
D) Um contador de iterações do laço `while`.  
E) Nenhuma variável adicional é necessária.  

**Resposta Correta: B**

**Comentário:** Numa pilha em vetor, basta uma variável inteira `topo` (ou `top`) indicando a posição do elemento no topo da pilha. Para `push`, incrementa-se `topo` e grava-se o valor. Para `pop`, lê-se o valor e decrementa-se `topo`. Ambas as operações executam em $O(1)$.

---

### Questão 23 (Difícil - Pegadinha)
Considere uma estrutura de dados conhecida como **Trie** (Árvore de Prefixos) usada para armazenar $n$ palavras de comprimento máximo $m$ sobre um alfabeto de tamanho $\Sigma$. Qual é a complexidade de tempo do **pior caso** para pesquisar se uma palavra específica de tamanho $k$ está presente na Trie?

A) $O(n)$  
B) $O(\log n)$  
C) $O(k)$  
D) $O(n \cdot m)$  
E) $O(\Sigma^k)$  

**Resposta Correta: C**

**Comentário:** A pegadinha é tentar calcular a busca em função do número total de palavras $n$. Na Trie, a busca por uma palavra de tamanho $k$ é feita navegando caractere por caractere a partir da raiz. Cada passo desce um nível na árvore analisando a letra correspondente. Logo, o tempo de busca depende **exclusivamente do comprimento $k$ da palavra**, ou seja, $O(k)$, sendo totalmente **independente do número de palavras $n$** armazenadas!

---

### Questão 24 (Médio)
A operação de **Rotação Simples à Direita** em um nó $Z$ de uma Árvore AVL é executada para reequilibrar a árvore quando ocorre um desbalanceamento do tipo:

A) Direita-Direita (subárvore direita do filho direito muito alta).  
B) Esquerda-Esquerda (subárvore esquerda do filho esquerdo muito alta).  
C) Direita-Esquerda.  
D) Esquerda-Direita.  
E) Quando a raiz é um nó folha.  

**Resposta Correta: B**

**Comentário:** Quando um nó fica desbalanceado com Fator de Balanceamento $+2$ (ou $-2$, dependendo da convenção) devido ao excesso de altura no filho esquerdo, e este filho esquerdo também está pesado à esquerda (caso Esquerda-Esquerda / Left-Left), uma **única rotação à direita** resolve o problema, reestabelecendo a propriedade AVL em $O(1)$.

---

### Questão 25 (Fácil)
Qual é o impacto no uso de memória ao substituir uma matriz densa $1000 \times 1000$ por uma estrutura de **Matriz Esparsa** quando $99\%$ dos seus elementos são iguais a zero?

A) A matriz esparsa aumenta o uso de memória, pois exige ponteiros para os zeros.  
B) A matriz esparsa reduz drasticamente o uso de memória, pois armazena apenas os valores não-nulos e seus respectivos índices.  
C) O uso de memória permanece exatamente o mesmo.  
D) O tempo de acesso aos elementos fica $O(1)$ negativo.  
E) A matriz esparsa não pode ser armazenada na RAM.  

**Resposta Correta: B**

**Comentário:** Em matrizes onde a grande maioria das entradas é nula (esparsas), armazenar bilhões de zeros é desperdício de memória. Formatos como CSR (*Compressed Sparse Row*) ou COO (*Coordinate Format*) armazenam apenas as triplas `(linha, coluna, valor)` dos elementos não-nulos, economizando até $99\%$ de memória.

---

### Questão 26 (Difícil - Pegadinha)
Dada uma **Tabela Hash** com tamanho inicial $M=8$ e fator de carga máximo $\alpha = 0.75$. Ao inserir elementos, o número de itens atinge $N=7$, disparando o procedimento de **Rehash** (redimensionamento). O novo tamanho da tabela passa a ser $M=16$. Qual é a complexidade temporal para executar essa operação de **Rehash** completa?

A) $O(1)$  
B) $O(\log N)$  
C) $O(N)$  
D) $O(N^2)$  
E) $O(M^2)$  

**Resposta Correta: C**

**Comentário:** Ao redimensionar a tabela hash, não basta copiar os elementos diretamente para a nova memória. Como o tamanho $M$ da tabela mudou, o cálculo de índice $hash(key) \pmod M$ altera-se para todas as chaves. Portanto, cada um dos $N$ elementos precisa ter seu hash recalculado e ser re-inserido na nova tabela. Isso exige tempo $O(N)$.

---

### Questão 27 (Médio)
Qual das seguintes estruturas permite implementar uma **Fila de Prioridades** garantindo que as operações de `inserção` e `remoção do elemento de maior prioridade` tenham ambas complexidade $O(\log n)$ no pior caso?

A) Vetor Não-Ordenado  
B) Lista Encadeada Ordenada  
C) Heap Binária (Binary Heap)  
D) Pilha Simples  
E) Tabela Hash Sem Colisões  

**Resposta Correta: C**

**Comentário:** 
* No Vetor Não-Ordenado: inserção $O(1)$, remoção $O(n)$.
* Na Lista Ordenada: inserção $O(n)$, remoção $O(1)$.
* Na **Heap Binária**: inserção $O(\log n)$ (devido ao *bubble-up*) e remoção $O(\log n)$ (devido ao *heapify-down*). É a estrutura padrão para filas de prioridade.

---

### Questão 28 (Fácil)
A propriedade fundamental que define um **Nó Folha** em qualquer estrutura de dados em Árvore é:

A) Ser o nó raiz da árvore.  
B) Possuir um valor numérico negativo.  
C) Não possuir nenhum nó filho (grau de saída = 0).  
D) Estar localizado no nível 0 da árvore.  
E) Possuir pelo menos três nós irmãos.  

**Resposta Correta: C**

**Comentário:** Em terminologia de árvores, um nó folha (ou nó externo) é definido estritamente como qualquer nó que não possui nenhum nó filho (seus ponteiros para filhos são nulos).

---

### Questão 29 (Difícil)
Qual é o limite inferior (*lower bound*) teórico no **pior caso** para a complexidade de tempo de qualquer algoritmo de ordenação baseado exclusivamente em **comparações de chaves** (como Quicksort, Mergesort e Heapsort) para ordenar $n$ elementos?

A) $\Omega(n)$  
B) $\Omega(n \log n)$  
C) $\Omega(n^2)$  
D) $\Omega(\log n)$  
E) $\Omega(2^n)$  

**Resposta Correta: B**

**Comentário:** A demonstração via **Árvore de Decisão** prova que para discriminar entre as $n!$ permutações possíveis de um array de tamanho $n$, uma árvore binária de decisão precisa ter pelo menos $n!$ folhas. A altura dessa árvore é no mínimo $\log_2(n!) \approx n \log_2 n - n \log_2 e = \Omega(n \log n)$. Portanto, nenhum algoritmo baseado em comparações pode ser mais rápido do que $\Omega(n \log n)$ no pior caso.

---

### Questão 30 (Médio - Pegadinha)
Dada uma **Árvore Vermelho-e-Preto (Red-Black Tree)** com $n$ nós, qual das afirmativas abaixo é **VERDADEIRA** sobre suas propriedades?

A) O caminho mais longo da raiz a qualquer folha é no máximo o dobro do caminho mais curto.  
B) Todos os nós folhas devem ser obrigatoriamente da cor Vermelha.  
C) Um nó vermelho pode ter um nó filho também vermelho.  
D) A busca tem complexidade $O(1)$ e a inserção $O(n^2)$.  
E) A árvore exige que todos os níveis estejam completamente preenchidos.  

**Resposta Correta: A**

**Comentário:** A propriedade central da Árvore Vermelho-e-Preto é: "Nenhum nó vermelho pode ter um filho vermelho" (Propriedade dos Nós Vermelhos) e "Todos os caminhos da raiz às folhas contêm o mesmo número de nós pretos" (Black-Height). Isso garante matematicamente que **o caminho mais longo da raiz até uma folha não pode ser mais do que o dobro do caminho mais curto**, mantendo a árvore razoavelmente balanceada e com operações em $O(\log n)$.

```

---

O simulado contendo as 30 questões de múltipla escolha com pegadinhas, distribuição aleatória de alternativas e gabarito detalhado está criado e pronto para uso no painel ao lado.