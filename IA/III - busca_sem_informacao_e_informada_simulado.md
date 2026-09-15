# SIMULADO — Estratégias de Busca sem Informação e Busca Informada
### Busca em largura, profundidade, custo uniforme, aprofundamento iterativo | Busca gulosa, A*, heurísticas admissíveis e consistentes

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas clássicas de Inteligência Artificial / Busca em espaço de estados.

---

**1.** Estratégias de busca **sem informação** (cega/"uninformed") são caracterizadas por:

a) Utilizar uma função heurística para estimar a distância até o objetivo
b) Não possuir nenhuma informação adicional sobre o problema além da própria definição do espaço de estados (estado inicial, ações, teste de objetivo e custo de caminho)
c) Serem sempre mais rápidas do que estratégias informadas
d) Utilizarem exclusivamente inteligência artificial baseada em redes neurais

> **Gabarito: b.** Buscas cegas/sem informação exploram o espaço de estados apenas com base na definição formal do problema, sem qualquer estimativa (heurística) de quão perto um estado está do objetivo.

---

**2.** A Busca em Largura (BFS — Breadth-First Search) explora o espaço de estados:

a) Expandindo primeiro o nó mais profundo da árvore de busca
b) Expandindo os nós nível por nível, isto é, todos os nós de profundidade *d* antes de qualquer nó de profundidade *d+1*
c) Utilizando uma pilha (LIFO) como estrutura de dados principal
d) Selecionando aleatoriamente o próximo nó a expandir

> **Gabarito: b.** A BFS usa uma fila (FIFO) e expande os nós em ordem de profundidade crescente, camada por camada.

---

**3.** **(Pegadinha)** Sobre a completude e otimalidade da Busca em Largura, é correto afirmar que:

a) A BFS nunca é completa, mesmo em espaços de estados finitos
b) A BFS é completa (encontra uma solução se ela existir) e, se todos os custos de passo forem iguais (ex.: todos = 1), também é ótima; porém, se os custos de passo forem diferentes, a BFS não garante encontrar a solução de menor custo
c) A BFS é sempre ótima, independentemente dos custos de cada passo/ação
d) A BFS não pode ser aplicada a espaços de estados infinitos sob nenhuma hipótese

> **Gabarito: b.** Pegadinha: a otimalidade da BFS depende da premissa de custos de passo uniformes/iguais — em grafos com custos de aresta diferentes, a BFS pode encontrar uma solução com mais passos, porém de menor custo total, e não identificá-la como a melhor.

---

**4.** A Busca em Profundidade (DFS — Depth-First Search) utiliza tipicamente qual estrutura de dados para gerenciar a fronteira de nós a expandir?

a) Fila (FIFO)
b) Pilha (LIFO) — ou recursão, que implicitamente usa uma pilha de chamadas
c) Fila de prioridade ordenada por custo
d) Tabela hash sem ordenação

> **Gabarito: b.** A DFS explora o ramo mais profundo primeiro, retrocedendo (backtracking) quando não há mais como avançar — comportamento naturalmente implementado com uma pilha (LIFO).

---

**5.** **(Pegadinha)** Em relação à Busca em Profundidade (DFS) em espaços de estados infinitos ou com ciclos, sem controle de estados visitados, é correto afirmar que:

a) A DFS é sempre completa, mesmo em espaços infinitos
b) A DFS pode entrar em um ramo infinito e nunca encontrar uma solução existente, mesmo que ela esteja em outro ramo da árvore — ou seja, não é, em geral, completa em espaços infinitos ou com ciclos não controlados
c) A DFS sempre encontra a solução de menor custo
d) A DFS nunca pode ser usada em problemas com espaço de estados muito grande

> **Gabarito: b.** Pegadinha: diferentemente da BFS, a DFS pode "descer" indefinidamente por um ramo infinito (ou ciclo) sem nunca retroceder para explorar outros ramos onde a solução realmente está — por isso não é completa em geral, salvo com tratamento de estados repetidos ou espaço finito.

