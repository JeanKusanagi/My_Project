# O Guia Definitivo sobre Monte Carlo Tree Search (MCTS)
Este guia consolida todo o conhecimento abordado sobre o algoritmo **MCTS**, desde os fundamentos clássicos até as implementações modernas de Deep Learning, jogos de informação oculta e exemplos práticos em Python.

---

## 1. O que é o MCTS?
O **MCTS** (**Monte Carlo Tree Search**) é um algoritmo heurístico de busca em árvore usado em inteligência artificial para tomada de decisão, planejamento e jogos. Ele combina a construção gradual de uma árvore de possibilidades com simulações de Monte Carlo (amostragem aleatória) para encontrar o melhor movimento sem precisar de uma função de avaliação complexa ou de conhecer toda a extensão do problema.

### As 4 Etapas do Algoritmo Clássico
Cada ciclo (ou rodada) de MCTS é composto por quatro passos sequenciais:
1. **Seleção (Selection):** A partir do nó raiz (estado atual), o algoritmo navega pela árvore descendo pelos nós já existentes. Ele utiliza uma fórmula matemática — geralmente a **UCT** (*Upper Confidence Bound applied to Trees*) — para equilibrar exploração (testar caminhos novos) e aproveitamento (seguir caminhos vitoriosos).
2. **Expansão (Expansion):** Quando chega a um nó que ainda não foi totalmente explorado, o algoritmo cria um ou mais nós filhos para representar novas ações possíveis.
3. **Simulação / Playout (Simulation):** A partir do novo nó, é feita uma simulação rápida (muitas vezes com jogadas aleatórias) até atingir um estado final (vitória, derrota ou empate).
4. **Retropropagação / Backup (Backpropagation):** O resultado da simulação é propagado de volta por todos os nós visitados naquele caminho, atualizando as estatísticas de vitórias e a contagem de visitas de cada um.

---

### O que é Monte Carlo?

O termo **Monte Carlo** refere-se principalmente a dois conceitos muito distintos: uma técnica matemática e computacional de simulação ou um distrito luxuoso no Principado de Mônaco.

---

#### 1. O Método de Monte Carlo (Simulação)

O **Método de Monte Carlo** é uma técnica estatística que utiliza **amostragem aleatória repetida** para computar resultados numéricos e estimar a probabilidade de eventos complexos ou incertos.

* **Como funciona:** Em problemas com muitas variáveis onde o cálculo exato é inviável, o computador executa milhares ou milhões de simulações. A cada execução, o algoritmo escolhe valores aleatórios baseados em uma distribuição de probabilidade predefinida. No final, consolida-se um leque de cenários possíveis e suas respectivas chances de ocorrência.
* **Origem do nome:** Foi criado nos anos 1940 pelos cientistas Stanislaw Ulam, John von Neumann e Nicholas Metropolis durante o Projeto Manhattan. O codinome foi inspirado no famoso **Cassino de Monte Carlo**, devido à dependência do método em eventos aleatórios e probabilidades (semelhante aos jogos de azar).
* **Aplicações Comuns:**
    * **Finanças:** Projeção de risco em investimentos, precificação de opções e simulação de carteiras de ações.
    * **Engenharia e Ciência:** Análise de confiabilidade de estruturas, meteorologia e simulações de física quântica.
    * **Gestão de Projetos:** Estimativa de prazos de entrega e custos orçamentários sob condições de incerteza.

---

## 2. Monte Carlo (Geografia)

**Monte Carlo** é um distrito (ou bairro administrativo) do **Principado de Mônaco**, uma cidade-estado localizada na Riviera Francesa.

* **Principais Características:**
    * **Glamour:** É mundialmente conhecido pela riqueza, residentes famosos, iates e hotéis de alto luxo.
    * **Cassino de Monte Carlo:** Uma das construções mais icônicas da região, inaugurada no século XIX, que impulsionou a economia local.
    * **Esporte:** Sedia parte do famoso circuito de rua do Grande Prêmio de Mônaco de Fórmula 1 e o Rally de Monte Carlo.
  
---

## 2. A Matemática do MCTS Clássico: Fórmula UCT
Para decidir qual nó selecionar, o algoritmo calcula o índice **UCT** para cada nó filho disponível:

$$UCT = \frac{W_i}{N_i} + C \times \sqrt{\frac{\ln(N_p)}{N_i}}$$

