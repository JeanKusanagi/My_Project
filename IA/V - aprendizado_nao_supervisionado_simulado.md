# 30 Questões de Múltipla Escolha
## Aprendizado de Máquina Não-Supervisionado: Modelos e Métricas de Avaliação

---

### 1. O objetivo principal do aprendizado não-supervisionado é:
a) Prever uma variável-alvo rotulada<br>
b) Encontrar padrões, estruturas ou agrupamentos em dados sem rótulos<br>
c) Maximizar a acurácia em um conjunto de teste rotulado<br>
d) Ajustar uma função de regressão linear

**Gabarito: b)** No aprendizado não-supervisionado não há variável-alvo (y); o objetivo é descobrir estrutura latente nos dados, como grupos (clustering), associações ou reduções de dimensionalidade.

---

### 2. O algoritmo K-Means tem como objetivo principal:
a) Maximizar a distância entre pontos do mesmo cluster<br>
b) Minimizar a soma das distâncias quadráticas intra-cluster (inércia)<br>
c) Maximizar o número de clusters automaticamente<br>
d) Encontrar a fronteira de decisão linear entre classes

**Gabarito: b)** O K-Means minimiza o WCSS (Within-Cluster Sum of Squares), a soma das distâncias quadráticas entre cada ponto e o centróide do seu cluster.

---

### 3. Qual é uma limitação conhecida do K-Means?
a) Não converge nunca<br>
b) Não funciona com dados numéricos<br>
c) Assume clusters de formato aproximadamente esférico e é sensível à inicialização<br>
d) Exige rótulos para funcionar

**Gabarito: c)** O K-Means assume clusters convexos de tamanho/variância semelhantes e depende da posição inicial dos centróides — por isso técnicas como k-means++ foram criadas para mitigar esse problema.

---

### 4. O método do "cotovelo" (elbow method) serve para:
a) Definir o número ideal de clusters observando a queda da inércia<br>
b) Calcular a acurácia do modelo<br>
c) Normalizar os dados antes do treinamento<br>
d) Escolher a métrica de distância euclidiana

**Gabarito: a)** Plota-se a inércia contra diferentes valores de k; o "cotovelo" indica o ponto em que aumentar k traz ganhos marginais decrescentes.

---

### 5. O algoritmo K-Means++ foi criado para:
a) Substituir a distância euclidiana pela distância de Manhattan<br>
b) Melhorar a escolha inicial dos centróides, reduzindo a chance de mínimos locais ruins<br>
c) Eliminar a necessidade de definir k<br>
d) Tornar o algoritmo determinístico para qualquer valor de k

**Gabarito: b)** O K-Means++ escolhe os centróides iniciais de forma probabilística, favorecendo pontos distantes uns dos outros, o que reduz a chance de convergência para soluções subótimas.

---

### 6. O DBSCAN é um algoritmo baseado em densidade. Uma vantagem sobre o K-Means é:
a) Necessitar que o usuário defina k previamente<br>
b) Conseguir identificar clusters de formatos arbitrários e detectar outliers (ruído)<br>
c) Ser sempre mais rápido, independente do tamanho dos dados<br>
d) Gerar sempre o mesmo número de clusters que o K-Means

**Gabarito: b)** O DBSCAN agrupa por densidade (parâmetros `eps` e `min_samples`), permitindo formatos não-convexos e classificando pontos isolados como ruído — algo que o K-Means não faz.

---

### 7. No DBSCAN, um "ponto de núcleo" (core point) é definido como:
a) Qualquer ponto do conjunto de dados<br>
b) Um ponto que possui pelo menos `min_samples` vizinhos dentro do raio `eps`<br>
c) O ponto mais distante do centro de um cluster<br>
d) O centróide de um cluster

**Gabarito: b)** Um ponto de núcleo tem, dentro do raio `eps`, um número de vizinhos igual ou superior a `min_samples`. Pontos de borda têm menos vizinhos, mas estão na vizinhança de um core point; pontos de ruído não satisfazem nenhuma dessas condições.

---

### 8. Uma desvantagem do DBSCAN é:
a) Não conseguir lidar com ruído<br>
b) Ter dificuldade com clusters de densidades muito diferentes entre si<br>
c) Exigir que o número de clusters seja definido a priori<br>
d) Só funcionar com dados categóricos

**Gabarito: b)** Como usa um único par de parâmetros globais (`eps` e `min_samples`), o DBSCAN tem dificuldade quando os clusters do conjunto de dados possuem densidades muito distintas.

---

