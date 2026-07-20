# 30 Questões de Múltipla Escolha
## Aprendizado por Reforço: Modelos e Métricas de Avaliação

---

### 1. O que caracteriza fundamentalmente o Aprendizado por Reforço (RL)?
a) Um agente aprende a partir de exemplos rotulados fornecidos por um supervisor<br>
b) O algoritmo apenas descobre agrupamentos em dados sem rótulos<br>
c) Um agente aprende a tomar decisões por meio de interação com um ambiente, recebendo recompensas ou punições<br>
d) O modelo é treinado uma única vez e nunca interage com o ambiente

**Gabarito: c)** No RL, um agente interage sequencialmente com um ambiente, executando ações e recebendo recompensas (sinais de feedback), com o objetivo de aprender uma política que maximize a recompensa acumulada ao longo do tempo — diferente do aprendizado supervisionado (rótulos) e não-supervisionado (sem feedback).

---

### 2. Os elementos fundamentais de um problema de RL são:
a) Features, rótulos e função de perda<br>
b) Agente, ambiente, estado, ação e recompensa<br>
c) Centróides, clusters e distância<br>
d) Camadas, neurônios e pesos

**Gabarito: b)** Um problema de RL é tipicamente descrito por um agente que observa estados do ambiente, executa ações, recebe recompensas e transita para novos estados, buscando aprender uma política ótima.

---

### 3. Um Processo de Decisão de Markov (MDP) é definido, formalmente, pela tupla:
a) (Estados, Ações, Função de Transição, Função de Recompensa, Fator de Desconto)<br>
b) (Centróides, Distâncias, Clusters)<br>
c) (Pesos, Bias, Função de Ativação)<br>
d) (Rótulos, Features, Acurácia)

**Gabarito: a)** O MDP é formalizado como (S, A, P, R, γ), em que S é o conjunto de estados, A o conjunto de ações, P a função de transição de estados, R a função de recompensa e γ o fator de desconto.

---

### 4. A "propriedade de Markov" implica que:
a) O próximo estado depende de toda a história de estados e ações passadas<br>
b) O próximo estado depende apenas do estado atual e da ação tomada, não do histórico completo<br>
c) Não existe transição entre estados<br>
d) A recompensa é sempre igual a zero

**Gabarito: b)** A propriedade de Markov assume que o estado atual contém toda a informação relevante para prever o futuro: P(s_{t+1} | s_t, a_t) não depende dos estados/ações anteriores a t.

---

### 5. O fator de desconto (γ, gamma) em RL serve para:
a) Aumentar artificialmente a recompensa recebida<br>
b) Ponderar a importância de recompensas futuras em relação a recompensas imediatas<br>
c) Definir o número de estados possíveis<br>
d) Eliminar a necessidade de exploração

**Gabarito: b)** O gamma (0 ≤ γ ≤ 1) determina o quanto recompensas futuras são "descontadas" em relação a recompensas imediatas; γ próximo de 0 torna o agente mais "imediatista", enquanto γ próximo de 1 valoriza recompensas de longo prazo.

---

### 6. Uma política (policy), em RL, é definida como:
a) Uma tabela de rótulos verdadeiros<br>
b) Uma função que mapeia estados para ações (ou distribuições de probabilidade sobre ações)<br>
c) A soma total das recompensas recebidas<br>
d) O conjunto de todos os estados possíveis

**Gabarito: b)** A política π(a|s) define o comportamento do agente: para cada estado, indica qual ação tomar (política determinística) ou a probabilidade de tomar cada ação possível (política estocástica).

---

### 7. A Função de Valor de Estado V(s) representa:
a) A recompensa imediata recebida no estado s<br>
b) O retorno esperado (soma de recompensas futuras descontadas) a partir do estado s, seguindo uma determinada política<br>
c) O número de ações possíveis no estado s<br>
d) A probabilidade de transição entre dois estados

