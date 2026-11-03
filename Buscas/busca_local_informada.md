# Busca Local Informada em Inteligência Artificial

Uma **busca local informada** é uma estratégia de resolução de problemas em Inteligência Artificial onde o algoritmo utiliza conhecimento específico do domínio (geralmente uma **função heurística**) para guiar a exploração do espaço de estados, buscando encontrar a melhor solução de forma mais eficiente do que uma busca cega.

Diferente de algoritmos como a Busca em Largura ou Profundidade, que exploram caminhos sem saber se estão se aproximando do objetivo, a busca local informada avalia e modifica os estados atuais com base em quão "perto" eles parecem estar da meta.

---

## 🧠 Principais Características

* **Foco no Estado Atual:** Mantém em memória apenas o estado atual (ou um conjunto muito pequeno de estados) e tenta melhorá-lo passo a passo, em vez de guardar caminhos completos.
* **Uso de Heurísticas:** Utiliza uma função $h(n)$ que estima o "custo" ou a "distância" do estado atual até o objetivo.
* **Eficiência de Memória:** Como não guardam a árvore de busca inteira, esses algoritmos são ideais para problemas com espaços de estados gigantescos ou infinitos (ex: otimização de rotas, alocação de recursos). Assim, o algoritmo geralmente mantém em memória apenas o estado atual (e não uma árvore de caminhos explorados), o consumo de espaço é mínimo (muitas vezes constante).
* **Foco no resultado:** O caminho percorrido até a solução é irrelevante; o que importa é a qualidade do estado final.
* **Ótimos locais:** Eles podem ficar presos em ótimos locais (pontos que são melhores que seus vizinhos diretos, mas piores que o ótimo global do problema).

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

---

# Algoritmos de Busca Local e Otimização em Python

Este documento reúne explicações teóricas e implementações práticas em Python dos principais conceitos de busca local e inteligência artificial aplicados à otimização, utilizando o clássico **Problema das N-Rainhas** como base de teste.

---

## 1. Hill-Climbing (Subida de Encosta)

O **Hill-Climbing** funciona de forma gananciosa (*greedy*). Ele avalia os vizinhos imediatos do estado atual e move-se estritamente na direção que melhora a função objetivo. Ele para assim que todos os vizinhos ao redor forem piores do que o estado atual.

### Exemplo Base: Maximizar f(x) = -(x - 3)² + 10

```python
import random

def funcao_objetivo(x):
    return -(x - 3)**2 + 10

def obter_vizinhos(x, passo=0.1):
    return [x - passo, x + passo]

def hill_climbing(estado_inicial, max_iteracoes=100):
    estado_atual = estado_inicial
    valor_atual = funcao_objetivo(estado_atual)
    
    for i in range(max_iteracoes):
        vizinhos = obter_vizinhos(estado_atual)
        melhor_vizinho = max(vizinhos, key=funcao_objetivo)
        melhor_valor_vizinho = funcao_objetivo(melhor_vizinho)
        
        if melhor_valor_vizinho > valor_atual:
            estado_atual = melhor_vizinho
            valor_atual = melhor_valor_vizinho
        else:
            break
            
    return estado_atual, valor_atual

x_otimo, f_otimo = hill_climbing(estado_inicial=-5.0)
print(f"Hill-Climbing Simples -> x = {x_otimo:.4f} | f(x) = {f_otimo:.4f}")
```

---

## 2. Random Restart Hill-Climbing

Para contornar o problema dos **máximos locais** (picos secundários mais baixos que o ótimo global), o **Random Restart** executa o Hill-Climbing tradicional várias vezes, iniciando cada tentativa a partir de uma coordenada completamente aleatória.

### Exemplo Prático: Múltiplos Picos

```python
import random
import math

def funcao_com_multiplos_picos(x):
    return x * math.sin(5 * x) + 2

def obter_vizinhos_reinicio(x, passo=0.01):
    return [x - passo, x + passo]

def hill_climbing_simples(estado_inicial, max_iteracoes=200):
    estado_atual = estado_inicial
    valor_atual = funcao_com_multiplos_picos(estado_atual)
    
    for _ in range(max_iteracoes):
        vizinhos = obter_vizinhos_reinicio(estado_atual)
        melhor_vizinho = max(vizinhos, key=funcao_com_multiplos_picos)
        melhor_valor = funcao_com_multiplos_picos(melhor_vizinho)
        
        if melhor_valor > valor_atual:
            estado_atual = melhor_vizinho
            valor_atual = melhor_valor
        else:
            break
    return estado_atual, valor_atual

def random_restart_hill_climbing(num_reinicios=5):
    melhor_global_x = None
    melhor_global_valor = float('-inf')
    
    for i in range(num_reinicios):
        estado_inicial = random.uniform(0, 5)
        x_encontrado, valor_encontrado = hill_climbing_simples(estado_inicial)
        
        if valor_encontrado > melhor_global_valor:
            melhor_global_valor = valor_encontrado
            melhor_global_x = x_encontrado
            
    return melhor_global_x, melhor_global_valor

x_final, valor_final = random_restart_hill_climbing()
print(f"Random Restart -> Ótimo Global em x = {x_final:.4f} com f(x) = {valor_final:.4f}")
```

---

## 3. Problema das N-Rainhas com Simulated Annealing (Têmpera Simulada)

