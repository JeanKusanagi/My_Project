# Busca Local Informada em Inteligência Artificial

Uma **busca local informada** é uma estratégia de resolução de problemas em Inteligência Artificial onde o algoritmo utiliza conhecimento específico do domínio (geralmente uma **função heurística**) para guiar a exploração do espaço de estados, buscando encontrar a melhor solução de forma mais eficiente do que uma busca cega.

Diferente de algoritmos como a Busca em Largura ou Profundidade, que exploram caminhos sem saber se estão se aproximando do objetivo, a busca local informada avalia e modifica os estados atuais com base em quão "perto" eles parecem estar da meta.

---

## 🧠 Principais Características

* **Foco no Estado Atual:** Mantém em memória apenas o estado atual (ou um conjunto muito pequeno de estados) e tenta melhorá-lo passo a passo, em vez de guardar caminhos completos.
* **Uso de Heurísticas:** Utiliza uma função $h(n)$ que estima o "custo" ou a "distância" do estado atual até o objetivo.
* **Eficiência de Memória:** Como não guardam a árvore de busca inteira, esses algoritmos são ideais para problemas com espaços de estados gigantescos ou infinitos (ex: otimização de rotas, alocação de recursos).

---

## 🛠️ Principais Algoritmos de Busca Local Informada

### 1. Subida de Encosta (*Hill Climbing*)
É o algoritmo de busca local mais clássico. Ele avalia os vizinhos do estado atual e se move para o vizinho que trouxer a maior melhoria em direção ao objetivo.
* **Analogia:** É como tentar subir uma montanha no meio de uma névoa espessa: você olha ao redor, dá um passo na direção que parece subir mais rápido e repete.
* **Limitação:** Pode ficar preso em **máximos locais** (picos que são mais altos que os vizinhos, mas não são o ponto mais alto do mapa).

### 2. Têmpera Simulada (*Simulated Annealing*)
Inspirado no processo de metalurgia (onde o metal é aquecido e resfriado lentamente para cristalizar sem defeitos).
* **Como funciona:** No início (alta "temperatura"), o algoritmo aceita movimentos ruins com frequência para escapar de máximos locais. À medida que o tempo passa (a temperatura "esfria"), ele se torna mais estrito e só aceita movimentos de melhoria.

### 3. Busca Local em Feixe (*Local Beam Search*)
Em vez de manter apenas um único estado atual, o algoritmo acompanha **$k$ estados simultaneamente**.
* **Como funciona:** Em cada passo, todos os vizinhos de todos os $k$ estados são gerados. Destes, apenas os $k$ melhores de todo o grupo são selecionados para a próxima rodada. Isso permite compartilhar informações entre diferentes caminhos de busca.

### 4. Algoritmos Genéticos
Uma variante da busca local em feixe onde os novos estados são gerados combinando dois estados "pais" (cruzamento) e aplicando pequenas alterações aleatórias (mutação), imitando a evolução natural.
