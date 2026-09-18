# Processamento de Linguagem Natural (PLN) e Modelos de Linguagem
## Conceitos, Modelos e Métricas de Avaliação — Material de Estudo

---

## 1. Conceito Central

**Processamento de Linguagem Natural (PLN/NLP)** é o campo da IA dedicado a fazer com que computadores **compreendam, interpretem e gerem linguagem humana** (texto ou fala) de forma útil.

> **Definição de prova:** "PLN combina linguística computacional com aprendizado de máquina para lidar com a **ambiguidade, informalidade e variabilidade** inerentes à linguagem humana — desafios que não existem (ou são bem menores) em dados estruturados/tabulares."

⚠️ **Pegadinha clássica de prova:** achar que PLN é sinônimo de "usar um LLM". PLN é um campo **muito mais amplo**, que inclui desde tarefas clássicas com regras/estatística (ex.: correção ortográfica baseada em regras) até os modelos de linguagem modernos baseados em Transformers — os LLMs são apenas o **estado da arte atual**, não a definição do campo.

---

## 2. Pipeline Clássico de Pré-Processamento de Texto

| Etapa | O que faz | Exemplo |
|---|---|---|
| **Tokenização** | Divide o texto em unidades menores (tokens: palavras, subpalavras ou caracteres) | "gato preto" → ["gato", "preto"] |
| **Normalização** | Padroniza o texto (minúsculas, remoção de acentos/pontuação) | "Gato!" → "gato" |
| **Remoção de stopwords** | Remove palavras de baixo valor semântico e alta frequência | remover "de", "o", "e" |
| **Stemming** | Reduz a palavra ao seu radical, de forma **bruta/heurística** (corte de sufixos) | "correndo", "correu" → "corr" |
| **Lematização (lemmatization)** | Reduz a palavra à sua **forma canônica/dicionário**, usando conhecimento linguístico | "correndo", "correu" → "correr" |
| **POS Tagging** | Marca a classe gramatical de cada token | "gato" → substantivo |
| **NER (Named Entity Recognition)** | Identifica entidades nomeadas no texto | "Sócrates viveu em Atenas" → Pessoa: Sócrates; Local: Atenas |

⚠️ **Pegadinha número 1 (a mais cobrada desta seção):** confundir **stemming** com **lematização**.
- **Stemming** é um processo **heurístico e bruto**, que pode gerar radicais que **não são palavras reais** (ex.: "melhor" → "melhor", mas "estudando" pode virar "estud" — não é uma palavra válida).
- **Lematização** usa **análise morfológica/dicionário** e sempre retorna uma **palavra real e válida** (o lema/forma canônica), sendo mais precisa, porém mais custosa computacionalmente.

---

## 3. Representações de Texto (da mais simples à mais sofisticada)

### 3.1 Bag of Words (BoW)
- Representa um texto como um **vetor de contagem de palavras**, ignorando completamente a ordem e o contexto.

### 3.2 TF-IDF (Term Frequency – Inverse Document Frequency)
- Pondera a frequência de um termo em um documento (**TF**) pela **raridade** desse termo no corpus geral (**IDF**) — termos muito comuns em todos os documentos (ex.: "o", "de") recebem peso baixo; termos raros e discriminativos recebem peso alto.

⚠️ **Pegadinha:** tanto BoW quanto TF-IDF **não capturam semântica nem contexto** — "banco" (instituição financeira) e "banco" (assento) são tratados como o **mesmo token idêntico**, e frases com as mesmas palavras em ordens diferentes podem gerar representações muito parecidas mesmo com significados distintos.

### 3.3 Word Embeddings Estáticos (Word2Vec, GloVe, FastText)
- Representam palavras como **vetores densos** em um espaço contínuo, capturando relações semânticas (palavras com significados parecidos ficam próximas no espaço vetorial).
- **Word2Vec** tem duas arquiteturas principais:
  - **CBOW (Continuous Bag of Words):** prevê a palavra central a partir do contexto ao redor.
  - **Skip-gram:** prevê as palavras de contexto a partir da palavra central (geralmente melhor para palavras raras).

**Exemplo clássico de analogia vetorial:** rei − homem + mulher ≈ rainha (relações semânticas capturadas geometricamente).

