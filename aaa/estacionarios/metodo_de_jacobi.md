# Método de Jacobi (Método de Gauss-Jacobi)

O **Método de Jacobi** é um algoritmo iterativo de análise numérica utilizado para encontrar soluções aproximadas para sistemas de equações lineares do tipo $Ax = b$, onde $A$ é uma matriz de coeficientes, $x$ é o vetor de incógnitas e $b$ é o vetor de termos independentes.

---

## 📋 Funcionamento do Algoritmo

O princípio básico consiste em isolar cada incógnita $x_i$ a partir da linha correspondente da matriz, assumindo que os elementos da diagonal principal ($a_{ii}$) não são nulos.

Dada a $i$-ésima equação do sistema:
$$a_{i1}x_1 + a_{i2}x_2 + \dots + a_{ii}x_i + \dots + a_{in}x_n = b_i$$

Isolando $x_i$, obtemos a fórmula de iteração:
$$x_i^{(k+1)} = rac{1}{a_{ii}} \left( b_i - \sum_{j 
eq i} a_{ij} x_j^{(k)} ight)$$

No Método de Jacobi, o cálculo do novo vetor aproximado $x^{(k+1)}$ depende **exclusivamente** dos valores obtidos na iteração anterior $x^{(k)}$.

---

## 📐 Critério de Convergência (Critério das Linhas)

Para que o método tenha garantia de convergência para qualquer estimativa inicial $x^{(0)}$, a matriz $A$ deve ser **estritamente diagonal dominante**. Isso significa que, para cada linha $i$, o valor absoluto do elemento da diagonal deve ser maior que a soma dos valores absolutos dos demais elementos daquela linha:

$$|a_{ii}| > \sum_{j 
eq i} |a_{ij}|, \quad orall i = 1, \dots, n$$

Se a matriz satisfizer este critério, o método convergirá independentemente do chute inicial.

---

## ⚙️ Exemplo Prático

Considere o seguinte sistema linear:
$$egin{cases} 
10x_1 + x_2 + 2x_3 = 13 \
x_1 + 10x_2 + 3x_3 = 14 \
2x_1 + 3x_2 + 10x_3 = 15 
\end{cases}$$

### Step 1: Isolando as variáveis
$$egin{aligned}
x_1^{(k+1)} &= rac{13 - x_2^{(k)} - 2x_3^{(k)}}{10} \
x_2^{(k+1)} &= rac{14 - x_1^{(k)} - 3x_3^{(k)}}{10} \
x_3^{(k+1)} &= rac{15 - 2x_1^{(k)} - 3x_2^{(k)}}{10}
\end{aligned}$$

### Step 2: Primeira iteração ($k=0$ com aproximação inicial $x^{(0)} = [0, 0, 0]^T$)
$$egin{aligned}
x_1^{(1)} &= rac{13 - 0 - 0}{10} = 1.3 \
x_2^{(1)} &= rac{14 - 0 - 0}{10} = 1.4 \
x_3^{(1)} &= rac{15 - 0 - 0}{10} = 1.5
\end{aligned}$$

O processo se repete substituindo $[1.3, 1.4, 1.5]^T$ nas equações até atingir a tolerância estipulada.