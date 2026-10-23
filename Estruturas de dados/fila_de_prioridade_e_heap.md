# Estruturas de Dados: Fila de Prioridade e Heap

## 1. O que é uma Fila de Prioridade?

Uma **fila de prioridade** (*priority queue*) é uma estrutura de dados abstrata onde cada elemento possui uma **prioridade** associada. 

Ao contrário de uma fila comum (tipo **FIFO** — *First-In, First-Out*, onde sai primeiro quem chega primeiro), na fila de prioridade o elemento que sai primeiro é **o que tem a maior (ou menor) prioridade**, independentemente de quando ele chegou.

---

### Tipos Principais
* **Fila de Prioridade Máxima:** O elemento com o *maior* valor de prioridade (ou maior chave) é removido primeiro.
* **Fila de Prioridade Mínima:** O elemento com o *menor* valor de prioridade é removido primeiro.

---

### Operações Principais
* **Inserir (*push / enqueue*):** Adiciona um novo elemento com a sua respectiva prioridade à estrutura.
* **Remover (*pop / dequeue*):** Retira e retorna o elemento de maior (ou menor) prioridade.
* **Consultar (*peek / top*):** Apenas visualiza o elemento de maior/menor prioridade sem removê-lo.

---

### Exemplo de Código Simples (Python)

Por padrão, o módulo `heapq` do Python implementa uma fila de **prioridade mínima** (o menor número sai primeiro).

```python
import heapq

# Cria uma lista vazia para a fila de prioridade
fila_prioridade = []

# Inserindo elementos na fila (prioridade, "nome do elemento")
heapq.heappush(fila_prioridade, (3, "Paciente Clínico (Verde)"))
heapq.heappush(fila_prioridade, (1, "Paciente em Emergência (Vermelho)"))
heapq.heappush(fila_prioridade, (2, "Paciente Urgente (Amarelo)"))

print("--- Atendimento no Pronto-Socorro ---")

# Removendo e processando os elementos por ordem de prioridade
while fila_prioridade:
    prioridade, paciente = heapq.heappop(fila_prioridade)
    print(f"Atendendo: {paciente} [Prioridade nível {prioridade}]")
```

**Saída do código:**
```text
--- Atendimento no Pronto-Socorro ---
Atendendo: Paciente em Emergência (Vermelho) [Prioridade nível 1]
Atendendo: Paciente Urgente (Amarelo) [Prioridade nível 2]
Atendendo: Paciente Clínico (Verde) [Prioridade nível 3]
```

---

## 2. Como o Heap Organiza Tudo por Baixo dos Panos?

O **Heap** é uma árvore binária que obedece a uma regra muito clara de organização chamada **propriedade do heap**. É graças a essa estrutura que a fila de prioridade consegue ser eficiente, sem precisar ordenar toda a lista a cada nova inserção.

* **Min-Heap:** O nó pai é sempre **menor ou igual** aos seus nós filhos. Logo, o **menor elemento** do sistema fica na **raiz** (topo).
* **Max-Heap:** O nó pai é sempre **maior ou igual** aos seus nós filhos. Logo, o **maior elemento** fica na **raiz**.

---

### Visualização Prática (Árvore vs. Vetor/Array)

Embora a gente imagine o Heap como uma árvore binária, por baixo dos panos ele é armazenado de forma super compacta dentro de uma **lista simples (array)**. Para isso, ela precisa ser uma **árvore binária completa** (todos os níveis preenchidos da esquerda para a direita). 

Isso permite encontrar os filhos e os pais usando fórmulas matemáticas simples nos índices da lista:

Se um nó está na posição `i`:
* **Filho esquerdo:** `2 * i + 1`
* **Filho direito:** `2 * i + 2`
* **Nó pai:** `(i - 1) // 2`

#### Exemplo de Estrutura Estruturada (Min-Heap):

* **Representação Visual em Árvore:**
```text
          10      <- Raiz (Índice 0)
        /    \
      20      15  <- Filhos da Raiz (Índices 1 e 2)
     /  \
   30    40       <- Filhos do 20 (Índices 3 e 4)
```

* **Como fica na memória (Array/Lista):**
```text
Índice: [ 0,  1,  2,  3,  4]
Valor:  [10, 20, 15, 30, 40]
```
*Note que o array não está totalmente ordenado (o 15 vem depois do 20), mas a regra do Heap é mantida: todo pai é menor ou igual a seus filhos.*

---

### Como as Operações Funcionam?

#### A Inserção (*Up-Heap* ou *Bubble-Up*)
1. O algoritmo coloca o novo elemento na **última posição livre** da árvore (fim do array).
2. Se o elemento violar a regra do Heap (por exemplo, for menor que o pai em um Min-Heap), ele **sobe**, trocando de lugar com o seu pai repetidamente até encontrar a posição correta.

#### A Remoção (*Down-Heap* ou *Bubble-Down*)
1. O algoritmo remove o elemento que está na **raiz** (o topo da prioridade).
2. Para preencher o espaço vazio, ele pega o **último elemento** do fim da fila e o coloca na raiz.
3. Como esse elemento costuma ser grande, ele viola a regra. O algoritmo faz esse elemento **descer**, trocando de lugar com o **menor de seus dois filhos**, até restaurar a propriedade do Heap.

---

### Comparação de Eficiência (Complexidade de Tempo)

A tabela abaixo mostra a diferença de desempenho entre implementar uma Fila de Prioridade com listas comuns vs. usando um **Heap Binário**:

| Estrutura de Dados | Inserção (*Push*) | Remoção (*Pop*) | Espaço em Memória |
| :--- | :--- | :--- | :--- |
| **Lista não ordenada** | O(1) | O(n) | O(n) |
| **Lista ordenada** | O(n) | O(1) | O(n) |
| **Heap Binária** | **O(log n)** | **O(log n)** | **O(n)** |

Em uma lista com 1.000.000 de itens, enquanto a lista desordenada precisa checar **1.000.000** de posições para remover o menor elemento, o Heap resolve o problema subindo ou descendo no máximo **20 níveis** da árvore (log2 1.000.000 ≈ 20).
