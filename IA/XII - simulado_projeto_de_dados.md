# Simulado: Projeto de Ciência de Dados
**Coleta, Preparação, Modelagem, Avaliação e Implantação de Modelos**

---

### Questão 1 (Fácil)
No ciclo de vida de um projeto de Ciência de Dados, qual metodologia padrão de mercado define o fluxo de trabalho em seis fases iterativas: *Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation* e *Deployment*?

A) Scrum  
B) CRISP-DM  
C) KDD (Knowledge Discovery in Databases)  
D) Kanban  
E) DevOps  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** O **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*) é o framework/metodologia mais adotado para projetos de análise e ciência de dados. Ele descreve as 6 fases fundamentais do ciclo de vida do projeto de forma não linear e iterativa. O KDD é um processo mais antigo e conceitual focado em mineração de dados; Scrum e Kanban são metodologias ágeis de gestão de projetos; e DevOps é focado em engenharia de software e infraestrutura.
</details>

---

### Questão 2 (Médio - *Pegadinha*)
Durante a fase de preparação de dados para um modelo de regressão, um cientista de dados aplica a técnica de **StandardScaler** (padronização Z-score) nos dados de treino e nos dados de teste. Para evitar o vazamento de dados (*data leakage*), como esse procedimento deve ser executado corretamente?

A) O `fit_transform` deve ser aplicado na base inteira (treino + teste) antes da divisão dos dados.  
B) O `fit_transform` deve ser aplicado na base de treino e o `fit_transform` deve ser aplicado novamente na base de teste.  
C) O `fit` deve ser calculado apenas no conjunto de treino; em seguida, aplica-se o `transform` no conjunto de treino e o `transform` no conjunto de teste com os parâmetros do treino.  
D) A padronização só deve ser aplicada nas variáveis-alvo (*targets*), nunca nas variáveis preditoras (*features*).  
E) O `fit` deve ser aplicado na base de teste para descobrir a média do teste e o `transform` na base de treino.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** *Pegadinha comum!* Se você fizer o `fit` no conjunto de dados completo ou fizer o `fit` no conjunto de teste, você estará inserindo informações do teste (média e desvio padrão do teste) no modelo, o que gera **vazamento de dados** (*data leakage*). A regra de ouro é: **Aprenda os parâmetros (`fit`) APENAS no conjunto de treino**, e depois aplique a transformação (`transform`) no treino e no teste com esses mesmos parâmetros aprendidos.
</details>

---

### Questão 3 (Difícil)
Em um problema de classificação binária altamente desbalanceado (99% classe Negativa e 1% classe Positiva), qual das seguintes abordagens de validação e avaliação é a mais **INADEQUADA**?

A) Utilizar a Acurácia como métrica principal de sucesso.  
B) Aplicar a técnica de *Stratified K-Fold Cross-Validation*.  
C) Utilizar a área sob a curva Precision-Recall (PR-AUC) em vez da curva ROC-AUC.  
D) Aplicar SMOTE (*Synthetic Minority Over-sampling Technique*) apenas dentro das dobras (*folds*) de treino da validação cruzada.  
E) Ajustar o limiar de decisão (*decision threshold*) do modelo com base no F1-Score ou Recall da classe minoritária.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: A**

**Comentário:** A **Acurácia** é a métrica mais inadequada para dados desbalanceados. Um modelo ingênuo que preveja *sempre* a classe Negativa terá 99% de acurácia, mas será totalmente inútil, pois não detectará nenhum caso da classe Positiva (de interesse). Para dados desbalanceados, métricas como Precision, Recall, F1-Score e PR-AUC são as recomendadas.
</details>

---

### Questão 4 (Médio)
Qual das alternativas descreve corretamente a diferença operacional entre as técnicas de pré-processamento **One-Hot Encoding** e **Label Encoding**?

