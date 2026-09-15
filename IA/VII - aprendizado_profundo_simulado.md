# 30 Questões de Múltipla Escolha
## Aprendizado Profundo (Deep Learning): Modelos e Métricas de Avaliação

---

### 1. O que caracteriza o Aprendizado Profundo (Deep Learning) em relação ao Aprendizado de Máquina tradicional?
a) O uso exclusivo de dados não-rotulados<br>
b) O uso de redes neurais artificiais com múltiplas camadas, capazes de aprender representações hierárquicas dos dados<br>
c) A ausência de qualquer processo de otimização<br>
d) A impossibilidade de uso em problemas de classificação

**Gabarito: b)** O Deep Learning é um subcampo do aprendizado de máquina baseado em redes neurais com várias camadas (profundas), que aprendem automaticamente representações cada vez mais abstratas dos dados, reduzindo a necessidade de engenharia manual de atributos (feature engineering).

---

### 2. O "neurônio artificial" em uma rede neural realiza, basicamente:
a) Uma soma ponderada das entradas seguida da aplicação de uma função de ativação<br>
b) Apenas uma comparação de igualdade entre valores<br>
c) Um agrupamento de dados por densidade<br>
d) Uma divisão recursiva do espaço de atributos

**Gabarito: a)** Cada neurônio calcula z = Σ(w_i · x_i) + b (soma ponderada das entradas mais um bias) e, em seguida, aplica uma função de ativação f(z), gerando a saída do neurônio.

---

### 3. As funções de ativação são importantes nas redes neurais porque:
a) Eliminam a necessidade de treinamento<br>
b) Introduzem não-linearidade, permitindo que a rede aprenda relações complexas entre entradas e saídas<br>
c) Servem apenas para normalizar os dados de entrada<br>
d) Substituem completamente a função de perda

**Gabarito: b)** Sem funções de ativação não-lineares, uma rede neural (independentemente do número de camadas) se comportaria como uma simples transformação linear. Funções como ReLU, sigmoide e tanh permitem à rede aprender padrões não-lineares complexos.

---

### 4. A função de ativação ReLU (Rectified Linear Unit) é definida como:
a) f(x) = 1 / (1 + e^(-x))<br>
b) f(x) = max(0, x)<br>
c) f(x) = tanh(x)<br>
d) f(x) = x²

**Gabarito: b)** A ReLU retorna 0 para entradas negativas e a própria entrada para valores positivos (f(x) = max(0, x)), sendo computacionalmente simples e eficaz para mitigar o problema do gradiente que desaparece (vanishing gradient), embora possa sofrer do problema de "neurônios mortos".

---

### 5. O algoritmo de Backpropagation (retropropagação) é utilizado para:
a) Inicializar aleatoriamente os pesos da rede<br>
b) Calcular os gradientes da função de perda em relação aos pesos da rede, permitindo sua atualização via gradiente descendente<br>
c) Normalizar os dados de entrada antes do treinamento<br>
d) Definir o número de camadas da rede

**Gabarito: b)** O backpropagation aplica a regra da cadeia para propagar o erro (calculado na saída) de volta pelas camadas da rede, calculando o gradiente da função de perda em relação a cada peso, o que possibilita a atualização via algoritmos como o gradiente descendente (ou variantes como Adam).

---

### 6. O problema do "gradiente que desaparece" (vanishing gradient) ocorre principalmente:
a) Em redes muito profundas, quando os gradientes se tornam extremamente pequenos ao serem propagados pelas camadas iniciais, dificultando o aprendizado<br>
b) Apenas em modelos de regressão linear<br>
c) Quando a taxa de aprendizado é igual a zero<br>
d) Exclusivamente em algoritmos de clustering

**Gabarito: a)** Em redes profundas com funções de ativação saturantes (como sigmoide/tanh), os gradientes podem diminuir exponencialmente ao serem propagados para trás através de muitas camadas, praticamente impedindo a atualização eficaz dos pesos nas camadas iniciais.

---

### 7. Uma solução comum para mitigar o problema do gradiente que desaparece é:
a) Usar apenas a função de ativação sigmoide em todas as camadas<br>
b) Utilizar funções de ativação como ReLU e técnicas como normalização em lote (Batch Normalization) e conexões residuais<br>
c) Reduzir a rede para apenas uma camada<br>
d) Remover completamente a função de perda

