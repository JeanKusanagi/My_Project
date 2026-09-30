# Simulado: Processamento de Linguagem Natural (PLN) e Modelos de Linguagem

**Instruções:**
* Responda às 30 questões de múltipla escolha (A, B, C, D ou E).
* Cada questão possui apenas uma alternativa correta.
* Preste atenção aos detalhes conceituais para não cair nas "pegadinhas".
* Ao final do teste, consulte o gabarito comentado para aprofundar seu aprendizado.

---

## Questões

### Questão 1 (Fácil)
O processo de redução de uma palavra à sua forma base ou raiz conceitual, utilizando análise morfológica completa e dicionários para garantir que a forma resultante seja uma palavra válida na língua, é denominado:

A) Stemming  
B) Lemmatization (Lematização)  
C) Tokenization (Tokenização)  
D) Part-of-Speech Tagging (POS Tagging)  
E) Parsing Sintático  

**Resposta Correta: B**
* **Comentário:** A **Lematização** (*Lemmatization*) utiliza dicionários e análise morfológica/gramatical para reduzir uma palavra ao seu lema oficial (ex: "correndo", "correu" $\rightarrow$ "correr"). O *Stemming* (A) apenas corta os afixos de forma heurística, muitas vezes gerando palavras inexistentes (ex: "assimilação" $\rightarrow$ "assimil").

---

### Questão 2 (Médio - *Pegadinha*)
Considere um modelo n-gram com $n=3$ (Trigram). Ao calcular a probabilidade da palavra $w_i$ dada a sequência antecedente $w_1, w_2, \dots, w_{i-1}$, o modelo Trigram assume a propriedade de Markov de qual ordem?

A) Ordem 3, pois considera 3 palavras no cálculo total da probabilidade condicional.  
B) Ordem 2, pois a probabilidade depende apenas das 2 palavras imediatamente anteriores.  
C) Ordem 1, pois depende apenas da transição de estado da palavra atual.  
D) Ordem 0, pois os modelos n-gram são estocásticos e independentes de contexto.  
E) Ordem $n+1$, no caso Ordem 4, devido aos tokens especiais de início de frase.  

**Resposta Correta: B**
* **Comentário:** *Pegadinha clássica!* Um modelo $n$-gram com $n=3$ considera sequências de 3 palavras ($w_{i-2}, w_{i-1}, w_i$). A probabilidade condicional é $P(w_i | w_{i-2}, w_{i-1})$. Como a previsão depende das **2** palavras anteriores, a propriedade de Markov é de **Ordem $n-1$**, ou seja, **Ordem 2**.


---

### Questão 3 (Difícil)
Na arquitetura Transformer original (*Attention Is All You Need*), a função de Atenção por Produto Escalar Escalado (*Scaled Dot-Product Attention*) divide o produto matricial $Q K^T$ por $\sqrt{d_k}$. Qual é o principal motivo matemático para a inclusão desse fator de escala $\sqrt{d_k}$?

A) Evitar que a complexidade computacional cresça de forma quadrática com o tamanho da sequência.  
B) Garantir que a matriz resultante seja estritamente ortogonal e inversível.  
C) Impedir que, para valores grandes de $d_k$, os produtos escalares cresçam muito em magnitude, empurrando a função Softmax para regiões de gradiente extremamente pequeno (saturação).  
D) Normalizar os vetores de Embeddings de posição para que tenham média zero e variância unitária.  
E) Permitir que a função de atenuação limite os pesos das palavras mais distantes no texto.  

**Resposta Correta: C**
* **Comentário:** Para dimensões grandes $d_k$, o produto escalar $Q K^T$ tende a produzir valores com magnitudes muito elevadas. Quando aplicados à função Softmax, esses valores grandes empurram a Softmax para regiões com gradientes extremamente pequenos (platôs/saturação), causando o problema do desaparecimento do gradiente durante o treino. A divisão por $\sqrt{d_k}$ escala a variância para 1.

---

### Questão 4 (Médio)
Qual das alternativas abaixo descreve corretamente a principal diferença entre os embeddings estáticos como Word2Vec (Skip-gram/CBOW) e os embeddings contextuais como BERT ou GPT?

A) O Word2Vec produz vetores dinâmicos ajustados no momento da inferência, enquanto o BERT possui uma tabela fixa (lookup table) pré-computada para cada palavra.  
B) O Word2Vec atribui uma única representação vetorial fixa para um determinado token, independentemente do contexto; já os modelos contextuais geram representações que variam de acordo com a vizinhança da palavra na frase.  
C) O Word2Vec opera exclusivamente ao nível de subpalavras (subwords), enquanto os modelos contextuais utilizam obrigatoriamente dicionários de palavras inteiras.  
D) Modelos contextuais não utilizam produtos escalares para medir similaridade de cosseno, ao passo que o Word2Vec depende inteiramente disso.  
E) O Word2Vec exige a arquitetura Transformer para ser treinado, enquanto BERT e GPT usam redes recorrentes bidirecionais (BiLSTM).  

