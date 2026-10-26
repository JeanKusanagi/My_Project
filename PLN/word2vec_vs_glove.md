# Word2Vec e GloVe: O que são?

**Word2Vec e GloVe são técnicas de Processamento de Linguagem Natural (PLN) usadas para transformar palavras em vetores numéricos**, um conceito conhecido como *word embeddings*. 

Em termos simples, os computadores não entendem palavras, mas entendem números. Essas duas ferramentas servem como um "tradutor" que transforma o texto em listas de números de forma que **palavras com significados parecidos fiquem representadas por números parecidos**.

---

## 📊 Comparação Direta: Word2Vec vs. GloVe

| Característica | Word2Vec | GloVe (Global Vectors) |
| :--- | :--- | :--- |
| **Criador** | Google (2013) | Stanford (2014) |
| **Abordagem** | Baseada em **predição** (Redes Neurais) | Baseada em **contagem** (Matriz de Coocorrência) |
| **Foco** | Examina palavras locais (vizinhas) em uma janela de texto. | Examina o corpus inteiro (global) para ver a frequência com que as palavras aparecem juntas. |
| **Vantagem** | Excelente para capturar analogias e relações sintáticas. | Ótimo para capturar o contexto global e estatístico do texto. |
| **Treinamento** | Mais rápido para atualizar com novos dados. | Requer computação pesada da matriz global no início. |

---

## 💡 Como cada um funciona?

### Word2Vec
O Word2Vec utiliza uma rede neural simples para prever palavras com base no seu contexto local (as palavras que vêm imediatamente antes ou depois). Ele possui dois modelos internos:
* **CBOW (Continuous Bag of Words):** Tenta adivinhar uma palavra secreta com base nas palavras ao redor. (Ex: "O gato ___ o leite" → prevê "bebeu").
* **Skip-gram:** Faz o oposto. Pega uma palavra e tenta adivinhar quais palavras costumam aparecer ao redor dela.

### GloVe
O GloVe não usa redes neurais para prever palavras individuais. Em vez disso, ele cria uma **matriz gigante de coocorrência** de todo o texto. 
* Ele conta quantas vezes a palavra "gelo" aparece perto de "sólido" em todo o conjunto de dados.
* Depois, usa fatoração de matrizes para transformar esses bilhões de contagens em vetores pequenos e eficientes.

---

## 🧠 O "Poder" dos Embeddings (Exemplo Prático)
A grande mágica de ambos os modelos é que eles conseguem fazer "álgebra com palavras". Se você pegar os vetores gerados por eles, a matemática funciona assim:

$$\text{Vetor(Rei)} - \text{Vetor(Homem)} + \text{Vetor(Mulher)} = \text{Vetor(Rainha)}$$