**Gabarito: b)** ReLU (e variantes como Leaky ReLU), Batch Normalization e arquiteturas com conexões residuais (skip connections, como nas ResNets) ajudam a manter gradientes mais estáveis, permitindo o treinamento eficaz de redes muito profundas.

---

### 8. As Redes Neurais Convolucionais (CNNs) são especialmente eficazes para:
a) Dados sequenciais e temporais, como texto e séries temporais<br>
b) Dados com estrutura espacial, como imagens, aproveitando padrões locais por meio de filtros convolucionais<br>
c) Problemas de clustering hierárquico<br>
d) Redução de dimensionalidade não-linear exclusivamente

**Gabarito: b)** CNNs utilizam filtros (kernels) convolucionais que se movem sobre a imagem, capturando padrões espaciais locais (bordas, texturas, formas) e compartilhando parâmetros, o que reduz drasticamente o número de parâmetros comparado a uma rede totalmente conectada.

---

### 9. As camadas de Pooling (ex.: Max Pooling), comuns em CNNs, têm como função:
a) Aumentar a resolução espacial da imagem<br>
b) Reduzir a dimensionalidade espacial dos mapas de características, resumindo informações e tornando a rede mais robusta a pequenas translações<br>
c) Substituir completamente as camadas convolucionais<br>
d) Normalizar os pesos da rede

**Gabarito: b)** O pooling (por exemplo, Max Pooling) reduz a dimensão espacial (largura/altura) dos mapas de características, diminuindo o custo computacional e tornando a representação aprendida mais robusta a pequenas variações de posição dos padrões na imagem.

---

### 10. As Redes Neurais Recorrentes (RNNs) foram projetadas para lidar com:
a) Apenas dados tabulares estáticos<br>
b) Dados sequenciais, mantendo um "estado oculto" que carrega informação ao longo dos passos de tempo<br>
c) Exclusivamente imagens<br>
d) Problemas de agrupamento sem rótulos

**Gabarito: b)** RNNs processam sequências (texto, séries temporais, áudio) mantendo um estado oculto (hidden state) que é atualizado a cada passo de tempo, permitindo, em teoria, capturar dependências temporais entre os elementos da sequência.

---

### 11. Uma limitação clássica das RNNs simples é:
a) Não conseguirem processar nenhum tipo de sequência<br>
b) Dificuldade em capturar dependências de longo prazo, devido ao problema do gradiente que desaparece/explode ao longo de muitos passos de tempo<br>
c) Serem aplicáveis apenas a imagens<br>
d) Não possuírem pesos treináveis

**Gabarito: b)** Ao propagar o erro por muitos passos de tempo, RNNs simples sofrem fortemente do problema de gradientes que desaparecem (ou explodem), dificultando o aprendizado de dependências entre elementos distantes na sequência.

---

### 12. As redes LSTM (Long Short-Term Memory) foram criadas para:
a) Substituir completamente as CNNs em qualquer tarefa<br>
b) Mitigar o problema de dependências de longo prazo das RNNs simples, por meio de mecanismos de "portas" (gates) que controlam o fluxo de informação<br>
c) Eliminar a necessidade de função de perda<br>
d) Funcionar exclusivamente com dados tabulares

**Gabarito: b)** As LSTMs introduzem uma célula de memória e portas (de entrada, esquecimento e saída) que regulam quais informações são mantidas, atualizadas ou descartadas ao longo do tempo, permitindo capturar dependências de prazo mais longo do que RNNs tradicionais.

---

### 13. A arquitetura Transformer, base de modelos como BERT e GPT, se diferencia das RNNs principalmente por:
a) Processar a sequência de forma estritamente sequencial, um elemento por vez<br>
b) Utilizar o mecanismo de atenção (self-attention) para relacionar diretamente todos os elementos de uma sequência entre si, permitindo paralelização<br>
c) Não poder ser usada para processamento de linguagem natural<br>
d) Ser exclusivamente aplicada a imagens

**Gabarito: b)** O Transformer substitui a recorrência pelo mecanismo de self-attention, que calcula relações entre todos os pares de posições da sequência simultaneamente, permitindo maior paralelização no treinamento e capturando dependências de longo alcance mais eficientemente que RNNs.

---

