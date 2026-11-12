# I - Resolução de problemas por meio de busca: busca sem informação, busca com informação, busca gulosa, algoritmo A*, busca com satisfação de restrições, busca competitiva

## 1. Formulação do problema de busca

A resolução de problemas por meio de busca constitui um dos paradigmas centrais da Inteligência Artificial, sendo amplamente utilizada para encontrar soluções em espaços de estados bem definidos. Formulado como um grafo ou árvore de possibilidades, o problema de busca é modelado a partir de um estado inicial s₀, um conjunto de ações possíveis AÇÕES(s), uma função de transição RESULTADO(s, a) = s', um ou mais estados objetivos (teste de objetivo) e, quando aplicável, uma função de custo c(s, a, s') associada às ações. O custo de um caminho é a soma dos custos de suas ações, e uma solução ótima é aquela de menor custo total, denotado C*. O processo de busca consiste em explorar sistematicamente esse espaço de estados até encontrar uma solução válida, podendo variar em eficiência e custo computacional conforme a estratégia adotada. As técnicas de busca são especialmente importantes em problemas de planejamento, jogos, robótica, otimização e resolução de problemas em geral.

Ao longo do texto, usaremos como exemplo recorrente o mapa simplificado da Romênia: o agente está em Arad e deseja chegar a Bucareste. Os estados são as cidades, as ações são as estradas e o custo de cada ação é a distância em km (por exemplo, Arad–Sibiu = 140, Sibiu–Fagaras = 99, Fagaras–Bucareste = 211, Sibiu–Rîmnicu Vâlcea = 80, Rîmnicu Vâlcea–Pitesti = 97, Pitesti–Bucareste = 101).

Os algoritmos de busca são avaliados segundo quatro critérios: **completude** (garante encontrar uma solução, se existir?), **otimalidade** (a solução encontrada é a de menor custo?), **complexidade de tempo** (quantos nós são gerados) e **complexidade de espaço** (quantos nós precisam ficar na memória).

Na **busca em árvores**, não há, em geral, um controle global dos estados já visitados. Assim, o mesmo estado pode ser alcançado por diferentes caminhos e aparecer várias vezes na árvore de busca, enquanto ciclos podem levar à expansão indefinida de determinados ramos (no exemplo, Arad → Sibiu → Arad → Sibiu → …). Na **busca em grafos**, utiliza-se normalmente um conjunto de estados explorados para evitar expansões repetidas e tratar ciclos, reduzindo o número de nós processados, embora à custa de maior consumo de memória.

## 2. Fator de ramificação e crescimento exponencial

O **fator de ramificação (b)** representa, aproximadamente, o número de sucessores de cada estado e desempenha papel fundamental na complexidade da busca. Em uma árvore com fator de ramificação aproximadamente uniforme, uma busca até a profundidade d pode gerar

$1 + b + b² + … + b^d = (b^(d+1) − 1) / (b − 1) = O(b^d)$

nós. Portanto, pequenas reduções no fator de ramificação podem produzir grandes ganhos computacionais, pois o número de nós cresce exponencialmente com a profundidade. Por exemplo, com d = 5, uma árvore com b = 10 tem cerca de 111.111 nós, enquanto com b = 5 tem apenas 3.906, ou seja, cerca de 28 vezes menos. Esse crescimento ajuda a explicar por que problemas com espaços de estados aparentemente simples podem se tornar computacionalmente difíceis.

Para reduzir esse custo, os algoritmos de busca podem ser classificados principalmente em **busca sem informação** e **busca informada**. A principal diferença entre elas é a utilização de conhecimento adicional sobre a proximidade dos estados em relação ao objetivo. As heurísticas procuram reduzir o custo da exploração ao direcionar a busca para estados considerados mais promissores, evitando, quando possível, a expansão de grandes regiões pouco relevantes do espaço de estados.

## 3. Busca sem informação

A **busca sem informação ou busca cega (uninformed search ou blind search)** caracteriza-se pela ausência de conhecimento adicional sobre o problema além de sua definição formal. Em outras palavras, utiliza apenas as informações fornecidas pela formulação do problema, sem estimativas heurísticas sobre a proximidade dos estados em relação ao objetivo, explorando o espaço de estados de maneira sistemática. Consequentemente, a escolha do próximo estado a ser explorado depende de propriedades estruturais da árvore ou do grafo de busca, como profundidade, custo acumulado ou ordem de geração. Exemplos clássicos incluem a busca em largura (Breadth-First Search – BFS), a busca em profundidade (Depth-First Search – DFS), a busca de custo uniforme (Uniform-Cost Search – UCS), a busca em profundidade limitada (DLS) e a busca de aprofundamento iterativo (Iterative Deepening Search – IDS).

**Busca em largura (BFS).** Expande todos os nós de uma camada antes de avançar à camada seguinte. Ela garante a solução de menor profundidade, sendo completa (para b finito) e ótima quando todas as ações têm o mesmo custo (por exemplo, grafos não ponderados). A estrutura de dados utilizada é uma fila FIFO (First In, First Out). Se o fator de ramificação é b e a solução está na profundidade d, a complexidade é aproximadamente $O(b^d)$, tanto para tempo quanto para memória, pois toda a fronteira precisa ser armazenada. Assim, embora a BFS possa encontrar rapidamente uma solução superficial, pode tornar-se inviável em espaços grandes: com b = 10, e supondo 1 milhão de nós por segundo e 1 KB por nó, uma solução em d = 8 exigiria cerca de 111 milhões de nós, ou seja, mais de 100 GB de memória. No exemplo da Romênia, a BFS devolve Arad → Sibiu → Fagaras → Bucareste (3 estradas, 450 km), que tem o menor número de passos, mas não o menor custo, já que existe uma rota de 418 km. Isso ilustra por que a BFS só é ótima quando os custos são uniformes.

