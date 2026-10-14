# Simulado Exame de Inteligência Artificial: Aprendizado Profundo (Deep Learning)

**Instruções do Elaborador:**

* Este simulado contém 30 questões de múltipla escolha cobrindo os fundamentos, arquiteturas, algoritmos de treinamento e técnicas avançadas de Aprendizado Profundo (*Deep Learning*).

* As alternativas corretas estão distribuídas de forma aleatória (A, B, C, D e E).

* Fique atento a pegadinhas conceituais sobre dimensões de tensores, dinâmica de gradientes, funções de ativação e regularizações.

* O gabarito comentado ao final de cada questão oferece a fundamentação teórico-matemática rigorosa.

---

### Questão 1 (Fácil)

Qual função de ativação linear por partes (piecewise linear) é amplamente utilizada nas camadas ocultas de redes neurais profundas por ser computacionalmente simples e mitigar o problema do desaparecimento do gradiente (*vanishing gradient*) para entradas positivas?

A) Sigmoide ($\sigma(x)$)

B) Tangente Hiperbólica ($\tanh(x)$)

C) Softmax

D) Unit Linear Retificada (ReLU - $\max(0, x)$)

E) Gaussian Error Linear Unit (GELU)

**Resposta Correta: D**

**Comentário:** A função ReLU ($f(x) = \max(0, x)$) possui derivada igual a $1$ para qualquer entrada $x > 0$. Isso impede que o gradiente seja atenuado exponencialmente ao ser multiplicado ao longo de várias camadas durante a retropropagação (*backpropagation*), resolvendo o problema de saturação/desaparecimento do gradiente comum em funções sigmoide e $\tanh$.

---

### Questão 2 (Médio - Pegadinha)

Considere uma camada convolucional 2D que recebe um tensor de entrada com dimensões $32 \times 32 \times 3$ (Altura $\times$ Largura $\times$ Canais de Cor). A camada aplica $16$ filtros convolucionais de tamanho $5 \times 5$, utilizando *padding* $P = 0$ e *stride* $S = 1$. Quantos **parâmetros treináveis** (pesos + biases) possui essa camada convolucional?

A) $1.216$

B) $400$

C) $1.200$

D) $2.416$

E) $16.384$

**Resposta Correta: A**

**Comentário:** *Pegadinha clássica de dimensões em CNNs!* Cada filtro convolucional deve ter a mesma profundidade que os canais do tensor de entrada (3 canais). Portanto, cada filtro $5 \times 5$ possui $5 \times 5 \times 3 = 75$ pesos, mais $1$ bias associado ao filtro, totalizando $76$ parâmetros por filtro. Como existem $16$ filtros independentes:

$$
\text{Total de Parâmetros} = 16 \times (5 \times 5 \times 3 + 1) = 16 \times 76 = 1.216
$$

Note que as dimensões espaciais de entrada ($32 \times 32$) não afetam o número de parâmetros da camada convolucional.

---

### Questão 3 (Difícil)

Durante o treinamento de uma rede neural profunda com a função de ativação Sigmoide, observa-se que as camadas mais próximas da entrada (*input layer*) atualizam seus pesos extremamente devagar ou quase congelam. Matematicamente, por que o fenômeno do **Desaparecimento do Gradiente (Vanishing Gradient)** ocorre predominantemente com a Sigmoide?

A) A derivada da função sigmoide é $\sigma'(x) = \sigma(x)(1 - \sigma(x))$, cujo valor máximo é $0,25$. A aplicação da Regra da Cadeia em $L$ camadas multiplica termos menores ou iguais a $0,25$, fazendo o gradiente tender a zero exponencialmente.

B) A função sigmoide não é diferenciável no ponto $x = 0$, criando instabilidade numérica.

C) A sigmoide causa um estouro dos pesos (*exploding weights*) devido ao seu contradomínio ser $(-\infty, +\infty)$.

D) O gradiente da sigmoide é sempre igual a 1, impossibilitando a descida do gradiente.

E) O cálculo da sigmoide introduz erros de arredondamento por ponto flutuante que zeram a perda (*loss*).

**Resposta Correta: A**

**Comentário:** A derivada da função sigmoide alcança seu pico absoluto em $x = 0$, onde $\sigma(0) = 0,5$, resultando em $\sigma'(0) = 0,5 \times (1 - 0,5) = 0,25$. Para valores distantes de zero ($|x| \gg 0$), $\sigma'(x) \to 0$. Ao retropropagar o erro por $L$ camadas, o gradiente do erro em relação aos primeiros pesos envolve o produto de $L$ derivadas de ativação: $\prod_{i=1}^L \sigma'(z_i) \le (0,25)^L$. Para $L=10$, $(0,25)^{10} \approx 9,5 \times 10^{-7}$, anulando a atualização dos pesos iniciais.

---

### Questão 4 (Médio)

