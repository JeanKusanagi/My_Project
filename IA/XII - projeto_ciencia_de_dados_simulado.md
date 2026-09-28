# SIMULADO — Projeto de Ciência de Dados
### Coleta, preparação, modelagem, avaliação e implantação de modelos

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas clássicas do ciclo de vida de projetos de Ciência de Dados.

---

**1.** O modelo de referência **CRISP-DM** (Cross-Industry Standard Process for Data Mining) descreve o ciclo de vida de um projeto de dados como um processo:

a) Estritamente linear e sequencial, sem qualquer possibilidade de retorno a etapas anteriores<br>
b) Iterativo, composto por fases como compreensão do negócio, compreensão dos dados, preparação dos dados, modelagem, avaliação e implantação, com possibilidade de retorno a fases anteriores conforme necessário<br>
c) Composto por uma única fase, focada exclusivamente na construção do modelo estatístico<br>
d) Aplicável apenas a projetos de aprendizado supervisionado

> **Gabarito: b.** O CRISP-DM é reconhecido justamente por seu caráter iterativo e cíclico — é comum, por exemplo, voltar da fase de modelagem para a de preparação de dados ao identificar problemas de qualidade não percebidos anteriormente.

---

**2.** **(Pegadinha)** Segundo a lógica do CRISP-DM e a prática comum em projetos de Ciência de Dados, a primeira fase de um projeto deveria ser:

a) A modelagem, pois é a etapa mais tecnicamente interessante<br>
b) A compreensão do negócio (business understanding), definindo claramente o problema a ser resolvido e os objetivos do projeto, antes mesmo de qualquer exploração de dados<br>
c) A implantação (deployment), para já validar a infraestrutura disponível<br>
d) A avaliação do modelo, para saber quais métricas serão utilizadas depois

> **Gabarito: b.** Pegadinha: é comum, especialmente entre iniciantes, "pular direto" para dados e modelagem — mas a prática recomendada é começar pela compreensão clara do problema de negócio e dos objetivos, evitando o retrabalho de construir modelos tecnicamente corretos, porém que não respondem à pergunta certa.

---

**3.** Na etapa de **coleta de dados**, uma preocupação relevante e frequentemente citada é:

a) Garantir que os dados sejam coletados de forma representativa do problema e do público de interesse, evitando vieses de amostragem que possam comprometer as conclusões do projeto<br>
b) Coletar exclusivamente dados numéricos, descartando qualquer dado textual ou categórico<br>
c) Utilizar sempre a maior quantidade possível de fontes de dados, independentemente de sua qualidade ou relevância<br>
d) Ignorar completamente questões de privacidade e conformidade legal na coleta de dados

> **Gabarito: a.** A representatividade da amostra em relação ao problema real é fundamental — dados coletados de forma enviesada (por exemplo, apenas de um subgrupo específico da população) podem comprometer a validade e a generalização de qualquer modelo construído a partir deles.

---

**4.** **(Pegadinha)** Um cientista de dados afirma: "Quanto mais dados eu coletar, sempre melhor será o modelo resultante, independentemente da qualidade desses dados." Essa afirmação está:

a) Correta, pois quantidade de dados é o único fator relevante para a qualidade de um modelo<br>
b) Incorreta — embora mais dados frequentemente ajudem, a **qualidade** dos dados (representatividade, ausência de erros sistemáticos, relevância para o problema) é igualmente ou mais importante do que a quantidade; grandes volumes de dados de baixa qualidade podem, inclusive, piorar o desempenho e a confiabilidade do modelo<br>
c) Correta, desde que os dados sejam armazenados em formato CSV<br>
d) Incorreta, mas apenas porque mais dados sempre aumentam o tempo de treinamento

> **Gabarito: b.** Pegadinha resumida na máxima "garbage in, garbage out" (lixo entra, lixo sai): volume de dados não compensa, por si só, problemas sistemáticos de qualidade, representatividade ou relevância dos dados coletados.

---

**5.** Na etapa de **preparação/limpeza de dados**, o tratamento de **valores ausentes (missing values)** pode envolver, entre outras estratégias:

a) Ignorar sempre a existência de valores ausentes, deixando o modelo lidar com eles automaticamente, sem qualquer tratamento<br>
b) Remover as observações/linhas com valores ausentes, imputar valores (como média, mediana, moda ou técnicas mais sofisticadas) ou utilizar métodos que lidem nativamente com ausência de dados, sendo a escolha dependente do contexto, da proporção de dados ausentes e do mecanismo de ausência<br>
c) Substituir automaticamente todo valor ausente por zero, em qualquer contexto, sem análise adicional<br>
d) Converter todos os valores ausentes em texto livre, sem qualquer padronização

> **Gabarito: b.** Não existe uma solução universal para valores ausentes — a estratégia adequada depende de fatores como a proporção de dados faltantes, se a ausência é aleatória ou sistemática, e o tipo de variável envolvida, entre outros aspectos do contexto do problema.

---

**6.** **(Pegadinha)** Um analista decide substituir automaticamente todo valor ausente numérico por zero, sem qualquer análise adicional sobre o significado dessa ausência. Essa prática pode ser problemática porque:

a) É sempre a melhor prática recomendada em qualquer cenário, sem exceções<br>
b) O valor zero pode não representar adequadamente a ausência de informação, introduzindo um viés artificial nos dados — por exemplo, em uma variável de "idade" ou "salário", um valor ausente substituído por zero pode ser interpretado incorretamente pelo modelo como um valor real e extremo, distorcendo padrões e relações estatísticas<br>
c) Zero é sempre um valor neutro e sem qualquer impacto estatístico, independentemente da variável<br>
d) Essa prática elimina completamente qualquer necessidade de análise exploratória de dados

> **Gabarito: b.** Pegadinha: substituir "ausência de dado" por um valor numérico específico (como zero) sem refletir sobre o significado dessa escolha pode introduzir distorções sérias, especialmente quando zero é um valor numericamente plausível e diferente de "informação faltante".

---

**7.** **Outliers** (valores atípicos/discrepantes), em um conjunto de dados, são:

a) Sempre erros de digitação que devem ser removidos automaticamente, sem análise<br>
b) Observações que se desviam significativamente do padrão geral dos demais dados, podendo representar tanto erros de coleta/digitação quanto fenômenos raros, porém legítimos e relevantes para o problema — por isso, exigem investigação contextual antes de qualquer decisão sobre tratamento<br>
c) Um sinônimo técnico de "valores ausentes"<br>
d) Sempre benéficos para o desempenho de qualquer modelo, sem exceção

> **Gabarito: b.** A identificação de um valor como outlier não implica automaticamente que ele deva ser removido — pode representar um erro real de coleta, mas também pode ser um evento raro, porém verdadeiro e informativo (como uma fraude, por exemplo), exigindo análise cuidadosa antes de qualquer decisão.

---

**8.** **Feature engineering** (engenharia de atributos/características) refere-se ao processo de:

a) Selecionar exclusivamente o algoritmo de aprendizado de máquina a ser utilizado<br>
b) Criar, transformar ou selecionar variáveis (features) a partir dos dados brutos, de forma a melhorar a capacidade do modelo de capturar padrões relevantes para o problema<br>
c) Implantar o modelo final em produção<br>
d) Calcular exclusivamente métricas de avaliação do modelo já treinado

> **Gabarito: b.** Feature engineering é o processo criativo e analítico de transformar dados brutos em representações (variáveis) mais úteis e informativas para o modelo — muitas vezes tão ou mais importante para o desempenho final do que a escolha do algoritmo em si.

---

**9.** **(Pegadinha)** O termo **data leakage** (vazamento de dados), em Ciência de Dados, refere-se a:

a) Um problema exclusivamente de segurança da informação, relacionado ao vazamento de dados sensíveis para terceiros não autorizados<br>
b) A situação em que informações do conjunto de teste (ou informações que só estariam disponíveis no momento da previsão real, no futuro) acabam sendo utilizadas, direta ou indiretamente, durante o treinamento do modelo, produzindo uma avaliação de desempenho artificialmente otimista, que não se sustenta quando o modelo é utilizado em produção<br>
c) Um sinônimo de overfitting, sem qualquer distinção conceitual<br>
d) Um problema que só ocorre em modelos de deep learning, nunca em modelos estatísticos tradicionais

> **Gabarito: b.** Pegadinha importante: apesar do nome sugerir um problema de segurança, data leakage em Ciência de Dados é um problema metodológico — o vazamento de informação do futuro (ou do conjunto de teste) para o treinamento, o que infla artificialmente as métricas de avaliação e compromete a validade real do modelo.