**Resposta Correta: B**
* **Comentário:** Em arquiteturas estáticas (Word2Vec, GloVe), a palavra "manga" possui uma única representação vetorial, seja no sentido de fruta ou parte da camisa. Já em arquiteturas contextuais (BERT, GPT), o vetor de saída para "manga" é calculado considerando todas as outras palavras da frase, gerando representações dinâmicas e contextuais.

---

### Questão 5 (Fácil)
A métrica BLEU (*Bilingual Evaluation Understudy*) é amplamente utilizada para avaliar sistemas de:

A) Classificação de sentimentos em redes sociais.  
B) Reconhecimento de Entidades Nomeadas (NER).  
C) Tradução Automática e geração de texto comparada a referências humanas.  
D) Agrupamento não supervisionado de documentos (Topic Modeling).  
E) Extração de sintaxe e dependências gramaticais.  

**Resposta Correta: C**
* **Comentário:** O **BLEU** (*Bilingual Evaluation Understudy*) mede a sobreposição de $n$-grams entre o texto gerado pela máquina e uma ou mais traduções de referência criadas por humanos, sendo o padrão clássico em Tradução Automática.

---

### Questão 6 (Difícil - *Pegadinha*)
Assinale a alternativa **INCORRETA** sobre os métodos de amostragem (sampling) utilizados no processo de decoding de Large Language Models (LLMs):

A) A técnica de *Temperature Scaling* ajusta a distribuição de probabilidade dividindo os *logits* antes da aplicação do Softmax.  
B) O *Top-k Sampling* seleciona as $k$ palavras com maior probabilidade e redistribui a probabilidade entre elas.  
C) O *Top-p Sampling* (também chamado de *Nucleus Sampling*) seleciona o menor conjunto de palavras cuja soma acumulada de probabilidades atinja o limiar $p$.  
D) Definir a Temperatura igual a $0.0$ transforma o decoding em uma amostragem estocástica puramente aleatória com distribuição uniforme sobre todo o vocabulário.  
E) Um valor alto de Temperatura ($> 1.0$) torna a distribuição de probabilidades mais "plana" (uniforme), aumentando a diversidade e a aleatoriedade do texto gerado.  

**Resposta Correta: D**
* **Comentário:** *Pegadinha!* Ao definir a Temperatura em $0.0$, o modelo **não** faz amostragem aleatória uniforme; na verdade, ele se torna puramente determinístico, equivale ao *Greedy Search* (sempre escolhe o token de maior probabilidade). Portanto, a afirmativa D é a **INCORRETA** (o que a questão pede).

---

### Questão 7 (Médio)
Qual é a principal função do mecanismo de Masked Language Modeling (MLM) no treinamento do modelo BERT?

A) Forçar o modelo a prever a próxima palavra da sequência, garantindo um aprendizado autoregressivo da esquerda para a direita.  
B) Permitir o treinamento bidirecional do encoder, onde o modelo aprende a prever tokens ocultados (mascarados) utilizando o contexto tanto à esquerda quanto à direita.  
C) Reduzir o tamanho do vocabulário removendo automaticamente palavras de parada (*stop words*).  
D) Implementar o mecanismo de atenuação causal para evitar o vazamento do futuro no decoder.  
E) Otimizar as projeções das matrizes $Q$, $K$ e $V$ via descida do gradiente estocástico com momentum.  

**Resposta Correta: B**
* **Comentário:** O BERT é um modelo baseado na arquitetura Encoder. Para aprender representações bidirecionais profundas sem "vazar" a palavra a ser prevista no treinamento, o objetivo de Masked Language Modeling (MLM) oculta aleatoriamente cerca de 15% dos tokens e força o modelo a prevê-los com base no contexto da esquerda e da direita simultaneamente.

---

### Questão 8 (Fácil)
O procedimento no qual um modelo de linguagem pré-treinado em uma grande quantidade de texto genérico é posteriormente adaptado em um dataset menor e específico de uma tarefa é conhecido como:

A) Zero-Shot Inference  
B) Fine-Tuning (Ajuste Fino)  
C) Tokenization BPE  
D) Data Augmentation  
E) Prompt Engineering  

**Resposta Correta: B**
* **Comentário:** **Fine-tuning** é o processo de pegar um modelo base já pré-treinado em um córpus massivo não supervisionado e atualizar seus pesos em um conjunto de dados supervisionado específico para uma determinada tarefa downstream.

---

