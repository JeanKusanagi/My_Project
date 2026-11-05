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
*Compilado para fins educacionais e de referência técnica sobre Teoria dos Grafos e Inteligência Artificial.*