---

**10.** **(Pegadinha)** Um exemplo clássico de **data leakage** ocorre quando:

a) Um cientista de dados divide corretamente os dados em treino e teste antes de qualquer pré-processamento<br>
b) A normalização (ou outra transformação estatística, como imputação de valores ausentes) dos dados é calculada utilizando **todo** o conjunto de dados (incluindo o conjunto de teste) antes da divisão treino/teste, fazendo com que informações estatísticas do conjunto de teste "vazem" indevidamente para o processo de treinamento<br>
c) O modelo é avaliado exclusivamente no conjunto de treino, sem qualquer conjunto de teste separado<br>
d) O cientista de dados utiliza validação cruzada (cross-validation) corretamente implementada

> **Gabarito: b.** Pegadinha muito comum na prática: calcular estatísticas de normalização, imputação ou seleção de features usando o conjunto completo (antes de separar treino e teste) é uma forma sutil, porém real, de vazamento de dados — a prática correta é calcular essas estatísticas apenas no conjunto de treino e aplicá-las, depois, ao conjunto de teste.

---

**11.** A divisão dos dados em **conjunto de treino e conjunto de teste** tem como principal objetivo:

a) Reduzir o tamanho total do conjunto de dados disponível<br>
b) Eliminar completamente a necessidade de qualquer validação futura do modelo<br>
c) Permitir avaliar a capacidade de generalização do modelo em dados não vistos durante o treinamento, simulando (de forma aproximada) o desempenho esperado do modelo em produção, sobre novos dados<br>
d) Garantir que o modelo memorize perfeitamente todos os exemplos de treino

> **Gabarito: c.** A separação treino/teste busca estimar, de forma mais honesta, como o modelo se comportará diante de dados novos (não utilizados no ajuste dos parâmetros), evitando avaliar o modelo apenas em dados que ele já "viu" durante o treinamento.

---

**12.** **Overfitting** (sobreajuste) ocorre quando um modelo:

a) Apresenta desempenho ruim tanto no conjunto de treino quanto no conjunto de teste<br>
b) Se ajusta excessivamente aos detalhes e ao ruído específicos do conjunto de treino, apresentando desempenho muito bom nesse conjunto, mas desempenho significativamente pior em dados novos (conjunto de teste ou produção), indicando baixa capacidade de generalização<br>
c) Nunca converge durante o processo de treinamento<br>
d) É sempre o resultado de um conjunto de dados de treino muito grande

> **Gabarito: b.** Overfitting é o cenário clássico de "decorar em vez de aprender": o modelo captura padrões específicos (inclusive ruído) do conjunto de treino que não se generalizam para novos dados, resultando em uma lacuna significativa entre desempenho no treino e no teste.

---

**13.** **(Pegadinha)** **Underfitting** (subajuste), por sua vez, é caracterizado por um modelo que:

a) Apresenta desempenho excelente no treino, mas desempenho ruim no teste — o oposto exato de overfitting<br>
b) Apresenta desempenho ruim tanto no conjunto de treino quanto no conjunto de teste, geralmente por ser excessivamente simples (com pouca capacidade) para capturar os padrões relevantes presentes nos dados<br>
c) É sempre preferível ao overfitting, em qualquer cenário, pois é mais "conservador"<br>
d) Ocorre exclusivamente quando o conjunto de dados de treino é excessivamente grande

> **Gabarito: b.** Pegadinha: é comum inverter os conceitos de overfitting e underfitting — enquanto overfitting apresenta ótimo desempenho no treino e ruim no teste, underfitting apresenta desempenho ruim **em ambos** os conjuntos, geralmente por o modelo ser simples ou mal ajustado demais para capturar a complexidade real dos dados.

---

**14.** A técnica de **validação cruzada (cross-validation)**, como o k-fold cross-validation, é utilizada principalmente para:

a) Aumentar artificialmente o tamanho do conjunto de dados original<br>
b) Obter uma estimativa mais robusta e menos dependente de uma única divisão treino/teste específica do desempenho do modelo, dividindo os dados em múltiplas partições (folds) e treinando/avaliando o modelo repetidamente em diferentes combinações dessas partições<br>
c) Substituir completamente a necessidade de um conjunto de teste final, isolado, antes da implantação em produção<br>
d) Ser aplicável exclusivamente a problemas de regressão, nunca de classificação