⚠️ **Pegadinha número 1 (muito cobrada):** Word2Vec/GloVe geram um **único vetor fixo por palavra**, independente do contexto de uso — são chamados de **embeddings estáticos**. Isso significa que a palavra "banco" tem **exatamente o mesmo vetor** em "fui ao banco sacar dinheiro" e "sentei no banco da praça", o que é uma limitação importante (problema da **polissemia**) que motivou o desenvolvimento dos **embeddings contextuais**.

### 3.4 Embeddings Contextuais (ELMo, BERT e sucessores)
- Geram uma representação vetorial **diferente para a mesma palavra**, dependendo do **contexto da frase** em que ela aparece — resolvendo o problema da polissemia dos embeddings estáticos.

⚠️ **Pegadinha:** essa é a principal diferença conceitual entre a geração de embeddings "pré-Transformer" (estáticos) e "pós-Transformer" (contextuais) — muito cobrada como pergunta de "o que mudou com o BERT em relação ao Word2Vec".

---

## 4. Modelos de Linguagem (Language Models)

### 4.1 Definição
- Um **modelo de linguagem** estima a **probabilidade de uma sequência de palavras/tokens**, ou, mais especificamente, a **probabilidade do próximo token dado os anteriores**: P(wₙ | w₁, w₂, ..., wₙ₋₁).

### 4.2 Modelos de N-gramas (abordagem clássica, pré-neural)
- Estimam a probabilidade do próximo token considerando apenas uma **janela fixa dos N tokens anteriores** (ex.: bigrama considera 1 token anterior, trigrama considera 2).

⚠️ **Pegadinha:** modelos de N-gramas sofrem do problema de **esparsidade** (muitas combinações de N palavras nunca aparecem no corpus de treino) e têm **memória de contexto muito limitada** — não capturam dependências de longo alcance, o que foi uma das motivações para modelos neurais (RNN/LSTM) e, depois, Transformers.

### 4.3 Modelos Neurais Sequenciais (RNN/LSTM) — ver material de Deep Learning
- Processam o texto token a token, mantendo um estado oculto — mas sofrem de vanishing gradient em sequências longas (ver material de Deep Learning para detalhes).

### 4.4 Transformers e a Arquitetura de LLMs Modernos
- Baseados no mecanismo de **self-attention** (ver material de Deep Learning), permitindo capturar dependências entre **todos os tokens da sequência simultaneamente**, sem o gargalo sequencial das RNNs.

**Duas grandes famílias de arquitetura de Transformer, muito cobradas em prova:**

| Arquitetura | Direção da atenção | Objetivo de treino típico | Exemplos | Uso típico |
|---|---|---|---|---|
| **Encoder-only** | Bidirecional (vê o texto inteiro de uma vez) | Masked Language Modeling (prever palavras "mascaradas" no meio do texto) | BERT, RoBERTa | Classificação, NER, busca semântica, compreensão de texto |
| **Decoder-only** | Unidirecional/autoregressiva (só "vê" tokens anteriores) | Predição do próximo token (autoregressive) | GPT, Claude, LLaMA | Geração de texto, chatbots, assistentes |
| **Encoder-decoder** | Encoder bidirecional + decoder autoregressivo | Sequence-to-sequence (traduzir, resumir) | T5, BART | Tradução, sumarização |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a unidade de LLMs):** confundir a natureza do **BERT** com a dos **GPT/Claude/LLaMA**.
- **BERT (encoder-only)** é **bidirecional**: enxerga o contexto **à esquerda e à direita** simultaneamente, sendo excelente para **compreensão** (classificação, extração), mas **não foi desenhado nativamente para gerar texto longo de forma autoregressiva**.
- **GPT-like (decoder-only)** é **unidirecional/causal**: em cada passo, só "enxerga" os tokens **anteriores**, o que é exatamente o que permite a **geração** de texto token a token — mas, em compensação, não tem acesso bidirecional ao contexto durante a geração.

⚠️ **Pegadinha número 2:** self-attention **não tem noção inerente de ordem** dos tokens — por isso Transformers precisam de **positional encoding** (codificação posicional) somada às entradas, para que o modelo saiba a posição relativa/absoluta de cada token na sequência.

### 4.5 Tokenização em LLMs modernos — subword tokenization
- LLMs modernos não tokenizam por **palavra inteira** nem por **caractere único**, mas por **subpalavras (subword tokens)**, usando algoritmos como **BPE (Byte Pair Encoding)** ou **WordPiece**.

