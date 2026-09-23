# SIMULADO — Estruturas de Dados e Complexidades
### Vetor, matriz, pilha, fila, listas encadeadas, heap, árvores e tabela hash

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas clássicas sobre complexidade de tempo e espaço.

---

**1.** Em um **vetor (array)** estático, o acesso a um elemento por índice tem complexidade de tempo:

a) O(n), pois é preciso percorrer todos os elementos anteriores<br>
b) O(1), pois a posição de memória do elemento pode ser calculada diretamente a partir do índice e do endereço base<br>
c) O(log n), usando busca binária<br>
d) O(n²), no pior caso

> **Gabarito: b.** O acesso indexado a um vetor é O(1) (tempo constante), pois a posição na memória é calculada diretamente por aritmética de endereços (endereço_base + índice × tamanho_do_elemento), sem necessidade de percorrer a estrutura.

---

**2.** **(Pegadinha)** Inserir um elemento no **início** de um vetor estático já preenchido (deslocando os demais elementos) tem complexidade de tempo:

a) O(1), pois vetores permitem inserção instantânea em qualquer posição<br>
b) O(n), pois é necessário deslocar todos os elementos existentes uma posição à frente para abrir espaço no início<br>
c) O(log n), usando um algoritmo de busca binária para achar a posição<br>
d) O(1) amortizado, como em listas dinâmicas

> **Gabarito: b.** Pegadinha: diferente do acesso por índice (O(1)), inserir no início de um vetor exige deslocar todos os *n* elementos existentes, tornando essa operação O(n) — muito mais cara do que se costuma supor à primeira vista.

---

**3.** Uma **matriz** bidimensional de tamanho m×n, armazenada de forma contígua na memória (row-major order), tem o acesso a um elemento A[i][j] com complexidade:

a) O(m × n), pois é preciso percorrer toda a matriz<br>
b) O(1), pois a posição do elemento pode ser calculada diretamente a partir de i, j e das dimensões da matriz<br>
c) O(m + n)<br>
d) O(log(m × n))

> **Gabarito: b.** Assim como em vetores unidimensionais, o acesso a um elemento de uma matriz armazenada de forma contígua é O(1), calculado por uma fórmula direta de endereçamento (ex.: endereço_base + (i × n + j) × tamanho_do_elemento).

---

**4.** Uma **pilha (stack)** segue a disciplina de acesso:

a) FIFO (First In, First Out) — o primeiro elemento inserido é o primeiro a sair<br>
b) LIFO (Last In, First Out) — o último elemento inserido é o primeiro a sair<br>
c) Acesso aleatório, sem ordem específica<br>
d) Ordenação crescente automática dos elementos

> **Gabarito: b.** Pilhas seguem a lógica LIFO: a última operação de inserção (push) é a primeira a ser removida (pop) — como uma pilha de pratos.

---

**5.** As operações de **push** (inserir) e **pop** (remover) em uma pilha implementada com um vetor (com espaço suficiente e sem necessidade de redimensionamento) têm complexidade de tempo:

a) O(n), pois é preciso reorganizar todos os elementos<br>
b) O(1), pois ambas as operações ocorrem apenas na extremidade (topo) da pilha, sem necessidade de deslocar outros elementos<br>
c) O(log n)<br>
d) O(n²)

> **Gabarito: b.** Como push e pop ocorrem exclusivamente no topo da pilha (geralmente a última posição ocupada do vetor), não há necessidade de deslocar elementos, resultando em complexidade O(1).

---

**6.** Uma **fila (queue)** segue a disciplina de acesso:

a) LIFO (Last In, First Out)<br>
b) FIFO (First In, First Out) — o primeiro elemento inserido é o primeiro a sair<br>
c) Prioridade decrescente automática<br>
d) Acesso apenas ao elemento do meio da estrutura

> **Gabarito: b.** Filas seguem a lógica FIFO: o primeiro elemento a entrar (enqueue) é o primeiro a sair (dequeue) — como uma fila de atendimento.

---

**7.** **(Pegadinha)** Se uma fila for implementada de forma **ingênua** com um vetor, removendo sempre o elemento da posição 0 e deslocando fisicamente todos os elementos restantes uma posição para trás a cada remoção, a operação de **dequeue** (remover do início) terá complexidade:

a) O(1), pois remover do início é sempre rápido em vetores<br>
b) O(n), devido à necessidade de deslocar todos os elementos restantes após a remoção do primeiro — por isso, implementações eficientes de filas com vetor costumam usar a técnica de **buffer circular**, evitando esse deslocamento<br>
c) O(log n), usando busca binária para localizar o próximo elemento<br>
d) O(1) amortizado, exatamente como em uma pilha

> **Gabarito: b.** Pegadinha: embora o dequeue conceitualmente pareça uma operação "simples", a implementação ingênua com vetor comum exige deslocar todos os elementos restantes, custando O(n) — daí a importância prática do buffer circular (fila circular), que evita esse deslocamento e mantém dequeue em O(1).

---

**8.** Em uma **lista encadeada simples (singly linked list)**, a inserção de um novo elemento **no início** da lista (já com ponteiro/referência para a cabeça) tem complexidade:

a) O(n), pois é preciso percorrer toda a lista<br>
b) O(1), pois basta criar o novo nó e ajustar o ponteiro da cabeça, sem necessidade de deslocar nenhum outro elemento<br>
c) O(log n)<br>
d) O(n²)

> **Gabarito: b.** Diferente de vetores, a inserção no início de uma lista encadeada não exige deslocamento de elementos — apenas o ajuste de referências/ponteiros, resultando em O(1).

---

**9.** **(Pegadinha)** Em uma **lista encadeada simples** (sem ponteiro para o final/tail armazenado), a inserção de um novo elemento **no final** da lista tem complexidade:

a) O(1), assim como a inserção no início<br>
b) O(n), pois, sem uma referência direta ao último nó, é necessário percorrer toda a lista a partir da cabeça até encontrar o último elemento antes de inserir o novo<br>
c) O(log n), usando uma técnica de busca binária sobre os nós<br>
d) Impossível de ser realizada em listas encadeadas simples

> **Gabarito: b.** Pegadinha: muitos assumem, por analogia com a inserção no início, que inserir no final também seria O(1) — mas, sem uma referência direta ao último nó (tail), é necessário percorrer toda a lista para localizá-lo, custando O(n). (Nota: se a implementação mantiver um ponteiro para o tail, a inserção no final também pode ser O(1).)

---

**10.** Qual é a principal vantagem de uma **lista duplamente encadeada (doubly linked list)** em relação a uma lista simplesmente encadeada?

a) Ocupa sempre menos memória, por nó, do que a lista simples<br>
b) Permite percorrer a lista em ambas as direções (para frente e para trás) e realizar remoções de um nó específico de forma mais eficiente, sem a necessidade de percorrer a lista desde o início apenas para encontrar o nó anterior<br>
c) Elimina totalmente a necessidade de ponteiros<br>
d) É a única estrutura que permite armazenar dados de tipos diferentes

> **Gabarito: b.** A lista duplamente encadeada mantém referências tanto para o próximo quanto para o nó anterior, permitindo navegação bidirecional e remoções mais diretas — ao custo de maior consumo de memória por nó (um ponteiro extra por elemento).

---

**11.** **(Pegadinha)** Sobre o consumo de memória, é correto afirmar que uma lista duplamente encadeada, em comparação com uma lista simplesmente encadeada com o mesmo número de elementos:

a) Consome exatamente a mesma quantidade de memória, pois ambas armazenam os mesmos dados<br>
b) Consome mais memória por nó, pois cada nó da lista dupla armazena um ponteiro adicional (para o nó anterior), além do ponteiro para o próximo nó já presente na lista simples<br>
c) Consome menos memória, pois a navegação bidirecional elimina a necessidade de um dos ponteiros<br>
d) O consumo de memória depende exclusivamente do tipo de dado armazenado, nunca da estrutura da lista

> **Gabarito: b.** Pegadinha: a vantagem funcional (navegação bidirecional) vem com um custo real de memória — cada nó da lista dupla armazena um ponteiro extra em comparação com a lista simples, o que é frequentemente esquecido ao se avaliar apenas os benefícios da estrutura.

---

**12.** Uma **lista circular** se diferencia de uma lista linear (simples ou dupla) principalmente por:

a) Não permitir a inserção de novos elementos<br>
b) O último nó apontar de volta para o primeiro nó (em vez de apontar para nulo/None), formando um ciclo, o que pode ser útil para estruturas que precisam de percurso cíclico contínuo (como escalonamento round-robin)<br>
c) Armazenar apenas números inteiros<br>
d) Ser, obrigatoriamente, uma lista duplamente encadeada