Em redes neurais recorrentes clássicas (RNNs), o problema da dependência de longo alcance (*long-range dependency*) levou ao desenvolvimento da arquitetura **LSTM (Long Short-Term Memory)**. Qual componente interno da célula LSTM é especificamente responsável por **decidir quais informações do estado da célula (*cell state*) serão descartadas**?

A) Portão de Entrada (*Input Gate*)

B) Portão de Esquecimento (*Forget Gate*)

C) Portão de Saída (*Output Gate*)

D) Camada de Tangente Hiperbólica Kandinsky

E) Mecanismo de Atenção Cruzada

**Resposta Correta: B**

**Comentário:** O *Forget Gate* ($f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$) recebe a entrada atual $x_t$ e o estado oculto anterior $h_{t-1}$, emitindo um número entre $0$ e $1$ para cada elemento do estado de célula $C_{t-1}$. O valor $0$ significa "esqueça completamente esta informação", enquanto $1$ significa "mantenha totalmente esta informação".

---

### Questão 5 (Difícil - Pegadinha)

Suponha que você aplique a técnica de **Dropout** com taxa $p = 0,4$ (desativando $40\%$ dos neurônios aleatoriamente) nas camadas ocultas de uma rede neural durante o **treinamento**. No momento da **inferência/teste**, como o algoritmo deve proceder com os pesos ou saídas da camada para manter o valor esperado da ativação correto sem alterar o fluxo do código?

A) Aplicar o Dropout com taxa $p = 0,4$ normalmente durante a inferência.

B) Desativar o Dropout e multiplicar todas as saídas das ativações por $(1 - p) = 0,6$ na inferência (caso não tenha usado *Inverted Dropout*).

C) Elevar os pesos ao quadrado para compensar os neurônios desativados.

D) Multiplicar a taxa de aprendizado por $0,4$.

E) Dividir todos os pesos por zero para desativar a camada.

**Resposta Correta: B**

**Comentário:** *Pegadinha de Inverted vs. Standard Dropout!* Durante o treinamento tradicional (*Standard Dropout*), como apenas uma fração $(1-p)$ dos neurônios está ativa em cada passagem, a soma esperada das entradas da camada seguinte é menor. Na inferência, todos os neurônios estão ativos. Para compensar essa discrepância de escala no tempo de teste, deve-se escalar as ativações/pesos multiplicando por $(1 - p)$. *(Obs: No Inverted Dropout, moderno e padrão do PyTorch/TensorFlow, realiza-se a divisão por $(1-p)$ durante o treinamento, dispensando modificações na inferência).*

---

### Questão 6 (Fácil)

Qual é o papel fundamental da função de ativação **Softmax** na camada final de uma rede neural voltada para **classificação multiclasse mutuamente exclusiva**?

A) Normalizar a perda (*loss*) para ficar entre $0$ e $1$.

B) Transformar um vetor de saídas reais arbitrárias (*logits*) em uma distribuição de probabilidade válida, onde todos os valores estão entre $0$ e $1$ e a soma total é igual a $1$.

C) Binarizar todas as saídas para $0$ ou $1$.

D) Zerar os gradientes negativos para acelerar a convergência.

E) Reduzir a dimensão das imagens de entrada.

**Resposta Correta: B**

**Comentário:** A função Softmax é definida como $P(y = i | \mathbf{z}) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$. Ela exponencializa os *logits* $z_i$ (tornando-os estritamente positivos) e os divide pela soma de todas as exponencializações, convertendo as saídas não delimitadas em uma distribuição de probabilidades formal.

---

### Questão 7 (Difícil)

A arquitetura do **Transformer** (Vaswani et al., 2017) revolucionou o PNL ao abandonar a recorrência e utilizar o mecanismo de **Atenção Auto-Dirigida (*Self-Attention*) Scaled Dot-Product**. Matematicamente, a fórmula da atenção é dada por:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V
$$

Qual é o propósito matemático rigoroso de dividir o produto escalar $Q K^T$ pelo fator de escala $\sqrt{d_k}$?

A) Impedir que o número de parâmetros da matriz de atenção cresça exponencialmente.

B) Para grandes valores da dimensão $d_k$, o produto escalar $Q K^T$ tende a crescer em magnitude, empurrando a função Softmax para regiões de gradiente extremamente pequeno (saturação). O fator $\sqrt{d_k}$ mantém a variância igual a 1.

C) Garantir que a matriz de atenção seja inversível para aplicar a decomposição SVD.

D) Converter o resultado da atenção em um vetor complexo conjugado.

E) Eliminar a necessidade de embeddings posicionais (*positional encodings*).

**Resposta Correta: B**

**Comentário:** Assumindo que os componentes de $Q$ e $K$ são variáveis aleatórias independentes com média $0$ e variância $1$, o produto escalar $Q K^T = \sum_{i=1}^{d_k} q_i k_i$ terá média $0$ e variância $d_k$. Para dimensões altas (ex: $d_k = 64$ ou $512$), os valores de $QK^T$ tornam-se grandes em magnitude. Como a Softmax utiliza exponenciais $e^z$, entradas muito grandes resultam em probabilidades extremamente concentradas (uma opção perto de 1 e as outras perto de 0), gerando derivadas extremamente pequenas durante o *backpropagation*. A divisão por $\sqrt{d_k}$ re-escala a variância de volta para $1$.

