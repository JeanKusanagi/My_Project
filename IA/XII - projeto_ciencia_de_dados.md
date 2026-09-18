# Projeto de Ciência de Dados
## Coleta, Preparação, Modelagem, Avaliação e Implantação — Material de Estudo

---

## 1. Conceito Central

Um **projeto de ciência de dados** é um processo estruturado (mas **iterativo**, não linear) para transformar dados brutos em **conhecimento acionável** ou em um **modelo em produção** que gera valor para um problema de negócio ou pesquisa.

> **Definição de prova:** "Diferente de um exercício acadêmico isolado de treinar um modelo, um projeto de ciência de dados começa e termina no **problema de negócio**: parte do entendimento do problema, passa por coleta, preparação, modelagem e avaliação, e só se conclui quando o modelo está **implantado, monitorado e gerando valor real**."

### 1.1 Metodologias de referência (muito cobrado em prova)

| Metodologia | Etapas | Observação |
|---|---|---|
| **CRISP-DM** (Cross-Industry Standard Process for Data Mining) | Entendimento do Negócio → Entendimento dos Dados → Preparação dos Dados → Modelagem → Avaliação → Implantação | A mais usada na indústria; **cíclica**, com setas de retorno entre praticamente todas as fases |
| **KDD** (Knowledge Discovery in Databases) | Seleção → Pré-processamento → Transformação → Mineração de Dados → Interpretação/Avaliação | Mais acadêmica/histórica, foco no processo de descoberta de conhecimento |
| **OSEMN** | Obtain → Scrub → Explore → Model → iNterpret | Popular em contextos mais informais/data science aplicada |

⚠️ **Pegadinha número 1 (a mais cobrada de toda a unidade):** tratar o processo como **linear e sequencial** (uma via de mão única). O **CRISP-DM é explicitamente cíclico**: é normal e esperado **voltar** de "Modelagem" para "Preparação dos Dados" (ao perceber necessidade de novas features), ou de "Avaliação" para "Entendimento do Negócio" (ao perceber que o problema foi mal formulado). Provas gostam de pedir para desenhar ou identificar essas setas de retorno.

⚠️ **Pegadinha número 2:** confundir as metodologias — CRISP-DM, KDD e OSEMN têm etapas parecidas, mas nomes e ênfases diferentes. A pergunta clássica de prova é "qual etapa do CRISP-DM corresponde a qual etapa do KDD/OSEMN".

---

## 2. Coleta de Dados (Data Collection)

### 2.1 Fontes comuns de dados
- **Bancos de dados internos** (transacionais, data warehouses).
- **APIs** de terceiros (dados públicos, serviços pagos).
- **Web scraping** (extração de dados de páginas web).
- **Sensores/IoT** (dados de streaming em tempo real).
- **Dados públicos/governamentais** (censos, bases abertas).

### 2.2 Qualidade e representatividade da amostra
- A qualidade do modelo final está diretamente limitada pela **qualidade e representatividade** dos dados coletados — princípio conhecido como **"garbage in, garbage out"**.
- **Viés de amostragem (sampling bias):** ocorre quando a amostra coletada não representa fielmente a população-alvo.
- **Viés de sobrevivência (survivorship bias):** ocorre quando só se observam os casos que "sobreviveram" a algum processo de seleção, ignorando os que foram descartados/perdidos ao longo do caminho.

⚠️ **Pegadinha:** achar que "mais dados" sempre resolve problemas de qualidade. Se a coleta é sistematicamente enviesada, **aumentar o volume de dados amplifica o viés**, não o corrige — o problema é de **representatividade**, não de quantidade.

---

## 3. Preparação dos Dados (Data Preparation / Data Wrangling)

### 3.1 Por que essa é a etapa mais demorada
- É consenso amplamente citado na indústria (e cobrado em prova) que a preparação de dados consome tipicamente **60% a 80% do tempo total** de um projeto de ciência de dados — mais do que a modelagem em si.

⚠️ **Pegadinha número 1 (muito cobrada):** achar que a parte "nobre"/mais importante do trabalho de um cientista de dados é escolher e ajustar o algoritmo. Na prática (e em prova), a etapa que mais consome tempo e mais impacta a qualidade final do modelo é a **preparação dos dados**.

### 3.2 Tratamento de valores ausentes (missing values)
| Estratégia | Quando usar |
|---|---|
| **Remoção de linhas/colunas** | Quando a proporção de ausência é pequena e aleatória |
| **Imputação por média/mediana/moda** | Simples, rápida, mas pode distorcer a variância dos dados |
| **Imputação por modelo preditivo** | Mais sofisticada, usa outras variáveis para prever o valor ausente |
| **Criação de indicador de ausência** | Mantém a informação de que o dado "faltava" como uma feature própria |