**Busca em profundidade (DFS).** Explora um ramo até sua extremidade antes de retroceder, utilizando memória proporcional à profundidade máxima da busca. Sua implementação típica emprega uma pilha LIFO (Last In, First Out) ou recursão. Embora possa encontrar rapidamente uma solução quando esta estiver em um ramo explorado inicialmente, a DFS não é ótima e pode não ser completa em espaços infinitos ou que contenham ciclos (em grafos finitos com conjunto de explorados, ela é completa). Se b representa o fator de ramificação e m a profundidade máxima, sua complexidade de tempo é $O(b^m)$ e a de memória é O(bm), já que só é necessário guardar o caminho atual e os irmãos não expandidos de cada nó do caminho.

**Busca de custo uniforme (UCS).** Pode ser vista como uma generalização da BFS para grafos ponderados, expandindo sempre o nó com o menor custo acumulado. Sua função de avaliação é

f(n) = g(n),

em que g(n) representa o custo do caminho do estado inicial até n. Quando os custos das ações são não negativos, a UCS garante uma solução ótima; com custos de ação estritamente positivos (isto é, c ≥ ε > 0), também é completa. Sua principal desvantagem é que pode explorar uma quantidade muito grande de estados antes de encontrar a solução, especialmente quando não possui conhecimento sobre a direção do objetivo. No pior caso, as complexidades de tempo e espaço são

$O(b^{(1 + ⌊C*/ε⌋)})$,

em que C* é o custo da solução ótima e ε é o menor custo de ação. Quando todos os custos são iguais, C*/ε = d e a UCS se comporta como a BFS. Na Romênia, a UCS encontra a rota ótima de 418 km (Arad → Sibiu → Rîmnicu Vâlcea → Pitesti → Bucareste), mas só depois de expandir cidades que se afastam do destino, como Zerind e Timișoara, cujo custo acumulado ainda é menor que 418.

**Busca em profundidade limitada (DLS).** Executa uma DFS com um limite fixo de profundidade L, com tempo $O(b^L)$ e espaço O(bL). Se o limite for menor que a profundidade da solução, ela não a encontra.

**Busca de aprofundamento iterativo (IDS).** Resolve esse problema ao executar sucessivas buscas em profundidade limitada com limite crescente (L = 0, 1, 2, …) até encontrar uma solução. Assim, combina as vantagens da BFS e da DFS: tem a completude e a otimalidade da BFS (quando os custos são uniformes), com o consumo de memória linear da DFS, O(bd). Embora regenere os nós das camadas superiores a cada iteração, o desperdício é pequeno, pois a maioria dos nós está na última camada. O número total de nós gerados é

$N(IDS) = (d + 1)·b⁰ + d·b¹ + (d − 1)·b² + … + 1·b^d = O(b^d)$.

Com b = 10 e d = 5, a IDS gera 6 + 50 + 400 + 3.000 + 20.000 + 100.000 = 123.456 nós, contra 111.111 da BFS, ou seja, um custo adicional de apenas cerca de 11%.

**Busca bidirecional.** É uma estratégia que realiza duas buscas simultâneas: uma a partir do estado inicial, em direção ao objetivo, e outra a partir do estado objetivo, em direção ao início. O algoritmo termina quando as duas buscas se encontram, permitindo reconstruir o caminho entre os estados. Em geral, quando o fator de ramificação é b e a profundidade da solução é d, sua complexidade temporal e espacial pode ser reduzida de $O(b^d)$, característica da busca em largura convencional, para aproximadamente $O(b^{(d/2)})$, pois cada busca só precisa chegar à metade do caminho $(2·b^{(d/2)} ≪ b^d)$. Por exemplo, com b = 10 e d = 6, a BFS convencional gera cerca de 10⁶ nós, enquanto a bidirecional gera cerca de 2 × 10³. Entretanto, sua aplicação depende de ser possível definir o estado objetivo e realizar a busca no sentido inverso (calcular os predecessores), o que nem sempre é viável em todos os problemas.

## 4. Busca com informação e heurísticas

A **busca com informação ou busca heurística (informed search ou heuristic search)** incorpora conhecimento adicional por meio de funções heurísticas, que estimam o custo restante para alcançar um estado objetivo a partir do estado atual. Essas estimativas orientam a exploração do espaço de estados de maneira mais eficiente, podendo reduzir significativamente o número de nós expandidos em comparação com as estratégias de busca sem informação. A qualidade da heurística é fundamental para o desempenho dos algoritmos e, em determinados casos, para a garantia da otimalidade da solução encontrada.

Uma heurística h(n) estima o custo do caminho de menor custo entre o nó n e um objetivo. Ela é denominada **admissível** quando nunca superestima esse custo, isto é,

0 ≤ h(n) ≤ h*(n) para todo n,

em que h*(n) representa o custo real mínimo de n até um objetivo. A admissibilidade caracteriza a heurística como otimista, pois fornece um limite inferior para o custo restante. Uma heurística **consistente** (ou monotônica) é aquela cuja estimativa respeita a desigualdade triangular entre nós consecutivos (olhando para passos locais):

