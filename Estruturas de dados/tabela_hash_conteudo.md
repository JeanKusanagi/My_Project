# Estrutura de Dados: Tabela Hash

Uma **tabela hash** (ou tabela de dispersão) é uma estrutura de dados eficiente que associa **chaves** de pesquisa a **valores** correspondentes. Ela utiliza uma **função hash** (ou função de espalhamento) para transformar uma chave em um índice numérico, que aponta para a posição exata de armazenamento em um vetor (array).

---

## 1. Complexidade de Tempo

O desempenho da tabela hash varia entre o caso médio e o pior caso, dependendo diretamente da eficiência da função hash e da estratégia adotada para tratar as colisões:

| Operação | Caso Médio | Pior Caso (Muitas Colisões) |
| :--- | :---: | :---: |
| **Busca** (`retrieve`) | $O(1)$ | $O(N)$ |
| **Inserção** (`insert`) | $O(1)$ | $O(N)$ |
| **Remoção** (`delete`) | $O(1)$ | $O(N)$ |

* **Caso Médio $O(1)$:** Ocorre quando a função hash distribui as chaves uniformemente pelo vetor e o fator de carga é mantido sob controle.
* **Pior Caso $O(N)$:** Ocorre se múltiplas chaves diferentes gerarem o mesmo índice (colisão), forçando a busca linear dentro de uma lista encadeada ou longas sondagens no vetor.

---

## 2. Principais Vantagens

* **Velocidade de Acesso:** Permite buscar, inserir e remover dados em tempo constante ($O(1)$) na grande maioria dos cenários computacionais.
* **Flexibilidade de Chaves:** Aceita diversos tipos de dados como chaves (como strings, números, ou objetos complexos), desde que possam ser mapeados para um valor numérico por uma função hash.
* **Eficiência em Grandes Volumes:** É ideal para gerenciar grandes conjuntos de dados associativos, sendo a base de dicionários, tabelas de símbolos de compiladores, sistemas de cache e roteamento de redes (como DNS).
* **Substituição de Buscas Lineares:** Elimina a necessidade de percorrer estruturas sequenciais inteiras ($O(N)$) para encontrar uma informação específica.

---

## 3. O Problema das Colisões

Uma **colisão** acontece quando duas ou mais chaves distintas produzem exatamente o mesmo índice através da função hash. Como o espaço de endereçamento da tabela é finito, o tratamento de colisões é obrigatório.

Existem duas abordagens principais para resolver esse problema:

### A) Encadeamento Fechado (Separado)
Nesta técnica, cada posição do vetor principal não armazena o elemento diretamente, mas sim um ponteiro para o início de outra estrutura, geralmente uma **lista encadeada**.

* **Como funciona:** Se houver colisão em um índice, o novo elemento é adicionado à lista vinculada àquela posição.
* **Vantagens:** A tabela nunca fica tecnicamente "cheia". A implementação é direta e o desempenho degrada suavemente.
* **Desvantagens:** Consome memória extra para armazenar os ponteiros da lista. Se a lista crescer demais, a busca perde a eficiência de tempo constante.

### B) Endereçamento Aberto
Nesta abordagem, **todos os elementos são armazenados diretamente no próprio vetor principal**. Quando ocorre uma colisão, o algoritmo varre o array em busca de uma posição que esteja livre.

* **Sondagem Linear (*Linear Probing*):** Se a posição `H` estiver ocupada, tenta a posição `H + 1`, `H + 2`, `H + 3`, sequencialmente. Pode gerar o problema de *agrupamento primário* (blocos de elementos ocupados que atrasam novas buscas).
* **Sondagem Quadrática (*Quadratic Probing*):** A distância de busca cresce de forma quadrática (`H + 1²`, `H + 2²`, `H + 3²`, ...), espalhando melhor os elementos colididos.
* **Duplo Hash (*Double Hashing*):** Utiliza uma segunda função hash para calcular o tamanho do "pulo" de busca. É um dos métodos mais eficientes para evitar agrupamentos.

---

## 4. Comparação entre os Tratamentos de Colisão

| Característica | Encadeamento Separado | Endereçamento Aberto |
| :--- | :--- | :--- |
| **Armazenamento** | Fora do vetor principal (listas externas) | Totalmente de forma interna no vetor |
| **Fator de Carga ($lpha$)** | Pode ser maior que $1.0$ (mais itens que posições) | Deve ser estritamente menor que $1.0$ |
| **Desperdício de Memória** | Alocação dinâmica para ponteiros das listas | Espaço reservado e não utilizado no array |
| **Remoção de Elementos** | Simples (deleção clássica em lista encadeada) | Complexa (exige marcação lógica como *deletado*) |

---

## 5. Fator de Carga e Rehashing

O **Fator de Carga** ($lpha$) é a razão entre o número de elementos armazenados ($n$) e o tamanho total do vetor ($m$):  
$$lpha = rac{n}{m}$$

Quando o fator de carga ultrapassa um limite crítico (geralmente $0.7$ ou $0.75$), a probabilidade de colisões aumenta drasticamente. Para contornar isso, a tabela realiza o **Rehashing**: o vetor é redimensionado (normalmente duplicando de tamanho) e todas as chaves existentes são remapeadas para novas posições usando o novo tamanho do vetor.