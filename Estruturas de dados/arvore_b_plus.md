# Guia Completo: Árvore B+ e Suas Operações

A **Árvore B+** é uma estrutura de dados do tipo árvore balanceada de busca, derivada da Árvore B. Ela é amplamente utilizada em **sistemas de arquivos** e **SGBDs** (Sistemas de Gerenciamento de Banco de Dados) para indexação de dados em memória secundária (disco).

---

## 1. Principais Características

* **Separação de Índices e Dados:** 
  * Os **nós internos** (raiz e intermediários) armazenam apenas **chaves e ponteiros** para guiar a navegação, sem guardar os registros de dados completos.
  * Os **nós folha** armazenam todas as chaves do arquivo junto com os dados reais ou ponteiros diretos para eles.
* **Lista Encadeada nas Folhas:** 
  * Todas as páginas folha são interligadas horizontalmente em formato de lista encadeada. 
  * Isso torna as buscas sequenciais e consultas por intervalo extremamente rápidas.
* **Menos I/O de Disco:** 
  * Como os nós internos guardam apenas chaves, cabe uma quantidade muito maior de caminhos em uma única página de disco. A árvore fica "mais curta" (com menos níveis), reduzindo o número de leituras em memória secundária (HD/SSD).

---

## 2. Operações Básicas

* **Busca:** Começa na raiz e utiliza as chaves dos nós internos para descer até a folha correta. Se for uma busca por intervalo, a árvore encontra o primeiro elemento na folha e percorre a lista encadeada horizontalmente.
* **Inserção:** O novo elemento é inserido na página folha correspondente de forma ordenada. Se a folha atingir a capacidade máxima (*overflow*), ela é dividida (*split*) e uma chave é promovida para o nível superior.
* **Remoção:** O item é removido da folha. Se o nó ficar abaixo da ocupação mínima (*underflow*), faz-se a redistribuição de chaves com nós vizinhos (empréstimo) ou a concatenação (fusão) de nós.

---

## 3. Exemplo Numérico de Inserção e Split

Para ilustrar a inserção e a operação de **split (divisão de nós)**, vamos construir uma árvore passo a passo utilizando uma ordem pequena.

### Regras do Exemplo:
* **Ordem da árvore ($M$) = 3**: Cada nó interno pode ter no máximo **3 ponteiros de filhos** e no máximo **2 chaves**.
* **Capacidade máxima das folhas ($L$) = 2**: Cada nó folha pode armazenar no máximo **2 chaves**. Se uma folha receber a 3ª chave, ocorre o *split*.
* **Sequência de inserção**: `10`, `20`, `5`, `15`, `25`

### Passo a Passo:

#### Passo 3.1: Inserir `10` e `20`
As primeiras chaves entram diretamente na raiz (que começa como um nó folha). Os elementos são guardados de forma ordenada.
```text
[ 10 | 20 ] (Nó Folha / Raiz)
```

#### Passo 3.2: Inserir `5` (Overflow e Split)
A chave `5` deveria entrar na folha `[ 10 | 20 ]`, ordenando-se como `[ 5 | 10 | 20 ]`. No entanto, a capacidade máxima da folha é de 2 chaves. Ocorre o **Split da Folha**:
1. O nó folha é dividido ao meio.
2. Os elementos menores ficam na folha da esquerda: `[ 5 ]`.
3. Os elementos maiores (incluindo o do meio) ficam na folha da direita: `[ 10 | 20 ]`.
4. Uma **cópia** da primeira chave da folha direita (`10`) é **promovida** para criar o novo nó raiz (índice).
5. As duas folhas são interligadas por um ponteiro sequencial.

```text
       Raiz (Índice):           [ 10 ]
                             /          \
Folhas (Dados):          [ 5 ]  ------> [ 10 | 20 ]
```

#### Passo 3.3: Inserir `15`
A busca começa na raiz. Como $15 \ge 10$, seguimos para a folha da direita. A inserção ordenada em `[ 10 | 20 ]` geraria `[ 10 | 15 | 20 ]`, causando um novo **Split da Folha**:
* O elemento do meio é o **15**.
* Esquerda: `[ 10 ]`
* Direita: `[ 15 | 20 ]`
* A chave **15** é **promovida** para a raiz, que tem espaço livre.