> **Gabarito: b.** A validação cruzada reduz a dependência de uma única divisão treino/teste (que pode ser "sortuda" ou "azarada" por acaso), fornecendo uma estimativa mais confiável e estável do desempenho esperado do modelo, especialmente útil também para comparação e ajuste de hiperparâmetros.

---

**15.** **(Pegadinha)** Sobre a relação entre **validação cruzada** e um **conjunto de teste final isolado (hold-out)**, é correto afirmar que:

a) A validação cruzada elimina totalmente a necessidade de qualquer conjunto de teste final separado, em qualquer cenário de projeto<br>
b) É uma boa prática manter um conjunto de teste final, completamente isolado do processo de treinamento e ajuste (inclusive da validação cruzada utilizada para tunar hiperparâmetros), para uma avaliação final e mais imparcial do modelo, já que utilizar a validação cruzada repetidamente para ajustar decisões de modelagem pode, sutilmente, "vazar" informação do processo de validação para as escolhas do modelo<br>
c) Um conjunto de teste final isolado nunca deve ser utilizado em conjunto com validação cruzada<br>
d) A validação cruzada é sinônimo exato de conjunto de teste final, sem qualquer distinção prática

> **Gabarito: b.** Pegadinha: embora a validação cruzada seja valiosa para ajuste de hiperparâmetros e seleção de modelos, utilizá-la repetidamente para tomar decisões pode, de forma sutil, introduzir um viés otimista — por isso, manter um conjunto de teste final, tocado apenas uma vez ao final do processo, é uma prática recomendada para uma avaliação mais honesta.

---

**16.** **Hiperparâmetros** de um modelo de aprendizado de máquina são:

a) Os mesmos que os parâmetros internos aprendidos automaticamente pelo modelo durante o treinamento (como os pesos de uma rede neural)<br>
b) Configurações definidas **antes** do processo de treinamento (como a profundidade máxima de uma árvore de decisão, a taxa de aprendizado, ou o número de vizinhos em KNN), que não são aprendidas diretamente pelos dados durante o ajuste padrão do modelo, mas que influenciam fortemente seu comportamento e desempenho<br>
c) Métricas de avaliação calculadas após o treinamento do modelo<br>
d) Um sinônimo de "features" (variáveis de entrada) do modelo

> **Gabarito: b.** Pegadinha implícita: é comum confundir parâmetros (aprendidos automaticamente durante o treinamento, como coeficientes de uma regressão ou pesos de uma rede neural) com hiperparâmetros (definidos externamente antes do treinamento, geralmente ajustados por técnicas como grid search, random search ou otimização bayesiana).

---

**17.** Na avaliação de um modelo de **classificação binária**, a **matriz de confusão** organiza os resultados em quatro categorias:

a) Média, mediana, moda e desvio padrão<br>
b) Verdadeiros Positivos (VP), Falsos Positivos (FP), Verdadeiros Negativos (VN) e Falsos Negativos (FN)<br>
c) Treino, validação, teste e produção<br>
d) Precisão, recall, F1-score e acurácia, diretamente

> **Gabarito: b.** A matriz de confusão organiza as previsões corretas e incorretas do modelo em relação às classes reais, servindo de base para calcular diversas métricas derivadas, como acurácia, precisão, recall e F1-score.

---

**18.** **(Pegadinha)** Em um problema de classificação com classes **fortemente desbalanceadas** (por exemplo, 99% dos casos pertencem à classe "negativo" e apenas 1% à classe "positivo", como na detecção de uma doença rara), a métrica de **acurácia** isoladamente:

a) É sempre a métrica mais adequada e suficiente para avaliar o modelo, independentemente do desbalanceamento<br>
b) Pode ser enganosa, pois um modelo "ingênuo" que sempre prevê a classe majoritária (negativo) alcançaria 99% de acurácia, apesar de nunca identificar corretamente nenhum caso da classe minoritária (positivo) — por isso, métricas como precisão, recall e F1-score, mais sensíveis ao desempenho na classe minoritária, costumam ser mais informativas nesse cenário<br>
c) Deixa de ser calculável matematicamente quando há desbalanceamento de classes<br>
d) É irrelevante em qualquer cenário de classificação, mesmo com classes balanceadas