### Questão 9 (Médio - *Pegadinha*)
A técnica de Byte-Pair Encoding (BPE) é amplamente utilizada para tokenização em LLMs modernos. Qual problema fundamental da tokenização baseada puramente em palavras inteiras a BPE resolve com eficiência?

A) O problema do desaparecimento do gradiente durante o backpropagation no tempo.  
B) O custo computacional quadrático do mecanismo de Self-Attention.  
C) O problema de Palavras Fora do Vocabulário (OOV - *Out-of-Vocabulary*) e a explosão do tamanho do vocabulário.  
D) A incapacidade das redes neurais de processarem dados numéricos sem normalização Z-score.  
E) A dependência de dados rotulados por linguistas humanos para tarefas de parsing gramatical.  

**Resposta Correta: C**
* **Comentário:** *Pegadinha!* A tokenização por palavras inteiras gera vocabulários gigantescos e falha totalmente com palavras não vistas no treino (OOV). A tokenização **Byte-Pair Encoding (BPE)** divide palavras raras ou compostas em subpalavras (subwords) ou até caracteres, garantindo que qualquer palavra possa ser representada com um vocabulário de tamanho fixo e razoável.

---

### Questão 10 (Difícil)
Em relação às arquiteturas de Transformers, qual é a diferença fundamental entre modelos **Encoder-only** (ex: BERT), **Decoder-only** (ex: família GPT) e **Encoder-Decoder** (ex: T5, BART)?

A) Modelos Encoder-only usam atenção causal; Decoder-only usam atenção bidirecional; Encoder-Decoder usam apenas atenção esparsa.  
B) Modelos Encoder-only processam a sequência com atenção bidirecional (ideal para análise/extração); Decoder-only utilizam máscara de atenção causal (ideal para geração autoregressiva); Encoder-Decoder combinam o processamento bidirecional da entrada com a geração autoregressiva da saída.  
C) Modelos Encoder-only só funcionam com embeddings estáticos; Decoder-only funcionam com embeddings contextuais; Encoder-Decoder usam apenas redes convolucionais.  
D) Modelos Decoder-only não utilizam a função Softmax em suas camadas de saída, ao contrário dos modelos Encoder-only.  
E) Não há diferença arquitetural real, apenas variação no número de camadas de Feed-Forward.  

**Resposta Correta: B**
* **Comentário:** 
  * **Encoder-only (ex: BERT):** Atenção bidirecional (vê todo o texto). Excelente para classificação e extração.
  * **Decoder-only (ex: GPT):** Atenção causal/unidirecional (só vê o passado). Excelente para geração autorregressiva.
  * **Encoder-Decoder (ex: T5):** Processa a entrada bidirecionalmente e gera a saída autoregressivamente. Ideal para tradução e sumarização.

---

### Questão 11 (Médio)
Na tarefa de Reconhecimento de Entidades Nomeadas (NER), o esquema de rotulagem BIO (ou IOB) é frequentemente utilizado. O que significam as siglas B, I e O nesse contexto?

A) Binary, Integer, Output  
B) Begin, Inside, Outside  
C) Base, Intermediate, Optimal  
D) Backward, Inward, Outward  
E) Block, Index, Object  

---

### Questão 12 (Difícil - *Pegadinha*)
Ao calcular a Perplexidade ($PP$) de um modelo de linguagem sobre uma sequência de teste, qual das seguintes afirmativas é **CORRETA**?

A) Quanto maior a Perplexidade, melhor é a capacidade de predição do modelo de linguagem.  
B) A Perplexidade é equivalente à exponencial da entropia cruzada (*cross-entropy loss*) média por token.  
C) A Perplexidade varia exclusivamente de $0.0$ a $1.0$, funcionando como uma porcentagem de precisão.  
D) A Perplexidade só pode ser calculada para modelos baseados em n-grams clássicos, sendo matematicamente indefinida em Transformers.  
E) A Perplexidade mede o tempo de inferência necessário em milissegundos para gerar um token.  

---

### Questão 13 (Médio)
A técnica de PEFT (*Parameter-Efficient Fine-Tuning*) conhecida como **LoRA** (*Low-Rank Adaptation*) reduz dramaticamente o número de parâmetros treináveis ao:

A) Quantizar os pesos do modelo de 16 bits para 4 bits usando tabelas de busca não lineares.  
B) Decompor a matriz de atualização de pesos $\Delta W$ no produto de duas matrizes de menor posto (rank inferior) $A$ e $B$.  
C) Congelar a camada de Atenção e treinar apenas as camadas de Feed-Forward da rede.  
D) Remover aleatoriamente 50% dos neurônios do modelo durante a fase de inferência.  
E) Transformar o modelo Transformer em uma rede recorrente LSTM equivalente.  

---

