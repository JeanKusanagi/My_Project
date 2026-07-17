# Aprendizado por Reforço (Reinforcement Learning)
## Modelos e Métricas de Avaliação — Material de Estudo

---

## 1. Conceito Central

**Aprendizado por reforço (RL)** é o paradigma de ML em que um **agente** aprende a tomar decisões através de **tentativa e erro**, interagindo com um **ambiente**, recebendo **recompensas (rewards)** ou **punições** como consequência de suas ações, com o objetivo de **maximizar a recompensa acumulada** ao longo do tempo.

> **Definição de prova:** "Diferente do supervisionado (que aprende com pares X-y rotulados) e do não-supervisionado (que busca estrutura em dados sem rótulo), o RL aprende através de um **sinal de recompensa escalar**, que não diz qual era a ação 'correta', apenas **o quão boa** foi a ação tomada."

⚠️ **Pegadinha número 1 (a mais cobrada de todas):** confundir RL com supervisionado. No RL, **não existe um rótulo correto explícito** — o agente só recebe uma recompensa (feedback fraco e atrasado), e precisa descobrir por conta própria qual sequência de ações levou a esse resultado (problema de **atribuição de crédito temporal**, *credit assignment*).

---

## 2. Elementos Fundamentais (vocabulário-base de prova)

| Elemento | Definição |
|---|---|
| **Agente** | Quem toma as decisões/ações |
| **Ambiente (environment)** | Tudo com que o agente interage; responde às ações com novo estado e recompensa |
| **Estado (state, s)** | Representação da situação atual do ambiente |
| **Ação (action, a)** | Escolha feita pelo agente em um estado |
| **Recompensa (reward, r)** | Sinal numérico de feedback (positivo ou negativo) |
| **Política (policy, π)** | Estratégia/função que mapeia estados em ações — o que o agente está tentando aprender |
| **Função de valor (value function, V ou Q)** | Estima o retorno esperado a partir de um estado (ou par estado-ação) |
| **Episódio** | Uma sequência completa de interações até um estado terminal |

⚠️ **Pegadinha:** confundir **recompensa (reward)**, que é imediata, com **retorno (return)**, que é a soma (geralmente descontada) de recompensas futuras — o que o agente realmente tenta maximizar é o **retorno esperado**, não a recompensa de um único passo.

---

## 3. MDP — Processo de Decisão de Markov