A) O One-Hot Encoding atribui um único número inteiro sequencial para cada categoria; o Label Encoding cria uma nova coluna binária para cada categoria.  
B) O Label Encoding cria uma matriz esparsa de vetores binários; o One-Hot Encoding converte apenas variáveis numéricas contínuas.  
C) O Label Encoding atribui um valor inteiro a cada categoria (o que pode introduzir uma relação ordinal não existente); o One-Hot Encoding cria $N$ colunas binárias para $N$ categorias (evitando ordenação implícita).  
D) Ambas as técnicas produzem exatamente os mesmos resultados matemáticos em algoritmos baseados em árvores de decisão e em regressões lineares.  
E) O One-Hot Encoding só pode ser utilizado para a variável resposta (*target*), enquanto o Label Encoding só pode ser aplicado nas *features*.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** O Label Encoding transforma categorias em inteiros (ex: Verde=0, Amarelo=1, Vermelho=2). Isso pode fazer com que algoritmos matemáticos (como Regressão Linear, SVM ou KNN) interpretem que "Vermelho > Amarelo > Verde", criando uma hierarquia falsa. O One-Hot Encoding resolve isso criando uma coluna binária para cada categoria, eliminando a falsa ordenação, embora aumente a dimensionalidade da base.
</details>

---

### Questão 5 (Fácil)
Na etapa de implantação (*deployment*) de modelos em produção, a arquitetura onde o modelo é disponibilizado como um endpoint HTTP (ex: via REST API ou gRPC) para responder a requisições individuais em tempo real é conhecida como:

A) Processamento em Lote (*Batch Scoring*)  
B) Predição Online / Tempo Real (*Stream / Real-time Serving*)  
C) ETL (Extract, Transform, Load)  
D) Treinamento Offline  
E) Data Pipelining Estático  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** No *Real-time Serving* (Predição Online), o modelo fica hospedado em um serviço web e responde a requisições via API em poucos milissegundos. Já no *Batch Scoring* (Processamento em Lote), o modelo roda periodicamente (ex: toda noite) sobre uma grande quantidade de dados salvos em banco de dados ou Data Lake.
</details>

---

### Questão 6 (Difícil - *Pegadinha*)
Considere um modelo de detecção de fraudes em transações financeiras. O custo de não detectar uma fraude (Falso Negativo) é de R\$ 5.000,00, enquanto o custo de bloquear indevidamente um cliente legítimo (Falso Positivo) é de R\$ 50,00. Sabendo disso, para otimizar o resultado financeiro do negócio, como a equipe de Ciência de Dados deve ajustar o modelo?

A) Maximizar a Acurácia global do modelo no conjunto de teste.  
B) Aumentar o limiar de decisão (*threshold*) de probabilidade da classe "Fraude" de 0.50 para 0.80.  
C) Reduzir o limiar de decisão (*threshold*) de probabilidade da classe "Fraude" de 0.50 para um valor menor (ex: 0.15), priorizando a métrica de Recall.  
D) Focar em maximizar unicamente a Precisão (*Precision*) do modelo.  
E) Aumentar a penalização de Regularização L2 para zerar os falsos positivos.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** *Pegadinha!* Um erro de Falso Negativo (deixar passar uma fraude) é 100 vezes mais caro que um Falso Positivo. Portanto, o negócio prefere **capturar o máximo de fraudes possível (alto Recall)**, mesmo que isso aumente um pouco os Falsos Positivos. Para aumentar o Recall da classe "Fraude", deve-se **diminuir o threshold de decisão**: se o modelo achar que a probabilidade de fraude é de apenas 15%, já devemos classificar/investigar como fraude.
</details>

---

### Questão 7 (Médio)
O fenômeno onde o desempenho de um modelo em produção se degrada ao longo do tempo devido a mudanças no comportamento das variáveis de entrada $P(X)$, mesmo que a relação condicional $P(Y|X)$ permaneça inalterada, é denominado:

A) Concept Drift  
B) Data Drift (Covariate Shift)  
C) Overfitting  
D) Target Leakage  
E) Label Noise  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** 
- **Data Drift (ou Covariate Shift):** Ocorre quando a distribuição das *features* de entrada $P(X)$ muda com o tempo (ex: a renda média dos novos usuários do aplicativo aumentou), mas a relação $P(Y|X)$ continua a mesma.  
- **Concept Drift:** Ocorre quando a relação entre a entrada e a variável-alvo $P(Y|X)$ se altera com o tempo (ex: o comportamento de consumo mudou radicalmente durante a pandemia).
</details>

