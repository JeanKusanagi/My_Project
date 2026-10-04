# Simulado: Erros Numéricos, Aritmética de Ponto Flutuante e Análise de Erros

**Instruções:**

* Responda às 30 questões de múltipla escolha (A, B, C, D ou E).
* Atente para os detalhes sobre representação segundo a IEEE 754, erros de arredondamento vs. truncamento, propagação de erros e cancelamento subtrativo.
* Ao final de cada questão, consulte o gabarito comentado para validar os fundamentos teóricos e matemáticos.

---

### Questão 1 (Fácil)

Qual é a diferença fundamental entre o **Erro Absoluto** ($EA$) e o **Erro Relativo** ($ER$) na aproximação de um valor exato $x$ por um valor aproximado $\bar{x}$?

A) O erro absoluto é adimensional, enquanto o erro relativo preserva as unidades da grandeza medida.

B) O erro absoluto é dado por $EA = |x - \bar{x}|$, e o erro relativo é normalizado pelo valor exato (ou aproximado), dado por $ER = \frac{|x - \bar{x}|}{|x|}$ (para $x \neq 0$).

C) O erro relativo é sempre maior ou igual ao erro absoluto para qualquer número real.

D) O erro absoluto mede o erro de truncamento da série de Taylor, enquanto o erro relativo mede o erro de arredondamento do hardware.

E) O erro absoluto é aplicado apenas a números inteiros, enquanto o erro relativo aplica-se exclusivamente a números complexos.

**Resposta Correta: B**

**Comentário:** O erro absoluto $EA = |x - \bar{x}|$ fornece a magnitude escalar direta da diferença entre o valor real e a aproximação, mantendo a unidade da variável. O erro relativo $ER = \frac{|x - \bar{x}|}{|x|}$ adimensionaliza a medição, permitindo comparar a precisão de aproximações em ordens de grandeza discrepantes (por exemplo, um erro absoluto de 1 cm é irrelevante ao medir a distância Terra-Lua, mas desastroso ao medir o diâmetro de uma microesfera).

---

### Questão 2 (Médio - *Pegadinha*)

Considere o número racional $x = 0,1$ na base decimal ($10^{-1}$). Ao converter este número para a representação binária (base 2), o que acontece na aritmética de ponto flutuante?

A) $0,1_{10}$ transforma-se em um número binário exato e finito com apenas 2 bits significativos.

B) $0,1_{10}$ resulta em uma dízima periódica infinita na base binária ($0,0001100110011\dots_2$), sofrendo erro inevitável de representação/arredondamento ao ser armazenado em registria de memória com número finito de bits.

C) O número $0,1_{10}$ causa um estouro de memória (*overflow*) em qualquer arquitetura de 64 bits.

D) O valor converte-se exatamente em $2^{-1} + 2^{-2}$.

E) A conversão resulta em zero absoluto ($0,0_2$) devido às regras do padrão IEEE 754.

**Resposta Correta: B**

**Comentário:** *Pegadinha clássica de arquitetura de computadores!* Um número fracionário decimal só possui representação binária finita se puder ser expresso como uma soma finita de potências negativas de 2 (isto é, se seu denominador na fração irredutível for uma potência de 2). Como $0,1 = \frac{1}{10} = \frac{1}{2 \times 5}$, a presença do fator 5 faz com que sua expansão binária seja a dízima periódica $0,0001100110011\dots_2$. Ao armazená-lo no computador, os bits são cortados/arredondados, fazendo com que $0,1$ não seja armazenado de forma 100% exata.

---

### Questão 3 (Médio)

Na representação de números em ponto flutuante padrão **IEEE 754 de Precisão Simpla** (32 bits), como estão distribuídos os bits entre as três partes fundamentais da palavra de memória (Sinal, Expoente com viés/bias, Mantissa/Frac)?

A) 1 bit de sinal, 8 bits de expoente, 23 bits de mantissa (fração).

B) 1 bit de sinal, 11 bits de expoente, 52 bits de mantissa.

C) 2 bits de sinal, 10 bits de expoente, 20 bits de mantissa.

D) 8 bits de sinal, 8 bits de expoente, 16 bits de mantissa.

E) 1 bit de sinal, 15 bits de expoente, 16 bits de mantissa.

**Resposta Correta: A**

**Comentário:** O padrão IEEE 754 de precisão simples (32 bits / `float`) aloca:
- 1 bit para o Sinal ($S$);
- 8 bits para o Expoente ($E$), usando viés (*bias*) de 127;
- 23 bits para a Mantissa/Significand ($M$), com um bit implícito de valor 1 em números normalizados.
*(Para precisão dupla/64 bits / `double`, a distribuição é de 1 bit de sinal, 11 de expoente e 52 de mantissa).*

