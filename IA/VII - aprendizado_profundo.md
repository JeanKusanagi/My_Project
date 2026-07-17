# Aprendizado Profundo (Deep Learning)
## Modelos e Métricas de Avaliação — Material de Estudo

---

## 1. Conceito Central

**Deep Learning** é um subcampo do Machine Learning baseado em **redes neurais artificiais com múltiplas camadas** (por isso "profundo"), capazes de aprender **representações hierárquicas** dos dados automaticamente — sem a necessidade de engenharia manual de features.

> **Definição de prova:** "Enquanto o ML clássico geralmente exige que um especialista extraia as features relevantes (feature engineering manual), o Deep Learning aprende essas features **automaticamente**, camada por camada, a partir dos dados brutos (pixels, texto, áudio)."

⚠️ **Pegadinha número 1 (muito cobrada):** Deep Learning **não é um paradigma separado** de supervisionado/não-supervisionado/reforço — é uma **classe de arquiteturas de modelos** (redes neurais profundas) que pode ser aplicada em **qualquer um dos três paradigmas**: CNNs supervisionadas para classificação de imagem, Autoencoders não-supervisionados, DQN é RL com redes profundas etc.

---

## 2. Blocos Fundamentais de uma Rede Neural

| Componente | Definição |
|---|---|
| **Neurônio/Unidade** | Combinação linear das entradas + bias, seguida de função de ativação |
| **Camada (layer)** | Conjunto de neurônios processando em paralelo |
| **Peso (weight)** | Parâmetro aprendido que escala a importância de cada entrada |
| **Função de ativação** | Introduz não-linearidade (ReLU, Sigmoid, Tanh, Softmax) |
| **Forward propagation** | Passagem dos dados da entrada até a saída, gerando a predição |
| **Função de perda (loss function)** | Mede o erro entre predição e valor real |
| **Backpropagation** | Algoritmo que calcula o gradiente da perda em relação a cada peso, propagando o erro de volta pelas camadas |
| **Otimizador (optimizer)** | Regra de atualização dos pesos usando o gradiente (SGD, Adam, RMSprop) |

⚠️ **Pegadinha:** sem função de ativação **não-linear**, uma rede com várias camadas se comporta matematicamente como **uma única camada linear** — é a não-linearidade que dá à rede o poder de aprender padrões complexos.

### 2.1 Funções de Ativação — tabela de referência

| Função | Uso comum | Observação |
|---|---|---|
| **ReLU** | Camadas ocultas (padrão atual) | Rápida, mas sofre do problema de "neurônios mortos" (dying ReLU) |
| **Sigmoid** | Saída de classificação binária | Sofre de "vanishing gradient" em redes profundas |
| **Tanh** | Camadas ocultas (mais raro hoje) | Saída entre -1 e 1, também sofre vanishing gradient |
| **Softmax** | Saída de classificação multiclasse | Converte saídas em distribuição de probabilidade que soma 1 |

---

## 3. Problemas Clássicos de Treinamento (muito cobrados)

### 3.1 Vanishing e Exploding Gradients
- **Vanishing gradient:** em redes muito profundas, os gradientes ficam cada vez menores conforme retropropagam, praticamente "zerando" nas primeiras camadas → elas quase não aprendem.
- **Exploding gradient:** o oposto — gradientes crescem descontroladamente, causando instabilidade no treino.

**Soluções comuns:** ativação ReLU (mitiga vanishing), **normalização em lote (Batch Normalization)**, **inicialização adequada dos pesos** (Xavier/He), **conexões residuais (ResNet)**, **gradient clipping** (para exploding).

⚠️ **Pegadinha:** achar que só redes recorrentes (RNN) sofrem vanishing gradient — **qualquer** rede muito profunda pode sofrer, mas é especialmente crítico em RNNs por causa da retropropagação **através do tempo** (BPTT).

### 3.2 Overfitting em Redes Profundas
Redes profundas têm **muitos parâmetros** e alta capacidade de memorizar o treino.

**Técnicas de regularização:**
- **Dropout:** desativa aleatoriamente uma fração dos neurônios durante o treino, forçando a rede a não depender excessivamente de neurônios específicos.
- **Regularização L1/L2** nos pesos (igual ao ML clássico).
- **Data Augmentation:** gera variações artificiais dos dados de treino (rotação, corte, ruído) para aumentar a diversidade sem coletar mais dados reais.
- **Early Stopping:** interrompe o treino quando a perda de validação para de melhorar.
- **Batch Normalization:** também tem efeito regularizador secundário, além de estabilizar o treino.

---

## 4. Principais Arquiteturas