---

### Questão 8 (Difícil - *Pegadinha*)
Ao utilizar a técnica de validação cruzada *K-Fold* tradicional em um problema de previsão de séries temporais (ex: previsão de preço de ações dia a dia), qual é a falha grave cometida e como ela deve ser corrigida?

A) O K-Fold tradicional é inviável porque reduz o número de dados de treino; a solução é usar Hold-out simples de 50/50.  
B) O K-Fold tradicional viola a ordem cronológica dos dados ao embaralhar e usar dados do futuro para prever o passado; a solução é usar *Time Series Split* (janelas expansivas ou deslizantes).  
C) O K-Fold tradicional não funciona para séries temporais porque não é capaz de calcular a métrica RMSE; a solução é utilizar o *Stratified K-Fold*.  
D) O K-Fold exige que a série seja transformada em uma variável categórica antes da validação.  
E) Não há falha; o K-Fold aleatório é a técnica recomendada para séries temporais por garantir a independência dos resíduos.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Pegadinha conceitual sobre vazamento temporal!* Dados temporais possuem dependência cronológica (autocorrelação). Ao usar *K-Fold* tradicional, que embaralha os dados aleatoriamente, o modelo vai usar dados de Quinta-feira para prever Terça-feira (olhando o "futuro" para prever o "passado"). Para séries temporais, deve-se usar estratégias de **Time Series Split** (onde os treinos sempre antecedem cronologicamente os testes).
</details>

---

### Questão 9 (Fácil)
Qual das seguintes métricas de avaliação é indicada especificamente para modelos de **Regressão** (variáveis numéricas contínuas)?

A) Precision  
B) ROC-AUC  
C) Log-Loss  
D) MAE (Mean Absolute Error)  
E) Matriz de Confusão  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: D**

**Comentário:** O **MAE** (*Erro Médio Absoluto*), assim como o MSE e RMSE, avalia a diferença entre valores numéricos previstos e reais em problemas de Regressão. Precision, ROC-AUC, Log-Loss e Matriz de Confusão são ferramentas exclusivas para avaliação de modelos de Classificação.
</details>

---

### Questão 10 (Médio)
Em um projeto de Ciência de Dados, o que é a técnica de **Feature Engineering** (Engenharia de Recursos)?

A) O processo automático de escolha do algoritmo de Machine Learning que apresenta o menor tempo de treino.  
B) O processo de criar novas variáveis preditoras ou transformar variáveis existentes a partir do conhecimento do domínio para facilitar o aprendizado do modelo.  
C) O descarte automatizado de todas as colunas que possuem mais de 5% de dados faltantes.  
D) A configuração dos hiperparâmetros de uma rede neural profunda usando pesquisa em grade (*Grid Search*).  
E) A conversão de um código Python em C++ para aumentar a velocidade de execução na nuvem.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** A **Engenharia de Recursos** consiste em extrair, combinar ou transformar dados brutos em variáveis com maior poder discriminatório ou explicativo (ex: extrair o "dia da semana" de uma coluna de timestamp, ou calcular a razão "dívida/renda"). É frequentemente a etapa que mais impacta a performance de um modelo.
</details>

---

### Questão 11 (Difícil - *Pegadinha*)
Durante a fase de tratamento de dados faltantes (*missing values*), a imputação pela **Mediana** em uma variável numérica contínua é preferível em relação à imputação pela **Média** quando:

A) A variável possui uma distribuição Perfeitamente Normal e sem ruídos.  
B) A variável é do tipo categórica nominal.  
C) A variável apresenta uma distribuição altamente assimétrica (*skewed*) e/ou a presença de *outliers* extremos.  
D) A quantidade de dados faltantes representa mais de 90% de toda a base de dados.  
E) O modelo utilizado posteriormente for unicamente a Regressão Linear Simples.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** A média é extremamente sensível a valores discrepantes (*outliers*). Se uma coluna de salário possui alguns bilionários, a média será distorcida para cima. A **mediana** é uma estatística robusta a outliers e melhor representante da tendência central quando a distribuição é assimétrica. (Obs: para variáveis categóricas nominais, usa-se a Moda, não a mediana).
</details>