---

**6.** A principal vantagem da DFS em relação à BFS, em termos de recursos computacionais, é:

a) A DFS é sempre mais rápida em número de nós expandidos
b) A DFS geralmente requer bem menos memória, pois só precisa armazenar o caminho atual e os nós irmãos não explorados, em vez de todos os nós de uma camada inteira
c) A DFS é sempre completa e ótima, ao contrário da BFS
d) A DFS elimina totalmente a necessidade de backtracking

> **Gabarito: b.** A complexidade de espaço da DFS é tipicamente O(b·m) (linear na profundidade), muito menor que a complexidade de espaço exponencial da BFS, O(b^d).

---

**7.** A Busca de Custo Uniforme (Uniform-Cost Search) expande, a cada passo, o nó da fronteira com:

a) A maior profundidade na árvore de busca
b) O menor custo de caminho acumulado desde a raiz (g(n)) até aquele nó
c) O maior número de filhos
d) O valor heurístico mais baixo

> **Gabarito: b.** A Busca de Custo Uniforme usa uma fila de prioridade ordenada por g(n), o custo acumulado do caminho, garantindo expandir sempre o nó de menor custo total até o momento.

---

**8.** **(Pegadinha)** Qual é a relação entre a Busca em Largura (BFS) e a Busca de Custo Uniforme?

a) São exatamente o mesmo algoritmo, sem qualquer distinção
b) A BFS é um caso especial da Busca de Custo Uniforme quando todos os custos de passo são iguais (por exemplo, iguais a 1) — nesse caso particular, ambas produzem os mesmos resultados
c) A BFS é sempre mais lenta que a Busca de Custo Uniforme, mesmo com custos iguais
d) A Busca de Custo Uniforme nunca pode ser reduzida à BFS, em nenhuma circunstância

> **Gabarito: b.** Pegadinha: embora sejam algoritmos distintos em geral (BFS ordena por profundidade; custo uniforme ordena por custo acumulado), quando todos os custos de passo são idênticos elas coincidem em comportamento e resultado.

---

**9.** A Busca em Profundidade Limitada (Depth-Limited Search) resolve qual problema típico da DFS pura?

a) O alto consumo de memória
b) A possibilidade de a DFS "se perder" descendo indefinidamente por um ramo infinito, impondo um limite máximo de profundidade *l* para a exploração
c) A ausência de heurística
d) A necessidade de ordenar os nós por custo

> **Gabarito: b.** Ao impor um limite de profundidade *l*, evita-se que a busca desça indefinidamente por ramos infinitos — ao custo de poder não encontrar soluções que estejam além desse limite.

---

**10.** **(Pegadinha)** A Busca de Aprofundamento Iterativo (Iterative Deepening Search — IDS) combina:

a) As vantagens de memória da BFS com a completude teórica da DFS
b) As vantagens de memória da DFS (baixo uso de memória) com a completude e otimalidade (sob custos uniformes) tipicamente associadas à BFS, executando buscas de profundidade limitada sucessivas com limites crescentes (0, 1, 2, ...)
c) É idêntica à DFS pura, sem qualquer diferença prática
d) Elimina totalmente a necessidade de reexpandir nós já visitados em iterações anteriores

> **Gabarito: b.** Pegadinha: é comum inverter as vantagens — a IDS busca justamente unir o baixo consumo de memória da DFS com as garantias de completude/otimalidade (com custos uniformes) da BFS, ainda que reexpanda nós de camadas superiores a cada nova iteração (o que, surpreendentemente, tem custo assintótico aceitável).

---

**11.** Sobre a Busca Bidirecional, é correto afirmar que:

a) Ela nunca pode ser aplicada quando as ações são reversíveis
b) Ela busca simultaneamente a partir do estado inicial em direção ao objetivo e a partir do objetivo em direção ao estado inicial, encontrando-se no meio — o que pode reduzir drasticamente a complexidade de tempo em relação a uma busca unidirecional equivalente
c) Ela é idêntica, em desempenho, à busca em profundidade
d) Ela exige necessariamente uma heurística para funcionar