```text
       Raiz (Índice):          [ 10 | 15 ]
                             /      |      \
Folhas (Dados):          [ 5 ] --> [ 10 ] --> [ 15 | 20 ]
```

#### Passo 3.4: Inserir `25` (Split em Cascata / Novo Nível)
A busca determina que o 25 deve entrar na folha `[ 15 | 20 ]`, resultando em `[ 15 | 20 | 25 ]` (*Overflow*).
1. **Split da Folha**: Esquerda `[ 15 ]`, Direita `[ 20 | 25 ]`. O `20` é promovido para o nó pai.
2. **Split de Nó Interno (Raiz Cheia)**: A raiz receberia o `20`, tornando-se `[ 10 | 15 | 20 ]`. Como o limite de chaves internas é 2, o nó interno é dividido. O elemento do meio (`15`) sobe para virar a **nova raiz isolada** (sem duplicar na raiz). Os outros viram nós internos intermediários.

```text
          Nova Raiz:                   [ 15 ]
                                    /          \
          Nós Internos:          [ 10 ]        [ 20 ]
                                /    \        /    \
          Folhas (Dados):    [ 5 ] -> [ 10 ] -> [ 15 ] -> [ 20 | 25 ]
```

---

## 4. Remoção com Sob Fluxo (Underflow)

O **underflow** ocorre quando um nó fica abaixo da sua ocupação mínima permitida (geralmente metade da capacidade máxima). Para $L=2$, o mínimo é **1 chave por folha**.

### Cenário 4.1: Remoção Simples (Sem Underflow)
Removendo a chave **`25`** da folha `[ 20 | 25 ]`:
* O `25` é apagado. A folha passa a ser apenas `[ 20 ]`. Como ela ainda respeita o limite mínimo de 1 chave, nenhuma reestruturação é necessária.

### Cenário 4.2: Remoção com Underflow e Fusão (Merge)
Removendo a chave **`20`** da folha `[ 20 ]`:
1. Ao apagar o `20`, a folha fica vazia `[ ]` (**Underflow**).
2. **Tentativa de Empréstimo:** O irmão à esquerda `[ 15 ]` tem apenas 1 chave e não pode emprestar.
3. **Fusão (Merge) de Folhas:** A folha vazia e a folha `[ 15 ]` se fundem em um único nó `[ 15 ]`.
4. **Propagação do Underflow:** O nó interno pai `[ 20 ]` perdeu um filho e fica com 0 chaves. Ele tenta pegar emprestado do irmão esquerdo `[ 10 ]`, que também está no mínimo.
5. **Fusão de Nós Internos e Encolhimento:** Os nós internos se fundem trazendo a chave da raiz (`15`) para baixo. A árvore diminui de altura e o nó composto passa a ser a nova raiz.

```text
          Nova Raiz (Índice):          [ 10 | 15 ]
                                     /      |      \
          Folhas (Dados):        [ 5 ] --> [ 10 ] --> [ 15 ]
```

---

## 5. Diferença Prática: Árvore B vs. Árvore B+

| Característica | Árvore B | Árvore B+ |
| :--- | :--- | :--- |
| **Onde os dados ficam?** | Espalhados por **todos os nós** (raiz, internos e folhas). | **Apenas nos nós folha**. Os nós superiores são apenas índices. |
| **Busca por chave exata** | Pode terminar antes, caso o dado seja encontrado na raiz ou em nós internos. | Sempre vai até o **último nível** (nó folha) para encontrar o dado. |
| **Consultas por intervalo / paginação**| **Muito lenta**. Exige subir e descer a árvore repetigens estruturais (percurso em ordem). | **Ultra rápida**. Basta achar o primeiro elemento e seguir a lista encadeada horizontal. |
| **Espaço nos nós internos** | Menor. Como guarda dados no nó, cabem poucas chaves por página de disco. | Maior. Sem dados atrapalhando, cabem milhares de chaves por página de disco. |
| **Altura da árvore (Níveis)** | Geralmente **mais alta**, gerando mais operações de leitura em disco (I/O). | Geralmente **mais baixa (larga)**, reduzindo drasticamente o acesso ao disco. |

---

## 6. Onde é Utilizada

