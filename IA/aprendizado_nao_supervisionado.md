# Aprendizado de Máquina Não-Supervisionado: Modelos e Métricas de Avaliação

## 1. Conceitos-chave e definições

**Aprendizado não-supervisionado**: aprender padrões, estrutura ou representações em dados **sem rótulos (labels)**. O objetivo não é prever um `y`, mas descobrir organização latente nos dados (`X`).

**Principais tarefas:**
- **Clusterização (clustering)**: agrupar exemplos semelhantes (K-Means, DBSCAN, Hierárquico, GMM).
- **Redução de dimensionalidade**: encontrar representações compactas (PCA, t-SNE, UMAP, autoencoders).
- **Detecção de anomalias**: identificar pontos que não seguem o padrão geral.
- **Estimação de densidade**: modelar a distribuição de probabilidade dos dados (GMM, KDE).
- **Regras de associação**: encontrar relações frequentes entre itens (Apriori, FP-Growth).

**Diferença fundamental supervisionado vs. não-supervisionado:**
| Aspecto | Supervisionado | Não-supervisionado |
|---|---|---|
| Rótulos | Sim | Não |
| Objetivo | Minimizar erro de predição | Descobrir estrutura |
| Avaliação | Métricas diretas (acurácia, F1) | Métricas indiretas/proxies |
| Ground truth | Disponível | Geralmente ausente |

---

## 2. Modelos principais

### 2.1 K-Means
- Particiona os dados em **k clusters**, minimizando a soma das distâncias quadráticas intra-cluster (inércia/WCSS).
- Assume clusters **convexos, de tamanho e variância semelhantes**.
- Sensível à inicialização (usar **k-means++**) e à escolha de **k**.
- Não lida bem com clusters de formato não-esférico ou densidades muito distintas.
- Algoritmo iterativo:<br>
   (1) inicializa centróides,<br>
   (2) atribui pontos ao centróide mais próximo,<br>
   (3) recalcula centróides, repete até convergir.

### 2.2 Clusterização Hierárquica
- Existem duas estratégias principais para construção da hierarquia:
  - **Aglomerativa** (bottom-up): cada ponto começa como cluster próprio e se funde progressivamente.
  - **Divisiva** (top-down): parte de um único cluster e o divide.
- Critérios de ligação (linkage): *single*, *complete*, *average*, *Ward*.
- Resultado visualizado em um **dendrograma**; corta-se em uma altura para definir o número de clusters.

### 2.3 DBSCAN (Density-Based Spatial Clustering)
- Agrupa por densidade: pontos "core" (com número mínimo de vizinhos, `minPts`, dentro de raio `eps`), pontos de borda e **ruído (outliers)**.
- Encontra clusters de formato arbitrário e detecta outliers naturalmente.
- Não exige k, mas é sensível a `eps` e `minPts`; sofre com densidades muito heterogêneas.
- DBSCAN tem dificuldade quando os clusters têm densidades muito diferentes entre si — um único par (eps, minPts) pode não servir para todos.
- Variante **HDBSCAN** lida melhor com densidades variáveis.

### 2.4 GMM (Gaussian Mixture Models)
- Modelo probabilístico: assume que os dados vêm de uma **mistura de k distribuições gaussianas**.
- Ajustado via **algoritmo EM (Expectation-Maximization)**.
- Fornece **clusterização soft** (probabilidade de pertencimento), diferente do K-Means (hard assignment).
- Mais flexível quanto à forma dos clusters (elipsoides via matriz de covariância).

### 2.5 Redução de dimensionalidade
- **PCA (Análise de Componentes Principais)**:
   - transformação linear que maximiza a variância explicada; usa autovalores/autovetores da matriz de covariância.
   - Técnica linear que projeta os dados em novos eixos (componentes principais) que maximizam a variância explicada.
   - Os componentes são ortogonais entre si (não-correlacionados).
   - Muito usado para visualização, remoção de ruído e mitigação da "maldição da dimensionalidade".
   - PCA é linear e sensível à escala — sempre padronizar dados antes. Também não é seleção de features: ele cria novas variáveis (combinações lineares), não escolhe um subconjunto das originais.
