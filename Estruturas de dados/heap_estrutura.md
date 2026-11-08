# Estrutura de Dados: Heap

O **heap** é uma estrutura de dados baseada em uma **árvore binária quase completa** que satisfaz obrigatoriamente a **propriedade do heap**. Isso significa que ela é preenchida nível por nível, da esquerda para a direita, e os nós mantêm uma relação de ordem específica com seus filhos:

*   **Max-Heap:** O valor de cada nó pai é *maior ou igual* ao valor de seus nós filhos. A raiz sempre contém o **maior elemento**.
*   **Min-Heap:** O valor de cada nó pai é *menor ou igual* ao valor de seus nós filhos. A raiz sempre contém o **menor elemento**.

Conceitualmente visualizado como uma árvore, o heap é estruturado de forma extremamente eficiente diretamente na memória usando um **vetor (array)**, onde as relações de parentesco são encontradas por aritmética simples de índices.

*(Nota: Não confunda a estrutura de dados Heap com a região de memória Heap usada para alocação dinâmica).*

---

## Complexidade de Tempo e Espaço

Por ser uma árvore estritamente balanceada (quase completa), a altura de um heap com $n$ elementos é sempre $O(\log n)$. Suas complexidades de tempo mapeiam-se da seguinte forma:

| Operação | Complexidade | Descrição / Motivação |
| :--- | :--- | :--- |
| **Buscar Máximo / Mínimo** | $O(1)$ | O elemento prioritário está sempre imediatamente acessível na raiz (índice 0). |
| **Inserção** | $O(\log n)$ | O elemento é inserido no final do vetor e "sobe" (*up-heap*) reposicionando-se conforme sua prioridade. |
| **Remoção (da Raiz)** | $O(\log n)$ | A raiz é trocada pelo último elemento, que depois "desce" (*down-heap / heapify*) para reorganizar a estrutura. |
| **Construção (*Build Heap*)** | $O(n)$ | Criar um heap a partir de um vetor desordenado leva tempo linear, aplicando o rearranjo de baixo para cima. |
| **Complexidade de Espaço** | $O(n)$ | Utiliza apenas o espaço do próprio vetor, sem ponteiros adicionais para filhos ou pais. |

---

## Vantagens do Heap

*   **Acesso Imediato ao Extremo:** Permite consultar instantaneamente $O(1)$ o maior ou menor elemento de um conjunto dinâmico.
*   **Eficiência em Atualizações:** Inserções e remoções são executadas de forma previsível em tempo logarítmico ($O(\log n)$), mesmo para milhões de itens.
*   **Economia de Memória (In-place):** Como pode ser implementado usando vetores simples, dispensa o gasto de memória com ponteiros (*pointers*) típicos de árvores binárias tradicionais.
*   **Ideal para Algoritmos de Prioridade:** É a base mais eficiente para implementar Filas de Prioridade, largamente utilizadas no algoritmo de caminho mínimo de *Dijkstra*, em ordenação de dados (*Heapsort*) e no escalonamento de processos em sistemas operacionais.

---

## Simulação de Movimentação no Vetor

Para entender a movimentação em um vetor com índice iniciando em **0**, utilizamos as seguintes fórmulas de navegação:
*   Se um nó está no índice `i`:
    *   O **Pai** dele está no índice `(i - 1) // 2`
    *   O **Filho Esquerdo** está em `2 * i + 1`
    *   O **Filho Direito** está em `2 * i + 2`

Abaixo, simulamos um **Max-Heap**.

### Parte 1: Inserção e Subida (*Up-Heap / Bubble-Up*)

Imagine o seguinte Max-Heap inicial no vetor: `[50, 30, 20, 15, 10]`
*(Em formato de árvore: 50 é a raiz; 30 e 20 são seus filhos; 15 e 10 são filhos do 30).*

Queremos **inserir o elemento 40**.

1.  **Passo 1: Inserção no final**
    O novo elemento é colocado na primeira posição livre (fim do vetor).
    *   Vetor atual: `[50, 30, 20, 15, 10, 40]`
    *   O elemento **40** está no índice `5`.
    *   Pai do índice 5: `(5 - 1) // 2 = 2`. O elemento no índice 2 é o **20**.

2.  **Passo 2: Primeira Comparação e Troca**
    Como 40 é maior que seu pai (20), a propriedade do Max-Heap foi violada. Eles trocam de lugar.
    *   Vetor atual: `[50, 30, 40, 15, 10, 20]`
    *   Agora, o **40** está no índice `2`.
    *   Novo pai do índice 2: `(2 - 1) // 2 = 0`. O elemento no índice 0 é o **50**.

3.  **Passo 3: Segunda Comparação e Parada**
    Como 40 é menor que seu pai (50), a estrutura está correta. O processo de subida para aqui.
    *   **Vetor final após inserção:** `[50, 30, 40, 15, 10, 20]`

---

### Parte 2: Remoção da Raiz e Descida (*Down-Heap / Heapify*)

Vamos remover o elemento prioritário (a raiz, índice 0), que atualmente é o **50**.

1.  **Passo 1: Substituição pela folha**
    Pegamos o último elemento (`20`, no índice 5) e o colocamos no lugar da raiz. O 50 é removido do vetor.
    *   Vetor atual: `[20, 30, 40, 15, 10]`
    *   O elemento **20** agora está na raiz (índice 0) e precisa descer para o seu lugar correto.