---

### Questão 4 (Fácil)

Qual é a origem do **Erro de Truncamento** em métodos numéricos?

A) Inexactidão nos circuitos eletrônicos e falhas de fabricação dos processadores.

B) Limitação do número de dígitos/bits armazenados na memória do computador ao arredondar um número.

C) Aproximação de um processo matemático infinito (como o limite de uma série, uma derivada ou uma integral) por um processo finito.

D) Conversão incorreta de dados inseridos pelo usuário via teclado.

E) Ruídos eletromagnéticos em redes de computadores.

**Resposta Correta: C**

**Comentário:** O erro de truncamento decorre da aproximação de procedimentos matemáticos contínuos/infinitos por procedimentos discretos/finitos (por exemplo, ao truncar uma Série de Taylor em seu terceiro termo para aproximar $\operatorname{sen}(x)$, ou ao aproximar uma derivada por diferenças finitas). Não confundir com o *erro de arredondamento*, este sim decorrente da precisão finita da representação numérica no hardware.

---

### Questão 5 (Difícil - *Pegadinha*)

O fenômeno conhecido como **Cancelamento Catastrófico** (ou cancelamento subtrativo) ocorre tipicamente quando:

A) Multiplicamos dois números positivos extremamente grandes, ultrapassando a capacidade do expoente (*overflow*).

B) Subtraímos dois números quase iguais que contêm erros de arredondamento em suas partes menos significativas, resultando na perda severa de dígitos significativos corretos na resposta.

C) Dividimos qualquer número de ponto flutuante por zero em um laço `for`.

D) Somamos um número positivo a um número negativo de mesma magnitude em precisão infinita.

E) Somamos zero a uma matriz identidade.

**Resposta Correta: B**

**Comentário:** *Pegadinha sutil!* Ao calcular $a - b$ onde $a \approx b$, os dígitos mais significativos de $a$ e $b$ se anulam na subtração (viram zeros). Como o resultado é normalizado deslocando a mantissa para a esquerda, os bits menos significativos — que continham os erros de arredondamento acumulados — são promovidos aos dígitos mais significativos do resultado. Por exemplo, ao resolver a fórmula de quadratura $b^2 - 4ac$ quando $b^2 \gg 4ac$, perde-se grande parte da precisão dos dígitos válidos.

---

### Questão 6 (Médio)

O parâmetro conhecido como **Épsilon da Máquina** ($\epsilon_{máq}$) representa:

A) O maior número real que o computador consegue armazenar antes de gerar *overflow*.

B) O menor número positivo $\epsilon$ tal que $1,0 + \epsilon > 1,0$ na aritmética de ponto flutuante da máquina.

C) O tempo necessário para realizar uma instrução de adição de ponto flutuante na ULA.

D) O número exato de bits do barramento de dados da CPU.

E) A diferença entre o erro absoluto e o erro relativo para $x = 0$.

**Resposta Correta: B**

**Comentário:** O Épsilon da Máquina ($\epsilon_{máq}$) mede a precisão relativa do sistema de ponto flutuante. É definido como o menor valor positivo que, somado a 1,0 na aritmética do computador, produz um resultado estritamente diferente de 1,0. Para precisão simples IEEE 754 (23 bits de mantissa), $\epsilon_{máq} = 2^{-23} \approx 1,19 \times 10^{-7}$. Para precisão dupla, $\epsilon_{máq} = 2^{-52} \approx 2,22 \times 10^{-16}$.

---

### Questão 7 (Difícil)

Deseja-se avaliar a função $f(x) = \sqrt{x+1} - \sqrt{x}$ para valores extremamente grandes de $x$ ($x \to \infty$). Na computação direta de $f(x)$ ocorre severo cancelamento subtrativo. Qual das seguintes formulações algebricamente equivalentes **elimina** o problema do cancelamento numérico?

A) $f(x) = \frac{1}{\sqrt{x+1} + \sqrt{x}}$

B) $f(x) = (\sqrt{x+1})^2 - (\sqrt{x})^2$

C) $f(x) = \sqrt{\frac{x+1}{x}}$

D) $f(x) = \ln(x+1) - \ln(x)$

E) $f(x) = \frac{x+1 - x}{\sqrt{x}}$

**Resposta Correta: A**

**Comentário:** Racionalizando o numerador:
$$f(x) = (\sqrt{x+1} - \sqrt{x}) \cdot \frac{\sqrt{x+1} + \sqrt{x}}{\sqrt{x+1} + \sqrt{x}} = \frac{(x+1) - x}{\sqrt{x+1} + \sqrt{x}} = \frac{1}{\sqrt{x+1} + \sqrt{x}}$$
Nesta nova forma, substituímos uma *subtração de números quase iguais* por uma *soma no denominador*. A soma de dois números grandes e positivos é numericamente estável e não sofre cancelamento catastrófico.