- **t-SNE e UMAP**:
   - Técnicas não-lineares, focadas em visualização (normalmente reduzindo para 2D/3D).
      - **t-SNE**: preserva estrutura local (vizinhança), útil para visualização, mas **distâncias globais e tamanhos de cluster não são interpretáveis**.
      - **UMAP**: similar ao t-SNE, mas geralmente mais rápido e preserva melhor estrutura global.
- **Autoencoders**:
   - redes neurais que aprendem a comprimir e reconstruir os dados (encoder + decoder) de forma não-linear.
   - A camada latente (gargalo) é a representação reduzida.
   - Vantagem sobre PCA: consegue capturar relações não-lineares.

### 2.6 Outros modelos relevantes
- **Mean Shift**: clusterização por deslocamento de médias, baseada em densidade, sem k fixo.
- **Spectral Clustering**: usa autovalores do grafo de similaridade; bom para clusters não-convexos.
- **Self-Organizing Maps (SOM)**: redes neurais para mapeamento topológico.
- **Isolation Forest / One-Class SVM**: detecção de anomalias.

---

## 3. Métricas de avaliação

### 3.1 Métricas internas (sem ground truth)
Avaliam a qualidade da estrutura encontrada usando apenas os próprios dados.

- **Coeficiente de Silhueta (Silhouette Score)**: para cada ponto, compara a distância média intra-cluster (`a`) com a distância média ao cluster vizinho mais próximo (`b`): 
  `s = (b - a) / max(a, b)`. Varia de -1 a 1; valores próximos de 1 indicam boa separação.
- **Índice de Davies-Bouldin**: razão entre dispersão intra-cluster e separação entre clusters. **Quanto menor, melhor** (diferente da silhueta). Varia de 0 a ∞.
- **Índice de Calinski-Harabasz (variance ratio criterion)**: razão entre dispersão inter-cluster e intra-cluster. **Quanto maior, melhor**. Varia de 0 a ∞.
- **Inércia / WCSS (Within-Cluster Sum of Squares)**: usada no **método do cotovelo (elbow method)** para escolher k no K-Means. Varia de 0 a ∞. Menor é mais compacto (mas sempre cai ao aumentar k)

### 3.2 Métricas externas (com ground truth, quando disponível para validação)
- **Adjusted Rand Index (ARI)**: mede concordância entre clusters previstos e rótulos verdadeiros, corrigido para acerto aleatório. Varia de -1 a 1 (1 = concordância perfeita).
- **Normalized Mutual Information (NMI)**: baseada em teoria da informação, mede quanto os agrupamentos compartilham informação com os rótulos reais.
- **Fowlkes-Mallows Index**: média geométrica entre precisão e recall de pares de pontos.
- **Homogeneidade, Completude e V-measure**: homogeneidade avalia se cada cluster contém só uma classe; completude avalia se todos os membros de uma classe estão no mesmo cluster; V-measure é a média harmônica das duas.

### 3.3 Para redução de dimensionalidade
- **Variância explicada (explained variance ratio)** — usada em PCA para decidir quantos componentes manter.
- **Erro de reconstrução** — usado em autoencoders e PCA.
- **Trustworthiness e Continuity** — avaliam se vizinhanças locais foram preservadas (t-SNE, UMAP).

---

## 4. Exemplos práticos

1. **Segmentação de clientes (RFM + K-Means)**: uma empresa de varejo agrupa clientes por recência, frequência e valor monetário de compras para criar campanhas de marketing direcionadas.
2. **Detecção de fraude com DBSCAN**: transações que não pertencem a nenhum cluster denso (marcadas como ruído) são investigadas como possíveis fraudes.
3. **Compressão de imagens com PCA**: reduzir dimensionalidade de pixels mantendo 95% da variância, diminuindo espaço de armazenamento.
4. **Visualização de dados genômicos com t-SNE/UMAP**: agrupar amostras de expressão genética em 2D para inspeção visual de subtipos de câncer.
5. **Agrupamento hierárquico de documentos**: organizar artigos de notícias em um dendrograma por similaridade textual (TF-IDF + linkage).

