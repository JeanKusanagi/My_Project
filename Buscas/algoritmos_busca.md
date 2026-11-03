# Guia Completo: Algoritmos de Busca em Inteligência Artificial
> Da Teoria Clássica e Algoritmos Cegos ao Estado da Arte com Redes Neurais Profundas.

No campo da Inteligência Artificial e da Ciência da Computação, os algoritmos de busca dividem-se fundamentalmente em dois grandes grupos: os algoritmos de **busca sem informação** (também chamados de busca cega ou desinformada) e os algoritmos de **busca com informação** (comumente referidos como busca informada ou busca heurística).

---

## 1. Classificação dos Algoritmos Clássicos

### Busca Sem Informação (Cega)
Estes algoritmos não possuem nenhum conhecimento específico sobre o domínio do problema além da própria definição do mapa de estados (sabem apenas gerar sucessores e identificar se o estado atual é o objetivo).

*   **Busca em Largura (BFS - Breadth-First Search):** Explora o espaço de estados nível por nível, de forma horizontal. Utiliza uma estrutura de **Fila (FIFO - Primeiro a entrar, primeiro a sair)**.
*   **Busca em Profundidade (DFS - Depth-First Search):** Explora o caminho mais longo de cada ramo até o fim antes de retroceder (*backtracking*). Utiliza uma estrutura de **Pilha (LIFO - Último a entrar, primeiro a sair)** ou recursão.
*   **Busca de Custo Uniforme (UCS - Uniform-Cost Search):** Funciona de forma similar à BFS, mas expande sempre o nó com o menor custo acumulado do caminho $g(n)$. Utiliza uma **Fila de Prioridade**.

### Busca Com Informação (Heurística)
Utilizam conhecimento do domínio através de uma **função heurística $h(n)$**, que estima o custo do nó atual até o objetivo final para guiar a busca de forma mais inteligente e eficiente.

*   **Busca Gulosa (Greedy Best-First Search):** Expande o nó que aparenta estar mais próximo do objetivo com base exclusivamente na estimativa da heurística: $f(n) = h(n)$.
*   **Busca A\* (A-Estrela):** Avalia os nós somando o custo já pago com a estimativa futura do caminho para o objetivo: $f(n) = g(n) + h(n)$.

### Tabela Comparativa Resumida

Abaixo, os algoritmos clássicos estão sintetizados considerando as seguintes variáveis de análise:
*   $b$: fator de ramificação (número médio de sucessores por nó).
*   $d$: profundidade da solução mais rasa.
*   $m$: profundidade máxima do espaço de estados.
*   $C^*$: custo da solução ótima.
*   $\epsilon$: custo mínimo de um passo individual.

| Tipo de Busca | Algoritmo | Complexidade de Tempo | Complexidade de Espaço | Completo? | Ótimo? | Vantagens | Principais Desvantagens |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sem Informação** | **Largura (BFS)** | $O(b^d)$ | $O(b^d)$ | Sim | Sim (se custos iguais) | Encontra o caminho mais raso; nunca fica presa. | Uso massivo de memória RAM. |
| **Sem Informação** | **Profundidade (DFS)** | $O(b^m)$ | $O(b \cdot m)$ | Não | Não | Baixo consumo de memória em caminhos finitos. | Pode ficar presa em caminhos infinitos/loops. |
| **Sem Informação** | **Custo Uniforme (UCS) Ponderado** | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | Sim | Sim | Ótima para qualquer custo de passo positivo. | Explora muitos caminhos desnecessários de baixo custo. |
| **Com Informação** | **Gulosa (Greedy)** | $O(b^m)$ | $O(b^m)$ | Não | Não | Muito rápida para cenários comuns e diretos. | Pode tomar caminhos errados por ser míope. |
| **Com Informação** | **A\* (A-Estrela)** | $O(b^d)$ | $O(b^d)$ | Sim | Sim | Melhor eficiência teórica (se heurística correta). | Mantém todos os nós gerados na memória RAM. |

---

## 2. Detalhemento de Funcionamento Passo a Passo

### Cenário de Exemplo
**Objetivo:** Encontrar a rota ideal para ir da **Cidade A** até a **Cidade Final (F)**.

*   **Caminhos e custos reais de viagem $g(n)$:**
    *   A → B (custo: 2) | A → C (custo: 5)
    *   B → D (custo: 4) | B → E (custo: 2)
    *   C → F (custo: 6)
    *   E → F (custo: 3)