**Gabarito: b)** V^π(s) é o valor esperado do retorno acumulado (recompensas futuras descontadas) que o agente obterá a partir do estado s, seguindo a política π.

---

### 8. A Função de Valor de Ação Q(s, a), diferente de V(s), representa:
a) O valor esperado de estar no estado s e executar a ação a, seguindo a política a partir daí<br>
b) Apenas a recompensa imediata da ação a<br>
c) A probabilidade do estado s ocorrer<br>
d) O número total de episódios de treinamento

**Gabarito: a)** Q^π(s, a) estima o retorno esperado ao tomar a ação a no estado s e, a partir daí, seguir a política π — é a base de algoritmos como Q-Learning, que buscam aprender diretamente essa função.

---

### 9. A Equação de Bellman é fundamental em RL porque:
a) Define a arquitetura de uma rede neural<br>
b) Expressa o valor de um estado (ou par estado-ação) de forma recursiva, em função do valor dos estados seguintes<br>
c) Calcula diretamente a acurácia do agente<br>
d) Elimina a necessidade de recompensas

**Gabarito: b)** A equação de Bellman decompõe o valor de um estado na soma da recompensa imediata mais o valor descontado do(s) próximo(s) estado(s), permitindo métodos iterativos de estimação (Programação Dinâmica, TD-Learning, etc.).

---

### 10. O dilema Exploração vs. Explotação (Exploration vs. Exploitation) refere-se a:
a) A escolha entre normalizar ou não os dados de entrada<br>
b) O equilíbrio entre experimentar novas ações para descobrir melhores estratégias (exploração) e escolher as ações já conhecidas como boas (explotação)<br>
c) A escolha entre usar CPU ou GPU no treinamento<br>
d) A divisão entre dados de treino e teste

**Gabarito: b)** Um agente precisa balancear explorar o ambiente (testar ações menos conhecidas, que podem revelar recompensas melhores) e explotar o conhecimento já adquirido (escolher ações que sabidamente geram boas recompensas).

---

### 11. A estratégia ε-greedy (epsilon-greedy) funciona da seguinte forma:
a) O agente sempre escolhe a ação de maior valor estimado<br>
b) O agente nunca explora, apenas explota<br>
c) ε representa o número total de episódios<br>
d) Com probabilidade ε, o agente escolhe uma ação aleatória (exploração); com probabilidade 1-ε, escolhe a ação de maior valor estimado (explotação)

**Gabarito: d)** É uma das estratégias mais simples para equilibrar exploração e explotação: com pequena probabilidade ε, uma ação aleatória é escolhida; caso contrário, a ação considerada ótima segundo as estimativas atuais é selecionada.

---

### 12. O Q-Learning é classificado como um algoritmo:
a) On-policy, pois aprende a partir da política que está sendo seguida<br>
b) Off-policy, pois pode aprender a política ótima mesmo enquanto segue uma política de exploração diferente<br>
c) Exclusivo para problemas de regressão<br>
d) Baseado em clustering

**Gabarito: b)** O Q-Learning é off-policy: ele atualiza suas estimativas de Q(s,a) usando a ação de maior valor no próximo estado (max), independentemente da ação realmente executada pela política de comportamento (que pode incluir exploração aleatória).

---

### 13. A regra de atualização do Q-Learning utiliza:
a) A diferença entre a estimativa atual de Q(s,a) e um "alvo" baseado na recompensa recebida mais o valor máximo estimado do próximo estado (TD-target)<br>
b) Apenas a recompensa imediata, ignorando estados futuros<br>
c) Uma função de perda de entropia cruzada<br>
d) A distância euclidiana entre estados

