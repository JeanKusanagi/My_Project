# SIMULADO — Métodos Numéricos para Resolução de Sistemas Lineares
### Métodos diretos (Eliminação de Gauss, decomposição LU, pivoteamento) e métodos iterativos (Jacobi, Gauss-Seidel, convergência)

**Instruções:** Cada questão possui 4 ou 5 alternativas, das quais apenas uma é correta. O gabarito comentado aparece imediatamente após cada questão. Leia com atenção — várias questões contêm pegadinhas clássicas de cálculo numérico.

---

**1.** Métodos **diretos** para resolução de sistemas lineares são caracterizados por:

a) Produzir, em aritmética exata (sem erros de arredondamento), a solução exata do sistema em um número finito e predeterminado de operações<br>
b) Gerar uma sequência de aproximações que converge para a solução, sem nunca alcançá-la exatamente<br>
c) Serem aplicáveis apenas a sistemas com matriz singular<br>
d) Exigirem sempre um chute inicial para a solução

> **Gabarito: a.** Métodos diretos (como Eliminação de Gauss e decomposição LU) chegam à solução exata em um número finito e conhecido de passos, em aritmética exata — diferente dos métodos iterativos, que geram aproximações sucessivas.

---

**2.** Métodos **iterativos** para resolução de sistemas lineares são caracterizados por:

a) Fornecerem sempre a solução exata em um número fixo de operações<br>
b) Partirem de uma aproximação inicial e gerarem, a cada iteração, uma nova aproximação, que idealmente converge para a solução do sistema<br>
c) Não poderem ser aplicados a sistemas grandes e esparsos<br>
d) Serem sempre mais rápidos que métodos diretos, independentemente do tamanho do sistema

> **Gabarito: b.** Métodos iterativos (como Jacobi e Gauss-Seidel) constroem uma sequência de aproximações a partir de um ponto inicial, sendo particularmente úteis para sistemas grandes e esparsos, onde métodos diretos podem ser computacionalmente caros.

---

**3.** O método de **Eliminação de Gauss** consiste em:

a) Transformar o sistema original em um sistema triangular equivalente, por meio de operações elementares sobre as linhas, seguido de substituição retroativa (back substitution)<br>
b) Gerar aproximações sucessivas a partir de um chute inicial<br>
c) Calcular diretamente a inversa da matriz de coeficientes<br>
d) Aplicar exclusivamente a sistemas 2x2

> **Gabarito: a.** A Eliminação de Gauss usa operações elementares (combinações lineares de linhas) para zerar os elementos abaixo da diagonal principal, chegando a um sistema triangular superior, resolvido depois por substituição retroativa.

---

**4.** **(Pegadinha)** Sobre a complexidade computacional da Eliminação de Gauss em um sistema de ordem *n*, é correto afirmar que:

a) O número de operações cresce linearmente com n, sendo O(n)<br>
b) O número de operações cresce aproximadamente com a ordem O(n³), tornando o método custoso para sistemas muito grandes<br>
c) O número de operações é constante, independentemente de n<br>
d) O número de operações decresce à medida que n aumenta

> **Gabarito: b.** Pegadinha: é comum subestimar o custo — a Eliminação de Gauss tem complexidade cúbica, O(n³), o que a torna proibitiva para sistemas muito grandes, motivando o uso de métodos iterativos ou de matrizes esparsas nesses casos.

---

**5.** O que é **pivoteamento parcial** na Eliminação de Gauss?

a) A troca de linhas do sistema para colocar, na posição do pivô, o elemento de maior valor absoluto disponível naquela coluna, entre as linhas ainda não processadas<br>
b) O processo de eliminar completamente a última linha da matriz<br>
c) A substituição de todos os elementos da matriz por zero<br>
d) Um método usado apenas quando o sistema não tem solução

> **Gabarito: a.** O pivoteamento parcial busca, a cada etapa, o maior elemento em módulo na coluna (entre as linhas restantes) para usá-lo como pivô, reduzindo erros de arredondamento e evitando divisões por valores muito pequenos ou por zero.

---

**6.** **(Pegadinha)** Qual é o principal motivo para se utilizar pivoteamento na Eliminação de Gauss, mesmo quando o pivô original não é exatamente zero?

