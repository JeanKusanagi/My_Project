# Árvores de Decisão e Modelos Supervisionados: O Guia Completo

Este documento reúne uma visão teórica, matemática e prática sobre o funcionamento de **Árvores de Decisão**, métricas de impureza, técnicas de poda e algoritmos avançados de **Ensemble** baseados em árvores (*Random Forest*, *XGBoost*, *LightGBM* e *CatBoost*).

---

## 1. Visão Geral das Árvores de Decisão

As **Árvores de Decisão** são algoritmos de aprendizado supervisionado não paramétricos usados para tarefas de **classificação** (previsão de categorias) e **regressão** (previsão de valores numéricos). Elas funcionam como um fluxograma lógico, dividindo os dados em subconjuntos cada vez menores até chegar a uma resposta final.

### Estrutura Básica
* **Nó Raiz (Root Node):** O ponto de partida no topo da árvore, que representa a divisão inicial mais importante do conjunto de dados.
* **Nós Internos (Decision Nodes):** Pontos intermediários que fazem perguntas baseadas em características (*features*) específicas dos dados.
* **Ramos (Branches):** As conexões que representam o resultado de cada pergunta (ex: "Sim" ou "Não").
* **Nós Folha (Leaf Nodes):** Os terminais da árvore que contêm a **previsão final** (a classe ou o valor numérico estimado).

### Vantagens e Desvantagens
* **Vantagens:** Alta interpretabilidade, pouca necessidade de preparação de dados (não exige normalização) e capacidade de lidar com dados numéricos e categóricos.
* **Desvantagens:** Alta propensão ao **Overfitting** (sobreajuste) e alta variância (pequenas mudanças nos dados geram árvores totalmente diferentes).

---

## 2. Diferença Matemática: Gini vs. Entropia

O **Índice de Gini** e a **Entropia** medem o grau de impureza ou desordem de um nó em tarefas de classificação. Ambos variam de $0$ (pureza máxima) até um valor máximo que representa a incerteza total.

Considere um nó com $C$ classes, onde $p_i$ é a proporção de amostras pertencentes à classe $i$.

### Índice de Gini
Mede a probabilidade de um elemento escolhido aleatoriamente ser rotulado incorretamente se fosse classificado de acordo com a distribuição das classes no nó:
$$Gini = 1 - \sum_{i=1}^{C} (p_i)^2$$
* **Valor Máximo (2 classes):** $0.5$ (Incerteza máxima, $50\%$ de chance para cada).

### Entropia
Vinda da Teoria da Informação de Shannon, mede a quantidade de desordem ou surpresa no nó utilizando o logaritmo na base 2:
$$Entropia = - \sum_{i=1}^{C} p_i \log_2(p_i)$$
* **Valor Máximo (2 classes):** $1.0$ (Incerteza máxima, $50\%$ de chance para cada).

### Resumo Comparativo (2 Classes)

| Distribuição de Classes | Cenário | Índice de Gini | Entropia |
| :--- | :--- | :--- | :--- |
| **100% Classe A / 0% Classe B** | Puro | **0.0** | **0.0** |
| **80% Classe A / 20% Classe B** | Majoritário | **0.32** | **0.72** |
| **50% Classe A / 50% Classe B** | Impuro (Máximo) | **0.50** | **1.0** |

* **Custo Computacional:** O Índice de Gini é computacionalmente mais rápido por envolver apenas multiplicações e subtrações simples, enquanto a Entropia requer o cálculo de logaritmos.

---

## 3. Ganho de Informação e Decisão de Corte

O **Ganho de Informação** usa a Entropia para calcular a redução da desordem nos dados após uma divisão, escolhendo o corte que gera os subconjuntos mais puros possíveis.

$$	ext{Ganho}(T, 	ext{corte}) = 	ext{Entropia}(T) - \sum_{v \in 	ext{filhos}} rac{|T_v|}{|T|} 	imes 	ext{Entropia}(T_v)$$

