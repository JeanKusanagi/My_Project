# O Posto de uma Matriz

O posto (ou *rank*) de uma matriz é o número máximo de linhas ou colunas linearmente independentes que a compõem. Ele também pode ser entendido como o número de linhas não nulas após transformar a matriz em sua **forma escalonada**.

## Passo a passo para calcular o posto

1. **Aplique operações elementares nas linhas:**
   Utilize operações permitidas (trocar duas linhas de posição, multiplicar uma linha por um número diferente de zero ou somar/subtrair múltiplos de uma linha em outra).
2. **Transforme a matriz na forma escalonada:**
   O objetivo é criar zeros em todos os elementos abaixo da diagonal principal.
3. **Conte as linhas não nulas:**
   Após o escalonamento, conte quantas linhas sobraram que **não** possuem apenas zeros. Esse número é o posto da matriz.

---

## Exemplo prático

Dada a matriz A:

```
[ 1  2  3 ]
[ 2  4  5 ]
[ 3  6  8 ]
```

1. Subtraia 2 × (Linha 1) da Linha 2, e 3 × (Linha 1) da Linha 3 para zerar a primeira coluna abaixo do pivô:
   ```
   [ 1  2  3 ]
   [ 0  0 -1 ]
   [ 0  0 -1 ]
   ```

2. Subtraia a Linha 2 da Linha 3:
   ```
   [ 1  2  3 ]
   [ 0  0 -1 ]
   [ 0  0  0 ]
   ```

3. **Contagem:**
   A matriz escalonada possui **2 linhas não nulas** (a primeira e a segunda). Portanto, o posto da matriz A é **2**.