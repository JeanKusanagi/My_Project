# Aprendizado de Máquina Não-Supervisionado
## Modelos e Métricas de Avaliação — Material de Estudo

---

## 1. Conceito Central

**Aprendizado não-supervisionado** é o ramo do ML em que o algoritmo recebe **dados sem rótulos (labels)** e deve encontrar estrutura, padrões ou relações escondidas nos dados por conta própria.

> **Definição de prova:** "Diferente do aprendizado supervisionado, não há uma variável-alvo (y) conhecida. O objetivo não é prever, e sim **descrever/organizar** os dados."

**Três grandes famílias de tarefas:**
| Tarefa | Objetivo | Exemplos de algoritmos |
|---|---|---|
| **Clusterização (agrupamento)** | Agrupar amostras similares | K-Means, DBSCAN, Hierárquico, GMM |
| **Redução de dimensionalidade** | Comprimir features mantendo informação | PCA, t-SNE, UMAP, Autoencoders |
| **Regras de associação / detecção de anomalias** | Encontrar padrões de co-ocorrência ou desvios | Apriori, FP-Growth, Isolation Forest, LOF |

⚠️ **Pegadinha clássica de prova:** associar "não-supervisionado" apenas a clustering. Bancas cobram redução de dimensionalidade e detecção de anomalias também como não-supervisionado — muita gente esquece.

---

## 2. Modelos de Clusterização

### 2.1 K-Means
- Particiona os dados em **k** grupos, minimizando a **soma das distâncias quadráticas** ao centróide (inércia/WCSS — *Within-Cluster Sum of Squares*).
- Algoritmo iterativo: (1) inicializa centróides, (2) atribui pontos ao centróide mais próximo, (3) recalcula centróides, repete até convergir.

**Pressupostos (muito cobrado em prova):**
- Clusters **esféricos** e de tamanho semelhante.
- Sensível à **escala das variáveis** → sempre normalizar/padronizar antes.
- Sensível a **outliers** (média é puxada).
- **k precisa ser definido a priori.**
- Sensível à **inicialização** dos centróides (por isso existe o K-Means++).

⚠️ **Pegadinha:** dizer que k-means "descobre" o número de clusters. Ele **não descobre** — você define k, e usa métricas (cotovelo, silhueta) para *escolher* um bom k, mas o algoritmo em si não infere isso sozinho.

### 2.2 Clusterização Hierárquica
- **Aglomerativa (bottom-up):** cada ponto começa como seu próprio cluster e vai fundindo os mais próximos.
- **Divisiva (top-down):** todos começam juntos e vão se dividindo (menos comum).
- Resultado visualizado em um **dendrograma**; corta-se em uma altura para definir o número de clusters.
- Métodos de linkage: *single*, *complete*, *average*, *Ward*.

⚠️ **Pegadinha:** custo computacional alto — geralmente **O(n²) a O(n³)**, inviável para datasets muito grandes (diferente do K-Means, que é O(n·k·i)).

### 2.3 DBSCAN (Density-Based Spatial Clustering)
- Agrupa por **densidade**: pontos com muitos vizinhos próximos formam um cluster; pontos isolados viram **ruído (outliers)**.
- Parâmetros: `eps` (raio de vizinhança) e `minPts` (mínimo de vizinhos).
- **Não exige definir k** e consegue achar clusters de formato arbitrário (não só esféricos).

⚠️ **Pegadinha:** DBSCAN tem dificuldade quando os clusters têm **densidades muito diferentes** entre si — um único par (eps, minPts) pode não servir para todos.

### 2.4 GMM — Gaussian Mixture Models
- Modelo **probabilístico**: assume que os dados vêm de uma mistura de distribuições gaussianas.
- Usa o algoritmo **EM (Expectation-Maximization)**.
- Diferença-chave em relação ao K-Means: gera **atribuição probabilística** (soft clustering) em vez de "hard clustering" (cada ponto pertence 100% a um cluster).

⚠️ **Pegadinha de prova:** perguntam "qual a diferença entre soft e hard clustering?" — K-Means e DBSCAN são *hard*; GMM é *soft* (dá probabilidade de pertencimento a cada cluster).

---

## 3. Redução de Dimensionalidade

### 3.1 PCA (Análise de Componentes Principais)
- Técnica **linear** que projeta os dados em novos eixos (componentes principais) que **maximizam a variância explicada**.
- Os componentes são **ortogonais** entre si (não-correlacionados).
- Muito usado para visualização, remoção de ruído e mitigação da "maldição da dimensionalidade".

⚠️ **Pegadinha:** PCA é **linear** e sensível à **escala** — sempre padronizar dados antes. Também **não é seleção de features**: ele cria *novas* variáveis (combinações lineares), não escolhe um subconjunto das originais.