### Exemplo Prático
Num nó pai com **10 clientes** (6 Compraram / 4 Não Compraram):
* **Entropia Inicial:** $- (0.6 \cdot \log_2(0.6) + 0.4 \cdot \log_2(0.4)) pprox 0.971$

Se testarmos o corte **"Idade $\le$ 30 anos"** e ele dividir os dados em:
1. **Filho Esquerdo ($\le 30$):** 4 pessoas (3 Sim / 1 Não) $ightarrow 	ext{Entropia} = 0.811$
2. **Filho Direito ($> 30$):** 6 pessoas (3 Sim / 3 Não) $ightarrow 	ext{Entropia} = 1.000$

**Cálculo do Ganho:**
$$	ext{Ganho} = 0.971 - \left[ \left(rac{4}{10} \cdot 0.811ight) + \left(rac{6}{10} \cdot 1.000ight) ight] = 0.971 - 0.924 = \mathbf{0.047}$$

O algoritmo testa recursivamente todos os pontos de corte e escolhe a característica e o valor que entregarem o **maior Ganho de Informação**.

---

## 4. Técnicas de Poda (Pruning) contra Overfitting

A poda remove seções da árvore que trazem pouco ganho preditivo para evitar que o modelo decore o ruído dos dados de treino.

* **Pré-poda (Pre-pruning / Early Stopping):** Interrompe o crescimento da árvore durante o treino baseando-se em travas como profundidade máxima (`max_depth`), número mínimo de amostras para divisão (`min_samples_split`) ou número mínimo de amostras por folha (`min_samples_leaf`).
* **Pós-poda (Post-pruning):** Permite que a árvore cresça totalmente e depois remove ramos insignificantes usando critérios matemáticos como a **Poda por Complexidade de Custo (CCP)**:
  $$R_lpha(T) = R(T) + lpha |T|$$
  Onde $lpha$ é o parâmetro de penalização pela complexidade (número de folhas $|T|$). Através de validação cruzada, encontra-se o $lpha$ ideal.

---

## 5. Conexão com Random Forest

Enquanto uma árvore de decisão única exige poda estrita para não sofrer overfitting, a **Random Forest** adota o caminho inverso: ela permite que as árvores cresçam ao máximo (**sem poda**) e resolve o overfitting de forma coletiva.

* **Bagging (Bootstrap Aggregating):** Cada árvore é treinada com uma subamostra aleatória dos dados.
* **Aleatoriedade de Recursos:** Cada nó testa apenas um subconjunto aleatório de variáveis.
* **Efeito Cancelamento:** Árvores profundas não podadas possuem baixo viés e alta variância. Ao agregar centenas delas por meio da votação da maioria ou média, os erros individuais de alta variância se cancelam, gerando um modelo extremamente robusto.

---

## 6. Modelos de Gradient Boosting

O **Gradient Boosting** constrói modelos de forma sequencial. Cada nova árvore adicionada é treinada especificamente para **corrigir os resíduos (erros) das árvores anteriores**, minimizando uma função de perda via Gradiente Descendente.

### Comparativo das Principais Implementações

| Critério | XGBoost | LightGBM | CatBoost |
| :--- | :--- | :--- | :--- |
| **Crescimento** | Por nível (*Level-wise*) | Por folha (*Leaf-wise*) | Simétrico (*Symmetric*) |
| **Variáveis Categóricas** | Requer codificação prévia | Codifica internamente | Suporte nativo avançado |
| **Velocidade** | Rápido (Histogramas) | **Extremamente Rápido** | Moderado em CPU / Rápido em GPU |
| **Memória** | Médio / Alto | **Muito Baixo** | Baixo / Médio |

* **XGBoost:** Introduz regularização L1 e L2 diretamente na função de custo. É altamente estável e o mais documentado do ecossistema.
* **LightGBM:** Desenvolvido pela Microsoft, foca em Big Data utilizando estratégias como *GOSS* e *EFB* para reduzir drasticamente o tempo de processamento e uso de memória.
* **CatBoost:** Criado pela Yandex, lida com variáveis categóricas nativamente com algoritmos avançados de Target Encoding estatístico em tempo de execução, reduzindo o risco de *target leakage*.