# Guia Completo de Estruturas de Dados: Árvores

Este documento apresenta uma visão consolidada sobre a estrutura de dados de Árvore, abordando desde conceitos fundamentais até estruturas avançadas auto-balanceadas e multidirecionais como as Árvores AVL, B e B+.

---

## 1. O que é uma Árvore?

Uma **árvore** é uma **estrutura de dados não linear e hierárquica** composta por elementos chamados **nós** (ou nodos) interconectados por **arestas** (ou ponteiros).

Diferente de estruturas lineares (como arrays e listas encadeadas), onde os dados são organizados em sequência, a árvore organiza os dados de forma vertical em níveis. 
* **Raiz:** O nó principal no topo da árvore.
* **Filhos/Subnós:** Nós ramificados a partir de um nó superior (pai).
* **Folhas:** Nós terminais localizados na base, que não possuem filhos.

### ⏳ Complexidade das Operações (Visão Geral)
A eficiência de uma árvore depende do seu **balanceamento** (distribuição uniforme das ramificações). Para uma Árvore Binária de Busca tradicional (BST), as complexidades são:

| Operação | Caso Médio (Árvore Balanceada) | Pior Caso (Árvore Desbalanceada/Degenerada) |
| :--- | :--- | :--- |
| **Busca** | $O(\log n)$ | $O(n)$ |
| **Inserção** | $O(\log n)$ | $O(n)$ |
| **Remoção** | $O(\log n)$ | $O(n)$ |

### 🚀 Vantagens Gerais das Árvores
1. **Busca e Recuperação Rápidas:** Reduzem drasticamente o número de comparações em relação a buscas lineares (ex: resolve uma busca entre 1.000.000 de registros em cerca de 20 passos em caso balanceado).
2. **Hierarquia Natural:** Mapeiam perfeitamente relações de subordinação e dependência (ex: sistemas de arquivos, estruturas HTML/DOM, organogramas).
3. **Estrutura Dinâmica:** Crescem e diminuem dinamicamente na memória, evitando a necessidade de realocação total de espaço físico.
4. **Eficiência Superior a Arrays Ordenados:** Modificações como inserção e remoção mantém custos de $O(\log n)$ em árvores balanceadas, enquanto arrays ordenados exigem $O(n)$ devido ao deslocamento de elementos.

---

## 2. Tipos Específicos de Árvores

### A. Árvore Binária de Busca (BST)
Segue uma regra estrita de ordenação: para qualquer nó, todos os valores na **subárvore esquerda são menores** que o valor do nó pai, e todos os valores na **subárvore direita são maiores**.
* **Ponto Forte:** Simplicidade de implementação.
* **Ponto Fraco:** Se os dados forem inseridos de forma ordenada (ex: 1, 2, 3, 4, 5), ela se degenera em uma lista linear, degradando a performance para $O(n)$.

### B. Árvore AVL
Primeira árvore binária de busca **auto-balanceada**. Ela introduz o **Fator de Balanceamento (FB)**, que é a diferença de altura entre as subárvores esquerda e direita.
* **Regra:** O FB de qualquer nó deve ser estritamente **-1, 0 ou 1**. Se violado, a árvore realiza **rotações** para reestabelecer o equilíbrio.
* **Ponto Forte:** Garante a complexidade de $O(\log n)$ mesmo no pior caso. Excelente para cenários com alta frequência de leituras/buscas.
* **Ponto Fraco:** Inserções e remoções são ligeiramente mais lentas devido ao custo computacional de calcular os fatores e aplicar rotações frequentemente.

### C. Árvore B (B-Tree)
Uma árvore **auto-balanceada de busca multidirecional**. Ela quebra a regra de ser exclusivamente binária.
* **Funcionamento:** Cada nó pode armazenar **múltiplas chaves** e possuir **múltiplos ponteiros para filhos**. Projetada especificamente para otimizar sistemas de armazenamento secundário (Discos rígidos e SSDs).
* **Ponto Forte:** Reduz o número de acessos ao disco (I/O) mantendo a estrutura extremamente baixa e larga.
* **Ponto Fraco:** Implementação complexa devido à lógica de divisão (*split*) e fusão (*merge*) de nós.

---

## 3. Comparativo: Árvore B vs. Árvore B+

A **Árvore B+** é a evolução direta e a variação mais famosa da Árvore B, servindo hoje como o padrão definitivo para índices em bancos de dados relacionais e sistemas de arquivos modernos.

| Recurso | Árvore B | Árvore B+ |
| :--- | :--- | :--- |
| **Localização dos Dados** | Armazenados em qualquer nível (nós internos e folhas). | Armazenados **estritamente nos nós folhas**. |
| **Nós Internos** | Contêm chaves de busca e os dados associados. | Contêm **apenas chaves de roteamento** e ponteiros. |
| **Conexão entre Folhas** | Nós folhas são isolados entre si. | Nós folhas são interligados por uma **lista encadeada**. |
| **Busca por Intervalo** | Lenta (requer subir e descer na árvore repetidamente). | **Muito rápida** (localiza o início e percorre horizontalmente). |
| **Fator de Ramificação** | Menor (as chaves ocupam mais espaço com os dados junto). | **Maior** (cabe muito mais chaves de índice por bloco de disco). |
| **Altura da Árvore** | Moderada. | **Muito baixa** (otimizando severamente os saltos de leitura). |

---

## 📊 Resumo de Complexidade por Tipo

| Tipo de Árvore | Busca (Médio / Pior) | Inserção (Médio / Pior) | Principal Aplicação |
| :--- | :--- | :--- | :--- |
| **BST Tradicional** | $O(\log n)$ / $O(n)$ | $O(\log n)$ / $O(n)$ | Dicionários simples na memória RAM |
| **Árvore AVL** | $O(\log n)$ / $O(\log n)$ | $O(\log n)$ / $O(\log n)$ | Tabelas de símbolos e caches de leitura intensa |
| **Árvore B / B+** | $O(\log n)$ / $O(\log n)$ | $O(\log n)$ / $O(\log n)$ | Índices de Bancos de Dados e Sistemas de Arquivos |