---

### Questão 8 (Médio)

O algoritmo otimizador **Adam (Adaptive Moment Estimation)** combina os princípios de dois outros métodos de otimização muito populares em Deep Learning. Quais são esses dois métodos?

A) SGD puro e Nesterov Accelerated Gradient.

B) AdaGrad e RMSProp (utilizando os momentos de primeira e segunda ordem dos gradientes).

C) BFGS e L-BFGS.

D) Descida do Gradiente por Mini-lote e Algoritmos Genéticos.

E) Newton-Raphson e Regra do Trapézio.

**Resposta Correta: B**

**Comentário:** O Adam calcula estimativas adaptativas dos momentos de primeira ordem (média do gradiente, herdado do conceito de Momentum) e de segunda ordem (variância não-centralizada do gradiente, herdado do RMSProp e AdaGrad). Isso permite ajustar as taxas de aprendizado individuais de cada parâmetro dinamicamente.

---

### Questão 9 (Médio - Pegadinha)

Em uma Rede Neural Convolucional (CNN), qual é o efeito primário da operação de **Max-Pooling $2 \times 2$ com stride $2$** aplicada sobre um mapa de recursos (*feature map*)?

A) Aumentar o número de canais do tensor pelo dobro.

B) Reduzir as dimensões espaciais (largura e altura) do mapa de recursos pela metade, reduzindo a carga computacional e conferindo invariância a pequenas translações locais, sem alterar o número de canais.

C) Multiplicar todos os pesos da camada convolucional anterior por 2.

D) Introduzir novos parâmetros treináveis para regularizar a rede.

E) Inverter os valores dos pixels positivos para negativos.

**Resposta Correta: B**

**Comentário:** *Pegadinha:* O *pooling* **não possui parâmetros treináveis**! Ele atua de forma independente em cada canal do tensor de entrada. Uma janela de $2 \times 2$ com stride $2$ seleciona o valor máximo dentro de cada bloco de $4$ pixels, reduzindo a largura e a altura pela metade (ex: de $28 \times 28 \times 64$ para $14 \times 14 \times 64$), mantendo a profundidade dos canais inalterada.

---

### Questão 10 (Difícil)

A técnica de **Batch Normalization (BN)** é amplamente utilizada para estabilizar e acelerar o treinamento de redes profundas. Durante a etapa de **treinamento**, a BN normaliza as ativações de um mini-lote $B$. Contudo, o algoritmo introduz dois parâmetros aprendíveis $\gamma$ (escala) e $\beta$ (deslocamento/shift). Qual é a necessidade matemática de incluir $\gamma$ e $\beta$?

A) Permitir que a rede desfaza a normalização se necessário, recuperando a capacidade representacional original da camada caso a distribuição padronizada com média 0 e variância 1 limite a expressividade do modelo.

B) Impedir que a perda (*loss*) assuma valores complexos.

C) Garantir que a matriz de covariância das entradas seja estritamente diagonal.

D) Eliminar a necessidade de calcular a derivada no *backpropagation*.

E) Substituir a função de custo Cross-Entropy por MSE.

**Resposta Correta: A**

**Comentário:** Forçar estritamente que a saída de uma camada tenha média $0$ e variância $1$ pode limitar o poder de representação da rede neural. Por exemplo, se aplicarmos a normalização padrão antes de uma função sigmoide, a maioria dos valores cairá na região linear em torno de zero ($[-1, 1]$), perdendo a não-linearidade da rede. A introdução de $y = \gamma \hat{x} + \beta$ permite que a rede aprenda a identidade $\gamma = \sqrt{\text{Var}(x)}$ e $\beta = \text{E}[x]$ se essa for a transformação ideal para a tarefa.

---

### Questão 11 (Fácil)

Em relação às redes neurais recorrentes, qual arquitetura foi proposta para simplificar a LSTM ao fundir o estado da célula (*cell state*) e o estado oculto (*hidden state*), utilizando apenas dois portões (*gates*): **Reset Gate** e **Update Gate**?

A) ResNet-50

B) Gated Recurrent Unit (GRU)

C) Autoencoder Variacional (VAE)

D) Generative Adversarial Network (GAN)

E) Perceptron Multicamadas (MLP)

**Resposta Correta: B**

**Comentário:** A GRU (*Gated Recurrent Unit*) é uma variação popular da LSTM. Ela elimina a memória de célula separada e utiliza apenas dois portões (*Update Gate* e *Reset Gate*), tornando-a computacionalmente mais leve e com menos parâmetros do que a LSTM tradicional.

---

### Questão 12 (Difícil - Pegadinha)

