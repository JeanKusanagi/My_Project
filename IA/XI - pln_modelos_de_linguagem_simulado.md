# SIMULADO — Processamento de Linguagem Natural e Modelos de Linguagem
### Tokenização, embeddings, n-gramas, TF-IDF, RNN/LSTM, atenção, Transformers, modelos de linguagem e suas limitações

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas conceituais clássicas de PLN.

---

**1.** **Tokenização**, em Processamento de Linguagem Natural, é o processo de:

a) Traduzir automaticamente um texto de um idioma para outro<br>
b) Remover todos os sinais de pontuação de um texto, sem exceção<br>
c) Dividir um texto em unidades menores (tokens), como palavras, subpalavras ou caracteres, que servirão de base para o processamento posterior<br>
d) Calcular a frequência de ocorrência de cada palavra em um documento

> **Gabarito: c.** Tokenização é a etapa inicial que segmenta o texto bruto em unidades processáveis (tokens), sejam palavras completas, subpalavras (subwords) ou até caracteres individuais, dependendo da abordagem.

---

**2.** **(Pegadinha)** Modelos de linguagem modernos como GPT e BERT costumam utilizar, como estratégia de tokenização, técnicas de:

a) Tokenização exclusivamente por palavra completa (word-level), nunca dividindo palavras<br>
b) Tokenização exclusivamente por caractere individual, sempre<br>
c) Tokenização baseada unicamente em espaços em branco, sem qualquer outro critério<br>
d) Tokenização em **subpalavras** (subword tokenization), como Byte-Pair Encoding (BPE) ou WordPiece, que dividem palavras raras ou desconhecidas em unidades menores e mais frequentes, equilibrando o tamanho do vocabulário com a capacidade de representar palavras fora do vocabulário original

> **Gabarito: d.** Pegadinha: muitos assumem que a tokenização é sempre por palavra inteira ou por caractere — mas a abordagem dominante em LLMs modernos é a tokenização por subpalavras, que lida melhor com palavras raras, neologismos e línguas morfologicamente ricas, sem exigir um vocabulário gigantesco.

---

**3.** Um **n-grama** é definido como:

a) Uma sequência contígua de n itens (geralmente palavras ou caracteres) extraída de um texto<br>
b) Um tipo específico de rede neural profunda<br>
c) Uma métrica de avaliação de tradução automática, exclusivamente<br>
d) Um algoritmo de clustering aplicado a documentos

> **Gabarito: a.** N-gramas são sequências contíguas de n elementos (por exemplo, bigrama = 2 palavras consecutivas, trigrama = 3 palavras consecutivas) utilizadas como base para diversos modelos estatísticos de linguagem e extração de características textuais.

---

**4.** **(Pegadinha)** Um modelo de linguagem baseado puramente em **n-gramas** (como um modelo de trigramas) apresenta qual limitação relevante em relação a modelos baseados em redes neurais (como Transformers)?

a) Modelos de n-gramas nunca podem ser treinados em textos grandes<br>
b) Modelos de n-gramas capturam dependências apenas dentro de uma janela fixa e curta de contexto (definida pelo valor de n), sendo incapazes de capturar relações de longo alcance entre palavras distantes no texto, algo que arquiteturas como Transformers conseguem modelar de forma mais eficaz<br>
c) Modelos de n-gramas são sempre mais precisos do que modelos neurais, em qualquer tarefa<br>
d) Modelos de n-gramas não podem ser usados para prever a próxima palavra em uma sequência

> **Gabarito: b.** Pegadinha: a limitação central dos modelos de n-gramas é justamente a "miopia" contextual — como consideram apenas uma janela fixa de n-1 palavras anteriores, não capturam dependências de longo alcance, diferentemente de arquiteturas mais modernas baseadas em atenção.

---

**5.** **TF-IDF** (Term Frequency–Inverse Document Frequency) é uma técnica utilizada para:

a) Ponderar a importância de uma palavra em um documento específico, dentro de uma coleção (corpus) de documentos, equilibrando sua frequência local (TF) com o quão rara ou comum ela é no conjunto geral de documentos (IDF)<br>
b) Traduzir textos automaticamente entre idiomas<br>
c) Gerar texto de forma autoregressiva, palavra por palavra<br>
d) Corrigir erros ortográficos automaticamente

