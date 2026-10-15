# Fórmulas de métricas de avaliação de modelos

## 1. Métricas de classificação

Considere:

- **TP (True Positive):** verdadeiro positivo.
- **TN (True Negative):** verdadeiro negativo.
- **FP (False Positive):** falso positivo.
- **FN (False Negative):** falso negativo.

### Acurácia (*Accuracy*)

Proporção de predições corretas entre todas as predições:

$$
\[
\mathrm{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}
\]
$$

### Sensibilidade (*Sensitivity* ou *Recall*)

Proporção de exemplos positivos reais identificados corretamente:

$$
\[
\mathrm{Recall}=\frac{TP}{TP+FN}
\]
$$

### Especificidade (*Specificity*)

Proporção de exemplos negativos reais identificados corretamente:

$$
\[
\mathrm{Specificity}=\frac{TN}{TN+FP}
\]
$$

### Precisão (*Precision*)

Proporção de predições positivas que são realmente positivas:

$$
\[
\mathrm{Precision}=\frac{TP}{TP+FP}
\]
$$

### F1-score

Média harmônica entre precisão e recall:

$$
\[
F_1=2\frac{\mathrm{Precision}\cdot\mathrm{Recall}}
{\mathrm{Precision}+\mathrm{Recall}}
\]
$$

Forma equivalente, em função dos elementos da matriz de confusão:

$$
\[
F_1=\frac{2TP}{2TP+FP+FN}
\]
$$

## 2. Métricas de segmentação de imagens

Considere \(A\) a região segmentada pelo modelo e \(B\) a região de referência (*ground truth*).

### Dice

Mede a sobreposição entre a região predita e a região de referência:

$$
\[
\mathrm{Dice}=\frac{2|A\cap B|}{|A|+|B|}
\]
$$

Em termos de verdadeiros positivos, falsos positivos e falsos negativos:

$$
\[
\mathrm{Dice}=\frac{2TP}{2TP+FP+FN}
\]
$$

### Intersection over Union (IoU) ou índice de Jaccard

$$
\[
\mathrm{IoU}=\frac{|A\cap B|}{|A\cup B|}
\]
$$

Forma equivalente:

$$
\[
\mathrm{IoU}=\frac{TP}{TP+FP+FN}
\]
$$

Relação entre Dice e IoU:

$$
\[
\mathrm{Dice}=\frac{2\mathrm{IoU}}{1+\mathrm{IoU}}
\]
$$

$$
\[
\mathrm{IoU}=\frac{\mathrm{Dice}}{2-\mathrm{Dice}}
\]
$$

Ambas variam entre 0 e 1, sendo 1 o valor correspondente à sobreposição perfeita.

A Distância de Hausdorff (Hausdorff Distance) é uma métrica utilizada para medir a diferença entre dois conjuntos de pontos, considerando a maior distância entre um ponto de um conjunto e o ponto mais próximo do outro conjunto. É amplamente empregada em processamento de imagens, visão computacional, reconhecimento de padrões e avaliação de modelos de segmentação.

## 3. Métricas de regressão

Considere $\(y_i\)$ o valor real, $\(\hat{y}_i\)$ o valor predito, $\(\bar{y}\)$ a média dos valores reais e $\(n\)$ o número de amostras.

### Erro quadrático médio (MSE)

 MSE corresponde à média dos quadrados das diferenças entre os valores reais e os valores previstos. Como os erros são elevados ao quadrado, o método atribui maior penalização a erros elevados devido ao termo quadrático, tornando-se mais sensível à presença de outliers.

$$
\[
\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
\]
$$

### Raiz do Erro Quadrático Médio (RMSE)

O RMSE mede desvio padrão dos resíduos e preserva a unidade original da variável predita, facilitando a interpretação dos resultados.

$$
\[
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]
$$

### Erro absoluto médio (MAE)

O MAE mede o erro médio absoluto de forma mais robusta em relação a valores extremos quando comparado ao MSE.

$$
\[
\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]
$$