h(n) ≤ c(n, a, n') + h(n') para todo nó n e todo sucessor n' de n, e h(g) = 0 para todo objetivo g,

em que h(n) é o custo estimado do nó n até o objetivo, c(n, a, n') é o custo real (não negativo) da ação a que leva de n a n' e h(n') é o custo estimado do sucessor n' até o objetivo.

Toda heurística consistente é admissível, embora o contrário não seja necessariamente verdadeiro. Para ver por quê, considere um caminho n = n₀, n₁, …, $n_k$ = g até um objetivo; aplicando a desigualdade repetidamente, h(n₀) ≤ c(n₀,n₁) + h(n₁) ≤ … ≤ (custo total do caminho) + h(g) = custo do caminho, o que vale em particular para o caminho ótimo e implica h(n) ≤ h*(n). A consistência é uma propriedade mais forte e, no A*, garante que os valores de f(n) = g(n) + h(n) não diminuam ao longo de um caminho. De fato, se n' é sucessor de n:

f(n') = g(n') + h(n') = g(n) + c(n, a, n') + h(n') ≥ g(n) + h(n) = f(n).

Assim, em problemas de busca em grafos, o A* com heurística consistente encontra uma solução ótima sem precisar reabrir nós já expandidos, sob as condições usuais de custos não negativos.

Quanto mais próxima h(n) estiver de h*(n), em geral, mais informativa é a heurística, o que tende a direcionar a busca de maneira mais eficiente. Essa proximidade, no entanto, não é condição necessária para a admissibilidade: uma heurística pode ser admissível mesmo sendo pouco informativa (por exemplo, h(n) = 0 para todo n, caso em que o A* se reduz à UCS).

A **dominância** entre heurísticas é outro conceito fundamental: diz-se que h₂ domina h₁ quando h₂(n) ≥ h₁(n) para todo nó n, com ambas sendo admissíveis. O A* com a heurística dominante expande, em geral, um subconjunto dos nós expandidos com a heurística dominada, sendo preferível (desde que o custo de calcular h₂ não seja proibitivo). Heurísticas admissíveis podem ser construídas sistematicamente a partir de **problemas relaxados** (versões simplificadas do problema original obtidas pela remoção de restrições), cujo custo ótimo de solução fornece um limite inferior válido para o problema original; além disso, essas heurísticas costumam ser consistentes.

**Exemplo (quebra-cabeça de 8 peças).** Considere o estado inicial com as peças 7 2 4 / 5 _ 6 / 8 3 1 e o objetivo _ 1 2 / 3 4 5 / 6 7 8. A regra original diz que uma peça só pode ser movida para uma casa adjacente vazia. Relaxando-a, obtemos duas heurísticas:

- h₁(n) = número de peças fora do lugar (relaxando para "uma peça pode ir para qualquer casa"). Aqui, h₁ = 8.
- h₂(n) = soma das distâncias de Manhattan das peças às suas posições finais (relaxando para "uma peça pode ir para qualquer casa adjacente, ocupada ou não"). Aqui, h₂ = 3 + 1 + 2 + 2 + 2 + 3 + 3 + 2 = 18.

Ambas são admissíveis, pois cada peça fora do lugar precisa de pelo menos um movimento, e de pelo menos |Δlinha| + |Δcoluna| movimentos. Como h₂(n) ≥ h₁(n) para todo n, h₂ domina h₁ e leva o A* a expandir menos nós. Outros exemplos clássicos são a **distância euclidiana (linha reta)**, em problemas de navegação espacial, que é admissível porque nenhuma estrada pode ser mais curta que a linha reta entre dois pontos, e a **distância de Manhattan**, em problemas de movimentação em grades sem movimentos diagonais.

Com essas propriedades definidas, podemos examinar os algoritmos que as utilizam.

## 5. Busca gulosa, A*, IDA* e SMA*

Os algoritmos informados diferem na função de avaliação f(n) que usam para escolher qual nó expandir:

- UCS: f(n) = g(n);
- Busca gulosa: f(n) = h(n);
- A*: f(n) = g(n) + h(n).

**Busca gulosa (Greedy Best-First Search).** É uma estratégia heurística que seleciona, a cada passo, o nó com menor valor de h(n), isto é, aquele que aparenta estar mais próximo de um objetivo. Dessa forma, ela considera apenas a estimativa do custo restante e ignora o custo já percorrido g(n). Embora possa encontrar soluções rapidamente em muitos problemas, não garante uma solução ótima e, dependendo das características do espaço de busca (por exemplo, em busca em árvore com ciclos), pode não ser completa. No pior caso, sua complexidade é $O(b^m)$, mas uma boa heurística pode reduzi-la bastante. Na Romênia, usando como h a distância em linha reta até Bucareste (Arad = 366, Sibiu = 253, Timișoara = 329, Zerind = 374, Fagaras = 176, Rîmnicu Vâlcea = 193, Pitesti = 100), a gulosa vai de Arad a Sibiu (253 < 329 < 374), depois a Fagaras (176 < 193) e finalmente a Bucareste, com custo 140 + 99 + 211 = 450 km. A solução é encontrada rapidamente, mas não é a ótima (418 km).

**Algoritmo A\*.** É uma das estratégias de busca mais importantes e amplamente utilizadas. Ele combina o custo já percorrido com a estimativa heurística futura por meio da função de avaliação

f(n) = g(n) + h(n),

em que g(n) é o custo acumulado até o nó n e h(n) é a estimativa do custo restante até o objetivo; assim, f(n) estima o custo da melhor solução que passa por n. Com fator de ramificação finito e custos de ação positivos (c ≥ ε > 0), o A* é completo. Ele é ótimo quando a heurística é admissível (em buscas em árvore) ou consistente (em buscas em grafos, sem reabrir nós). Isso o torna uma escolha robusta para problemas como planejamento de rotas e navegação em robótica. A consistência, que implica admissibilidade quando h(g) = 0 nos estados objetivo, tem uma consequência prática importante: os valores de f(n) não diminuem ao longo de um caminho, o que facilita a implementação eficiente em grafos e reduz a necessidade de reabrir estados já processados.

**Exemplo (A\* na Romênia).** Partindo de Arad (f = 0 + 366):

1. Expande-se Arad: Sibiu f = 140 + 253 = 393; Timișoara f = 118 + 329 = 447; Zerind f = 75 + 374 = 449.
2. Expande-se Sibiu (menor f): Rîmnicu Vâlcea f = 220 + 193 = 413; Fagaras f = 239 + 176 = 415 (entre outros).
3. Expande-se Rîmnicu Vâlcea (413): Pitesti f = 317 + 100 = 417.
4. Expande-se Fagaras (415): Bucareste f = 450 + 0 = 450.
5. Expande-se Pitesti (417): Bucareste f = 418 + 0 = 418. Como 418 < 450, essa passa a ser a melhor rota para Bucareste, e ela é expandida antes de qualquer nó de f maior.

O A* devolve a rota ótima de 418 km. Note que ele evitou a armadilha da gulosa: o nó Fagaras parecia melhor por h, mas o custo g já acumulado fez Rîmnicu Vâlcea e Pitesti competirem de forma justa.

No pior caso, a complexidade temporal e espacial do A* é $O(b^d)$, em que b é o fator de ramificação (número médio de sucessores por nó) e d é a profundidade. Na prática, o desempenho depende da qualidade da heurística e é frequentemente medido pelo **fator de ramificação efetivo** b*, definido como o valor que satisfaz N + 1 = 1 + b* + (b*)² + … + $(b*)^d$, em que N é o número de nós gerados; quanto mais próximo de 1 for b*, melhor é a heurística. O principal desafio do A* é o consumo de memória, exponencial no pior caso, o que motivou variantes como o IDA* e o SMA*. Uma outra variante, o A* ponderado, usa f(n) = g(n) + w·h(n), com w > 1: ele sacrifica a otimalidade (a solução tem custo no máximo w·C* se h for admissível) em troca de expandir menos nós.

**IDA\* (Iterative Deepening A\*).** Combina a estratégia de busca em profundidade (DFS) com a avaliação heurística do A*. Em vez de estabelecer um limite de profundidade, o algoritmo realiza sucessivas buscas em profundidade utilizando como limite um valor de f(n) = g(n) + h(n), em que g(n) representa o custo acumulado do caminho desde o estado inicial até o nó n, e h(n) estima o custo restante até um objetivo. O limite inicial é f(s₀) = h(s₀). Em cada iteração, são explorados os nós cujo valor de f(n) não excede o limite atual; quando a solução não é encontrada, o novo limite passa a ser o menor valor de f(n) que excedeu o limite anterior. O IDA* pode encontrar uma solução de custo ótimo sob condições semelhantes às do A*, como a utilização de uma heurística admissível, e apresenta consumo de memória muito menor que o A* (proporcional à profundidade da solução). Como desvantagem, pode expandir repetidamente os mesmos nós em diferentes iterações, aumentando o tempo de execução.

**SMA\* (Simplified Memory-Bounded A\*).** É uma variação do algoritmo A* que opera dentro de um limite de memória predefinido. Enquanto o A* clássico pode consumir memória exponencialmente à medida que a busca cresce, o SMA* utiliza todo o espaço disponível; quando a memória se esgota, remove o nó folha menos promissor (de maior f) e guarda seu valor de f no nó pai, para poder regenerá-lo mais tarde se necessário. Ele é completo se a solução couber na memória e encontra a melhor solução que pode ser representada dentro do limite de memória.

## 6. Comparação entre os algoritmos

Considere um problema em que um agente precisa encontrar um caminho entre duas cidades. Na BFS, o agente explora primeiro todas as cidades a uma distância de uma conexão, depois duas conexões e assim sucessivamente. Na DFS, o agente segue um caminho até determinado limite antes de retroceder. Na UCS, o agente prioriza o caminho com menor custo acumulado, considerando, por exemplo, as distâncias percorridas. Na busca gulosa, o agente prioriza a cidade aparentemente mais próxima do destino, utilizando uma estimativa de distância. No A*, o agente considera simultaneamente a distância já percorrida e a distância estimada até o destino. Portanto, enquanto as estratégias sem informação exploram o espaço de estados sem estimar a proximidade da solução, as estratégias informadas utilizam conhecimento heurístico para orientar a tomada de decisão.

A busca gulosa utiliza somente h(n), enquanto o A* utiliza g(n) + h(n). Essa diferença explica por que o A* considera tanto o custo já percorrido quanto o custo estimado restante, podendo garantir uma solução ótima quando as condições de admissibilidade e implementação são satisfeitas. A tabela a seguir resume as propriedades dos principais algoritmos (b = fator de ramificação, d = profundidade da melhor solução, m = profundidade máxima, L = limite de profundidade):

| Algoritmo | Completo? | Ótimo? | Tempo | Espaço |
|---|---|---|---|---|
| BFS | Sim (b finito) | Sim, se custos uniformes | $O(b^d)$ | $O(b^d)$ |
| UCS | Sim, se c ≥ ε > 0 | Sim | $O(b^(1+⌊C*/ε⌋))$ | $O(b^(1+⌊C*/ε⌋))$ |
| DFS | Não (em árvores/espaços infinitos) | Não | O(b^m) | O(bm) |
| DLS | Não (se L < d) | Não | $O(b^L)$ | O(bL) |
| IDS | Sim | Sim, se custos uniformes | $O(b^d)$ | O(bd) |
| Bidirecional | Sim (com BFS) | Sim, se custos uniformes | $O(b^(d/2))$ | $O(b^(d/2))$ |
| Gulosa | Não (em árvores) | Não | $O(b^m)$ | $O(b^m)$ |
| A* | Sim, se c ≥ ε > 0 | Sim, se h admissível (árvore) ou consistente (grafo) | exponencial | exponencial |

## 7. Busca local

Os algoritmos de busca local, como o hill climbing e o simulated annealing, operam de forma diferente dos anteriores: em vez de manter a fronteira completa, mantêm apenas o estado corrente (ou um pequeno conjunto de estados) e exploram a vizinhança local, sendo adequados a problemas de otimização em que o caminho até a solução é irrelevante e apenas o estado final importa. Como não guardam a árvore de busca inteira, esses algoritmos são ideais para problemas com espaços de estados gigantescos ou infinitos (por exemplo, otimização de rotas e alocação de recursos). Entretanto, eles podem ficar presos em ótimos locais (pontos que são melhores que seus vizinhos diretos, mas piores que o ótimo global do problema). Os principais algoritmos desse grupo são descritos a seguir.

**Subida de encosta (Hill Climbing).** É o algoritmo de busca local mais clássico. Ele avalia os vizinhos do estado atual e se move para o vizinho que trouxer a maior melhoria em relação a uma função objetivo V (ou, equivalentemente, para o de menor custo heurístico, se o problema for de minimização):

s ← argmax V(s'), com s' ∈ vizinhos(s); o algoritmo para quando nenhum vizinho tem V(s') > V(s).

Uma analogia seria como tentar subir uma montanha no meio de uma névoa espessa: você olha ao redor, dá um passo na direção que parece subir mais rápido e repete. Entretanto, o algoritmo é vulnerável a extremos locais (picos mais altos que os vizinhos, mas que não são o ponto mais alto do mapa) e a platôs (regiões planas, onde nenhum vizinho é melhor). Variações como reinício aleatório (random restart) reduzem esse problema.

**Têmpera simulada (Simulated Annealing).** É inspirada no processo de metalurgia (em que o metal é aquecido e resfriado lentamente para cristalizar sem defeitos). A cada passo, sorteia-se um vizinho s'; se ele for melhor, é aceito; se for pior, com ΔE = V(s') − V(s) < 0, é aceito com probabilidade

$P = e^{(ΔE / T)}$,

em que T é a "temperatura". No início (T alta), P é próxima de 1 e o algoritmo aceita movimentos ruins com frequência para escapar de máximos locais. À medida que o tempo passa e a temperatura "esfria" (T → 0), P → 0 e ele se torna mais estrito, aceitando praticamente só movimentos de melhoria. Se o resfriamento for suficientemente lento, o algoritmo converge para o ótimo global com probabilidade que tende a 1, ao custo de uma convergência mais lenta.

**Busca local em feixe (Local Beam Search).** Em vez de manter apenas um único estado atual, o algoritmo acompanha k estados simultaneamente. Em cada passo, todos os vizinhos de todos os k estados são gerados. Destes, apenas os k melhores de todo o grupo são selecionados para a próxima rodada. Isso permite compartilhar informações entre diferentes caminhos de busca, o que a diferencia de simplesmente executar k buscas independentes.

**Algoritmos genéticos.** É uma estratégia de busca populacional inspirada na evolução natural, que mantém um conjunto de estados candidatos (população) e gera novas soluções por meio de operadores genéticos, como seleção dos indivíduos mais aptos, cruzamento (crossover) entre dois estados (pais) e pequenas alterações aleatórias (mutação). O processo é repetido ao longo de várias gerações, buscando produzir soluções cada vez melhores de acordo com uma função de aptidão (fitness). No problema das 8 rainhas, por exemplo, um indivíduo pode ser codificado como uma cadeia de 8 dígitos (a linha da rainha em cada coluna), como 32752411; a aptidão pode ser o número de pares de rainhas que não se atacam (máximo 28); o cruzamento troca os sufixos de dois pais (32752|411 e 24748|552 geram 32752|552); e a mutação altera aleatoriamente um dígito.

## 8. Busca com satisfação de restrições (CSP)

Uma terceira família de problemas não busca um caminho nem otimiza uma função, mas procura uma atribuição de valores que respeite um conjunto de condições. A busca com satisfação de restrições (Constraint Satisfaction Problems – CSP) aborda problemas nos quais se busca atribuir valores a um conjunto de variáveis, respeitando seus respectivos domínios e satisfazendo todas as restrições definidas entre elas. Formalmente, um CSP é composto por três elementos: um conjunto de variáveis X = {X₁, …, Xₙ}, os domínios D = {D₁, …, Dₙ} de valores possíveis para cada variável e um conjunto de restrições C que estabelecem as condições que devem ser satisfeitas pelas atribuições. Nesse contexto, o objetivo não é encontrar um caminho até um estado, mas encontrar uma atribuição completa e consistente de valores às variáveis. Exemplos incluem problemas clássicos como o das N-rainhas, a coloração de grafos e o Sudoku.

**Exemplo (coloração do mapa da Austrália).** As variáveis são as regiões X = {WA, NT, SA, Q, NSW, V, T}; o domínio de cada uma é {vermelho, verde, azul}; e as restrições dizem que regiões vizinhas devem ter cores diferentes, como WA ≠ NT, WA ≠ SA, NT ≠ SA, NT ≠ Q, SA ≠ Q, SA ≠ NSW, SA ≠ V, Q ≠ NSW e NSW ≠ V. Uma solução é WA = vermelho, NT = verde, SA = azul, Q = vermelho, NSW = verde, V = vermelho e T = qualquer cor. Sem aproveitar a estrutura do problema, haveria 3⁷ = 2.187 atribuições completas possíveis para testar.

Técnicas como backtracking, forward checking e consistência de arco são utilizadas para reduzir o espaço de busca e aumentar a eficiência da resolução. O algoritmo de **backtracking com propagação de restrições** constitui uma das principais abordagens para resolver CSPs. A cada passo, uma variável não atribuída é selecionada, um valor de seu domínio é escolhido e as restrições são verificadas. Caso uma inconsistência seja detectada, o algoritmo retrocede e tenta outro valor disponível, explorando sistematicamente as possíveis atribuições.

Heurísticas de ordenação reduzem significativamente o esforço de busca. Para escolher a variável, usa-se a **Minimum Remaining Values (MRV)**, que seleciona a variável não atribuída com o menor número de valores restantes em seu domínio, e a **Degree Heuristic**, que prioriza a variável envolvida no maior número de restrições com outras variáveis ainda não atribuídas (útil para desempatar a MRV). Para escolher o valor, usa-se a **Least Constraining Value (LCV)**, que prefere o valor que menos reduz os domínios dos vizinhos. No mapa da Austrália, após atribuir WA = vermelho e NT = verde, a variável SA tem apenas um valor restante (azul) e a MRV a escolhe em seguida.

Técnicas de propagação de restrições, como a verificação antecipada (forward checking) e o algoritmo AC-3 (Arc Consistency Algorithm 3), também contribuem para essa redução. O **forward checking** elimina dos domínios das variáveis vizinhas os valores incompatíveis com uma atribuição recém-realizada (no exemplo, ao atribuir WA = vermelho, remove-se vermelho dos domínios de NT e SA). Já o **AC-3** propaga a **consistência de arco** entre variáveis relacionadas por restrições binárias: um arco (Xᵢ, Xⱼ) é consistente se, para todo valor x ∈ Dᵢ, existe algum valor y ∈ Dⱼ que satisfaz a restrição entre Xᵢ e Xⱼ; valores sem suporte são removidos de Dᵢ. Por exemplo, com a restrição X < Y e D_X = D_Y = {1, 2, 3}, a revisão do arco (X, Y) remove 3 de D_X (não há y > 3) e a do arco (Y, X) remove 1 de D_Y (não há x < 1), resultando em D_X = {1, 2} e D_Y = {2, 3}. O AC-3 repete essas revisões até que não haja mais mudanças, em tempo O(c·d³), em que c é o número de restrições binárias e d o tamanho máximo dos domínios. Essas técnicas permitem detectar inconsistências antecipadamente, reduzindo o número de retrocessos necessários. Para CSPs grandes, também é comum usar busca local com a heurística de **mínimos conflitos** (min-conflicts), que reatribui uma variável em conflito ao valor que viola o menor número de restrições.

## 9. Busca competitiva

Por fim, a busca competitiva refere-se a cenários em que múltiplos agentes interagem em ambientes adversariais, contexto típico de jogos de soma zero como xadrez, damas e Go. Nesses casos, o problema é modelado como uma árvore de decisões em que os agentes com objetivos conflitantes alternam suas jogadas: o jogador MAX tenta maximizar a utilidade e o jogador MIN tenta minimizá-la. O algoritmo **minimax** maximiza o ganho de um agente assumindo que o oponente também age de forma racional, calculando:

MINIMAX(s) = UTILIDADE(s), se s é terminal;
MINIMAX(s) = max_a MINIMAX(RESULTADO(s, a)), se é a vez de MAX;
MINIMAX(s) = min_a MINIMAX(RESULTADO(s, a)), se é a vez de MIN.

A principal limitação do minimax é seu custo exponencial em relação à profundidade da árvore: tempo O(b^m) e espaço O(bm) (varredura em profundidade). Como exemplo, considere uma árvore em que MAX escolhe entre três jogadas, cada uma levando a um nó de MIN com três folhas: (3, 12, 8), (2, 4, 6) e (14, 5, 2). Os nós de MIN valem min = 3, 2 e 2, respectivamente, e o valor do nó raiz é max(3, 2, 2) = 3, de modo que MAX escolhe a primeira jogada.

A **poda alfa-beta** (alpha-beta pruning) reduz esse custo ao eliminar ramos que não podem influenciar a decisão final (reduzindo o número de nós avaliados sem alterar o resultado do minimax), tornando viável a aplicação em problemas de maior complexidade. Ela mantém dois limites: α (melhor valor já garantido para o maximizador ao longo do caminho) e β (melhor valor já garantido para o minimizador), e descarta subárvores em que α ≥ β. No exemplo anterior, depois de avaliar o primeiro nó de MIN (valor 3), tem-se α = 3. No segundo nó de MIN, a primeira folha vale 2; como 2 ≤ α, esse nó nunca valerá mais que 2 e não pode superar o 3 já garantido, de modo que as folhas 4 e 6 não precisam ser avaliadas. No melhor caso (com boa ordenação das jogadas), a alfa-beta reduz a complexidade de O(b^m) para O(b^(m/2)), o que dobra a profundidade explorável com o mesmo orçamento computacional e viabiliza problemas mais complexos.

Em jogos com horizonte temporal limitado, funções de avaliação heurística substituem o cálculo exato do valor minimax nos estados correspondentes às folhas da árvore de busca truncada, estimando a qualidade das posições alcançadas. Uma forma comum é a combinação linear de características:

Aval(s) = w₁·f₁(s) + w₂·f₂(s) + … + wₙ·fₙ(s).

No xadrez, por exemplo, f₁ pode ser a diferença de peças de cada tipo e os pesos podem ser os valores materiais usuais (peão 1, cavalo e bispo 3, torre 5, dama 9). Em ambientes que envolvem eventos aleatórios, como lançamentos de dados, o algoritmo **expectiminimax** estende o minimax por meio da introdução de nós de chance, nos quais são calculados os valores esperados das possíveis jogadas, considerando suas respectivas probabilidades:

EXPECTIMINIMAX(s) = Σᵣ P(r) · EXPECTIMINIMAX(RESULTADO(s, r)), para nós de chance.

**Busca em árvore Monte Carlo (MCTS).** Abordagens modernas, como a MCTS (Monte Carlo Tree Search), combinam amostragem aleatória com expansão seletiva da árvore de busca, priorizando as decisões mais promissoras sem precisar explorar todas as possibilidades. Em vez de analisar todas as jogadas possíveis, o MCTS simula muitas partidas a partir das opções disponíveis e aprende, na prática, quais decisões funcionam melhor. O algoritmo tem quatro etapas:

1. **Seleção:** percorre a árvore existente para escolher um nó promissor.
2. **Expansão:** adiciona novos nós que representam ações ainda não exploradas.
3. **Simulação:** executa uma trajetória a partir do novo nó até uma condição terminal ou um limite predefinido.
4. **Retropropagação:** atualiza as estatísticas dos nós visitados com base no resultado obtido.

O processo se repete até um limite de tempo ou de simulações, e então se escolhe a ação de melhor desempenho estimado. Uma estratégia comum para equilibrar a exploração de ações pouco avaliadas e o aproveitamento das que já têm bons resultados é a Upper Confidence Bound for Trees (UCT), que usa o valor médio das recompensas e um termo de exploração:

UCT(i) = Qᵢ / Nᵢ + c · √( ln N / Nᵢ ),

em que Qᵢ é a soma das recompensas obtidas passando pelo filho i, Nᵢ é o número de visitas a i, N é o número de visitas ao nó pai e c é a constante de exploração (frequentemente c = √2). O primeiro termo favorece o aproveitamento (médias altas) e o segundo, a exploração (nós pouco visitados). Entre as vantagens do MCTS estão a flexibilidade, a capacidade de lidar com espaços de busca complexos e a concentração de recursos nas alternativas promissoras. Seu desempenho, porém, depende da qualidade das simulações, da função de recompensa e do orçamento computacional. Além de jogos como Go e xadrez, é empregado em planejamento robótico e otimização combinatória, e pode ser combinado com redes neurais para orientar a seleção de ações e estimar resultados futuros, como veremos a seguir.

## 10. Heurísticas aprendidas: busca e aprendizado profundo

Nas abordagens tradicionais de busca em inteligência artificial, as heurísticas, como a distância em linha reta utilizada na busca A*, são frequentemente projetadas com base no conhecimento de especialistas ou em propriedades matemáticas do problema. Entretanto, em domínios complexos, como o Cubo de Rubik (com cerca de 4,3 × 10¹⁹ estados), o xadrez ou o dobramento de proteínas, desenvolver funções capazes de estimar com precisão o custo restante até o objetivo pode ser extremamente difícil ou inviável. Sistemas modernos utilizam redes neurais para automatizar esse processo.

Nesse contexto, as redes neurais profundas (Deep Learning) permitem aprender heurísticas e funções de avaliação a partir de dados ou da interação com o ambiente, inclusive por meio do aprendizado por reforço. Essas funções podem orientar a exploração do espaço de estados, contribuindo para que os algoritmos de busca priorizem estados mais promissores e reduzam o esforço computacional necessário para encontrar soluções. Redes neurais profundas são treinadas como aproximadoras de funções: elas recebem o estado atual do problema como entrada (por exemplo, a imagem de um tabuleiro) e fazem uma predição rápida (forward pass) para estimar o valor de h(n), substituindo fórmulas geométricas ou matemáticas tradicionais.

**DeepCubeA.** Essa arquitetura combina o algoritmo de busca clássico A* (na variante ponderada, f(n) = λ·g(n) + h(n), com 0 < λ ≤ 1) com aprendizado por reforço profundo. Ela foi projetada para resolver problemas de caminhos complexos, como o Cubo de Rubik. O DeepCubeA aprende a heurística gerando estados por embaralhamentos a partir do estado resolvido (isto é, em sentido reverso) e atualizando iterativamente a estimativa de custo até o objetivo. Com isso, consegue encontrar soluções de qualidade ótima ou muito próxima da ótima na grande maioria dos casos, explorando apenas uma fração minúscula do espaço de estados.

**AlphaZero.** O AlphaZero, da DeepMind, é outro exemplo dessa combinação. Ele combina redes neurais profundas, busca em MCTS e aprendizado por reforço (Reinforcement Learning) para aprender a jogar jogos como xadrez, Go e shogi sem depender de conhecimento especializado sobre estratégias humanas (além das regras do jogo). Sua arquitetura utiliza uma rede neural fθ que recebe como entrada o estado atual do jogo s e produz duas saídas, (p, v) = fθ(s): uma política (policy) p, que estima a probabilidade de selecionar cada ação possível, e um valor (value) v ∈ [−1, 1], que estima o resultado esperado da partida a partir daquele estado (da derrota à vitória), atuando como a função heurística automática. Essas informações orientam o MCTS, que explora possíveis sequências de ações, simulando trajetórias futuras e equilibrando a exploração de movimentos promissores com o aproveitamento daqueles que já apresentam bons resultados. No AlphaZero, a seleção usa uma variante da UCT que incorpora a política da rede (PUCT):

a = argmax_a [ Q(s, a) + c · P(s, a) · √N(s) / (1 + N(s, a)) ],

em que P(s, a) é a probabilidade a priori fornecida pela rede. Durante o treinamento, o AlphaZero joga contra si mesmo (self-play) em um processo contínuo de aprendizado por reforço, utilizando os resultados z das partidas (+1, 0 ou −1) e as distribuições de visitas π do MCTS para atualizar os parâmetros da rede, minimizando a perda

ℓ = (z − v)² − πᵀ log p + c′‖θ‖².

A combinação entre busca e aprendizado por reforço permite que o algoritmo desenvolva estratégias progressivamente mais eficientes, sem utilizar bases de partidas humanas ou avaliações heurísticas específicas para cada jogo. (Seu antecessor, o AlphaGo, usava inicialmente partidas de jogadores humanos no treinamento.) Dessa forma, o AlphaZero exemplifica uma abordagem na qual a rede neural generaliza padrões estratégicos via reforço, enquanto o MCTS realiza uma busca deliberada por ações promissoras, combinando aprendizado estatístico e planejamento para a tomada de decisões em ambientes com grandes espaços de estados e ações. As duas saídas da rede desempenham papéis distintos:

- **Rede de políticas (Policy Network):** avalia as ações disponíveis e indica quais caminhos são promissores. Isso impede que a árvore expanda ramos absurdos ou inválidos, realizando uma poda inteligente.
- **Rede de valor (Value Network):** atua como a função heurística automática. Ela avalia um estado da simulação e fornece uma nota probabilística de vitória. Isso elimina a necessidade de simular o jogo exaustivamente até o final para saber se a jogada foi boa.

**Tree of Thoughts (ToT).** A ideia de busca também chegou aos grandes modelos de linguagem (LLMs). O Tree of Thoughts é um método de raciocínio em que, em vez de gerar o texto de forma puramente linear (como na cadeia de pensamento comum), o modelo gera múltiplos "pensamentos" intermediários candidatos, avalia a qualidade de cada um (o próprio modelo julga se o ramo é promissor ou sem saída) e conduz uma busca estruturada em árvore sobre eles, utilizando algoritmos clássicos como BFS ou DFS. Se uma contradição ou erro for detectado, aplica-se o conceito clássico de backtracking, abandonando o ramo e tentando outra linha de pensamento. Um exemplo é o jogo dos 24: dados quatro números (como 4, 9, 10 e 13), cada pensamento é uma operação parcial (por exemplo, 13 − 9 = 4, restando 4, 4, 10), e o avaliador classifica cada estado como "certamente alcança 24", "talvez" ou "impossível", podando os ramos impossíveis. Já os modelos modernos de raciocínio, treinados para produzir longas cadeias de pensamento antes de responder, podem exibir comportamentos semelhantes (explorar hipóteses, descartar e retomar), mas isso emerge do treinamento do modelo; não se deve supor que executem internamente uma busca em árvore explícita como a do ToT.

## 11. Garantias teóricas e síntese

Heurísticas aprendidas costumam apresentar bom desempenho empírico, mas ele não garante as propriedades teóricas exigidas por certos algoritmos: uma rede neural pode superestimar o custo restante e, portanto, não ser admissível. No caso do A*, por exemplo, a garantia de otimalidade depende das condições da busca e das propriedades da heurística utilizada, como a admissibilidade e, em determinadas implementações, a consistência. Se h(n) > h*(n) em algum nó, o A* pode devolver uma solução de custo maior que C* (no A* ponderado, o limite é w·C*). Portanto, quando a obtenção de uma solução ótima é fundamental, essas propriedades devem ser verificadas ou devem ser adotados mecanismos que preservem as garantias teóricas do algoritmo.

Em síntese, as diferentes estratégias de busca oferecem abordagens complementares para a resolução de problemas em IA, variando quanto à utilização de informação, eficiência e garantias teóricas. A escolha do método mais adequado depende das características do problema, como tamanho do espaço de estados, disponibilidade de heurísticas, presença de restrições ou adversários e recursos computacionais. A evolução para técnicas como o MCTS demonstra que os fundamentos clássicos da busca permanecem vivos e relevantes, frequentemente servindo de alicerce para os sistemas de inteligência artificial mais avançados da atualidade, inclusive aqueles baseados em aprendizado profundo e por reforço.