> **Gabarito: b.** Em uma lista circular, não existe um "fim" apontando para nulo — o último elemento aponta de volta ao primeiro, criando um ciclo, útil em cenários como filas circulares e algoritmos de escalonamento cíclico.

---

**13.** Um **heap binário** (min-heap ou max-heap) é uma estrutura de dados frequentemente implementada sobre:

a) Uma lista encadeada, exclusivamente<br>
b) Um vetor (array), aproveitando a estrutura de árvore binária completa implícita nos índices (o filho de um nó em posição i estando nas posições 2i+1 e 2i+2, por exemplo), sem necessidade de ponteiros explícitos<br>
c) Uma tabela hash<br>
d) Uma pilha

> **Gabarito: b.** Heaps binários são classicamente implementados sobre vetores, explorando a propriedade de árvore binária completa para calcular as posições de pais e filhos por aritmética de índices, evitando o overhead de ponteiros explícitos.

---

**14.** Em um **min-heap**, a propriedade estrutural fundamental é que:

a) Cada nó é sempre maior que seus filhos<br>
b) Cada nó é sempre menor ou igual a seus filhos, garantindo que o menor elemento de toda a estrutura esteja sempre na raiz<br>
c) Os elementos estão sempre ordenados de forma totalmente crescente ao se percorrer o vetor da esquerda para a direita<br>
d) Não existe nenhuma relação de ordem entre pais e filhos

> **Gabarito: b.** A propriedade de min-heap garante que o valor de cada nó seja menor ou igual ao de seus filhos — o que assegura que o menor elemento da estrutura esteja sempre na raiz, mas **não** implica uma ordenação total dos elementos no vetor (esse é um erro comum — ver próxima questão).

---

**15.** **(Pegadinha)** Considerando um min-heap representado em um vetor, é correto afirmar que:

a) O vetor está sempre completamente ordenado de forma crescente, da esquerda para a direita<br>
b) O vetor **não** está necessariamente ordenado de forma crescente — a única garantia é a relação de ordem entre cada nó pai e seus filhos diretos (propriedade de heap), não uma ordenação total entre todos os elementos do vetor<br>
c) Apenas o primeiro e o último elemento do vetor precisam respeitar alguma ordem<br>
d) A ordenação total do vetor é uma consequência automática e obrigatória da propriedade de heap

> **Gabarito: b.** Pegadinha muito comum: confundir "propriedade de heap" (relação pai-filho) com "vetor totalmente ordenado" — um heap garante apenas que cada pai seja menor (min-heap) ou maior (max-heap) que seus filhos diretos, não que o vetor, lido em sequência, esteja em ordem crescente/decrescente total.

---

**16.** As operações de **inserção** e **remoção da raiz** (extração do mínimo/máximo) em um heap binário com *n* elementos têm complexidade de tempo:

a) O(1) para ambas as operações<br>
b) O(log n) para ambas, devido à necessidade de "subir" (sift-up) ou "descer" (sift-down) o elemento ao longo da altura da árvore, que é proporcional a log n<br>
c) O(n) para ambas as operações<br>
d) O(n log n) para ambas as operações

> **Gabarito: b.** Como a altura de um heap binário completo com n elementos é O(log n), tanto a inserção (que pode exigir um sift-up até a raiz) quanto a remoção da raiz (que exige um sift-down após reposicionar o último elemento) têm complexidade O(log n).

---

**17.** Uma **Árvore Binária de Busca (BST)** mantém a propriedade de que, para cada nó:

a) Todos os valores na subárvore esquerda são maiores, e todos na subárvore direita são menores<br>
b) Todos os valores na subárvore esquerda são menores (ou iguais, dependendo da convenção), e todos os valores na subárvore direita são maiores que o valor do nó<br>
c) As subárvores esquerda e direita devem ter, obrigatoriamente, a mesma quantidade de nós<br>
d) Não existe nenhuma relação de ordem entre os nós

> **Gabarito: b.** Essa é a propriedade fundamental de uma BST: para todo nó, os valores à esquerda são menores e os valores à direita são maiores, o que permite buscas eficientes por comparação sucessiva.

---

**18.** **(Pegadinha)** Em uma BST **balanceada**, a complexidade de busca, inserção e remoção é O(log n). Já em uma BST que **não é balanceada** (por exemplo, resultante da inserção sequencial de elementos já ordenados), a complexidade dessas operações, no pior caso, pode chegar a:

a) O(1), pois BSTs são sempre eficientes, independentemente do balanceamento<br>
b) O(n), pois a árvore pode degenerar em uma estrutura semelhante a uma lista encadeada (todos os nós em uma única "cadeia"), perdendo a vantagem logarítmica<br>
c) O(log n), sempre, independentemente do balanceamento<br>
d) O(n²), pois cada nível da árvore desbalanceada dobra o número de comparações

> **Gabarito: b.** Pegadinha central sobre BSTs: sem mecanismos de balanceamento, inserir elementos já ordenados (ex.: 1, 2, 3, 4, 5...) faz a árvore degenerar em uma lista encadeada, com altura O(n) em vez de O(log n), degradando drasticamente o desempenho das operações.

---

**19.** Árvores como **AVL** e **Rubro-Negra (Red-Black Tree)** são exemplos de:

a) Estruturas que eliminam completamente a necessidade de comparação entre elementos<br>
b) Árvores binárias de busca **auto-balanceadas**, que aplicam rotações (e outras técnicas) após inserções e remoções para manter a altura da árvore em O(log n), garantindo desempenho eficiente mesmo em cenários adversos de inserção<br>
c) Tipos de tabelas hash, não de árvores<br>
d) Estruturas exclusivas para armazenamento de números de ponto flutuante

> **Gabarito: b.** AVL e árvores Rubro-Negras são BSTs auto-balanceadas: após cada inserção/remoção, aplicam rotações para manter a árvore aproximadamente balanceada, garantindo altura O(log n) e, consequentemente, operações eficientes mesmo no pior caso.

---

**20.** Uma **tabela hash (hash table)** utiliza, como ideia central, uma **função hash** para:

a) Ordenar os elementos de forma crescente automaticamente<br>
b) Mapear uma chave (key) para um índice (geralmente dentro de um vetor interno), permitindo, idealmente, acesso, inserção e remoção em tempo médio O(1)<br>
c) Comprimir os dados armazenados, reduzindo seu tamanho em disco<br>
d) Criptografar os dados de forma irreversível, sempre

> **Gabarito: b.** A função hash converte uma chave em um índice dentro do array interno da tabela, permitindo, em condições ideais (boa função hash e poucas colisões), acesso praticamente direto aos dados.

---

**21.** **(Pegadinha)** Qual é a complexidade de tempo, no **caso médio**, e no **pior caso**, para as operações de busca, inserção e remoção em uma tabela hash bem implementada?

a) O(1) no caso médio e O(1) no pior caso, sempre, para qualquer implementação<br>
b) O(1) no caso médio (assumindo uma boa função hash e baixo fator de carga), mas O(n) no pior caso, quando há muitas colisões (por exemplo, todas as chaves mapeando para o mesmo índice, no caso de encadeamento)<br>
c) O(log n) no caso médio e O(n) no pior caso<br>
d) O(n) no caso médio e O(1) no pior caso

> **Gabarito: b.** Pegadinha: é um erro muito comum tratar tabelas hash como "sempre O(1)" — essa é a complexidade esperada no **caso médio**, sob boas condições (boa função hash, fator de carga controlado); no **pior caso** (muitas colisões concentradas), a complexidade pode degenerar para O(n), como no caso extremo de todas as chaves colidindo em um único "balde" (bucket) tratado com lista encadeada.

---

**22.** O que é uma **colisão** em uma tabela hash?

a) Um erro fatal que impede totalmente o funcionamento da estrutura<br>
b) A situação em que duas (ou mais) chaves diferentes são mapeadas pela função hash para o mesmo índice/posição na tabela, exigindo alguma estratégia de tratamento (como encadeamento ou endereçamento aberto)<br>
c) A ordenação incorreta dos elementos dentro da tabela<br>
d) Um fenômeno que só ocorre em tabelas hash muito pequenas, nunca em tabelas grandes

> **Gabarito: b.** Colisões são inevitáveis em tabelas hash de tamanho finito (pelo Princípio da Casa dos Pombos, quando há mais chaves possíveis que posições), exigindo estratégias como encadeamento separado (chaining) ou endereçamento aberto (open addressing) para resolvê-las.

---

**23.** **(Pegadinha)** O **fator de carga** (load factor) de uma tabela hash, definido geralmente como o número de elementos armazenados dividido pelo número de posições (buckets) disponíveis, está relacionado a:

a) O tamanho exato de cada chave armazenada<br>
b) A probabilidade de colisões e o desempenho geral da tabela — fatores de carga muito altos aumentam a chance de colisões, degradando o desempenho médio das operações, o que geralmente motiva o redimensionamento (rehashing) da tabela quando esse limite é ultrapassado<br>
c) A quantidade de memória RAM disponível no sistema, um parâmetro externo à estrutura<br>
d) O número de threads utilizadas para acessar a estrutura simultaneamente

> **Gabarito: b.** Pegadinha: o fator de carga é uma métrica interna da tabela hash que impacta diretamente a probabilidade de colisões — implementações de qualidade monitoram esse valor e redimensionam a tabela (rehashing) quando ele ultrapassa um limiar razoável, mantendo o desempenho próximo de O(1) no caso médio.

---

**24.** Compare o **espaço** consumido por uma lista encadeada e por um vetor estático, ambos armazenando *n* elementos do mesmo tipo de dado. É correto afirmar que:

a) A lista encadeada sempre consome menos memória, pois não precisa de um tamanho fixo pré-alocado<br>
b) A lista encadeada tipicamente consome mais memória por elemento, devido ao armazenamento adicional de um (ou mais) ponteiros por nó, além do próprio dado — algo que o vetor não precisa, armazenando apenas os dados de forma contígua<br>
c) Ambas consomem exatamente a mesma quantidade de memória, sempre<br>
d) O vetor sempre consome mais memória, independentemente do cenário

> **Gabarito: b.** Pegadinha (comparação inversa à intuição): embora vetores exijam alocação contígua (às vezes com espaço extra não utilizado, se superdimensionados), listas encadeadas pagam um custo extra de memória por elemento, devido aos ponteiros de encadeamento — um trade-off importante na escolha entre as duas estruturas.

---

**25.** **(Pegadinha)** Um vetor **dinâmico** (como `ArrayList` em Java, `list` em Python ou `std::vector` em C++), que redimensiona automaticamente sua capacidade interna quando fica cheio (geralmente dobrando o tamanho), tem a operação de inserção no final com complexidade:

a) Sempre O(n), pois cada inserção pode exigir redimensionamento<br>
b) O(1) **amortizado**: embora inserções que disparam o redimensionamento custem O(n) naquele momento específico, essas operações caras são raras o suficiente para que o custo médio, distribuído ao longo de uma sequência de n inserções, seja O(1) por inserção<br>
c) O(log n), pois o redimensionamento usa uma estratégia de busca binária<br>
d) O(n²), no pior caso de qualquer sequência de inserções

> **Gabarito: b.** Pegadinha conceitual clássica: a análise de complexidade **amortizada** revela que, apesar de operações individuais de redimensionamento custarem O(n), a estratégia de dobrar a capacidade faz com que o custo médio por inserção, ao longo de muitas operações, seja O(1) — diferente de uma análise ingênua "pior caso por operação", que erroneamente concluiria O(n) para toda inserção.

---

**26.** Qual estrutura de dados é mais adequada para implementar o algoritmo de **busca em largura (BFS)** em um grafo, controlando a ordem de visitação dos nós?

a) Pilha (LIFO)<br>
b) Fila (FIFO)<br>
c) Heap de máximo<br>
d) Tabela hash, exclusivamente

> **Gabarito: b.** A BFS explora os nós "camada por camada", visitando primeiro os vizinhos mais próximos do nó inicial — esse comportamento é naturalmente implementado com uma fila (FIFO), que garante processar os nós na ordem em que foram descobertos.

---

**27.** **(Pegadinha)** Qual estrutura de dados é mais adequada para implementar o algoritmo de **busca em profundidade (DFS)** em um grafo, de forma iterativa (não recursiva)?

a) Fila (FIFO), assim como na BFS<br>
b) Pilha (LIFO), pois a DFS explora primeiro o ramo mais recentemente descoberto antes de retroceder — comportamento naturalmente equivalente ao de uma pilha (e, de fato, a versão recursiva da DFS usa implicitamente a pilha de chamadas da linguagem)<br>
c) Heap de mínimo, exclusivamente<br>
d) Tabela hash, pois a ordem de visitação é irrelevante na DFS

> **Gabarito: b.** Pegadinha: inverter as estruturas associadas a BFS e DFS é um erro comum — enquanto BFS usa fila (exploração em largura, por camadas), DFS usa pilha (exploração em profundidade, indo o mais fundo possível antes de retroceder).

---

