# Estrutura de Dados: Filas (Queues)

Uma **fila (queue)** é uma estrutura de dados linear que segue o princípio **FIFO (First-In, First-Out)**, o que significa que o primeiro elemento a ser inserido será o primeiro a ser removido. Ela funciona exatamente como uma fila do mundo real (como a fila de um banco).

As operações principais são o **enqueue** (inserir no final/cauda) e o **dequeue** (remover do início/cabeça).

---

## Complexidade de Tempo e Espaço

Quando implementada de forma eficiente (usando listas encadeadas ou arrays circulares), a fila apresenta as seguintes complexidades:

| Operação | Complexidade de Tempo | Descrição |
| :--- | :--- | :--- |
| **Enqueue** (Inserção) | **$O(1)$** | Adiciona um elemento ao final da fila instantaneamente. |
| **Dequeue** (Remoção) | **$O(1)$** | Remove o elemento do início da fila instantaneamente. |
| **Peek/Front** (Espiar) | **$O(1)$** | Apenas visualiza o primeiro elemento sem removê-lo. |
| **Espaço** (Memória) | **$O(n)$** | O consumo de memória cresce linearmente com o número de elementos $n$. |

---

## Vantagens da Fila

* **Ordem garantida:** É a estrutura ideal quando a ordem de chegada precisa ser estritamente respeitada (justiça no processamento).
* **Operações ultra-rápidas ($O(1)$):** A inserção e a remoção não exigem o deslocamento de outros elementos da estrutura.
* **Desacoplamento de sistemas:** Permite que dois sistemas trabalhem em velocidades diferentes (ex: um sistema envia milhares de e-mails para uma fila, e outro vai processando aos poucos sem travar o primeiro).
* **Gerenciamento de recursos compartilhados:** Essencial para organizar o uso de recursos únicos por múltiplos usuários, como filas de impressão ou agendamento de tarefas na CPU.

---

## Tipos Especiais de Fila

Além da fila linear padrão, existem variações especiais projetadas para resolver problemas específicos de gerenciamento de memória e regras de negócio.

### 1. Fila Circular (Circular Queue)

A fila circular resolve uma grande limitação da fila estática (baseada em arrays/vetores). Em uma fila linear comum, quando removemos elementos do início, aquelas posições ficam vazias e inutilizadas, o que pode levar a um falso aviso de "fila cheia" (*overflow*) mesmo restando espaço no começo.

Na **fila circular**, o último elemento é logicamente conectado de volta ao primeiro, formando um círculo.

* **Como funciona:** Os índices de controle se movem usando o operador matemático de módulo (`%`). Quando o ponteiro do fim atinge o limite do array, ele "pula" de volta para o índice `0` (caso este esteja livre).
  * *Fórmula matemática de avanço:* `fim = (fim + 1) % CAPACIDADE`.
* **Vantagens:**
  * **Desempenho estrito:** Evita o custo computacional de ter que deslocar (*shift*) todos os elementos para a esquerda a cada remoção.
  * **Uso eficiente da memória:** Garante o reaproveitamento total dos espaços vazios liberados.
* **Complexidade:** Mantém o tempo ideal de **$O(1)$** tanto para inserção quanto para remoção.

### 2. Fila de Prioridade (Priority Queue)

Diferente do padrão FIFO estrito, na **fila de prioridade** cada elemento inserido possui uma "chave" ou valor associado que dita sua importância. Os elementos são atendidos com base nessa prioridade, e não meramente pelo tempo de chegada. Se dois elementos possuem a mesma prioridade, eles seguem a ordem de chegada.

Existem duas variações principais:
1. **Fila de Prioridade Máxima:** O elemento com o maior valor de prioridade sai primeiro.
2. **Fila de Prioridade Mínima:** O elemento com o menor valor numérico sai primeiro (muito usado em algoritmos de menor caminho).

* **Aplicações reais:** Triagem de prontos-socorros (casos graves passam à frente), algoritmos de redes (roteamento de pacotes de dados prioritários) e o escalonador de processos de sistemas operacionais.
* **Complexidade:** Depende da forma como é construída:
  * Se implementada com uma lista simples ordenada: A remoção é rápida **$O(1)$**, mas a inserção exige busca e custa **$O(n)$**.
  * Se implementada de forma eficiente usando a estrutura **Heap Binária**: Tanto a inserção quanto a remoção passam a custar **$O(\log n)$**, que é altamente performático para grandes volumes de dados.

### 3. Fila de Duas Pontas (Deque)

O **Deque** (*Double-ended queue*) é uma fila flexível que **permite inserções e remoções em ambas as extremidades** (tanto no início quanto no fim). Ela pode se comportar tanto como uma fila tradicional quanto como uma pilha, dependendo de como você restringe o acesso às pontas.