a) Pivoteamento só é necessário quando o pivô é exatamente igual a zero; caso contrário, é irrelevante do ponto de vista numérico<br>
b) Mesmo com um pivô pequeno, mas não nulo, a divisão por esse valor pode amplificar significativamente os erros de arredondamento já presentes nos cálculos, comprometendo a precisão da solução — por isso, pivôs pequenos (não apenas nulos) também motivam o pivoteamento<br>
c) Pivoteamento é usado apenas por razões estéticas, sem impacto na precisão numérica<br>
d) Pivoteamento torna o método mais lento sem qualquer benefício de precisão

> **Gabarito: b.** Pegadinha: a necessidade de pivoteamento não se limita a evitar divisão por exatamente zero — pivôs pequenos, mesmo não nulos, já são numericamente perigosos, pois amplificam erros de arredondamento na aritmética de ponto flutuante.

---

**7.** A **decomposição LU** consiste em escrever uma matriz A como o produto:

a) A = L + U, sendo L e U matrizes triangulares<br>
b) A = L · U, sendo L uma matriz triangular inferior e U uma matriz triangular superior<br>
c) A = L / U, uma divisão elemento a elemento<br>
d) A = L · U⁻¹

> **Gabarito: b.** A decomposição LU fatora a matriz A no produto de uma triangular inferior (L) por uma triangular superior (U), essencialmente registrando os multiplicadores usados durante a eliminação de Gauss.

---

**8.** **(Pegadinha)** Qual é a principal vantagem prática da decomposição LU em relação a repetir a Eliminação de Gauss do zero, quando é preciso resolver o sistema Ax = b para **vários vetores b diferentes**, mantendo a mesma matriz A?

a) Não há vantagem alguma, pois o custo é idêntico em qualquer abordagem<br>
b) Uma vez obtida a fatoração A = LU (feita apenas uma vez, com custo O(n³)), cada novo sistema com um b diferente pode ser resolvido resolvendo dois sistemas triangulares (Ly = b e Ux = y), com custo muito menor, O(n²), evitando refazer toda a eliminação para cada b<br>
c) A decomposição LU só pode ser usada uma única vez e depois deve ser descartada<br>
d) A decomposição LU elimina a necessidade de qualquer pivoteamento em qualquer sistema

> **Gabarito: b.** Pegadinha: o ganho de eficiência da LU está justamente em reaproveitar a fatoração (feita uma única vez) para resolver múltiplos sistemas com a mesma matriz A, mas vetores b diferentes, a um custo bem menor por sistema adicional.

---

**9.** Uma matriz A é dita **singular** quando:

a) Seu determinante é diferente de zero<br>
b) Seu determinante é igual a zero, o que implica que o sistema Ax = b pode não ter solução única (pode não ter solução ou ter infinitas soluções)<br>
c) Ela é sempre simétrica<br>
d) Ela é sempre diagonal

> **Gabarito: b.** Determinante nulo é a condição clássica de singularidade — nesse caso, a matriz não é invertível, e o sistema associado não possui solução única.

---

**10.** **(Pegadinha)** Um sistema linear é dito **mal condicionado** (ill-conditioned) quando:

a) Sua matriz de coeficientes é sempre singular (determinante exatamente zero)<br>
b) Pequenas perturbações nos dados de entrada (coeficientes ou termos independentes) podem causar variações desproporcionalmente grandes na solução, mesmo que a matriz não seja singular — geralmente associado a um número de condição elevado<br>
c) O sistema tem, obrigatoriamente, mais equações do que incógnitas<br>
d) O sistema não pode ser resolvido por nenhum método numérico

> **Gabarito: b.** Pegadinha: mal condicionamento não é sinônimo de singularidade — uma matriz pode ser invertível (não singular), mas ainda assim mal condicionada, sendo extremamente sensível a pequenos erros nos dados ou de arredondamento.

---

**11.** O **número de condição** de uma matriz é uma medida que:

a) Indica exclusivamente o tamanho (ordem) da matriz<br>
b) Quantifica o quanto o sistema é sensível a perturbações nos dados de entrada; quanto maior o número de condição, mais mal condicionado tende a ser o sistema<br>
c) É sempre igual a 1 para qualquer matriz<br>
d) Só pode ser calculado para matrizes triangulares

> **Gabarito: b.** O número de condição relaciona a sensibilidade da solução a perturbações nos dados — valores próximos de 1 indicam sistemas bem condicionados, enquanto valores muito altos indicam sistemas mal condicionados.

---