⚠️ **Pegadinha:** usar a **mediana** em vez da **média** quando há outliers relevantes na variável — a média é sensível a valores extremos, a mediana é robusta.

### 3.3 Normalização vs. Padronização (distinção clássica de prova)

| Técnica | O que faz | Fórmula (conceitual) | Quando usar |
|---|---|---|---|
| **Normalização (Min-Max Scaling)** | Reescala os valores para um intervalo fixo, geralmente [0,1] | (x − min) / (max − min) | Quando se sabe que os dados não têm outliers extremos e o algoritmo é sensível à escala (ex.: redes neurais, KNN) |
| **Padronização (Standardization / Z-score)** | Centraliza os dados em média 0 e desvio-padrão 1 | (x − média) / desvio-padrão | Quando os dados podem ter outliers, ou o algoritmo assume distribuição aproximadamente normal (ex.: regressão linear, PCA, SVM) |

⚠️ **Pegadinha número 1 (super cobrada):** trocar normalização por padronização na explicação — normalização **comprime para um intervalo fixo** (sensível a outliers, pois um único valor extremo distorce toda a escala); padronização **não tem limite fixo**, mas é mais **robusta a outliers** por usar média e desvio-padrão.

### 3.4 Codificação de Variáveis Categóricas (Encoding)
| Técnica | Como funciona | Cuidado |
|---|---|---|
| **One-Hot Encoding** | Cria uma coluna binária para cada categoria | Pode gerar **alta dimensionalidade** com muitas categorias |
| **Label Encoding** | Atribui um número inteiro a cada categoria | Só apropriado para **variáveis ordinais** (com ordem natural); em variáveis nominais, cria uma **falsa relação de ordem/magnitude** |
| **Target Encoding** | Substitui a categoria pela média da variável-alvo para aquela categoria | Risco de **data leakage** se não for calculado corretamente (só com dados de treino) |

⚠️ **Pegadinha número 1 (muito cobrada):** usar **Label Encoding em variável categórica nominal** (sem ordem, ex.: "cor: vermelho, azul, verde"). Isso introduz uma relação numérica falsa (ex.: azul=2 sendo "maior" que vermelho=1), que muitos algoritmos vão interpretar erroneamente como uma relação de magnitude. Nesse caso, o correto é **One-Hot Encoding**.

### 3.5 Vazamento de Dados (Data Leakage) — pegadinha central de todo o projeto
- Ocorre quando **informação do conjunto de teste (ou informação que não estaria disponível no momento real da previsão) "vaza" para o treinamento**, inflando artificialmente a performance do modelo durante avaliação, mas gerando um modelo que falha em produção.

**Fontes comuns de data leakage:**
- Ajustar (`fit`) o normalizador/scaler/encoder em **todo o dataset**, antes de separar treino e teste.
- Usar uma feature que só existe **depois** do evento que se quer prever (ex.: usar "data de cancelamento" para prever "se o cliente vai cancelar").
- Fazer seleção de features olhando para o dataset completo (incluindo teste) antes da divisão.

⚠️ **Pegadinha número 1 (a mais grave de toda a matéria de preparação de dados):** o `fit` de qualquer transformação (scaler, encoder, imputador) deve ser feito **somente com os dados de treino**, e depois aplicado (`transform`) igualmente no treino e no teste. Fazer `fit` no dataset inteiro é uma das causas mais comuns de data leakage, e o modelo pode parecer ótimo na avaliação e **falhar silenciosamente em produção**.

### 3.6 Balanceamento de Classes
- Em problemas de classificação com classes desbalanceadas (ex.: fraude, doenças raras), técnicas comuns incluem:
  - **Undersampling:** reduzir a classe majoritária.
  - **Oversampling:** replicar ou gerar exemplos sintéticos da classe minoritária (ex.: **SMOTE** — Synthetic Minority Oversampling Technique).

⚠️ **Pegadinha:** aplicar técnicas de balanceamento (como SMOTE) **antes** de separar treino/teste também é uma forma de data leakage — os exemplos sintéticos podem "vazar" características do conjunto de teste. O balanceamento deve ser aplicado **somente no conjunto de treino**.

### 3.7 Engenharia e Seleção de Features
- **Feature Engineering:** criação de novas variáveis a partir das existentes (ex.: extrair "dia da semana" de uma data), frequentemente o fator que mais impacta a performance final do modelo.
- **Feature Selection:** remoção de variáveis irrelevantes ou redundantes (reduz overfitting, melhora interpretabilidade e custo computacional).

---

## 4. Modelagem (Modeling)