---

### Questão 8 (Fácil)

Em aritmética de ponto flutuante, o fenômeno de **Underflow** (subtransbordamento) ocorre quando:

A) O resultado de uma operação gera um valor cujo módulo é maior que o maior número representável pelo sistema.

B) O resultado de uma operação não-nula tem módulo estritamente menor do que o menor número positivo normalizado representável pelo sistema.

C) A divisão por zero é solicitada ao sistema operacional.

D) A mantissa ultrapassa o tamanho limite de 64 bits.

E) O usuário tenta armazenar um número negativo em uma variável declarada como sem sinal (*unsigned*).

**Resposta Correta: B**

**Comentário:** O *Underflow* ocorre quando o módulo do número calculado é tão pequeno (próximo de zero) que o expoente do sistema de ponto flutuante não consegue representá-lo sem perder os dígitos significativos da mantissa (podendo resultar em denormalização ou em alocação direta como zero absoluto). O oposto — um número grande demais para o expoente máximo — chama-se *Overflow*.

---

### Questão 9 (Médio)

Seja a Série de Taylor para a função $e^x$ em torno de $x=0$:
$$e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$$
Se aproximarmos $e^{0,5}$ utilizando apenas os três primeiros termos da série ($k=0, 1, 2$), qual é o **erro de truncamento limitado pelo Resto de Lagrange**?

*(Dado: $e^{0,5} < 2$)*

A) $R_2(0,5) \le \frac{2 \cdot (0,5)^3}{3!} = \frac{2 \cdot 0,125}{6} \approx 0,04167$

B) $R_2(0,5) = 0,5$

C) $R_2(0,5) = \frac{(0,5)^2}{2!} = 0,125$

D) $R_2(0,5) = 0$

E) $R_2(0,5) = \frac{2^3}{3!} \approx 1,333$

**Resposta Correta: A**

**Comentário:** Pela fórmula do Resto de Lagrange para o polinômio de ordem $n=2$:
$$R_2(x) = \frac{f'''(\xi)}{3!} x^3 \quad \text{para algum } \xi \in (0, x)$$
Como $f(x) = e^x$, temos $f'''(\xi) = e^\xi$. Para $x = 0,5$, o valor máximo de $e^\xi$ no intervalo $(0; 0,5)$ é $e^{0,5} < 2$.
Logo:
$$|R_2(0,5)| \le \frac{2 \cdot (0,5)^3}{6} = \frac{2 \cdot 0,125}{6} = \frac{0,25}{6} \approx 0,04167$$

---

### Questão 10 (Difícil - *Pegadinha*)

Na aritmética de ponto flutuante padrão IEEE 754, a operação de adição **NÃO** satisfaz necessariamente qual propriedade algébrica clássica da matemática pura?

A) Comutatividade ($a + b = b + a$)

B) Identidade do elemento neutro ($a + 0 = a$)

C) Associatividade ($(a + b) + c = a + (b + c)$)

D) Simetria em relação à reflexão na origem

E) Monotonicidade para valores não negativos

**Resposta Correta: C**

**Comentário:** *Pegadinha conceitual de álgebra computacional!* A adição de ponto flutuante é **comutativa** ($a \oplus b = b \oplus a$), mas **NÃO É ASSOCIATIVA**!
Exemplo em máquina com pouca precisão:
Seja $a = 10^{16}$, $b = -10^{16}$, $c = 1$.
- $(a + b) + c = (10^{16} - 10^{16}) + 1 = 0 + 1 = 1$.
- $a + (b + c) = 10^{16} + (-10^{16} + 1) = 10^{16} + (-10^{16})$ (pois $-10^{16} + 1$ arredonda para $-10^{16}$) $= 0$.
Assim, $(a+b)+c \neq a+(b+c)$. Por esse motivo, a ordem de somatório de vetores em códigos numéricos altera o resultado final.

---

### Questão 11 (Médio)

Suponha que um procedimento numérico meça uma extensão $x = 200\text{ m}$ com erro absoluto de $EA = 0,2\text{ m}$, e outro procedimento meça uma extensão $y = 2\text{ m}$ com erro absoluto de $EA = 0,05\text{ m}$. Comparando a precisão relativa das duas medições:

A) A medição de $y$ é mais precisa porque seu erro absoluto é menor.

B) A medição de $x$ é mais precisa porque seu erro relativo é $0,1\%$ ($0,001$), enquanto o erro relativo de $y$ é $2,5\%$ ($0,025$).

C) Ambas possuem exatamente a mesma precisão relativa.