**12.** No **método de Jacobi**, o cálculo de cada componente da nova aproximação x⁽ᵏ⁺¹⁾ é feito:

a) Utilizando os valores já atualizados de x⁽ᵏ⁺¹⁾ das componentes anteriores, dentro da mesma iteração<br>
b) Utilizando exclusivamente os valores da iteração anterior completa, x⁽ᵏ⁾, para todas as componentes, sem usar nenhum valor já atualizado na iteração corrente<br>
c) Resolvendo diretamente o sistema por eliminação de Gauss a cada iteração<br>
d) Sem qualquer relação com a matriz de coeficientes original

> **Gabarito: b.** No método de Jacobi, todas as componentes da nova aproximação são calculadas usando apenas os valores da iteração anterior (x⁽ᵏ⁾) — as atualizações "simultâneas" só passam a valer, de fato, na iteração seguinte.

---

**13.** **(Pegadinha)** A principal diferença entre o método de **Jacobi** e o método de **Gauss-Seidel** está em:

a) Gauss-Seidel não é um método iterativo, apenas Jacobi é<br>
b) O método de Gauss-Seidel utiliza, no cálculo de cada componente da nova aproximação, os valores já atualizados das componentes anteriores **dentro da mesma iteração**, em vez de esperar a iteração completa terminar (como faz Jacobi) — isso tende a acelerar a convergência<br>
c) Jacobi sempre converge mais rápido que Gauss-Seidel, em qualquer sistema<br>
d) Não há diferença relevante entre os dois métodos; são essencialmente idênticos

> **Gabarito: b.** Pegadinha: é o contrário do que muitos assumem — Gauss-Seidel geralmente converge mais rápido que Jacobi (quando ambos convergem), justamente por reaproveitar valores já atualizados dentro da própria iteração.

---

**14.** **(Pegadinha)** Um critério **suficiente** (mas não necessário) para garantir a convergência dos métodos de Jacobi e Gauss-Seidel é que a matriz de coeficientes seja:

a) Simétrica, sempre e exclusivamente<br>
b) Diagonalmente dominante (em módulo, o valor absoluto de cada elemento da diagonal principal é maior ou igual à soma dos valores absolutos dos demais elementos da mesma linha, com desigualdade estrita em pelo menos uma linha)<br>
c) Uma matriz identidade<br>
d) Triangular superior

> **Gabarito: b.** Pegadinha: dominância diagonal é uma condição **suficiente**, não necessária — existem sistemas que convergem mesmo sem diagonal estritamente dominante, mas quando essa condição é satisfeita, a convergência de Jacobi e Gauss-Seidel fica garantida.

---

**15.** **(Pegadinha)** Um estudante afirma: "Se a matriz não é diagonalmente dominante, os métodos de Jacobi e Gauss-Seidel certamente não convergem." Essa afirmação está:

a) Correta, pois dominância diagonal é condição necessária e suficiente para convergência<br>
b) Incorreta — a ausência de dominância diagonal não implica necessariamente divergência; ela apenas significa que essa condição suficiente específica não está satisfeita, mas o método ainda pode convergir dependendo de outras propriedades da matriz (como o raio espectral da matriz de iteração)<br>
c) Correta apenas para o método de Jacobi, mas não para Gauss-Seidel<br>
d) Incorreta, mas apenas porque dominância diagonal nunca é relevante para convergência

> **Gabarito: b.** Pegadinha: confundir condição suficiente com condição necessária é um erro clássico — a real condição necessária e suficiente para convergência dos métodos iterativos lineares é que o **raio espectral** da matriz de iteração seja menor que 1.

---

**16.** O **raio espectral** de uma matriz de iteração é definido como:

a) A soma de todos os elementos da matriz<br>
b) O maior valor absoluto entre os autovalores (eigenvalues) da matriz<br>
c) O determinante da matriz<br>
d) O traço (soma dos elementos da diagonal) da matriz

> **Gabarito: b.** O raio espectral (ρ) é o maior módulo entre os autovalores da matriz — e é a condição necessária e suficiente para a convergência de métodos iterativos lineares estacionários: ρ < 1 garante convergência.

---

**17.** **(Pegadinha)** Para que um método iterativo estacionário (como Jacobi ou Gauss-Seidel) convirja para a solução do sistema, independentemente do vetor inicial escolhido, é necessário e suficiente que:

a) O determinante da matriz de coeficientes seja positivo<br>
b) O raio espectral da matriz de iteração associada ao método seja estritamente menor que 1<br>
c) A matriz de coeficientes seja simétrica<br>
d) O sistema tenha um número par de equações

> **Gabarito: b.** Esse é o critério teórico fundamental (necessário e suficiente) de convergência para métodos iterativos lineares estacionários — as demais alternativas descrevem condições apenas suficientes (em certos casos) ou irrelevantes para a convergência.

---

**18.** Um **critério de parada** comum em métodos iterativos para sistemas lineares é:

a) Parar exatamente após uma única iteração, sempre<br>
b) Parar quando a diferença (em alguma norma) entre duas aproximações sucessivas, ||x⁽ᵏ⁺¹⁾ − x⁽ᵏ⁾||, for menor que uma tolerância pré-estabelecida, ou quando um número máximo de iterações for atingido<br>
c) Parar apenas quando o determinante da matriz se tornar zero<br>
d) Parar quando a matriz deixar de ser diagonalmente dominante

> **Gabarito: b.** É prática padrão combinar um critério de tolerância (erro relativo/absoluto entre iterações sucessivas) com um limite máximo de iterações, para evitar loops infinitos em casos de convergência lenta ou ausência de convergência.

---

**19.** **(Pegadinha)** Sobre o número de operações necessárias em métodos iterativos versus métodos diretos para sistemas **grandes e esparsos** (com muitos elementos nulos), é correto afirmar que:

a) Métodos diretos são sempre preferíveis, pois têm menor custo computacional em qualquer cenário<br>
b) Métodos iterativos podem ser mais vantajosos nesse cenário, pois conseguem explorar a esparsidade da matriz (evitando operar sobre elementos nulos) e, muitas vezes, atingem uma aproximação suficientemente boa com poucas iterações, enquanto métodos diretos como a Eliminação de Gauss podem preencher ("fill-in") posições originalmente nulas, aumentando o custo de memória e processamento<br>
c) Métodos iterativos nunca podem ser usados em sistemas esparsos<br>
d) Não há diferença prática entre os dois tipos de métodos nesse cenário

> **Gabarito: b.** Pegadinha: para sistemas grandes e esparsos, a Eliminação de Gauss pode gerar "fill-in" (preenchimento de posições antes nulas), aumentando custo de memória e tempo — por isso, métodos iterativos costumam ser preferidos nesses casos, especialmente quando conseguem convergir rapidamente.

---

**20.** No método de Gauss-Seidel, se a matriz de coeficientes for simétrica e definida positiva, é correto afirmar que:

a) O método nunca converge<br>
b) O método converge, independentemente do vetor inicial escolhido — esse é outro resultado teórico clássico de garantia de convergência<br>
c) O método converge apenas se a matriz também for diagonal<br>
d) A convergência depende exclusivamente do tamanho do sistema, não das propriedades da matriz

> **Gabarito: b.** Além da dominância diagonal, matriz simétrica e definida positiva é outra condição suficiente clássica que garante a convergência do método de Gauss-Seidel, independentemente do ponto de partida.

---

**21.** **(Pegadinha)** Na Eliminação de Gauss, ao realizar a substituição retroativa (back substitution) após obter o sistema triangular superior, a ordem correta de resolução das incógnitas é:

a) Da primeira equação (topo) para a última (base), resolvendo x₁ primeiro<br>
b) Da última equação (base) para a primeira (topo), resolvendo primeiro a última incógnita, pois a última equação do sistema triangular superior já envolve apenas uma incógnita isolada<br>
c) Em ordem aleatória, sem importância para o resultado final<br>
d) Simultaneamente, todas as incógnitas ao mesmo tempo, sem qualquer ordem

> **Gabarito: b.** Pegadinha: é comum inverter a lógica — no sistema triangular **superior**, a última linha já contém apenas uma incógnita isolada, por isso a substituição começa "de baixo para cima".

---

**22.** **(Pegadinha)** Considere um sistema Ax = b em que a matriz A é triangular **inferior**. Nesse caso, a forma mais direta e natural de resolver o sistema (sem necessidade de eliminação prévia) é por:

a) Substituição retroativa, começando pela última equação<br>
b) Substituição progressiva (forward substitution), começando pela primeira equação, que já envolve apenas uma incógnita isolada, e avançando sucessivamente<br>
c) Decomposição LU, obrigatoriamente<br>
d) Não é possível resolver diretamente sistemas triangulares inferiores