2.  **Passo 2: Primeira Comparação e Troca**
    O nó no índice 0 (`20`) olha para os seus dois filhos e deve trocar com o **maior** deles para garantir a propriedade do Max-Heap.
    *   Filho Esquerdo (índice 1): **30**
    *   Filho Direito (índice 2): **40**
    *   O maior filho é o **40**. Como 20 < 40, eles trocam de lugar.
    *   Vetor atual: `[40, 30, 20, 15, 10]`

3.  **Passo 3: Próxima Comparação e Parada**
    O elemento **20** agora está no índice `2`. Vamos checar seus novos filhos:
    *   Filho Esquerdo: `2 * 2 + 1 = 5` (Não existe, o vetor só vai até o índice 4).
    *   Como o 20 não tem mais filhos abaixo dele, ele se tornou uma folha. O processo de descida termina aqui.
    *   **Vetor final após remoção:** `[40, 30, 20, 15, 10]`

---

# Exemplo de Heap Binária

Uma **heap binária** (*Binary Heap*) é uma estrutura de dados baseada em uma árvore binária completa, utilizada principalmente na implementação de filas de prioridade e em algoritmos de ordenação, como o Heap Sort.

Existem dois tipos principais:

- **Max-Heap:** o valor de cada nó é maior ou igual aos valores de seus filhos. A raiz contém o maior elemento.
- **Min-Heap:** o valor de cada nó é menor ou igual aos valores de seus filhos. A raiz contém o menor elemento.

## 1. Exemplo de Max-Heap

Considere a inserção dos seguintes valores, nesta ordem:

**50, 30, 40, 10, 20, 35, 25**

A árvore é construída mantendo duas propriedades:

1. A árvore deve ser completa.
2. Cada nó pai deve ser maior ou igual aos seus filhos.

### Passo 1 – Inserir 50

```text
    50
```

### Passo 2 – Inserir 30

```text
    50
   /
  30
```

### Passo 3 – Inserir 40

```text
      50
     /  \
   30    40
```

### Passo 4 – Inserir 10

```text
       50
      /  \
    30    40
   /
  10
```

### Passo 5 – Inserir 20

```text
       50
      /  \
    30    40
   / \
  10  20
```

### Passo 6 – Inserir 35

```text
       50
      /  \
    30    40
   / \   /
  10  20 35
```

### Passo 7 – Inserir 25

```text
          50
        /    \
      30      40
     /  \    /  \
   10   20  35   25
```

A árvore resultante é uma Max-Heap válida, pois todos os nós pais possuem valores maiores ou iguais aos de seus respectivos filhos.

## 2. Representação em vetor

Uma heap binária pode ser armazenada em um vetor, sem a necessidade de utilizar ponteiros para representar os nós.

Para a Max-Heap construída, temos:

```text
Índice:  0   1   2   3   4   5   6
Valor:  50  30  40  10  20  35  25
```

Considerando índices iniciados em zero, as relações entre os nós são:

- Filho esquerdo de i: `2i + 1`.
- Filho direito de i: `2i + 2`.
- Pai de i: `(i - 1) // 2`.

Por exemplo, para o nó de índice 1 (valor 30):

- Pai: índice 0 (valor 50).
- Filho esquerdo: índice 3 (valor 10).
- Filho direito: índice 4 (valor 20).

## 3. Operação de remoção (Extract-Max)

Na Max-Heap, a remoção normalmente consiste em retirar o maior elemento, localizado na raiz.

Considere a heap:

```text
          50
        /    \
      30      40
     /  \    /  \
   10   20  35   25
```

**Passo 1:** Remover a raiz (50).

**Passo 2:** Substituir a raiz pelo último elemento (25).

```text
          25
        /    \
      30      40
     /  \    /
   10   20  35
```

**Passo 3:** Comparar 25 com seus filhos (30 e 40). Trocar com o maior filho (40).

```text
          40
        /    \
      30      25
     /  \    /
   10   20  35
```

**Passo 4:** Comparar 25 com seu filho (35). Trocar os elementos.

```text
          40
        /    \
      30      35
     /  \    /
   10   20  25
```

A Max-Heap foi reconstruída e o maior elemento (50) foi removido.

## 4. Complexidade das operações

| Operação | Complexidade |
|---|---|
| Acessar o maior elemento (Max-Heap) | O(1) |
| Inserir elemento | O(log n) |
| Remover a raiz | O(log n) |
| Construir heap (Heapify) | O(n) |
| Buscar um elemento qualquer | O(n) |
| Heap Sort | O(n log n) |

## 5. Aplicações de Heap Binária

As heaps binárias são utilizadas em diversas aplicações:

- **Filas de prioridade:** processamento de tarefas de acordo com sua prioridade.
- **Algoritmo de Dijkstra:** seleção do vértice com menor distância conhecida.
- **Algoritmo de Prim:** seleção da aresta de menor peso.
- **Heap Sort:** ordenação de elementos com complexidade O(n log n).
- **Escalonamento de processos:** gerenciamento de tarefas em sistemas operacionais.

## Conclusão

A heap binária é uma estrutura de dados eficiente para implementar filas de prioridade. Sua principal vantagem é permitir a inserção e a remoção da raiz em tempo O(log n), mantendo a propriedade de ordenação parcial da árvore.