* **Sistemas de Arquivos:** NTFS, ReiserFS, XFS, JFS2.
* **Bancos de Dados:** PostgreSQL, Oracle, Microsoft SQL Server, MySQL (InnoDB), SQLite, IBM DB2.

---

---

## 📌 Propriedades Fundamentais

* **Ordem (m):** Define o número máximo de ponteiros (filhos) que um nó pode ter.
* **Capacidade dos Nós:**
  * **Nós Internos:** Podem conter no máximo $m-1$ chaves e devem conter pelo menos $\lceil m/2 \rceil - 1$ chaves.
  * **Nós Folha:** Armazenam os dados reais (ou ponteiros para os registros) e também seguem a regra de preenchimento mínimo de $\lceil m/2 \rceil - 1$ chaves.
* **Separação de Conteúdo:** Os nós internos servem estritamente como *índices de navegação*. Os dados reais residem **apenas** nas folhas.
* **Encadeamento:** Todos os nós folha são interconectados por uma lista encadeada, otimizando buscas por intervalos (*range queries*).

---

## 📥 Algoritmo de Inserção

Toda inserção começa obrigatoriamente em um nó folha. O balanceamento é mantido de baixo para cima através de divisões de nós (*splits*).

### Passo a Passo:
1. **Busca:** Navega a partir da raiz até encontrar a folha correta onde a chave deve ser guardada.
2. **Inserção Direta:** Se a folha tiver espaço disponível (número de chaves $< m-1$), insere a chave mantendo a ordenação.
3. **Divisão da Folha (Split):** Se a folha estiver cheia (atingiu $m$ chaves):
   * O nó é dividido em duas folhas distintas.
   * As chaves menores permanecem na folha original; as chaves maiores vão para a nova folha.
   * **Regra B+:** A menor chave da nova folha (o elemento do meio) é **copiada** para o nó pai.
4. **Propagação nos Nós Internos:** Se o nó pai também estiver cheio ao receber a nova chave de índice:
   * O nó interno é dividido em dois.
   * **Regra B+:** O elemento do meio é **movido** (e não copiado) para o pai de nível superior.
   * Se a raiz original for dividida, cria-se uma nova raiz com uma única chave, aumentando a altura da árvore em 1 nível.

---

## 📤 Algoritmo de Remoção

A remoção remove uma chave de um nó folha e trata as violações de preenchimento mínimo (sub-preenchimento ou *underflow*) de baixo para cima.

### Passo a Passo:
1. **Busca:** Localiza o nó folha que contém a chave a ser removida.
2. **Remoção Direta:** Remove a chave do nó folha. Se o nó continuar com o número mínimo exigido de chaves ($\ge \lceil m/2 \rceil - 1$), a operação encerra.
3. **Tratamento de Sub-preenchimento:** Se o nó ficar com menos chaves do que o permitido:
   * **Caso 1: Empréstimo (Redistribuição):** Se um nó irmão adjacente (esquerdo ou direito) tiver chaves além do mínimo necessário:
     * O nó atual pega uma chave emprestada desse irmão.
     * A chave correspondente no nó pai é **atualizada** para refletir o novo menor elemento do nó à direita.
   * **Caso 2: Fusão (Merge):** Se nenhum dos irmãos adjacentes tiver chaves sobressalentes:
     * O nó atual é **fundido** com seu irmão.
     * Como os dados combinados agora cabem em um único nó, a chave separadora no nó pai torna-se redundante e é **removida**.
4. **Propagação da Fusão:** A remoção de uma chave no nó pai pode desencadear um sub-preenchimento nele mesmo. O processo de empréstimo ou fusão repete-se subindo os níveis da árvore. Se a raiz perder sua última chave, ela é eliminada e o nó filho fundido assume como a nova raiz, reduzindo a altura da árvore.

---

## 📊 Comparativo das Operações

| Operação | Caso Ideal | Caso de Estouro de Limite | Efeito na Altura |
| :--- | :--- | :--- | :--- |
| **Inserção** | Espaço livre na folha. | Divisão (*Split*) do nó folha / interno. | Pode **aumentar** a altura pela raiz. |
| **Remoção** | Nó mantém preenchimento mínimo. | Empréstimo ou Fusão (*Merge*) de nós. | Pode **diminuir** a altura se a raiz sumir. |
