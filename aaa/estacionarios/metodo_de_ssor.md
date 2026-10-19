# Método de Sobrerrelaxação Sucessiva Simétrico (SSOR)

O método **Symmetric Successive Over-Relaxation (SSOR)** é uma extensão do método SOR tradicional desenvolvida para matrizes simétricas (geralmente simétricas e definitas positivas). A principal diferença é que cada iteração completa do SSOR consiste em **duas meias-iterações**: uma passada para a frente (*forward*) e uma passada para trás (*backward*).

Embora possa ser usado como um solver iterativo direto, a aplicação mais importante e comum do SSOR na álgebra linear computacional moderna é como um **Pré-condicionador** para acelerar métodos de subespaço de Krylov, como o **Método dos Gradientes Conjugados (CG)**.

---

## 1. Funcionamento Algorítmico

Dada uma matriz de coeficientes $A$ decomposta em suas partes diagonal ($D$), estritamente inferior ($L$) e estritamente superior ($U$), tal que $A = D - L - U$:

### Passo 1: Passada para Frente (Forward Pass)
Equivale a uma iteração exata do método SOR convencional. Para cada componente $i = 1, 2, \dots, n$:

$$x_i^{(k+1/2)} = (1 - \omega)x_i^{(k)} + rac{\omega}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1/2)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)} ight)$$

### Passo 2: Passada para Trás (Backward Pass)
Executa a mesma estratégia de relaxação, porém varrendo as variáveis na ordem inversa, de $i = n, n-1, \dots, 1$. Ela utiliza os valores recém-calculados no Passo 1 como o estado anterior:

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k+1/2)} + rac{\omega}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1/2)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k+1)} ight)$$

---

## 2. A Matriz de Pré-condicionamento SSOR

Quando $A$ é simétrica ($U = L^T$), a matriz do pré-condicionador SSOR, denotada por $M_{	ext{SSOR}}$, é definida de forma que sua aplicação seja computacionalmente eficiente por meio de substituições diretas:

$$M_{	ext{SSOR}} = rac{1}{\omega(2-\omega)} (D - \omega L) D^{-1} (D - \omega L^T)$$

### Vantagens do Pré-condicionador SSOR:
* **Simetria:** Ao contrário do SOR padrão, a matriz $M_{	ext{SSOR}}$ é **simétrica e definida positiva** (se $A$ também for), mantendo as propriedades necessárias para trabalhar em conjunto com o método de Gradientes Conjugados.
* **Custo computacional:** Não exige a inversão explícita de matrizes cheias; sua aplicação requer apenas uma substituição progressiva (*forward substitution*) e uma regressiva (*backward substitution*).

---

## 3. Comparação Direta de Métodos Iterativos

| Método | Passadas por Iteração | Mantém Simetria? | Aplicação Primária |
| :--- | :--- | :--- | :--- |
| **Gauss-Seidel** | 1 (Apenas para frente) | Não | Solver Direto / Suavizador |
| **SOR** | 1 (Apenas para frente com $\omega$) | Não | Solver Direto |
| **SSOR** | 2 (Para frente e para trás com $\omega$) | **Sim** | **Pré-condicionador para CG** |

---

## 4. Exemplo Numérico Prático

Considere o sistema simétrico $Ax = b$ com $\omega = 1.1$ e vetor inicial $x^{(0)} = [0, 0]^T$:

$$egin{bmatrix} 4 & 1 \ 1 & 3 \end{bmatrix} egin{bmatrix} x_1 \ x_2 \end{bmatrix} = egin{bmatrix} 5 \ 4 \end{bmatrix}$$

### Passo 1: Passada para Frente ($k=0 ightarrow k=1/2$)

* **Calcular $x_1^{(1/2)}$:**
  $$x_1^{(1/2)} = (1 - 1.1)x_1^{(0)} + rac{1.1}{4}(5 - 1 \cdot x_2^{(0)}) = -0.1(0) + rac{1.1}{4}(5 - 0) = 1.375$$

* **Calcular $x_2^{(1/2)}$:** (usa $x_1^{(1/2)}$ atualizado)
  $$x_2^{(1/2)} = (1 - 1.1)x_2^{(0)} + rac{1.1}{3}(4 - 1 \cdot x_1^{(1/2)}) = -0.1(0) + rac{1.1}{3}(4 - 1.375) = rac{1.1}{3}(2.625) pprox 0.9625$$

O vetor intermediário é $x^{(1/2)} = [1.375, \;\; 0.9625]^T$.

### Passo 2: Passada para Trás ($k=1/2 ightarrow k=1$)

* **Calcular $x_2^{(1)}$:** (varredura inversa começa por $i=2$, usa $x^{(1/2)}$ como base)
  $$x_2^{(1)} = (1 - 1.1)x_2^{(1/2)} + rac{1.1}{3}(4 - 1 \cdot x_1^{(1/2)}) = -0.1(0.9625) + 0.9625 = 0.86625$$

* **Calcular $x_1^{(1)}$:** (usa o $x_2^{(1)}$ que acabou de ser atualizado)
  $$x_1^{(1)} = (1 - 1.1)x_1^{(1/2)} + rac{1.1}{4}(5 - 1 \cdot x_2^{(1)}) = -0.1(1.375) + rac{1.1}{4}(5 - 0.86625) pprox -0.1375 + 1.13678 = 0.99928$$

Ao final da primeira iteração completa do SSOR, o vetor aproximado é **$x^{(1)} pprox [0.99928, \;\; 0.86625]^T$**.