---

### Questão 12 (Médio)
O conceito conhecido como **Vazamento de Dados** (*Data Leakage*) em Ciência de Dados ocorre quando:

A) Dados confidenciais de clientes são expostos na internet sem criptografia durante a API de inferência.  
B) O modelo recebe informações durante o treinamento que não estarão disponíveis no momento real da predição em produção.  
C) O banco de dados relacional perde registros devido a falhas no processo de ETL.  
D) As variáveis independentes possuem alta multicolinearidade entre si.  
E) A base de dados utilizada para treino foi coletada sem autorização prévia da LGPD.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Data Leakage* na Ciência de Dados é um viés metodológico grave onde informações da variável resposta (futuro) ou dados que não existirão na hora da inferência vazam para o conjunto de treinamento. Isso resulta em métricas falsamente espetaculares nos testes, mas desempenho pífio em produção.
</details>

---

### Questão 13 (Fácil)
Qual das seguintes alternativas apresenta uma técnica não supervisionada muito utilizada na fase de preparação de dados para **Redução de Dimensionalidade**?

A) Random Forest Classifier  
B) PCA (Principal Component Analysis)  
C) Regressão Logística  
D) Gradient Boosting (XGBoost)  
E) Naive Bayes  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** O **PCA** (*Análise de Componentes Principais*) é uma técnica estatística não supervisionada que projeta dados de alta dimensão em um espaço de menor dimensão (componentes ortogonais) preservando o máximo possível da variância dos dados originais.
</details>

---

### Questão 14 (Difícil)
Em relação aos métodos de seleção de variáveis (*Feature Selection*), assinale a afirmativa que define corretamente a categoria dos métodos do tipo **Wrapper**:

A) Avaliam a relevância das variáveis individualmente com base apenas em testes estatísticos (ex: Chi-quadrado, Correlação de Pearson) independentemente do algoritmo de aprendizado.  
B) A seleção de variáveis ocorre internamente como parte integrante do próprio algoritmo de treinamento (ex: penalizações L1 / Lasso).  
C) Utilizam um modelo de aprendizado de máquina como "caixa-preta" para avaliar iterativamente combinações de subconjuntos de variáveis com base na performance do modelo (ex: *Recursive Feature Elimination - RFE*).  
D) São algoritmos que agrupam variáveis similares usando agrupamento hierárquico antes do treino.  
E) Funcionam apenas para dados não estruturados de imagem e áudio.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** 
- **Filter methods:** Usam estatística pura (correlação, teste F) antes do modelo.  
- **Wrapper methods:** Usam um modelo treinado repetidamente para testar subconjuntos de features (ex: RFE, Forward Selection).  
- **Embedded methods:** A seleção é embutida no algoritmo (ex: Lasso L1, Árvores).
</details>

---

### Questão 15 (Médio - *Pegadinha*)
Um cientista de dados está treinando um modelo de classificação e observa os seguintes resultados de acurácia:
- Acurácia na base de **Treino**: 99,8%  
- Acurácia na base de **Validação**: 62,1%  

Qual é o diagnóstico do modelo e qual estratégia é a mais recomendada para mitigar o problema?

A) Underfitting (subajuste); a solução é aumentar a complexidade do modelo ou adicionar mais *features*.  
B) Overfitting (sobreajuste); a solução é simplificar o modelo, aplicar técnicas de regularização ou coletar mais dados.  
C) Data Drift; a solução é fazer o re-treino do modelo usando uma API REST.  
D) Overfitting; a solução é remover a validação cruzada e utilizar apenas o conjunto de treino.  
E) Baixo viés e baixa variância; o modelo está pronto para implantação imediata em produção.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** A diferença gritante entre a alta performance no treino e a baixa performance na validação indica **Overfitting** (o modelo "decorou" o treino e perdeu a capacidade de generalização para dados não vistos). Para corrigir, devemos aplicar regularização (L1/L2, pruning), reduzir a complexidade do modelo ou aumentar o volume de dados.
</details>

---

### Questão 16 (Fácil)
O que é o **MLops** (*Machine Learning Operations*) no contexto do ciclo de vida de projetos de Ciência de Dados?

