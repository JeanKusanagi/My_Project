# O Algoritmo de Busca A* (A-Estrela)

O **Algoritmo A*** é um método de **busca informada (heurística)** em grafos e matrizes, amplamente utilizado para encontrar o caminho mais curto entre um vértice inicial e um destino final. Ele combina a eficiência da Busca Gulosa com a precisão e otimalidade do Algoritmo de Dijkstra.

---

## 🔬 Como Funciona?

O A* avalia os nós à sua disposição combinando o custo real acumulado com uma estimativa do custo restante. A função de avaliação fundamental é dada por:

f(n) = g(n) + h(n)

* **g(n)**: Custo real do caminho já percorrido do início até o nó atual n.
* **h(n)**: Estimativa heurística do custo para ir do nó n até o destino final.
* **f(n)**: Custo total estimado do caminho mais barato que passa pelo nó n.

---

## 📐 Admissibilidade da Heurística

Uma heurística é considerada **admissível** se ela **nunca superestima o custo real** para atingir o objetivo. Ela deve ser sempre otimista ou, no limite, exata.

### A Regra de Ouro
h(n) <= h*(n)
*(Onde h*(n) é o custo real mínimo e verdadeiro até o destino).*

### Exemplos no Mundo Real
1. **Distância em Linha Reta:** Em mapas de trânsito ou ruas, a distância em linha reta (voo de pássaro) é sempre admissível. O caminho real por terra, cheio de curvas e quarteirões, sempre será igual ou maior do que a reta perfeita.
2. **Distância de Manhattan:** Em malhas ortogonais (onde só se move em 4 direções), calcular a soma das diferenças absolutas de x e y assumindo zero obstáculos é admissível.

> Se a heurística NÃO for admissível, o algoritmo perde a garantia de otimalidade. Ele pode superestimar uma rota excelente, ignorá-la e entregar um caminho final mais longo e ineficiente.

---

## ⚡ Consistência (Monotonicidade)

A **consistência** é uma propriedade ainda mais forte que a admissibilidade. Uma heurística é consistente se, para cada nó n e cada vizinho p de n, a estimativa para o destino respeitar a desigualdade triangular:

h(n) <= c(n, p) + h(p)

* **c(n, p)**: Custo real de dar um único passo de n até p.

### Impacto Prático: Admissível vs. Consistente
* **Apenas Admissível:** Garante o caminho mais curto no final, mas o algoritmo pode fechar um nó e, mais tarde, achar um atalho melhor para ele. Isso exige reabrir o nó e reavaliar seus descendentes (retrabalho).
* **Consistente:** Quando o A* expande e fecha um nó, o custo g(n) associado a ele já é **com certeza absoluta o menor da história**. Nunca há necessidade de reabrir nós na lista fechada.

---

## 🧱 Resolução em Grids 2D e Labirintos

Em matrizes ou labirintos planos, o A* mapeia células livres como nós transitáveis e paredes como nós bloqueados.

### Principais Heurísticas para Grids
* **Manhattan (4 direções - Cima/Baixo/Esq/Dir):** h = |x1 - x2| + |y1 - y2|
* **Chebyshev (8 direções - Inclui diagonais com custo 1):** h = max(|x1 - x2|, |y1 - y2|)
* **Euclidiana (Qualquer ângulo - Reta geométrica):** h = sqrt((x1 - x2)^2 + (y1 - y2)^2)

---

## 💻 Implementação Prática em Python

Abaixo está o código completo para um resolvedor de labirinto em grade quadrada utilizando Fila de Prioridades (`heapq`) e a distância de Manhattan.