**Gabarito: a)** A atualização segue: Q(s,a) ← Q(s,a) + α[r + γ·max_a' Q(s',a') − Q(s,a)], em que o termo entre colchetes é o erro de diferença temporal (TD-error) entre o valor atual e o alvo estimado.

---

### 14. O algoritmo SARSA (State-Action-Reward-State-Action) difere do Q-Learning porque:
a) É um algoritmo de clustering<br>
b) É on-policy: usa a ação realmente escolhida pela política de comportamento (incluindo exploração) para calcular o alvo, em vez do valor máximo possível<br>
c) Não usa recompensas<br>
d) Só funciona em ambientes contínuos

**Gabarito: b)** No SARSA, a atualização usa Q(s', a'), em que a' é a ação efetivamente escolhida (segundo a política atual, incluindo exploração), tornando-o on-policy — diferente do Q-Learning, que usa o valor máximo teórico (max_a' Q(s', a')).

---

### 15. O Deep Q-Network (DQN) combina Q-Learning com:
a) Árvores de decisão<br>
b) Regressão linear simples<br>
d) Clustering hierárquico
d) Redes neurais profundas, para aproximar a função Q(s,a) em espaços de estados muito grandes ou contínuos<br>

**Gabarito: d)** O DQN utiliza uma rede neural para aproximar Q(s,a), permitindo aplicar Q-Learning em problemas com espaços de estados de altíssima dimensão (ex.: pixels de um jogo), o que seria inviável com uma tabela Q tradicional.

---

### 16. Técnicas como "Experience Replay" e "Target Network", usadas no DQN, servem para:
a) Aumentar a instabilidade do treinamento<br>
b) Estabilizar o treinamento, reduzindo correlações entre amostras sequenciais e evitando alvos que mudam a cada passo<br>
c) Eliminar a necessidade de recompensas<br>
d) Substituir completamente a rede neural por uma tabela Q

**Gabarito: b)** O Experience Replay armazena transições passadas em um buffer e as amostra aleatoriamente para treinar a rede, reduzindo a correlação temporal entre exemplos consecutivos. A Target Network mantém uma cópia "congelada" da rede para calcular os alvos (targets), sendo atualizada periodicamente, o que estabiliza o treinamento.

---

### 17. Métodos baseados em valor (value-based), como Q-Learning e DQN, diferem de métodos baseados em política (policy-based) porque:
a) Métodos baseados em valor aprendem diretamente uma política parametrizada, enquanto métodos baseados em política aprendem apenas Q(s,a)<br>
b) Não há diferença prática entre as duas abordagens<br>
c) Métodos baseados em valor aprendem a estimar funções de valor (como Q) e derivam a política a partir delas; métodos baseados em política otimizam diretamente os parâmetros de uma política<br>
d) Métodos baseados em política não podem ser usados em ambientes contínuos

**Gabarito: c)** Métodos value-based (ex.: Q-Learning) estimam V(s) ou Q(s,a) e definem a política implicitamente (ex.: escolhendo a ação de maior valor). Métodos policy-based (ex.: REINFORCE, PPO) otimizam diretamente os parâmetros da política π_θ(a|s), o que é especialmente útil em espaços de ação contínuos.

---

### 18. O algoritmo REINFORCE é um exemplo clássico de método:
a) Baseado em valor (value-based)<br>
b) Baseado em gradiente de política (policy gradient), que ajusta os parâmetros da política na direção que aumenta o retorno esperado<br>
c) De clustering hierárquico<br>
d) De regressão linear

**Gabarito: b)** O REINFORCE é um algoritmo de policy gradient: utiliza o retorno obtido em episódios completos (Monte Carlo) para estimar o gradiente da recompensa esperada em relação aos parâmetros da política, ajustando-os para aumentar a probabilidade de ações que levaram a bons retornos.

---

### 19. Métodos Ator-Crítico (Actor-Critic) combinam:
a) Dois algoritmos de clustering diferentes<br>
b) Um "ator", que aprende a política, e um "crítico", que estima uma função de valor para reduzir a variância das estimativas de gradiente<br>
c) Apenas árvores de decisão<br>
d) Regressão logística e SVM