### 14. O mecanismo de "atenção" (attention), em termos gerais, permite que o modelo:
a) Ignore completamente partes da entrada<br>
b) Atribua pesos diferentes (de importância) a diferentes partes da entrada, ao gerar uma representação ou saída<br>
c) Substitua a função de perda por uma métrica de clustering<br>
d) Elimine a necessidade de qualquer treinamento supervisionado

**Gabarito: b)** A atenção calcula, para cada elemento de saída, um conjunto de pesos que indicam a relevância de cada parte da entrada, permitindo que o modelo "foque" dinamicamente nas partes mais relevantes para a tarefa em questão.

---

### 15. As Redes Generativas Adversariais (GANs) são compostas por:
a) Apenas uma rede neural convolucional<br>
b) Um Gerador, que tenta criar dados sintéticos realistas, e um Discriminador, que tenta distinguir dados reais de sintéticos, treinados de forma adversarial<br>
c) Duas árvores de decisão competindo entre si<br>
d) Um único autoencoder

**Gabarito: b)** Em uma GAN, o Gerador aprende a produzir amostras que se pareçam com os dados reais, enquanto o Discriminador aprende a distinguir amostras reais de geradas; ambos são treinados simultaneamente em um jogo adversarial, idealmente convergindo para um Gerador capaz de criar dados muito realistas.

---

### 16. Os Autoencoders são redes neurais utilizadas principalmente para:
a) Classificação supervisionada com rótulos balanceados<br>
b) Aprender uma representação comprimida (codificação) dos dados de entrada, reconstruindo-os na saída, sendo úteis para redução de dimensionalidade e detecção de anomalias<br>
c) Gerar sequências de texto de forma autoregressiva exclusivamente<br>
d) Substituir totalmente redes convolucionais em tarefas de visão

**Gabarito: b)** Um autoencoder é composto por um encoder (que comprime a entrada em uma representação latente de menor dimensão) e um decoder (que tenta reconstruir a entrada original a partir dessa representação), sendo aplicado em redução de dimensionalidade, remoção de ruído e detecção de anomalias (quando o erro de reconstrução é alto).

---

### 17. A função de perda Entropia Cruzada (Cross-Entropy Loss) é comumente utilizada em:
a) Problemas de regressão com saída contínua ilimitada<br>
b) Problemas de classificação, medindo a diferença entre a distribuição de probabilidade prevista e a distribuição real (rótulos)<br>
c) Redução de dimensionalidade não-supervisionada<br>
d) Clustering baseado em densidade

**Gabarito: b)** A entropia cruzada penaliza mais fortemente previsões de probabilidade muito distantes da classe verdadeira, sendo a função de perda padrão para problemas de classificação (binária ou multiclasse) treinados com uma camada de saída softmax ou sigmoide.

---

### 18. O algoritmo Adam (Adaptive Moment Estimation), muito usado no treinamento de redes profundas, é caracterizado por:
a) Utilizar uma taxa de aprendizado fixa e idêntica para todos os parâmetros, sem qualquer adaptação<br>
b) Adaptar a taxa de aprendizado de cada parâmetro com base em estimativas do primeiro e segundo momentos dos gradientes (médias móveis)<br>
c) Não usar gradientes de forma alguma<br>
d) Ser exclusivo para problemas de clustering

**Gabarito: b)** O Adam combina ideias do Momentum (média móvel dos gradientes) e do RMSProp (média móvel dos gradientes ao quadrado), adaptando a taxa de aprendizado de cada parâmetro individualmente, o que geralmente acelera e estabiliza a convergência em comparação ao SGD simples.

---

### 19. A técnica de Dropout, usada como regularização em redes neurais, consiste em:
a) Remover permanentemente neurônios da arquitetura da rede<br>
b) Desativar aleatoriamente uma fração dos neurônios durante cada passo de treinamento, reduzindo o overfitting e evitando dependência excessiva de neurônios específicos<br>
c) Aumentar artificialmente o número de camadas da rede<br>
d) Normalizar as entradas da rede

**Gabarito: b)** Durante o treinamento, o Dropout "desliga" aleatoriamente (com uma certa probabilidade) alguns neurônios em cada iteração, forçando a rede a não depender excessivamente de neurônios específicos, o que atua como uma forma de regularização e reduz o overfitting.

---