> **Gabarito: a.** TF-IDF combina a frequência de um termo em um documento específico (TF) com o inverso de sua frequência em toda a coleção de documentos (IDF), dando maior peso a palavras que são frequentes em um documento mas raras no corpus geral — úteis para diferenciar documentos por seu conteúdo distintivo.

---

**6.** **(Pegadinha)** Em TF-IDF, uma palavra extremamente comum (como artigos e preposições, ex.: "de", "a", "o"), presente em praticamente todos os documentos de um corpus, tende a receber:

a) Um peso (score) TF-IDF muito alto, pois aparece com alta frequência em cada documento<br>
b) Um peso TF-IDF exatamente igual a zero, sempre, independentemente do corpus<br>
c) Um peso indefinido, pois o TF-IDF não pode ser calculado para palavras muito frequentes<br>
d) Um peso (score) TF-IDF baixo, mesmo tendo alta frequência local (TF alto), pois seu componente IDF (frequência inversa nos documentos) será muito baixo, já que ela aparece em quase todos os documentos do corpus — refletindo sua baixa capacidade de distinguir um documento dos demais

> **Gabarito: d.** Pegadinha: alta frequência local (TF) não garante alto TF-IDF — o componente IDF penaliza palavras que aparecem em quase todos os documentos, reduzindo seu peso final, já que elas contribuem pouco para diferenciar um documento específico dos demais.

---

**7.** **Word embeddings** (como Word2Vec ou GloVe) são representações de palavras caracterizadas por:

a) Codificar cada palavra como um vetor binário esparso (one-hot encoding), sem qualquer relação semântica entre vetores<br>
b) Serem calculados exclusivamente por contagem de caracteres em cada palavra<br>
c) Não terem qualquer relação com o significado das palavras, sendo apenas identificadores numéricos arbitrários<br>
d) Representar palavras como vetores densos de números reais em um espaço contínuo, de forma que palavras semanticamente similares tendam a ficar próximas nesse espaço vetorial<br>

> **Gabarito: d.** Word embeddings mapeiam palavras para vetores densos em um espaço vetorial contínuo, capturando relações semânticas — palavras com significados ou usos similares tendem a ter vetores próximos nesse espaço (diferente do one-hot encoding, que não carrega nenhuma noção de similaridade).

---

**8.** **(Pegadinha)** Um exemplo clássico frequentemente citado para ilustrar a capacidade de embeddings do tipo Word2Vec de capturar relações semânticas é a operação vetorial aproximada:

a) "rei" − "homem" + "mulher" ≈ "rainha", demonstrando que relações semânticas (como gênero) podem ser capturadas por operações aritméticas simples no espaço vetorial<br>
b) "rei" × "homem" = "rainha", uma operação de multiplicação vetorial<br>
c) "rei" − "rainha" = 0, sempre, para qualquer modelo de embeddings<br>
d) Essa propriedade nunca foi observada empiricamente, sendo apenas uma expectativa teórica não confirmada

> **Gabarito: a.** Pegadinha: é importante lembrar o exemplo correto e a operação certa (subtração e soma vetorial, não multiplicação) — esse resultado empírico, embora não seja perfeito em todos os casos, é um dos exemplos mais citados para ilustrar como embeddings capturam relações semânticas de forma geométrica.

---

**9.** Qual é a principal diferença entre **word embeddings estáticos** (como Word2Vec e GloVe) e **embeddings contextuais** (como os gerados por BERT)?

a) Embeddings estáticos são sempre mais precisos do que embeddings contextuais, em qualquer tarefa<br>
b) Embeddings estáticos atribuem um único vetor fixo para cada palavra, independentemente do contexto em que ela aparece, enquanto embeddings contextuais geram uma representação diferente para a mesma palavra dependendo da frase/contexto em que está inserida (capturando, por exemplo, a diferença entre "banco" de sentar e "banco" financeiro)<br>
c) Não existe diferença relevante entre os dois tipos de embeddings<br>
d) Embeddings contextuais nunca podem ser usados para tarefas de classificação de texto

> **Gabarito: b.** Essa é uma distinção central em PLN moderna: embeddings estáticos (Word2Vec, GloVe) têm um vetor fixo por palavra; embeddings contextuais (BERT e afins) geram representações dinâmicas, sensíveis ao contexto da frase, resolvendo o problema clássico da polissemia (palavras com múltiplos significados).

---

**10.** O mecanismo de **atenção (attention)**, popularizado pela arquitetura Transformer, permite que um modelo:

a) Ignore completamente o contexto ao redor de uma palavra, processando cada token isoladamente<br>
b) Pondere, para cada token, a relevância (peso) de todos os outros tokens da sequência (ou de partes dela) ao gerar sua representação, permitindo capturar dependências de longo alcance de forma mais direta do que arquiteturas recorrentes tradicionais<br>
c) Aumente artificialmente o tamanho do vocabulário do modelo<br>
d) Substitua totalmente a necessidade de qualquer tipo de embedding

> **Gabarito: b.** O mecanismo de atenção permite que cada posição da sequência "observe" e pondere dinamicamente a importância de outras posições, capturando relações de longo alcance de forma mais direta e paralelizável do que redes recorrentes, que processam a sequência passo a passo.

---

**11.** **(Pegadinha)** Sobre a arquitetura Transformer, um erro comum é acreditar que ela processa sequências:

a) De forma sequencial e recorrente, token por token, exatamente como uma RNN/LSTM<br>
b) De forma altamente paralelizável, processando (em grande medida) todos os tokens da sequência de entrada simultaneamente durante o treinamento, ao contrário de arquiteturas recorrentes que processam token por token, de forma sequencial e dependente do estado anterior<br>
c) Sem qualquer noção de ordem entre os tokens, tratando a entrada como um "saco de palavras" (bag of words) desordenado, sem qualquer mecanismo compensatório<br>
d) Apenas em modelos muito pequenos, sendo inviável em modelos de grande escala

> **Gabarito: b.** Pegadinha: uma das maiores vantagens práticas do Transformer sobre RNNs/LSTMs é justamente a paralelização — o processamento simultâneo dos tokens (via mecanismo de atenção) acelera drasticamente o treinamento em hardware moderno (GPUs/TPUs), ao contrário do processamento estritamente sequencial das arquiteturas recorrentes.

---

**12.** **(Pegadinha)** Como o Transformer processa tokens de forma amplamente paralela (sem recorrência sequencial explícita), ele precisa, no entanto, de um componente adicional para não perder a noção de ordem das palavras na sequência. Esse componente é chamado de:

a) Normalização em lote (batch normalization), exclusivamente<br>
b) Codificação posicional (positional encoding), que injeta informação sobre a posição de cada token na sequência, já que o mecanismo de atenção, por si só, não distingue a ordem dos tokens<br>
c) Dropout, uma técnica de regularização sem relação com ordem<br>
d) Função de ativação ReLU

> **Gabarito: b.** Pegadinha: como o mecanismo de atenção, isoladamente, trata a entrada de forma praticamente invariante à ordem (sem recorrência ou convolução sequencial), o Transformer precisa somar (ou combinar) informações de codificação posicional aos embeddings de entrada para que o modelo tenha alguma noção da posição relativa/absoluta de cada token.

---

**13.** Sobre RNNs (Redes Neurais Recorrentes) tradicionais aplicadas a sequências longas, é conhecido o problema de:

a) Overfitting garantido em qualquer conjunto de dados<br>
b) Desaparecimento (vanishing) ou explosão (exploding) do gradiente durante o treinamento, dificultando o aprendizado de dependências de longo alcance na sequência<br>
c) Impossibilidade total de processar qualquer tipo de sequência textual<br>
d) Incapacidade de serem treinadas com o algoritmo de retropropagação (backpropagation)

> **Gabarito: b.** RNNs tradicionais sofrem, ao propagar gradientes através de muitos passos de tempo, do problema clássico de vanishing/exploding gradients, o que dificulta capturar dependências entre elementos distantes na sequência — motivando o desenvolvimento de arquiteturas como LSTM e GRU.

---

**14.** **(Pegadinha)** A arquitetura **LSTM (Long Short-Term Memory)** foi desenvolvida principalmente para:

a) Substituir totalmente a necessidade de qualquer tipo de embedding<br>
b) Mitigar o problema de vanishing/exploding gradient das RNNs tradicionais, por meio de um mecanismo de "portões" (gates — de entrada, esquecimento e saída) e uma célula de memória (cell state), permitindo à rede reter (ou descartar) informações relevantes ao longo de sequências mais longas<br>
c) Eliminar completamente a necessidade de processamento sequencial<br>
d) Ser utilizada exclusivamente em tarefas de visão computacional, sem relação com texto