### 3.2 t-SNE e UMAP
- Técnicas **não-lineares**, focadas em **visualização** (normalmente reduzindo para 2D/3D).
- Preservam melhor a **estrutura local** (vizinhança) do que a global.

⚠️ **Pegadinha comum:** achar que distâncias entre clusters distantes num gráfico de t-SNE têm significado quantitativo — **não têm**. t-SNE preserva vizinhança local, não distâncias globais reais.

### 3.3 Autoencoders
- Redes neurais que aprendem a **comprimir e reconstruir** os dados (encoder + decoder).
- A camada latente (gargalo) é a representação reduzida.
- Vantagem sobre PCA: consegue capturar relações **não-lineares**.

---

## 4. Métricas de Avaliação

Este é o ponto que mais cai em prova, porque exige diferenciar **avaliação sem rótulo (interna)** de **avaliação com rótulo (externa)** — e saber que a segunda só é possível em contexto de *pesquisa/benchmark*, não em produção real (senão seria supervisionado).

### 4.1 Métricas Internas (não usam rótulo verdadeiro)

| Métrica | O que mede | Intervalo | Interpretação |
|---|---|---|---|
| **Silhouette Score** | Quão bem separado e coeso está cada ponto | -1 a 1 | Quanto mais perto de 1, melhor |
| **Inertia / WCSS** | Soma das distâncias ao centróide | 0 a ∞ | Menor é mais compacto (mas **sempre cai** ao aumentar k) |
| **Davies-Bouldin Index** | Razão entre dispersão intra-cluster e separação inter-cluster | 0 a ∞ | Menor é melhor |
| **Calinski-Harabasz Index** | Razão entre variância inter e intra-cluster | 0 a ∞ | Maior é melhor |

⚠️ **Pegadinha número 1 (a mais cobrada):** usar apenas a **inertia** para escolher k. Como a inertia **sempre diminui** conforme k aumenta (no limite, k = n dá inertia = 0), ela sozinha nunca aponta um "melhor k" — por isso se usa o **método do cotovelo** (procurar o ponto de inflexão no gráfico) e/ou o **silhouette score**, que penaliza overfitting de clusters.

⚠️ **Pegadinha número 2:** aplicar o Silhouette Score diretamente em resultados do **DBSCAN** sem tratar os pontos de ruído (label -1) — isso distorce a métrica, pois ruído não é um "cluster" de verdade.

### 4.2 Métricas Externas (exigem rótulo verdadeiro conhecido)

Usadas em **contextos de validação/pesquisa**, quando por algum motivo você tem o rótulo real (ex.: dataset benchmark) mas está testando um algoritmo não-supervisionado.

| Métrica | O que faz |
|---|---|
| **Adjusted Rand Index (ARI)** | Compara pares de pontos: mesmo cluster nos dois agrupamentos ou não; corrigido pelo acaso |
| **Normalized Mutual Information (NMI)** | Mede quanto de informação um agrupamento dá sobre o outro |
| **Homogeneity** | Cada cluster contém só membros de uma única classe verdadeira? |
| **Completeness** | Todos os membros de uma classe verdadeira estão no mesmo cluster? |
| **V-measure** | Média harmônica entre Homogeneity e Completeness |

⚠️ **Pegadinha conceitual importante:** se você está usando métrica externa (com rótulo), tecnicamente está fazendo **avaliação supervisionada de um modelo não-supervisionado** — isso é comum em pesquisa acadêmica e provas adoram perguntar "por que isso não descaracteriza o método como não-supervisionado?". Resposta: porque o **rótulo não foi usado no treinamento**, apenas na avaliação posterior.

### 4.3 Avaliação em Redução de Dimensionalidade
- **Variância explicada acumulada** (PCA): quanto da informação original os componentes escolhidos retêm.
- **Erro de reconstrução** (Autoencoders/PCA): diferença entre dado original e reconstruído.

---

## 5. Detecção de Anomalias (tópico frequentemente esquecido)

- **Isolation Forest:** isola anomalias construindo árvores aleatórias — anomalias são isoladas com **menos divisões** (mais próximas da raiz).
- **LOF (Local Outlier Factor):** compara a densidade local de um ponto com a de seus vizinhos.
- **One-Class SVM:** aprende uma fronteira que engloba a "normalidade" dos dados.

⚠️ **Pegadinha:** confundir detecção de anomalias não-supervisionada (sem rótulo de "normal/anômalo") com detecção **supervisionada** de fraude, por exemplo — muitos sistemas reais de fraude são supervisionados porque têm histórico rotulado.

---