D) Não é possível comparar erros relativos em grandezas de comprimentos diferentes.

E) A medição de $y$ possui erro relativo nulo.

**Resposta Correta: B**

**Comentário:**
- Erro relativo de $x$: $ER_x = \frac{0,2}{200} = 0,001 = 0,1\%$.
- Erro relativo de $y$: $ER_y = \frac{0,05}{2} = 0,025 = 2,5\%$.
A medição de $x$ apresenta maior precisão relativa por apresentar uma incerteza proporcionalmente menor em relação ao total medido.

---

### Questão 12 (Difícil)

Seja $y = f(x)$ uma função diferenciável. O **Número de Condição Relativo** ($K$) que quantifica a sensibilidade da resposta $y$ a pequenas variações percentuais na entrada $x$ é dado por:

A) $K = |f'(x)|$

B) $K = \left| \frac{x \cdot f'(x)}{f(x)} \right|$

C) $K = \left| \frac{f(x)}{x \cdot f'(x)} \right|$

D) $K = |f''(x) - f'(x)|$

E) $K = \frac{|x - f(x)|}{|x|}$

**Resposta Correta: B**

**Comentário:** O erro relativo transmitido para a saída $y$ através do erro relativo da entrada $x$ é derivado via Série de Taylor:
$$\Delta y \approx f'(x) \Delta x \implies \frac{\Delta y}{y} \approx \frac{f'(x) \Delta x}{f(x)} = \left[ \frac{x f'(x)}{f(x)} \right] \frac{\Delta x}{x}$$
Portanto, a razão entre o erro relativo relativo de saída e o erro relativo de entrada define o Número de Condição da Função: $K = \left| \frac{x f'(x)}{f(x)} \right|$. Se $K \gg 1$, o problema é mal condicionado.

---

### Questão 13 (Médio - *Pegadinha*)

Usando o conceito de Número de Condição da questão anterior para a função $f(x) = \frac{1}{1-x}$ perto de $x = 1$, o problema de avaliar $f(x)$ é:

A) Bem condicionado, pois $K \to 0$ quando $x \to 1$.

B) Mal condicionado, pois $K = \left| \frac{x}{1-x} \right|$, o que tende ao infinito quando $x \to 1$.

C) Insensível a erros de arredondamento em qualquer hardware.

D) Estável somente se trabalharmos em base octal.

E) Indeterminado, pois a função não é contínua para $x = 0$.

**Resposta Correta: B**

**Comentário:** *Pegadinha de amplificação de erro!*
$$f'(x) = \frac{1}{(1-x)^2}$$
$$K = \left| \frac{x f'(x)}{f(x)} \right| = \left| \frac{x \cdot \frac{1}{(1-x)^2}}{\frac{1}{1-x}} \right| = \left| \frac{x}{1-x} \right|$$
Conforme $x \to 1$, o denominador $(1-x) \to 0$, fazendo $K \to \infty$. Isso significa que variações minúsculas no último bit de $x$ serão absurdamente amplificadas ao calcular $f(x)$, caracterizando uma avaliação mal condicionada.

---

### Questão 14 (Fácil)

No padrão IEEE 754, qual valor especial é retornado ao efetuar a operação $1,0 / 0,0$ em ponto fluantante sem interromper a execução do programa por exceção fatal?

A) `NaN` (Not a Number)

B) `+Infinity` (+$\infty$)

C) `0.0`

D) `-1.0`

E) `Overflow_Error_Code_99`

**Resposta Correta: B**

**Comentário:** O padrão IEEE 754 define comportamentos bem determinados para operações limítrofes:
- Número positivo não-nulo dividido por $+0,0$ gera `+Infinity` ($+\infty$).
- Operações indeterminadas como $0,0 / 0,0$, $\infty - \infty$ ou $\sqrt{-1}$ geram `NaN` (*Not a Number*).

---

### Questão 15 (Difícil)

Considere a propagação do erro absoluto na adição de duas variáveis $x$ e $y$ cujas aproximações possuem erros absolutos limitados por $\Delta x$ e $\Delta y$, ou seja, $\bar{x} = x \pm \Delta x$ e $\bar{y} = y \pm \Delta y$. Qual é o **limite superior máximo** para o erro absoluto da soma $z = x + y$?

A) $\Delta z = \Delta x \cdot \Delta y$

B) $\Delta z = \Delta x + \Delta y$

C) $\Delta z = \sqrt{(\Delta x)^2 + (\Delta y)^2}$

D) $\Delta z = |\Delta x - \Delta y|$

E) $\Delta z = \frac{\Delta x}{\Delta y}$

**Resposta Correta: B**