**Gabarito: b)** No esquema Ator-Crítico, o ator escolhe as ações (aprendendo a política), enquanto o crítico estima V(s) ou Q(s,a) para avaliar essas ações, fornecendo um sinal de erro (vantagem) mais estável e com menor variância do que usar apenas os retornos observados (como no REINFORCE puro).

---

### 20. O algoritmo PPO (Proximal Policy Optimization) é conhecido por:
a) Não utilizar nenhuma função de recompensa<br>
b) Limitar (clipar) a magnitude das atualizações de política a cada passo, evitando mudanças bruscas que desestabilizem o treinamento<br>
c) Ser exclusivo para problemas de classificação supervisionada<br>
d) Não poder ser usado em ambientes com ações contínuas

**Gabarito: b)** O PPO introduz uma função objetivo "clipada" que restringe o quanto a nova política pode se afastar da política anterior em uma única atualização, tornando o treinamento mais estável do que métodos de policy gradient mais simples, sem exigir cálculos de segunda ordem como no TRPO.

---

### 21. Em RL, um "episódio" refere-se a:
a) Uma única ação isolada do agente<br>
b) O número total de parâmetros do modelo<br>
c) Uma métrica de avaliação de classificação<br>
d) Uma sequência completa de interações entre agente e ambiente, do estado inicial até um estado terminal

**Gabarito: d)** Um episódio é uma trajetória completa (s₀, a₀, r₁, s₁, a₁, r₂, ..., até um estado terminal), muito comum em tarefas episódicas como jogos, em contraste com tarefas contínuas, que não têm um fim natural.

---

### 22. A principal métrica utilizada para avaliar o desempenho de um agente de RL durante e após o treinamento é:
a) Acurácia de classificação<br>
b) Recompensa total (ou média) acumulada por episódio (retorno)<br>
c) Coeficiente de silhueta<br>
d) R² (coeficiente de determinação)

**Gabarito: b)** A métrica central em RL é o retorno (soma das recompensas, possivelmente descontadas) obtido por episódio; a evolução da recompensa média ao longo dos episódios de treinamento é o principal indicador de aprendizado do agente.

---

### 23. Ao avaliar um agente de RL, por que é importante considerar não apenas a recompensa média, mas também sua variância entre episódios?
a) A variância não tem nenhuma relevância prática<br>
b) Alta variância pode indicar uma política instável ou pouco confiável, mesmo que a recompensa média seja boa<br>
c) A variância substitui completamente a necessidade de calcular a recompensa média<br>
d) Variância baixa sempre indica que o agente está explorando o suficiente

**Gabarito: b)** Um agente pode ter boa recompensa média, mas com desempenho muito inconsistente entre episódios (alta variância), o que pode ser problemático em aplicações que exigem confiabilidade (ex.: robótica, sistemas críticos).

---

### 24. A "taxa de convergência" de um algoritmo de RL refere-se a:
a) A velocidade de processamento da GPU utilizada<br>
b) A quantidade de episódios/interações necessárias para que a política do agente se estabilize em (ou se aproxime de) um bom desempenho<br>
c) O número de estados do ambiente<br>
d) A precisão de ponto flutuante usada nos cálculos

**Gabarito: b)** É comum comparar algoritmos de RL observando quantos episódios (ou passos de interação) cada um necessita até atingir um determinado nível de recompensa, o que reflete a eficiência de amostragem (sample efficiency) do método.

---

### 25. A "eficiência amostral" (sample efficiency) em RL refere-se a:
a) O quão eficientemente o agente utiliza a memória RAM disponível<br>
b) A quantidade de interações com o ambiente necessárias para o agente aprender uma boa política<br>
c) O número de camadas de uma rede neural<br>
d) A precisão do cálculo do fator de desconto

**Gabarito: b)** Algoritmos com alta eficiência amostral conseguem aprender boas políticas com relativamente poucas interações com o ambiente — algo especialmente importante quando essas interações são caras ou arriscadas (ex.: robôs físicos, sistemas reais).