A) Uma linguagem de programação desenvolvida para substituir o Python no treinamento de redes neurais.  
B) Um conjunto de práticas e ferramentas que busca automatizar e padronizar todo o ciclo de vida de ML (integração, entrega, monitoramento e governança de modelos) unindo Ciência de Dados e Engenharia de Software.  
C) Um algoritmo de otimização estocástico para ajuste de hiperparâmetros.  
D) Uma ferramenta de visualização gráfica baseada em Javascript para gráficos 3D.  
E) Um protocolo de segurança de banco de dados para evitar ataques de injeção SQL.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** MLOps é a cultura e prática de aplicar princípios de DevOps ao ciclo de vida do Machine Learning. Garante que os modelos não fiquem apenas em "notebooks de laboratório", mas sejam implantados com segurança, monitorados continuamente e atualizados de forma automatizada.
</details>

---

### Questão 17 (Difícil - *Pegadinha*)
Considere a matriz de confusão abaixo para um teste médico de diagnóstico de uma doença rara (Classe Positiva = Doente):

| | Previsto Não Doente | Previsto Doente |
| :--- | :---: | :---: |
| **Real Não Doente** | 900 | 10 |
| **Real Doente** | 20 | 70 |

Calcule a **Precisão** (*Precision*) e a **Revocação** (*Recall*) para a detecção de doentes:

A) Precisão = 78,0% e Revocação = 87,5%  
B) Precisão = 87,5% e Revocação = 77,8%  
C) Precisão = 90,0% e Revocação = 70,0%  
D) Precisão = 87,5% e Revocação = 70,0%  
E) Precisão = 70,0% e Revocação = 87,5%  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Pegadinha nos cálculos da Matriz de Confusão!*
- Verdadeiros Positivos (VP) = 70
- Falsos Positivos (FP) = 10
- Falsos Negativos (FN) = 20
- Verdadeiros Negativos (VN) = 900

Fórmulas:
- $\text{Precisão} = \frac{VP}{VP + FP} = \frac{70}{70 + 10} = \frac{70}{80} = 0.875 \text{ ou } 87,5\%$
- $\text{Revocação (Recall)} = \frac{VP}{VP + FN} = \frac{70}{70 + 20} = \frac{70}{90} \approx 0.7777 \text{ ou } 77,8\%$
</details>

---

### Questão 18 (Médio)
A técnica de otimização de hiperparâmetros conhecida como **Random Search** (Busca Aleatória) frequentemente apresenta resultados superiores ou comparáveis ao **Grid Search** (Busca em Grade) em menos tempo computacional porque:

A) O Random Search testa rigorosamente todas as combinações do espaço de busca definido sem pular nenhuma.  
B) O Random Search explora melhor o espaço de parâmetros amostrando valores em uma distribuição contínua, focando o tempo computacional nas dimensões que realmente impactam o modelo.  
C) O Random Search garante matematicamente encontrar o mínimo global da função de perda.  
D) O Grid Search utiliza derivada parcial para encontrar os hiperparâmetros, o que exige muito processamento gráfico (GPU).  
E) O Random Search ajusta os pesos da rede neural via backpropagation durante a busca.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** O *Grid Search* testa combinações em uma grade fixa, gastando muito tempo testando variações de parâmetros que às vezes não afetam o resultado. O *Random Search* escolhe pontos aleatórios no espaço de busca contínuo, cobrindo uma variedade muito maior de valores para os hiperparâmetros mais importantes com uma fração do custo computacional.
</details>

---

### Questão 19 (Médio)
Qual das alternativas apresenta a melhor conduta para o tratamento de **Outliers** (valores discrepantes) na etapa de preparação de dados?