> **Gabarito: b.** Pegadinha clássica e extremamente citada em Ciência de Dados: em cenários de forte desbalanceamento, um modelo trivial (que sempre prevê a classe majoritária) pode ter acurácia altíssima e, ainda assim, ser completamente inútil para o objetivo prático do problema — daí a importância de métricas complementares.

---

**19.** A métrica de **precisão (precision)**, em um problema de classificação, é definida como:

a) VP / (VP + FN) — a proporção de casos positivos reais que foram corretamente identificados<br>
b) VP / (VP + FP) — dentre todos os casos que o modelo classificou como positivos, a proporção que de fato era positiva<br>
c) (VP + VN) / Total — a proporção geral de acertos do modelo<br>
d) FP / (FP + VN)

> **Gabarito: b.** Precisão responde à pergunta: "de tudo que o modelo disse ser positivo, quanto realmente era positivo?" — é uma métrica especialmente relevante quando o custo de falsos positivos é alto (ex.: marcar um e-mail legítimo como spam).

---

**20.** **(Pegadinha)** A métrica de **recall** (também chamada de sensibilidade ou revocação), diferente da precisão, é definida como:

a) VP / (VP + FP), exatamente como a precisão<br>
b) VP / (VP + FN) — dentre todos os casos que realmente eram positivos, a proporção que o modelo conseguiu identificar corretamente como tal<br>
c) (VP + VN) / Total<br>
d) FN / (FN + VP), invertendo a fórmula correta

> **Gabarito: b.** Pegadinha: confundir precisão (foco nos casos que o modelo *chamou* de positivos) com recall (foco nos casos que *realmente são* positivos) é um erro muito comum — recall é especialmente relevante quando o custo de um falso negativo é alto (ex.: deixar de detectar uma doença grave).

---

**21.** O **F1-score** é definido como:

a) A soma simples entre precisão e recall<br>
b) A média harmônica entre precisão e recall, que busca equilibrar as duas métricas em um único valor, sendo especialmente útil quando se deseja um balanço entre ambas, penalizando fortemente casos em que uma das duas é muito baixa<br>
c) A média aritmética simples entre acurácia e especificidade<br>
d) Um sinônimo exato de acurácia

> **Gabarito: b.** O F1-score usa média harmônica (não aritmética simples) justamente porque essa forma de média penaliza mais fortemente desequilíbrios grandes entre precisão e recall — um modelo só terá F1 alto se ambas as métricas forem razoavelmente boas simultaneamente.

---

**22.** **(Pegadinha)** Para problemas de **regressão** (não de classificação), métricas comumente utilizadas incluem MAE (Erro Absoluto Médio), MSE (Erro Quadrático Médio) e RMSE (Raiz do Erro Quadrático Médio). Sobre a diferença entre MAE e MSE/RMSE, é correto afirmar que:

a) MAE e MSE são exatamente equivalentes em qualquer conjunto de dados, sem qualquer diferença de comportamento<br>
b) O MSE (e, por extensão, o RMSE) eleva os erros ao quadrado antes de calcular a média, o que faz com que erros grandes (outliers de previsão) sejam penalizados de forma desproporcionalmente maior do que no MAE, que trata todos os erros de forma linear (proporcional à sua magnitude absoluta)<br>
c) O MAE é sempre numericamente maior que o MSE, para qualquer conjunto de previsões<br>
d) Essas métricas só podem ser aplicadas a problemas de classificação, nunca de regressão

> **Gabarito: b.** Pegadinha: a diferença essencial entre essas métricas está na sensibilidade a erros grandes — como o MSE eleva os erros ao quadrado, valores de erro muito grandes (previsões muito distantes do real) têm impacto desproporcionalmente maior na métrica final, comparado ao MAE, que trata os erros de forma linear.

---

**23.** O coeficiente de determinação **R²** (R-quadrado), em um modelo de regressão, indica, de forma geral:

a) O erro médio absoluto das previsões, em unidades da variável original<br>
b) A proporção da variância da variável dependente (resposta) que é explicada pelas variáveis independentes (preditoras) incluídas no modelo, geralmente variando entre 0 e 1 (podendo ser negativo em modelos muito ruins)<br>
c) O número total de variáveis utilizadas no modelo<br>
d) Um sinônimo exato de acurácia, usado apenas em problemas de regressão