*   **Heurísticas $h(n)$ (distância estimada em linha reta até F):**
    *   h(A) = 6 | h(B) = 5 | h(C) = 4 | h(D) = 6 | h(E) = 2 | h(F) = 0

### Execução na Busca de Custo Uniforme (UCS)
A UCS escolhe sempre o nó com o menor custo acumulado do passado:
1.  **Passo 1:** Inicia em **A** ($g(A) = 0$). Fila de prioridade: `[(A, custo 0)]`. Expande A para B (custo 2) e C (custo 5).
2.  **Passo 2:** Fila ordenada: `[(B, custo 2), (C, custo 5)]`. Menor custo é B. Expande B para D ($2+4=6$) e E ($2+2=4$).
3.  **Passo 3:** Fila ordenada: `[(E, custo 4), (C, custo 5), (D, custo 6)]`. Menor custo é E. Expande E para F ($4+3=7$).
4.  **Passo 4:** Fila ordenada: `[(C, custo 5), (D, custo 6), (F, custo 7)]`. Menor custo é C. Expande C para F ($5+6=11$). Como já existe um caminho conhecido e melhor para F (custo 7), a rota via C é descartada.
5.  **Passo 5:** Fila ordenada: `[(D, custo 6), (F, custo 7)]`. Expande D (não gera novos nós úteis).
6.  **Passo 6:** Próximo da fila é **F** (custo 7). Como F é o objetivo e alcançou o topo da fila, a busca encerra.
    *   **Caminho final:** A → B → E → F com custo real total **7**.

### Execução na Busca A\* (A-Estrela)
O A\* equilibra passado e futuro através da avaliação de $f(n) = g(n) + h(n)$:
1.  **Passo 1:** Inicia em **A** ($f = 0 + 6 = 6$). Fila: `[(A, f=6)]`. Expande A calculando o $f$ dos vizinhos:
    *   B: $g(B)=2, h(B)=5 \implies f(B) = 2 + 5 = 7$
    *   C: $g(C)=5, h(C)=4 \implies f(C) = 5 + 4 = 9$
2.  **Passo 2:** Fila ordenada por $f$: `[(B, f=7), (C, f=9)]`. O menor é B. Expande B:
    *   D: $g(D)=2+4=6, h(D)=6 \implies f(D) = 6 + 6 = 12$
    *   E: $g(E)=2+2=4, h(E)=2 \implies f(E) = 4 + 2 = 6$
3.  **Passo 3:** Fila ordenada por $f$: `[(E, f=6), (C, f=9), (D, f=12)]`. O menor é E. Expande E:
    *   F: $g(F)=4+3=7, h(F)=0 \implies f(F) = 7 + 0 = 7$
4.  **Passo 4:** Fila ordenada por $f$: `[(F, f=7), (C, f=9), (D, f=12)]`. O menor da fila é **F** ($f=7$). Como o objetivo chegou ao topo da fila de prioridades, a busca encerra imediatamente.
    *   **Caminho final:** A → B → E → F com custo real total **7**.
    *   *Nota de Eficiência:* O A\* evitou expandir desnecessariamente os nós C e D, poupando processamento em relação à UCS graças ao direcionamento da heurística.

---

## 3. Propriedades Matemáticas das Heurísticas

Para que o algoritmo A\* garanta a descoberta da rota matematicamente ótima, a heurística $h(n)$ deve respeitar duas propriedades fundamentais:

### Heurística Admissível
Uma heurística é **admissível** se ela **nunca superestima o custo real** para atingir o objetivo a partir de qualquer nó. Ela deve ser sempre otimista ou perfeitamente realista.
$$h(n) \le h^*(n)$$
*(Onde $h^*(n)$ é o custo real mínimo do nó $n$ até o objetivo).*

