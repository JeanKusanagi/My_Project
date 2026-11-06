# Guia Completo: Redes Neurais Recorrentes (RNNs) e suas Variantes (LSTM e GRU)

Este documento reúne os conceitos fundamentais, estruturas matemáticas, implementações práticas e variantes das arquiteturas de redes neurais voltadas para dados sequenciais.

---

## 1. Introdução às Redes Neurais Recorrentes (RNNs)

As **Redes Neurais Recorrentes** (RNNs, do inglês *Recurrent Neural Networks*) são uma classe de redes neurais artificiais projetadas para processar **dados sequenciais e temporais** (como textos, fala, séries temporais e áudio), onde a ordem dos elementos é fundamental.

### O que as difere das redes tradicionais?
* **Redes *Feedforward* tradicionais:** Tratam cada entrada de forma totalmente independente e assumem que não há conexão temporal entre elas.
* **Redes Recorrentes (RNNs):** Possuem uma "memória" interna (chamada de **estado oculto**). A saída gerada em um passo de tempo é retroalimentada e combinada com a nova entrada no passo seguinte, permitindo que a rede lembre de informações anteriores.
* **Compartilhamento de pesos:** Ao contrário das redes tradicionais que usam pesos diferentes em cada nó, a RNN reutiliza os mesmos pesos em todas as etapas da sequência.

### Principais Estruturas de Entrada/Saída
As RNNs se dividem em diferentes formatos conforme a necessidade do problema:
* **Um-para-muitos (*One-to-Many*):** Uma única entrada gera uma sequência (ex: legendagem de imagens).
* **Muitos-para-um (*Many-to-One*):** Uma sequência de entrada gera uma única saída (ex: análise de sentimentos ou previsão de preços de ações).
* **Muitos-para-muitos (*Many-to-Many*):** Sequência de entrada gera uma sequência de saída (ex: tradução automática ou reconhecimento de fala).

### Principais Limitações das RNNs Padrão
* **Dificuldade com sequências longas:** Sofrem com o problema do gradiente explosivo ou desaparecente durante a retropropagação no tempo (*Backpropagation Through Time* - BPTT). O sinal do erro dissipa ao longo de muitos passos e a rede "esquece" o passado distante.

---

## 2. Camadas LSTM (Long Short-Term Memory)

As **camadas LSTM** foram criadas especificamente para resolver o problema da perda de memória em sequências longas. O grande segredo da LSTM é a sua estrutura interna baseada em uma **linha de estado da célula (Cell State)** — que funciona como uma esteira transportadora de informações — controlada por três comportas matemáticas chamadas **portas (*gates*)**.

### Como funciona uma célula LSTM (Passo a Passo)

1. **Porta de Esquecimento (*Forget Gate*):** Decide o que descartar do passado. Ela analisa a informação atual e o estado anterior aplicando uma função *sigmoide* (valores próximos de 0 deletam, próximos de 1 mantêm).
2. **Porta de Entrada (*Input Gate*):** Decide quais novas informações salvar no estado da célula.
3. **Atualização do Estado da Célula (*Cell State*):** A esteira é atualizada: a rede joga fora o que decidiu esquecer e soma os novos dados validados pela porta de entrada.
4. **Porta de Saída (*Output Gate*):** Decide qual será a próxima previsão ou estado oculto lançado para o próximo passo.

### Fórmulas Matemáticas da LSTM

Considerando:
* $x_t$: Vetor de entrada no momento atual.
* $h_{t-1}$: Estado oculto (*hidden state*) do passo anterior.
* $C_{t-1}$: Estado da célula (*cell state*) do passo anterior.
* $W$ e $b$: Pesos e vieses (*biases*) aprendidos no treinamento.
* $\sigma$: Função de alta ativação Sigmoide.
* $	anh$: Função de ativação Tangente Hiperbólica.
* $\odot$: Multiplicação elemento a elemento (Produto de Hadamard).

As 6 equações fundamentais que regem uma célula LSTM são:

1. **Porta de Esquecimento:**
   $$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$

2. **Porta de Entrada:**
   $$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$

3. **Candidato ao Estado da Célula:**
   $$	ilde{C}_t = 	anh(W_c \cdot [h_{t-1}, x_t] + b_c)$$

4. **Atualização do Estado da Célula:**
   $$C_t = f_t \odot C_{t-1} + i_t \odot 	ilde{C}_t$$

5. **Porta de Saída:**
   $$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$

6. **Novo Estado Oculto:**
   $$h_t = o_t \odot 	anh(C_t)$$

---

## 3. Implementação Prática: Previsão de Séries Temporais