### 4.1 Divisão dos dados
- **Treino/Validação/Teste:** o conjunto de **treino** ajusta os parâmetros do modelo; o de **validação** é usado para ajustar hiperparâmetros e comparar modelos; o de **teste** é usado **uma única vez**, no final, para estimar a performance real do modelo em dados nunca vistos.
- **Validação cruzada (cross-validation, k-fold):** técnica que reduz a dependência de uma única divisão treino/validação, repetindo o treino/avaliação em k partições diferentes dos dados.

⚠️ **Pegadinha:** usar o conjunto de **teste** para escolher hiperparâmetros ou comparar modelos repetidamente — isso "queima" o teste, tornando a estimativa final de performance **otimista e não confiável**. Essa decisão deve ser feita com o conjunto de **validação** (ou cross-validation no treino).

### 4.2 Escolha do algoritmo
- Depende da **natureza do problema** (classificação, regressão, clustering — ver materiais anteriores de aprendizado supervisionado/não-supervisionado), do **volume de dados**, da **necessidade de interpretabilidade**, e de **restrições computacionais**.

### 4.3 Baseline (linha de base)
- Antes de partir para modelos complexos, é boa prática (e frequentemente cobrado) estabelecer um **modelo baseline simples** (ex.: prever sempre a classe majoritária, ou uma regressão linear básica) para servir de referência mínima de comparação.

⚠️ **Pegadinha:** pular direto para modelos complexos (deep learning, ensembles) sem estabelecer um baseline — sem essa referência, é impossível saber se o ganho de performance do modelo complexo **realmente compensa** a perda de interpretabilidade/custo computacional.

### 4.4 Ajuste de Hiperparâmetros (Hyperparameter Tuning)
| Técnica | Como funciona |
|---|---|
| **Grid Search** | Testa exaustivamente todas as combinações de um conjunto pré-definido de valores |
| **Random Search** | Testa combinações aleatórias dentro de um espaço de busca — geralmente mais eficiente que Grid Search em espaços grandes |
| **Otimização Bayesiana** | Usa os resultados anteriores para **guiar inteligentemente** a próxima combinação a ser testada, sendo mais eficiente que busca aleatória em espaços caros de avaliar |

---

## 5. Avaliação (Evaluation)

### 5.1 Avaliação técnica vs. avaliação de negócio (pegadinha conceitual central desta etapa)
- **Avaliação técnica:** métricas estatísticas do modelo (acurácia, F1, RMSE, etc. — ver materiais anteriores de métricas supervisionadas/não-supervisionadas).
- **Avaliação de negócio:** o modelo, mesmo com boas métricas técnicas, **resolve de fato o problema de negócio** que motivou o projeto? Está alinhado aos **critérios de sucesso definidos na fase de Entendimento do Negócio** do CRISP-DM?

⚠️ **Pegadinha número 1 (muito cobrada):** achar que um modelo com métricas técnicas excelentes (ex.: 95% de acurácia) é automaticamente um **projeto de sucesso**. O CRISP-DM exige, na fase de Avaliação, checar se os **objetivos de negócio originais** foram atingidos — um modelo tecnicamente "bom" pode ser inútil se, por exemplo, é lento demais para o caso de uso real, ou se otimiza uma métrica que não se traduz em valor de negócio (ex.: prever cliques quando o objetivo real era prever vendas).

### 5.2 Retorno ao início do ciclo
- É nessa fase que, com frequência, o projeto **retorna a etapas anteriores** — se o modelo não atinge os critérios de negócio, pode ser necessário revisar a preparação dos dados, coletar mais/outras variáveis, ou até reformular o problema.

---

## 6. Implantação (Deployment)

### 6.1 Modalidades de implantação
| Modalidade | Descrição | Exemplo de uso |
|---|---|---|
| **Batch (em lote)** | O modelo roda periodicamente sobre um conjunto de dados acumulado | Relatórios diários de risco de churn |
| **Online/Real-time (tempo real)** | O modelo responde a requisições individuais, geralmente via API | Sistema de recomendação em um app, aprovação de crédito instantânea |
| **Edge deployment** | Modelo executado diretamente no dispositivo do usuário, sem depender de servidor central | Reconhecimento facial em smartphones |

### 6.2 Conceitos de MLOps (Machine Learning Operations)
- **MLOps** é o conjunto de práticas que aplica princípios de DevOps ao ciclo de vida de modelos de ML, incluindo versionamento de dados/modelos, automação de pipelines de treino e implantação (CI/CD para ML), e monitoramento contínuo.
- **Model Registry:** repositório centralizado que versiona modelos treinados, facilitando rollback e rastreabilidade.
- **Estratégias de implantação gradual:** **Canary deployment** (libera o novo modelo para uma pequena fração do tráfego antes de expandir) e **Shadow deployment** (o novo modelo roda em paralelo ao modelo em produção, sem afetar decisões reais, apenas para comparação).

