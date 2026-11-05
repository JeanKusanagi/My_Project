# Estrutura de Dados: Tabela Hash

Uma **tabela hash** (ou tabela de dispersão) é uma estrutura de dados eficiente que associa **chaves** de pesquisa a **valores** correspondentes. Ela utiliza uma **função hash** (ou função de espalhamento) para transformar uma chave em um índice numérico, que aponta para a posição exata de armazenamento em um vetor (array).

---

## 1. Complexidade de Tempo

O desempenho da tabela hash varia entre o caso médio e o pior caso, dependendo diretamente da eficiência da função hash e da estratégia adotada para tratar as colisões:

| Operação | Caso Médio | Pior Caso (Muitas Colisões) |
| :--- | :---: | :---: |
| **Busca** (`retrieve`) | $O(1)$ | $O(N)$ |
| **Inserção** (`insert`) | $O(1)$ | $O(N)$ |
| **Remoção** (`delete`) | $O(1)$ | $O(N)$ |

* **Caso Médio $O(1)$:** Ocorre quando a função hash distribui as chaves uniformemente pelo vetor e o fator de carga é mantido sob controle.
* **Pior Caso $O(N)$:** Ocorre se múltiplas chaves diferentes gerarem o mesmo índice (colisão), forçando a busca linear dentro de uma lista encadeada ou longas sondagens no vetor.

---

## 2. Principais Vantagens

* **Velocidade de Acesso:** Permite buscar, inserir e remover dados em tempo constante ($O(1)$) na grande maioria dos cenários computacionais.
* **Flexibilidade de Chaves:** Aceita diversos tipos de dados como chaves (como strings, números, ou objetos complexos), desde que possam ser mapeados para um valor numérico por uma função hash.
* **Eficiência em Grandes Volumes:** É ideal para gerenciar grandes conjuntos de dados associativos, sendo a base de dicionários, tabelas de símbolos de compiladores, sistemas de cache e roteamento de redes (como DNS).
* **Substituição de Buscas Lineares:** Elimina a necessidade de percorrer estruturas sequenciais inteiras ($O(N)$) para encontrar uma informação específica.

---

## 3. O Problema das Colisões

Uma **colisão** acontece quando duas ou mais chaves distintas produzem exatamente o mesmo índice através da função hash. Como o espaço de endereçamento da tabela é finito, o tratamento de colisões é obrigatório.

Existem duas abordagens principais para resolver esse problema:

### A) Encadeamento Fechado (Separado)
Nesta técnica, cada posição do vetor principal não armazena o elemento diretamente, mas sim um ponteiro para o início de outra estrutura, geralmente uma **lista encadeada**.

* **Como funciona:** Se houver colisão em um índice, o novo elemento é adicionado à lista vinculada àquela posição.
* **Vantagens:** A tabela nunca fica tecnicamente "cheia". A implementação é direta e o desempenho degrada suavemente.
* **Desvantagens:** Consome memória extra para armazenar os ponteiros da lista. Se a lista crescer demais, a busca perde a eficiência de tempo constante.

### B) Endereçamento Aberto
Nesta abordagem, **todos os elementos são armazenados diretamente no próprio vetor principal**. Quando ocorre uma colisão, o algoritmo varre o array em busca de uma posição que esteja livre.

* **Sondagem Linear (*Linear Probing*):** Se a posição `H` estiver ocupada, tenta a posição `H + 1`, `H + 2`, `H + 3`, sequencialmente. Pode gerar o problema de *agrupamento primário* (blocos de elementos ocupados que atrasam novas buscas).
* **Sondagem Quadrática (*Quadratic Probing*):** A distância de busca cresce de forma quadrática (`H + 1²`, `H + 2²`, `H + 3²`, ...), espalhando melhor os elementos colididos.
* **Duplo Hash (*Double Hashing*):** Utiliza uma segunda função hash para calcular o tamanho do "pulo" de busca. É um dos métodos mais eficientes para evitar agrupamentos.

---

## 4. Comparação entre os Tratamentos de Colisão

| Característica | Encadeamento Separado | Endereçamento Aberto |
| :--- | :--- | :--- |
| **Armazenamento** | Fora do vetor principal (listas externas) | Totalmente de forma interna no vetor |
| **Fator de Carga ($\alpha$)** | Pode ser maior que $1.0$ (mais itens que posições) | Deve ser estritamente menor que $1.0$ |
| **Desperdício de Memória** | Alocação dinâmica para ponteiros das listas | Espaço reservado e não utilizado no array |
| **Remoção de Elementos** | Simples (deleção clássica em lista encadeada) | Complexa (exige marcação lógica como *deletado*) |

---

## 5. Fator de Carga e Rehashing

O **Fator de Carga** ($\alpha$) é a razão entre o número de elementos armazenados ($n$) e o tamanho total do vetor ($m$):  
$$\alpha = \frac{n}{m}$$

