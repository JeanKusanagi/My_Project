# 30 Questões de Múltipla Escolha
## Aprendizado de Máquina Supervisionado: Modelos e Métricas de Avaliação

---

### 1. O que caracteriza o aprendizado supervisionado?
a) Os dados não possuem nenhuma estrutura conhecida
b) O modelo aprende a partir de exemplos com entradas (X) e saídas (rótulos/y) conhecidas
c) Não há necessidade de dados de treinamento
d) O algoritmo descobre grupos sem qualquer informação prévia

**Gabarito: b)** No aprendizado supervisionado, o modelo é treinado com pares (X, y), em que y é a variável-alvo (rótulo ou valor numérico), e o objetivo é aprender uma função que generalize essa relação para novos dados.

---

### 2. Os dois principais tipos de problemas em aprendizado supervisionado são:
a) Clustering e associação
b) Classificação e regressão
c) Redução de dimensionalidade e clustering
d) Aprendizado por reforço e clustering

**Gabarito: b)** Classificação prevê uma variável categórica (classes), enquanto regressão prevê uma variável numérica contínua. Ambos são supervisionados, pois exigem rótulos/valores conhecidos durante o treinamento.

---

### 3. Na Regressão Linear Simples, o objetivo do método dos Mínimos Quadrados Ordinários (OLS) é:
a) Maximizar o erro entre valores previstos e observados
b) Minimizar a soma dos quadrados dos resíduos (diferença entre valores observados e previstos)
c) Maximizar o número de variáveis do modelo
d) Igualar a média dos resíduos a 1

**Gabarito: b)** O OLS encontra os coeficientes que minimizam a soma dos quadrados das diferenças entre os valores observados (y) e os valores previstos pelo modelo (ŷ).

---

### 4. Qual métrica de regressão penaliza mais fortemente erros grandes, por elevá-los ao quadrado?
a) MAE (Erro Absoluto Médio)
b) MSE (Erro Quadrático Médio)
c) R² (Coeficiente de Determinação)
d) MAPE (Erro Percentual Absoluto Médio)

**Gabarito: b)** O MSE eleva cada erro ao quadrado antes de calcular a média, o que penaliza desproporcionalmente erros grandes (outliers), diferente do MAE, que trata todos os erros de forma linear.

---

### 5. O RMSE (Root Mean Squared Error) é vantajoso em relação ao MSE porque:
a) É sempre menor que o MSE
b) Está na mesma unidade da variável-alvo, facilitando a interpretação
c) Não é sensível a outliers
d) Não pode ser comparado entre diferentes modelos

**Gabarito: b)** Como o RMSE é a raiz quadrada do MSE, seu valor volta à escala original da variável de saída, tornando a métrica mais interpretável (ex.: erro médio em reais, em vez de reais ao quadrado).

---

### 6. O coeficiente de determinação R² indica:
a) A proporção da variância da variável-alvo explicada pelo modelo
b) O número de variáveis independentes do modelo
c) A acurácia de um modelo de classificação
d) O erro absoluto médio do modelo

**Gabarito: a)** O R² varia (geralmente) entre 0 e 1 e representa a fração da variabilidade total de y que é explicada pelas variáveis preditoras do modelo. Valores próximos de 1 indicam melhor ajuste.

---

### 7. Um R² ajustado (Adjusted R²) é preferível ao R² comum quando:
a) O modelo tem apenas uma variável preditora
b) Se deseja comparar modelos com números diferentes de variáveis preditoras, penalizando a adição de variáveis irrelevantes
c) Os dados são categóricos
d) O modelo é de classificação, não de regressão

**Gabarito: b)** O R² comum tende a aumentar (ou nunca diminuir) conforme se adicionam variáveis, mesmo irrelevantes. O R² ajustado penaliza esse aumento artificial, sendo mais adequado para comparar modelos com diferentes quantidades de preditores.

---

### 8. Em um problema de classificação binária, a Matriz de Confusão organiza os resultados em:
a) Média, mediana, moda e desvio padrão
b) Verdadeiros Positivos, Verdadeiros Negativos, Falsos Positivos e Falsos Negativos
c) MSE, RMSE, MAE e R²
d) Apenas taxa de acerto e taxa de erro

**Gabarito: b)** A matriz de confusão cruza as classes previstas com as reais, gerando quatro quadrantes: VP (verdadeiro positivo), VN (verdadeiro negativo), FP (falso positivo) e FN (falso negativo), base para diversas métricas de classificação.