A) Outliers devem ser sempre deletados imediatamente da base de dados sem qualquer análise prévia.  
B) Outliers devem ser sempre substituídos pelo valor zero para não afetar o cálculo da variância.  
C) A causa do outlier deve ser investigada: se for erro de digitação/coleta, corrige-se ou remove-se; se for um evento real legítimo do negócio, deve-se avaliar o uso de transformações (ex: logarítmica) ou modelos robustos.  
D) Deve-se duplicar as linhas com outliers para balancear o conjunto de dados.  
E) Outliers só impactam modelos baseados em árvores de decisão, devendo ser removidos apenas se o modelo for XGBoost.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** Excluir outliers sem critério é uma péssima prática. Em domínios como detecção de fraudes ou diagnósticos raros, o outlier é justamente o sinal de interesse! A remoção só é automática se comprovado que é um erro de medição/sistema. Caso contrário, usam-se transformações de dados ou modelos imunes a outliers (como modelos baseados em árvore).
</details>

---

### Questão 20 (Difícil - *Pegadinha*)
Qual é a função do conjunto de dados de **Validação** (*Validation Set*) e como ele difere do conjunto de **Teste** (*Test Set*)?

A) O conjunto de validação é usado para treinar os pesos internos do modelo; o conjunto de teste é usado para calibrar os hiperparâmetros.  
B) O conjunto de validação serve para ajustar hiperparâmetros e tomar decisões de arquitetura durante o desenvolvimento; o conjunto de teste deve ser mantido intocado e serve apenas para a avaliação final não viesada da generalização.  
C) Validação e Teste são termos estritamente sinônimos na literatura e podem ser intercalados no código sem prejuízos.  
D) O conjunto de teste é utilizado exclusivamente no ambiente de produção após o *deploy*, enquanto o de validação é utilizado no ambiente local.  
E) O conjunto de validação é composto por dados sintéticos, enquanto o de teste é composto por dados reais.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Pegadinha de metodologia!* Se você ajustar hiperparâmetros olhando para o conjunto de teste, o conjunto de teste passa a "vazar" informações indiretamente para a sua escolha de modelo (overfitting no teste). O fluxo correto é:  
1. **Treino:** Ajusta os pesos/coeficientes.  
2. **Validação:** Seleciona o melhor modelo/hiperparâmetros.  
3. **Teste:** Avalia a performance final do modelo escolhido de forma neutra.
</details>

---

### Questão 21 (Médio)
No contexto de explicabilidade e interpretabilidade de modelos de Machine Learning (XAI), a técnica baseada na teoria dos jogos cooperativos que calcula a contribuição marginal individual de cada *feature* para a predição de uma instância específica é chamada de:

A) LIME (Local Interpretable Model-agnostic Explanations)  
B) Valores de SHAP (Shapley Additive exPlanations)  
C) Matriz de Covariância  
D) Gradient Descent  
E) Coeficiente de Gini  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** O **SHAP** (*Shapley Additive exPlanations*) baseia-se no valor de Shapley da Teoria dos Jogos. Ele quantifica o impacto individual de cada variável para uma previsão específica comparando a previsão com e sem essa variável em todas as combinações possíveis de subconjuntos de recursos.
</details>

---

### Questão 22 (Fácil)
Ao realizar o pré-processamento de dados de texto para uso em modelos preditivos de machine learning clássicos, o processo de conversão de texto em matrizes de frequência de palavras (como TF-IDF ou Bag of Words) é um exemplo de:

A) Vetorização de Texto  
B) Clustering K-Means  
C) Binarização de Rótulos  
D) Compressão sem perdas  
E) Normalização Min-Max  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: A**

**Comentário:** Algoritmos matemáticos de Machine Learning exigem dados numéricos na entrada. A **Vetorização** é o processo de transformar cadeias de caracteres e textos brutos em representações vetoriais numéricas legíveis pelos modelos.
</details>

---

### Questão 23 (Difícil - *Pegadinha*)
Suponha que você construiu um pipeline de Machine Learning no Scikit-Learn contendo: Imputador de dados faltantes $\rightarrow$ OneHotEncoder $\rightarrow$ StandardScaler $\rightarrow$ Regressão Logística. Ao salvar esse pipeline para produção em formato serializado (ex: arquivo `.joblib` ou `.pkl`), qual é a principal vantagem operacional?