Redes **ResNet (Deep Residual Networks)** introduziram as conexões de atalho (*shortcut/skip connections*) que aprendem um mapeamento residual $F(\mathbf{x}) = H(\mathbf{x}) - \mathbf{x}$, onde a saída do bloco é $H(\mathbf{x}) = F(\mathbf{x}) + \mathbf{x}$. Como essa modificação estrutural simples resolve o problema do desaparecimento do gradiente em redes com centenas de camadas (ex: ResNet-152)?

A) Ela força $F(\mathbf{x})$ a ser sempre igual a zero.

B) Durante o *backpropagation*, a derivada da adição de identidade $\frac{\partial (F(\mathbf{x}) + \mathbf{x})}{\partial \mathbf{x}} = \frac{\partial F(\mathbf{x})}{\partial \mathbf{x}} + 1$. O termo $+1$ garante que o gradiente possa fluir diretamente para as camadas anteriores sem ser atenuado por multiplicações sucessivas de pesos.

C) A conexão de atalho multiplica o gradiente pela constante de Euler $e$.

D) Ela converte todas as convoluções 2D em convoluções 1D.

E) As conexões de atalho desativam automaticamente o cálculo do erro na saída.

**Resposta Correta: B**

**Comentário:** *Pegadinha sutil:* Na regra da cadeia para derivadas de soma, a derivada de $\mathbf{x}$ em relação a $\mathbf{x}$ é a matriz identidade $I$ (ou $1$ escalar). Assim, $\frac{\partial L}{\partial \mathbf{x}} = \frac{\partial L}{\partial H} \cdot \left( \frac{\partial F}{\partial \mathbf{x}} + 1 \right) = \frac{\partial L}{\partial H} \frac{\partial F}{\partial \mathbf{x}} + \frac{\partial L}{\partial H}$. Mesmo que o gradiente $\frac{\partial F}{\partial \mathbf{x}}$ tenda a zero em camadas profundas, o termo $\frac{\partial L}{\partial H}$ passa diretamente para as camadas anteriores, permitindo treinar redes extremamente profundas.

---

### Questão 13 (Médio)

Nas redes **GANs (Generative Adversarial Networks)** propostas por Goodfellow et al. (2014), o treinamento consiste em um jogo de soma zero entre dois modelos. Quais são esses dois modelos e suas respectivas funções?

A) Encoder (comprime a imagem) e Decoder (reconstrói a imagem).

B) Gerador (cria dados sintéticos realistas a partir de um ruído aleatório) e Discriminador (tenta diferenciar entre dados reais e dados sintéticos gerados).

C) Ator (toma ações) e Crítico (avalia as recompensas em aprendizado por reforço).

D) Classificador (rotula as imagens) e Regressor (estima coordenadas).

E) Teacher (modelo grande) e Student (modelo comprimido).

**Resposta Correta: B**

**Comentário:** Uma GAN é composta pelo **Gerador ($G$)**, que tenta aprender a distribuição real dos dados para gerar amostras falsas indistinguíveis, e pelo **Discriminador ($D$)**, uma rede classificadora binária que avalia amostras para determinar se são autênticas (do conjunto real) ou forjadas por $G$.

---

### Questão 14 (Fácil)

Qual é o nome da função de perda (*loss function*) comumente utilizada para treinar redes neurais em problemas de **classificação binária**, medindo a divergência entre a probabilidade prevista $\hat{y} \in (0,1)$ e o rótulo real $y \in \{0, 1\}$?

A) Erro Quadrático Médio (MSE)

B) Entropia Cruzada Binária (Binary Cross-Entropy / Log Loss)

C) Divergência KL (Kullback-Leibler)

D) Perda de Hinge (Hinge Loss)

E) Erro Absoluto Médio (MAE)

**Resposta Correta: B**

**Comentário:** A Entropia Cruzada Binária é dada por $L(y, \hat{y}) = - [y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})]$. Ela penaliza severamente previsões confiantes porém incorretas.

---

### Questão 15 (Difícil - Pegadinha)

No contexto de modelos de linguagem e redes neurais recorrentes, o que é a técnica de **Teacher Forcing** utilizada durante a etapa de treinamento de sequências?

A) Forçar o modelo a usar uma taxa de aprendizado 10 vezes maior quando ele erra a predição.

B) Substituir a saída prevista pela rede no passo de tempo $t-1$ pelo valor real de referência (*ground truth*) como entrada para o próximo passo de tempo $t$ durante o treinamento.

C) Utilizar um modelo GPT-4 para corrigir as saídas de uma rede menor.

D) Congelar as duas primeiras camadas da rede para acelerar a época.

E) Adicionar ruído gaussiano às saídas da camada recorrente para evitar o overfitting.

**Resposta Correta: B**

**Comentário:** *Pegadinha:* Durante a inferência, uma RNN usa sua própria previsão gerada no passo $t-1$ como entrada para o passo $t$. Porém, no início do treinamento, previsões erradas no começo da sequência propagam erros catastróficos para o restante da cadeia. O *Teacher Forcing* resolve isso fornecendo o rótulo real da sequência no passo $t-1$ como entrada para $t$, estabilizando e acelerando drasticamente a convergência do treinamento.