---

### 9. A Acurácia é calculada como:
a) VP / (VP + FP)
b) (VP + VN) / (VP + VN + FP + FN)
c) VP / (VP + FN)
d) 2 × (Precisão × Recall) / (Precisão + Recall)

**Gabarito: b)** A acurácia mede a proporção de previsões corretas (positivas e negativas) sobre o total de casos. Ela pode ser uma métrica enganosa em datasets desbalanceados.

---

### 10. Por que a Acurácia pode ser uma métrica inadequada em datasets desbalanceados?
a) Porque não pode ser calculada nesses casos
b) Porque um modelo que sempre prevê a classe majoritária pode obter acurácia alta sem realmente aprender a distinguir as classes
c) Porque a acurácia só existe para regressão
d) Porque ela ignora completamente os verdadeiros positivos

**Gabarito: b)** Em um dataset com 95% de exemplos de uma classe, um modelo "ingênuo" que sempre prevê essa classe atinge 95% de acurácia sem capturar nenhum padrão útil, escondendo um desempenho ruim na classe minoritária.

---

### 11. A Precisão (Precision) é definida como:
a) VP / (VP + FN)
b) VP / (VP + FP)
c) (VP + VN) / Total
d) FP / (FP + VN)

**Gabarito: b)** Precisão mede, dentre todos os casos previstos como positivos, quantos realmente eram positivos. É importante quando o custo de falsos positivos é alto (ex.: marcar e-mail legítimo como spam).

---

### 12. O Recall (Revocação ou Sensibilidade) é definido como:
a) VP / (VP + FP)
b) VP / (VP + FN)
c) VN / (VN + FP)
d) (VP + VN) / Total

**Gabarito: b)** Recall mede, dentre todos os casos que realmente eram positivos, quantos o modelo conseguiu identificar corretamente. É crucial quando o custo de falsos negativos é alto (ex.: diagnóstico de doenças graves).

---

### 13. O F1-Score é:
a) A média aritmética simples entre Precisão e Recall
b) A média harmônica entre Precisão e Recall, equilibrando ambas as métricas
c) Igual à acurácia em qualquer situação
d) Calculado apenas para problemas de regressão

**Gabarito: b)** F1 = 2 × (Precisão × Recall) / (Precisão + Recall). A média harmônica penaliza mais fortemente valores baixos em qualquer uma das duas métricas, sendo útil quando se busca equilíbrio entre Precisão e Recall.

---

### 14. A curva ROC (Receiver Operating Characteristic) plota:
a) Precisão versus Recall em diferentes limiares (thresholds)
b) Taxa de Verdadeiros Positivos (Recall) versus Taxa de Falsos Positivos, em diferentes limiares de classificação
c) Erro quadrático médio versus número de épocas de treinamento
d) Acurácia versus tamanho do conjunto de treino

**Gabarito: b)** A curva ROC mostra como a Taxa de Verdadeiros Positivos (TPR/Recall) e a Taxa de Falsos Positivos (FPR) variam conforme se altera o limiar de decisão do classificador.

---

### 15. A métrica AUC (Area Under the Curve), da curva ROC, indica:
a) A área sob a curva de erro do modelo
b) A capacidade geral do modelo de distinguir entre as classes positiva e negativa, independentemente do limiar escolhido
c) O tempo de treinamento do modelo
d) O número de falsos negativos

**Gabarito: b)** AUC varia de 0 a 1 (0,5 equivale a um classificador aleatório); quanto mais próxima de 1, melhor a capacidade do modelo de separar as classes em todos os limiares possíveis.

---

### 16. Para problemas de classificação com forte desbalanceamento de classes, a curva Precision-Recall costuma ser preferida à curva ROC porque:
a) É mais fácil de calcular
b) Foca no desempenho relativo à classe positiva (minoritária), sendo menos otimista quando há muitos verdadeiros negativos triviais
c) Não depende do limiar de decisão
d) Substitui completamente a matriz de confusão

**Gabarito: b)** Como a curva ROC inclui a Taxa de Falsos Positivos (que usa VN no denominador), ela pode parecer "otimista" quando há muitos negativos verdadeiros fáceis de acertar. A curva Precision-Recall, por focar em VP, FP e FN, é mais informativa em cenários desbalanceados.

---

