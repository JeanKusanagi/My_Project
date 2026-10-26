# Guia Completo: Modelos Transformers e Fine-Tuning

Este documento reúne os conceitos fundamentais sobre as arquiteturas BERT, GPT, BART e T5, além de um guia prático passo a passo para aplicação de Fine-Tuning em Processamento de Linguagem Natural (PLN).

---

## 1. Comparação de Arquiteturas Transformers

Abaixo está um resumo das diferenças estruturais e objetivos principais de cada modelo:

| Modelo | Arquitetura | Direcionalidade / Fluxo | Foco Principal |
| :--- | :--- | :--- | :--- |
| **BERT** | Encoder-Only | Bidirecional (vê a frase inteira) | Compreensão e análise de texto |
| **GPT** | Decoder-Only | Unidirecional (da esquerda para a direita) | Geração de texto e conversação |
| **T5** | Encoder-Decoder | Texto-para-Texto (Text-to-Text) | Versatilidade máxima (tradução, resumo) |
| **BART** | Encoder-Decoder | Bidirecional (Encoder) + Autoregressivo (Decoder) | Resumos e reconstrução de sequências |

---

## 2. Detalhes de Cada Modelo

### BERT (*Bidirectional Encoder Representations from Transformers*)
* **Desenvolvedor:** Google
* **Como funciona:** Usa apenas a parte de **Encoder** do Transformer. Ele analisa o contexto de uma palavra olhando tanto para a esquerda quanto para a direita ao mesmo tempo (bidirecional).
* **Melhor para:** Compreensão de texto, análise de sentimentos, extração de informações e resposta a perguntas (QA).

### GPT (*Generative Pre-trained Transformer*)
* **Desenvolvedor:** OpenAI
* **Como funciona:** Usa apenas a parte de **Decoder** do Transformer. Ele é **autoregressivo**, ou seja, prevê o próximo token (palavra) com base apenas no contexto anterior (da esquerda para a direita).
* **Melhor para:** Geração de texto fluido, conclusão de frases, redação e assistentes conversacionais (chatbots).

### T5 (*Text-to-Text Transfer Transformer*)
* **Desenvolvedor:** Google Research
* **Como funciona:** Usa a estrutura completa de **Encoder-Decoder**. O T5 trata **todas** as tarefas de PLN como um problema de "texto para texto" (você fornece um comando em formato de texto e ele devolve a resposta também em texto).
* **Melhor para:** Tradução automática, sumarização e conversão/transformação de formatos.

### BART (*Bidirectional and Auto-Regressive Transformer*)
* **Desenvolvedor:** Meta (Facebook AI)
* **Como funciona:** Combina um **Encoder bidirecional** (semelhante ao BERT) com um **Decoder autoregressivo** (semelhante ao GPT). É pré-treinado corrompendo o texto original e treinando o modelo para reconstruí-lo (*denoising*).
* **Melhor para:** Geração de resumos (*summarization*), tradução e reescrita de textos.

---

## 3. Como Aplicar Fine-Tuning

O **fine-tuning** (ajuste fino) consiste em pegar um modelo pré-treinado e treiná-lo levemente em um **conjunto de dados específico** para realizar uma tarefa dedicada.

### Passo a Passo Prático (Hugging Face `transformers`)

#### Passo 1: Preparar o Dataset
Os dados precisam estar no formato aceito pelo modelo (geralmente pares de texto e rótulo).

```python
from datasets import load_dataset

# Exemplo carregando um dataset de classificação de texto
dataset = load_dataset("imdb")
```

#### Passo 2: Carregar o Tokenizador e o Modelo
Converta o texto bruto em números (tokens) usando o tokenizador do próprio modelo.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Escolha do modelo base (ex: BERT para classificação)
model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
```

#### Passo 3: Tokenizar os Dados
Aplique a tokenização em lote (*batch*) em todo o seu conjunto de dados.

```python
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
```

#### Passo 4: Configurar os Hiperparâmetros (`TrainingArguments`)
Define taxas de aprendizado (*learning rate*), épocas, tamanhos de lote (*batch size*) e diretórios.

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    evaluation_strategy="epoch"
)
```

#### Passo 5: Iniciar o Treinamento (`Trainer`)
Gerencie o loop de treinamento de forma simplificada sem precisar estruturar o código bruto em PyTorch ou TensorFlow.

```python
from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

# Executa o ajuste fino
trainer.train()
```

---

## 4. Estratégias Modernas de Fine-Tuning (PEFT)

Para modelos de grande porte onde o ajuste fino completo é inviável devido ao custo computacional, utilizam-se técnicas de **PEFT (Parameter-Efficient Fine-Tuning)**:

* **LoRA (Low-Rank Adaptation):** Congela os pesos originais do modelo e injeta pequenas matrizes matemáticas adicionais para serem treinadas. Reduz o uso de memória de GPU em até 3 vezes.
* **QLoRA:** Evolução do LoRA que carrega o modelo original em alta compressão quantizada (4-bit), viabilizando o fine-tuning de LLMs comerciais em GPUs de nível de consumidor.