---

### Questão 16 (Médio)

Em computação visual, qual é a principal razão teórica e prática para substituir camadas totalmente conectadas (*Fully Connected*) por **camadas convolucionais** nas primeiras etapas do processamento de imagens?

A) Convoluções utilizam compartilhamento de pesos (*weight sharing*) e conexões locais (*local receptivity*), reduzindo drasticamente o número de parâmetros e preservando a topologia espacial da imagem.

B) Convoluções são imunes ao problema de overfitting e não exigem funções de ativação.

C) Camadas totalmente conectadas só funcionam com imagens em escala de cinza.

D) A convolução transforma qualquer matriz em um escalar positivo.

E) Camadas convolucionais não realizam operações de multiplicação de matrizes na GPU.

**Resposta Correta: A**

**Comentário:** Se conectássemos uma imagem de $1000 \times 1000$ pixels a uma camada oculta com $1000$ neurônios em uma rede totalmente conectada, teríamos $10^9$ (1 bilhão) de pesos apenas no primeiro nível. A convolução aplica pequenos filtros (ex: $3 \times 3$) que deslizam pela imagem compartilhando os mesmos pesos, reduzindo drasticamente os parâmetros e capturando padrões locais independentemente de sua posição na imagem.

---

### Questão 17 (Difícil)

A **Divergência de Kullback-Leibler (KL Divergence)** desempenha um papel central no treinamento de **Autoencoders Variacionais (VAEs)**. Qual é a função da perda por Divergência KL no espaço latente de um VAE?

A) Garantir que as imagens reconstruídas tenham alta resolução espacial.

B) Forçar a distribuição do espaço latente gerada pelo Encoder $q_\phi(z|x)$ a se aproximar de uma distribuição a priori conhecida, geralmente uma Normal Padrão $\mathcal{N}(0, I)$.

C) Eliminar a necessidade de reparametrização (*reparameterization trick*).

D) Minimizar a perda de classificação das camadas convolucionais.

E) Calcular a derivada da função Softmax no decoder.

**Resposta Correta: B**

**Comentário:** A função de perda total do VAE combina o erro de reconstrução com a Divergência KL: $L_{VAE} = \text{Reconstruction Loss} + D_{KL}(q_\phi(z|x) \parallel \mathcal{P}(z))$. A Divergência KL atua como um regularizador que penaliza o Encoder se ele criar distribuições latentes distorcidas ou desconectadas, forçando a representação $z$ a se organizar segundo uma Gaussiana contínua e suave $\mathcal{N}(0, I)$, o que permite amostrar novos dados realistas diretamente a partir do espaço latente.

---

### Questão 18 (Fácil)

Qual das alternativas abaixo descreve o **Truque da Reparametrização (*Reparameterization Trick*)** essencial para viabilizar o treinamento de Autoencoders Variacionais (VAEs) via Backpropagation?

A) Substituir a amostragem estocástica $z \sim \mathcal{N}(\mu, \sigma^2)$ por $z = \mu + \sigma \odot \epsilon$, onde $\epsilon \sim \mathcal{N}(0, I)$, isolando a aleatoriedade e permitindo o cálculo dos gradientes em relação a $\mu$ e $\sigma$.

B) Reordenar a ordem das multiplicações de matrizes na GPU.

C) Converter os pesos da rede para precisão de 8 bits (Quantização).

D) Inverter a matriz de pesos utilizando a pseudoinversa de Moore-Penrose.

E) Substituir a função de ativação ReLU por uma função polinomial de terceiro grau.

**Resposta Correta: A**

**Comentário:** Não é possível propagar gradientes através de um nó de amostragem estocástica pura ($z \sim \mathcal{N}(\mu, \sigma^2)$). O *Reparameterization Trick* re-expressa a variável aleatória $z$ como uma transformação determinística: $z = \mu + \sigma \odot \epsilon$, onde $\epsilon$ é uma fonte de ruído auxiliar estocástica externa com distribuição fixa. Isso permite derivar $z$ diretamente em relação a $\mu$ e $\sigma$ pelo algoritmo de retropropagação.

---

### Questão 19 (Médio - Pegadinha)

Em otimizadores estocásticos como SGD com **Momentum**, adiciona-se um termo $v_t = \beta v_{t-1} + \alpha \nabla_{\theta} J(\theta)$ para atualizar os parâmetros $\theta_{t} = \theta_{t-1} - v_t$. Qual é o principal benefício prático do termo de Momentum?

A) Garantir que a taxa de aprendizado seja multiplicada por zero ao atingir um mínimo local.

B) Acelerar a convergência na direção de menor curvatura e amortecer oscilações ruidosas em direções de alta variação (efeito de "ravina" na superfície de erro).

C) Eliminar a necessidade de calcular a função de perda.

D) Forçar os pesos da rede a serem estritamente positivos.

E) Reduzir o número de dados do mini-lote para 1 exemplo.

