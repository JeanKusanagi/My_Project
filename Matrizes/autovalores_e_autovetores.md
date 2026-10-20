# Álgebra Linear: Autovalores, Autovetores e Transformações Geométricas

Este documento reúne a teoria e os exemplos práticos sobre **autovetores e autovalores**, incluindo o caso de matrizes com raízes reais e complexas, além da interpretação geométrica de magnitude e rotação.

---

## 1. Definição Teórica

Um **autovetor** é um vetor não nulo $v$ que, ao ser multiplicado por uma matriz quadrada $A$, muda apenas de tamanho (escala) e não de direção. O **autovalor** ($\lambda$) é o número escalar que representa esse fator de multiplicação.

A relação fundamental entre eles é expressa pela equação:
$$A \cdot v = \lambda \cdot v$$

### Conceitos Principais

* **Matriz Quadrada ($A$):** Os autovalores e autovetores só existem para matrizes que possuem o mesmo número de linhas e colunas ($n \times n$).
* **Autovetor ($v$):** É um vetor diferente do vetor nulo ($v \neq 0$). Se você aplicar a transformação da matriz nele, o resultado aponta para a mesma linha geométrica de antes.
* **Autovalor ($\lambda$):** É o fator de escala. Se $\lambda = 2$, o autovetor dobra de tamanho; se $\lambda = -1$, ele inverte o sentido; se $\lambda = 1$, ele permanece idêntico.
* **Equação Característica:** Para encontrar os autovalores, resolve-se o determinante da matriz subtraída de $\lambda$ vezes a matriz identidade $I$ igual a zero:
  $$\det(A - \lambda I) = 0$$
* **Encontrando o Autovetor:** Após achar cada valor de $\lambda$, substitui-se na equação $(A - \lambda I)v = 0$ para descobrir o vetor $v$ correspondente.

---

## 2. Exemplo Prático 1: Caso Real (Matriz $2 \times 2$)

Dada a matriz $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$, vamos encontrar seus autovalores e autovetores.

### Passo 1: Encontrar os Autovalores ($\lambda$)
Usamos a equação característica: $\det(A - \lambda I) = 0$.

$$A - \lambda I = \begin{pmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{pmatrix}$$

Calculando o determinante:
$$\det = (4 - \lambda)(3 - \lambda) - (1 \cdot 2) = 0$$
$$12 - 4\lambda - 3\lambda + \lambda^2 - 2 = 0$$
$$\lambda^2 - 7\lambda + 10 = 0$$

Resolvendo essa equação de 2º grau, encontramos as raízes:
* **$\lambda_1 = 5$**
* **$\lambda_2 = 2$**

### Passo 2: Encontrar os Autovetores ($v$)

#### Para $\lambda_1 = 5$:
$$\begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -x + y = 0 \implies x = y$$
Escolhendo $x = 1$, temos:
$$v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

#### Para $\lambda_2 = 2$:
$$\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies 2x + y = 0 \implies y = -2x$$
Escolhendo $x = 1$, temos:
$$v_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$$

---

## 3. Exemplo Prático 2: Caso Complexo

Dada a matriz $A = \begin{pmatrix} 1 & -2 \\ 3 & 4 \end{pmatrix}$, vamos calcular seus parâmetros.

### Passo 1: Encontrar os Autovalores ($\lambda$)
$$\det(A - \lambda I) = \det \begin{pmatrix} 1 - \lambda & -2 \\ 3 & 4 - \lambda \end{pmatrix} = 0$$
$$(1 - \lambda)(4 - \lambda) - (-2 \cdot 3) = 0$$
$$\lambda^2 - 5\lambda + 10 = 0$$

Aplicando a fórmula de Bhaskara ($\Delta = 25 - 40 = -15$):
* **$\lambda_1 = \frac{5}{2} + \frac{\sqrt{15}}{2}i \approx 2,5 + 1,93i$**
* **$\lambda_2 = \frac{5}{2} - \frac{\sqrt{15}}{2}i \approx 2,5 - 1,93i$**

### Passo 2: Encontrar os Autovetores ($v$)
Para $\lambda_1 = \frac{5}{2} + \frac{\sqrt{15}}{2}i$, substituímos na primeira linha do sistema:
$$\left(1 - \left(\frac{5}{2} + \frac{\sqrt{15}}{2}i\right)\right)x - 2y = 0 \implies y = \left(-\frac{3}{4} - \frac{\sqrt{15}}{4}i\right)x$$
Escolhendo $x = 4$:
$$v_1 = \begin{pmatrix} 4 \\ -3 - i\sqrt{15} \end{pmatrix}, \quad v_2 = \begin{pmatrix} 4 \\ -3 + i\sqrt{15} \end{pmatrix}$$

---

## 4. Magnitude e Ângulo de Rotação (Forma Polar)

Quando os autovalores são complexos, a matriz realiza uma transformação combinada de **expansão** e **rotação** no plano real. Transformamos $\lambda = a + bi$ para a forma polar:

### 1. Magnitude (Fator de Escala)
A magnitude ($r$) indica quanto o espaço é "esticado" a cada aplicação:
$$r = |\lambda| = \sqrt{a^2 + b^2}$$
$$r = \sqrt{\left(\frac{5}{2}\right)^2 + \left(rac{\sqrt{15}}{2}\right)^2} = \sqrt{\frac{25}{4} + \frac{15}{4}} = \sqrt{10} \approx 3,16$$

### 2. Ângulo de Rotação ($	heta$)
O ângulo indica quantos graus o espaço rotaciona (sentido anti-horário se positivo):
$$\theta = \arctan\left(\frac{b}{a}\right)$$
$$\theta = \arctan\left(\frac{\sqrt{15}}{5}\right) \approx \arctan(0,7746)$$
* **$\theta \approx 0,659 \text{ rad}$**
* **$\theta \approx 37,76^\circ$**

### Resumo Geométrico
Qualquer vetor no plano real submetido à matriz $A = \begin{pmatrix} 1 & -2 \\ 3 & 4 \end{pmatrix}$ será **rotacionado em $37,76^\circ$** e **expandido em $\sqrt{10} \approx 3,16$ vezes** o seu comprimento original.