A) O arquivo pickle substitui a necessidade de ter uma máquina com Python instalado no servidor de produção.  
B) O pipeline serializado garante que exatamente as mesmas transformações aprendidas no treino (médias do scaler, categorias do encoder, etc.) sejam aplicadas aos dados novos de produção, prevenindo inconsistências e vazamento.  
C) O pipeline serializado converte automaticamente o modelo para executar em linguagem SQL no banco de dados.  
D) O pipeline garante que o modelo nunca sofrerá de *Data Drift* ou degradação em produção.  
E) A serialização reduz a acurácia do modelo para otimizar o tempo de resposta do servidor.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Pegadinha!* Salvar o objeto `Pipeline` inteiro (e não apenas o modelo final) empacota o estado interno de todos os transformadores pré-processadores (`fit`). Na hora da inferência em produção, ao rodar `pipeline.predict()`, os novos dados brutos passam exatamente pelas mesmas réguas do treino de forma atômica e segura.
</details>

---

### Questão 24 (Médio)
Para comparar se a diferença de desempenho entre dois modelos de classificação treinados na mesma base de dados é estatisticamente significativa, qual das opções abaixo é um teste estatístico adequado?

A) Teste T de Student pareado ou Teste de McNemar  
B) Teste A/B sem grupo de controle  
C) Análise de Variância (ANOVA) de um fator sem amostras aleatórias  
D) Teste de Durbin-Watson para autocorrelação  
E) Cálculo da distância Euclidiana entre as matrizes de confusão  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: A**

**Comentário:** Para verificar se o ganho de acurácia/F1-score de um modelo sobre outro não foi mero acaso do teste, utilizam-se testes estatísticos de hipótese adequados para amostras pareadas, como o **Teste T de Student pareado** (aplicado nos resultados de k-folds) ou o **Teste de McNemar** (para tabelas de contingência de erros/acertos).
</details>

---

### Questão 25 (Fácil)
Qual é o objetivo da técnica de **Amostragem Estratificada** (*Stratified Sampling*) ao dividir um conjunto de dados em Treino e Teste?

A) Garantir que os dados mais recentes fiquem todos no conjunto de treino.  
B) Garantir que a proporção das classes da variável-alvo (*target*) seja mantida idêntica tanto no conjunto de treino quanto no de teste.  
C) Garantir que não existam valores *outliers* na base de treino.  
D) Selecionar apenas as colunas que possuem forte correlação linear.  
E) Reduzir o número total de linhas do dataset pela metade.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** A amostragem estratificada garante que as proporções das classes (ex: 90% classe A e 10% classe B) sejam preservadas igualmente na divisão entre treino e teste, evitando que o conjunto de teste, por azar da aleatoriedade, fique sem exemplos da classe minoritária.
</details>

---

### Questão 26 (Difícil)
Em relação às estratégias de implantação (*deployment*) de modelos, a estratégia conhecida como **Canary Deployment** consiste em:

A) Substituir 100% dos servidores do modelo antigo pelo novo modelo instantaneamente de uma só vez.  
B) Executar o modelo novo em paralelo com o modelo antigo processando todas as requisições, mas retornando para o usuário final apenas a resposta do modelo antigo para avaliar a latência.  
C) Redirecionar gradualmente uma pequena porcentagem do tráfego real de usuários (ex: 5%) para a versão nova do modelo e monitorar sua performance antes de expandir para o restante da base.  
D) Treinar o modelo diretamente no dispositivo do usuário final (Edge Computing) sem tráfego de rede.  
E) Manter o modelo em ambiente local sem qualquer conexão com a internet por motivos de segurança.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** 
- **Canary Deployment:** Roteia uma pequena fatia do tráfego real (o "canário na mina") para o modelo novo. Se tudo correr bem, aumenta-se a porcentagem gradativamente.  
- **Blue-Green Deployment:** Alterna a chave do ambiente antigo para o novo de uma vez só.  
- **Shadow Deployment:** Executa o modelo novo "nas sombras" em paralelo, sem enviar as respostas ao usuário.
</details>

---

### Questão 27 (Médio - *Pegadinha*)
Considere um modelo preditivo que utiliza a transformação logarítmica $\log(y)$ na variável dependente de treino para corrigir a heterocedasticidade. Para avaliar o erro do modelo em unidades monetárias originais (Reais) usando a métrica RMSE, qual procedimento é **obrigatório** na fase de predição?

