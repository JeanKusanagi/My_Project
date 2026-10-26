# Guia Completo de Tokenização: BPE, WordPiece e Unigram

Este documento reúne todo o conteúdo abordado sobre algoritmos de tokenização por subpalavras utilizados em Grandes Modelos de Linguagem (LLMs).

---

## 1. O que é Byte-Pair Encoding (BPE)
O **Byte-Pair Encoding (BPE)** é um algoritmo de tokenização e compressão de dados que divide textos em unidades chamadas de **subpalavras**. 

Originalmente criado em 1994 por Philip Gage para compressão de arquivos, o BPE foi adaptado para o **Processamento de Linguagem Natural (PLN)** e é amplamente utilizado por LLMs como o GPT (OpenAI) e o LLaMA (Meta).

### Como Funciona o Algoritmo
O BPE busca um meio-termo entre tratar cada letra isoladamente (muito lento e sem sentido semântico) e tratar cada palavra inteira como um token único (o que exigiria um vocabulário gigantesco e falharia com palavras raras ou novas). 

O processo acontece em etapas:
1. **Inicialização:** O texto é separado em caracteres individuais ou bytes básicos.
2. **Contagem de frequência:** O algoritmo analisa o texto e conta a frequência de pares de símbolos adjacentes (digramas).
3. **Fusão (*Merge*):** O par de símbolos que aparece junto com mais frequência é combinado em um **novo símbolo único**.
4. **Repetição:** O processo de contagem e fusão é repetido várias vezes até que o vocabulário atinja um tamanho pré-determinado (geralmente entre 32.000 e 128.000 tokens).

### Principais Vantagens
* **Eficiência com palavras desconhecidas:** Se o modelo encontrar uma palavra que nunca viu antes, ele não quebra por completo; em vez disso, divide a palavra em subpalavras ou pedaços menores que ele já conhece.
* **Equilíbrio no tamanho do vocabulário:** Palavras muito comuns viram um único token, enquanto palavras complexas ou derivadas são divididas em radicais, prefixos e sufixos lógicos (como separar *infelizmente* em *infeliz* + *mente*).
* **Suporte universal:** Pode representar qualquer sequência de texto usando apenas a combinação do seu vocabulário base de caracteres e subpalavras.

---

## 2. Exemplo Prático Passo a Passo (BPE)
Simulação do treinamento do BPE em um texto muito curto contendo as seguintes palavras e suas frequências:
* **"gato"** (aparece 5 vezes)
* **"garganta"** (aparece 3 vezes)
* **"alto"** (aparece 2 vezes)

### Passo 1: Inicialização do Vocabulário Base
O algoritmo começa separando cada palavra em caracteres e adicionando um caractere especial de fim de palavra (`</w>`). 
> **Vocabulário Inicial:** `[a, g, l, o, n, r, t, </w>]`

O texto separado fica assim:
* 5x: `g` `a` `t` `o` `</w>`
* 3x: `g` `a` `r` `g` `a` `n` `t` `a` `</w>`
* 2x: `a` `l` `t` `o` `</w>`

### Passo 2: Contagem de Pares (1ª Rodada)
O BPE analisa quais pares de letras adjacentes aparecem com mais frequência em todo o texto:
* O par **`g` `a`** aparece 5 vezes em "gato" e 6 vezes em "garganta" (já que aparece duas vezes na palavra). **Total = 11**
* O par **`a` `t`** aparece 5 vezes em "gato" e 2 vezes em "alto". **Total = 7**
* O par **`t` `o`** aparece 5 vezes em "gato" e 2 vezes em "alto". **Total = 7**

O par mais frequente é **`g` `a`** (11 vezes).

### Passo 3: Primeira Fusão (Merge)
O algoritmo cria um novo token chamado **`ga`** e o adiciona ao vocabulário.
> **Vocabulário Atual:** `[a, g, l, o, n, r, t, </w>, ga]`

O texto agora é atualizado onde havia `g` e `a` juntos:
* 5x: `ga` `t` `o` `</w>`
* 3x: `ga` `r` `ga` `n` `t` `a` `</w>`
* 2x: `a` `l` `t` `o` `</w>`

### Passo 4: Próxima Fusão (2ª Rodada)
O algoritmo reconta os pares com os novos dados:
* O par **`ga` `t`** aparece 5 vezes (em "gato"). **Total = 5**
* O par **`t` `o`** aparece 5 vezes em "gato" e 2 vezes em "alto". **Total = 7**

Agora o par mais frequente é **`t` `o`**. O algoritmo cria o token **`to`**.
> **Vocabulário Atual:** `[a, g, l, o, n, r, t, </w>, ga, to]`

O texto atualizado:
* 5x: `ga` `to` `</w>`
* 3x: `ga` `r` `ga` `n` `t` `a` `</w>`
* 2x: `a` `l` `to` `</w>`

### Passo 5: Fusão Final (3ª Rodada)
Buscando o próximo par mais frequente:
* O par **`ga` `to`** aparece 5 vezes (em "gato"). **Total = 5**
* O par **`to` `</w>`** aparece 5 vezes em "gato" e 2 vezes em "alto". **Total = 7**