> **Gabarito: b.** Pegadinha: é comum confundir a motivação da LSTM — ela não elimina a natureza sequencial do processamento (isso é mais associado ao Transformer), mas resolve o problema de retenção de informação ao longo do tempo por meio de seus portões e célula de memória, mitigando o vanishing gradient.

---

**15.** Um **modelo de linguagem** (language model), de forma geral, é definido como um modelo que:

a) Traduz texto entre diferentes idiomas de forma determinística<br>
b) Estima a probabilidade de uma sequência de palavras (ou tokens), sendo comumente usado para prever a próxima palavra/token dado um contexto anterior<br>
c) Classifica imagens em categorias predefinidas<br>
d) Executa análise sintática exclusivamente por regras gramaticais explícitas, sem qualquer componente estatístico

> **Gabarito: b.** A tarefa central de um modelo de linguagem é estimar P(próximo token | tokens anteriores), o que permite tanto avaliar a probabilidade de sequências completas quanto gerar texto de forma autoregressiva, token por token.

---

**16.** **(Pegadinha)** A métrica de **perplexidade (perplexity)**, comumente usada para avaliar modelos de linguagem, é interpretada da seguinte forma:

a) Quanto maior a perplexidade, melhor o desempenho do modelo em prever a sequência de teste<br>
b) Quanto **menor** a perplexidade, melhor, em geral, o desempenho do modelo — perplexidade baixa indica que o modelo atribui, em média, probabilidades mais altas às sequências reais observadas no conjunto de teste, ou seja, está menos "surpreso" (perplexo) com os dados<br>
c) A perplexidade é sempre igual a zero para modelos bem treinados<br>
d) A perplexidade mede exclusivamente o tamanho do vocabulário do modelo

> **Gabarito: b.** Pegadinha: é comum inverter essa relação — perplexidade é, intuitivamente, uma medida de "quão surpreso" o modelo fica ao ver os dados reais; quanto menor esse valor, melhor o modelo está capturando a distribuição real da linguagem no conjunto avaliado.

---

**17.** Modelos como **BERT** são caracterizados, em sua arquitetura Transformer, principalmente por utilizarem:

a) Apenas a parte de decodificador (decoder) do Transformer, de forma autoregressiva, gerando texto token por token da esquerda para a direita<br>
b) Apenas (ou principalmente) a parte de codificador (encoder) do Transformer, sendo treinado de forma bidirecional, considerando o contexto tanto à esquerda quanto à direita de cada token — o que o torna especialmente adequado para tarefas de compreensão de texto, mas não para geração autoregressiva direta<br>
c) Uma arquitetura totalmente distinta do Transformer, sem qualquer relação com atenção<br>
d) Exclusivamente redes convolucionais (CNNs), sem qualquer componente recorrente ou de atenção

> **Gabarito: b.** BERT utiliza majoritariamente a parte de encoder do Transformer, sendo treinado com objetivos como o mascaramento de tokens (Masked Language Modeling), permitindo capturar contexto bidirecional — diferente de modelos decoder-only como o GPT, que geram texto de forma autoregressiva (esquerda para direita).

---

**18.** **(Pegadinha)** Modelos como a família **GPT** são caracterizados, em sua arquitetura, principalmente por utilizarem:

a) Apenas a parte de encoder do Transformer, de forma bidirecional, assim como o BERT<br>
b) Principalmente a parte de decodificador (decoder) do Transformer, treinados de forma autoregressiva (prevendo o próximo token dado apenas o contexto anterior, à esquerda), o que os torna naturalmente adequados para tarefas de geração de texto<br>
c) Uma combinação obrigatória de redes convolucionais com árvores de decisão<br>
d) Nenhuma relação com o mecanismo de atenção, dependendo apenas de camadas totalmente conectadas

> **Gabarito: b.** Pegadinha: é comum confundir a arquitetura de BERT (encoder, bidirecional) com a de GPT (decoder, autoregressivo/unidirecional) — essa distinção arquitetural explica por que BERT costuma ser mais usado para tarefas de compreensão/classificação e GPT para tarefas de geração de texto.

---

**19.** O que caracteriza a chamada **"alucinação"** (hallucination) em modelos de linguagem generativos?

a) Um erro exclusivo de hardware durante a inferência do modelo<br>
b) A geração, pelo modelo, de conteúdo que soa fluente e coerente do ponto de vista linguístico, mas que é factualmente incorreto, inventado ou não sustentado pelos dados/contexto fornecidos<br>
c) Um sinônimo técnico para "overfitting" do modelo durante o treinamento<br>
d) Um fenômeno que ocorre apenas em modelos muito pequenos, sendo automaticamente eliminado em modelos de grande escala