> **Gabarito: b.** A busca bidirecional explora "dos dois lados" simultaneamente, o que pode reduzir a complexidade de O(b^d) para aproximadamente O(b^(d/2)) em cada frente — mas exige que seja viável identificar predecessores e gerar buscas reversas a partir do objetivo.

---

**12.** Uma **função heurística** h(n), em busca informada, estima:

a) O custo já percorrido desde o estado inicial até o nó n
b) O custo estimado do caminho mais barato do nó n até um estado objetivo
c) O número total de nós já expandidos na busca
d) A profundidade exata do nó n na árvore de busca

> **Gabarito: b.** h(n) é uma estimativa (nem sempre exata) do custo restante até o objetivo, a partir do estado n — é essa estimativa que orienta as buscas informadas.

---

**13.** **(Pegadinha)** Uma heurística h(n) é dita **admissível** quando:

a) Ela sempre superestima o custo real até o objetivo, para garantir uma busca mais rápida
b) Ela nunca superestima o custo real (verdadeiro) do caminho mais barato até o objetivo, ou seja, h(n) ≤ h*(n) para todo n, sendo h*(n) o custo real ótimo
c) Ela é igual a zero para todos os nós, exceto o nó objetivo
d) Ela é calculada exclusivamente por métodos estatísticos, nunca de forma analítica

> **Gabarito: b.** Pegadinha: é o contrário do que a alternativa "a" afirma — admissibilidade exige que a heurística nunca **superestime** o custo real restante (ela pode subestimar, inclusive sendo igual a zero, mas nunca prometer menos trabalho do que realmente existe).

---

**14.** A Busca Gulosa (Greedy Best-First Search) expande, a cada passo, o nó com:

a) O menor valor de g(n), o custo acumulado
b) O menor valor de h(n), a estimativa heurística até o objetivo, ignorando o custo já percorrido
c) O maior valor de f(n) = g(n) + h(n)
d) A maior profundidade

> **Gabarito: b.** A busca gulosa é "míope": escolhe sempre o nó que *parece* mais próximo do objetivo segundo h(n), sem considerar quanto custo já foi gasto para chegar até ali.

---

**15.** **(Pegadinha)** Sobre a Busca Gulosa (Greedy Best-First Search), é correto afirmar que:

a) Ela é sempre ótima, pois usa uma heurística
b) Mesmo utilizando uma heurística admissível, a busca gulosa **não** garante, em geral, encontrar a solução de menor custo, pois ignora o custo já percorrido (g(n)) e pode seguir por caminhos aparentemente promissores que, na verdade, são mais caros no total
c) Ela é idêntica ao algoritmo A* em todos os casos
d) Ela nunca pode ficar "presa" em decisões subótimas

> **Gabarito: b.** Pegadinha: admissibilidade da heurística garante otimalidade para o A*, mas **não** para a busca gulosa, já que essa ignora totalmente g(n) — pode escolher um caminho que parece bom localmente, mas que se revela pior globalmente.

---

**16.** O algoritmo **A\*** utiliza a função de avaliação:

a) f(n) = h(n) apenas
b) f(n) = g(n) apenas
c) f(n) = g(n) + h(n), combinando o custo já percorrido com a estimativa heurística restante
d) f(n) = g(n) − h(n)

> **Gabarito: c.** A ideia central do A* é equilibrar "quanto já custou chegar até aqui" (g) com "quanto deve custar dali até o objetivo" (h), evitando tanto a "miopia" da busca gulosa quanto a "cegueira" da busca de custo uniforme.

---

**17.** **(Pegadinha)** O algoritmo A*, usando uma heurística **admissível** em busca em árvore (tree search, sem verificação de estados repetidos), é:

a) Apenas completo, mas não ótimo
b) Completo e ótimo — encontra a solução de menor custo, caso exista
c) Nem completo, nem ótimo, servindo apenas para estimativas aproximadas
d) Ótimo apenas quando h(n) = 0 para todos os nós