### 20. A Normalização em Lote (Batch Normalization) tem como principal benefício:
a) Aumentar artificialmente o tamanho do conjunto de dados<br>
b) Normalizar as ativações de uma camada dentro de cada mini-lote, estabilizando e acelerando o treinamento, além de atuar como regularizador leve<br>
c) Eliminar completamente a necessidade de funções de ativação<br>
d) Substituir a função de perda por uma métrica de clustering

**Gabarito: b)** O Batch Normalization normaliza (média zero, variância unitária) as ativações de uma camada considerando o mini-lote atual, o que reduz problemas como a "mudança de distribuição interna" (internal covariate shift), permitindo taxas de aprendizado mais altas e acelerando a convergência.

---

### 21. O "Early Stopping" (parada antecipada) é uma técnica de regularização que consiste em:
a) Aumentar indefinidamente o número de épocas de treinamento<br>
b) Interromper o treinamento quando o desempenho no conjunto de validação para de melhorar (ou começa a piorar), evitando overfitting<br>
c) Remover camadas da rede durante o treinamento<br>
d) Ignorar completamente o conjunto de validação

**Gabarito: b)** Monitorando uma métrica no conjunto de validação (ex.: perda de validação), o treinamento é interrompido quando essa métrica deixa de melhorar por um determinado número de épocas (patience), evitando que o modelo continue treinando até memorizar ruído do conjunto de treino.

---

### 22. Para avaliar um modelo de classificação de imagens com deep learning, quais métricas são comumente utilizadas, além da acurácia?
a) MSE e RMSE exclusivamente<br>
b) Precisão, Recall, F1-Score e a Matriz de Confusão, especialmente quando há desbalanceamento entre classes<br>
c) Coeficiente de silhueta e Davies-Bouldin<br>
d) Retorno acumulado por episódio

**Gabarito: b)** Assim como em outros problemas de classificação supervisionada, métricas como Precisão, Recall, F1-Score e a Matriz de Confusão são fundamentais, principalmente em datasets desbalanceados, onde a acurácia isolada pode ser enganosa.

---

### 23. Na avaliação de modelos de detecção de objetos (object detection), a métrica mAP (mean Average Precision) mede:
a) A acurácia média de um classificador binário simples<br>
b) A precisão média (considerando diferentes limiares de confiança e sobreposição de caixas delimitadoras - IoU) agregada entre as classes do problema<br>
c) O erro quadrático médio das previsões<br>
d) A recompensa média acumulada de um agente

**Gabarito: b)** O mAP calcula, para cada classe, a área sob a curva Precisão-Recall (Average Precision), considerando diferentes limiares de sobreposição entre as caixas previstas e as reais (IoU - Intersection over Union), e depois calcula a média entre as classes — sendo o padrão em benchmarks de detecção de objetos.

---

### 24. A métrica IoU (Intersection over Union), usada em segmentação e detecção de objetos, é calculada como:
a) A soma entre a área prevista e a área real<br>
b) A área de interseção entre a região prevista e a região real, dividida pela área de união entre elas<br>
c) A diferença absoluta entre os pixels previstos e reais<br>
d) O número total de pixels classificados corretamente

**Gabarito: b)** IoU = Área de Interseção / Área de União entre a região (caixa ou máscara) prevista pelo modelo e a região real (ground truth); quanto mais próximo de 1, melhor a sobreposição entre previsão e realidade.

---

### 25. Para avaliar modelos de linguagem geradores de texto, a métrica de Perplexidade (Perplexity) indica:
a) O número de parâmetros do modelo<br>
b) O quão "surpreso" o modelo fica, em média, ao prever a próxima palavra/token de um texto; valores mais baixos indicam melhor capacidade de previsão<br>
c) A acurácia de classificação binária<br>
d) A quantidade de camadas ocultas da rede

**Gabarito: b)** A perplexidade está relacionada à entropia cruzada exponenciada; um valor baixo de perplexidade indica que o modelo atribui alta probabilidade às sequências observadas (bom ajuste ao padrão da linguagem), enquanto valores altos indicam maior incerteza/surpresa nas previsões.

---

