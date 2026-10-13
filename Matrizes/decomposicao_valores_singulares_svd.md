# Decomposição em Valores Singulares (SVD)

A **Decomposição em Valores Singulares** (*Singular Value Decomposition — SVD*) é uma técnica de álgebra linear que permite decompor uma matriz em três matrizes: uma matriz ortogonal (ou unitária), uma matriz diagonal contendo os valores singulares e outra matriz ortogonal (ou unitária). Ela pode ser aplicada a qualquer matriz real ou complexa, inclusive matrizes retangulares e matrizes que não são invertíveis.

A SVD é amplamente utilizada em redução de dimensionalidade, compressão de imagens, processamento de sinais, análise de dados, sistemas de recomendação e aprendizado de máquina.

## 1. Definição matemática

Para uma matriz real \(A\) de dimensões \(m \times n\), a decomposição em valores singulares é dada por:

$$
\[
A = U\Sigma V^T
\]
$$

Em que:

- **\(A\):** matriz original, de dimensões \(m \times n\).
- **\(U\):** matriz ortogonal de dimensões \(m \times m\), cujas colunas são os vetores singulares à esquerda de \(A\).
- **\(\Sigma\):** matriz diagonal retangular de dimensões \(m \times n\), cujos elementos diagonais são os valores singulares de \(A\), normalmente ordenados em ordem decrescente.
- **\(V\):** matriz ortogonal de dimensões \(n \times n\), cujas colunas são os vetores singulares à direita de \(A\).
- **\($V^T$\):** transposta de \(V\).

As matrizes \(U\) e \(V\) são ortogonais, isto é, $\(U^TU=I\)$ e $\(V^TV=I\)$.

Os valores singulares são sempre não negativos e correspondem às raízes quadradas dos autovalores de $\(A^TA\)$. Equivalentemente, seus quadrados são os autovalores de $\(AA^T\)$, desconsiderando os valores adicionais iguais a zero que podem surgir devido às dimensões das matrizes.

## 2. Exemplo de decomposição em valores singulares

Considere a matriz:

$$
\[
A=\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}
\]
$$

Queremos encontrar sua decomposição em valores singulares, ou seja, determinar \(U\), \(\Sigma\) e \(V\).

### Etapa 1 — Calcular \(A^TA\)

Como \(A\) é uma matriz diagonal, temos \(A^T=A\). Portanto:

$$
\[
A^TA=
\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}
$$
$$
\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}
$$ = $$
\begin{bmatrix}
9&0\\
0&4
\end{bmatrix}
\]
$$

### Etapa 2 — Calcular os autovalores de $\(A^TA\)$

Os autovalores são obtidos resolvendo:

$$
\[
\det(A^TA-\lambda I)=0
\]
$$

Logo:

$$
\[
\begin{vmatrix}
9-\lambda&0\\
0&4-\lambda
\end{vmatrix}=0
\]
$$

$$
\[
(9-\lambda)(4-\lambda)=0
\]
$$

Assim, os autovalores são:

$$
\[
\lambda_1=9,\qquad \lambda_2=4
\]
$$

### Etapa 3 — Calcular os valores singulares

Os valores singulares são as raízes quadradas não negativas dos autovalores de \(A^TA\):

$$
\[
\sigma_i=\sqrt{\lambda_i}
\]
$$

Portanto:

$$
\[
\sigma_1=\sqrt{9}=3
\]
$$

$$
\[
\sigma_2=\sqrt{4}=2
\]
$$

A matriz \(\Sigma\) é:

$$
\[
\Sigma=
\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}
\]
$$

### Etapa 4 — Determinar \(U\) e \(V\)

Nesse exemplo, \(A\) é diagonal, simétrica e possui valores diagonais positivos. Podemos escolher \(U\) e \(V\) como matrizes identidade:

$$
\[
U=V=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\]
$$

Consequentemente, a decomposição é:

$$
\[
\boxed{
A=
\underbrace{\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}}_{U}
\underbrace{\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}}_{\Sigma}
\underbrace{\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}}_{V^T}
}
\]
$$

Nesse caso, a decomposição é particularmente simples porque \(A\) já está na forma diagonal.

## 3. Interpretação geométrica dos valores singulares

Uma matriz pode ser interpretada como uma transformação linear que modifica vetores. A SVD representa essa transformação como a composição de três operações:

1. **Rotação ou reflexão:** transformação associada a $\(V^T\)$.
2. **Escalonamento:** transformação realizada por \(\Sigma\), que estica ou comprime o espaço nas direções singulares.
3. **Rotação ou reflexão:** transformação associada a \(U\).

No exemplo, como \(U\) e \(V\) são matrizes identidade, não há rotação nem reflexão. A matriz simplesmente multiplica a primeira coordenada por 3 e a segunda por 2.

Os valores singulares indicam a intensidade do escalonamento em cada direção. Quanto maior o valor singular, maior o alongamento nessa direção.

## 4. Aplicações da SVD

### Redução de dimensionalidade

Na análise de componentes principais (PCA), a decomposição permite identificar direções importantes de variação dos dados. A SVD também pode ser aplicada diretamente aos dados centralizados para obter essas direções.

### Compressão de imagens

Uma matriz de imagem pode ser aproximada usando apenas os maiores valores singulares e seus vetores associados. Isso reduz a quantidade de informação necessária para representar a imagem, com alguma perda de qualidade.

### Sistemas de equações lineares

A SVD pode auxiliar na resolução de sistemas, inclusive quando a matriz é singular ou mal condicionada. A pseudoinversa calculada a partir da SVD permite obter soluções de mínimos quadrados e, em determinados casos, a solução de norma mínima.

### Aprendizado de máquina

Pode ser utilizada para redução de dimensionalidade, análise de matrizes de dados, filtragem de ruído e sistemas de recomendação.

## 5. Relação entre SVD, autovalores e norma matricial

A SVD possui uma relação importante com outros conceitos da álgebra linear:

- **Autovalores:** os quadrados dos valores singulares não nulos são os autovalores de \(A^TA\).
- **Posto da matriz:** o número de valores singulares não nulos corresponde ao posto de \(A\).
- **Norma espectral:** a norma 2 de \(A\) é igual ao maior valor singular, isto é, $\(\|A\|_2=\sigma_1\)$.
- **Norma de Frobenius:** o quadrado da norma de Frobenius é a soma dos quadrados de todos os valores singulares, isto é, $\(\|A\|_F^2=\sum_i \sigma_i^2\)$.

É importante destacar que, diferentemente da decomposição em autovalores, a SVD existe para qualquer matriz real ou complexa, mesmo que ela não seja quadrada ou diagonalizável.

## Síntese

A decomposição em valores singulares expressa uma matriz como \(A=U\Sigma V^T\). Ela permite identificar direções relevantes de transformação, medir a intensidade do escalonamento e construir aproximações de baixa dimensão. Por sua generalidade e estabilidade numérica, é uma das ferramentas fundamentais da álgebra linear numérica e da ciência de dados.