* **$W_i$**: Número de vitórias (ou pontuação acumulada) do nó filho.
* **$N_i$**: Número de vezes que o nó filho foi visitado.
* **$N_p$**: Número de vezes que o nó pai foi visitado.
* **$C$**: Parâmetro de exploração (frequentemente $\sqrt{2} \approx 1.41$).
* **$\frac{W_i}{N_i}$**: Componente de *Exploitation* (aproveitar o que já funcionou).
* **$\sqrt{\frac{\ln(N_p)}{N_i}}$**: Componente de *Exploration* (explorar caminhos menos visitados).

---

## 3. Evolução Moderna: MCTS + Deep Learning (Fórmula PUCT)
Sistemas modernos (como AlphaZero e LLMs de raciocínio) eliminam as simulações aleatórias demoradas. Eles introduzem uma **Rede Neural** que prevê:
* **Política ($P(s, a)$):** Probabilidade a priori de quais ações são semanticamente melhores.
* **Valor ($Q(s, a)$):** Avaliação instantânea de vitória ou acerto lógico de um estado intermediário.

A fase de seleção passa a utilizar a fórmula **PUCT** (*Predictor Upper Confidence Bound applied to Trees*):

$$\text{PUCT} = \frac{W_i}{N_i} + C_{puct} \times P(s, a) \times \frac{\sqrt{N_p}}{1 + N_i}$$

### Exemplo de Código 1: Simulação da Seleção PUCT em Python
Este código demonstra como o bônus de exploração e o palpite da rede neural ($P$) se equilibram dinamicamente na tomada de decisão.

```python
import math

class NoLLMPUCT:
    def __init__(self, texto_pensamento, prioridade_p=0.0):
        self.texto = texto_pensamento
        self.prioridade_p = prioridade_p  # P: Probabilidade inicial dada pelo LLM
        self.visitas = 0                  # Ni: Número de visitas deste nó
        self.valor_acumulado = 0.0        # Usado para calcular a média Q
        
    @property
    def Q(self):
        if self.visitas == 0:
            return 0.0
        return self.valor_acumulado / self.visitas

    def calcular_puct(self, N_p, c_puct=1.5):
        exploitation = self.Q
        exploration = c_puct * self.prioridade_p * (math.sqrt(N_p) / (1 + self.visitas))
        return exploitation + exploration, exploitation, exploration

if __name__ == "__main__":
    visitas_pai = 50
    constante_c = 1.5

    # Pensamento A: Resposta óbvia, muito testada, mas com nota de qualidade em queda
    pensamento_A = NoLLMPUCT("Abordagem Padrão (Fórmula Decorada)", prioridade_p=0.85)
    pensamento_A.visitas = 35
    pensamento_A.valor_acumulado = 35 * 0.40

    # Pensamento B: Resposta criativa, pouco testada, mas com nota de lógica perfeita
    pensamento_B = NoLLMPUCT("Abordagem Criativa (Truque Algébrico)", prioridade_p=0.10)
    pensamento_B.visitas = 5
    pensamento_B.valor_acumulado = 5 * 0.95

    puct_A, exp_A, exl_A = pensamento_A.calcular_puct(visitas_pai, constante_c)
    puct_B, exp_B, exl_B = pensamento_B.calcular_puct(visitas_pai, constante_c)

    print(f"Pensamento A -> PUCT: {puct_A:.4f} (Q: {exp_A:.2f}, Bônus: {exl_A:.4f})")
    print(f"Pensamento B -> PUCT: {puct_B:.4f} (Q: {exp_B:.2f}, Bônus: {exl_B:.4f})")
```

---

## 4. O MCTS nos LLMs de Raciocínio
Nos LLMs focados em raciocínio complexo, o MCTS substitui o tabuleiro de jogo por uma **Árvore de Pensamentos**:
* **Nó Raiz:** A pergunta ou problema enviado pelo usuário.
* **Nós Filhos:** Passos ou etapas individuais de dedução textual/matemática.
* **Rede de Valor (Process Reward Model - PRM):** Um juiz automatizado que avalia a precisão de cada linha gerada, permitindo que a árvore retropropague penalidades para raciocínios errados e mude de rota antes de exibir o texto final na tela.

---

## 5. Jogos de Informação Oculta (Pôquer e ISMCTS)
Em cenários onde dados do jogo estão escondidos (como as cartas do oponente no Pôquer), o algoritmo evolui para o **ISMCTS** (*Information Set Monte Carlo Tree Search*) através de:

1. **Determinização:** Amostragem estocástica onde a IA gera múltiplos cenários fictícios preenchendo as informações ocultas aleatoriamente, porém respeitando as probabilidades históricas.
2. **Conjuntos de Informação (Information Sets):** Agrupamento matemático dos nós baseando-se unicamente nas informações visíveis. Estatísticas de mundos diferentes acumulam-se no mesmo nó visível, permitindo calcular o valor matemático do **blefe** de forma nativa.

---

## 6. Exemplo de Código 2: Jogo da Velha com MCTS Clássico Completo
Abaixo está o script executável de uma IA imbatível para o Jogo da Velha utilizando MCTS puramente clássico baseado em UCT.

```python
import math
import random

class JogoDaVelha:
    def __init__(self, tabuleiro=None, jogador_atual=1):
        self.tabuleiro = tabuleiro if tabuleiro is not None else [0] * 9
        self.jogador_atual = jogador_atual

    def movimentos_possiveis(self):
        return [i for i, v in enumerate(self.tabuleiro) if v == 0]

    def fazer_movimento(self, movimento):
        novo_tabuleiro = list(self.tabuleiro)
        novo_tabuleiro[movimento] = self.jogador_atual
        return JogoDaVelha(novo_tabuleiro, -self.jogador_atual)

    def checar_vencedor(self):
        linhas_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for linha in linhas_vitoria:
            soma = sum(self.tabuleiro[i] for i in linha)
            if soma == 3: return 1
            if soma == -3: return -1
        if 0 not in self.tabuleiro: return 0
        return None

class NoMCTS:
    def __init__(self, estado: JogoDaVelha, pai=None, movimento_origem=None):
        self.estado = estado
        self.pai = pai
        self.movimento_origem = movimiento_origem
        self.filhos = []
        self.visitas = 0
        self.vitorias = 0.0

    def totalmente_expandido(self):
        return len(self.filhos) == len(self.estado.movimentos_possiveis())

    def selecionar_filho_uct(self, C=1.414):
        melhor_valor = -float('inf')
        melhores_filhos = []
        for filho in self.filhos:
            valor_uct = (filho.vitorias / filho.visitas) + C * math.sqrt(math.log(self.visitas) / filho.visitas)
            if valor_uct > melhor_valor:
                melhor_valor = valor_uct
                melhores_filhos = [filho]
            elif valor_uct == melhor_valor:
                melhores_filhos.append(filho)
        return random.choice(melhores_filhos)

def mcts(estado_raiz, iteracoes=1500):
    raiz = NoMCTS(estado_raiz)
    for _ in range(iteracoes):
        no = raiz
        estado_simulado = estado_raiz
        
        while no.totalmente_expandido() and no.filhos:
            no = no.selecionar_filho_uct()
            estado_simulado = no.estado
            
        vencedor = estado_simulado.checar_vencedor()
        if vencedor is None:
            movimentos_testados = [f.movimento_origem for f in no.filhos]
            movimentos_disponiveis = [m for m in estado_simulado.movimentos_possiveis() if m not in movimentos_testados]
            if movimentos_disponiveis:
                mov = random.choice(movimentos_disponiveis)
                estado_simulado = estado_simulado.fazer_movimento(mov)
                novo_no = NoMCTS(estado_simulado, pai=no, movimento_origem=mov)
                no.filhos.append(novo_no)
                no = novo_no

        vencedor = estado_simulado.checar_vencedor()
        while vencedor is None:
            mov = random.choice(estado_simulado.movimentos_possiveis())
            estado_simulado = estado_simulado.fazer_movimento(mov)
            vencedor = estado_simulado.checar_vencedor()

        while no is not None:
            no.visitas += 1
            if vencedor == 0: no.vitorias += 0.5
            elif vencedor == no.estado.jogador_atual: no.vitorias += 1.0
            no = no.pai
            
    return max(raiz.filhos, key=lambda f: f.visitas).movimento_origem

def renderizar_tabuleiro(t):
    s = {1: 'X', -1: 'O', 0: ' '}
    print(f" {s[t[0]]} | {s[t[1]]} | {s[t[2]]} \n-----------\n {s[t[3]]} | {s[t[4]]} | {s[t[5]]} \n-----------\n {s[t[6]]} | {s[t[7]]} | {s[t[8]]} ")

def jogar():
    jogo = JogoDaVelha()
    while jogo.checar_vencedor() is None:
        if jogo.jogador_atual == 1:
            renderizar_tabuleiro(jogo.tabuleiro)
            try:
                mov = int(input("\nSua vez (0-8): "))
                if mov not in jogo.movimentos_possiveis(): continue
            except ValueError: continue
        else:
            print("\n🤖 IA pensando com MCTS...")
            mov = mcts(jogo, iteracoes=1500)
        jogo = jogo.fazer_movimento(mov)
    renderizar_tabuleiro(jogo.tabuleiro)
    print("\nFim de jogo! Vencedor:", jogo.checar_vencedor())

if __name__ == '__main__':
    # Para jogar via console, remova o comentário da linha abaixo:
    # jogar()
    print("MCTS pronto.")
```