Abaixo está um script em **Python** utilizando **Keras/TensorFlow** para transformar uma série temporal contínua em um problema de aprendizado supervisionado usando uma janela de histórico (*lookback*).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1. Gerar dados sintéticos (série temporal com tendência e ruído)
np.random.seed(42)
tempo = np.arange(0, 200, 0.5)
dados = np.sin(tempo) + 0.1 * tempo + np.random.normal(0, 0.1, len(tempo))
dados = dados.reshape(-1, 1)

# 2. Normalizar os dados (essencial para evitar saturação de gradientes na LSTM)
scaler = MinMaxScaler(feature_range=(0, 1))
dados_normalizados = scaler.fit_transform(dados)

# 3. Criar a estrutura de janelas temporais (Lookback)
def criar_dataset(dataset, look_back=10):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        X.append(dataset[i:(i + look_back), 0])
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

LOOK_BACK = 10
X, Y = criar_dataset(dados_normalizados, LOOK_BACK)

# Redimensionar para o formato da LSTM: [amostras, passos_de_tempo, recursos]
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Divisão em Treino (80%) e Teste (20%)
divisao = int(len(X) * 0.8)
X_treino, X_teste = X[:divisao], X[divisao:]
Y_treino, Y_teste = Y[:divisao], Y[divisao:]

# 4. Construir o Modelo
modelo = Sequential([
    LSTM(50, input_shape=(LOOK_BACK, 1), activation='tanh'),
    Dense(1)
])
modelo.compile(optimizer='adam', loss='mean_squared_error')

# 5. Treinar a Rede Neural
modelo.fit(X_treino, Y_treino, epochs=20, batch_size=4, verbose=1)

# 6. Fazer as Previsões
previsoes_teste = modelo.predict(X_teste)

# Inverter a normalização para escala original
previsoes_teste = scaler.inverse_transform(previsoes_teste)
Y_teste_original = scaler.inverse_transform(Y_teste.reshape(-1, 1))

# 7. Plotar os Resultados
plt.figure(figsize=(12, 6))
plt.plot(Y_teste_original, label='Dados Reais (Teste)', color='blue')
plt.plot(previsoes_teste, label='Previsão LSTM', color='red', linestyle='--')
plt.title('Previsão de Série Temporal com LSTM')
plt.xlabel('Passos de Tempo')
plt.ylabel('Valor')
plt.legend()
plt.show()
```

---

## 4. Variantes de Arquitetura: LSTM e GRU

As variantes surgiram para equilibrar o poder de memorização com a eficiência de processamento.

### Gated Recurrent Unit (GRU)
A **GRU** é a variante simplificada mais famosa da LSTM (Cho et al., 2014).
* **Fusão de Estados:** Elimina o *Cell State* e mantém apenas o *Hidden State*.
* **Duas Portas:** Possui a porta de **Atualização (*Update Gate*)** (combina esquecimento e entrada) e a porta de **Redefinição (*Reset Gate*)** (controla o quanto do passado ignorar).
* **Vantagem:** Possui cerca de **25% a menos de parâmetros** que a LSTM, tornando-a muito mais rápida para treinar em computadores modestos ou datasets menores.

### Peephole LSTM
Permite que as portas de controle olhem diretamente para o *Cell State* ($C_{t-1}$) antes de tomarem decisões, garantindo uma sincronização temporal milimétrica (muito usada em processamento de áudio).

### Coupled Input and Forget Gate (CIFG)
Acopla as portas de esquecimento e entrada de modo que o que entra de nova informação é exatamente o inverso do que se esquece ($1 - f_t$), reduzindo o número total de matrizes de peso a calcular.

### Redes Bidirecionais (BiLSTM / BiGRU)
Duplica a estrutura da camada: uma processa o dado de forma cronológica normal (esquerda para a direita) e a outra lê de trás para frente (direita para a esquerda). Essencial para extrair contexto em Processamento de Linguagem Natural (NLP).

---

## Comparativo de Escolha de Arquitetura

| Arquitetura | Quando Escolher? | Principal Gargalo |
| :--- | :--- | :--- |
| **LSTM Tradicional** | Sequências longas onde dependências históricas profundas importam. | Treinamento lento e pesado. |
| **GRU** | Hardware limitado, datasets menores ou necessidade de iterações rápidas. | Pode falhar em sequências excessivamente longas. |
| **Peephole LSTM** | Sinais analógicos ou áudios com precisão de tempo milimétrica. | Maior custo de desenvolvimento matemático. |
| **Bidirecional** | Análise de textos ou sequências onde o futuro ajuda a entender o passado. | Inviável para previsões em tempo real (online). |