RL é formalizado matematicamente como um **MDP (Markov Decision Process)**, definido pela tupla **(S, A, P, R, γ)**:
- **S:** conjunto de estados
- **A:** conjunto de ações
- **P:** função de transição de probabilidade P(s'|s,a)
- **R:** função de recompensa
- **γ (gamma):** fator de desconto (0 ≤ γ ≤ 1)

**Propriedade de Markov:** o próximo estado depende **apenas do estado e ação atuais**, não do histórico completo.

> **Definição de prova:** "O futuro é independente do passado, dado o presente."

⚠️ **Pegadinha:** o fator de desconto **γ** — se γ = 0, o agente só se importa com a recompensa **imediata** (miopia total); se γ próximo de 1, o agente valoriza fortemente recompensas **futuras** (visão de longo prazo). Provas gostam de perguntar o efeito de γ = 0 vs. γ = 1.

---

## 4. Exploração vs. Explotação (Exploration vs. Exploitation)

Um dos **dilemas centrais** do RL:
- **Explotação (exploitation):** usar o conhecimento já aprendido para escolher a ação que parece melhor até agora.
- **Exploração (exploration):** testar ações novas/desconhecidas para descobrir se existem recompensas melhores ainda não descobertas.

**Estratégia clássica:** **ε-greedy** (epsilon-greedy) — com probabilidade ε, escolhe uma ação aleatória (explora); com probabilidade 1−ε, escolhe a melhor ação conhecida (explota).

⚠️ **Pegadinha (queridinha de prova):** ε muito alto → agente explora demais e nunca consolida uma boa política (ineficiente). ε muito baixo (ou zero) → agente explota cedo demais e pode ficar preso em um **ótimo local**, nunca descobrindo uma estratégia melhor.

---

## 5. Modelos e Algoritmos

### 5.1 Programação Dinâmica (Value Iteration / Policy Iteration)
- Exigem **conhecimento completo do modelo** do ambiente (P e R conhecidos) — chamado de **model-based**.
- Pouco usados na prática porque o modelo do ambiente raramente é conhecido de antemão.

### 5.2 Métodos Model-Free — Baseados em Valor

**Q-Learning**
- Aprende a **função Q(s,a)**, que estima o retorno esperado ao tomar a ação *a* no estado *s* e seguir a política ótima depois.
- É um método **off-policy**: aprende a política ótima **independentemente** da política usada para explorar o ambiente.
- Atualização (equação de Bellman) via **diferença temporal (TD-learning)**.

**SARSA (State-Action-Reward-State-Action)**
- Muito parecido com Q-Learning, mas é **on-policy**: atualiza Q com base na ação que **realmente será tomada** pela política atual (incluindo exploração), não na ação ótima teórica.

⚠️ **Pegadinha número 1 (super cobrada):** diferença entre **on-policy** e **off-policy**:
- **On-policy (SARSA):** aprende sobre a política que está sendo **usada** para agir (mais "conservador", considera os riscos da própria exploração).
- **Off-policy (Q-Learning):** aprende sobre a política **ótima**, mesmo enquanto explora com outra política (mais "otimista"/agressivo).
- Exemplo clássico: no problema do "cliff walking" (andar na beira do penhasco), Q-Learning aprende o caminho mais curto (arriscado), SARSA aprende um caminho mais seguro (considera que às vezes vai explorar e pode cair).

### 5.3 Deep Q-Network (DQN)
- Combina **Q-Learning** com **redes neurais profundas** para aproximar Q(s,a) quando o espaço de estados é grande/contínuo (ex.: pixels de um jogo).
- Inovações-chave: **Experience Replay** (guarda experiências passadas e re-amostra aleatoriamente para treinar, quebrando correlação temporal) e **rede-alvo (target network)** (estabiliza o treinamento).

### 5.4 Métodos Baseados em Política (Policy Gradient)
- Em vez de estimar Q(s,a) e derivar a política dela, **aprende diretamente a política π(a|s)**.
- Útil em espaços de ação **contínuos** (ex.: controle de robôs), onde métodos baseados em valor (Q-Learning) são difíceis de aplicar.
- Exemplos: REINFORCE, PPO (Proximal Policy Optimization), TRPO.

### 5.5 Métodos Ator-Crítico (Actor-Critic)
- Combina os dois mundos: um **Ator** (aprende a política) e um **Crítico** (aprende a função de valor, avalia as ações do ator).
- Reduz a variância dos métodos puros de policy gradient.
- Exemplos: A2C, A3C, DDPG, PPO (também pode ser visto como ator-crítico).

⚠️ **Pegadinha:** confundir **Policy Gradient puro** com **Actor-Critic** — o primeiro só tem a política sendo otimizada diretamente pelo retorno observado (alta variância); o segundo usa um crítico para dar um feedback mais estável e reduzir a variância das atualizações.

---

## 6. Métricas de Avaliação em RL

Diferente do supervisionado (com métricas fechadas como acurácia/F1) e não-supervisionado (com silhouette etc.), em RL a avaliação é mais **empírica e baseada em desempenho no ambiente**.

| Métrica | O que mede |
|---|---|
| **Retorno acumulado (cumulative reward)** | Soma total de recompensas em um episódio |
| **Retorno médio por episódio** | Média do retorno em vários episódios de teste — mede desempenho e estabilidade |
| **Taxa de convergência** | Quantos episódios/passos são necessários até a política estabilizar |
| **Regret (arrependimento)** | Diferença entre a recompensa obtida e a recompensa que seria obtida pela política ótima |
| **Amostragem eficiente (sample efficiency)** | Quantas interações com o ambiente são necessárias para aprender uma boa política |
| **Taxa de sucesso (success rate)** | % de episódios em que o agente atinge o objetivo (comum em robótica/jogos) |

⚠️ **Pegadinha número 1:** olhar só a **recompensa de um único episódio** para julgar o modelo — recompensas em RL têm **alta variância** (o ambiente e a exploração são estocásticos); a avaliação correta exige **média e desvio-padrão ao longo de múltiplos episódios/seeds**.

⚠️ **Pegadinha número 2:** confundir "recompensa alta" com "modelo bom" sem considerar o **design da função de recompensa** — um agente pode encontrar um *"reward hacking"* (maximizar a recompensa de um jeito não-intencional, explorando falhas no design da recompensa, sem de fato resolver o problema real). Isso é um tópico clássico de pegadinha avançada.

⚠️ **Pegadinha número 3:** RL não tem "conjunto de teste" no mesmo sentido do supervisionado — a avaliação geralmente é feita **rodando a política aprendida no próprio ambiente (ou em variações dele)**, e não em um dataset estático separado.

---

## 7. Exploração de Bandits (Multi-Armed Bandit) — caso simplificado

- Versão **simplificada** de RL, **sem estados** (ou com um único estado) — só existe a escolha de qual "braço" (ação) puxar para maximizar recompensa.
- Muito usado como introdução ao dilema exploração vs. explotação.
- Aplicação real: **testes A/B dinâmicos**, otimização de anúncios/recomendações em tempo real.

⚠️ **Pegadinha:** achar que Multi-Armed Bandit é "RL completo" — falta o conceito de **estado** e **transição entre estados**, que é central em MDPs completos.

---

## 8. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Diferença entre RL e supervisionado | RL não tem rótulo correto, só recompensa (feedback fraco/atrasado) |
| γ = 0 vs. γ próximo de 1 | γ=0: só recompensa imediata (miopia); γ≈1: valoriza o futuro |
| Diferença entre on-policy e off-policy | SARSA (on-policy, conservador) vs. Q-Learning (off-policy, otimista) |
| Espaço de ações contínuo | Métodos de Policy Gradient (não Q-Learning tabular) |
| Reduzir variância do Policy Gradient | Actor-Critic |
| Ambiente grande demais para tabela Q | Deep Q-Network (aproximação por rede neural) |
| Avaliar desempenho de um agente | Retorno médio em múltiplos episódios, nunca um único episódio |
| Agente "trapaceando" a métrica | Reward hacking / má especificação da função de recompensa |
| Sem conceito de estado, só ações | Multi-Armed Bandit |
| Dilema exploração x explotação | ε-greedy: ε alto explora demais, ε baixo trava em ótimo local |

---

## 9. Aplicação Profissional (além da prova)

- **Jogos e simulações** (AlphaGo, Atari, robótica simulada): DQN, Actor-Critic, PPO.
- **Sistemas de recomendação em tempo real:** Multi-Armed Bandits para decidir qual conteúdo/anúncio mostrar, balanceando explorar novos itens e explotar os que já sabem que convertem.
- **Precificação dinâmica e alocação de recursos** (ex.: preços de ride-hailing, alocação de servidores em cloud): RL para decisões sequenciais sob incerteza.
- **Robótica e controle:** Policy Gradient/Actor-Critic para ações contínuas (torque de motores, direção).
- **RLHF (Reinforcement Learning from Human Feedback):** usado no treinamento de modelos de linguagem (como o próprio Claude) — humanos avaliam respostas e esse feedback é convertido em sinal de recompensa para ajustar o modelo via RL. Tópico cada vez mais cobrado em provas atuais de IA.
- Na prática, o maior desafio profissional de RL costuma **não ser o algoritmo em si, mas o design da função de recompensa** — recompensas malformadas geram comportamentos inesperados (reward hacking), então boa parte do trabalho de um profissional é simular, testar e iterar sobre o *reward shaping* antes de colocar o agente em produção.

---

## 10. Perguntas típicas de prova (para se testar)

1. Por que o aprendizado por reforço não é considerado "supervisionado", mesmo recebendo um feedback numérico (recompensa)?
2. Explique a diferença entre Q-Learning (off-policy) e SARSA (on-policy) usando o exemplo do "cliff walking".
3. O que acontece com o comportamento do agente se γ (fator de desconto) for igual a 0? E se for próximo de 1?
4. O que é "reward hacking" e por que ele é um risco no design de sistemas de RL?
5. Por que avaliar um agente de RL com apenas um episódio de teste é estatisticamente problemático?
6. Qual a diferença entre métodos baseados em valor (Q-Learning) e métodos baseados em política (Policy Gradient), e quando usar cada um?