⚠️ **Pegadinha:** a tokenização por subpalavras resolve o problema de **vocabulário aberto (out-of-vocabulary)** — palavras raras, neologismos ou erros de digitação podem ser decompostos em subpartes conhecidas (ex.: "PLNzinho" → "PLN" + "zinho"), em vez de serem tratadas como um token totalmente desconhecido, como aconteceria em uma tokenização estritamente por palavra inteira.

---

## 5. Adaptação de Modelos: Fine-tuning, Prompting e RAG

| Técnica | O que faz | Atualiza os pesos do modelo? |
|---|---|---|
| **Fine-tuning** | Retreina (total ou parcialmente) os pesos do modelo pré-treinado em uma tarefa/domínio específico | **Sim** |
| **Prompt Engineering / In-context learning** | Formula a entrada (prompt) de forma a guiar o modelo a produzir a saída desejada, incluindo exemplos (few-shot) diretamente no prompt | **Não** |
| **RAG (Retrieval-Augmented Generation)** | Busca informações relevantes em uma base externa e as insere no contexto antes de gerar a resposta | **Não** (o modelo em si não é retreinado; a base de conhecimento é externa) |

⚠️ **Pegadinha número 1 (muito cobrada):** achar que **prompt engineering "ensina"** o modelo permanentemente. Técnicas como **few-shot prompting** (dar exemplos dentro do próprio prompt) melhoram a resposta **apenas para aquela interação específica** — **não alteram os pesos do modelo**, diferente do fine-tuning, que modifica os parâmetros de forma persistente.

⚠️ **Pegadinha número 2:** RAG é frequentemente confundido com fine-tuning como forma de "adicionar conhecimento novo" ao modelo. RAG é geralmente **preferível** quando a informação muda com frequência ou precisa ser **rastreável/auditável** (a fonte pode ser citada), pois não exige retreinar o modelo a cada atualização de dados.

### 5.1 RLHF (Reinforcement Learning from Human Feedback)
- Técnica (já abordada no material de Aprendizado por Reforço) usada para **alinhar** o comportamento de LLMs às preferências humanas, usando avaliações humanas como sinal de recompensa em um processo de RL.

---

## 6. Métricas de Avaliação em PLN

### 6.1 Perplexidade (Perplexity)
- Mede o quão "surpreso" o modelo fica ao prever o próximo token em um texto real — **quanto menor, melhor** (o modelo atribui alta probabilidade às sequências corretas).

⚠️ **Pegadinha:** perplexidade **não é diretamente comparável entre modelos com vocabulários/tokenizadores diferentes** — comparar a perplexidade de dois modelos com tokenizações distintas pode ser enganoso.

### 6.2 BLEU vs. ROUGE (a comparação mais cobrada desta seção)

| Métrica | Baseada em... | Uso típico | Característica |
|---|---|---|---|
| **BLEU** (Bilingual Evaluation Understudy) | **Precisão** de n-gramas (quanto do texto gerado aparece na referência) | Tradução automática | Penaliza textos gerados muito curtos (usa "brevity penalty") |
| **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) | **Recall** de n-gramas (quanto da referência aparece no texto gerado) | Sumarização automática | Foca em quanta informação da referência foi capturada |

⚠️ **Pegadinha número 1 (super cobrada):** trocar BLEU por ROUGE na explicação — **BLEU é baseado em precisão** (adequado quando o risco maior é o modelo "inventar" conteúdo que não está na referência, como em tradução), enquanto **ROUGE é baseado em recall** (adequado quando o risco maior é o modelo "esquecer" informação importante da referência, como em sumarização).

### 6.3 Outras métricas relevantes
- **F1-Score:** usado em tarefas como NER e QA (Question Answering), combinando precisão e recall na identificação de entidades/respostas corretas.
- **Acurácia:** usada em tarefas de classificação de texto (ex.: análise de sentimento).
- **Avaliação humana:** para qualidade de geração de texto aberta (coerência, fluência, relevância), métricas automáticas são limitadas, e **avaliação humana** (ou LLM-as-a-judge) continua sendo referência importante.