> **Gabarito: b.** O R² mede, intuitivamente, "quanto da variação nos dados observados o modelo consegue explicar" — um R² próximo de 1 indica que o modelo explica bem a variabilidade da variável resposta, enquanto valores próximos de zero (ou negativos, em casos extremos) indicam baixo poder explicativo.

---

**24.** **(Pegadinha)** Um cientista de dados afirma: "Um R² muito alto (próximo de 1) garante, por si só, que o modelo é excelente e adequado para uso em produção, sem necessidade de qualquer outra análise." Essa afirmação está:

a) Correta, pois R² alto é suficiente para garantir qualidade em qualquer cenário<br>
b) Incorreta — um R² muito alto pode, inclusive, ser um sinal de overfitting (especialmente se calculado apenas no conjunto de treino) ou de outros problemas metodológicos (como data leakage); é necessário avaliar o modelo também em dados de teste/validação e considerar outros aspectos, como a interpretabilidade, a robustez e a adequação ao problema de negócio<br>
c) Correta, desde que o modelo seja uma regressão linear simples<br>
d) Incorreta, mas apenas porque R² nunca deve ser usado como métrica de avaliação

> **Gabarito: b.** Pegadinha: um R² excessivamente alto, especialmente medido apenas no conjunto de treino, pode ser um sinal de alerta (overfitting ou vazamento de dados) em vez de garantia de qualidade — avaliação robusta exige mais do que uma única métrica isolada.

---

**25.** Na etapa de **implantação (deployment)** de um modelo de Ciência de Dados, um dos principais objetivos é:

a) Encerrar completamente qualquer envolvimento da equipe de dados com o modelo, uma vez que ele está em produção<br>
b) Tornar o modelo acessível e integrado a sistemas reais (aplicações, APIs, pipelines de decisão), de forma que suas previsões possam efetivamente ser utilizadas para apoiar decisões ou automatizar processos no contexto de negócio real<br>
c) Retreinar o modelo do zero a cada nova previsão individual solicitada<br>
d) Eliminar toda a documentação técnica produzida durante o desenvolvimento do modelo

> **Gabarito: b.** A implantação é a etapa em que o modelo deixa de ser um experimento isolado e passa a gerar valor real, sendo integrado a sistemas e processos de negócio de forma que suas previsões sejam efetivamente utilizadas.

---

**26.** **(Pegadinha)** O fenômeno de **drift de dados** (data drift) ou **drift de conceito** (concept drift), relevante após a implantação de um modelo em produção, refere-se a:

a) Um erro de programação no código do modelo, sem relação com os dados<br>
b) A mudança, ao longo do tempo, na distribuição estatística dos dados de entrada (data drift) ou na própria relação entre as variáveis de entrada e a variável alvo (concept drift), fazendo com que o desempenho de um modelo antes eficaz se degrade gradualmente, já que ele foi treinado sobre padrões que podem não refletir mais a realidade atual<br>
c) Um fenômeno que ocorre exclusivamente durante o treinamento do modelo, nunca após a implantação<br>
d) Um sinônimo técnico de overfitting

> **Gabarito: b.** Pegadinha: é essencial entender que um modelo, mesmo bem avaliado no momento da implantação, pode se degradar ao longo do tempo à medida que o mundo real muda (novos comportamentos, sazonalidade, mudanças de mercado etc.) — por isso, monitoramento contínuo em produção é uma prática essencial, não opcional.

---

**27.** **(Pegadinha)** Um gestor afirma: "Uma vez que o modelo foi validado com boas métricas e implantado em produção, não há necessidade de qualquer monitoramento contínuo, pois seu desempenho permanecerá constante indefinidamente." Essa afirmação está:

a) Correta, pois um modelo bem validado nunca se degrada ao longo do tempo<br>
b) Incorreta — devido a fenômenos como data drift e concept drift, o desempenho de um modelo em produção pode se degradar ao longo do tempo, mesmo que tenha sido bem avaliado inicialmente; por isso, o monitoramento contínuo do desempenho (e, eventualmente, o retreinamento periódico) é uma prática recomendada e frequentemente essencial em projetos reais<br>
c) Correta, desde que o modelo tenha sido treinado com uma grande quantidade de dados<br>
d) Incorreta, mas apenas porque modelos em produção nunca funcionam corretamente desde o início