### 9. No clustering hierárquico aglomerativo, a estratégia geral é:
a) Dividir recursivamente um grande cluster em clusters menores<br>
b) Começar com cada ponto como um cluster e ir fundindo os mais próximos sucessivamente<br>
c) Definir k centróides aleatórios e refinar iterativamente<br>
d) Aplicar uma rede neural para agrupar os dados

**Gabarito: b)** O método aglomerativo (bottom-up) inicia com cada observação como seu próprio cluster e vai unindo os pares mais próximos até restar um único cluster (ou até o critério de parada).

---

### 10. O dendrograma, gerado no clustering hierárquico, é útil porque:
a) Mostra a acurácia do modelo em cada iteração<br>
b) Permite visualizar como os clusters se fundem em diferentes níveis de distância<br>
c) Substitui a necessidade de qualquer métrica de avaliação<br>
d) Só funciona para dados categóricos

**Gabarito: b)** Cortando o dendrograma em determinada altura, é possível escolher visualmente o número de clusters, observando a distância em que as fusões ocorrem.

---

### 11. Qual método de "linkage" (ligação) no clustering hierárquico usa a distância mínima entre pontos de clusters diferentes?
a) Complete linkage<br>
b) Average linkage<br>
c) Single linkage<br>
d) Ward linkage

**Gabarito: c)** O single linkage considera a menor distância entre qualquer par de pontos de dois clusters diferentes. Ele tende a formar clusters alongados e é sensível ao efeito de "encadeamento" (chaining).

---

### 12. O método de Ward, usado no clustering hierárquico, tem como critério:
a) Minimizar o aumento da variância intra-cluster a cada fusão<br>
b) Maximizar a distância entre os centróides<br>
c) Escolher aleatoriamente qual par de clusters unir<br>
d) Utilizar apenas a distância de Manhattan

**Gabarito: a)** O linkage de Ward funde, a cada passo, o par de clusters que resulta no menor aumento possível da soma de quadrados intra-cluster, produzindo clusters geralmente mais compactos e homogêneos.

---

### 13. O Coeficiente de Silhueta (Silhouette Score) varia entre:
a) 0 e 1<br>
b) -1 e 1<br>
c) 0 e 100<br>
d) -infinito e +infinito

**Gabarito: b)** Valores próximos de 1 indicam boa alocação (o ponto está bem mais próximo de seu cluster do que de outros); próximos de -1 indicam alocação provavelmente incorreta; próximos de 0 indicam sobreposição entre clusters.

---

### 14. A fórmula da silhueta de um ponto i é baseada em:
a) Apenas a distância até o centróide do seu cluster<br>
b) A(i), distância média intra-cluster, e B(i), a menor distância média a outro cluster<br>
c) O número total de clusters formados<br>
d) A variância dos atributos do dataset

**Gabarito: b)** A silhueta de um ponto é s(i) = (b(i) - a(i)) / max(a(i), b(i)), onde a(i) é a distância média do ponto aos demais pontos do seu próprio cluster, e b(i) é a menor distância média a pontos do cluster vizinho mais próximo.

---

### 15. O Índice de Davies-Bouldin (Davies-Bouldin Index) é uma métrica interna que:
a) Deve ser maximizada, pois valores altos indicam clusters bem separados<br>
b) Deve ser minimizada, pois valores baixos indicam clusters compactos e bem separados<br>
c) Só pode ser usada quando há rótulos verdadeiros disponíveis<br>
d) É equivalente ao coeficiente de silhueta em todos os casos

**Gabarito: b)** O índice mede a razão entre dispersão intra-cluster e separação inter-cluster; quanto menor, melhor a qualidade da clusterização.

---

### 16. O Índice de Calinski-Harabasz (também chamado Variance Ratio Criterion) é interpretado como:
a) Quanto maior o valor, melhor a separação entre clusters<br>
b) Quanto maior o valor, pior a separação entre clusters<br>
c) É sempre igual ao silhouette score<br>
d) Só pode ser usado com dados categóricos

**Gabarito: a)** Esse índice calcula a razão entre a dispersão entre clusters (between-cluster) e a dispersão dentro dos clusters (within-cluster). Valores mais altos indicam clusters mais densos e bem separados.

---

### 17. Métricas internas de avaliação de clustering (como silhueta, Davies-Bouldin e Calinski-Harabasz) têm em comum o fato de:
a) Exigirem rótulos verdadeiros (ground truth)<br>
b) Avaliarem a qualidade da clusterização usando apenas a estrutura dos próprios dados, sem rótulos externos<br>
c) Serem aplicáveis apenas a dados de imagem<br>
d) Sempre produzirem o mesmo resultado, independentemente do algoritmo usado