> **Gabarito: b.** Pegadinha: um erro comum é achar que A* só é "uma boa aproximação"; na verdade, com heurística admissível, o A* tem a garantia formal de otimalidade (e completude, em espaços com custos de passo positivos) — é um dos resultados mais importantes da busca informada.

---

**18.** **(Pegadinha)** Uma heurística h(n) é dita **consistente** (ou monótona) quando, para todo nó n e todo sucessor n' gerado por uma ação de custo c(n,n'):

a) h(n) ≥ h(n') + c(n,n'), ou seja, o custo estimado nunca pode diminuir mais do que o custo real de uma ação
b) h(n) ≤ c(n,n') + h(n'), garantindo que a estimativa não "cai" mais rápido do que o custo real percorrido — o que implica que a sequência de valores f(n) ao longo de qualquer caminho é não decrescente
c) h(n) é sempre igual a h(n')
d) h(n) é sempre maior que h*(n), o custo real

> **Gabarito: b.** Consistência é uma condição mais forte que admissibilidade: garante que f(n) nunca diminui ao longo de um caminho, o que permite ao A* evitar reabrir nós já expandidos (tornando a busca em grafo mais eficiente e ainda ótima).

---

**19.** Toda heurística consistente é necessariamente admissível. Já o contrário:

a) Também é sempre verdadeiro: toda heurística admissível é necessariamente consistente
b) Não é necessariamente verdadeiro: existem heurísticas admissíveis que não são consistentes, embora, na prática, muitas heurísticas comuns (como distância em linha reta) sejam ambas
c) É impossível determinar, pois admissibilidade e consistência são conceitos totalmente independentes
d) Nunca ocorre na prática, sendo apenas um exercício teórico sem exemplos reais

> **Gabarito: b.** Consistência implica admissibilidade, mas a recíproca não vale em geral — é possível construir (embora seja incomum na prática cotidiana) heurísticas admissíveis que violam a condição de consistência em algum par de nós.

---

**20.** No problema clássico do quebra-cabeça de 8 peças (8-puzzle), qual das opções é um exemplo comum de heurística admissível?

a) O número de peças fora do lugar (Hamming) e a soma das distâncias de Manhattan de cada peça até sua posição objetivo
b) O número total de movimentos já realizados desde o início
c) Um valor aleatório gerado a cada expansão de nó
d) A profundidade máxima da árvore de busca

> **Gabarito: a.** Ambas — número de peças fora do lugar e distância de Manhattan — são heurísticas clássicas e admissíveis para o 8-puzzle, pois nunca superestimam o número mínimo de movimentos necessários.

---

**21.** **(Pegadinha)** Comparando duas heurísticas admissíveis h1 e h2 para o mesmo problema, se h2(n) ≥ h1(n) para todo nó n (sendo ambas admissíveis), diz-se que h2 **domina** h1. Isso implica que:

a) h2 é necessariamente pior, pois superestima mais o custo
b) A busca A* usando h2 tende a expandir um número igual ou menor de nós do que usando h1, sendo geralmente mais eficiente, mantendo-se ambas admissíveis (portanto, o A* continua ótimo com qualquer uma das duas)
c) h2 deixa de ser admissível automaticamente, pois é maior que h1
d) A dominância entre heurísticas não tem qualquer relação com a eficiência da busca

> **Gabarito: b.** Pegadinha: uma heurística maior (mas ainda admissível — ou seja, ainda ≤ custo real) é mais "informativa" e tende a reduzir o número de nós expandidos pelo A*, sem perder a garantia de otimalidade.

---

**22.** A variante **IDA\*** (Iterative Deepening A*) tem como principal motivação:

a) Eliminar totalmente o uso de heurísticas
b) Combinar os benefícios de memória da busca em profundidade limitada com a orientação heurística do A*, evitando o alto consumo de memória que o A* tradicional pode ter ao armazenar toda a fronteira
c) Ser idêntica, em consumo de memória, ao A* tradicional
d) Substituir completamente g(n) por h(n)

