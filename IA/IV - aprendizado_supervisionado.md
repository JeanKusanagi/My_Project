# Aprendizado de Máquina Supervisionado
## Modelos e Métricas de Avaliação — Material de Estudo

---

## 1. Conceito Central

**Aprendizado supervisionado** é o ramo do ML em que o algoritmo aprende a partir de dados **rotulados**: cada exemplo de treino tem um par **(X, y)**, onde X são as features (variáveis de entrada) e y é o **rótulo/alvo (target)** que se quer prever.

> **Definição de prova:** "O modelo aprende uma função f(X) ≈ y a partir de exemplos conhecidos, e o objetivo é generalizar essa função para prever y em dados novos e não vistos."

**Duas grandes famílias de tarefas:**
| Tarefa | Objetivo | y (alvo) | Exemplos de algoritmos |
|---|---|---|---|
| **Classificação** | Prever uma **categoria/classe** | Discreto (ex.: "sim/não", "spam/não-spam") | Regressão Logística, KNN, Árvores, SVM, Naive Bayes, Random Forest |
| **Regressão** | Prever um **valor numérico contínuo** | Contínuo (ex.: preço, temperatura) | Regressão Linear, Ridge/Lasso, Árvores de Regressão, SVR |

⚠️ **Pegadinha clássica de prova:** confundir classificação binária com regressão quando o alvo é numérico mas representa categoria codificada (ex.: 0/1). O que define a tarefa é a **natureza semântica do alvo**, não o tipo de dado armazenado — se é probabilidade/classe, é classificação.

---

## 2. Modelos de Classificação

### 2.1 Regressão Logística
- Apesar do nome, é um modelo de **classificação**.
- Modela a **probabilidade** de pertencer a uma classe usando a função **sigmoide**, que comprime a saída entre 0 e 1.
- É um modelo **linear** na fronteira de decisão.

⚠️ **Pegadinha:** achar que "regressão" no nome significa que é modelo de regressão numérica — é usada para **classificar**, geralmente binária (pode ser estendida para multiclasse via softmax/one-vs-rest).

### 2.2 K-Nearest Neighbors (KNN)
- Classifica um novo ponto pela **classe majoritária entre os k vizinhos mais próximos**.
- **Não tem fase de "treinamento" tradicional** — é um algoritmo *lazy* (baseado em instância), guarda os dados e só computa na hora da predição.
- Sensível à **escala das features** e à **maldição da dimensionalidade**.

⚠️ **Pegadinha:** k pequeno → overfitting (modelo muito sensível a ruído); k grande → underfitting (fronteira de decisão muito suave, ignora padrões locais).

### 2.3 Árvores de Decisão
- Divide o espaço de features em regiões através de **perguntas binárias sucessivas** (ex.: "idade > 30?").
- Critérios de divisão: **Gini** ou **Entropia/Ganho de Informação** (classificação); **erro quadrático** (regressão).
- Fácil de interpretar, mas **tende a overfitting** se crescer demais (sem *pruning*/poda ou profundidade máxima).

### 2.4 Random Forest
- **Ensemble** de várias árvores de decisão treinadas em subamostras diferentes dos dados (*bagging*) e de features (*feature bagging*).
- Reduz a variância em relação a uma árvore isolada.
- Predição final: **votação majoritária** (classificação) ou **média** (regressão).

⚠️ **Pegadinha:** achar que Random Forest elimina totalmente o overfitting — ele **reduz a variância**, mas ainda pode overfitar dados muito ruidosos ou se as árvores forem muito profundas e correlacionadas.

### 2.5 SVM (Support Vector Machine)
- Busca o **hiperplano que maximiza a margem** entre as classes.
- Pontos mais próximos da fronteira = **vetores de suporte**.
- Com o **kernel trick** (ex.: RBF, polinomial), consegue criar fronteiras **não-lineares** sem calcular explicitamente o espaço transformado.

⚠️ **Pegadinha:** SVM é sensível à **escala das features** (assim como KNN) — sempre normalizar antes.

### 2.6 Naive Bayes
- Baseado no **Teorema de Bayes**, assumindo **independência condicional** entre as features (daí "naive"/ingênuo).
- Muito usado em classificação de texto (ex.: filtro de spam).

⚠️ **Pegadinha:** a suposição de independência entre features **raramente é verdadeira na prática**, mas o modelo costuma funcionar bem mesmo assim — prova pode pedir para você explicar esse paradoxo.

### 2.7 Boosting (XGBoost, Gradient Boosting, AdaBoost)
- Ensemble **sequencial**: cada novo modelo (geralmente árvore fraca) tenta corrigir os **erros dos modelos anteriores**.
- Diferença-chave em relação ao Random Forest: Random Forest é **paralelo/bagging** (árvores independentes); Boosting é **sequencial** (árvores dependentes, focadas nos erros).

