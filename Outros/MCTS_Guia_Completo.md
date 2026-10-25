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