# MCTS Avançado: Da Teoria Clássica aos LLMs de Raciocínio

Este documento apresenta uma visão técnica e prática consolidada sobre o algoritmo **Monte Carlo Tree Search (MCTS)**, cobrindo desde os fundamentos clássicos da busca em árvore até as modificações modernas usadas em Inteligência Artificial para jogos complexos, tomada de decisão sob incerteza e Modelos de Linguagem Avançados (LLMs).

---

## 1. O Algoritmo MCTS Clássico

O MCTS é um algoritmo heurístico de busca em árvore que combina a construção gradual de um grafo de decisões com simulações estatísticas (amostragem aleatória). O ciclo principal do algoritmo é repetido milhares de vezes por segundo e é dividido em quatro etapas sequenciais:

```
      [Seleção] ──> Navega pela árvore usando critérios como UCT
          │
          ▼
      [Expansão] ──> Adiciona novos estados plausíveis à árvore
          │
          ▼
     [Simulação] ──> Executa um playout rápido (aleatório) até o fim do jogo
          │
          ▼
  [Retropropagação] ──> Sobe atualizando as estatísticas de vitórias e visitas
```

1. **Seleção (Selection):** Partindo da raiz (estado atual), o algoritmo navega pelos nós existentes selecionando a melhor opção de acordo com uma fórmula de equilíbrio.
2. **Expansão (Expansion):** Quando alcança um nó que não está completamente mapeado, cria um ou mais nós filhos correspondentes às ações legais seguintes.
3. **Simulação / Playout (Simulation):** A partir do novo estado, o algoritmo simula movimentos rápidos (geralmente aleatórios) até atingir um estado terminal (vitória, derrota ou empate).
4. **Retropropagação (Backpropagation):** O resultado do término da partida é enviado de volta por toda a rota percorrida, incrementando a contagem de visitas e atualizando os scores de recompensa de cada nó pai.

---

## 2. Balanço Matemático: A Fórmula UCT

A seleção clássica de caminhos na árvore utiliza a fórmula **UCT** (*Upper Confidence Bound applied to Trees*) para balancear *Exploitation* (aproveitar o que já funcionou) e *Exploration* (testar novas possibilidades):

$$UCT = \frac{W_i}{N_i} + C \times \sqrt{\frac{\ln(N_p)}{N_i}}$$

*   **$W_i$**: Pontuação acumulada ou número de vitórias do nó filho.
*   **$N_i$**: Número de vezes que o nó filho foi visitado.
*   **$N_p$**: Número de vezes que o nó pai foi visitado.
*   **$C$**: Constante teórica de exploração (comumente definida como $\sqrt{2} \approx 1.414$).

---

## 3. Integração com Deep Learning: A Fórmula PUCT

Em IA moderna (AlphaZero, MuZero), o MCTS clássico foi modificado para mitigar a explosão combinatória eliminando os *playouts* puramente aleatórios. Substitui-se a simulação demorada por duas funções preditivas fornecidas por uma **Rede Neural Avançada**:
*   **Rede de Política ($P$):** Dá um palpite probabilístico a priori de quais movimentos são esteticamente melhores.
*   **Rede de Valor ($Q$):** Avalia e estima instantaneamente a chance de vitória de um estado intermediário, truncando a necessidade de jogar até o fim.

A seleção adota a fórmula **PUCT** (*Predictor Upper Confidence Bound applied to Trees*):

$$\text{PUCT} = \frac{W_i}{N_i} + C_{puct} \times P(s, a) \times \frac{\sqrt{N_p}}{1 + N_i}$$

### Código em Python: Simulação PUCT para Tomada de Decisões