> **Gabarito: b.** O IDA* realiza sucessivas buscas em profundidade limitadas por um valor de corte em f(n) = g(n)+h(n), crescente a cada iteração, reduzindo drasticamente o uso de memória em relação ao A* tradicional.

---

**23.** **(Pegadinha)** Um dos principais problemas práticos do algoritmo A* tradicional, especialmente em problemas com espaços de estados muito grandes, é:

a) Ele nunca encontra a solução ótima
b) O consumo de memória, pois o A* mantém todos os nós gerados na fronteira e/ou na lista de nós já explorados, o que pode se tornar proibitivo mesmo com heurísticas boas
c) Ele é incapaz de lidar com heurísticas admissíveis
d) Ele é sempre mais lento do que a busca cega em qualquer cenário

> **Gabarito: b.** Pegadinha: a limitação prática mais citada do A* não é sua qualidade de solução (que é ótima com heurística admissível), mas sim o consumo de memória — algo que motivou variantes como IDA* e A* com memória limitada (SMA*).

---

**24.** Em busca local, o algoritmo de **Subida da Colina (Hill Climbing)** funciona, em sua versão básica, movendo-se:

a) Sempre para o vizinho de pior valor, buscando explorar amplamente o espaço
b) Sempre para o vizinho com melhor valor (maior, em problemas de maximização) em relação ao estado atual, parando quando nenhum vizinho é melhor
c) Aleatoriamente, sem considerar o valor dos vizinhos
d) Mantendo toda a árvore de busca já explorada em memória, como o A*

> **Gabarito: b.** Hill climbing é uma busca local "gulosa": sempre escolhe o melhor vizinho imediato, sem manter histórico da árvore de busca — por isso, tem baixíssimo consumo de memória.

---

**25.** **(Pegadinha)** A principal limitação do Hill Climbing básico é que ele pode ficar preso em:

a) Um laço infinito garantido em todo e qualquer problema
b) Máximos locais, platôs (regiões planas) e cumes ("ridges"), interrompendo a busca antes de alcançar a solução ótima global, já que o algoritmo não enxerga além dos vizinhos imediatos
c) Nenhuma limitação relevante, pois sempre converge para o ótimo global
d) Apenas problemas com heurísticas inconsistentes

> **Gabarito: b.** Pegadinha: hill climbing não tem qualquer mecanismo de "olhar além" do vizinho imediato nem de retroceder, por isso é vulnerável a ficar preso nesses tipos de armadilhas topológicas do espaço de busca.

---

**26.** Diferente das buscas em árvore/grafo tradicionais (como BFS, DFS e A*), a busca local (como Hill Climbing e Simulated Annealing) é caracterizada por:

a) Manter toda a árvore de busca em memória, com todos os caminhos já percorridos
b) Trabalhar apenas com o estado atual (ou um pequeno conjunto de estados), sem manter o caminho percorrido, focando em encontrar um estado que otimize uma função objetivo, e não necessariamente um caminho até ele
c) Ser sempre completa e ótima, ao contrário das buscas em árvore
d) Não poder ser usada em problemas de otimização

> **Gabarito: b.** Buscas locais são especialmente úteis quando o caminho até a solução é irrelevante e o que importa é o estado final (ex.: otimização de configuração), com a vantagem de exigir memória praticamente constante.

---

**27.** O algoritmo de **Simulated Annealing (Recozimento Simulado)** se diferencia do Hill Climbing puro por:

a) Nunca aceitar movimentos que piorem o valor atual, exatamente como o Hill Climbing
b) Permitir, com uma certa probabilidade (que diminui ao longo do tempo, conforme um parâmetro de "temperatura"), a aceitação de movimentos para estados piores, o que ajuda a escapar de máximos locais
c) Exigir, obrigatoriamente, uma heurística admissível para funcionar
d) Ser idêntico ao algoritmo A* em sua estratégia de busca