## 6. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Escolher número de clusters | Método do cotovelo + Silhouette Score (nunca só inertia) |
| Clusters de formato irregular | DBSCAN (não K-Means) |
| Necessidade de escala numérica | K-Means e PCA são sensíveis à escala → sempre normalizar |
| Clustering "soft" com probabilidade | GMM |
| Reduzir dimensões para visualização | t-SNE / UMAP |
| Reduzir dimensões preservando variância (linear) | PCA |
| Avaliar sem ter rótulo | Métricas internas (Silhouette, Davies-Bouldin, Calinski-Harabasz) |
| Avaliar comparando com rótulo real (benchmark) | Métricas externas (ARI, NMI, V-measure) |
| Detectar outliers sem rótulo | Isolation Forest, LOF, One-Class SVM |

---

## 7. Aplicação Profissional (além da prova)

- **Segmentação de clientes** (marketing): K-Means ou GMM sobre dados de comportamento de compra.
- **Redução de dimensionalidade em Big Data**: PCA antes de aplicar modelos supervisionados, para acelerar treino e reduzir overfitting.
- **Detecção de fraude/anomalias** em transações financeiras: Isolation Forest, LOF.
- **Sistemas de recomendação**: regras de associação (Apriori) — "quem compra X também compra Y".
- Na prática, a escolha do **k** ou dos **hiperparâmetros** (eps, minPts) raramente é só matemática — envolve também **interpretabilidade de negócio** (ex.: "3 segmentos de cliente" é mais acionável para o time de marketing do que "7 microssegmentos estatisticamente ótimos").

---

## 8. Perguntas típicas de prova (para se testar)

1. Por que a inertia não pode ser usada sozinha para escolher k?

A inertia (soma das distâncias quadráticas dentro dos clusters) diminui monotonicamente conforme k aumenta — no limite, se k = número de amostras, a inertia é zero (cada ponto é seu próprio cluster). Ou seja, ela sempre "melhora" com mais clusters, então escolher k apenas minimizando a inertia levaria a um overfitting, criando clusters excessivamente fragmentados e sem significado prático. É por isso que se usa o método do "cotovelo" (elbow), que busca o ponto de retorno decrescente, combinado com outras métricas (como silhouette score) que penalizam ou avaliam a qualidade da separação entre clusters, não só a compactação interna.

---

2. Qual a diferença entre clustering hard e soft? Dê um exemplo de cada.

- Hard clustering: cada ponto pertence exclusivamente a um único cluster, com atribuição binária (0 ou 1). Exemplo: K-Means, onde cada amostra recebe um rótulo de cluster único.
- Soft clustering: cada ponto recebe uma probabilidade (ou grau de pertinência) de pertencer a cada cluster, permitindo pertencimento parcial. Exemplo: Gaussian Mixture Models (GMM), onde cada ponto tem uma probabilidade de pertencer a cada uma das gaussianas/componentes.

---

3. Por que o PCA é considerado uma técnica linear e qual sua limitação?

O PCA é linear porque encontra os componentes principais através de combinações lineares das variáveis originais (projeções sobre os autovetores da matriz de covariância). Ele assume que a variância relevante dos dados pode ser capturada por hiperplanos lineares.

Limitação: quando os dados possuem estrutura não linear (por exemplo, formam uma espiral, um "S" ou estão dispostos em variedades curvas — manifolds), o PCA não consegue capturar essa estrutura corretamente, pois tenta "esticar" uma superfície curva em um espaço linear, perdendo informação relevante. Nesses casos, técnicas não lineares como t-SNE, UMAP ou Kernel PCA são mais adequadas.

---

4. Explique por que métricas externas não tornam o método "supervisionado".

Métricas externas (como Adjusted Rand Index, homogeneidade, V-measure) usam rótulos verdadeiros apenas para avaliar a qualidade do agrupamento após ele ter sido feito — os rótulos não são usados durante o processo de treinamento/formação dos clusters. O algoritmo continua sendo não supervisionado porque ele descobre a estrutura dos dados sem acesso a nenhum rótulo durante o aprendizado. Os rótulos servem só como um "gabarito externo" de comparação, um recurso disponível apenas para fins de validação (geralmente em datasets de benchmark), não como sinal de treinamento.

---

5. Em que situação o DBSCAN seria preferível ao K-Means?

O DBSCAN é preferível quando:

- Os clusters têm formatos arbitrários/não convexos (K-Means assume clusters esféricos/convexos);
- Existem outliers/ruído nos dados, já que o DBSCAN pode classificá-los como ruído em vez de forçá-los a um cluster;
- Não se sabe o número de clusters k a priori (DBSCAN não exige que se defina k);
- Os clusters têm densidades variáveis dentro de uma mesma região, mas com separação clara por densidade (ex.: dados geoespaciais, detecção de anomalias, clusters em formato de "lua crescente" ou espiral).

---