### Questão 14 (Fácil)
Qual das seguintes tarefas de PLN é um exemplo clássico de **Geração de Texto Conditional / Sequência para Sequência (Seq2Seq)**?

A) Análise de Sentimento de um tweet (Positivo / Negativo)  
B) Detecção de Spam em e-mails  
C) Tradução de um texto do Inglês para o Português  
D) Agrupamento de documentos por K-Means  
E) Classificação de tópicos jornalísticos  

---

### Questão 15 (Difícil)
O método RLHF (*Reinforcement Learning from Human Feedback*) é amplamente utilizado para alinhar LLMs com a intenção humana. O pipeline padrão do RLHF compreende três etapas principais. Qual é a ordem e constituição correta dessas etapas?

A) Pre-training supervisionado $\rightarrow$ Fine-tuning supervisionado (SFT) $\rightarrow$ Quantização.  
B) Supervised Fine-Tuning (SFT) $\rightarrow$ Treinamento de um Modelo de Recompensa (Reward Model) $\rightarrow$ Otimização da política via PPO (Proximal Policy Optimization).  
C) Treinamento PPO $\rightarrow$ Coleta de preferências $\rightarrow$ Masked Language Modeling.  
D) Fine-tuning com LoRA $\rightarrow$ Avaliação BLEU $\rightarrow$ Injeção de Prompts.  
E) Alinhamento Direct Preference Optimization (DPO) $\rightarrow$ Pre-training $\rightarrow$ SFT.  

---

### Questão 16 (Médio - *Pegadinha*)
Considere os modelos de embedding Word2Vec (Skip-gram e CBOW). Assinale a afirmação correta sobre a diferença operacional entre eles:

A) CBOW prevê uma palavra de contexto com base em uma palavra central; Skip-gram prevê a palavra central com base no contexto.  
B) CBOW prevê a palavra central a partir das palavras do contexto ao redor; Skip-gram prevê as palavras do contexto a partir de uma palavra central.  
C) O Skip-gram é infinitamente mais rápido de treinar do que o CBOW em grandes volumes de dados, mas apresenta desempenho pior para palavras raras.  
D) Ambos usam mecânica de atenção e dependem da ordem exata das palavras dentro da janela de contexto.  
E) CBOW utiliza matrizes de atenuação causais, enquanto Skip-gram utiliza recorrencia bidirecional.  

---

### Questão 17 (Médio)
Qual das alternativas apresenta uma limitação intrínseca clássica das redes Recorrentes simples (RNNs vanila) ao lidar com sequências longas de texto, que motivou a criação das LSTMs e posteriormente dos Transformers?

A) Falta de suporte para vocabulários com mais de 10.000 palavras.  
B) Problema do Desaparecimento ou Explosão do Gradiente (*Vanishing/Exploding Gradient*), que dificulta a captura de dependências de longo alcance.  
C) Impossibilidade de calcular a perda por Entropia Cruzada.  
D) Altíssima capacidade de paralelização durante o treinamento, o que estoura a memória da GPU.  
E) Necessidade infalível de aplicar tokenização por caracteres individuais.  

---

### Questão 18 (Fácil)
Em PLN, o processo de remoção de pontuações, conversão de todos os caracteres para letras minúsculas e eliminação de palavras muito frequentes que agregam pouco valor semântico (como "de", "a", "com", "em") faz parte da fase de:

A) Inferência Causal  
B) Pré-processamento e Limpeza de Texto  
C) RLHF  
D) Softmax Scaling  
E) Beam Search  

---

### Questão 19 (Difícil - *Pegadinha*)
Por que a arquitetura Transformer necessita de **Encodamento Posicional** (*Positional Encoding*) adicionado aos embeddings de entrada?

A) Porque as multiplicações de matrizes no mecanismo de Self-Attention são invariantes à ordem da sequência (permutação) se os tokens não contiverem informação sobre sua posição.  
B) Para garantir que o modelo saiba a classe gramatical de cada palavra (POS Tag).  
C) Porque sem o Positional Encoding o gradiente da função Softmax seria sempre zero.  
D) Para limitar a quantidade máxima de tokens que o modelo pode gerar na inferência.  
E) Porque o modelo Transformer processa o texto palavra por palavra sequencialmente no tempo, igual a uma RNN.  

---

### Questão 20 (Médio)
O conceito de **Hallucination** (Alucinação) em Large Language Models refere-se a:

A) Quando o modelo entra em um loop infinito gerando o mesmo token repetidamente.  
B) Quando o modelo gera informações plausíveis do ponto de vista sintático/fluência, porém incorretas, inventadas ou sem respaldo na realidade/contexto.  
C) O estouro da memória VRAM da placa de vídeo durante a geração de saídas longas.  
D) O tempo de latência excessivo na inferência decorrente de uma amostragem de alta temperatura.  
E) O erro gerado quando o prompt contém caracteres em outros idiomas.  