```python
import heapq

def heuristica_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_estrela_grid(grid, inicio, fim):
    linhas, colunas = len(grid), len(grid[0])
    
    lista_aberta = []
    heapq.heappush(lista_aberta, (0, inicio))
    
    caminho_pai = {}
    g_score = {inicio: 0}
    f_score = {inicio: heuristica_manhattan(inicio, fim)}
    
    lista_fechada = set()
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while lista_aberta:
        atual_f, atual = heapq.heappop(lista_aberta)

        if atual == fim:
            caminho = []
            while atual in caminho_pai:
                caminho.append(atual)
                atual = caminho_pai[atual]
            caminho.append(inicio)
            return caminho[::-1]

        lista_fechada.add(atual)

        for dx, dy in movimentos:
            vizinho = (atual[0] + dx, atual[1] + dy)
            
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if grid[vizinho[0]][vizinho[1]] == 1 or vizinho in lista_fechada:
                    continue
                
                g_tentativo = g_score[atual] + 1
                
                if g_tentativo < g_score.get(vizinho, float('inf')):
                    caminho_pai[vizinho] = atual
                    g_score[vizinho] = g_tentativo
                    f_score[vizinho] = g_tentativo + heuristica_manhattan(vizinho, fim)
                    
                    if vizinho not in [item[1] for item in lista_aberta]:
                        heapq.heappush(lista_aberta, (f_score[vizinho], vizinho))
                        
    return None

# --- MAPA DE TESTE ---
# 0 = Caminho livre, 1 = Parede/Obstáculo
labirinto = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
fim = (4, 4)

resultado = a_estrela_grid(labirinto, inicio, fim)
print("Caminho encontrado pelo A*:", resultado)
```

---

# Exemplo de busca A* (A-Star)

O algoritmo **A\*** é um algoritmo de busca informada utilizado para encontrar o caminho de menor custo entre um estado inicial e um estado objetivo. Ele combina o custo já percorrido com uma estimativa do custo restante até o objetivo.

Sua função de avaliação é:

\[
\boxed{f(n)=g(n)+h(n)}
\]

Em que:

- \(f(n)\): custo total estimado do caminho passando pelo nó \(n\).
- \(g(n)\): custo real acumulado do nó inicial até \(n\).
- \(h(n)\): estimativa heurística do custo de \(n\) até o objetivo.

## 1. Definição do problema

Considere o seguinte grafo, no qual desejamos encontrar o caminho de menor custo entre os nós **A (inicial)** e **G (objetivo)**.

Os valores nas arestas representam os custos de deslocamento, enquanto os valores entre parênteses representam as heurísticas \(h(n)\).

### Conexões do grafo

| Origem | Destino | Custo |
|---|---|---:|
| A | B | 2 |
| A | C | 4 |
| B | D | 7 |
| B | E | 3 |
| C | F | 3 |
| D | G | 2 |
| E | G | 5 |
| F | G | 2 |

Valores heurísticos:

| Nó | \(h(n)\) |
|---|---:|
| A | 7 |
| B | 6 |
| C | 4 |
| D | 2 |
| E | 4 |
| F | 2 |
| G | 0 |

## 2. Execução passo a passo

O algoritmo começa no nó A.

### Passo 1: Expandir A

Como estamos no nó inicial:

\[
g(A)=0
\]

\[
f(A)=g(A)+h(A)=0+7=7
\]

Expandimos A e encontramos dois sucessores: B e C.

Para B:

\[
g(B)=0+2=2
\]

\[
f(B)=2+6=8
\]

Para C:

\[
g(C)=0+4=4
\]

\[
f(C)=4+4=8
\]

Lista de nós disponíveis (OPEN):

| Nó | \(g(n)\) | \(h(n)\) | \(f(n)\) |
|---|---:|---:|---:|
| B | 2 | 6 | 8 |
| C | 4 | 4 | 8 |

Os dois possuem o mesmo valor de \(f(n)\). Para este exemplo, em caso de empate, escolhemos o nó com menor \(h(n)\).

Portanto, selecionamos C.

### Passo 2: Expandir C

Expandimos C e encontramos F.

O custo acumulado até F é:

\[
g(F)=g(C)+c(C,F)
\]

\[
g(F)=4+3=7
\]

Calculamos:

\[
f(F)=7+2=9
\]

Lista OPEN:

| Nó | \(g(n)\) | \(h(n)\) | \(f(n)\) |
|---|---:|---:|---:|
| B | 2 | 6 | 8 |
| F | 7 | 2 | 9 |

Selecionamos B, pois possui o menor valor de \(f(n)\).

### Passo 3: Expandir B

Expandimos B e encontramos D e E.

Para D:

\[
g(D)=2+7=9
\]

\[
f(D)=9+2=11
\]

Para E:

\[
g(E)=2+3=5
\]

\[
f(E)=5+4=9
\]

Lista OPEN:

| Nó | \(g(n)\) | \(h(n)\) | \(f(n)\) |
|---|---:|---:|---:|
| F | 7 | 2 | 9 |
| E | 5 | 4 | 9 |
| D | 9 | 2 | 11 |

Temos um empate entre F e E. Novamente, escolhemos o nó com menor heurística.

Selecionamos F.

### Passo 4: Expandir F

Expandimos F e encontramos G.

\[
g(G)=g(F)+c(F,G)
\]

\[
g(G)=7+2=9
\]

Como G é o objetivo:

\[
f(G)=9+0=9
\]

Lista OPEN:

| Nó | \(g(n)\) | \(h(n)\) | \(f(n)\) |
|---|---:|---:|---:|
| E | 5 | 4 | 9 |
| G | 9 | 0 | 9 |
| D | 9 | 2 | 11 |

**Importante:** para garantir a solução ótima, não basta encerrar ao gerar G. O algoritmo deve encerrar quando G for removido da lista OPEN para expansão, isto é, quando for selecionado como o nó de menor \(f\). Neste exemplo, G e E empatam em \(f=9\). Se o desempate selecionar G, podemos encerrar: o caminho por E custaria \(5+5=10\), portanto não é melhor.

## 3. Resultado final

O caminho de menor custo encontrado é:

\[
\boxed{A \rightarrow C \rightarrow F \rightarrow G}
\]

Custo total:

\[
C(A,C,F,G)=4+3+2
\]

\[
\boxed{C=9}
\]

## 4. Resumo da execução

| Iteração | Nó expandido | Nós gerados | Próximo nó |
|---|---|---|---|
| 1 | A | B, C | C |
| 2 | C | F | B |
| 3 | B | D, E | F |
| 4 | F | G | G ou E (empate em \(f=9\)) |

A ordem exata dos nós selecionados em caso de empate depende da regra de desempate adotada. O resultado ótimo permanece o mesmo.

## 5. Propriedades do algoritmo A*

**Completude:** encontra uma solução se existir, desde que as condições necessárias sejam satisfeitas, como fator de ramificação finito e custos positivos limitados inferiormente por uma constante positiva.

**Otimalidade:** encontra uma solução de custo mínimo quando utiliza uma heurística admissível. Na busca em grafo sem reabertura de nós, exige-se uma heurística consistente.

**Heurística admissível:** nunca superestima o custo real restante até o objetivo:

\[
h(n)\leq h^*(n)
\]

Em que \(h^*(n)\) representa o custo real mínimo até o objetivo.

**Complexidade:** no pior caso, tanto o tempo quanto o espaço podem crescer exponencialmente com a profundidade da solução.

## 6. Diferença entre busca gulosa e A*

| Característica | Busca Gulosa | Busca A* |
|---|---|---|
| Função de avaliação | \(f(n)=h(n)\) | \(f(n)=g(n)+h(n)\) |
| Considera custo percorrido? | Não | Sim |
| Utiliza heurística? | Sim | Sim |
| Garante solução ótima? | Não, em geral | Sim, sob condições adequadas |
| Memória | Pode ser elevada | Pode ser elevada |

**Conclusão:** a principal vantagem do A* é combinar o custo real percorrido com uma estimativa do custo restante. Dessa forma, consegue direcionar a busca ao objetivo sem ignorar os custos já acumulados, encontrando soluções ótimas quando as condições da heurística são respeitadas.

---

*Compilado para fins educacionais e de referência técnica sobre Teoria dos Grafos e Inteligência Artificial.*