**Comentário:** Pela análise de erro de pior caso (*worst-case error bound*):
$$\bar{z} = \bar{x} + \bar{y} = (x + \epsilon_x) + (y + \epsilon_y) = (x + y) + (\epsilon_x + \epsilon_y)$$
Pela desigualdade triangular:
$$|\bar{z} - z| = |\epsilon_x + \epsilon_y| \le |\epsilon_x| + |\epsilon_y| \le \Delta x + \Delta y$$
Portanto, os erros absolutos **se somam** na adição/subtração de variáveis.

---

### Questão 16 (Médio)

Ao multiplicar duas variáveis $x$ e $y$ com pequenos erros relativos $ER_x$ e $ER_y$, qual é a relação aproximada para o erro relativo do produto $z = x \cdot y$?

A) $ER_z \approx ER_x \cdot ER_y$

B) $ER_z \approx ER_x + ER_y$

C) $ER_z \approx \frac{ER_x}{ER_y}$

D) $ER_z \approx |ER_x - ER_y|$

E) $ER_z \approx (ER_x)^2 + (ER_y)^2$

**Resposta Correta: B**

**Comentário:** Tomando o logaritmo natural do produto $z = x \cdot y$:
$$\ln(z) = \ln(x) + \ln(y)$$
Diferenciando ambos os lados:
$$\frac{dz}{z} = \frac{dx}{x} + \frac{dy}{y}$$
Passando para os limites de erros relativos superiores: $ER_z \le ER_x + ER_y$. Ou seja, na multiplicação (e divisão), os **erros relativos se somam**.

---

### Questão 17 (Difícil - *Pegadinha*)

Seja o algoritmo para calcular a média de dois números $a$ e $b$ em ponto flutuante. Duas fórmulas matematicamente idênticas são propostas:
1. $m_1 = \frac{a + b}{2,0}$
2. $m_2 = a + \frac{b - a}{2,0}$

Qual das afirmativas abaixo descreve **corretamente** o comportamento numérico dessas fórmulas para valores de $a$ e $b$ extremamente grandes e próximos do limite de *overflow* do sistema?

A) $m_1$ é numericamente superior a $m_2$ em todas as situações.

B) $m_1$ pode sofrer *overflow* intermediário durante a soma $a + b$ mesmo que a média final caiba no intervalo de representação, enquanto $m_2$ evita esse *overflow*.

C) $m_2$ causa divisão por zero obrigatoriamente se $a = b$.

D) Ambas as fórmulas geram o exato mesmo estouro de memória em qualquer ordem de execução.

E) $m_2$ só pode ser executada em processadores de 128 bits.

**Resposta Correta: B**

**Comentário:** *Pegadinha clássica de implementação de software (ex: busca binária)!* Se $a$ e $b$ forem números positivos muito grandes (próximos de `FLOAT_MAX`), a soma $a + b$ na fórmula $m_1$ ultrapassa `FLOAT_MAX`, gerando $+\infty$, e a divisão por 2 resulta em $+\infty$ (erro de *overflow*). Na fórmula $m_2$, calcula-se a diferença $b - a$ (que é um valor pequeno se $a \approx b$), divide-se por 2 e soma-se a $a$, sem que nenhuma etapa intermediária ultrapasse a capacidade de representação.

---

### Questão 18 (Fácil)

Quantos **dígitos significativos** corretos possui a aproximação $\bar{x} = 3,1415$ para o número $\pi \approx 3,14159265\dots$?

A) 2 dígitos significativos

B) 3 dígitos significativos

C) 5 dígitos significativos

D) 8 dígitos significativos

E) Nenhum dígito significativo

**Resposta Correta: C**

**Comentário:** Um número aproximado $\bar{x}$ tem $d$ dígitos significativos corretos se o erro absoluto for menor que metade de uma unidade na $d$-ésima posição contada a partir do primeiro dígito não-nulo à esquerda.
Aqui, $|3,14159265 - 3,1415| = 0,00009265 < 0,0001 = 10^{-4}$. Os dígitos `3`, `1`, `4`, `1`, `5` (total de 5 dígitos) estão totalmente corretos.

---

### Questão 19 (Médio)

O que são números **Denormalizados** (ou Subnormais) no padrão IEEE 754?

A) Números cujo bit de sinal é indefinido.

B) Números extremamente pequenos situados entre zero e o menor número normalizado, nos quais o bit implícito da mantissa passa a ser $0$ em vez de $1$, evitando a interrupção abrupta por underflow (*underflow gradual*).

C) Números inteiros convertidos para texto ASCII.

D) Valores numéricos armazenados em memória ROM estática.

E) Números gerados exclusivamente por erros de divisão por zero.

**Resposta Correta: B**