> **Gabarito: b.** Pegadinha ligada diretamente à questão anterior: a validação inicial não é uma garantia permanente — práticas de MLOps recomendam monitoramento contínuo de métricas de desempenho e de possíveis sinais de drift, com planos de retreinamento ou atualização do modelo quando necessário.

---

**28.** O termo **MLOps** (Machine Learning Operations) refere-se a:

a) Um algoritmo específico de aprendizado de máquina<br>
b) Um conjunto de práticas, ferramentas e processos que buscam unir o desenvolvimento de modelos de aprendizado de máquina (ML) com sua operação confiável em produção, incluindo versionamento de dados/modelos, automação de pipelines, monitoramento e retreinamento<br>
c) Um sinônimo exato de "análise exploratória de dados"<br>
d) Uma métrica de avaliação de modelos de classificação

> **Gabarito: b.** MLOps estende práticas de DevOps para o contexto de Machine Learning, abordando desafios específicos como versionamento de dados e modelos, automação de pipelines de treinamento/implantação, monitoramento de desempenho e drift, e reprodutibilidade — indo além da construção do modelo em si.

---

**29.** **(Pegadinha)** Um cientista de dados relata: "Meu modelo atingiu 98% de acurácia no conjunto de treino." Isoladamente, essa informação:

a) É suficiente para concluir, com segurança, que o modelo terá ótimo desempenho em produção<br>
b) É insuficiente para avaliar a real qualidade do modelo, pois alto desempenho **apenas no conjunto de treino** pode simplesmente refletir overfitting; é necessário conhecer também o desempenho em um conjunto de teste (ou validação) independente para avaliar a real capacidade de generalização do modelo<br>
c) Garante automaticamente que o modelo não sofre de nenhum tipo de viés<br>
d) É irrelevante para qualquer análise, devendo ser descartada

> **Gabarito: b.** Pegadinha final que reforça um tema central da prova: métricas calculadas exclusivamente no conjunto de treino, isoladas de qualquer avaliação em dados não vistos, não permitem concluir nada sobre a real capacidade de generalização do modelo — um ponto de atenção recorrente em avaliação de modelos.

---

**30.** **(Pegadinha)** Um gestor de projeto afirma: "Ciência de Dados é, essencialmente, um processo linear: primeiro coletamos todos os dados necessários, depois preparamos tudo de uma vez, depois modelamos, depois avaliamos e, por fim, implantamos — sem qualquer necessidade de revisitar etapas anteriores." Do ponto de vista da prática real de projetos de dados, essa afirmação está:

a) Correta, pois todo projeto de Ciência de Dados segue rigorosamente essa ordem fixa, sem exceções<br>
b) Incorreta — na prática, projetos de Ciência de Dados costumam ser altamente **iterativos**: problemas identificados durante a modelagem ou avaliação frequentemente levam a revisitar a preparação de dados (ou até a compreensão do problema de negócio), e mesmo após a implantação, o monitoramento pode revelar a necessidade de coletar mais dados, ajustar features ou retreinar o modelo — refletindo o espírito cíclico de frameworks como o CRISP-DM (ver questão 1)<br>
c) Correta, mas apenas em projetos de aprendizado supervisionado<br>
d) Incorreta, mas apenas porque a etapa de implantação nunca é, de fato, necessária

> **Gabarito: b.** Pegadinha conceitual final, que conecta com a primeira questão da prova: a visão de um pipeline estritamente linear e "de mão única" contraria a prática real e a própria filosofia de frameworks de referência como o CRISP-DM, que reconhecem explicitamente a natureza iterativa e cíclica de projetos de dados bem-sucedidos.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Os pontos mais recorrentes de pegadinha nesta prova foram: **data leakage e suas formas sutis** (questões 9 e 10), a **distinção entre overfitting e underfitting** (questões 12 e 13), a **armadilha da acurácia em classes desbalanceadas** (questão 18), a **confusão entre precisão e recall** (questões 19 e 20), a **diferença de sensibilidade a outliers entre MAE e MSE/RMSE** (questão 22), e o **caráter iterativo (não linear) do ciclo de vida de projetos de dados**, incluindo a necessidade de monitoramento contínuo após a implantação (questões 1, 26, 27 e 30) — vale reforçar esses pontos na correção em sala.