### Heurística Consistente (Monotônica)
Uma heurística é **consistente** se, ao passar de um nó $n$ para um nó vizinho $n'$ por meio de uma ação, a estimativa para chegar ao objetivo não diminuir mais do que o custo real do passo dado. Ela respeita a desigualdade triangular.
$$h(n) \le c(n, a, n') + h(n')$$
*(Onde $c(n, a, n')$ é o custo real para ir do nó $n$ até o seu vizinho $n'$).*

### Contraexemplo: Admissível, mas NÃO Consistente
Considere os custos reais: $A \to B = 2$ e $B \to F = 4$ (Custo real total de A até F é 6).
Se definirmos as estimativas da heurística como:
*   $h(A) = 5$ (Admissível, pois $5 \le 6$)
*   $h(B) = 1$ (Admissível, pois $1 \le 4$)

Testando a consistência ao avançar de A para B:
$$h(A) \le c(A \to B) + h(B)$$
$$5 \le 2 + 1 \implies 5 \le 3 \quad (\mathbf{Falso!})$$

**Consequência Prática:** A estimativa caiu bruscamente (uma diferença de 4 unidades), enquanto o custo real cobrado pelo passo foi de apenas 2 unidades. No cálculo do A\*, teríamos $f(A) = 0 + 5 = 5$ e $f(B) = 2 + 1 = 3$. O valor de $f(n)$ diminuir ao avançar quebra a eficiência do algoritmo, forçando o A\* a reabrir nós na memória e reprocessar subcaminhos já visitados, atrasando a execução.

---

## 4. O Impacto de Loops Infinitos (Ciclos)

Considere o seguinte grafo cíclico, onde o objetivo final do sistema é encontrar a sala **D**:
```text
    A ───> B ───> D (Objetivo)
    ▲      │
    │      ▼
    └──────C
```

### Comportamento da Busca em Profundidade (DFS)
*   **Sem controle de visitados (Implementação Ingênua):** Como a DFS prioriza caminhos profundos imediatamente, ela entra em uma sequência infinita eterna: $A \to B \to C \to A \to B \to C \dots$ Ela nunca avaliará o ramo D e gerará um estouro de memória (*Stack Overflow*).
*   **Com controle de visitados (Implementação Correta):** O algoritmo utiliza uma estrutura de dados de conjunto (`visited = {A, B, C}`). Ao tentar retornar a **A** a partir de **C**, ela detecta o loop, aborta o caminho por *backtracking* e limpa a pilha para processar o nó **D** com sucesso.

### Comportamento da Busca em Largura (BFS)
*   **Naturalmente protegida contra loops:** Por explorar em camadas horizontais, a BFS coloca o nó **D** em sua fila na mesma rodada em que o ciclo é completado. Como consequência, ela encontra o objetivo e encerra a execução antes que o ciclo cause problemas.
*   **Importância do controle de visitados na BFS:** Se o objetivo **D** *não existisse* no mapa, a BFS sem controle continuaria gerando expansões duplicadas do loop indefinidamente dentro da fila, acumulando dados até esgotar toda a memória RAM disponível no computador.

---

## 5. Estado da Arte: Busca Guiada por Redes Neurais

Em problemas modernos de altíssima complexidade (como jogos de tabuleiro avançados, quebra-cabeças massivos ou planejamento de IA generativa de raciocínio), projetar heurísticas manuais é inviável. Sistemas modernos utilizam redes neurais para automatizar esse processo.

### 1. Heurísticas Aprendidas via Aprendizado Supervisionado
Redes neurais profundas são treinadas como aproximadoras de funções. Elas recebem o estado atual do problema como entrada (por exemplo, a imagem de um tabuleiro) e fazem uma predição rápida (*forward pass*) para estimar o valor de $h(n)$, substituindo fórmulas geométricas ou matemáticas tradicionais.

### 2. DeepCubeA
Esta arquitetura combina o algoritmo de busca clássico $A^*$ com Aprendizado por Reforço Profundo. Ela foi projetada para resolver problemas de caminhos complexos, como o Cubo de Rubik. O DeepCubeA aprende a heurística simulando embaralhamentos em sentido reverso, conseguindo encontrar rotas ótimas explorando apenas uma fração minúscula de todos os trilhões de estados possíveis do cubo.

### 3. AlphaZero (MCTS + Redes Neurais)
A arquitetura criada pela Google DeepMind revolucionou problemas de busca ao fundir a Busca em Árvore Monte Carlo (MCTS) com redes neurais que desempenham dois papéis fundamentais:
*   **Rede de Políticas (Policy Network):** Avalia as ações disponíveis e filtra quais caminhos são promissores. Isso impede que a árvore expanda ramos absurdos ou inválidos, realizando uma poda inteligente.
*   **Rede de Valor (Value Network):** Atua como a **função heurística automática**. Ela avalia um estado da simulação e fornece uma nota probabilística de vitória. Isso elimina a necessidade de simular o jogo exaustivamente até o final para saber se a jogada foi boa.

```text
    [Estado Atual] ──> Rede de Políticas ──> Filtra os melhores caminhos
                            │
                            ▼
                     MCTS (Simulações)
                            │
                            ▼
                      Rede de Valor ───> Substitui a heurística (Dá a nota)
```

### 4. Tree of Thoughts (ToT) em Grandes Modelos de Linguagem
Modelos de inteligência artificial focados em raciocínio lógico avançado (como a linha OpenAI o1) não geram textos de forma puramente linear. Eles implementam buscas estruturadas em árvores de pensamentos.

O modelo gera múltiplos ramos de hipóteses de solução de forma assíncrona. Uma rede neural avaliadora interna julga a qualidade lógica de cada ramificação. Se um erro matemático ou contradição for detectado, o sistema aplica o conceito clássico de *backtracking* da DFS, abandonando o ramo e tentando outra linha de pensamento antes de exibir a resposta final ao usuário.






## 6. # Exemplo de Falha na Busca Gulosa (Greedy Best-First Search)

A **Busca Gulosa** escolhe o próximo passo baseando-se *apenas* na estimativa heurística até o objetivo ($h(n)$), ignorando o custo do caminho já percorrido ($g(n)$). Isso faz com que ela seja míope e suscetível a ficar presa em loops ou becos sem saída.

---

### Exemplo 1: O Labirinto com Parede Côncava (Beco sem Saída)

Imagine um agente em uma grade 2D tentando chegar ao objetivo usando a **Distância de Manhattan** como heurística.

```text
Linha 4: [   ] [   ] [   ] [   ] [   ]
Linha 3: [--- Parede Barreira --] [   ]  <-- Bloqueio
Linha 2: [   ] [ A ] [   ] [   ] [ O ]  <-- A (Início) e O (Objetivo)
Linha 1: [   ] [   ] [   ] [   ] [   ]
          Col 1  Col 2  Col 3  Col 4  Col 5
```

### O Comportamento do Algoritmo:
1. **Movimento Inicial:** No ponto **A (2,2)**, o objetivo está à direita. O algoritmo se move sequencialmente para a direita até a coordenada **(2,4)** porque a distância heurística diminui a cada passo.
2. **O Bloqueio:** Em **(2,4)**, o caminho direto está bloqueado pela parede. O algoritmo avalia os vizinhos e decide subir para **(3,4)**.
3. **O Loop:** Em **(3,4)**, ele colide com o recuo do obstáculo. Se o algoritmo não mantiver um registro rígido de nós visitados, ele olhará para baixo **(2,4)**, verá que a heurística lá é numericamente melhor (mais perto do objetivo em linha reta) e **voltará para trás**.
4. **Resultado:** O agente fica preso oscilando infinitamente entre os mesmos estados.

---

### Exemplo 2: O Mapa com Heurística Enganosa (Loop de Cidades)

Considere um cenário simplificado de navegação entre cidades onde o objetivo final é chegar a **Făgăraș**. O algoritmo utiliza a distância em linha reta até o destino final como função heurística ($h$).

```text
       [Neamț] (h = 234)
        /
   [Iași] (h = 226) 
        [Vaslui] (h = 199)
```

### O Comportamento do Algoritmo:
1. **Decisão Gulosa:** Estando em **Iași**, o algoritmo avalia os vizinhos disponíveis: **Neamț** ($h=234$) e **Vaslui** ($h=199$).
2. **A Escolha:** Como $199 < 234$, a busca gulosa assume que **Vaslui** é o melhor caminho e se move para lá.
3. **O Problema:** Na estrutura real do mapa, **Vaslui** é um beco sem saída para este trajeto. A única conexão viável a partir de lá é retornar para **Iași**.
4. **Resultado:** Ao voltar para **Iași**, o algoritmo repete a mesma análise e escolhe **Vaslui** novamente, entrando em um **loop infinito** (Iași $\leftrightarrow$ Vaslui).

---

### Como Solucionar Este Problema?

* **Busca em Grafo (Graph Search):** Implementar uma lista de estados fechados (nós já visitados) para impedir que o algoritmo retorne a um estado anterior, embora isso ainda possa gerar caminhos muito mais longos e ineficientes.
* **Algoritmo A\*:** A solução ideal. O A\* combina a heurística com o custo real do caminho acumulado ($f(n) = g(n) + h(n)$). Se o algoritmo começar a andar em círculos ou entrar em um beco sem saída, o custo $g(n)$ aumenta drasticamente, forçando-o a explorar caminhos alternativos mais viáveis.