> **Gabarito: b.** A ideia inspirada em processos físicos de recozimento é permitir "pioras" ocasionais no início da busca (temperatura alta), reduzindo essa permissividade gradualmente, o que ajuda a escapar de ótimos locais que prenderiam o Hill Climbing puro.

---

**28.** **(Pegadinha)** Um aluno afirma: "Se uma heurística é admissível, então o A* sempre expande o menor número possível de nós entre todos os algoritmos de busca informada corretos." Essa afirmação está:

a) Correta, pois admissibilidade garante o número mínimo de expansões em qualquer cenário
b) Incorreta — a admissibilidade garante a **otimalidade** da solução encontrada pelo A*, mas não garante, por si só, que o número de nós expandidos seja o menor possível; heurísticas mais informativas (que dominam outras, mas ainda admissíveis) tendem a expandir menos nós, evidenciando que a eficiência depende da qualidade específica da heurística, não apenas de sua admissibilidade
c) Correta, desde que o espaço de estados seja finito
d) Incorreta, pois admissibilidade não tem relação alguma com o desempenho do algoritmo

> **Gabarito: b.** Pegadinha: confundir "garantia de otimalidade da solução" com "garantia de eficiência máxima na busca" é um erro comum — são propriedades relacionadas, mas distintas (ver também a questão 21, sobre dominância entre heurísticas).

---

**29.** **(Pegadinha)** Em relação à complexidade de tempo e espaço, é correto afirmar que, no pior caso, tanto a BFS quanto a DFS em um espaço de estados com fator de ramificação *b* e profundidade máxima *m* (ou *d*, no caso da BFS) têm complexidade de tempo:

a) Sempre polinomial, jamais exponencial, independentemente de b e d
b) Tipicamente exponencial em relação à profundidade da solução (ordem de b^d ou b^m), o que torna ambas impraticáveis para espaços de estados muito profundos ou com alto fator de ramificação, mesmo diferindo bastante em complexidade de espaço
c) Sempre idêntica em espaço e tempo, sem qualquer diferença prática entre as duas
d) Independente do fator de ramificação b

> **Gabarito: b.** Pegadinha: embora a DFS use muito menos memória que a BFS, ambas compartilham, no pior caso, complexidade de tempo exponencial em relação à profundidade — a diferença essencial entre elas está na complexidade de **espaço**, não de tempo.

---

**30.** **(Pegadinha)** Um estudante afirma: "Buscas informadas são sempre melhores que buscas sem informação, então nunca faz sentido usar BFS, DFS ou custo uniforme na prática." Essa afirmação está:

a) Correta, pois heurísticas sempre reduzem o número de nós expandidos em qualquer problema
b) Incorreta — buscas informadas dependem da existência de uma heurística útil e computável para o problema em questão; em muitos problemas não há uma heurística natural disponível, ou seu cálculo é caro, e buscas sem informação continuam sendo ferramentas relevantes e, em certos contextos (como custos de passo uniformes e a necessidade de garantias simples), até preferíveis pela simplicidade
c) Correta, pois toda heurística admissível é trivial de se obter em qualquer problema
d) Incorreta, mas apenas porque BFS é sempre mais rápida que A* em qualquer situação

> **Gabarito: b.** Pegadinha final: a superioridade de buscas informadas depende crucialmente da disponibilidade de uma boa heurística — quando ela não existe, é cara de calcular ou é pouco informativa, buscas sem informação continuam sendo escolhas legítimas e, por vezes, mais simples e previsíveis.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Os pontos mais recorrentes de pegadinha nesta prova foram: **admissibilidade vs. consistência de heurísticas** (questões 13, 18 e 19), a **diferença entre busca gulosa e A\*** (questões 15 a 17), a **relação entre otimalidade e eficiência (número de nós expandidos)** (questões 21 e 28), e a **confusão entre complexidade de tempo e de espaço** na comparação BFS vs. DFS (questões 6 e 29) — vale reforçar esses pontos na correção em sala.