> **Gabarito: b.** Pegadinha (espelhada em relação à questão anterior): sistemas triangulares **inferiores** são resolvidos "de cima para baixo" (substituição progressiva/forward substitution), pois é a primeira equação que já contém apenas uma incógnita isolada — o oposto do caso triangular superior.

---

**23.** Ao aplicar a Eliminação de Gauss, se, durante o processo, surgir uma linha inteiramente composta por zeros (incluindo o termo independente) abaixo da diagonal, isso indica que o sistema:

a) Tem, necessariamente, solução única<br>
b) É provavelmente indeterminado (possui infinitas soluções), pois essa linha representa uma equação redundante (combinação linear das demais)<br>
c) Não pode ser resolvido por nenhum método<br>
d) Deve ser descartado sem qualquer análise adicional

> **Gabarito: b.** Uma linha nula (0 = 0) durante a eliminação indica dependência linear entre as equações, sinalizando um sistema indeterminado (infinitas soluções), desde que não haja inconsistência em outra linha.

---

**24.** **(Pegadinha)** Se, durante a Eliminação de Gauss, surgir uma linha do tipo "0 = c", sendo c um número diferente de zero, isso indica que o sistema:

a) É indeterminado, com infinitas soluções<br>
b) É impossível (inconsistente), ou seja, não possui nenhuma solução, pois essa linha representa uma contradição matemática (0 nunca pode ser igual a um número diferente de zero)<br>
c) Tem solução única, apesar da aparência estranha<br>
d) Deve ser resolvido ignorando essa linha específica

> **Gabarito: b.** Pegadinha: diferente da linha "0 = 0" (questão anterior, que indica sistema indeterminado), a linha "0 = c" com c ≠ 0 revela uma contradição — o sistema é impossível, sem qualquer solução.

---

**25.** O método de **Gauss-Jordan** se diferencia da Eliminação de Gauss tradicional por:

a) Não usar nenhuma operação elementar sobre linhas<br>
b) Continuar as operações de eliminação até obter uma matriz totalmente diagonal (ou identidade, se normalizada), eliminando também os elementos **acima** da diagonal principal, e não apenas os de baixo — dispensando a etapa de substituição retroativa, mas com custo computacional geralmente maior<br>
c) Ser aplicável apenas a matrizes triangulares<br>
d) Ser idêntico, em número de operações, à Eliminação de Gauss padrão

> **Gabarito: b.** No método de Gauss-Jordan, o objetivo é chegar a uma matriz totalmente reduzida (diagonal/identidade), eliminando elementos tanto acima quanto abaixo da diagonal, o que evita a substituição retroativa, mas geralmente exige mais operações que a Eliminação de Gauss padrão.

---

**26.** **(Pegadinha)** Um estudante afirma: "Métodos iterativos como Jacobi e Gauss-Seidel são sempre superiores aos métodos diretos, pois usam menos memória." Sobre essa afirmação:

a) Ela está correta em todos os cenários, sem exceção<br>
b) Ela é uma generalização incorreta — métodos iterativos costumam ser vantajosos especialmente em sistemas grandes e esparsos, mas, para sistemas pequenos ou densos, ou quando é necessário resolver o sistema para vários vetores b com a mesma matriz A, métodos diretos (como LU) podem ser mais eficientes e até mais confiáveis quanto à convergência<br>
c) Ela está correta, pois métodos diretos nunca podem ser usados em sistemas grandes<br>
d) Ela está incorreta, mas apenas porque métodos iterativos nunca convergem na prática

> **Gabarito: b.** Pegadinha: a escolha entre método direto e iterativo depende do contexto (tamanho, esparsidade, número de sistemas a resolver com a mesma matriz, garantias de convergência) — não existe superioridade absoluta e universal de um tipo sobre o outro.

---

**27.** **(Pegadinha)** Sobre erros de arredondamento em métodos diretos como a Eliminação de Gauss, é correto afirmar que:

a) Eles nunca ocorrem, pois métodos diretos trabalham sempre com aritmética exata na prática<br>
b) Mesmo em métodos diretos, a aritmética de ponto flutuante utilizada na prática introduz erros de arredondamento a cada operação, que podem se acumular ao longo do processo — por isso, mesmo um "método exato" em teoria pode produzir resultados numericamente imprecisos na implementação computacional real<br>
c) Erros de arredondamento só ocorrem em métodos iterativos, nunca em métodos diretos<br>
d) Erros de arredondamento são sempre desprezíveis, independentemente do número de operações realizadas