O **Simulated Annealing** simula o resfriamento de metais. No início (alta temperatura), ele aceita movimentos que aumentam o erro (movimentos ruins) para escapar de armadilhas locais. À medida que o sistema esfria, ele se torna rigoroso e foca apenas em refinar o resultado.

```python
import random
import math

def calcular_ataques(tabuleiro):
    ataques = 0
    n = len(tabuleiro)
    for i in range(n):
        for j in range(i + 1, n):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                ataques += 1
    return ataques

def obter_vizinho_aleatorio(tabuleiro):
    n = len(tabuleiro)
    vizinho = list(tabuleiro)
    coluna = random.randint(0, n - 1)
    nova_linha = random.randint(0, n - 1)
    while nova_linha == tabuleiro[coluna]:
        nova_linha = random.randint(0, n - 1)
    vizinho[coluna] = nova_linha
    return vizinho

def simulated_annealing_rainhas(n=8, temp_inicial=100.0, taxa_resfriamento=0.995, temp_final=0.001):
    tabuleiro_atual = [random.randint(0, n - 1) for _ in range(n)]
    ataques_atuais = calcular_ataques(tabuleiro_atual)
    T = temp_inicial
    
    while T > temp_final and ataques_atuais > 0:
        vizinho = obter_vizinho_aleatorio(tabuleiro_atual)
        ataques_vizinho = calcular_ataques(vizinho)
        delta_E = ataques_vizinho - ataques_atuais
        
        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            tabuleiro_atual = vizinho
            ataques_atuais = ataques_vizinho
            
        T *= taxa_resfriamento
        
    return tabuleiro_atual, ataques_atuais

solucao_sa, ataques_sa = simulated_annealing_rainhas(n=8)
print(f"Simulated Annealing -> Tabuleiro: {solucao_sa} com {ataques_sa} ataques.")
```

---

## 4. Problema das N-Rainhas com Algoritmos Genéticos

Os **Algoritmos Genéticos** utilizam conceitos de seleção natural e evolução biológica. Uma população de soluções compete entre si; os melhores tabuleiros cruzam suas características (Crossover) e passam por mutações genéticas ocasionais para gerar novas e melhores soluções.

```python
import random

def calcular_ataques_ag(tabuleiro):
    ataques = 0
    n = len(tabuleiro)
    for i in range(n):
        for j in range(i + 1, n):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                ataques += 1
    return ataques

def funcao_aptidao(tabuleiro):
    n = len(tabuleiro)
    max_ataques = (n * (n - 1)) // 2
    return max_ataques - calcular_ataques_ag(tabuleiro)

def criar_individuo(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def selecao_roleta(populacao, aptidoes):
    soma_aptidoes = sum(aptidoes)
    if soma_aptidoes == 0:
        return random.choice(populacao)
    ponto_sorteio = random.uniform(0, soma_aptidoes)
    acumulado = 0
    for individuo, aptidao in zip(populacao, aptidoes):
        acumulado += aptidao
        if acumulado >= ponto_sorteio:
            return individuo
    return populacao[-1]

def cruzamento(pai, mae):
    n = len(pai)
    ponto_corte = random.randint(1, n - 2)
    filho1 = pai[:ponto_corte] + mae[ponto_corte:]
    filho2 = mae[:ponto_corte] + pai[ponto_corte:]
    return child1, child2 if 'child2' in locals() else filho2
    # Ajustado abaixo para evitar erros de sintaxe locais:
    return filho1, filho2

def mutacao(tabuleiro, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        n = len(tabuleiro)
        coluna = random.randint(0, n - 1)
        nova_linha = random.randint(0, n - 1)
        tabuleiro[coluna] = nova_linha
    return tabuleiro

def algoritmo_genetico_rainhas(n=8, tam_populacao=100, max_geracoes=1000, taxa_mutacao=0.1):
    populacao = [criar_individuo(n) for _ in range(tam_populacao)]
    aptidao_maxima_alvo = (n * (n - 1)) // 2
    
    for geracao in range(max_geracoes):
        aptidoes = [funcao_aptidao(ind) for ind in populacao]
        if aptidao_maxima_alvo in aptidoes:
            return populacao[aptidoes.index(aptidao_maxima_alvo)]
            
        nova_populacao = []
        while len(nova_populacao) < tam_populacao:
            pai = selecao_roleta(populacao, aptidoes)
            mae = selecao_roleta(populacao, aptidoes)
            filho1, filho2 = cruzamento(pai, mae)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            if len(nova_populacao) < tam_populacao:
                nova_populacao.append(mutacao(filho2, taxa_mutacao))
        populacao = nova_populacao
    return populacao[aptidoes.index(max(aptidoes))]

solucao_ag = algoritmo_genetico_rainhas(n=8)
print(f"Algoritmo Genético -> Melhor Tabuleiro Encontrado: {solucao_ag}")
```

---

## ⚖️ Tabela de Comparação dos Algoritmos

| Característica | Hill-Climbing | Random Restart | Simulated Annealing | Algoritmo Genético |
| :--- | :--- | :--- | :--- | :--- |
| **Abordagem** | Solução única | Soluções independentes | Solução única com variação | População em evolução |
| **Uso de Memória** | Mínimo | Baixo | Mínimo | Médio/Alto |
| **Escapa de Ótimos Locais?** | Não | Sim | Sim | Sim |
| **Complexidade de Ajuste** | Muito Baixa | Baixa | Média (Taxas e Temp) | Alta (Múltiplos parâmetros) |