---

### Questão 21 (Médio)
A métrica ROUGE (especialmente ROUGE-N e ROUGE-L) é predominantemente utilizada para avaliar qual tipo de tarefa em PLN?

A) Análise de Sentimento  
B) Sumarização Automática de Textos  
C) Classificação de Spam  
D) Análise do tom de voz do usuário  
E) Estimativa do tamanho de vocabulário  

---

### Questão 22 (Difícil)
O método de busca **Beam Search** é utilizado no decoding de geração de texto. Como ele se diferencia da estratégia **Greedy Search** (Busca Gulosa)?

A) A Greedy Search explora todas as combinações possíveis no vocabulário de forma exaustiva (busca em largura total), enquanto o Beam Search escolhe aleatoriamente uma palavra.  
B) O Beam Search mantém a rastreabilidade de um número fixo $B$ (beam width) de sequências hipóteses mais prováveis a cada passo, enquanto a Greedy Search apenas seleciona o token de maior probabilidade individual no passo atual.  
C) A Greedy Search é imune a repetições de texto, ao passo que o Beam Search sempre gera frases idênticas.  
D) O Beam Search só funciona em modelos Encoder-only, e a Greedy Search apenas em modelos Decoder-only.  
E) Não há diferença prática; os termos são sinônimos para o algoritmo de amostragem por temperatura.  

---

### Questão 23 (Fácil)
O framework **RAG** (*Retrieval-Augmented Generation*) é uma arquitetura que melhora as respostas dos LLMs ao:

A) Recarregar os pesos da rede neural a cada nova pergunta feita pelo usuário.  
B) Buscar documentos/informações relevantes em uma base de conhecimento externa e incluí-los como contexto no prompt enviado ao LLM.  
C) Reduzir o número de camadas do modelo Transformer para acelerar a execução.  
D) Substituir o mecanismo de Self-Attention por busca em grafos.  
E) Treinar o modelo do zero usando apenas dados não estruturados da internet.  

---

### Questão 24 (Médio - *Pegadinha*)
Considere a tarefa de cálculo de similaridade de texto usando modelos como Word2Vec versus modelos como BERT. Qual das afirmativas abaixo é **VERDADEIRA** sobre a palavra "banco" nas frases:
1. *Fui ao **banco** pagar uma conta.*
2. *Sentei no **banco** do parque para descansar.*

A) Em ambos os modelos (Word2Vec e BERT), a palavra "banco" terá o exato mesmo vetor numérico de representação.  
B) No Word2Vec, a palavra "banco" terá o mesmo vetor em ambas as frases; no BERT, a palavra "banco" terá vetores representacionais diferentes devido à atenção contextual.  
C) No BERT, o vetor da palavra "banco" será idêntico, pois a tokenização BPE mapeia a mesma string para a mesma id de token antes da camada de atenção.  
D) O Word2Vec consegue diferenciar o sentido de "banco" porque analisa a gramática da frase sequencialmente através de portões de esquecimento.  
E) Em nenhum dos dois modelos é possível calcular a similaridade de cosseno entre vetores.  

---

### Questão 25 (Difícil)
Qual é a principal inovação da arquitetura **FlashAttention** em relação ao Self-Attention padrão do Transformer?

A) Ela substitui a operação de produto escalar por adições simples, alterando o resultado matemático final da atenção.  
B) Ela otimiza o acesso à memória (SRAM vs High Bandwidth Memory - HBM) na GPU através de tiling e recomputação no backward pass, reduzindo drasticamente o consumo de memória e acelerando a execução sem alterar o resultado matemático exato da atenção.  
C) Ela aplica quantização de 1-bit em todos os tensores de Query, Key e Value.  
D) Ela elimina a necessidade de treinar com GPUs, permitindo execução rápida apenas em CPUs.  
E) Ela converte a atenção em uma rede convolucional de uma dimensão.  

---

### Questão 26 (Médio)
Qual das seguintes alternativas define corretamente o conceito de **Zero-Shot Learning** no contexto de Large Language Models?

A) Capacidade do modelo de responder a uma tarefa sem ter sido atualizado com nenhum exemplo de treino específico para aquela tarefa através de fine-tuning.  
B) Treinamento do modelo sem utilizar nenhuma palavra (zerar os tokens).  
C) Executar a inferência mantendo a taxa de aprendizado (learning rate) em zero durante o pré-treinamento.  
D) Ajustar apenas a primeira camada da rede neural com zero épocas de treino.  
E) Treinar um modelo do zero utilizando hardware com zero latência.  

---

### Questão 27 (Difícil - *Pegadinha*)
Sobre a técnica de **Quantização** de LLMs (ex: GGUF, AWQ, GPTQ), assinale a afirmativa **CORRETA**:

A) A quantização aumenta o tamanho dos pesos do modelo para ter maior precisão matemática de ponto flutuante.  
B) A quantização de FP16 (16-bit float) para INT4 (4-bit integer) reduz drasticamente o uso de memória VRAM e acelera a inferência, contudo pode acarretar pequenas perdas de precisão no modelo.  
C) A quantização exige o retreinamento do modelo do zero durante vários meses em clusters de supercomputadores.  
D) Um modelo quantizado em 4 bits precisa de mais memória do que um modelo original de 16 bits para funcionar.  
E) A quantização impede que o modelo seja utilizado em sistemas de RAG.  

---

### Questão 28 (Fácil)
Qual das alternativas apresenta uma biblioteca de código aberto (*open-source*) em Python amplamente utilizada na comunidade científica e industrial para carregar, treinar e disponibilizar modelos de linguagem baseados em Transformers?

A) NumPy  
B) Hugging Face `transformers`  
C) Pandas  
D) Matplotlib  
E) Flask  

---

### Questão 29 (Médio)
Na avaliação de modelos de classificação de texto em PLN, o que representa a métrica **F1-Score**?

A) A média aritmética simples entre Acurácia e Perdas.  
B) A média harmônica entre a Precisão (Precision) e a Revocação (Recall).  
C) O tempo total de treinamento dividido pelo número de instâncias de teste.  
D) A probabilidade logarítmica da menor palavra do vocabulário.  
E) A porcentagem de erros cometidos no conjunto de validação.  

---

### Questão 30 (Difícil - *Pegadinha*)
Considere a técnica de **Chain-of-Thought (CoT) Prompting** (Cadeia de Pensamento). Qual das alternativas descreve melhor o seu funcionamento e o porquê de sua eficácia em tarefas de raciocínio complexo?

A) Ela altera diretamente os pesos da matriz de atenção do LLM via gradiente em tempo de inferência.  
B) Ela força o modelo a gerar passos intermediários de raciocínio antes de chegar à resposta final, permitindo que os tokens intermediários sirvam de "memória computacional/contextual" adicional durante o decoding autoregressivo.  
C) Ela comprime o contexto de entrada removendo verbos e adjetivos desnecessários do prompt.  
D) Ela é uma técnica usada exclusivamente para pré-treinar encoders BERT em textos acadêmicos.  
E) Ela garante 100% de precisão matemática sem possibilidade de erros em cálculos complexos.  

---

---

# Gabarito Comentado

### Questão 1
**Resposta Correta: B**
* **Comentário:** A **Lematização** (*Lemmatization*) utiliza dicionários e análise morfológica/gramatical para reduzir uma palavra ao seu lema oficial (ex: "correndo", "correu" $\rightarrow$ "correr"). O *Stemming* (A) apenas corta os afixos de forma heurística, muitas vezes gerando palavras inexistentes (ex: "assimilação" $\rightarrow$ "assimil").

---

### Questão 2
**Resposta Correta: B**
* **Comentário:** *Pegadinha clássica!* Um modelo $n$-gram com $n=3$ considera sequências de 3 palavras ($w_{i-2}, w_{i-1}, w_i$). A probabilidade condicional é $P(w_i | w_{i-2}, w_{i-1})$. Como a previsão depende das **2** palavras anteriores, a propriedade de Markov é de **Ordem $n-1$**, ou seja, **Ordem 2**.

---

### Questão 3
**Resposta Correta: C**
* **Comentário:** Para dimensões grandes $d_k$, o produto escalar $Q K^T$ tende a produzir valores com magnitudes muito elevadas. Quando aplicados à função Softmax, esses valores grandes empurram a Softmax para regiões com gradientes extremamente pequenos (platôs/saturação), causando o problema do desaparecimento do gradiente durante o treino. A divisão por $\sqrt{d_k}$ escala a variância para 1.

---

### Questão 4
**Resposta Correta: B**
* **Comentário:** Em arquiteturas estáticas (Word2Vec, GloVe), a palavra "manga" possui uma única representação vetorial, seja no sentido de fruta ou parte da camisa. Já em arquiteturas contextuais (BERT, GPT), o vetor de saída para "manga" é calculado considerando todas as outras palavras da frase, gerando representações dinâmicas e contextuais.

---

### Questão 5
**Resposta Correta: C**
* **Comentário:** O **BLEU** (*Bilingual Evaluation Understudy*) mede a sobreposição de $n$-grams entre o texto gerado pela máquina e uma ou mais traduções de referência criadas por humanos, sendo o padrão clássico em Tradução Automática.

---