**Resposta Correta: B**

**Comentário:** Ao navegar por superfícies de custo em formato de "ravina" (onde a superfície se inclina muito mais acentuadamente em uma direção do que em outra), a descida do gradiente padrão oscila transversalmente sem avançar na direção do mínimo. O Momentum acumula o histórico de gradientes anteriores: componentes que oscilam em direções opostas se anulam, enquanto componentes que apontam consistentemente na mesma direção ganham velocidade, acelerando a descida.

---

### Questão 20 (Difícil)

Deseja-se projetar uma arquitetura de visões computacionais para segmentação semântica pixel a pixel de imagens médicas. Qual das arquiteturas abaixo, caracterizada por um caminho de contração (*encoder*) e um caminho de expansão (*decoder*) simétricos interligados por **conexões de salto cruzadas (*skip connections*)**, é o padrão da indústria para essa tarefa?

A) LeNet-5

B) U-Net

C) AlexNet

D) Transformer Vanilla (Decoder-only)

E) Deep Q-Network (DQN)

**Resposta Correta: B**

**Comentário:** A **U-Net** (Ronneberger et al., 2015) foi projetada especificamente para segmentação de imagens. As *skip connections* conectam os mapas de recursos de alta resolução da fase de contração (Encoder) diretamente aos mapas da fase de expansão (Decoder). Isso permite que o Decoder recupere informações espaciais de borda e textura precisas que foram perdidas durante as operações de subamostragem (*downsampling/pooling*).

---

### Questão 21 (Fácil)

O fenómeno de **Overfitting** em redes neurais profundas manifesta-se quando:

A) A perda no conjunto de treinamento é alta e a perda no conjunto de validação é baixa.

B) O modelo memoriza os dados do conjunto de treinamento (perda de treino muito baixa), mas apresenta péssima capacidade de generalização em dados não vistos de validação/teste (perda de validação alta).

C) O tempo de treinamento atinge 0 segundos.

D) As saídas da rede neural contêm apenas números irracionais.

E) O gradiente dos pesos é exatamente igual a 1 em todas as camadas.

**Resposta Correta: B**

**Comentário:** O *overfitting* ocorre quando a capacidade do modelo (número de parâmetros) é excessiva em relação à quantidade/diversidade de dados. O modelo aprende o ruído específico do conjunto de treino em vez dos padrões subjacentes gerais, resultando em excelente desempenho no treino e falhas na validação.

---

### Questão 22 (Médio)

Qual é a diferença conceitual e funcional entre o **Mecanismo de Atenção do Encoder-Decoder (Cross-Attention)** e a **Auto-Atenção (Self-Attention)** em um modelo Transformer como o de tradução automática?

A) A Self-Attention calcula relações entre os elementos da própria sequência de entrada (ou própria sequência de saída), enquanto a Cross-Attention conecta a representação da sequência de entrada (Query do Decoder) com a saída do Encoder (Keys e Values do Encoder).

B) A Cross-Attention não utiliza multiplicações de matrizes.

C) A Self-Attention é usada apenas em imagens, enquanto a Cross-Attention é usada apenas em áudio.

D) Não há diferença; ambas são nomes alternativos para a mesma camada de convolução 1D.

E) A Cross-Attention elimina as matrizes de projeção $W_Q, W_K, W_V$.

**Resposta Correta: A**

**Comentário:** Na *Self-Attention*, as projeções de $Q$ (Query), $K$ (Key) e $V$ (Value) vêm da mesma sequência original. Na *Cross-Attention* (usada no Decoder), as *Queries* ($Q$) são geradas pelo estado atual do Decoder, enquanto as *Keys* ($K$) e *Values* ($V$) são provenientes da saída processada pelo Encoder. Isso permite ao Decoder focar nas partes relevantes da frase de origem durante a geração do texto de destino.

---

### Questão 23 (Difícil - Pegadinha)

Considere a técnica de regularização **L2 Regularization** (também conhecida como *Weight Decay* em SGD padrão). Ao adicionar o termo $\frac{1}{2} \lambda \sum w^2$ à função de perda $J(\theta)$, como fica a regra de atualização dos pesos no passo da descida do gradiente?

A) $w_{t+1} = w_t - \alpha \nabla J(w_t) + \lambda$

B) $w_{t+1} = (1 - \alpha \lambda) w_t - \alpha \nabla J(w_t)$

C) $w_{t+1} = \frac{w_t}{1 + \alpha \nabla J(w_t)}$

D) $w_{t+1} = w_t \cdot \alpha \lambda$

E) $w_{t+1} = w_t - \alpha \lambda \nabla J^2(w_t)$

**Resposta Correta: B**

**Comentário:** *Pegadinha matemática!* A nova função de custo é $J_{reg}(w) = J(w) + \frac{1}{2} \lambda w^2$. A derivada em relação a $w$ é $\frac{\partial J_{reg}}{\partial w} = \frac{\partial J}{\partial w} + \lambda w$. Substituindo na regra do gradiente $w_{t+1} = w_t - \alpha \frac{\partial J_{reg}}{\partial w}$:

$$
w_{t+1} = w_t - \alpha \left(\frac{\partial J}{\partial w} + \lambda w_t\right) = w_t - \alpha \lambda w_t - \alpha \frac{\partial J}{\partial w} = (1 - \alpha \lambda) w_t - \alpha \nabla J(w_t)
$$

O termo $(1 - \alpha \lambda)$ multiplica o peso atual por um fator ligeiramente menor que $1$ a cada iteração (decay), reduzindo continuamente os pesos irrelevantes para zero.

---

### Questão 24 (Médio)

O que é a técnica de **Convolução Separável em Profundidade (*Depthwise Separable Convolution*)** utilizada em arquiteturas eficientes para dispositivos móveis, como a **MobileNet**?

A) Uma convolução que divide a imagem em 4 quadrantes independentes.

B) A divisão da convolução padrão em duas etapas mais leves: uma *Depthwise Convolution* (convolução espacial $k \times k$ independente aplicativa a cada canal) seguida por uma *Pointwise Convolution* (convolução $1 \times 1$ que combina os canais).

C) A substituição de todas as multiplicações por somas inteiras.

D) Uma convolução executada exclusivamente na CPU para economizar bateria.

E) A aplicação de filtros convolucionais apenas nos pixels de borda da imagem.

**Resposta Correta: B**

**Comentário:** A convolução tradicional $k \times k$ processa espaço e canais simultaneamente, exigindo $D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$ operações. A *Depthwise Separable Convolution* fatia o processo em:
1. **Depthwise:** Aplica filtros $k \times k$ em cada um dos $M$ canais de entrada individualmente.
2. **Pointwise:** Aplica filtros $1 \times 1$ para projetar os $M$ canais em $N$ canais de saída.
Isso reduz o custo computacional e o número de parâmetros em até $8$ a $9$ vezes sem perda significativa de acurácia.

---

### Questão 25 (Fácil)

Em visão computacional, o que caracteriza a técnica de **Transfer Learning (Aprendizado por Transferência)** usando um modelo pré-treinado na ImageNet?

A) Treinar uma rede neural do zero sem utilizar nenhum dado de entrada.

B) Aproveitar os pesos e representações visuais genéricas (como bordas, texturas e formas) já aprendidas por um modelo em um grande conjunto de dados e adaptá-lo para uma nova tarefa específica com poucos dados.

C) Transferir o código de execução do PyTorch para o TensorFlow sem alterar a linguagem.

D) Exportar os dados de treinamento via pendrive entre servidores.

E) Converter automaticamente redes neurais em árvores de decisão.

**Resposta Correta: B**

**Comentário:** O *Transfer Learning* evita o custo proibitivo de treinar redes profundas do zero. As primeiras camadas de redes treinadas no ImageNet aprendem extratores de recursos genéricos (*low-level features*). Congelam-se essas camadas iniciais e substitui-se apenas a camada final de classificação (*head*) para ser treinada no novo dataset alvo.

---

### Questão 26 (Difícil - Pegadinha)

Ao utilizar a função de perda **Cross-Entropy Loss** combinada com a camada de ativação **Softmax** na saída de uma rede neural, o cálculo das derivadas parciais durante a retropropagação resulta em uma forma notavelmente simples para o gradiente da perda em relação ao *logit* pré-ativação $z_i$. Qual é essa expressão simplificada?

A) $\frac{\partial L}{\partial z_i} = p_i - y_i$ (onde $p_i$ é a probabilidade prevista pela Softmax e $y_i$ é o rótulo real codificado em one-hot)

B) $\frac{\partial L}{\partial z_i} = \frac{p_i}{y_i}$

C) $\frac{\partial L}{\partial z_i} = p_i(1 - p_i) y_i$

D) $\frac{\partial L}{\partial z_i} = \ln(p_i - y_i)$

E) $\frac{\partial L}{\partial z_i} = 0$ para todas as saídas.

**Resposta Correta: A**

**Comentário:** *Pegadinha de elegância matemática!* Embora a derivada da Softmax envolva uma matriz Jacobiana complexa e a Cross-Entropy envolva logaritmos, a combinação das duas ($L = -\sum y_i \ln(p_i)$ com $p_i = \frac{e^{z_i}}{\sum e^{z_j}}$) resulta em um cancelamento perfeito ao aplicar a regra da cadeia:

$$
\frac{\partial L}{\partial z_i} = p_i - y_i
$$

O gradiente transmitido para a camada anterior é simplesmente a diferença linear entre a probabilidade estimada $p_i$ e o alvo verdadeiro $y_i$. Isso evita a saturação de gradientes no treinamento e explica por que Softmax e Cross-Entropy são quase sempre usadas juntas.

---

### Questão 27 (Médio)

O que é a técnica de **Gradient Clipping (Corte do Gradiente)** e para qual problema crítico em redes neurais recorrentes profundas ela foi projetada?

