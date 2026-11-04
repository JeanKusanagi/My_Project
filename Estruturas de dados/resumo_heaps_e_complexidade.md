# Estudo Avançado: Heaps, Algoritmos de Grafos e Complexidade Assintótica

Este documento reúne uma análise teórica e matemática aprofundada sobre as estruturas de dados baseadas em **Heaps**, suas variantes avançadas como o **Heap de Fibonacci**, e seus impactos diretos em algoritmos fundamentais como **Heapsort** e **Dijkstra**.

---

## 1. O Heapsort e a Propriedade In-Place

O **Heapsort** é um algoritmo de ordenação por comparação clássico que apresenta complexidade de tempo $\mathcal{O}(n \log n)$ em todos os casos (pior, melhor e médio). Seu grande diferencial prático é ser um algoritmo **in-place**, operando com espaço adicional constante $\mathcal{O}(1)$.

### Representação Vetorial da Árvore
Para evitar o uso de ponteiros e memória extra, o Heap mapeia uma árvore binária quase completa diretamente sobre os índices de um array $A$ (indexado de $1$ a $n$):

*   $\text{Pai}(i) = \lfloor i / 2 \rfloor$
*   $\text{Esquerdo}(i) = 2i$
*   $\text{Direito}(i) = 2i + 1$

A propriedade do **Max-Heap** exige que:
$$\forall i \in [2, n], \quad A[\text{Pai}(i)] \ge A[i]$$

### Análise Matemática do Build-Max-Heap
Embora a operação `Max-Heapify` custe $\mathcal{O}(\log n)$ e seja executada $n/2$ vezes na fase de construção, o custo total do `Build-Max-Heap` é linear, ou seja, $\mathcal{O}(n)$.

A altura $h$ de um nó varia de $0$ (folhas) até $\lfloor \log_2 n \rfloor$ (raiz). O número máximo de nós em qualquer altura $h$ é $\lceil n / 2^{h+1} \rceil$. Como o tempo para executar o Heapify é proporcional à altura $\mathcal{O}(h)$, o custo total é modelado por:

$$T_{\text{Build}}(n) \le \sum_{h=0}^{\lfloor \log_2 n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil \mathcal{O}(h) = \mathcal{O}\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right)$$

Dada a convergência da série geométrica derivada $\sum_{h=0}^{\infty} \frac{h}{2^h} = 2$, temos:
$$T_{\text{Build}}(n) = \mathcal{O}(n \cdot 2) = \mathbf{\mathcal{O}(n)}$$

---

## 2. Heap de Fibonacci e Avaliação Preguiçosa (Lazy)

O **Heap de Fibonacci** foi projetado para otimizar operações que acontecem com alta frequência em algoritmos de grafos. Ele utiliza o conceito de **avaliação preguiçosa (*lazy evaluation*)**, adiando a consolidação da estrutura até o momento estrito em que uma remoção (`extract-min`) é solicitada.

### Tabela Comparativa de Complexidade Amortizada

| Operação | Heap Binário | Heap Binomial | Heap de Fibonacci (Amortizado) |
| :--- | :--- | :--- | :--- |
| **`insert`** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(1)$** |
| **`union`** | $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(1)$** |
| **`decrease-key`** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(1)$** |
| **`extract-min`** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | **$\mathcal{O}(\log n)$** |

### Consolidação de Árvores (`extract-min`)
Quando o menor elemento é extraído, a faxina estrutural é ativada. O algoritmo promove todos os filhos do nó mínimo a raízes e inicia uma varredura utilizando um array auxiliar indexado pelo **grau** (número de filhos) das árvores. Sempre que duas árvores com o mesmo grau são encontradas, elas sofrem **fusão**: a de maior chave torna-se filha da de menor chave, incrementando o grau desta em $1$. Este processo repete-se recursivamente até estabilizar a floresta.

### Corte em Cascata (`decrease-key`)
Para garantir o tempo $\mathcal{O}(1)$ ao reduzir o valor de uma chave, se a propriedade do heap for violada, o nó modificado é cortado de seu pai e movido para a lista de raízes. 

Para impedir que as árvores fiquem desbalanceadas e lineares, adota-se a regra do bit de marcação (`mark`): **um nó não-raiz pode perder no máximo um filho**.
*   Se o pai $Y$ do nó cortado não for raiz e já estiver marcado (`mark == true`), significa que ele está perdendo seu *segundo* filho.
*   O algoritmo então realiza um **corte em cascata**, desvinculando $Y$ de seu respectivo pai $Z$ e jogando-o também nas raízes. O processo sobe recursivamente pela árvore até encontrar um nó não marcado (que agora recebe a marca) ou atingir uma raiz.

---

## 3. Impacto Teórico no Algoritmo de Dijkstra

O algoritmo de **Dijkstra** calcula caminhos mínimos a partir de uma origem executando exatamente $V$ operações de `extract-min` e, no pior caso, $E$ operações de `decrease-key` (relaxamento de arestas).

O custo total é expresso matematicamente por:
$$\text{Custo Total} = V \cdot T_{\text{extract-min}} + E \cdot T_{\text{decrease-key}}$$

*   **Com Heap Binário:** $V \cdot \mathcal{O}(\log V) + E \cdot \mathcal{O}(\log V) = \mathbf{\mathcal{O}((V + E) \log V)}$
*   **Com Heap de Fibonacci:** $V \cdot \mathcal{O}(\log V) + E \cdot \mathcal{O}(1) = \mathbf{\mathcal{O}(E + V \log V)}$

Em grafos altamente densos onde $E \approx V^2$, o Heap de Fibonacci reduz o limite teórico de $\mathcal{O}(V^2 \log V)$ para uma complexidade puramente quadrática **$\mathcal{O}(V^2)$**, eliminando a dependência logarítmica das arestas.

*Nota Prática: Apesar da vantagem teórica do Heap de Fibonacci para grafos densos, a sobrecarga de ponteiros e a falta de localidade de cache fazem com que o Heap Binário baseado em arrays seja frequentemente mais veloz em aplicações industriais reais.*