### 4.1 MLP (Multilayer Perceptron / Feedforward)
- Arquitetura mais básica: camadas totalmente conectadas (*fully connected/dense*).
- Boa para dados **tabulares**, mas não captura bem estrutura espacial (imagem) ou sequencial (texto/série temporal).

### 4.2 CNN (Convolutional Neural Network)
- Especializada em dados com **estrutura espacial** (imagens, principalmente).
- **Camada convolucional:** aplica filtros (kernels) que detectam padrões locais (bordas, texturas), preservando relações espaciais.
- **Camada de pooling:** reduz a dimensionalidade espacial (ex.: max pooling), tornando a rede mais eficiente e um pouco mais robusta a pequenas translações.
- Vantagem central: **compartilhamento de pesos** entre regiões da imagem → muito menos parâmetros do que uma MLP equivalente.

⚠️ **Pegadinha:** achar que CNN só serve para imagem — também é usada em **séries temporais e texto** (CNN 1D), sempre que houver padrões locais relevantes.

### 4.3 RNN, LSTM e GRU (dados sequenciais)
- **RNN (Recurrent Neural Network):** processa sequências mantendo um "estado oculto" que carrega informação dos passos anteriores.
- Sofre fortemente de **vanishing gradient** em sequências longas → dificuldade de capturar dependências de longo prazo.
- **LSTM (Long Short-Term Memory)** e **GRU (Gated Recurrent Unit):** variantes com **mecanismos de "portões" (gates)** que controlam o que é lembrado e esquecido, mitigando o vanishing gradient.

⚠️ **Pegadinha:** LSTM/GRU **não eliminam totalmente** o problema de dependências de longuíssimo prazo, apenas o **atenuam** — foi justamente essa limitação residual que motivou o surgimento dos **Transformers**.

### 4.4 Transformers (arquitetura dominante atual)
- Baseados no mecanismo de **atenção (self-attention)**, que permite ao modelo pesar a importância de **todos os elementos da sequência simultaneamente**, sem depender de processamento sequencial passo a passo (como RNN).
- Vantagem central: **paralelização** no treino (muito mais rápido que RNN) e melhor captura de dependências de longo alcance.
- Base dos LLMs modernos (GPT, Claude, BERT etc.).

⚠️ **Pegadinha:** self-attention **não tem noção inerente de ordem/posição** — por isso os Transformers precisam de **positional encoding** (codificação posicional) adicionada explicitamente às entradas.

### 4.5 Autoencoders e GANs (generativos)
- **Autoencoder:** aprende a comprimir (encoder) e reconstruir (decoder) dados — usado em redução de dimensionalidade e detecção de anomalias (não-supervisionado).
- **GAN (Generative Adversarial Network):** dois modelos competindo — o **Gerador** cria dados falsos, o **Discriminador** tenta distinguir reais de falsos. O treino é um **jogo adversarial** que melhora ambos simultaneamente.
- **VAE (Variational Autoencoder):** versão probabilística do autoencoder, gera novas amostras a partir do espaço latente aprendido.

⚠️ **Pegadinha:** confundir o objetivo do Gerador e do Discriminador na GAN — o **Gerador** quer **enganar** o Discriminador (minimizar a capacidade dele de identificar dados falsos); o **Discriminador** quer **acertar** (maximizar sua capacidade de distinguir real de falso). É um jogo **minimax**.

---

## 5. Otimizadores

| Otimizador | Característica |
|---|---|
| **SGD (Stochastic Gradient Descent)** | Atualização simples com base no gradiente de um mini-batch |
| **SGD com Momentum** | Acumula uma "inércia" das atualizações anteriores, suavizando o caminho até o mínimo |
| **RMSprop** | Adapta a taxa de aprendizado por parâmetro, baseado na média dos gradientes recentes |
| **Adam** | Combina Momentum + RMSprop; padrão mais usado atualmente por convergir rápido e ser robusto |

⚠️ **Pegadinha:** **taxa de aprendizado (learning rate)** muito alta → o treino diverge/oscila sem convergir; muito baixa → treino extremamente lento ou fica preso em mínimos locais ruins.

---

## 6. Métricas de Avaliação

Aqui vale um ponto **importante de prova**: Deep Learning **não tem métricas exclusivas** — como é uma classe de modelos, ele **usa as métricas do paradigma em que está sendo aplicado** (classificação, regressão, geração, etc.), mas com algumas particularidades práticas de monitoramento.

### 6.1 Métricas herdadas do paradigma
- **Classificação (CNN/Transformer classificador):** Acurácia, Precisão, Recall, F1, AUC-ROC (iguais ao ML supervisionado clássico).
- **Regressão:** MAE, MSE, RMSE, R².
- **Geração de texto (LLMs):** **Perplexidade** (quão "surpreso" o modelo fica com o texto real — menor é melhor), **BLEU/ROUGE** (comparação com texto de referência, comuns em tradução/resumo).
- **Geração de imagem (GANs):** **FID (Fréchet Inception Distance)** — mede a similaridade estatística entre distribuição de imagens geradas e reais (menor é melhor).