A) Elevar o erro RMSE ao quadrado antes da apresentação aos stakeholders.  
B) Aplicar a função exponencial $\exp(\hat{y})$ (função inversa do logaritmo) nas predições do modelo antes de calcular o RMSE contra o $y$ real em escala original.  
C) Dividir o valor obtido no RMSE pelo desvio padrão da variável preditora.  
D) Nenhuma transformação é necessária, pois o RMSE calcula automaticamente o logaritmo inverso interno.  
E) Aplicar o operador Softmax nos resíduos de saída.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Pegadinha de escala!* Se você treinou o modelo para prever $\log(y)$, as predições $\hat{y}$ estarão na escala logarítmica. Se você calcular o RMSE diretamente nessa escala, a métrica estará em "unidades logarítmicas", desprovida de sentido para o negócio. Para avaliar o erro real em Reais, você deve reverter a transformação aplicando a função exponencial $\exp(\hat{y})$ nos valores previstos antes de subtraí-los dos valores reais $y$.
</details>

---

### Questão 28 (Fácil)
Qual das variáveis a seguir é classificada do ponto de vista estatístico como **Qualitativa Ordinal**?

A) Temperatura em graus Celsius  
B) Estado Civil (Solteiro, Casado, Divorciado)  
C) Nível de Escolaridade (Ensino Fundamental, Ensino Médio, Ensino Superior)  
D) Salário mensal em Reais  
E) Número de filhos de um funcionário  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: C**

**Comentário:** 
- **Qualitativa Ordinal:** Categórica, porém possui uma ordenação ou hierarquia natural entre as categorias (ex: Ensino Fundamental < Médio < Superior).  
- Estado Civil é *Qualitativa Nominal* (não há ordem).  
- Salário é *Quantitativa Contínua*.  
- Número de filhos é *Quantitativa Discreta*.
</details>

---

### Questão 29 (Difícil - *Pegadinha*)
A técnica de validação de modelos conhecida como **Bootstrapping** se baseia em qual procedimento estatístico?

A) Divisão determinística da base em 10 partes iguais sem repetição.  
B) Reamostragem com reposição (*sampling with replacement*) a partir do conjunto de dados original para gerar múltiplos subconjuntos do mesmo tamanho.  
C) Agrupamento espacial por k-vizinhos mais próximos para remover amostras redundantes.  
D) Eliminação sistemática do último registro de cada classe a cada iteração.  
E) Filtragem de Kalman para suavização de resíduos aleatórios.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** *Pegadinha sobre amostragem!* O **Bootstrap** cria novos conjuntos de dados retirando amostras aleatórias com reposição da base original. Isso significa que uma mesma linha pode aparecer repetida múltiplas vezes no subconjunto gerado, enquanto cerca de 36,8% dos dados originais ficam de fora (usados como base *Out-of-Bag* para teste/validação).
</details>

---

### Questão 30 (Médio)
Durante o monitoramento contínuo de um modelo de concessão de crédito em produção, a equipe detecta uma queda abrupta na métrica de **KS (Kolmogorov-Smirnov)**. O que esse resultado indica?

A) O servidor web onde a API do modelo está hospedada está sofrendo falta de memória RAM.  
B) A capacidade do modelo em discriminar/separar os bons pagadores dos maus pagadores diminuiu.  
C) O modelo tornou-se 100% preciso e não precisa mais ser monitorado.  
D) Os dados de entrada contêm caracteres especiais não aceitos no JSON.  
E) O tempo de resposta (latência) do modelo aumentou para mais de 5 segundos.  

<details>
<summary><b>Gabarito e Comentário</b></summary>

**Resposta Correta: B**

**Comentário:** A estatística **KS (Kolmogorov-Smirnov)** é uma métrica amplamente utilizada no mercado financeiro/crédito para medir a capacidade de separação entre duas distribuições acumuladas (ex: maus pagadores vs bons pagadores). Quanto maior o KS, melhor o modelo diferencia os dois grupos. Uma queda no KS em produção é um alerta claro de perda de poder discriminatório, sinalizando a necessidade de re-treinamento do modelo.
</details>