6. Por que normalizar os dados antes de rodar K-Means ou PCA?

Ambos os algoritmos são sensíveis à escala das variáveis, pois se baseiam em distâncias (K-Means) ou variância (PCA):

- No K-Means, a distância euclidiana é dominada por variáveis com escalas maiores. Se uma feature varia de 0 a 10.000 e outra de 0 a 1, a primeira dominará o cálculo de distância, distorcendo os clusters.
- No PCA, os componentes principais são escolhidos maximizando a variância. Sem normalização, variáveis com escalas maiores terão variância artificialmente maior e dominarão os primeiros componentes, mesmo que não sejam as mais informativas.

Por isso, normalizar (ex.: StandardScaler, colocando média 0 e desvio padrão 1) garante que todas as variáveis contribuam de forma equilibrada para o resultado do algoritmo.

---

**Questão 7.**
Um analista de dados aplica t-SNE em um conjunto de dados de alta dimensão e observa dois clusters visualmente distantes no gráfico 2D. Ele conclui que esses clusters são "muito diferentes entre si" e que o cluster A é "maior" que o B, pois ocupa mais área visual. Isso está correto?

**Resposta: Não.**
*Comentário:* t-SNE preserva relações de **vizinhança local**, mas não garante que distâncias globais entre clusters ou tamanhos aparentes reflitam a realidade dos dados originais. Essa é uma das pegadinhas mais cobradas em provas e entrevistas técnicas.

---

**Questão 8.**
Por que o K-Means é considerado um caso particular do GMM?

**Resposta:**
Porque o K-Means pode ser derivado do GMM assumindo que: (1) todos os componentes gaussianos têm a **mesma variância (esférica e isotrópica)**; (2) a atribuição de pontos aos clusters é **hard** (0 ou 1), em vez de probabilística (soft), como o EM produz no GMM.

---

**Questão 9.**
Em um projeto de segmentação de clientes, você não possui rótulos verdadeiros de "segmentos corretos". Qual conjunto de métricas você pode usar para validar o número ideal de clusters?

**Resposta:**
Métricas **internas**: Silhouette Score, Índice de Davies-Bouldin, Calinski-Harabasz e o método do cotovelo (inércia/WCSS). Métricas externas (ARI, NMI, V-measure) não se aplicam, pois exigem rótulos verdadeiros, que não existem nesse cenário.

---

**Questão 10.**
Um aluno afirma: "DBSCAN é sempre superior ao K-Means porque não exige definir k antecipadamente." Essa afirmação é totalmente correta?

**Resposta: Não, é uma simplificação equivocada.**
*Comentário:* Embora o DBSCAN não exija k, ele exige a calibração de `eps` e `minPts`, que podem ser tão difíceis de ajustar quanto k. Além disso, o DBSCAN tem dificuldade com clusters de **densidades muito diferentes**, situação em que o K-Means (ou HDBSCAN) pode performar melhor. A escolha do modelo depende da estrutura dos dados.

---

**Questão 11.**
Explique por que a padronização (standardization/normalization) dos dados é geralmente necessária antes de aplicar K-Means ou PCA.

**Resposta:**
Porque ambos os métodos dependem de **distâncias euclidianas** (K-Means) ou de **variância** (PCA). Se as features estiverem em escalas muito diferentes (ex.: idade em anos vs. renda em reais), a feature de maior magnitude dominará o cálculo de distância/variância, distorcendo os clusters ou componentes encontrados, independentemente de sua real importância.

---

**Questão 12 (aplicação prática).**
Você aplicou K-Means com k=4 em dados de transações bancárias e obteve Silhouette Score = 0.15. O que esse valor sugere, e o que você faria a seguir?

**Resposta:**
Um Silhouette Score de 0.15 é **baixo** (próximo de 0), sugerindo clusters mal definidos, sobrepostos ou pouco separados. Passos possíveis: (1) testar outros valores de k com o método do cotovelo e Silhueta; (2) verificar se os dados foram padronizados; (3) considerar que a estrutura pode não ser esférica/convexa e testar DBSCAN, GMM ou Spectral Clustering; (4) revisar a seleção de features (redução de dimensionalidade ou remoção de ruído).

---

**Questão 13.**
Qual a diferença conceitual entre homogeneidade e completude na avaliação de clusters (com ground truth disponível)?

**Resposta:**
- **Homogeneidade**: cada cluster contém, idealmente, apenas membros de uma única classe verdadeira (pureza por cluster).
- **Completude**: todos os membros de uma dada classe verdadeira estão agrupados em um único cluster (não espalhados por vários).
Um modelo pode ter alta homogeneidade e baixa completude (clusters muito "puros", mas fragmentados) — a **V-measure** combina ambos numa métrica harmônica.