A) Ela desativa neurônios aleatoriamente para evitar *overfitting*.

B) Ela limita a norma máxima do vetor de gradiente a um limiar pré-definido $c$ (ex: se $\|\mathbf{g}\| > c$, faz-se $\mathbf{g} \leftarrow c \frac{\mathbf{g}}{\|\mathbf{g}\|}$), prevenindo a explosão do gradiente (*exploding gradient*).

C) Ela zera os pesos que são menores do que zero para comprimir o modelo.

D) Ela força todas as perdas a se tornarem negativas.

E) Ela corta as primeiras 10 camadas do modelo durante o teste.

**Resposta Correta: B**

**Comentário:** Em redes recorrentes (RNNs) processando sequências longas, os gradientes podem crescer exponencialmente a cada passo de tempo no *Backpropagation Through Time (BPTT)*, resultando em estouro numérico (`NaN`). O *Gradient Clipping* monitora a norma do vetor de gradiente e, se ela ultrapassar um limite $c$, o vetor é reescalado para ter norma $c$, mantendo a direção original do gradiente mas evitando saltos catastróficos nos pesos.

---

### Questão 28 (Fácil)

Qual é a função do termo de **Viés (Bias)** $b$ em um neurônio artificial padrão definido pela equação $y = f(\mathbf{w}^T \mathbf{x} + b)$?

A) Forçar a reta/hiperplano de decisão a passar obrigatoriamente pela origem $(0,0)$.

B) Permitir deslocar a função de ativação ao longo do eixo espacial, fornecendo ao neurônio a capacidade de ajustar a fronteira de decisão independentemente da magnitude das entradas.

C) Multiplicar a taxa de aprendizado por uma constante.

D) Armazenar o gradiente da época anterior.

E) Evitar que a GPU utilize memória VRAM.

**Resposta Correta: B**

**Comentário:** Sem o termo de viés $b$, a equação do hiperplano $\mathbf{w}^T \mathbf{x} = 0$ seria estritamente vinculada a passar pela origem dos eixos coordenados. O viés $b$ atua como uma constante de translação, permitindo ajustar a linha de decisão para qualquer posição no espaço.

---

### Questão 29 (Difícil - Pegadinha)

O modelo **BERT (Bidirectional Encoder Representations from Transformers)** é pré-treinado utilizando duas tarefas auto-supervisionadas principais. Quais são elas?

A) Masked Language Modeling (MLM) e Next Sentence Prediction (NSP).

B) Causal Language Modeling (CLM) e Generative Adversarial Training.

C) Translation e Image Captioning.

D) Contrastive Learning e Triplet Loss.

E) Text-to-Speech e Sentiment Analysis.

**Resposta Correta: A**

**Comentário:** O BERT introduziu o pré-treinamento bidirecional combinando duas tarefas:
1. **Masked Language Modeling (MLM):** Mascara aleatoriamente $15\%$ dos tokens de entrada e treina o modelo para prever a palavra oculta com base no contexto à esquerda e à direita.
2. **Next Sentence Prediction (NSP):** Dada uma dupla de frases $A$ e $B$, o modelo prevê se a frase $B$ é a continuação lógica da frase $A$ no texto original.

---

### Questão 30 (Médio)

Considere o otimizador **Stochastic Gradient Descent (SGD)** operando com tamanho de mini-lote $B = 1$ (SGD puro), $B = 32$ (Mini-batch SGD) e $B = N$ (Batch Gradient Descent completo, onde $N$ é o dataset inteiro). Qual das afirmativas abaixo descreve **corretamente** as diferenças de comportamento durante o treinamento?

A) $B = N$ é o método mais ruidoso e requer o maior uso de memória RAM/GPU para instanciar as saídas de cada época.

B) $B = 1$ é altamente determinístico e avança diretamente em linha reta rumo ao mínimo global.

C) $B = 32$ (Mini-batch) oferece um compromisso ideal entre a eficiência de vetorização paralela em hardware (GPUs) e a introdução de ruído estocástico benéfico para escapar de selas e mínimos locais rasos.

D) O tamanho do mini-lote não altera o tempo de execução nem o cálculo dos gradientes.

E) $B = N$ garante que o modelo nunca sofra overfitting.

**Resposta Correta: C**

**Comentário:** O SGD por mini-lote ($B = 32$ ou $64$) é o padrão prático em Deep Learning. O cálculo sobre pequenos lotes de dados introduz uma flutuação estocástica suficiente no gradiente para ajudar a rede a saltar fora de pontos de sela (*saddle points*) e mínimos locais ruins. Ao mesmo tempo, ele aproveita a capacidade de multiprocessamento paralelo de tensores das GPUs, superando o gasto de tempo do ponto a ponto do $B=1$ e a imensa exigência de memória do $B=N$.

```

---

O simulado contendo as 30 questões sobre **Aprendizado Profundo (Deep Learning)**, com pegadinhas, alternativas distribuídas e gabarito comentado, está gerado e disponível para consulta no painel ao lado.