> **Gabarito: b.** Alucinações são respostas geradas com fluência e aparente confiança, mas que não correspondem a fatos reais ou ao contexto fornecido — um desafio relevante mesmo em modelos de grande escala, não exclusivo de modelos pequenos.

---

**20.** **(Pegadinha)** Sobre alucinações em modelos de linguagem de grande escala, é correto afirmar que:

a) Modelos maiores e mais recentes eliminaram completamente esse problema, tornando-o irrelevante na prática atual<br>
b) Ainda que modelos maiores e técnicas mais recentes (como recuperação aumentada — RAG, ou melhor ajuste fino) reduzam a frequência de alucinações, esse continua sendo um desafio relevante e não completamente resolvido em modelos de linguagem generativos, exigindo verificação humana e/ou mecanismos de checagem em aplicações críticas<br>
c) Alucinações ocorrem exclusivamente em respostas muito curtas, nunca em textos longos<br>
d) Alucinações são impossíveis de ocorrer quando o modelo é ajustado (fine-tuned) para um domínio específico

> **Gabarito: b.** Pegadinha: é um exagero comum (e incorreto) afirmar que o problema foi "resolvido" — técnicas como RAG e fine-tuning ajudam a mitigar, mas alucinações continuam sendo um desafio ativo de pesquisa e uma preocupação prática relevante em aplicações reais.

---

**21.** O termo **fine-tuning** (ajuste fino), aplicado a modelos de linguagem pré-treinados, refere-se a:

a) Treinar um modelo completamente do zero, sem aproveitar nenhum conhecimento prévio<br>
b) Continuar o treinamento de um modelo já pré-treinado (que aprendeu representações gerais de linguagem em um grande corpus) sobre um conjunto de dados menor e mais específico, adaptando-o para uma tarefa ou domínio particular<br>
c) Reduzir o tamanho do vocabulário do modelo original<br>
d) Um sinônimo exato de "tokenização"

> **Gabarito: b.** Fine-tuning aproveita o conhecimento geral já capturado por um modelo pré-treinado em grandes volumes de texto, refinando seus parâmetros com dados específicos de uma tarefa/domínio, geralmente com um custo computacional muito menor do que treinar um modelo do zero.

---

**22.** **(Pegadinha)** Um estudante afirma: "Modelos de linguagem de grande escala 'entendem' o significado do texto exatamente da mesma forma que um ser humano, com compreensão consciente do conteúdo." Do ponto de vista técnico, essa afirmação:

a) É consensualmente aceita e comprovada na comunidade científica, sem controvérsias<br>
b) É uma simplificação controversa — tecnicamente, esses modelos aprendem padrões estatísticos complexos de associação entre tokens a partir de grandes volumes de texto, e a comunidade científica ainda debate ativamente até que ponto esse comportamento reflete "compreensão" no sentido cognitivo/humano do termo, sem consenso definitivo sobre a questão<br>
c) É totalmente irrelevante para a área de PLN, sem qualquer discussão acadêmica associada<br>
d) É incorreta, pois modelos de linguagem apenas armazenam e reproduzem textos memorizados literalmente, sem qualquer capacidade de generalização

> **Gabarito: b.** Pegadinha filosófica/técnica: tanto afirmar categoricamente que os modelos "entendem como humanos" quanto afirmar que eles "apenas decoram" são simplificações — o mecanismo real (aprendizado estatístico de padrões complexos em larga escala) e a questão de que tipo de "compreensão" (se alguma) emerge disso permanecem temas de debate ativo, sem consenso definitivo.

---

**23.** O que é a **janela de contexto** (context window) de um modelo de linguagem?

a) O número total de parâmetros treináveis do modelo<br>
b) O número máximo de tokens que o modelo pode considerar simultaneamente como entrada (e, em geral, também como saída acumulada) em uma única inferência, limitando quanto texto anterior o modelo consegue "enxergar" ao gerar uma resposta<br>
c) O tamanho do vocabulário total suportado pelo modelo<br>
d) A quantidade de dados usados durante o treinamento original do modelo

> **Gabarito: b.** A janela de contexto define o limite de tokens (entrada + eventualmente saída, a depender da arquitetura/implementação) que o modelo processa de uma vez — textos ou conversas que excedam esse limite podem ser truncados ou exigir estratégias específicas de gerenciamento de contexto.

