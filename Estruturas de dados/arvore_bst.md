# Árvore Binária de Busca (BST)

Este arquivo contém uma referência completa sobre a estrutura de dados **Árvore Binária de Busca** (BST - *Binary Search Tree*), incluindo conceitos, regras de inserção/remoção e implementação prática em Python.

---

## 1. Propriedade Fundamental
Uma BST é uma estrutura de dados hierárquica onde cada nó possui no máximo dois filhos. Para qualquer nó:
* **Subárvore Esquerda:** Contém apenas nós com valores **menores** que o nó atual.
* **Subárvore Direita:** Contém apenas nós com valores **maiores** que o nó atual.

---

## 2. Inserção (Visualização)
A inserção sempre adiciona um novo nó como uma **folha** (no final da árvore), seguindo a propriedade fundamental.

### Sequência de Inserção: `50, 30, 70, 20, 40`

```text
1. Inserir 50 (Árvore vazia, vira a raiz):
       50

2. Inserir 30 (30 < 50, vai para a esquerda):
       50
      /
    30

3. Inserir 70 (70 > 50, vai para a direita):
       50
      /  \
    30    70

4. Inserir 20 (20 < 50 -> 20 < 30, esquerda de 30):
       50
      /  \
    30    70
   /
  20

5. Inserir 40 (40 < 50 -> 40 > 30, direita de 30):
        50
       /  \
     30    70
    /  \
   20  40
```

---

## 3. Remoção (Os 3 Casos)

* **Caso 1: Nó Folha (Sem filhos)** -> O nó é simplesmente removido (ex: remover `20`).
* **Caso 2: Um Filho** -> O filho único "sobe" e assume a posição do nó pai deletado.
* **Caso 3: Dois Filhos** -> O nó é substituído pelo seu **sucessor em ordem** (o menor valor da subárvore direita) ou pelo seu **antecessor em ordem** (o maior valor da subárvore esquerda). O nó substituto original é então deletado.

---

## 4. Implementação Completa em Python

```python
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

def inserir(raiz, chave):
    if raiz is None:
        return No(chave)
    
    if chave < raiz.chave:
        raiz.esquerda = inserir(raiz.esquerda, chave)
    elif chave > raiz.chave:
        raiz.direita = inserir(raiz.direita, chave)
        
    return raiz

def menor_valor_no(no):
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

def remover(raiz, chave):
    if raiz is None:
        return raiz

    if chave < raiz.chave:
        raiz.esquerda = remover(raiz.esquerda, chave)
    elif chave > raiz.chave:
        raiz.direita = remover(raiz.direita, chave)
    else:
        # Caso 1 e 2: Sem filhos ou apenas 1 filho
        if raiz.esquerda is None:
            return raiz.direita
        elif raiz.direita is None:
            return raiz.esquerda

        # Caso 3: Dois filhos
        temp = menor_valor_no(raiz.direita)
        raiz.chave = temp.chave
        raiz.direita = remover(raiz.direita, temp.chave)

    return raiz

def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.chave, end=" ")
        em_ordem(raiz.direita)

# --- Exemplo de Uso ---
if __name__ == "__main__":
    raiz = None
    valores = [50, 30, 70, 20, 40]

    for val in valores:
        raiz = inserir(raiz, val)

    print("Árvore original (Em-Ordem):")
    em_ordem(raiz)  # Saída: 20 30 40 50 70

    print("\n\nRemovendo o 20 (Caso 1 - Nó Folha)...")
    raiz = remover(raiz, 20)
    em_ordem(raiz)

    print("\n\nRemovendo o 30 (Caso 2 - Um Filho)...")
    raiz = remover(raiz, 30)
    em_ordem(raiz)

    print("\n\nRemovendo o 50 (Caso 3 - Dois Filhos)...")
    raiz = remover(raiz, 50)
    em_ordem(raiz)
```
