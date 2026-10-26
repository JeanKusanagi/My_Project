# A Evolução da Representação de Texto em NLP

Este documento reúne a evolução cronológica e conceitual das técnicas de Processamento de Linguagem Natural (PLN) para transformação de textos em vetores numéricos, partindo do básico Bag of Words até os modelos contextuais modernos (Transformers).

---

## 1. Bag of Words (BoW)

O **Bag of Words** (ou "saco de palavras") é uma técnica simples usada para transformar textos em **vetores numéricos** com base na contagem de termos.

### Como funciona
1. **Criação do vocabulário:** O algoritmo lê todos os textos do seu conjunto e monta uma lista única com todas as palavras existentes neles.
2. **Transformação em vetor:** Cada texto é convertido em uma sequência de números (um vetor). Cada posição do vetor corresponde a uma palavra do vocabulário.
3. **Contagem:** O valor inserido em cada posição representa a presença ou a frequência daquela palavra no texto.

### Exemplo Prático
* **Frase 1:** *"O gato comeu o peixe"*
* **Frase 2:** *"O cachorro comeu a ração"*

**Vocabulário único:** `[O, gato, comeu, peixe, cachorro, a, ração]`

* **Vetor da Frase 1:** [2, 1, 1, 1, 0, 0, 0] *(a palavra "O" aparece 2 vezes, "gato" 1 vez, etc.)*
* **Vetor da Frase 2:** [1, 0, 1, 0, 1, 1, 1]

### Limitações
* **Ignora a ordem e a gramática:** Ele joga fora a estrutura da frase. Para o modelo, *"O gato comeu o peixe"* e *"O peixe comeu o gato"* geram exatamente os mesmos vetores.

---

## 2. TF-IDF (Term Frequency-Inverse Document Frequency)

O **TF-IDF** é uma evolução do Bag of Words. Enquanto o BoW apenas conta a quantidade de vezes que uma palavra aparece, o TF-IDF calcula a **importância real de uma palavra em um texto** dentro de um conjunto de vários textos (chamado de *corpus*).

A principal vantagem do TF-IDF é **penalizar termos muito comuns** (como "o", "de", "que") que aparecem em quase todos os textos e não ajudam a diferenciar um assunto do outro.

### O Cálculo
O TF-IDF é o resultado da multiplicação de dois fatores:
* **TF (Term Frequency):** Mede a frequência de uma palavra em um documento específico.
* **IDF (Inverse Document Frequency):** Mede a raridade da palavra em todo o conjunto de textos. Quanto mais rara no ecossistema de dados, maior o seu peso.

### Exemplo Prático
Imagine um portal com **1.000 artigos**:
* **Palavra "O":** Aparece 50 vezes em um artigo sobre esportes, mas também aparece em todos os outros 1.000 artigos. Seu IDF será próximo de zero, resultando em um **TF-IDF muito baixo**.
* **Palavra "Neymar":** Aparece 50 vezes no mesmo artigo, mas só existe em 5 dos 1.000 artigos do portal. Seu IDF será altíssimo, gerando um **TF-IDF muito alto** (indicando relevância).

---

## 3. Embeddings de Palavras Estáticas (Word2Vec)

As **Embeddings de Palavras** resolvem as limitações do TF-IDF ao **capturar o significado (semântica) e o contexto**, transformando palavras em vetores densos onde termos com sentidos parecidos ficam matematicamente próximos.

### Como resolve as limitações anteriores:
1. **O problema dos sinônimos:** No TF-IDF, *"médico"* e *"doutor"* são tratados como termos totalmente distintos. No Word2Vec, como ambos aparecem cercados por palavras vizinhas parecidas ("hospital", "saúde"), eles ganham vetores muito similares.
2. **A "Maldição da Dimensionalidade":** Em vez de gerar vetores gigantescos e vazios (esparsos) do tamanho do vocabulário, as embeddings representam qualquer palavra em um espaço fixo e compacto (geralmente de 100 a 300 dimensões).
3. **Álgebra Semântica:** É possível realizar operações matemáticas com os conceitos:
   Vetor("Rei") - Vetor("Homem") + Vetor("Mulher") = Vetor("Rainha")

### Limitação do Word2Vec
* **Palavras homônimas:** A palavra *"banco"* (instituição financeira) e *"banco"* (assento de praça) recebem exatamente o mesmo vetor fixo no dicionário do modelo.

---

## 4. Embeddings Contextuais (BERT e GPT)

Para resolver o problema da polissemia (múltiplos significados), surgiram as **Embeddings Contextuais**, introduzidas por redes neurais modernas chamadas **Transformers**. Aqui, **o vetor de uma palavra muda dinamicamente dependendo da frase inteira**.

### O Mecanismo de Atenção (*Self-Attention*)
O modelo lê a frase inteira de uma vez e calcula o quanto cada palavra se relaciona com todas as outras da mesma sentença.

* **Frase A:** *"Fui ao **banco** pagar uma conta."* -> O modelo conecta "banco" a "pagar" e "conta". O vetor gerado foca no sentido **financeiro**.
* **Frase B:** *"Sentei no **banco** da praça."* -> O modelo conecta "banco" a "sentei" e "praça". O vetor gerado muda para o sentido de **mobiliário**.

### BERT vs. GPT
* **BERT (Bidirecional):** Olha para o contexto da esquerda e da direita ao mesmo tempo. Ideal para análise de texto e classificação.
* **GPT (Unidirecional):** Olha para o contexto apenas da esquerda para a direita (passado). Ideal para geração de texto e conversação.

---

## Resumo Comparativo

| Técnica | Abordagem Principal | Representação Vetorial | Captura Semântica? | Trata Homônimos? |
| :--- | :--- | :--- | :--- | :--- |
| **Bag of Words** | Contagem bruta de termos | Vetor Esparso (Longo / Zeros) | Não | Não |
| **TF-IDF** | Peso estatístico por raridade | Vetor Esparso (Longo / Zeros) | Não | Não |
| **Word2Vec** | Aprendizado por vizinhança | Vetor Denso (Curto / Fixo) | Sim (Estática) | Não |
| **BERT / GPT** | Mecanismo de Atenção Global | Vetor Denso (Curto / Dinâmico) | Sim (Contextual) | Sim |
