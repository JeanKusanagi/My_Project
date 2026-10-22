# Estruturas de Dados: Vetores (Arrays) e Listas Encadeadas

## 1. Definição de Vetor (Array)
Um **vetor (ou array)** é uma estrutura de dados linear e estática que armazena uma coleção de elementos do mesmo tipo em posições contíguas (seguidas) de memória física. Cada elemento dentro do vetor é acessado de forma direta por meio de um índice sequencial (que geralmente inicia em `0`).

### ⏱️ Complexidade de Tempo (Notação Big-O)

| Operação | Complexidade | Explicação |
| :--- | :--- | :--- |
| **Acesso / Leitura** | O(1) | **Tempo constante**. Permite ler qualquer posição diretamente pelo índice instantaneamente. |
| **Alteração / Escrita** | O(1) | **Tempo constante**. Modificar o valor de uma posição sabendo o índice é imediato. |
| **Busca (Não Ordenado)** | O(n) | **Tempo linear**. No pior cenário, é preciso checar elemento por elemento até o fim. |
| **Busca (Ordenado)** | O(log n) | **Tempo logarítmico**. Pode-se usar a busca binária se o vetor estiver ordenado. |
| **Inserção / Remoção** | O(n) | **Tempo linear**. Inserir ou remover itens no início/meio exige deslocar os outros elementos. |

### ⭐ Vantagens do Vetor
* **Acesso Aleatório Rápido:** A leitura em tempo constante O(1) elimina a necessidade de percorrer a estrutura.
* **Localidade de Referência:** Como os dados ficam juntos na memória, os processadores os colocam na memória cache, acelerando loops de repetição.
* **Economia de Memória:** Armazena estritamente os dados puros, sem gastar memória extra com ponteiros de conexão.

---

## 2. Implementação Prática

### Em Python (Array Dinâmico e NumPy)
O Python usa listas nativas como arrays dinâmicos (que mudam de tamanho automaticamente). Para performance estruturada pura, usa-se o NumPy.

```python
# --- 1. Usando Listas Nativas ---
frutas = ["maçã", "banana", "laranja"]

# Acesso O(1) e Alteração O(1)
print(frutas[0])  # Saída: maçã
frutas[1] = "pêra"

# Inserção no meio O(n) - desloca os elementos seguintes
frutas.insert(1, "melancia")


# --- 2. Usando NumPy (Vetor Clássico de Alta Performance) ---
import numpy as np

vetor_numeros = np.array([10, 20, 30, 40, 50])
resultado = vetor_numeros * 2  # Operação matemática otimizada em bloco
print(resultado)  # Saída: [ 20  40  60  80 100]
```

### Em C (Aritmética de Ponteiros e Memória Estática)
Em C, o vetor opera diretamente no hardware. O nome do vetor aponta para o endereço inicial de memória.

```c
#include <stdio.h>

int main() {
    // Declaração de vetor estático com 5 inteiros (cada inteiro usa 4 bytes)
    int vetor[5] = {10, 20, 30, 40, 50};

    // Acesso instantâneo O(1) via aritmética de ponteiros
    // Fórmula: Endereço = Base + (Índice * Tamanho do Tipo)
    printf("Posição 2: %d\n", vetor[2]); // Saída: 30

    // Alteração O(1)
    vetor[1] = 99; 

    return 0;
}
```

---

## 3. Diferença entre Array Estruturado e Lista Encadeada

A grande diferença está em como eles se organizam fisicamente na memória do computador.

* **Array Estruturado:** Exige um bloco de memória **contínuo** (todos os elementos juntos, lado a lado).
* **Lista Encadeada:** Armazena elementos de forma **dispersa** (espalhados na memória). Cada elemento (chamado de **nó**) guarda o seu próprio dado e um ponteiro (uma referência) indicando onde está o próximo nó.

### Quadro Comparativo Direto

| Característica / Operação | Array (Vetor Estruturado) | Lista Encadeada |
| :--- | :--- | :--- |
| **Organização Física** | Contígua na memória | Dispersa na memória |
| **Dimensionamento** | Tamanho fixo (estático) | Tamanho dinâmico (cresce fácil) |
| **Acesso a um Elemento** | O(1) — Instantâneo via índice | O(n) — Precisa percorrer do início |
| **Inserção / Remoção** | O(n) — Lento (desloca elementos) | O(1) — Rápido (só altera ponteiros) |
| **Consumo de Memória** | Menor (apenas o dado puro) | Maior (guarda dado + ponteiro) |

### Analogia Prática
* **Array:** Pense em uma fileira de armários numerados em um corredor. Se você quer ir ao armário 4, vai diretamente até ele (**Acesso Rápido**). Porém, para colocar um armário novo no meio, é preciso empurrar todos os outros para o lado (**Inserção Lenta**).
* **Lista Encadeada:** Pense em uma caça ao tesouro. Cada pista contém uma informação e um papelzinho dizendo onde encontrar a próxima pista. Para achar a quarta pista, você é obrigado a passar pela primeira, segunda e terceira (**Acesso Lento**). Mas se quiser colocar uma pista nova no meio, basta alterar o papelzinho da pista anterior (**Inserção Rápida**).