**Comentário:** Em números normalizados, a mantissa é interpretada como $1,M_1 M_2 \dots M_k$ (bit implícito igual a 1). Quando o expoente atinge seu valor mínimo possível, se o número diminuir ainda mais, o sistema transita para o modo **subnormal/denormalizado**: o expoente é mantido no valor mínimo fixo e o bit implícito passa a ser $0$ ($0,M_1 M_2 \dots$). Isso garante que a perda de precisão ao aproximar do zero ocorra de forma gradual (*gradual underflow*), em vez de cair abruptamente para zero.

---

### Questão 20 (Difícil)

Deseja-se somar um vetor de $10^6$ números positivos de ponto flutuante de precisão simples. Se os números forem somados na ordem direta usando um acumulador simples, o erro acumulado pode ser alto devido à adição recorrente de números pequenos a uma soma acumulada grande. Qual algoritmo é amplamente utilizado em bibliotecas numéricas para mitigar esse problema compensando os bits perdidos?

A) Algoritmo de Euclides estendido

B) Algoritmo de Soma de Kahan (Kahan Summation Algorithm)

C) Algoritmo de Strassen

D) Algoritmo de Horner

E) Método de Runge-Kutta de 4ª Ordem

**Resposta Correta: B**

**Comentário:** O **Algoritmo de Kahan** mantém uma variável separada para guardar a "compensação" dos bits de menor ordem perdidos na adição de ponto flutuante a cada iteração. Ao resgatar essa compensação na iteração seguinte, o erro acumulado total da soma de $N$ elementos cai de $O(N \cdot \epsilon)$ para $O(\epsilon)$, tornando a soma praticamente independente do número de termos $N$.

---

### Questão 21 (Fácil)

Dada a conversão de um número da base decimal para a base binária, dizemos que ocorreu um **Erro de Arredondamento por Truncamento** (*Chopping*) quando:

A) Os bits excedentes à capacidade da mantissa são simplesmente descartados.

B) Adiciona-se 1 ao bit menos significativo se o bit seguinte for 1.

C) O número é multiplicado por $2^{127}$.

D) Todos os bits 0 são invertidos para 1.

E) O número é convertido para complemento de dois.

**Resposta Correta: A**

**Comentário:** Há duas estratégias principais de arredondamento:
- **Truncamento / Corte (*Chopping*):** Simplesmente despreza-se todos os bits que excedem a quantidade de bits reservada para a mantissa.
- **Arredondamento Padrão (*Round-to-nearest*):** Ajusta-se o último bit preservado para o valor representável mais próximo (semelhante à regra de arredondamento decimal).

---

### Questão 22 (Médio - *Pegadinha*)

Considere a avaliação do polinômio $P(x) = 3x^3 - 2x^2 + 5x - 7$ em um ponto $x_0$. Qual método reduz o número total de multiplicações (de 6 para 3) e diminui a propagação dos erros de arredondamento?

A) Fórmula de Bhaskara estendida

B) Regra de Cramer

C) Esquema de Horner (ou Regra de Briot-Ruffini)

D) Expansão de Fourier em seno e cosseno

E) Interpolação de Lagrange

**Resposta Correta: C**

**Comentário:** *Pegadinha de otimização numérica!* Reescrevendo $P(x)$ na forma aninhada de **Horner**:
$$P(x) = ((3x - 2)x + 5)x - 7$$
Enquanto a forma ingênua $3(x \cdot x \cdot x) - 2(x \cdot x) + 5x - 7$ executa 6 multiplicações e 3 somas/subtrações, a forma de Horner executa apenas 3 multiplicações e 3 somas/subtrações. Além de ser duas vezes mais rápida, a forma aninhada minimiza o número de operações com potências, reduzindo substancialmente os erros de arredondamento intermediários.

---

### Questão 23 (Difícil)

Considere um algoritmo numérico $A$ para resolver um problema $P$. Dizemos que o algoritmo $A$ é **Numericamente Estável** quando:

A) Ele não utiliza variáveis em ponto flutuante, apenas números inteiros.

B) Ele garante que pequenas variações/erros de arredondamento introduzidos durante as etapas intermediárias dos cálculos não são amplificados descontroladamente ao longo da execução, produzindo uma solução próxima da solução exata do problema ligeiramente perturbado.

C) O tempo de execução do algoritmo independe do tamanho dos dados de entrada.

D) O algoritmo sempre retorna uma matriz simétrica definida positiva.

E) O erro de truncamento é rigorosamente igual a zero para qualquer função de entrada.

**Resposta Correta: B**