### Coeficiente de determinação (\(R^2\))

O $R^2$ uma medida estatística que indica o quão bem um modelo de regressão de regressão explica a variação dos dados observados (mede a proporção da variância da variável resposta explicada pelo modelo de regressão). Em geral, o R² assume valores entre 0 e 1, sendo que valores próximos de 1 indicam maior capacidade explicativa do modelo, enquanto valores próximos de 0 indicam que apenas uma pequena parcela da variância é explicada. O $\(R^2\)$ também pode assumir valores negativos quando o modelo apresenta desempenho inferior ao de uma previsão constante pela média, dependendo do procedimento de avaliação. O R² tende a aumentar, ou pelo menos não diminuir, à medida que novas variáveis são adicionadas ao modelo, mesmo quando elas possuem pouca ou nenhuma relevância preditiva. Para contornar essa limitação, utiliza-se o R² ajustado, que penaliza a inclusão de preditores desnecessários e, por isso, é mais apropriado para comparar modelos com diferentes quantidades de variáveis explicativas.

$$
\[
R^2=1-\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
{\sum_{i=1}^{n}(y_i-\bar{y})^2}
\]
$$

## 4. Métricas de reconstrução de imagens

### PSNR (*Peak Signal-to-Noise Ratio*)

$$
\[
\mathrm{PSNR}=10\log_{10}\left(\frac{MAX_I^2}{\mathrm{MSE}}\right)
\]
$$

Em que:

- $\(MAX_I\)$ é o valor máximo possível de intensidade dos pixels ou voxels.
- MSE é o erro quadrático médio entre a imagem de referência e a imagem reconstruída.

Para imagens com intensidade máxima igual a 1:

$$
\[
\mathrm{PSNR}=-10\log_{10}(\mathrm{MSE})
\]
$$

O resultado é expresso em decibéis (dB). Quanto maior o PSNR, menor o erro quadrático de reconstrução. Para imagens idênticas, o MSE é zero e o PSNR tende ao infinito.

### SSIM (*Structural Similarity Index*)

$$
\[
\mathrm{SSIM}(x,y)=
\frac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}
{(\mu_x^2+\mu_y^2+C_1)(\sigma_x^2+\sigma_y^2+C_2)}
\]
$$

Em que:

- $\(\mu_x\)$ e $\(\mu_y\)$ são as médias locais das intensidades das imagens.
- $\(\sigma_x^2\)$ e $\(\sigma_y^2\)$ são as variâncias locais.
- $\(\sigma_{xy}\)$ é a covariância entre as imagens.
- $\(C_1\)$ e $\(C_2\)$ são constantes de estabilização numérica.

Na formulação usual, valores próximos de 1 indicam maior similaridade estrutural; imagens idênticas apresentam SSIM igual a 1.

## 5. Métricas de processamento de linguagem natural

### BLEU (*Bilingual Evaluation Understudy*)

$$
\[
\mathrm{BLEU}=BP\cdot
\exp\left(\sum_{n=1}^{N}w_n\log p_n\right)
\]
$$

Em que:

- $\(p_n\)$ é a precisão modificada dos n-gramas de ordem \(n\).
- $\(w_n\)$ é o peso atribuído a cada ordem de n-grama, frequentemente $\(w_n=1/N\)$.
- $\(BP\)$ é a penalidade por brevidade (*Brevity Penalty*).

A penalidade por brevidade é definida por:

$$
\[
BP=
\begin{cases}
1, & c>r\\
e^{1-r/c}, & c\leq r
\end{cases}
\]
$$

Em que \(c\) é o comprimento do texto gerado e \(r\) é o comprimento de referência adotado no cálculo.

### ROUGE (*Recall-Oriented Understudy for Gisting Evaluation*)

O ROUGE possui diferentes variantes. Para o ROUGE-N, baseado na sobreposição de n-gramas, uma formulação usual é:

$$
\[
\mathrm{ROUGE\text{-}N}=
\frac{\sum_{g\in\mathcal{G}_N}
\min\bigl(\mathrm{Count}_{cand}(g),
\mathrm{Count}_{ref}(g)\bigr)}
{\sum_{g\in\mathcal{G}_N}\mathrm{Count}_{ref}(g)}
\]
$$

Em que:

- $\(\mathcal{G}_N\)$ é o conjunto de n-gramas.
- $\(\mathrm{Count}_{cand}(g)\)$ é a frequência do n-grama no texto gerado.
- $\(\mathrm{Count}_{ref}(g)\)$ é a frequência do n-grama no texto de referência.

Essa formulação representa a cobertura dos n-gramas da referência pelo texto gerado.

### Perplexidade (*Perplexity*)

Para uma sequência de tokens $\(w_1,w_2,\ldots,w_N\)$:

$$
\[
\mathrm{PPL}=
\exp\left(-\frac{1}{N}
\sum_{i=1}^{N}\log P(w_i\mid w_1,\ldots,w_{i-1})\right)
\]
$$

Em que \(P(w_i\mid w_1,\ldots,w_{i-1})\) é a probabilidade atribuída pelo modelo ao token atual, condicionada aos tokens anteriores.

A perplexidade corresponde à exponencial da entropia cruzada média quando se utiliza o logaritmo natural. Valores menores indicam melhor desempenho preditivo no conjunto avaliado, desde que os modelos sejam comparados sob condições equivalentes de tokenização e avaliação.

## 6. Métricas de detecção de objetos

### Average Precision (AP)

A AP corresponde à área sob a curva Precisão–Revocação. Uma formulação contínua comum é:

$$
\[
\mathrm{AP}=\int_0^1 p_{\mathrm{interp}}(r)\,dr
\]
$$

Em que \(p_{\mathrm{interp}}(r)\) é a precisão interpolada para o nível de revocação \(r\).

Na prática, a AP é calculada a partir de um conjunto discreto de predições ordenadas por confiança, podendo variar conforme o protocolo de avaliação.

### Mean Average Precision (mAP)

Para \(C\) classes avaliadas:

$$
\[
\mathrm{mAP}=\frac{1}{C}\sum_{c=1}^{C}\mathrm{AP}_c
\]
$$

Em conjuntos de dados como o COCO, utiliza-se frequentemente a média das APs em múltiplos limiares de IoU:

$$
\[
\mathrm{mAP}_{\mathrm{COCO}}=
\frac{1}{|\mathcal{T}|}
\sum_{t\in\mathcal{T}}\mathrm{mAP}_{t}
\]
$$

O conjunto usual de limiares é:

$$
\[
\mathcal{T}=\{0{,}50,0{,}55,\ldots,0{,}95\}
\]
$$

São, portanto, dez limiares de IoU entre 0,50 e 0,95, com incremento de 0,05.

## 7. Resumo das métricas

| Métrica | Objetivo principal | Direção desejável |
|---|---|---|
| Acurácia | Acertos totais | Maior |
| Sensibilidade / Recall | Identificação de positivos | Maior |
| Especificidade | Identificação de negativos | Maior |
| Precisão | Confiabilidade dos positivos preditos | Maior |
| F1-score | Equilíbrio entre precisão e recall | Maior |
| Dice | Sobreposição entre segmentações | Maior |
| IoU | Interseção relativa à união | Maior |
| MSE | Erro quadrático | Menor |
| MAE | Erro absoluto | Menor |
| $\(R^2\)$ | Variabilidade explicada pelo modelo | Geralmente maior |
| PSNR | Fidelidade da reconstrução | Maior |
| SSIM | Similaridade estrutural | Mais próximo de 1 |
| BLEU | Precisão de n-gramas | Maior |
| ROUGE | Cobertura de unidades da referência | Maior |
| Perplexidade | Qualidade preditiva probabilística | Menor |
| AP | Desempenho por classe em detecção | Maior |
| mAP | Desempenho médio entre classes e, quando aplicável, limiares de IoU | Maior |