```python
import math

class NoLLMPUCT:
    def __init__(self, texto_pensamento, prioridade_p=0.0):
        self.texto = texto_pensamento
        self.prioridade_p = prioridade_p  # Probabilidade inicial 'P' da rede
        self.visitas = 0                  # 'Ni'
        self.valor_acumulado = 0.0        # Recompensa somada para calcular 'Q'
        
    @property
    def Q(self):
        if self.visitas == 0:
            return 0.0
        return self.valor_acumulado / self.visitas

    def calcular_puct(self, N_p, c_puct=1.5):
        exploitation = self.Q
        exploration = c_puct * self.prioridade_p * (math.sqrt(N_p) / (1 + self.visitas))
        return exploitation + exploration, exploitation, exploration

if __name__ == "__main__":
    visitas_pai = 50
    constante_c = 1.5

    # Caminho A: Linha óbvia/padrão, muito visitada, mas com valor lógico caindo
    pensamento_A = NoLLMPUCT("Abordagem Padrão (Fórmula Decorada)", prioridade_p=0.85)
    pensamento_A.visitas = 35
    pensamento_A.valor_acumulado = 35 * 0.40  # Q médio = 0.40

    # Caminho B: Abordagem criativa, pouco testada, mas muito bem avaliada pelo validador
    pensamento_B = NoLLMPUCT("Abordagem Criativa (Truque Algébrico)", prioridade_p=0.10)
    pensamento_B.visitas = 5
    pensamento_B.valor_acumulado = 5 * 0.95   # Q médio = 0.95

    puct_A, exp_A, exl_A = pensamento_A.calcular_puct(visitas_pai, constante_c)
    puct_B, exp_B, exl_B = pensamento_B.calcular_puct(visitas_pai, constante_c)

    print(f"PUCT A: {puct_A:.4f} [Q: {exp_A:.2f}, Bonus: {exl_A:.2f}]")
    print(f"PUCT B: {puct_B:.4f} [Q: {exp_B:.2f}, Bonus: {exl_B:.2f}]")
```

---

## 4. Funcionamento do MCTS em LLMs de Raciocínio

Nos Modelos de Linguagem avançados focados em raciocínio estruturado, o MCTS substitui o tabuleiro de jogo por uma **Árvore de Pensamentos** (*Tree of Thoughts*):

*   **Nó Raiz:** O prompt ou problema inicial fornecido pelo usuário.
*   **Ações / Filhos:** Blocos de texto que representam passos dedutivos, premissas intermediárias ou sub-equações.
*   **Rede de Política:** O próprio LLM determinando a probabilidade de palavras continuarem de forma fluida o contexto textual.
*   **Process Reward Model (PRM):** Atua como a rede de valor de forma granular. Em vez de avaliar apenas a resposta final, o PRM avalia a correção factual de **cada linha** do raciocínio. Se o MCTS gera um erro lógico no "nó atual", a nota $Q$ despenca e a busca retropropaga a falha, forçando o LLM a podar essa ramificação e re-esboçar uma alternativa correta nos bastidores antes de exibir o output ao usuário.

---

## 5. MCTS sob Informação Oculta: ISMCTS e Blefe

Em ambientes parcialmente observáveis (como Pôquer ou Batalha Naval), onde dados fundamentais são invisíveis para o agente, o MCTS clássico falharia devido à *Ilusão de Clarividência*. IAs robustas contornam o problema aplicando o **Information Set MCTS (ISMCTS)** por meio de dois pilares:

1. **Determinização (Amostragem Estocástica):** A cada iteração da árvore, o simulador preenche as lacunas ocultas de maneira estatisticamente plausível. No Pôquer, chuta-se mãos hipotéticas para o adversário baseando-se no histórico de suas ações visíveis: $P(\text{Cartas} \mid \text{Ação})$.
2. **Conjuntos de Informação (Information Sets):** Nós idênticos no ponto de vista perceptível do agente são agrupados e mapeados para a mesma estrutura na árvore. Toda recompensa obtida de simulações em mundos ocultos distintos acumula dados estatísticos na mesma ação visível do jogador (ex: a ação `RAISE`). Se for constatado que o oponente tende a desistir (*Fold*) frequentemente contra apostas elevadas, o valor de $Q$ de blefar com uma mão ruim sobe estruturalmente através do MCTS, encontrando equilíbrios estratégicos similares ao *Equilíbrio de Nash*.

---

## 6. Exemplo Prático de Ponta a Ponta: Jogo da Velha com MCTS Clássico

O código a seguir é um script autônomo funcional em Python. Ele implementa o loop clássico do MCTS utilizando a fórmula **UCT** pura sobre as regras de um Jogo da Velha, entregando uma IA robusta e imbatível jogando via terminal.