⚠️ **Pegadinha:** métricas automáticas como BLEU e ROUGE **medem sobreposição lexical (n-gramas)**, não **qualidade semântica real** — um texto pode ser semanticamente equivalente à referência, mas usar palavras diferentes, e ainda assim receber uma pontuação baixa nessas métricas (uma limitação importante e cobrada em prova).

---

## 7. Alucinação (Hallucination) — tópico central em LLMs modernos

- **Alucinação** é quando um LLM gera informação **plausível na forma, mas factualmente incorreta ou inventada**, apresentada com o mesmo nível de confiança de uma informação correta.

⚠️ **Pegadinha:** alucinação **não é um "bug" pontual e raro** — é uma consequência **estrutural** da forma como LLMs geram texto (prevendo o token estatisticamente mais provável, sem um mecanismo interno de verificação factual nativo). Técnicas como RAG e fine-tuning ajudam a **mitigar**, mas não **eliminam** completamente o problema.

---

## 8. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Reduzir palavra a um radical bruto, sem garantia de ser palavra real | Stemming |
| Reduzir palavra à forma de dicionário, linguisticamente válida | Lematização |
| Representação que ignora ordem e contexto das palavras | Bag of Words / TF-IDF |
| Vetor fixo por palavra, mesmo em contextos diferentes | Embedding estático (Word2Vec, GloVe) |
| Vetor que muda conforme o contexto da frase | Embedding contextual (BERT e sucessores) |
| Modelo bidirecional, ótimo para classificação/NER | BERT (encoder-only) |
| Modelo unidirecional/autoregressivo, ótimo para gerar texto | GPT-like (decoder-only) |
| Resolver a falta de noção de ordem no self-attention | Positional encoding |
| Resolver problema de vocabulário aberto (palavras raras) | Tokenização por subpalavras (BPE, WordPiece) |
| Melhorar resposta sem alterar pesos do modelo | Prompt engineering / few-shot / RAG |
| Alterar pesos do modelo de forma persistente | Fine-tuning |
| Métrica de precisão de n-gramas, usada em tradução | BLEU |
| Métrica de recall de n-gramas, usada em sumarização | ROUGE |
| Modelo "inventa" informação com confiança | Alucinação (limitação estrutural, não só "erro raro") |

---

## 9. Aplicação Profissional

- **Chatbots e assistentes virtuais:** modelos decoder-only (GPT-like) para geração conversacional.
- **Busca semântica e sistemas de recomendação de conteúdo:** embeddings (estáticos ou contextuais) para encontrar textos semanticamente similares, mesmo sem sobreposição exata de palavras.
- **Extração de informação em documentos jurídicos/médicos:** NER e modelos encoder-only (BERT e variantes) para identificar entidades e classificar trechos.
- **Sistemas de RAG corporativos:** combinação de busca em bases de conhecimento internas (documentos, políticas, manuais) com LLMs para reduzir alucinação e permitir respostas rastreáveis/citáveis.
- **Moderação e classificação de conteúdo:** classificação de texto (spam, toxicidade, sentimento) usando desde modelos clássicos (TF-IDF + regressão logística) até fine-tuning de modelos Transformer, dependendo da complexidade e do volume de dados.
- Na prática profissional, uma decisão comum e frequentemente mal avaliada é **"fine-tuning vs. RAG vs. prompt engineering"** para adicionar conhecimento específico a um LLM — a escolha depende de fatores como frequência de atualização da informação, necessidade de rastreabilidade da fonte, orçamento computacional e volume de dados de treino disponível.

---

## 10. Perguntas típicas de prova (para se testar)

1. Qual a diferença entre stemming e lematização? Por que o stemming pode gerar radicais que não são palavras válidas?
2. Por que os embeddings gerados pelo Word2Vec são chamados de "estáticos", e qual limitação isso gera para palavras polissêmicas (ex.: "banco")?
3. Explique a diferença estrutural entre BERT (encoder-only) e GPT (decoder-only) em termos de direção da atenção e objetivo de treinamento.
4. Por que os Transformers precisam de positional encoding, diferente das RNNs?
5. Explique a diferença entre BLEU e ROUGE, indicando em qual cenário (tradução ou sumarização) cada uma é mais apropriada e por quê.
6. Por que prompt engineering (few-shot prompting) não é equivalente a fine-tuning, mesmo quando ambos melhoram a resposta do modelo para uma tarefa específica?