### 6.2 Métricas/curvas específicas de monitoramento de treino
- **Curva de perda (loss curve):** perda de treino vs. perda de validação por época.
- **Curva de aprendizado (learning curve):** ajuda a diagnosticar overfitting/underfitting.

⚠️ **Pegadinha número 1 (muito cobrada):** interpretar a curva de perda —
- Perda de **treino cai, perda de validação sobe/estagna** → **overfitting**.
- Ambas as perdas **altas e não caem** → **underfitting** (modelo simples demais ou taxa de aprendizado inadequada).
- Ambas caem e convergem próximas → modelo generalizando bem.

⚠️ **Pegadinha número 2:** usar apenas a **acurácia final** para julgar um modelo de deep learning sem observar a **curva de treino** — dois modelos podem ter acurácia final parecida, mas um pode estar **memorizando** (overfit tardio ainda não visível no conjunto de teste usado) enquanto o outro generaliza de forma mais robusta.

---

## 7. Transfer Learning e Fine-Tuning (tópico prático muito cobrado)

- **Transfer Learning:** reaproveitar um modelo **pré-treinado** em uma tarefa/dataset grande (ex.: ImageNet, corpora massivos de texto) e adaptá-lo para uma tarefa nova, geralmente com menos dados.
- **Fine-tuning:** ajustar (retreinar total ou parcialmente) os pesos do modelo pré-treinado na nova tarefa.
- **Feature extraction (congelamento):** usar o modelo pré-treinado só para extrair representações, treinando apenas uma camada final nova, mantendo o resto **congelado**.

⚠️ **Pegadinha:** achar que fine-tuning sempre significa retreinar **toda** a rede — na prática, é comum congelar as primeiras camadas (que aprendem features genéricas, como bordas em imagens) e treinar apenas as últimas camadas (mais específicas da tarefa).

---

## 8. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Dado com estrutura espacial (imagem) | CNN |
| Dado sequencial com dependência de longo prazo | LSTM/GRU, ou melhor ainda, Transformer |
| Modelo sem noção de ordem na sequência | Transformer precisa de positional encoding |
| Gradientes desaparecendo em rede profunda | Vanishing gradient → ReLU, BatchNorm, ResNet |
| Reduzir overfitting em rede neural | Dropout, Data Augmentation, Early Stopping, L1/L2 |
| Rede com poucos parâmetros para imagem | CNN (compartilhamento de pesos) |
| Jogo entre dois modelos competindo | GAN (Gerador vs. Discriminador) |
| Poucos dados disponíveis para treinar do zero | Transfer Learning / Fine-tuning |
| Avaliar qualidade de texto gerado | Perplexidade, BLEU, ROUGE |
| Avaliar qualidade de imagem gerada | FID |
| Diagnosticar overfitting durante o treino | Curva de perda treino vs. validação |

---

## 9. Aplicação Profissional (além da prova)

- **Visão computacional:** CNNs para diagnóstico por imagem médica, inspeção de qualidade industrial, veículos autônomos.
- **NLP/LLMs:** Transformers para chatbots, tradução automática, sumarização, geração de código (a arquitetura por trás de modelos como o Claude).
- **Geração de conteúdo:** GANs/Diffusion Models para geração de imagens sintéticas, upscaling, remoção de ruído.
- **Séries temporais:** LSTM/Transformer para previsão de demanda, detecção de anomalias em sensores industriais (IoT).
- Na prática profissional, boa parte do trabalho **não é criar arquiteturas do zero**, e sim fazer **fine-tuning de modelos pré-treinados**, otimizar hiperparâmetros (learning rate, batch size) e cuidar de infraestrutura de treino (GPUs, custo computacional) — pontos que também aparecem em entrevistas técnicas de ML/DL.

---

## 10. Perguntas típicas de prova (para se testar)

1. Por que sem função de ativação não-linear uma rede profunda "colapsa" em um modelo linear equivalente?
2. Explique o problema de vanishing gradient e cite duas técnicas para mitigá-lo.
3. Qual a principal vantagem do Transformer sobre a RNN/LSTM para sequências longas?
4. Por que o Gerador e o Discriminador de uma GAN têm objetivos opostos? Descreva o jogo minimax.
5. Como interpretar um gráfico onde a perda de treino continua caindo, mas a perda de validação começa a subir?
6. Qual a diferença entre transfer learning com "feature extraction" (congelamento) e fine-tuning completo?