```python
# -*- coding: utf-8 -*-
import math
import random

class JogoDaVelha:
    def __init__(self, tabuleiro=None, jogador_atual=1):
        self.tabuleiro = tabuleiro if tabuleiro is not None else [0] * 9
        self.jogador_atual = jogador_atual # 1 para X (Humano), -1 para O (IA MCTS)

    def movimentos_possiveis(self):
        return [i for i, v in enumerate(self.tabuleiro) if v == 0]

    def fazer_movimento(self, movimento):
        novo_tabuleiro = list(self.tabuleiro)
        novo_tabuleiro[movimento] = self.jogador_atual
        return JogoDaVelha(novo_tabuleiro, -self.jogador_atual)

    def checar_vencedor(self):
        linhas_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for linha in linhas_vitoria:
            soma = sum(self.tabuleiro[i] for i in linha)
            if soma == 3: return 1
            if soma == -3: return -1
        if 0 not in self.tabuleiro:
            return 0
        return None

class NoMCTS:
    def __init__(self, estado: JogoDaVelha, pai=None, movimento_origem=None):
        self.estado = estado
        self.pai = pai
        self.movimento_origem = movimento_origem
        self.filhos = []
        self.visitas = 0
        self.vitorias = 0.0

    def totalmente_expandido(self):
        return len(self.filhos) == len(self.estado.movimentos_possiveis())

    def selecionar_filho_uct(self, C=1.414):
        melhor_valor = -float('inf')
        melhores_filhos = []
        
        for filho in self.filhos:
            valor_uct = (filho.vitorias / filho.visitas) + C * math.sqrt(math.log(self.visitas) / filho.visitas)
            if valor_uct > melhor_valor:
                melhor_valor = valor_uct
                melhores_filhos = [filho]
            elif valor_uct == melhor_valor:
                melhores_filhos.append(filho)
                
        return random.choice(melhores_filhos)

def mcts(estado_raiz, iteracoes=1500):
    raiz = NoMCTS(estado_raiz)
    
    for _ in range(iteracoes):
        no = raiz
        estado_simulado = estado_raiz
        
        # 1. SELEÇÃO
        while no.totalmente_expandido() and no.filhos:
            no = no.selecionar_filho_uct()
            estado_simulado = no.estado
            
        # 2. EXPANSÃO
        vencedor = estado_simulado.checar_vencedor()
        if vencedor is None:
            movimentos_testados = [f.movimento_origem for f in no.filhos]
            movimentos_disponiveis = [m for m in estado_simulado.movimentos_possiveis() if m not in movimentos_testados]
            if movimentos_disponiveis:
                mov = random.choice(movimentos_disponiveis)
                estado_simulado = estado_simulado.fazer_movimento(mov)
                novo_no = NoMCTS(estado_simulado, pai=no, movimento_origem=mov)
                no.filhos.append(novo_no)
                no = novo_no

        # 3. SIMULAÇÃO
        vencedor = estado_simulado.checar_vencedor()
        while vencedor is None:
            mov = random.choice(estado_simulado.movimentos_possiveis())
            estado_simulado = estado_simulado.fazer_movimento(mov)
            vencedor = estado_simulado.checar_vencedor()

        # 4. RETROPROPAGAÇÃO
        while no is not None:
            no.visitas += 1
            if vencedor == 0:
                no.vitorias += 0.5
            elif vencedor == no.estado.jogador_atual:
                no.vitorias += 1.0
            no = no.pai
            
    melhor_filho = max(raiz.filhos, key=lambda f: f.visitas)
    return melhor_filho.movimento_origem

def renderizar_tabuleiro(tabuleiro):
    simbolos = {1: 'X', -1: 'O', 0: ' '}
    print(f" {simbolos[tabuleiro[0]]} | {simbolos[tabuleiro[1]]} | {simbolos[tabuleiro[2]]} ")
    print("-----------")
    print(f" {simbolos[tabuleiro[3]]} | {simbolos[tabuleiro[4]]} | {simbolos[tabuleiro[5]]} ")
    print("-----------")
    print(f" {simbolos[tabuleiro[6]]} | {simbolos[tabuleiro[7]]} | {simbolos[tabuleiro[8]]} ")

def jogar():
    jogo = JogoDaVelha()
    print("=== Jogo da Velha com MCTS Clássico ===")
    print("Você é o 'X'. Insira posições válidas de 0 a 8:")
    print(" 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8 
")
    
    while jogo.checar_vencedor() is None:
        if jogo.jogador_atual == 1:
            renderizar_tabuleiro(jogo.tabuleiro)
            try:
                mov = int(input("\nSua vez (0-8): "))
                if mov not in jogo.movimentos_possiveis():
                    print("Posição inválida ou ocupada!")
                    continue
            except ValueError:
                print("Insira um número!")
                continue
        else:
            print("\n🤖 IA pensando com MCTS...")
            mov = mcts(jogo, iteracoes=2000)
            print(f"A IA escolheu a posição: {mov}")
            
        jogo = jogo.fazer_movimento(mov)
        
    renderizar_tabuleiro(jogo.tabuleiro)
    vencedor = jogo.checar_vencedor()
    if vencedor == 1: print("\n🎉 Incrível! Você venceu.")
    elif vencedor == -1: print("\n🤖 A IA venceu.")
    else: print("\n🤝 Empate perfeito!")

if __name__ == '__main__':
    # Para jogar via prompt descomente a linha abaixo:
    # jogar()
    print("MCTS Clássico carregado perfeitamente.")
```