> **Gabarito: b.** Pegadinha: a distinção entre "método exato em teoria" e "comportamento numérico na prática" é fundamental — mesmo métodos diretos, exatos em aritmética infinita, sofrem efeitos de arredondamento de ponto flutuante em computadores reais, o que motiva técnicas como pivoteamento.

---

**28.** Qual das opções abaixo representa corretamente a fórmula de atualização do método de **Jacobi** para a i-ésima componente, em um sistema Ax = b com A = D − L − U (sendo D a diagonal, L a parte triangular inferior e U a triangular superior, ambas com sinal trocado)?

a) x_i⁽ᵏ⁺¹⁾ = (1/a_ii) [ b_i − Σ_{j≠i} a_ij · x_j⁽ᵏ⁾ ], utilizando os valores da iteração anterior x⁽ᵏ⁾ para todos os j ≠ i<br>
b) x_i⁽ᵏ⁺¹⁾ = a_ii · b_i, sem qualquer soma dos demais termos<br>
c) x_i⁽ᵏ⁺¹⁾ = Σ_j a_ij, ignorando completamente o vetor b<br>
d) x_i⁽ᵏ⁺¹⁾ = x_i⁽ᵏ⁾ + 1, incrementado a cada iteração

> **Gabarito: a.** Essa é a fórmula clássica de Jacobi: isola-se x_i na i-ésima equação do sistema, calculando-a a partir dos demais valores da iteração **anterior** (x⁽ᵏ⁾), dividindo pelo elemento da diagonal a_ii (daí a exigência prática de a_ii ≠ 0).

---

**29.** **(Pegadinha)** Um sistema linear quadrado (mesmo número de equações e incógnitas) sempre possui exatamente uma solução, desde que o número de equações seja igual ao número de incógnitas. Essa afirmação está:

a) Correta, pois "quadrado" garante sempre solução única<br>
b) Incorreta — o fato de o sistema ser quadrado (n equações e n incógnitas) não garante, por si só, solução única; isso depende do determinante da matriz de coeficientes ser diferente de zero (matriz não singular); sistemas quadrados também podem ser indeterminados ou impossíveis<br>
c) Correta, mas apenas para sistemas com n > 10<br>
d) Incorreta, mas apenas porque sistemas quadrados nunca têm solução

> **Gabarito: b.** Pegadinha: ser "quadrado" (mesmo número de linhas e colunas) é condição necessária, mas não suficiente, para garantir solução única — o que efetivamente determina isso é a não singularidade da matriz (determinante ≠ 0).

---

**30.** **(Pegadinha)** Um professor afirma: "Como os computadores modernos são extremamente rápidos, o problema do mal condicionamento numérico em sistemas lineares deixou de ser relevante na prática." Essa afirmação está:

a) Correta, pois velocidade de processamento resolve qualquer problema de precisão numérica<br>
b) Incorreta — o mal condicionamento é um problema de **precisão** (sensibilidade da solução a pequenas perturbações e erros de arredondamento), não de velocidade de processamento; mesmo em computadores extremamente rápidos, sistemas mal condicionados continuam produzindo soluções numericamente pouco confiáveis se não forem tratados com técnicas apropriadas (como pivoteamento, maior precisão numérica ou reformulação do problema)<br>
c) Correta, pois aritmética de ponto flutuante moderna elimina totalmente erros de arredondamento<br>
d) Incorreta, mas apenas porque computadores modernos são, na verdade, mais lentos que os antigos

> **Gabarito: b.** Pegadinha conceitual final: velocidade computacional e precisão numérica são questões distintas — aumentar a velocidade de processamento não resolve, por si só, problemas de sensibilidade numérica inerentes a sistemas mal condicionados, que continuam exigindo cuidados metodológicos específicos.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis.
- Os pontos mais recorrentes de pegadinha nesta prova foram: a **diferença entre Jacobi e Gauss-Seidel** (questões 12 e 13), a **condição suficiente vs. necessária para convergência** (dominância diagonal vs. raio espectral — questões 14 a 17), a **distinção entre mal condicionamento e singularidade** (questão 10), e os **casos especiais na Eliminação de Gauss** (linha "0 = 0" vs. "0 = c" — questões 23 e 24) — vale reforçar esses pontos na correção em sala.