Quando o fator de carga ultrapassa um limite crítico (geralmente $0.7$ ou $0.75$), a probabilidade de colisões aumenta drasticamente. Para contornar isso, a tabela realiza o **Rehashing**: o vetor é redimensionado (normalmente duplicando de tamanho) e todas as chaves existentes são remapeadas para novas posições usando o novo tamanho do vetor.

---

## 6. O Objetivo da Tabela Hash

O objetivo principal de uma tabela hash é **distribuir as chaves de maneira uniforme** por todas as posições (ou *buckets*) da estrutura física.

### Por que isso é importante?
* **Minimização de colisões:** Quando a função hash espalha os dados de forma equilibrada, reduz-se drasticamente a chance de duas chaves diferentes caírem no mesmo índice (*colisão*).
* **Eficiência nas operações:** Uma boa distribuição garante que as operações de busca, inserção e remoção mantenham um tempo médio de acesso constante ($O(1)$).
* **Evita gargalos:** Se as chaves forem concentradas em poucas posições, a tabela se comporta como uma lista lenta, anulando a vantagem de usar o mapeamento direto.

---

## 7. Funções Hash e Resolução de Colisões

Mesmo com uma excelente função hash, colisões (quando duas chaves geram o mesmo índice) ainda podem acontecer. 

### O Problema de uma Função Hash Ruim
Imagine uma tabela com **10 posições** (índices de 0 a 9). Se usarmos uma função hash ruim que pega apenas os dois últimos dígitos de um telefone e faz o resto da divisão por 10 (`chave % 10`):
* **Telefone A:** 9999-1234 $
ightarrow$ `34 % 10` = **Posição 4**
* **Telefone B:** 9888-5634 $
ightarrow$ `34 % 10` = **Posição 4** *(Colisão!)*
* **Telefone C:** 9777-0034 $
ightarrow$ `34 % 10` = **Posição 4** *(Outra colisão!)*

Todos os dados vão para a posição 4, deixando as outras vazias. Uma boa função hash misturaria os dígitos para espalhá-los.

### Métodos de Resolução de Colisões

1. **Encadeamento Externo (Chaining):** Cada posição da tabela vira o início de uma lista encadeada. Se houver colisão, o novo elemento é pendurado na lista daquela posição.
2. **Endereçamento Aberto (Open Addressing):** Todos os elementos precisam caber diretamente dentro da tabela. Se uma posição estiver ocupada, o algoritmo procura outra vaga:
   * **Sondagem Linear:** Procura sequencialmente de casa em casa (+1, +2, +3...).
   * **Sondagem Quadrática:** Procura dando saltos quadráticos (+1, +4, +9...).
   * **Duplo Hashing:** Aplica uma segunda função hash para calcular o tamanho do salto.

---

## 8. Fator de Carga (Load Factor)

O **Fator de Carga ($\alpha$)** indica o quão cheia a tabela hash está e serve como o medidor que avisa quando a estrutura precisa ser expandida.

$$\alpha = \frac{n}{m}$$

* **$n$** = Número total de elementos atualmente guardados na tabela.
* **$m$** = Número total de posições (tamanho físico da tabela).

### O "Ponto Doce" e o Rehashing
* **Fator muito alto (Perto de 1.0 ou acima):** A tabela está superlotada, as colisões disparam e o tempo de busca degrada para $O(n)$.
* **Fator muito baixo (Perto de 0.0):** Desperdício massivo de memória RAM.
* **Limites Ideais:** Para Encadeamento, tolera-se $\alpha$ entre **0.75 e 1.0**. Para Endereçamento Aberto, o limite é mais rígido, entre **0.5 e 0.7**.

Quando o limite é atingido, ocorre o **Rehashing**: a tabela dobra de tamanho e recalcula a posição de todos os elementos na nova estrutura.

---

## 9. Complexidade de Tempo e Custo Amortizado

No cenário ideal, a tabela hash opera em **$O(1)$ (Tempo Constante)** porque o acesso à memória é direto através do cálculo matemático da função hash.

### O Pior Caso: $O(n)$
No exato momento em que o Fator de Carga atinge o limite e o *Rehashing* é disparado, o computador precisa alocar o dobro de espaço e remapear todos os elementos antigos. Essa operação específica leva tempo linear $O(n)$.

### Por que ainda dizemos que é $O(1)$?
A resposta está no **Custo Amortizado**. Como a operação lenta de expansão ($O(n)$) acontece muito raramente em comparação com as milhares de inserções instantâneas ($O(1)$), quando diluímos esse custo pesado ao longo do tempo, a média por operação continua sendo virtualmente **$O(1)$ amortizado**.

---

## 10. Funções Hash Reais e Complexas