⚠️ **Pegadinha:** achar que a implantação é o **fim** do projeto de ciência de dados. Na prática (e no CRISP-DM), a implantação é seguida por uma fase contínua de **monitoramento**, que pode reiniciar todo o ciclo.

### 6.3 Monitoramento Pós-Implantação: Drift
| Tipo de drift | Definição |
|---|---|
| **Data drift (covariate shift)** | A **distribuição das variáveis de entrada (X)** muda ao longo do tempo, mesmo que a relação entre X e y permaneça a mesma |
| **Concept drift** | A **relação entre X e y muda** ao longo do tempo — o padrão que o modelo aprendeu deixa de ser válido |
| **Label/Target drift** | A **distribuição da variável-alvo (y)** muda ao longo do tempo |

⚠️ **Pegadinha número 1 (muito cobrada em MLOps):** confundir **data drift** com **concept drift**. Exemplo clássico: em um modelo de aprovação de crédito, se o perfil demográfico dos solicitantes muda (mais jovens pedindo crédito), isso é **data drift**; se o comportamento de pagamento muda para o mesmo perfil de solicitante (ex.: por uma crise econômica, o mesmo perfil que antes pagava em dia passa a inadimplir), isso é **concept drift** — muito mais grave, pois invalida a relação que o modelo aprendeu.

⚠️ **Pegadinha número 2:** um modelo em produção **não deve ser considerado "pronto para sempre"** — a degradação de performance ao longo do tempo (por drift) é esperada, e por isso é necessário monitoramento contínuo de métricas e, frequentemente, um processo definido de **retreinamento periódico**.

---

## 7. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Processo linear ou cíclico? | CRISP-DM é cíclico, com retorno entre fases |
| Etapa que mais consome tempo no projeto | Preparação dos Dados (60-80% do tempo) |
| Reescalar para intervalo fixo [0,1] | Normalização (Min-Max) — sensível a outliers |
| Reescalar para média 0, desvio 1 | Padronização (Z-score) — mais robusta a outliers |
| Codificar variável categórica sem ordem | One-Hot Encoding (não Label Encoding) |
| Fit do scaler/encoder no dataset inteiro | Data leakage — deve ser fit só no treino |
| Aplicar SMOTE antes do split treino/teste | Também é data leakage |
| Usar teste repetidamente para tunar hiperparâmetros | Errado — usar validação/cross-validation |
| Modelo com métricas técnicas ótimas, mas inútil na prática | Falha em avaliação de negócio (CRISP-DM) |
| Mudança na distribuição de X, mesma relação com y | Data drift |
| Mudança na relação entre X e y | Concept drift (mais grave) |
| Fim do projeto após colocar modelo em produção | Errado — exige monitoramento contínuo e possível retreinamento |

---

## 8. Aplicação Profissional

- **Times de dados maduros** organizam seus projetos explicitamente em torno do CRISP-DM (ou variações próprias), documentando cada fase para garantir rastreabilidade e comunicação com stakeholders de negócio.
- **Pipelines automatizados** (ex.: com ferramentas como Airflow, MLflow, Kubeflow) cobrem desde a ingestão de dados até o retreinamento automático, reduzindo erros manuais de data leakage.
- **Dashboards de monitoramento de drift** são cada vez mais padrão em empresas com modelos críticos em produção (crédito, fraude, saúde), disparando alertas quando a performance ou a distribuição dos dados se degrada.
- Um erro comum em entrevistas técnicas e no dia a dia profissional é **subestimar o tempo de preparação de dados** no planejamento de projetos — cronogramas que assumem que "modelagem é a maior parte do trabalho" tendem a estourar prazos.
- Cada vez mais, empresas exigem que a fase de avaliação inclua não só métricas técnicas, mas também **métricas de negócio (KPIs)**, validadas em conjunto com as áreas solicitantes antes da implantação.

---

## 9. Perguntas típicas de prova (para se testar)

1. Por que o CRISP-DM é descrito como um processo cíclico, e não linear? Dê um exemplo de quando o projeto precisaria "voltar" de uma fase posterior para uma anterior.
2. Explique a diferença entre normalização (Min-Max) e padronização (Z-score), e quando cada uma é mais apropriada.
3. O que é data leakage e cite três formas comuns de ele ocorrer durante a preparação de dados e a modelagem.
4. Por que usar Label Encoding em uma variável categórica nominal (sem ordem) pode prejudicar o modelo? Qual seria a alternativa mais apropriada?
5. Qual a diferença entre data drift e concept drift? Por que o concept drift é geralmente considerado mais grave?
6. Por que um modelo com excelentes métricas técnicas pode, ainda assim, ser considerado um "projeto de ciência de dados malsucedido"?
