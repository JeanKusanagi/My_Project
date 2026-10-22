# Estrutura de Dados: Pilha (Stack)

No contexto da Ciência da Computação, uma **pilha (ou *stack*) é uma estrutura de dados linear que segue o princípio LIFO (*Last In, First Out*)**. Isso significa que o **último elemento inserido é obrigatoriamente o primeiro a ser removido**. Todas as inserções e remoções são feitas exclusivamente por uma única extremidade chamada de **topo**.

---

## ⚙️ Operações Principais e Complexidade

Uma das maiores vantagens da pilha é a sua previsibilidade e eficiência. Quando implementada corretamente (seja por meio de arrays ou listas encadeadas), as operações fundamentais possuem **complexidade de tempo constante, ou seja, O(1)**, pois não exigem a varredura da estrutura.

| Operação | Descrição | Complexidade de Tempo | Complexidade de Espaço |
| :--- | :--- | :---: | :---: |
| **`Push`** | Insere um novo elemento no topo da pilha. | O(1) | O(1) |
| **`Pop`** | Remove e retorna o elemento que está no topo. | O(1) | O(1) |
| **`Peek` / `Top`** | Apenas visualiza o elemento do topo sem removê-lo. | O(1) | O(1) |
| **`IsEmpty`** | Verifica se a pilha está vazia. | O(1) | O(1) |

> **Nota:** A complexidade de espaço global da estrutura completa é **O(n)**, onde *n* é o número total de elementos armazenados.

---

## 👍 Vantagens da Pilha

*   **Eficiência de Desempenho:** Como as inserções e remoções acontecem apenas no topo, as operações de tempo O(1) garantem que a estrutura seja extremamente rápida, ideal para sistemas de alta performance.
*   **Gerenciamento de Memória Simplificado:** A memória é tratada de forma linear e direta. Não há necessidade de reorganizar ou deslocar os outros elementos quando um item é adicionado ou removido (diferente de um vetor tradicional).
*   **Controle de Fluxo Natural:** É a estrutura perfeita para rastrear estados anteriores. Ela permite reverter ações facilmente, pois mantém o histórico ordenado do mais recente para o mais antigo.
*   **Segurança e Restrição de Acesso:** Ao impedir o acesso aleatório aos elementos do meio ou do fundo, ela protege a integridade dos dados para algoritmos que dependem estritamente da ordem de execução.

---

## 💻 Aplicações Práticas no Mundo Real

*   **Mecanismos de Desfazer/Refazer (`Ctrl + Z`):** Armazena as últimas ações do usuário no topo para permitir a reversão imediata.
*   **Navegação na Web:** O botão "Voltar" do navegador utiliza uma pilha para registrar o histórico de páginas visitadas.
*   **Funções de Chamada (Call Stack):** O sistema operacional e os compiladores utilizam uma pilha de execução para gerenciar chamadas de funções e escopos de variáveis locais.
*   **Validação de Sintaxe:** Utilizada para verificar o fechamento correto de parênteses, colchetes e chaves em códigos-fonte.

---

## 🔬 Diferença Prática: Array vs. Lista Encadeada

Embora ambas as abordagens garantam a complexidade teórica de **O(1)** para as operações no topo, o comportamento no hardware varia conforme a alocação de memória.

### Tabela Comparativa

| Critério | Pilha com Array 📦 | Pilha com Lista Encadeada 🔗 |
| :--- | :--- | :--- |
| **Alocação de Memória** | **Contígua** (elementos ficam grudados, lado a lado na memória RAM). | **Dispersa** (elementos ficam espalhados em qualquer espaço vago da RAM). |
| **Tamanho da Pilha** | **Fixo ou Redimensionável** (pode encher e causar *Stack Overflow* ou exigir cópias). | **Dinâmico** (cresce indefinidamente enquanto houver memória livre). |
| **Gasto de Memória por Item**| **Menor** (guarda apenas o valor puro do dado). | **Maior** (cada nó precisa guardar o dado + um ponteiro com o endereço do próximo). |
| **Uso do Cache da CPU** | **Excelente** (alta localidade de referência, acelerando o processamento). | **Ruim** (causa muitos *cache misses*, pois a CPU precisa "pular" para endereços distantes). |
| **Custo de Inserção (`Push`)**| Geralmente instantâneo, mas **sofre gargalos esporádicos** se o array precisar dobrar. | **Sempre constante**, mas exige a criação dinâmica de um novo objeto/nó na RAM. |

---

### 1. Na Prática com Arrays: Velocidade Bruta e Limitações

Quando você cria uma pilha usando um Array, o computador reserva um **bloco inteiriço de memória**. 

*   **A Vantagem Oculta (Cache da CPU):** CPUs modernas não leem a memória RAM byte por byte; elas puxam blocos vizinhos inteiros para uma memória interna ultra-rápida chamada *Cache*. Como os elementos do array estão colados, quando a CPU busca o topo da pilha, ela traz os elementos anteriores juntos de forma otimizada.
*   **O Problema do Redimensionamento:** Se a sua pilha crescer além do tamanho inicial alocado, o sistema precisa criar um novo array maior, **copiar todos os elementos antigos** para ele e apagar o anterior. Esse processo é pesado e quebra temporariamente o tempo constante estrito O(1) naquele instante específico.

### 2. Na Prática com Listas Encadeadas: Flexibilidade Total e Overhead

Com listas encadeadas, cada elemento inserido na pilha vira um bloco isolado chamado **Nó**.

*   **A Vantagem do Tamanho Infinito:** Você nunca precisa se preocupar em prever o tamanho máximo da pilha. Se o usuário empilhar 1 ou 1.000.000 de itens, a estrutura simplesmente aloca nós dinamicamente e os conecta através de ponteiros.
*   **O Preço dos Ponteiros:** Se você tem uma pilha de números inteiros (4 bytes cada), uma lista encadeada precisará gastar cerca de 8 bytes adicionais em sistemas de 64 bits apenas para armazenar o ponteiro do próximo nó. Isso triplica o consumo de memória por item, além de degradar a performance do cache pela dispersão física na RAM.

---

## 🎯 Resumo de Decisão: Qual escolher?

*   **Escolha Array se:** Você conhece o limite máximo de dados que serão empilhados (ou tem uma boa estimativa) e a **performance e velocidade de execução** são prioridades absolutas (ex: engines de jogos, sistemas embarcados).
*   **Escolha Lista Encadeada se:** A quantidade de dados é **completamente imprevisível**, os dados crescem e diminuem drasticamente de tamanho, e você não pode tolerar pequenas variações de latência (*stuttering*) causadas por redimensionamento em tempo de execução.