### Questão 6
**Resposta Correta: D**
* **Comentário:** *Pegadinha!* Ao definir a Temperatura em $0.0$, o modelo **não** faz amostragem aleatória uniforme; na verdade, ele se torna puramente determinístico, equivale ao *Greedy Search* (sempre escolhe o token de maior probabilidade). Portanto, a afirmativa D é a **INCORRETA** (o que a questão pede).

---

### Questão 7
**Resposta Correta: B**
* **Comentário:** O BERT é um modelo baseado na arquitetura Encoder. Para aprender representações bidirecionais profundas sem "vazar" a palavra a ser prevista no treinamento, o objetivo de Masked Language Modeling (MLM) oculta aleatoriamente cerca de 15% dos tokens e força o modelo a prevê-los com base no contexto da esquerda e da direita simultaneamente.

---

### Questão 8
**Resposta Correta: B**
* **Comentário:** **Fine-tuning** é o processo de pegar um modelo base já pré-treinado em um córpus massivo não supervisionado e atualizar seus pesos em um conjunto de dados supervisionado específico para uma determinada tarefa downstream.

---

### Questão 9
**Resposta Correta: C**
* **Comentário:** *Pegadinha!* A tokenização por palavras inteiras gera vocabulários gigantescos e falha totalmente com palavras não vistas no treino (OOV). A tokenização **Byte-Pair Encoding (BPE)** divide palavras raras ou compostas em subpalavras (subwords) ou até caracteres, garantindo que qualquer palavra possa ser representada com um vocabulário de tamanho fixo e razoável.

---

### Questão 10
**Resposta Correta: B**
* **Comentário:** 
  * **Encoder-only (ex: BERT):** Atenção bidirecional (vê todo o texto). Excelente para classificação e extração.
  * **Decoder-only (ex: GPT):** Atenção causal/unidirecional (só vê o passado). Excelente para geração autorregressiva.
  * **Encoder-Decoder (ex: T5):** Processa a entrada bidirecionalmente e gera a saída autoregressivamente. Ideal para tradução e sumarização.

---

### Questão 11
**Resposta Correta: B**
* **Comentário:** No padrão BIO para NER:
  * **B (Begin):** Marca o início de uma entidade.
  * **I (Inside):** Marca a continuação/interior de uma entidade composta por múltiplos tokens.
  * **O (Outside):** Indica que o token não pertence a nenhuma entidade nomeada.

---

### Questão 12
**Resposta Correta: B**
* **Comentário:** *Pegadinha!* A Perplexidade é calculada como $PP(W) = \exp(H(W))$, ou seja, a exponencial da entropia cruzada. **Quanto menor a perplexidade, melhor o modelo**, pois significa que ele está "menos perplexo" (mais confiante/preciso) ao prever os próximos tokens.

---

### Questão 13
**Resposta Correta: B**
* **Comentário:** O **LoRA** congela os pesos originais $W_0 \in \mathbb{R}^{d \times k}$ do modelo e adiciona uma decomposição de baixo posto: $\Delta W = B \cdot A$, onde $B \in \mathbb{R}^{d \times r}$ e $A \in \mathbb{R}^{r \times k}$, com o rank $r \ll \min(d, k)$. Isso reduz exponencialmente a quantidade de parâmetros a serem atualizados.

---

### Questão 14
**Resposta Correta: C**
* **Comentário:** A Tradução Automática pega uma sequência de texto de entrada em um idioma e gera uma nova sequência em outro idioma (mapeamento de sequência para sequência). As opções A e B são classificação de texto simples (texto para rótulo).

---

### Questão 15
**Resposta Correta: B**
* **Comentário:** O pipeline do RLHF clássico (ex: InstructGPT/ChatGPT) segue rigorosamente:
  1. **SFT:** Fine-tuning supervisionado com pares de prompt/resposta de alta qualidade.
  2. **Reward Model:** Treinamento de um modelo que pontua respostas com base na preferência humana.
  3. **PPO:** Ajuste fino dos pesos do LLM usando Aprendizado por Reforço para maximizar a nota dada pelo Reward Model.

---

### Questão 16
**Resposta Correta: B**
* **Comentário:** *Pegadinha inverter as definições!* 
  * **CBOW (Continuous Bag-of-Words):** Entrada = Palavras do contexto $\rightarrow$ Saída = Palavra central.
  * **Skip-gram:** Entrada = Palavra central $\rightarrow$ Saída = Palavras do contexto ao redor.

---

### Questão 17
**Resposta Correta: B**
* **Comentário:** Devido à multiplicação sucessiva de matrizes ao longo dos passos de tempo no backpropagation através do tempo (BPTT), as RNNs tradicionais sofrem com a atenuação do gradiente ($<1$) ou com sua explosão ($>1$), tornando inviável aprender relacionamentos entre palavras distantes no texto.

---