⚠️ **Pegadinha número 1 de prova:** confundir Bagging com Boosting — Bagging reduz **variância** (treina em paralelo, dados independentes); Boosting reduz **bias** (treina em sequência, focando nos erros residuais).

---

## 3. Modelos de Regressão

### 3.1 Regressão Linear
- Modela y como combinação linear das features: y = β0 + β1·x1 + ... + βn·xn.
- Estimado geralmente por **Mínimos Quadrados Ordinários (OLS)**.
- Pressupostos clássicos: **linearidade**, **homocedasticidade** (variância constante dos erros), **independência dos erros**, **normalidade dos resíduos**, **ausência de multicolinearidade**.

⚠️ **Pegadinha:** cobrar os pressupostos do OLS é comum — principalmente **multicolinearidade** (quando features são correlacionadas entre si, os coeficientes ficam instáveis).

### 3.2 Ridge e Lasso (Regularização)
- **Ridge (L2):** adiciona penalidade proporcional ao **quadrado** dos coeficientes → encolhe coeficientes, mas **não zera** nenhum.
- **Lasso (L1):** adiciona penalidade proporcional ao **valor absoluto** dos coeficientes → pode **zerar** coeficientes, funcionando como **seleção de features**.

⚠️ **Pegadinha número 1 (muito cobrada):** trocar Ridge por Lasso na explicação de "seleção automática de variáveis" — só o **Lasso** zera coeficientes; Ridge apenas os reduz, mantendo todos no modelo.

---

## 4. Métricas de Avaliação para Classificação

### 4.1 Matriz de Confusão — base de tudo
| | Previsto Positivo | Previsto Negativo |
|---|---|---|
| **Real Positivo** | Verdadeiro Positivo (VP) | Falso Negativo (FN) |
| **Real Negativo** | Falso Positivo (FP) | Verdadeiro Negativo (VN) |

### 4.2 Métricas derivadas

| Métrica | Fórmula | O que responde |
|---|---|---|
| **Acurácia** | (VP+VN) / Total | "De tudo, quanto acertei?" |
| **Precisão (Precision)** | VP / (VP+FP) | "Dos que eu disse que eram positivos, quantos realmente eram?" |
| **Recall (Sensibilidade/Revocação)** | VP / (VP+FN) | "Dos que realmente eram positivos, quantos eu capturei?" |
| **F1-Score** | 2 · (Precisão · Recall) / (Precisão + Recall) | Média harmônica entre Precisão e Recall |
| **Especificidade** | VN / (VN+FP) | "Dos que realmente eram negativos, quantos eu identifiquei corretamente?" |

⚠️ **Pegadinha número 1 (a mais clássica de todas as provas de ML):** usar **acurácia** em datasets **desbalanceados**. Exemplo: se 95% dos casos são "não-fraude" e o modelo sempre prevê "não-fraude", ele tem **95% de acurácia** e é completamente inútil. Nesse cenário, **Precisão, Recall e F1** são muito mais informativos.

⚠️ **Pegadinha número 2:** trocar Precisão com Recall na hora da prova. Truque de memorização:
- **Precisão** = foco no que eu **previ como positivo** (evitar falsos positivos) → importante quando **FP é caro** (ex.: marcar e-mail legítimo como spam).
- **Recall** = foco no que **realmente é positivo** (evitar falsos negativos) → importante quando **FN é caro** (ex.: deixar passar um câncer / uma fraude).

### 4.3 Curva ROC e AUC
- **ROC:** plota **Taxa de Verdadeiro Positivo (Recall)** vs. **Taxa de Falso Positivo** em diferentes limiares (thresholds) de classificação.
- **AUC (Area Under the Curve):** resume a curva em um número — 0.5 = modelo aleatório, 1.0 = classificador perfeito.

⚠️ **Pegadinha:** ROC/AUC podem ser **enganosos em datasets muito desbalanceados** — nesse caso, prefere-se a **curva Precision-Recall (PR-AUC)**.

### 4.4 Log-Loss (Entropia Cruzada)
- Mede a qualidade das **probabilidades previstas**, não só da classe final.
- Penaliza fortemente previsões **confiantes e erradas** (ex.: prever 99% de chance de ser positivo quando é negativo).

---

## 5. Métricas de Avaliação para Regressão