---

**24.** **(Pegadinha)** Um usuário afirma: "Se a janela de contexto de um modelo é muito grande (por exemplo, centenas de milhares de tokens), o modelo automaticamente 'aprende' e memoriza permanentemente tudo o que foi dito na conversa para uso em conversas futuras." Essa afirmação está:

a) Correta, pois uma janela de contexto grande implica aprendizado permanente automático<br>
b) Incorreta — a janela de contexto se refere apenas à quantidade de informação que o modelo pode considerar **durante uma única inferência/conversa**; isso é diferente de atualizar os parâmetros (pesos) do modelo de forma permanente, o que exigiria re-treinamento ou fine-tuning — sem mecanismos adicionais, informações de uma conversa não são automaticamente incorporadas de forma persistente aos parâmetros do modelo para conversas futuras<br>
c) Correta, mas apenas para modelos com menos de mil tokens de contexto<br>
d) Incorreta, mas apenas porque janelas de contexto grandes não existem na prática

> **Gabarito: b.** Pegadinha comum entre usuários leigos: confundir "quantidade de contexto processada em uma inferência" com "aprendizado permanente/atualização de pesos" — são conceitos distintos; sem mecanismos externos de memória persistente ou re-treinamento, o modelo não retém automaticamente o conteúdo de uma conversa para uso em interações futuras totalmente separadas.

---

**25.** **RAG (Retrieval-Augmented Generation)** é uma técnica que combina:

a) Apenas técnicas de tokenização por subpalavras, sem qualquer outro componente<br>
b) Um componente de recuperação de informação (retrieval), que busca documentos ou trechos relevantes em uma base de conhecimento externa, com um modelo de geração de linguagem, que usa essas informações recuperadas como contexto adicional para produzir respostas mais fundamentadas e atualizadas<br>
c) Duas redes neurais convolucionais treinadas de forma independente e combinadas por votação<br>
d) Um método exclusivamente utilizado para compressão de modelos, sem relação com geração de texto

> **Gabarito: b.** RAG combina recuperação de informações relevantes (a partir de uma base externa, como documentos ou banco de dados vetorial) com a geração de texto, ajudando a fundamentar as respostas do modelo em informações concretas e reduzindo, entre outros benefícios, a propensão a alucinações sobre fatos específicos.

---

**26.** **(Pegadinha)** Sobre a relação entre o tamanho de um modelo de linguagem (número de parâmetros) e sua qualidade/desempenho, é correto afirmar que:

a) Um modelo maior é sempre e incondicionalmente melhor do que um modelo menor, em qualquer tarefa e cenário, sem exceções<br>
b) Embora o aumento de parâmetros geralmente melhore o desempenho em diversas tarefas (dentro de certos limites e com dados/treinamento adequados), fatores como qualidade e quantidade dos dados de treinamento, técnicas de ajuste fino, arquitetura e eficiência computacional também influenciam fortemente o desempenho final — tamanho não é o único, nem sempre o fator decisivo<br>
c) O tamanho do modelo não tem nenhuma relação com seu desempenho<br>
d) Modelos menores são sempre superiores a modelos maiores, pois processam mais rápido

> **Gabarito: b.** Pegadinha: embora exista uma correlação geral entre escala e capacidade em muitos cenários (as chamadas "leis de escala"), simplificar a relação para "maior é sempre melhor, sem exceção" ignora fatores relevantes como qualidade dos dados, técnicas de treinamento e eficiência — modelos menores bem treinados podem superar modelos maiores mal ajustados em tarefas específicas.

---

**27.** No contexto de **engenharia de prompt** (prompt engineering), a técnica conhecida como **few-shot prompting** consiste em:

a) Não fornecer nenhum exemplo ao modelo, apenas a instrução direta da tarefa<br>
b) Fornecer, dentro do próprio prompt, alguns exemplos (poucos, geralmente entre 1 e poucas dezenas) de entradas e saídas desejadas, para orientar o modelo sobre o formato ou padrão esperado de resposta, sem necessidade de re-treinar ou ajustar os parâmetros do modelo<br>
c) Treinar o modelo do zero utilizando um pequeno conjunto de dados<br>
d) Um sinônimo técnico de fine-tuning completo do modelo