### 26. Métricas como BLEU e ROUGE são amplamente utilizadas para avaliar:
a) Modelos de detecção de objetos em imagens<br>
b) Tarefas de geração de texto, como tradução automática (BLEU) e sumarização automática (ROUGE), comparando a saída do modelo com referências humanas<br>
c) Modelos de clustering não-supervisionado<br>
d) Agentes de aprendizado por reforço

**Gabarito: b)** BLEU (comum em tradução automática) e ROUGE (comum em sumarização) medem a sobreposição de n-gramas entre o texto gerado pelo modelo e uma ou mais referências de qualidade (geralmente escritas por humanos), fornecendo uma aproximação automática da qualidade da geração.

---

### 27. O "Transfer Learning" (aprendizado por transferência), muito usado em deep learning, consiste em:
a) Treinar um modelo do zero para cada nova tarefa, sem reaproveitar nenhum conhecimento prévio<br>
b) Reutilizar um modelo pré-treinado em uma tarefa/dataset (geralmente grande), ajustando-o (fine-tuning) para uma nova tarefa relacionada, geralmente com menos dados<br>
c) Transferir apenas os hiperparâmetros de um modelo para outro, sem reutilizar pesos<br>
d) Ser aplicável exclusivamente a problemas de regressão linear

**Gabarito: b)** No transfer learning, aproveita-se o conhecimento (pesos) aprendido por um modelo em uma tarefa de origem (geralmente com grandes volumes de dados, como ImageNet ou grandes corpora de texto) e o adapta, via fine-tuning, para uma nova tarefa, frequentemente com menos dados disponíveis, economizando tempo e recursos computacionais.

---

### 28. Ao avaliar um modelo de deep learning, comparar as curvas de perda (loss) de treino e de validação ao longo das épocas é útil para:
a) Substituir completamente qualquer outra métrica de avaliação<br>
b) Diagnosticar overfitting (perda de treino caindo enquanto a de validação sobe ou estagna) ou underfitting (ambas as perdas permanecem altas)<br>
c) Calcular diretamente a acurácia final do modelo<br>
d) Definir o número de camadas ideais sem qualquer outro teste

**Gabarito: b)** Se a perda de treino continua caindo enquanto a de validação para de melhorar (ou aumenta), é um sinal claro de overfitting; se ambas permanecem altas e não melhoram, pode indicar underfitting ou problemas na arquitetura/treinamento — por isso, essas curvas são ferramentas de diagnóstico essenciais.

---

### 29. Aumentar o tamanho de um modelo de deep learning (mais camadas/parâmetros) e o volume de dados de treinamento geralmente:
a) Sempre garante melhor desempenho, sem qualquer custo ou risco associado<br>
b) Pode melhorar o desempenho, mas aumenta o custo computacional e o risco de overfitting se não houver dados/regularização suficientes, exigindo validação cuidadosa<br>
c) Elimina completamente a necessidade de ajuste de hiperparâmetros<br>
d) Não afeta o tempo de treinamento do modelo

**Gabarito: b)** Modelos maiores têm maior capacidade de representação, podendo melhorar o desempenho quando há dados e regularização adequados, mas também aumentam o custo computacional/energético e o risco de overfitting caso o volume e a qualidade dos dados não acompanhem esse crescimento — daí a importância de validação cuidadosa (curvas de aprendizado, validação cruzada, etc.).

---

### 30. Boas práticas na avaliação de modelos de deep learning incluem:
a) Avaliar o modelo apenas no conjunto de treinamento, sem qualquer conjunto de validação/teste separado<br>
b) Utilizar conjuntos de validação/teste independentes do treino, métricas adequadas à tarefa (classificação, regressão, geração, detecção, etc.) e considerar também custo computacional e robustez do modelo<br>
c) Escolher sempre o modelo com maior número de parâmetros, independentemente do desempenho observado<br>
d) Ignorar qualquer análise de overfitting/underfitting

**Gabarito: b)** Uma avaliação robusta de modelos de deep learning combina: (i) conjuntos de dados de validação e teste independentes do treino, (ii) métricas apropriadas à natureza da tarefa (ex.: F1/AUC para classificação, RMSE para regressão, mAP para detecção, BLEU/ROUGE para geração de texto, perplexidade para modelos de linguagem), e (iii) considerações práticas como custo computacional, tempo de inferência e robustez a dados fora da distribuição de treinamento.

---

*Documento gerado para fins educacionais sobre Aprendizado Profundo (Deep Learning).*