**Comentário:** A **estabilidade numérica** é uma propriedade do *algoritmo* (diferente do *condicionamento*, que é uma propriedade do *problema*). Um algoritmo é estavelmente numérico se ele não amplifica os erros de arredondamento/ponto flutuante inerentes ao hardware durante suas operações intermediárias (análise de estabilidade direta/reversa de Wilkinson).

---

### Questão 24 (Médio)

Na análise da fórmula de diferenças finitas para aproximação de derivadas de $f(x)$:
$$f'(x) \approx \frac{f(x+h) - f(x)}{h}$$
O erro total da aproximação em computador é composto por duas fontes de erro conflitantes em relação ao tamanho do passo $h$. O que acontece quando reduzimos $h$ para valores extremamente próximos de zero ($h \to 0$)?

A) O erro de truncamento diminui, mas o erro de arredondamento (cancelamento subtrativo em $f(x+h)-f(x)$ dividido por $h$ muito pequeno) cresce drasticamente, gerando um valor ideal $h^*$ de compromisso.

B) Ambos os erros (truncamento e arredondamento) caem para zero simultaneamente.

C) O erro de truncamento cresce e o erro de arredondamento cai para zero.

D) O sistema entra em *overflow* imediatamente para qualquer função.

E) A aproximação torna-se exata sem qualquer tipo de erro para $h < 10^{-16}$.

**Resposta Correta: A**

**Comentário:** Trata-se do clássico dilema do tamanho do passo $h$:
- **Erro de Truncamento:** É da ordem $O(h)$. Logo, quanto *menor* o $h$, *menor* é o erro de truncamento.
- **Erro de Arredondamento:** Como $f(x+h) \approx f(x)$, a diferença no numerador sofre cancelamento subtrativo e o resultado é dividido por um $h$ diminuto, ampliando o erro na ordem $O(\epsilon_{máq}/h)$. Quanto *menor* o $h$, *maior* o erro de arredondamento.
Existe um $h_{ótimo}$ onde a soma desses dois erros é minimizada.

---

### Questão 25 (Fácil)

Em um sistema numérico hipotético em ponto flutuante $F(\beta, t, L, U)$, onde $\beta$ é a base, $t$ é o número de dígitos da mantissa, $L$ é o limite inferior do expoente e $U$ é o limite superior do expoente, quantos elementos existem se $\beta = 10$, $t = 1$, $L = -1$ e $U = 1$?

*(Considere apenas números normalizados e positivos, excluindo o zero)*

A) $9 \times 3 = 27$ números

B) 10 números

C) 100 números

D) 3 números

E) 81 números

**Resposta Correta: A**

**Comentário:**
- Na base $\beta = 10$ com $t = 1$ dígito significando normalizado, o primeiro e único dígito da mantissa pode assumir os valores $1, 2, 3, 4, 5, 6, 7, 8, 9$ (9 opções).
- O expoente $e$ pode assumir os valores no intervalo $[L, U] = [-1, 0, 1]$ (3 opções).
- Total de números positivos normalizados: $9 \text{ (dígitos)} \times 3 \text{ (expoentes)} = 27$ números representáveis.

---

### Questão 26 (Difícil - *Pegadinha*)

Seja a expressão $S = \sum_{k=1}^{\infty} \frac{1}{k}$ (Série Harmônica, sabidamente divergente na matemática real). Ao rodar um programa de computador em precisão simples que executa este somatório em um laço infinito `while(true)`, qual será o comportamento do programa?

A) O programa rodará para sempre até que a memória RAM do computador esgoste.

B) O programa eventualmente para de alterar o valor da soma e entra em um estado estático (estagna), pois quando $k$ fica suficientemente grande, $1/k < \epsilon_{máq} \cdot S$, tornando a adição de $1/k$ insignificante frente à precisão da mantissa.

C) O programa gera o erro `NaN` imediatamente na iteração $k=10$.

D) A variável estoura para $-\infty$ devido à inversão do bit de sinal.

E) O sistema operacional encerra o processo por violação de acesso à CPU.

**Resposta Correta: B**

**Comentário:** *Pegadinha de convergência numérica vs. matemática!* A Série Harmônica diverge matematicamente. Porém, na aritmética de ponto flutuante de precisão finita, conforme a soma acumulada $S$ cresce, a distância entre $S$ e o próximo número representável em máquina ($\Delta = S \cdot \epsilon_{máq}$) também cresce. Quando $k$ for tão grande que $\frac{1}{k} < \frac{S \cdot \epsilon_{máq}}{2}$, o resultado da operação $S + \frac{1}{k}$ arredonda de volta para $S$. A partir desse ponto, $S$ para de crescer e o laço torna-se um loop infinito com soma estagnada.

---

### Questão 27 (Médio)

