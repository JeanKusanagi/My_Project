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