---

### 26. O "arrependimento" (regret), usado principalmente em problemas de bandits multi-armados, mede:
a) A diferença entre a recompensa obtida pelo agente e a recompensa que seria obtida sempre escolhendo a melhor ação possível<br>
b) O tempo total de treinamento do agente<br>
c) O número de estados terminais alcançados<br>
d) A acurácia de um classificador supervisionado

**Gabarito: a)** O regret acumulado quantifica a "perda" total por não ter escolhido sempre a ação ótima desde o início; algoritmos com menor regret aprendem mais rapidamente qual é a melhor ação/estratégia.

---

### 27. Em Aprendizado por Reforço, o problema conhecido como "recompensa esparsa" (sparse reward) ocorre quando:
a) O agente recebe recompensas positivas a cada passo, facilitando o aprendizado<br>
b) O ambiente não possui estados terminais<br>
c) As recompensas informativas ocorrem raramente (ex.: apenas ao final de uma longa sequência de ações), dificultando o aprendizado<br>
d) O fator de desconto é igual a 1

**Gabarito: c)** Quando recompensas úteis são raras (ex.: só há recompensa ao vencer um jogo longo), o agente recebe pouco sinal de feedback ao longo do caminho, tornando o aprendizado mais lento e desafiador — problema frequentemente mitigado com técnicas como reward shaping ou métodos de exploração mais sofisticados.

---

### 28. O "Reward Shaping" é uma técnica que consiste em:
a) Modificar ou complementar a função de recompensa original com sinais adicionais, para guiar o aprendizado do agente de forma mais eficiente<br>
b) Eliminar completamente a função de recompensa original<br>
c) Substituir o ambiente por um conjunto de dados rotulados<br>
d) Aumentar artificialmente o fator de desconto para 2

**Gabarito: a)** Reward shaping adiciona recompensas intermediárias (bem projetadas) para tornar o aprendizado mais eficiente, especialmente em cenários de recompensa esparsa — mas deve ser feito com cuidado para não induzir comportamentos indesejados que "enganem" o objetivo original.

---

### 29. Comparar diferentes algoritmos de RL em um mesmo ambiente (benchmark) é importante porque:
a) Não há necessidade de comparação, todos os algoritmos têm desempenho idêntico<br>
b) Permite avaliar critérios como recompensa final obtida, velocidade de convergência, estabilidade do treinamento e eficiência amostral, sob as mesmas condições<br>
c) Substitui completamente a necessidade de ajuste de hiperparâmetros<br>
d) É relevante apenas para problemas de classificação supervisionada

**Gabarito: b)** Ambientes padronizados de benchmark (como os disponíveis em bibliotecas de simulação) permitem comparar algoritmos de forma justa, considerando múltiplos critérios (não apenas a recompensa final, mas também estabilidade e eficiência), já que diferentes aplicações podem priorizar aspectos distintos.

---

### 30. Por que a avaliação de agentes de RL costuma exigir múltiplas execuções (seeds) independentes do treinamento?
a) Porque o treinamento de RL é determinístico e sempre produz exatamente o mesmo resultado<br>
b) Porque o processo de treinamento envolve fontes de aleatoriedade (inicialização, exploração, amostragem), e múltiplas execuções ajudam a estimar a média e a variabilidade real do desempenho do agente<br>
c) Porque isso elimina a necessidade de qualquer métrica de avaliação<br>
d) Porque múltiplas execuções sempre produzem resultados idênticos entre si

**Gabarito: b)** Devido a fatores aleatórios (inicialização de pesos, estratégias de exploração, amostragem de experiências), um único treinamento pode não representar bem o desempenho típico do algoritmo. Repetir o treinamento com diferentes seeds e reportar média e desvio padrão da recompensa é uma prática recomendada para uma avaliação mais confiável e reprodutível.

---

*Documento gerado para fins educacionais sobre Aprendizado por Reforço.*