> **Gabarito: b.** Few-shot prompting aproveita a capacidade do modelo de "aprender" padrões a partir de exemplos fornecidos diretamente no contexto da conversa/prompt, sem qualquer atualização de parâmetros — diferente do fine-tuning, que modifica de fato os pesos do modelo.

---

**28.** **(Pegadinha)** Um estudante afirma: "Few-shot prompting e fine-tuning são exatamente a mesma coisa, apenas com nomes diferentes." Essa afirmação está:

a) Correta, pois ambas as técnicas envolvem, obrigatoriamente, a atualização dos pesos internos do modelo<br>
b) Incorreta — few-shot prompting fornece exemplos dentro do contexto de uma única inferência, sem alterar os parâmetros do modelo (efeito temporário, limitado àquela interação), enquanto fine-tuning efetivamente atualiza os pesos internos do modelo por meio de treinamento adicional, produzindo uma mudança persistente no comportamento do modelo em interações futuras<br>
c) Correta, pois ambos os métodos exigem exatamente o mesmo custo computacional<br>
d) Incorreta, mas apenas porque few-shot prompting não pode ser aplicado a nenhum modelo atual

> **Gabarito: b.** Pegadinha: a diferença fundamental está na persistência e no mecanismo — few-shot é um recurso de contexto temporário (não altera o modelo), enquanto fine-tuning é um processo de treinamento que modifica permanentemente os parâmetros do modelo.

---

**29.** **(Pegadinha)** Sobre vieses (bias) em modelos de linguagem treinados em grandes volumes de texto da internet, é correto afirmar que:

a) Modelos de linguagem são sempre neutros e livres de qualquer viés, por serem baseados puramente em estatística e matemática<br>
b) Como aprendem padrões estatísticos a partir de dados produzidos por humanos, modelos de linguagem tendem a refletir (e, em alguns casos, amplificar) vieses, estereótipos e desequilíbrios presentes nos dados de treinamento, o que motiva pesquisas e técnicas específicas voltadas à mitigação desses vieses<br>
c) Vieses em modelos de linguagem só existem em modelos muito antigos, tendo sido completamente eliminados nos modelos mais recentes<br>
d) A presença de vieses é exclusivamente um problema de hardware, não relacionado aos dados de treinamento

> **Gabarito: b.** Pegadinha: a ideia de que um modelo "puramente estatístico" seria automaticamente neutro ignora que a estatística aprendida reflete diretamente os padrões (incluindo desequilíbrios e estereótipos) presentes nos dados de treinamento — um tema de pesquisa e mitigação ativos, não um problema já resolvido ou exclusivo de sistemas antigos.

---

**30.** **(Pegadinha)** Um professor conclui: "Como os modelos de linguagem atuais conseguem gerar textos gramaticalmente corretos e coerentes sobre praticamente qualquer assunto, isso garante que as informações fornecidas por eles são sempre factualmente precisas e confiáveis, sem necessidade de verificação." Essa afirmação está:

a) Correta, pois fluência linguística é equivalente a precisão factual em modelos de linguagem<br>
b) Incorreta — fluência e coerência linguística (a capacidade de gerar texto bem formado gramaticalmente) são propriedades distintas da precisão factual; um modelo pode produzir texto perfeitamente fluente e coerente e, ainda assim, conter informações incorretas ou alucinadas, por isso a verificação de fatos (especialmente em aplicações críticas) continua sendo necessária<br>
c) Correta, desde que o texto gerado seja longo o suficiente<br>
d) Incorreta, mas apenas porque modelos de linguagem nunca geram texto gramaticalmente correto

> **Gabarito: b.** Pegadinha conceitual final, que resume um dos pontos centrais da disciplina: fluência linguística (forma) e correção factual (conteúdo) são dimensões independentes em modelos de linguagem generativos — um texto pode "soar" perfeitamente confiável e, ainda assim, estar factualmente errado, reforçando a importância de verificação humana e de técnicas complementares (como RAG) em aplicações que exigem precisão.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Os pontos mais recorrentes de pegadinha nesta prova foram: a **diferença entre embeddings estáticos e contextuais** (questões 7 a 9), a **distinção arquitetural entre BERT — encoder, bidirecional — e GPT — decoder, autoregressivo** (questões 17 e 18), a **interpretação correta da perplexidade** (questão 16), a **confusão entre janela de contexto e aprendizado/memória permanente** (questão 24), e a **diferença entre few-shot prompting e fine-tuning** (questões 27 e 28) — vale reforçar esses pontos na correção em sala.