### 17. A Regressão Logística é utilizada principalmente para:
a) Prever valores numéricos contínuos sem limites
b) Problemas de classificação, modelando a probabilidade de pertencimento a uma classe via função sigmoide/logit
c) Redução de dimensionalidade
d) Agrupamento de dados sem rótulos

**Gabarito: b)** Apesar do nome "regressão", a Regressão Logística é um algoritmo de classificação: ela modela a probabilidade de um exemplo pertencer a uma classe usando a função sigmoide (logit), transformando uma combinação linear das variáveis em um valor entre 0 e 1.

---

### 18. Em Árvores de Decisão, o critério de Gini (Gini Impurity) e a Entropia são usados para:
a) Definir o tamanho máximo da árvore
b) Medir a "pureza" dos nós e escolher a melhor divisão (split) em cada etapa
c) Calcular a acurácia final do modelo
d) Normalizar as variáveis antes do treinamento

**Gabarito: b)** Tanto o índice de Gini quanto a Entropia medem o grau de mistura de classes em um nó; a árvore escolhe, em cada divisão, o atributo e o ponto de corte que minimizam a impureza resultante nos nós filhos.

---

### 19. O overfitting (sobreajuste) em Árvores de Decisão pode ser controlado por meio de:
a) Aumentar indefinidamente a profundidade da árvore
b) Poda (pruning), limitação de profundidade máxima ou número mínimo de amostras por nó
c) Remover todas as variáveis categóricas
d) Utilizar apenas uma variável preditora

**Gabarito: b)** Técnicas como pruning (poda), definir `max_depth`, `min_samples_split` ou `min_samples_leaf` ajudam a limitar a complexidade da árvore, reduzindo o risco de memorizar ruído do conjunto de treino.

---

### 20. O Random Forest é um método de ensemble que:
a) Combina várias árvores de decisão treinadas em subconjuntos aleatórios dos dados e variáveis, agregando suas previsões
b) Utiliza apenas uma única árvore muito profunda
c) É exclusivo para problemas de regressão
d) Não pode ser usado para calcular importância de variáveis

**Gabarito: a)** O Random Forest usa bagging (bootstrap aggregating): treina múltiplas árvores em amostras bootstrap dos dados, considerando subconjuntos aleatórios de variáveis em cada split, e agrega as previsões (votação para classificação, média para regressão), reduzindo variância.

---

### 21. O Gradient Boosting (ex.: XGBoost, LightGBM) constrói o modelo de forma:
a) Paralela e independente, como no Random Forest
b) Sequencial, em que cada nova árvore tenta corrigir os erros (resíduos) cometidos pelas árvores anteriores
c) Sem uso de nenhuma função de perda
d) Idêntica à Regressão Linear

**Gabarito: b)** No boosting, os modelos (geralmente árvores) são treinados sequencialmente, cada um focando em corrigir os erros/resíduos do conjunto anterior, otimizando uma função de perda por meio de gradiente descendente funcional.

---

### 22. O algoritmo K-Nearest Neighbors (KNN) classifica uma nova instância com base em:
a) Uma função linear ajustada previamente
b) A classe majoritária entre os k vizinhos mais próximos no espaço de atributos
c) O cálculo de probabilidades via distribuição gaussiana
d) A divisão recursiva do espaço de atributos em nós

**Gabarito: b)** O KNN é um método baseado em instância (não paramétrico): para classificar um novo ponto, observa-se a classe mais frequente entre os k vizinhos mais próximos (segundo alguma métrica de distância, como euclidiana).

---

### 23. Uma desvantagem do KNN é:
a) Não conseguir lidar com problemas de classificação
b) Ser custoso computacionalmente em tempo de previsão, especialmente em datasets grandes, além de ser sensível à escala das variáveis
c) Sempre apresentar underfitting
d) Não poder ser usado para regressão

**Gabarito: b)** Como o KNN calcula distâncias para todos (ou muitos) os pontos de treino a cada nova previsão, ele pode ser lento para bases grandes; além disso, atributos em escalas diferentes distorcem as distâncias se não houver normalização prévia.

---

### 24. As Máquinas de Vetores de Suporte (SVM) para classificação buscam:
a) Minimizar o número de vizinhos considerados
b) Encontrar o hiperplano que maximiza a margem de separação entre as classes
c) Agrupar pontos por densidade
d) Ajustar uma função de distribuição gaussiana aos dados