### Questão 18
**Resposta Correta: B**
* **Comentário:** Essas etapas constituem os procedimentos tradicionais de higienização, normalização e pré-processamento de dados de texto antes de alimentar algoritmos de PLN.

---

### Questão 19
**Resposta Correta: A**
* **Comentário:** *Pegadinha!* Ao contrário das RNNs, o mecanismo de Self-Attention calcula a atenção entre todos os tokens em paralelo através de operações matriciais. A operação $\text{Softmax}(QK^T)V$ é **permutação-invariante**. Sem somar os vetores de *Positional Encoding* aos embeddings, o modelo trataria "O gato comeu o peixe" exatamente da mesma forma que "O peixe comeu o gato".

---

### Questão 20
**Resposta Correta: B**
* **Comentário:** A alucinação em LLMs é o fenômeno em que o modelo gera afirmações fáticas falsas, citações inexistentes ou dados incorretos apresentados com alto grau de confiança e fluência sintática.

---

### Questão 21
**Resposta Correta: B**
* **Comentário:** A família de métricas **ROUGE** (*Recall-Oriented Understudy for Gist Evaluation*) foca em recall e mede a sobreposição de $n$-grams/subsequências entre os resumos gerados pelo modelo e os resumos de referência humana, sendo o padrão para sumarização.

---

### Questão 22
**Resposta Correta: B**
* **Comentário:** Enquanto o *Greedy Search* é um algoritmo ambicioso que faz a escolha localmente ótima a cada token (passo a passo), o *Beam Search* mantém os $B$ caminhos hipotéticos mais prováveis em paralelo no grafo de busca, encontrando sequências globais de maior probabilidade.

---

### Questão 23
**Resposta Correta: B**
* **Comentário:** O **RAG** desacopla a memória do modelo em duas partes: um recuperador (*Retriever*, normalmente baseado em Busca Vetorial em banco vetorial) que busca trechos de documentos relevantes, e um gerador (*LLM*) que consome esses trechos como contexto no prompt para elaborar a resposta fundamentada.

---

### Questão 24
**Resposta Correta: B**
* **Comentário:** *Pegadinha!* A palavra "banco" possui significados completamente diferentes em ambas as frases. No Word2Vec, como cada palavra do vocabulário mapeia para uma única linha fixa na tabela de embeddings, o vetor de "banco" é **estático e idêntico**. No BERT, a atenção lê a palavra no contexto das palavras vizinhas, produzindo vetores **contextualizados e distintos**.

---

### Questão 25
**Resposta Correta: B**
* **Comentário:** A **FlashAttention** é uma reorganização exata da computação de Atenção no nível de hardware (Kernel CUDA). Ela divide a matriz de atenção em blocos (*tiling*) para operar dentro da memória rápida SRAM da GPU sem precisar escrever/ler a gigantesca matriz $N \times N$ inteira na memória principal HBM, atingindo acelerações expressivas de tempo e espaço sem perder precisão matemática.

---

### Questão 26
**Resposta Correta: A**
* **Comentário:** *Zero-Shot Learning* é a capacidade de um modelo performar uma tarefa apenas recebendo a instrução no prompt, sem ter recebido nenhum exemplo de treino (*few-shot*) ou ter passado por fine-tuning específico para aquele dataset.

---

### Questão 27
**Resposta Correta: B**
* **Comentário:** A quantização reduz a precisão da representação numérica dos pesos (ex: de 16 bits para 4 bits), permitindo encaixar modelos grandes em GPUs menores. A troca envolvida (*trade-off*) é uma ligeira degradação no desempenho/qualidade das respostas em troca de uma grande economia de memória VRAM e ganhos de velocidade.

---

### Questão 28
**Resposta Correta: B**
* **Comentário:** A biblioteca `transformers` da **Hugging Face** tornou-se o ecossistema padrão da indústria para carregar, treinar, compartilhar e rodar inferências em modelos estado-da-arte em PLN e LLMs.

---

### Questão 29
**Resposta Correta: B**
* **Comentário:** O F1-Score é a média harmônica entre a Precisão e a Revocação:
$$F1 = 2 \cdot \frac{\text{Precisão} \cdot \text{Revocação}}{\text{Precisão} + \text{Revocação}}$$
É amplamente utilizado para avaliar a performance global em datasets com classes desbalanceadas.

---

### Questão 30
**Resposta Correta: B**
* **Comentário:** *Pegadinha de engenharia de prompt!* O Chain-of-Thought não altera pesos (não é treino/fine-tuning). Em modelos autoregressivos, cada token gerado no output passa a fazer parte da janela de contexto para a geração do token seguinte. Quando o modelo descreve o "passo a passo", ele está utilizando seus próprios tokens gerados como um "rascunho de memória", o que melhora radicalmente o desempenho lógico da resposta final.