As funções do mundo real deixam de lado o resto da divisão simples e manipulam bits diretamente.

* **MurmurHash (Não Criptográfica):** Focada em performance extrema. Corta a chave em blocos de bits, multiplica por constantes mágicas, rotaciona os bits e mistura tudo (operações lógicas como `XOR`). É o padrão em linguagens como Java, Python e Ruby.
* **MD5 (Criptográfica/Integridade):** Focada em segurança e unicidade. Divide a mensagem em blocos de 512 bits, adiciona preenchimento (*padding*) e passa por 64 rodadas de funções não-lineares complexas misturadas com tabelas trigonométricas. 

---

## 11. O Efeito Avalanche

O **Efeito Avalanche** dita que uma modificação minúscula na entrada (como alterar um único bit) deve resultar em um hash completamente diferente e imprevisível.

### Exemplo Prático (MD5)
* **Texto 1:** `gato` $
ightarrow$ `ea81a2f60cf3dd49b74057864f7b4916`
* **Texto 2:** `Gato` $
ightarrow$ `83be58d40a7cf616f9f061f005f63d05`

A alteração de apenas um bit na tabela ASCII entre o 'g' e o 'G' gerou uma reação em cadeia nas rodadas matemáticas internas do algoritmo, alterando cerca de 50% dos bits do hash final. Isso garante segurança e uma distribuição uniforme perfeita em tabelas hash.

---

## 12. Ataque de Negação de Serviço por Colisão (Hash DoS)

O **Hash DoS** é um ataque em que o invasor envia poucas requisições, mas com chaves calculadas cirurgicamente para colidirem de propósito no servidor.

1. **O Cenário:** O servidor web armazena os parâmetros de um formulário ou JSON em uma tabela hash interna.
2. **A Vulnerabilidade:** Se o algoritmo de hash for previsível, o hacker envia, por exemplo, 50.000 chaves que geram o mesmo índice.
3. **O Impacto:** A tabela hash interna do servidor se deforma em uma única lista encadeada gigante. O custo de inserção salta de $O(1)$ para $O(n^2)$, jogando o uso da CPU para 100% e congelando o servidor com uma única requisição.

### Defesas Modernas
* **Randomização (Hash Seed):** As linguagens injetam um valor aleatório secreto na inicialização do servidor, tornando os hashes imprevisíveis para o hacker externo.
* **SipHash:** Substituição de algoritmos simples por funções que misturam velocidade com propriedades criptográficas fortes contra colisões provocadas.

---

## 13. Filtros de Bloom

Um **Filtro de Bloom** é uma estrutura de dados probabilística e extremamente econômica em memória que serve para responder se um elemento pertence ou não a um conjunto.

### As Duas Respostas Possíveis
* ❌ **"Definitivamente não está no conjunto":** 100% de certeza.
* ❓ **"Provavelmente está no conjunto":** Existe uma pequena chance de falso positivo.

### Funcionamento Interno
Consiste em um **vetor de bits** (inicializado com zeros) e **$k$ funções hash independentes**.
* **Inserção:** A chave passa pelas $k$ funções hash, gerando $k$ índices. O filtro vai até esses índices e muda o bit de `0` para `1`.
* **Verificação:** A chave passa pelas mesmas funções. Se pelo menos um dos índices contiver o bit `0`, o elemento **com certeza nunca foi inserido**. Se todos forem `1`, ele **provavelmente** está lá (podendo ser um falso positivo causado por sobreposição de outros elementos).
* **Limitação:** Não é possível remover elementos em um Filtro de Bloom padrão, pois apagar um bit `1` destruiria o rastro de outros dados.

### A Matemática de Dimensionamento Perfeito
Para planejar um Filtro de Bloom com $n$ elementos máximos e uma taxa de falso positivo aceitável $p$, calcula-se:

* **Tamanho do vetor de bits ($m$):**
  $$m \approx -2{,}08 \cdot n \cdot \ln(p)$$
* **Número ideal de funções hash ($k$):**
  $$k \approx 0{,}693 \cdot \frac{m}{n}$$

*Regra de bolso para erro de 1%:* Aloque **10 bits por elemento** ($m pprox 10n$) e use **7 funções hash** ($k = 7$).

### O Truque das Duas Funções Hash (Kirsch-Mitzenmacher)
Para não deixar o sistema lento calculando 7 hashes complexas do zero, desenvolvedores usam apenas duas funções base ($H_1(x)$ e $H_2(x)$) para simular infinitas funções através de aritmética simples:

$$	ext{Posição}_i(x) = (H_1(x) + i \cdot H_2(x)) \pmod m$$
$$\text{Posição}_i(x) = (H_1(x) + i \cdot H_2(x)) \bmod m$$

Dessa forma, a chave de texto só é lida e processada uma vez, e os outros índices são gerados instantaneamente por operações básicas na CPU.