| Métrica | Fórmula (conceitual) | Característica |
|---|---|---|
| **MAE (Mean Absolute Error)** | Média dos erros absolutos | Robusto a outliers |
| **MSE (Mean Squared Error)** | Média dos erros ao quadrado | Penaliza fortemente erros grandes |
| **RMSE (Root MSE)** | Raiz do MSE | Mesma unidade do y original |
| **R² (Coeficiente de Determinação)** | 1 − (SQResidual/SQTotal) | Proporção da variância explicada pelo modelo |

⚠️ **Pegadinha número 1:** MSE/RMSE são **muito sensíveis a outliers** (por elevarem o erro ao quadrado) — se o dataset tem outliers relevantes, o MAE é mais robusto.

⚠️ **Pegadinha número 2:** R² **sempre aumenta (ou mantém) ao adicionar mais variáveis**, mesmo que irrelevantes — por isso existe o **R² ajustado**, que penaliza a inclusão de variáveis que não melhoram o modelo de fato.

---

## 6. Overfitting, Underfitting e Validação

- **Overfitting:** modelo memoriza o treino, mas generaliza mal (alta variância).
- **Underfitting:** modelo é simples demais para capturar o padrão (alto bias).
- **Trade-off Bias-Variância:** é o equilíbrio central de todo modelo supervisionado.

**Técnicas de validação:**
- **Train/Test Split:** separar dados de treino e teste.
- **Cross-Validation (k-fold):** dividir em k partes, treinar em k-1 e testar na restante, repetindo k vezes — reduz dependência de uma única divisão de dados.
- **Holdout de validação:** conjunto separado para ajuste de hiperparâmetros (evita "vazar" informação do teste).

⚠️ **Pegadinha número 1 (recorrente):** usar o **conjunto de teste** para escolher hiperparâmetros. Isso gera **data leakage** — o conjunto de teste deve ser usado **só uma vez, no final**, para estimar a performance real. Hiperparâmetros se ajustam com validação (ou cross-validation no treino).

⚠️ **Pegadinha número 2:** aplicar normalização/padronização (`fit`) usando **todo o dataset antes do split** — isso "vaza" informação do teste para o treino. O correto é ajustar (`fit`) o scaler **só no treino** e depois aplicar (`transform`) no teste.

---

## 7. Quadro-Resumo para Revisão Rápida

| Se a prova perguntar sobre... | Pense em... |
|---|---|
| Dataset desbalanceado | Não confiar só na acurácia → usar Precisão, Recall, F1, PR-AUC |
| FN é mais caro que FP | Priorizar **Recall** (ex.: diagnóstico médico) |
| FP é mais caro que FN | Priorizar **Precisão** (ex.: filtro de spam) |
| Seleção automática de variáveis | **Lasso** (L1), não Ridge |
| Reduzir variância de um modelo | **Bagging** / Random Forest |
| Reduzir bias de um modelo | **Boosting** |
| Erro sensível a outliers | Preferir **MAE** ao invés de MSE/RMSE |
| R² aumenta mas modelo não melhorou de fato | Usar **R² ajustado** |
| Vazamento de dados (data leakage) | Normalizar só com dados de treino; nunca usar teste para tunar hiperparâmetros |
| Modelo "lazy", sem fase de treino real | KNN |
| Fronteira de decisão não-linear sem transformar features manualmente | SVM com **kernel trick** |

---

## 8. Aplicação Profissional (além da prova)

- **Concessão de crédito:** Regressão Logística ou XGBoost para prever risco de inadimplência (aqui Recall alto é crítico para não liberar crédito a maus pagadores).
- **Diagnóstico médico:** priorizar Recall (evitar falsos negativos — deixar passar uma doença é mais grave que um falso alarme).
- **Precificação dinâmica (ex.: imóveis, passagens):** modelos de regressão (Linear, Random Forest Regressor, Gradient Boosting).
- **Detecção de churn (cancelamento de clientes):** classificação binária, geralmente com dataset desbalanceado — F1 e AUC são as métricas mais usadas no mercado, não a acurácia.
- Na prática profissional, a escolha da métrica **depende do custo de negócio de cada tipo de erro** — é comum times de dados discutirem com o time de produto/negócio **qual erro é mais caro** antes de decidir a métrica-alvo do modelo.

---

## 9. Perguntas típicas de prova (para se testar)

1. Por que a acurácia pode ser uma métrica perigosa em datasets desbalanceados? Dê um exemplo.
2. Explique a diferença conceitual entre Precisão e Recall com um exemplo de negócio para cada.
3. Qual a diferença fundamental entre Bagging e Boosting em termos de bias e variância?
4. Por que apenas o Lasso (e não o Ridge) pode ser usado como técnica de seleção de features?
5. O que é data leakage e cite dois exemplos comuns de como ele ocorre no pipeline de ML.
6. Por que o RMSE é mais sensível a outliers do que o MAE?