---

## 5. Pegadinhas comuns (armadilhas de prova e de prática)

1. **"K-Means sempre encontra os clusters ótimos"** — Falso. K-Means converge para **mínimos locais**; é sensível à inicialização (mitigado com múltiplas execuções e k-means++).
2. **Confundir Silhueta com Davies-Bouldin quanto à direção da otimização** — Silhueta: **maior é melhor**. Davies-Bouldin: **menor é melhor**. Calinski-Harabasz: **maior é melhor**. Essa inversão é clássica pegadinha de prova.
3. **Usar métricas internas como prova definitiva de "clusters corretos"** — Métricas internas avaliam **compacidade/separação geométrica**, não necessariamente correspondência com significado semântico ou de negócio.
4. **Achar que ARI/NMI podem ser usados sempre** — Só se aplicam quando existe algum **ground truth** disponível (raro em não-supervisionado "puro"); em provas, costuma-se testar se o aluno sabe que essas métricas **não são não-supervisionadas em espírito puro** — são usadas para *validação*, não para o treinamento em si.
5. **Interpretar distâncias entre clusters no t-SNE como significativas** — Erro grave: t-SNE preserva vizinhança **local**, não distâncias globais nem tamanhos relativos de clusters.
6. **Achar que PCA é sempre a melhor redução de dimensionalidade** — PCA é **linear**; falha em capturar estruturas não-lineares (nesse caso, t-SNE, UMAP ou autoencoders são mais adequados).
7. **Elbow method é sempre claro e objetivo** — Na prática, o "cotovelo" é frequentemente ambíguo; por isso combina-se com silhueta ou outros critérios.
8. **DBSCAN funciona bem em qualquer dado** — Ele falha quando há **clusters com densidades muito diferentes**; nesse caso HDBSCAN é mais indicado.
9. **Padronização dos dados é opcional** — Em modelos baseados em distância (K-Means, DBSCAN, PCA), a **ausência de padronização** (escala) distorce fortemente os resultados. Pegadinha comum: esquecer de mencionar que features em escalas diferentes dominam a distância euclidiana.
10. **GMM e K-Means são a mesma coisa "com nome diferente"** — Falso. K-Means é um caso particular/restrito de GMM (assume clusters esféricos, variância igual, hard assignment); GMM é mais geral (soft assignment, covariâncias distintas).

---

## 6. Questionário com respostas comentadas

**Questão 1.**
Qual das métricas abaixo deve ser **minimizada** para indicar melhor qualidade de clusterização?

a) Silhouette Score<br>
b) Calinski-Harabasz Index<br>
c) Davies-Bouldin Index<br>
d) Adjusted Rand Index

**Resposta: c) Davies-Bouldin Index.**
*Comentário:* Diferente das outras métricas listadas (que devem ser maximizadas), o Davies-Bouldin mede a razão entre dispersão intra-cluster e separação inter-cluster — quanto menor essa razão, mais compactos e bem separados estão os clusters.

---

**Questão 2.**
Um analista de dados aplica t-SNE em um conjunto de dados de alta dimensão e observa dois clusters visualmente distantes no gráfico 2D. Ele conclui que esses clusters são "muito diferentes entre si" e que o cluster A é "maior" que o B, pois ocupa mais área visual. Isso está correto?

**Resposta: Não.**
*Comentário:* t-SNE preserva relações de **vizinhança local**, mas não garante que distâncias globais entre clusters ou tamanhos aparentes reflitam a realidade dos dados originais. Essa é uma das pegadinhas mais cobradas em provas e entrevistas técnicas.

---

**Questão 3.**
Por que o K-Means é considerado um caso particular do GMM?

