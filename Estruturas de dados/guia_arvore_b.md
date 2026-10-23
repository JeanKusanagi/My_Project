# Guia Completo: Árvore B

Uma **Árvore B** (em inglês, *B-tree*) é uma estrutura de dados do tipo árvore, auto-balanceada, que mantém os dados ordenados e permite buscas, acessos sequenciais, inserções e remoções em tempo logarítmico $O(\log n)$.

Diferente das árvores binárias comuns, a árvore B é de **múltiplos caminhos** (ou *multiway*), o que significa que cada nó pode ter mais do que dois filhos.

---

## 1. Principais Características

* **Otimização para Discos:** É amplamente utilizada em **bancos de dados** e **sistemas de arquivos** (como HDs e SSDs) porque minimiza as caras operações de E/S (leitura e escrita em blocos de memória secundária).
* **Balanceamento:** Todas as folhas da árvore ficam sempre no mesmo nível, garantindo uma altura reduzida.
* **Capacidade dos Nós:** Controlada por um grau mínimo $T$. Todo nó (exceto a raiz) possui entre $T-1$ e $2T-1$ chaves, e entre $T$ e $2T$ filhos.
* **Operações Rápidas:** Como a ramificação por nó é alta, a altura da árvore é muito menor que a de uma árvore binária, mantendo a complexidade de busca e atualização próxima de tempo constante.

---

## 2. Inserção Passo a Passo

Vamos simular a construção de uma **Árvore B com grau mínimo $T = 3$** (máximo de $2T - 1 = 5$ chaves por nó). Quando um nó atinge 5 chaves e uma nova precisa entrar, ele sofre uma **divisão (split)**: a chave do meio (mediana) sobe para o nó pai.

### Sequência Inicial: 10, 20, 30, 40, 50
As primeiras chaves entram ordenadas em um único nó raiz:
* **Estado da Raiz:** `[10, 20, 30, 40, 50]` (Nó cheio)

### Inserindo o 25 (Ocorre a Divisão)
O nó está com 5 chaves e não tem espaço. A árvore divide este nó subindo a chave do meio (**30**):
* O **30** vira a nova raiz.
* Os elementos menores `[10, 20]` viram o filho da esquerda.
* Os elementos maiores `[40, 50]` viram o filho da direita.

Após inserir o **25** de forma ordenada no nó correto ($25 < 30$):
```text
          [30]
         /    \
  [10, 20, 25] [40, 50]
```

---

## 3. Divisão do Nó Pai

Para fazer o nó pai (raiz) se dividir, precisamos encher a raiz com chaves vindas de baixo. Continuando com $T = 3$:

1. Inserindo **60, 70, 80**: Força a divisão do nó da direita. O **60** sobe para a raiz.
2. Inserindo **90, 100, 110**: Força outra divisão. O **90** sobe para a raiz.

A raiz agora possui três chaves: `[30, 60, 90]`.

Se continuarmos inserindo elementos até forçar mais duas divisões nos nós folhas, a raiz atingirá seu limite máximo de 5 chaves:
* **Raiz cheia:** `[30, 55, 60, 85, 90]`

### O Momento do Split da Raiz
Na próxima inserção que forçar uma chave a subir para a raiz, a raiz **não terá espaço** e se dividirá de baixo para cima:
1. A mediana da raiz (o número **60**) é empurrada para cima, criando uma **nova raiz suprema**.
2. As chaves restantes se separam em dois nós intermediários: `[30, 55]` à esquerda e `[85, 90]` à direita.

```text
                      [60]                    <-- Nova Raiz Suprema
                    /      \
              [30, 55]     [85, 90]          <-- Antiga raiz dividida em duas
             /    |   \   /    |   \
           ...   ...  ... ...  ...  ...       <-- Nós folha originais
```
A árvore cresce de baixo para cima, mantendo-se perfeitamente balanceada.

---

## 4. Remoção e a Operação de Fusão (Merge)

A remoção exige que nenhum nó fique com **menos chaves do que o mínimo permitido** ($T-1$ chaves). Para $T=3$, o mínimo é **2 chaves** (exceto a raiz). Quando um nó viola essa regra, ocorre um *underflow*.

Se os nós irmãos vizinhos também estiverem no limite mínimo e não puderem emprestar chaves, ocorre uma **fusão (merge)**.

### Exemplo Prático de Fusão
Imagine o seguinte cenário antes de remover a chave **20**:
```text
            [30, 60]
           /    |   \
     [10, 20]  [40, 50]  [70, 80]
```
O nó da esquerda `[10, 20]` e o do meio `[40, 50]` possuem exatamente 2 chaves cada. 

Se removermos a chave **20**, o nó da esquerda ficaria apenas com `[10]` (inválido). Como o vizinho `[40, 50]` também está no mínimo, fazemos o **Merge**:

1. A chave separadora do pai (**30**) desce.
2. Ela une-se com o nó deficitário `[10]` e com o irmão `[40, 50]`.
3. É gerado um novo nó unificado ordenado: `[10, 30, 40, 50]`.

### Estrutura Resultante:
```text
              [60]
             /    \
 [10, 30, 40, 50]  [70, 80]
```
Note que o pai perdeu a chave 30. Como o pai era a raiz e ficou vazio, o nó fundido intermediário não perdeu o balanceamento porque a árvore reduziu um nível de altura por completo.

---

## 5. Variações Comuns

* **Árvore B+:** Os dados reais ficam apenas nos nós-folha, e as folhas são encadeadas de forma sequencial. Isso otimiza buscas por intervalo (*range queries*) em bancos de dados relacionais.
* **Árvore B* (B Estrela):** Exige que os nós estejam pelo menos 2/3 cheios (em vez de 1/2), reduzindo ainda mais a frequência de divisões e a altura da árvore.