**Gabarito: b)** Métricas internas usam somente a geometria/estrutura interna dos dados (coesão e separação), sem necessidade de rótulos verdadeiros — por isso são as mais usadas em cenários genuinamente não-supervisionados.

---

### 18. O Adjusted Rand Index (ARI) é um exemplo de métrica:
a) Interna<br>
b) Externa, pois compara os clusters obtidos com uma partição de referência (rótulos verdadeiros)<br>
c) Que não pode ser normalizada<br>
d) Exclusiva para dados hierárquicos

**Gabarito: b)** O ARI é uma métrica externa: mede a concordância entre a partição gerada pelo algoritmo e uma partição de referência conhecida, corrigindo para concordâncias esperadas ao acaso.

---

### 19. O Adjusted Rand Index varia, tipicamente, em qual intervalo?
a) De 0 a 1, sendo 1 concordância perfeita<br>
b) De -1 (ou próximo disso) a 1, sendo 1 concordância perfeita e valores próximos de 0 equivalentes ao acaso<br>
c) De 0 a 100, sendo 100 a pior concordância<br>
d) Sempre é positivo e ilimitado

**Gabarito: b)** O ARI é ajustado para que agrupamentos aleatórios tenham valor esperado próximo de 0, podendo ser levemente negativo em casos de discordância pior que o acaso, com valor máximo 1.

---

### 20. A métrica "Mutual Information" (Informação Mútua) e sua versão ajustada (AMI), quando aplicadas à avaliação de clustering, medem:
a) A distância euclidiana média entre clusters<br>
b) O quanto a informação sobre a partição obtida reduz a incerteza sobre a partição verdadeira (e vice-versa)<br>
c) O número ideal de clusters<br>
d) A variância interna de cada cluster

**Gabarito: b)** Informação mútua mede a quantidade de informação compartilhada entre duas partições (a predita e a verdadeira); a versão ajustada (AMI) corrige o viés causado pelo número de clusters e pelo acaso.

---

### 21. Em um Gaussian Mixture Model (GMM), a principal diferença em relação ao K-Means é:
a) O GMM não permite calcular log-likelihood<br>
b) O GMM atribui a cada ponto uma probabilidade de pertencer a cada cluster (soft clustering), enquanto o K-Means faz atribuição rígida (hard clustering)<br>
c) O GMM só funciona com uma única dimensão<br>
d) O K-Means é probabilístico e o GMM é determinístico

**Gabarito: b)** O GMM modela os dados como uma mistura de distribuições gaussianas, estimando via algoritmo EM a probabilidade de cada ponto pertencer a cada componente — diferente da atribuição determinística do K-Means.

---

### 22. O algoritmo EM (Expectation-Maximization), usado para ajustar GMMs, consiste em:
a) Uma única etapa de otimização por gradiente descendente<br>
b) Alternar entre estimar as probabilidades de pertencimento (E-step) e reestimar os parâmetros das gaussianas (M-step) até convergência<br>
c) Escolher aleatoriamente os parâmetros e nunca atualizá-los<br>
d) Um método exclusivo para aprendizado supervisionado

**Gabarito: b)** O EM alterna entre a etapa E (calcular a responsabilidade/probabilidade de cada ponto pertencer a cada componente, dados os parâmetros atuais) e a etapa M (reestimar médias, covariâncias e pesos das gaussianas maximizando a log-verossimilhança esperada).

---

### 23. Os critérios de informação AIC e BIC são usados no contexto de GMMs para:
a) Medir a acurácia de classificação<br>
b) Ajudar a escolher o número de componentes (clusters), penalizando a complexidade do modelo<br>
c) Substituir a necessidade do algoritmo EM<br>
d) Normalizar os dados de entrada

**Gabarito: b)** AIC (Akaike Information Criterion) e BIC (Bayesian Information Criterion) equilibram o ajuste do modelo (log-verossimilhança) com uma penalidade pelo número de parâmetros, ajudando a evitar overfitting ao escolher o número de componentes do GMM.

---

### 24. O PCA (Análise de Componentes Principais), embora seja uma técnica de redução de dimensionalidade, é frequentemente combinado com clustering porque:
a) Substitui completamente a necessidade de métricas de avaliação<br>
b) Ajuda a visualizar clusters em 2D/3D e pode reduzir ruído/redundância antes da clusterização<br>
c) Transforma dados não-supervisionados em supervisionados<br>
d) Garante que o K-Means encontrará o número ótimo de clusters