Se aproximarmos a função $f(x) = \cos(x)$ pelo seu polinômio de Taylor de ordem 2 em torno de $x_0 = 0$, dado por $P_2(x) = 1 - \frac{x^2}{2}$, qual é o erro absoluto de truncamento ao estimar $\cos(0,1)$ sabendo que o valor exato aproximado é $\cos(0,1) \approx 0,995004165$?

A) $EA \approx 0,000004165$

B) $EA \approx 0,1$

C) $EA \approx 0,005$

D) $EA \approx 0,05004$

E) $EA \approx 0$

**Resposta Correta: A**

**Comentário:**
1. Avaliação do polinômio em $x = 0,1$:
$$P_2(0,1) = 1 - \frac{(0,1)^2}{2} = 1 - \frac{0,01}{2} = 1 - 0,005 = 0,995000000$$
2. Cálculo do Erro Absoluto:
$$EA = |f(0,1) - P_2(0,1)| = |0,995004165 - 0,995000000| = 0,000004165 = 4,165 \times 10^{-6}$$

---

### Questão 28 (Médio)

Qual é a representação gráfica do efeito da **arredondamento por corte** (*chopping*) versus **arredondamento ao mais próximo** (*round to nearest*) na distribuição do erro de representação ao longo do eixo real?

A) O corte (*chopping*) introduz um viés (*bias*) sempre negativo/positivo (unilateral), enquanto o arredondamento ao mais próximo distribui os erros de forma simétrica ao redor de zero.

B) O corte não possui nenhum erro para números ímpares.

C) O arredondamento ao mais próximo dobra a amplitude total do erro absoluto máximo.

D) Ambos possuem viés estritamente positivo para todos os números complexos.

E) O corte zera o erro de representação para números irracionais.

**Resposta Correta: A**

**Comentário:** No *chopping*, desprezam-se sempre as frações restantes para baixo (para números positivos), fazendo com que o valor representado seja sistematicamente menor ou igual ao valor real ($\bar{x} \le x$). Isso cria um **viés estatístico (bias)** na propagação de erros. Já o *round-to-nearest* escolhe o ponto flutuante mais próximo, fazendo com que os erros se distribuam simetricamente no intervalo $[-\frac{\epsilon}{2}, \frac{\epsilon}{2}]$, cancelando-se parcialmente na média de longas cadeias de cálculo.

---

### Questão 29 (Difícil)

Para resolver a equação do segundo grau $a x^2 + b x + c = 0$ quando $b > 0$ e $b^2 \gg 4ac$, a raiz $x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}$ sofre forte cancelamento subtrativo, pois $\sqrt{b^2 - 4ac} \approx b$. Como podemos calcular $x_1$ de forma numericamente estável usando a outra raiz $x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}$ (que não sofre cancelamento)?

A) Utilizando as Relações de Viète: $x_1 = \frac{c}{a \cdot x_2}$

B) Fazendo $x_1 = -x_2$

C) Fazendo $x_1 = x_2^2$

D) Somando $b$ a ambos os lados da equação

E) Multiplicando $x_2$ por $\det(A)$

**Resposta Correta: A**

**Comentário:** Pelas **Relações de Viète**, o produto das raízes de uma equação do segundo grau satisfaz $x_1 \cdot x_2 = \frac{c}{a}$.
Como $x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}$ é a soma de dois números de mesmo sinal (não sofre cancelamento subtrativo), podemos calculá-lo de forma precisa e, em seguida, obter a primeira raiz sem cancelamento via:
$$x_1 = \frac{c}{a \cdot x_2}$$
Esta é uma reformulação clássica em software numérico para evitar a perda de precisão em equações do segundo grau.

---

### Questão 30 (Fácil)

A conversão do número binário em ponto flutuante com mantissa normalizada $+1,101_2 \times 2^3$ para a base decimal resulta em qual valor?

A) $13,0_{10}$

B) $6,5_{10}$

C) $26,0_{10}$

D) $1,625_{10}$

E) $3,25_{10}$

**Resposta Correta: A**

**Comentário:**
1. Valor da mantissa em binário:
$$1,101_2 = 1 \cdot 2^0 + 1 \cdot 2^{-1} + 0 \cdot 2^{-2} + 1 \cdot 2^{-3} = 1 + 0,5 + 0 + 0,125 = 1,625_{10}$$
2. Multiplicação pelo expoente $2^3 = 8$:
$$1,625 \times 8 = 13,0_{10}$$
*(Ou simplesmente deslocar a vírgula 3 casas para a direita: $1101_2 = 8 + 4 + 0 + 1 = 13_{10}$)*.
```

O simulado sobre **Erros Numéricos e Aritmética de Ponto Flutuante** contendo as 30 questões, gabaritos e análises de estabilidade/cancelamento já está disponível no painel ao lado.