**Gabarito: b)** O SVM busca o hiperplano de separação que maximiza a margem (distância) entre as classes, utilizando os vetores de suporte (pontos mais próximos da fronteira) para definir essa margem.

---

### 25. O uso do "kernel trick" em SVMs permite:
a) Reduzir a dimensionalidade dos dados de entrada
b) Projetar implicitamente os dados em um espaço de maior dimensão, permitindo separações não-lineares sem calcular explicitamente essa transformação
c) Eliminar a necessidade de normalizar os dados
d) Transformar o problema em não-supervisionado

**Gabarito: b)** Kernels (ex.: RBF, polinomial) permitem que o SVM opere como se os dados estivessem em um espaço de maior dimensão, capturando relações não-lineares, sem a necessidade de calcular explicitamente as coordenadas transformadas (truque do produto interno).

---

### 26. O que caracteriza o underfitting (subajuste) de um modelo supervisionado?
a) O modelo é excessivamente complexo e memoriza o conjunto de treino
b) O modelo é excessivamente simples e não consegue capturar os padrões relevantes, apresentando desempenho ruim tanto no treino quanto no teste
c) O modelo apresenta desempenho perfeito em qualquer conjunto de dados
d) O underfitting só ocorre em problemas de classificação

**Gabarito: b)** No underfitting, o modelo tem alta viés (bias) e baixa capacidade de representar a relação real entre X e y, resultando em erro elevado tanto nos dados de treino quanto nos de teste/validação.

---

### 27. O overfitting (sobreajuste), por sua vez, caracteriza-se por:
a) Bom desempenho no treino e desempenho significativamente pior em dados novos (teste/validação), devido à alta variância do modelo
b) Erro alto tanto no treino quanto no teste
c) Ausência de qualquer erro do modelo
d) Ocorrer apenas em modelos lineares

**Gabarito: a)** No overfitting, o modelo "memoriza" particularidades e ruído do conjunto de treino (alta variância), obtendo desempenho excelente nesses dados, mas generalizando mal para dados novos.

---

### 28. A validação cruzada (cross-validation), como o método k-fold, é utilizada para:
a) Eliminar a necessidade de um conjunto de teste
b) Obter uma estimativa mais robusta do desempenho do modelo, treinando e testando em diferentes divisões dos dados
c) Aumentar artificialmente a acurácia do modelo
d) Substituir a necessidade de qualquer métrica de avaliação

**Gabarito: b)** No k-fold cross-validation, os dados são divididos em k partes; o modelo é treinado em k-1 partes e testado na parte restante, repetindo o processo k vezes. A média (e desvio) dos resultados fornece uma estimativa mais robusta e menos dependente de uma única divisão treino/teste.

---

### 29. O trade-off entre viés (bias) e variância (variance) descreve que:
a) É sempre possível reduzir simultaneamente o viés e a variância sem qualquer custo
b) Modelos muito simples tendem a ter alto viés (underfitting), enquanto modelos muito complexos tendem a ter alta variância (overfitting), e o objetivo é equilibrar ambos
c) O viés só existe em problemas de regressão
d) A variância não está relacionada à complexidade do modelo

**Gabarito: b)** Esse é um dos conceitos centrais de aprendizado supervisionado: aumentar a complexidade do modelo tende a reduzir o viés, mas pode aumentar a variância (sensibilidade a pequenas mudanças nos dados de treino), e vice-versa. Bons modelos buscam o ponto de equilíbrio que minimiza o erro total de generalização.

---

### 30. Ao comparar diferentes modelos supervisionados para um mesmo problema, é considerado boa prática:
a) Escolher sempre o modelo mais complexo disponível, independentemente do desempenho
b) Avaliar os modelos usando métricas apropriadas ao problema (ex.: F1/AUC para classificação desbalanceada, RMSE/R² para regressão) em dados de validação/teste não usados no treinamento
c) Avaliar apenas o desempenho no próprio conjunto de treino
d) Escolher o modelo com maior número de parâmetros treináveis

**Gabarito: b)** A comparação justa entre modelos deve usar métricas alinhadas ao objetivo do problema (considerando, por exemplo, desbalanceamento de classes ou sensibilidade a outliers) e ser feita em dados que o modelo não viu durante o treinamento, evitando conclusões enganosas causadas por overfitting.

---

*Documento gerado para fins educacionais sobre Aprendizado de Máquina Supervisionado.*