# MCTS Clássico aplicado ao Jogo da Velha

Este documento apresenta a explicação conceitual e o código-fonte completo em Python de uma Inteligência Artificial para o **Jogo da Velha** utilizando o algoritmo **MCTS (Monte Carlo Tree Search)** clássico.

---

## 1. Como as 4 Etapas funcionam no Jogo da Velha

Como o Jogo da Velha possui apenas 255.168 estados possíveis, o MCTS clássico consegue convergir rapidamente para o jogo perfeito em milissegundos. A IA torna-se completamente imbatível, resultando sempre em vitória ou empate.

1. **Seleção (Selection):** A IA avalia as jogadas já simuladas na árvore. Utilizando a fórmula **UCT**, se uma posição (como o centro do tabuleiro) resultou em maior aproveitamento histórico ponderado, ela opta por descer por essa ramificação.
2. **Expansão (Expansion):** Ao atingir a fronteira do conhecimento atual da árvore (uma jogada que ainda não foi simulada), o algoritmo cria um novo nó filho correspondente a esse movimento.
3. **Simulação (Simulation / Playout):** A partir do novo nó criado, a IA joga de forma totalmente **aleatória** contra si mesma (ora marcando `X`, ora marcando `O`) até que ocorra uma condição de fim de jogo (vitória, derrota ou empate).
4. **Retropropagação (Backpropagation):** O resultado final da simulação rápida sobe de volta por todos os nós visitados na árvore, somando pontos de vitória ao jogador vitorioso e atualizando a contagem de visitas de cada nó.

---

## 2. Código Completo em Python

Este script em Python implementa a estrutura do jogo, o motor de busca estruturado no algoritmo UCT e uma interface interativa via terminal para você jogar contra a IA.