**Gabarito: b)** O PCA projeta os dados nos componentes de maior variância, facilitando a visualização de clusters em baixa dimensão e podendo remover ruído/multicolinearidade antes de aplicar algoritmos de agrupamento.

---

### 25. O t-SNE e o UMAP são técnicas usadas principalmente para:
a) Clusterização direta dos dados<br>
b) Redução de dimensionalidade não-linear voltada à visualização, preservando estrutura local dos dados<br>
c) Cálculo de métricas externas de avaliação<br>
d) Substituir o K-Means em produção

**Gabarito: b)** t-SNE e UMAP são técnicas de redução de dimensionalidade não-linear, muito usadas para visualizar dados de alta dimensão em 2D/3D, preservando principalmente relações de vizinhança local — não são, por si só, algoritmos de clustering.

---

### 26. Um cuidado importante ao usar t-SNE é:
a) As distâncias entre clusters distantes no gráfico final têm interpretação quantitativa direta e confiável<br>
b) O tamanho e a distância aparentes entre clusters no gráfico podem não refletir fielmente as relações reais nos dados originais<br>
c) O algoritmo é determinístico e sempre gera o mesmo resultado<br>
d) Ele preserva perfeitamente distâncias globais entre todos os pontos

**Gabarito: b)** O t-SNE foca em preservar vizinhanças locais; tamanhos de clusters e distâncias entre clusters distantes no gráfico 2D não devem ser interpretados literalmente, e o resultado pode variar com a semente aleatória e hiperparâmetros como a perplexidade.

---

### 27. Antes de aplicar algoritmos de clustering baseados em distância (como K-Means), é importante:
a) Não normalizar os dados, pois isso distorce os clusters<br>
b) Padronizar/normalizar as variáveis, para que atributos com escalas maiores não dominem o cálculo de distância<br>
c) Remover todos os valores numéricos<br>
d) Converter todas as variáveis em categóricas

**Gabarito: b)** Como algoritmos como K-Means e DBSCAN usam métricas de distância, variáveis com escalas muito diferentes (ex.: idade vs. renda) podem dominar o cálculo se não forem padronizadas (ex.: StandardScaler), distorcendo os clusters.

---

### 28. Sobre a escolha do número de clusters (k), é correto afirmar que:
a) Existe uma fórmula fechada e universal que sempre indica o k ideal<br>
b) Métodos como elbow method, silhueta e Davies-Bouldin são heurísticas complementares, e frequentemente é necessário também considerar o conhecimento do domínio<br>
c) O valor de k deve ser sempre igual ao número de atributos do dataset<br>
d) O valor de k nunca deve ser testado empiricamente

**Gabarito: b)** Não há uma solução analítica universal; recomenda-se combinar métodos como cotovelo, silhueta, Davies-Bouldin/Calinski-Harabasz e, sempre que possível, validar a interpretabilidade dos clusters à luz do conhecimento do domínio.

---

### 29. Em relação a outliers, qual afirmação é mais correta?
a) O K-Means é robusto a outliers, pois usa medianas<br>
b) O K-Means é sensível a outliers, pois eles podem distorcer a posição dos centróides (médias); já o DBSCAN pode tratá-los naturalmente como ruído<br>
c) O DBSCAN não é capaz de lidar com ruído de forma alguma<br>
d) Outliers nunca afetam algoritmos de clustering

**Gabarito: b)** Como o K-Means usa a média para atualizar centróides, outliers podem puxar fortemente sua posição. Já o DBSCAN, por ser baseado em densidade, naturalmente rotula pontos isolados como ruído, sendo mais robusto nesse aspecto.

---

### 30. Em um cenário real, sem rótulos disponíveis, qual conjunto de métricas seria mais apropriado para avaliar a qualidade de um clustering?
a) Apenas métricas externas, como ARI e AMI<br>
b) Apenas acurácia e F1-score<br>
c) Métricas internas, como coeficiente de silhueta, Davies-Bouldin e Calinski-Harabasz<br>
d) Nenhuma métrica pode ser calculada sem rótulos

**Gabarito: c)** Métricas externas (ARI, AMI, etc.) exigem rótulos verdadeiros, que por definição não existem em problemas genuinamente não-supervisionados. Nesses casos, usam-se métricas internas — silhueta, Davies-Bouldin, Calinski-Harabasz — que avaliam a coesão e separação dos clusters apenas com base na estrutura dos próprios dados.

---

*Documento gerado para fins educacionais sobre Aprendizado de Máquina Não-Supervisionado.*
