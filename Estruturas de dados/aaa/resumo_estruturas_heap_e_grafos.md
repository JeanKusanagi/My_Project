# Resumo Avançado: Heaps, Algoritmos de Grafos e Complexidade Assintótica

Este documento reúne uma análise matemática rigorosa das estruturas de dados baseadas em Heap e suas aplicações nos algoritmos de ordenação e grafos.

---

## 1. O Heapsort e o Conceito de Ordenação In-Place

O **Heapsort** é um algoritmo de ordenação por comparação que atua diretamente sobre o array original, apresentando complexidade de tempo $\mathcal{O}(n \log n)$ em todos os casos (pior, melhor e médio) e complexidade de espaço auxiliar $\mathcal{O}(1)$, o que o classifica como um algoritmo **in-place**.

A ordenação baseia-se em uma árvore binária quase completa mapeada implicitamente sobre um array indexado de $1$ a $n$:
- $\text{Pai}(i) = \lfloor i / 2 \rfloor$
- $\text{Esquerdo}(i) = 2i$
- $\text{Direito}(i) = 2i + 1$

### Demonstração Matemática do Custo Linear $\mathcal{O}(n)$ do `Build-Max-Heap`
Embora uma análise superficial sugira que construir um heap fazendo $n$ chamadas ao `Max-Heapify` custaria $\mathcal{O}(n \log n)$, o custo real é linear $\mathcal{O}(n)$.

A altura $h$ de um nó varia de $0$ (folhas) até $\lfloor \log_2 n \rfloor$ (raiz). O número máximo de nós em qualquer altura $h$ em uma árvore de tamanho $n$ é $\lceil n / 2^{h+1} \rceil$. O tempo para executar o `Max-Heapify` em um nó de altura $h$ é $\mathcal{O}(h)$. O custo total $T_{\text{Build}}$ é delimitado por:

$$T_{\text{Build}}(n) \le \sum_{h=0}^{\lfloor \log_2 n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil \mathcal{O}(h) = \mathcal{O}\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right)$$

Pela propriedade da série geométrica infinita baseada em derivadas, sabemos que:
$$\sum_{h=0}^{\infty} \frac{h}{2^h} = 2$$

Substituindo de volta na equação:
$$T_{\text{Build}}(n) = \mathcal{O}(n \cdot 2) = \mathbf{\mathcal{O}(n)}$$

A segunda fase do algoritmo (extração e ordenação) realiza $n-1$ chamadas de `Max-Heapify` na raiz, custando $\sum_{i=2}^{n} \mathcal{O}(\log i) = \mathcal{O}(n \log n)$. Portanto, o custo total do Heapsort é dominado pela segunda fase: $\mathcal{O}(n) + \mathcal{O}(n \log n) = \mathbf{\mathcal{O}(n \log n)}$.

---

## 2. O Heap de Fibonacci e a Avaliação Preguiçosa (Lazy)

O **Heap de Fibonacci** é uma coleção de árvores ordenadas que violam deliberadamente a rigidez estrutural em prol da eficiência temporal assintótica. Ele adia a consolidação de seus nós até o momento em que uma extração do mínimo é estritamente obrigatória.

O nome advém da propriedade matemática em que o tamanho mínimo de uma subárvore enraizada em um nó de grau $k$ é limitado pelo $(k+2)$-ésimo número de Fibonacci ($F_{k+2}$), o que limita o grau máximo de qualquer nó a $\mathcal{O}(\log n)$.

### Tabela Comparativa de Operações (Custos Amortizados)

| Operação | Heap Binário | Heap Binomial | Heap de Fibonacci |
| :--- | :--- | :--- | :--- |
| **`insert`** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(1)$** |
| **`union`** | $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(1)$** |
| **`decrease-key`** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(1)$** |
| **`extract-min`** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(\log n)$** |

### Mecanismos Internos de Controle

1. **Consolidação de Árvores (no `extract-min`):** Ao remover o elemento mínimo, todos os seus filhos tornam-se raízes na lista principal. O algoritmo realiza uma varredura utilizando um array auxiliar indexado pelo grau da árvore. Árvores de mesmo grau sofrem fusão (a de maior chave torna-se filha da de menor chave) de forma iterativa até que restem apenas raízes com graus estritamente distintos.
2. **Corte em Cascata (no `decrease-key`):** Se uma chave é reduzida violando a propriedade do min-heap, ela é cortada de seu pai e movida para a lista de raízes. Para evitar o desbalanceamento estrutural (árvores longas e magras), aplica-se a regra de que um nó interno só pode perder **um** filho. Se perder o segundo filho (rastreado por um bit `mark`), esse pai é cortado em cascata e levado recursivamente para a lista de raízes.

---

## 3. Aplicações em Grafos: Dijkstra e Prim

Tanto o algoritmo de **Dijkstra** (caminhos mínimos a partir de uma origem) quanto o algoritmo de **Prim** (Árvore Geradora Mínima) possuem estruturas de execução idênticas sob a ótica da teoria da computação. Ambos são algoritmos gulosos (*greedy*) estruturados em um laço principal baseado em duas operações repetitivas sobre a fila de prioridades:

- **$V$ operações** de `extract-min` (uma para cada vértice).
- **Até $E$ operações** de `decrease-key` (uma para cada aresta relaxada ou avaliada).

### A Diferença Conceitual no Relaxamento

- **Dijkstra:** Avalia a distância acumulada a partir da raiz.
  $$\text{Se } \text{dist}[u] + w(u, v) < \text{dist}[v] \implies \text{Atualiza por } \text{decrease-key}$$
- **Prim:** Avalia estritamente o peso isolado da aresta que conecta o vértice à árvore existente.
  $$\text{Se } w(u, v) < \text{key}[v] \implies \text{Atualiza por } \text{decrease-key}$$

### Análise da Complexidade de Acordo com a Fila de Prioridades

O custo total combinado de execução é dado pela equação:
$$\text{Custo Total} = V \cdot T_{\text{extract-min}} + E \cdot T_{\text{decrease-key}}$$

#### Cenário 1: Implementação com Heap Binário
Dado que tanto `extract-min` quanto `decrease-key` custam $\mathcal{O}(\log V)$:
$$\text{Custo} = V \cdot \mathcal{O}(\log V) + E \cdot \mathcal{O}(\log V) = \mathbf{\mathcal{O}((V + E) \log V)}$$

#### Cenário 2: Implementação com Heap de Fibonacci
Como `decrease-key` cai para tempo constante amortizado $\mathcal{O}(1)$:
$$\text{Custo} = V \cdot \mathcal{O}(\log V) + E \cdot \mathcal{O}(1) = \mathbf{\mathcal{O}(E + V \log V)}$$

### O Paradoxo Teoria vs. Prática
Embora o Heap de Fibonacci reduza a complexidade de algoritmos em grafos densos ($E \approx V^2$) eliminando o fator logarítmico das arestas, **na prática industrial o Heap Binário costuma ser superior**. O alto fator constante de sobrecarga (*overhead*) de memória do Heap de Fibonacci (múltiplos ponteiros por nó, bits de marcação e inteiros de grau) destrói a **localidade de cache** que o Heap Binário nativamente usufrui ao operar em blocos contíguos de memória estruturados em array.