**Resposta:**
Porque o K-Means pode ser derivado do GMM assumindo que: (1) todos os componentes gaussianos têm a **mesma variância (esférica e isotrópica)**; (2) a atribuição de pontos aos clusters é **hard** (0 ou 1), em vez de probabilística (soft), como o EM produz no GMM.

---

**Questão 4.**
Em um projeto de segmentação de clientes, você não possui rótulos verdadeiros de "segmentos corretos". Qual conjunto de métricas você pode usar para validar o número ideal de clusters?

**Resposta:**
Métricas **internas**: Silhouette Score, Índice de Davies-Bouldin, Calinski-Harabasz e o método do cotovelo (inércia/WCSS). Métricas externas (ARI, NMI, V-measure) não se aplicam, pois exigem rótulos verdadeiros, que não existem nesse cenário.

---

**Questão 5.**
Um aluno afirma: "DBSCAN é sempre superior ao K-Means porque não exige definir k antecipadamente." Essa afirmação é totalmente correta?

**Resposta: Não, é uma simplificação equivocada.**
*Comentário:* Embora o DBSCAN não exija k, ele exige a calibração de `eps` e `minPts`, que podem ser tão difíceis de ajustar quanto k. Além disso, o DBSCAN tem dificuldade com clusters de **densidades muito diferentes**, situação em que o K-Means (ou HDBSCAN) pode performar melhor. A escolha do modelo depende da estrutura dos dados.

---

**Questão 6.**
Explique por que a padronização (standardization/normalization) dos dados é geralmente necessária antes de aplicar K-Means ou PCA.

**Resposta:**
Porque ambos os métodos dependem de **distâncias euclidianas** (K-Means) ou de **variância** (PCA). Se as features estiverem em escalas muito diferentes (ex.: idade em anos vs. renda em reais), a feature de maior magnitude dominará o cálculo de distância/variância, distorcendo os clusters ou componentes encontrados, independentemente de sua real importância.

---

**Questão 7 (aplicação prática).**
Você aplicou K-Means com k=4 em dados de transações bancárias e obteve Silhouette Score = 0.15. O que esse valor sugere, e o que você faria a seguir?

**Resposta:**
Um Silhouette Score de 0.15 é **baixo** (próximo de 0), sugerindo clusters mal definidos, sobrepostos ou pouco separados. Passos possíveis: (1) testar outros valores de k com o método do cotovelo e Silhueta; (2) verificar se os dados foram padronizados; (3) considerar que a estrutura pode não ser esférica/convexa e testar DBSCAN, GMM ou Spectral Clustering; (4) revisar a seleção de features (redução de dimensionalidade ou remoção de ruído).

---

**Questão 8.**
Qual a diferença conceitual entre homogeneidade e completude na avaliação de clusters (com ground truth disponível)?

**Resposta:**
- **Homogeneidade**: cada cluster contém, idealmente, apenas membros de uma única classe verdadeira (pureza por cluster).
- **Completude**: todos os membros de uma dada classe verdadeira estão agrupados em um único cluster (não espalhados por vários).
Um modelo pode ter alta homogeneidade e baixa completude (clusters muito "puros", mas fragmentados) — a **V-measure** combina ambos numa métrica harmônica.

---

## 7. Resumo rápido (cola para revisão)

| Modelo | Exige k? | Formato de cluster | Lida com outliers? | Tipo de assignment |
|---|---|---|---|---|
| K-Means | Sim | Esférico/convexo | Não | Hard |
| Hierárquico | Não (mas exige corte) | Flexível | Não naturalmente | Hard |
| DBSCAN | Não | Arbitrário | Sim (nativo) | Hard |
| GMM | Sim | Elipsoidal | Não naturalmente | Soft |

| Métrica | Direção ótima | Precisa de ground truth? |
|---|---|---|
| Silhouette | Maior | Não |
| Davies-Bouldin | Menor | Não |
| Calinski-Harabasz | Maior | Não |
| ARI | Maior (máx=1) | Sim |
| NMI | Maior (máx=1) | Sim |