**28.** Em relação à complexidade de espaço, uma **matriz esparsa** (com a grande maioria dos elementos iguais a zero ou a um valor padrão) armazenada de forma **densa** (todos os elementos explicitamente na memória, m×n posições) versus uma representação **esparsa** (armazenando apenas os elementos não nulos, por exemplo, em listas de coordenadas), é correto afirmar que:

a) A representação densa é sempre mais eficiente em espaço, independentemente da esparsidade<br>
b) Para matrizes com poucos elementos não nulos em relação ao total m×n, a representação esparsa tende a consumir significativamente menos memória, pois evita armazenar explicitamente os inúmeros elementos com valor padrão (geralmente zero)<br>
c) Não existe diferença de consumo de memória entre as duas representações, em nenhum cenário<br>
d) A representação esparsa sempre exige mais memória do que a densa, independentemente da proporção de zeros

> **Gabarito: b.** Quando a matriz tem poucos elementos não nulos em relação ao total de posições (m×n), representações esparsas (como listas de coordenadas, ou estruturas como dicionários de posições não nulas) evitam o desperdício de memória com valores repetidos e previsíveis (como zero), sendo muito mais econômicas nesse cenário específico.

---

**29.** **(Pegadinha)** Um estudante afirma: "Sempre que precisar de busca rápida, devo usar uma tabela hash, pois ela é sempre superior a uma árvore de busca balanceada em qualquer cenário." Essa afirmação está:

a) Correta, pois tabelas hash são sempre mais rápidas em qualquer operação<br>
b) Incorreta — tabelas hash oferecem O(1) esperado para busca, inserção e remoção, mas não mantêm os elementos ordenados nem suportam eficientemente operações como encontrar o mínimo, o máximo, ou percorrer os elementos em ordem — nesses casos, árvores de busca balanceadas (O(log n), mas ordenadas) são mais adequadas<br>
c) Correta, pois árvores de busca balanceadas nunca oferecem busca eficiente<br>
d) Incorreta, mas apenas porque tabelas hash nunca podem ser usadas para busca

> **Gabarito: b.** Pegadinha: a escolha entre tabela hash e árvore balanceada depende do que se precisa fazer com os dados — se a ordenação e operações de intervalo (mínimo, máximo, sucessor, predecessor, percurso ordenado) forem importantes, árvores balanceadas são mais adequadas, apesar de sua complexidade "apenas" logarítmica, em vez de O(1) esperado.

---

**30.** **(Pegadinha)** Um professor afirma: "Estrutura de dados X é sempre a melhor escolha, independentemente do problema, pois tem a menor complexidade assintótica no pior caso." Do ponto de vista de projeto de algoritmos e estruturas de dados, essa afirmação:

a) É sempre verdadeira, desde que X seja uma tabela hash, que domina qualquer outra estrutura em qualquer cenário<br>
b) É, em geral, uma simplificação equivocada — a escolha da estrutura de dados ideal depende do conjunto específico de operações necessárias (busca, inserção, remoção, ordenação, acesso sequencial etc.), do padrão de uso esperado (leitura intensiva vs. escrita intensiva), de restrições de memória e da necessidade ou não de manter ordenação, entre outros fatores — não existe uma estrutura universalmente ótima para todos os cenários<br>
c) É sempre verdadeira, desde que X seja uma árvore balanceada, que é comprovadamente ótima em qualquer contexto<br>
d) É irrelevante, pois toda estrutura de dados tem exatamente o mesmo desempenho na prática

> **Gabarito: b.** Pegadinha conceitual final, que resume o espírito de toda a prova: a escolha de estrutura de dados é sempre contextual — envolve trade-offs entre tempo de acesso, tempo de inserção/remoção, consumo de memória, necessidade de ordenação e padrão de uso, e não existe uma estrutura "vencedora universal" independentemente do problema a ser resolvido.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Os pontos mais recorrentes de pegadinha nesta prova foram: a **diferença entre acesso O(1) e inserção O(n) em vetores** (questões 1 e 2), a **falsa suposição de que heap = vetor totalmente ordenado** (questões 14 e 15), a **degeneração de BSTs não balanceadas em O(n)** (questão 18), a **complexidade amortizada de vetores dinâmicos** (questão 25), a **troca entre estruturas associadas a BFS (fila) e DFS (pilha)** (questões 26 e 27), e a ideia de que **"tabela hash é sempre a melhor escolha"** (questões 21 e 29) — vale reforçar esses pontos na correção em sala.