```python
# -*- coding: utf-8 -*-
import math
import random

class JogoDaVelha:
    def __init__(self, tabuleiro=None, jogador_atual=1):
        # 1 para X (Humano), -1 para O (IA MCTS)
        self.tabuleiro = tabuleiro if tabuleiro is not None else [0] * 9
        self.jogador_atual = jogador_atual

    def movimentos_possiveis(self):
        return [i for i, v in enumerate(self.tabuleiro) if v == 0]

    def fazer_movimento(self, movimento):
        novo_tabuleiro = list(self.tabuleiro)
        novo_tabuleiro[movimento] = self.jogador_atual
        return JogoDaVelha(novo_tabuleiro, -self.jogador_atual)

    def checar_vencedor(self):
        linhas_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
            [0, 4, 8], [2, 4, 6]             # Diagonais
        ]
        for linha in linhas_vitoria:
            soma = sum(self.tabuleiro[i] for i in linha)
            if soma == 3: return 1   # Vitória do X
            if soma == -3: return -1 # Vitória do O
        if 0 not in self.tabuleiro:
            return 0 # Empate
        return None # Jogo continua

class NoMCTS:
    def __init__(self, estado: JogoDaVelha, pai=None, movimento_origem=None):
        self.estado = estado
        self.pai = pai
        self.movimento_origem = movimento_origem
        self.filhos = []
        self.visitas = 0
        self.vitorias = 0.0

    def totalmente_expandido(self):
        return len(self.filhos) == len(self.estado.movimentos_possiveis())

    def selecionar_filho_uct(self, C=1.414):
        melhor_valor = -float('inf')
        melhores_filhos = []
        
        for filho in self.filhos:
            # Fórmula Clássica UCT: Exploitation + Exploration
            valor_uct = (filho.vitorias / filho.visitas) + C * math.sqrt(math.log(self.visitas) / filho.visitas)
            if valor_uct > melhor_valor:
                melhor_valor = valor_uct
                melhores_filhos = [filho]
            elif valor_uct == melhor_valor:
                melhores_filhos.append(filho)
                
        return random.choice(melhores_filhos)

def mcts(estado_raiz, iteracoes=1500):
    raiz = NoMCTS(estado_raiz)
    
    for _ in range(iteracoes):
        no = raiz
        estado_simulado = estado_raiz
        
        # 1. SELEÇÃO
        while no.totalmente_expandido() and no.filhos:
            no = no.selecionar_filho_uct()
            estado_simulado = no.estado
            
        # 2. EXPANSÃO
        vencedor = estado_simulado.checar_vencedor()
        if vencedor is None:
            movimentos_testados = [f.movimento_origem for f in no.filhos]
            movimentos_disponiveis = [m for m in estado_simulado.movimentos_possiveis() if m not in movimentos_testados]
            if movimentos_disponiveis:
                mov = random.choice(movimentos_disponiveis)
                estado_simulado = estado_simulado.fazer_movimento(mov)
                novo_no = NoMCTS(estado_simulado, pai=no, movimiento_origem=mov)
                no.filhos.append(novo_no)
                no = novo_no

        # 3. SIMULAÇÃO (Playout Aleatório)
        vencedor = estado_simulado.checar_vencedor()
        while vencedor is None:
            mov = random.choice(estado_simulado.movimentos_possiveis())
            estado_simulado = estado_simulado.fazer_movimento(mov)
            vencedor = estado_simulado.checar_vencedor()

        # 4. RETROPROPAGAÇÃO
        while no is not None:
            no.visitas += 1
            if vencedor == 0:
                no.vitorias += 0.5  # Empate recebe recompensa parcial
            elif vencedor == no.estado.jogador_atual:
                no.vitorias += 1.0  # Vitória do jogador correspondente ao nó
            no = no.pai
            
    # O movimento selecionado é baseado na opção mais visitada (mais robusta)
    melhor_filho = max(raiz.filhos, key=lambda f: f.visitas)
    return melhor_filho.movimento_origem

def renderizar_tabuleiro(tabuleiro):
    simbolos = {1: 'X', -1: 'O', 0: ' '}
    print(f" {simbolos[tabuleiro[0]]} | {simbolos[tabuleiro[1]]} | {simbolos[tabuleiro[2]]} ")
    print("-----------")
    print(f" {simbolos[tabuleiro[3]]} | {simbolos[tabuleiro[4]]} | {simbolos[tabuleiro[5]]} ")
    print("-----------")
    print(f" {simbolos[tabuleiro[6]]} | {simbolos[tabuleiro[7]]} | {simbolos[tabuleiro[8]]} ")

def jogar():
    jogo = JogoDaVelha()
    print("=== Jogo da Velha com MCTS Clássico ===")
    print("Você é o 'X' e joga primeiro. Escolha posições de 0 a 8:")
    print(" 0 | 1 | 2 \n-----------\n 3 | 4 | 5 \n-----------\n 6 | 7 | 8 \n")
    
    while jogo.checar_vencedor() is None:
        if jogo.jogador_atual == 1:
            renderizar_tabuleiro(jogo.tabuleiro)
            try:
                mov = int(input("\nSua vez (0-8): "))
                if mov not in jogo.movimentos_possiveis():
                    print("Posição ocupada ou inválida! Tente outra.")
                    continue
            except ValueError:
                print("Digite um número válido de 0 a 8.")
                continue
        else:
            print("\n🤖 IA pensando com MCTS...")
            mov = mcts(jogo, iteracoes=1500)
            print(f"A IA jogou na posição: {mov}")
            
        jogo = 	jogo.fazer_movimento(mov)
        
    renderizar_tabuleiro(jogo.tabuleiro)
    vencedor = jogo.checar_vencedor()
    if vencedor == 1:   print("\n🎉 Incrível! Você venceu a IA!")
    elif vencedor == -1: print("\n🤖 A IA venceu! O MCTS não perdoa erros.")
    else:               print("\n🤝 Empate perfeito!")

if __name__ == '__main__':
    jogar()
```