O par mais frequente é **`to` `</w>`**. O algoritmo cria o token **`to</w>`**.
> **Vocabulário Final:** `[a, g, l, o, n, r, t, </w>, ga, to, to</w>]`

O texto finalizado:
* 5x: `ga` `to</w>` (Transformado em apenas 2 tokens!)
* 3x: `ga` `r` `ga` `n` `t` `a` `</w>`
* 2x: `a` `l` `to</w>`

### Resultado Prático na Tokenização
Se o modelo treinado com esse vocabulário encontrar a palavra **"galpão"** (uma palavra nova que ele nunca viu antes), ele a dividirá usando os pedaços que conhece:
> **"galpão"** viraria os tokens: `[ga]` + `[l]` + `[p]` + `[ã]` + `[o]`

---

## 3. Lidar com Espaços em Branco no Texto Real
No texto real, os **espaços em branco são tratados como caracteres normais**, mas recebem uma marcação especial para permitir a reconstrução exata do texto (*lossless*).

### Abordagem 1: O caractere especial de espaço inicial (`Ġ` ou `_`)
Modelos como o GPT-2, GPT-3 e GPT-4 substituem os espaços normais pelo caractere **`Ġ`** (ou `_` no *SentencePiece*) antes de iniciar as fusões.
* Exemplo: O texto *"o gato"* vira internamente `o` `Ġgato`. O espaço fica grudado na palavra seguinte.

### Abordagem 2: O caractere de fim de palavra (`</w>`)
Abordagem original do BPE. Ele marca o *final* de cada palavra isolada.
* Exemplo: *"gato preto"* vira `g a t o </w> p r e t o </w>`. Ao encontrar `</w>`, o modelo sabe que deve inserir um espaço na hora de reconstruir o texto.

### Por que isso é feito?
1. **Perda de formatação:** Permite entender múltiplos espaços seguidos (como códigos com indentação Tab ou quatro espaços).
2. **Linguagens sem espaços:** Permite que o BPE funcione de forma universal para idiomas que não separam palavras por espaços (como Chinês ou Japonês).

---

## 4. Como Descobrir o Número Exato de Tokens no GPT
A contagem de tokens pode variar conforme o modelo utilizado (GPT-3.5/4 usa o tokenizador `cl100k_base`, enquanto o GPT-4o usa o `o200k_base`, que é muito mais otimizado para o português).

1. **Interface Visual:** Através da ferramenta web oficial **OpenAI Tokenizer** (ou ferramentas similares de terceiros, como o Tiktokenizer).
2. **Usando Python (`tiktoken`):**
   ```python
   import tiktoken
   enc = tiktoken.get_encoding("o200k_base")
   tokens = enc.encode("O gato subiu no telhado.")
   print(len(tokens))
   ```
3. **Pelo ChatGPT:** Solicitando diretamente ao ChatGPT usando um comando que acione a execução de código para maior precisão.

---

## 5. Algoritmo WordPiece
Muito utilizado no **BERT** (Google) e seus derivados. Embora quebre palavras em subpalavras assim como o BPE, seu critério de escolha é diferente.

* **Diferença de Critério (Frequência vs. Probabilidade):** O BPE une os pares mais *frequentes*. O WordPiece usa **Máxima Verossimilhança**, escolhendo o par que traz o maior ganho probabilístico/estatístico para o modelo como um todo.
* **Marcador de continuação (`##`):** Em vez de marcar o começo com um espaço, ele marca as partes do meio ou do fim de uma palavra recortada.
  * BPE (GPT): `[infeliz]` + `[mente]`
  * WordPiece (BERT): `[infeliz]` + `[##mente]`

---

## 6. Algoritmo Unigram
Usado no framework **SentencePiece** (Google, adotado no T5 e LLaMA original). Opera na lógica inversa (de cima para baixo).

* **Processo de Poda (*Pruning*):** Ele começa com um vocabulário gigante contendo todas as palavras completas e subpalavras possíveis e vai eliminando (podando) gradualmente os tokens que menos importam para a precisão estatística do modelo, até atingir o tamanho final desejado.
* **Múltiplos Caminhos:** Uma mesma palavra pode ser dividida de formas diferentes. Ele calcula qual o caminho estatisticamente mais provável.
* **BPE-Dropout (Regularização):** Permite treinar a IA mostrando a mesma palavra dividida de formas diferentes ao longo do treino, tornando o modelo mais robusto a erros de digitação.

---

## Resumo Comparativo dos Três Algoritmos

| Característica | Byte-Pair Encoding (BPE) | WordPiece | Unigram |
| :--- | :--- | :--- | :--- |
| **Direção** | De baixo para cima (Fusão) | De baixo para cima (Fusão) | De cima para baixo (Poda/Corte) |
| **Critério** | Frequência pura (Mais repetido) | Probabilidade (Soma de informação) | Perda de probabilidade (Descarta o inútil) |
| **Flexibilidade** | Determinístico (Apenas 1 caminho fixo) | Determinístico (Apenas 1 caminho fixo) | Probabilístico (Pode gerar múltiplos caminhos) |