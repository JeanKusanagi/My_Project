# Guia Completo da Árvore AVL: Conceitos, Exemplos Práticos e Códigos

Uma **Árvore AVL** é uma árvore binária de busca (BST) **auto-balanceada**. Ela foi criada por Adelson-Velskii e Landis em 1962 e garante que o tempo de execução para operações de busca, inserção e remoção permaneça eficiente mesmo no pior cenário.

---

## 1. Características Principais e Regras

* **Fator de Balanço (FB):** Para cada nó da árvore, a diferença de altura entre a subárvore esquerda e a subárvore direita deve ser no máximo **1** em módulo.
  $$FB = altura(esquerda) - altura(direita)$$
  A árvore estará balanceada se, para todos os nós, $FB \in \{-1, 0, 1\}$.
* **Garantia de Desempenho:** A altura máxima de uma árvore AVL com $n$ nós é limitada a cerca de $1.44 \times \log_2(n)$. Isso garante que o pior caso seja **$O(\log n)$**.

### Rotações para Rebalanceamento
Quando uma operação desbalanceia um nó ($FB = \pm 2$), aplicam-se rotações:
* **Simples à Direita (LL):** Inserção/remoção pesada à esquerda do filho esquerdo.
* **Simples à Esquerda (RR):** Inserção/remoção pesada à direita do filho direito.
* **Dupla à Direita (LR):** Inserção/remoção pesada à direita do filho esquerdo.
* **Dupla à Esquerda (RL):** Inserção/remoção pesada à esquerda do filho direito.

---

## 2. Análise de Complexidade

| Operação / Recurso | Melhor Caso | Caso Médio | Pior Caso |
| :--- | :--- | :--- | :--- |
| **Busca (Tempo)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **Inserção (Tempo)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **Remoção (Tempo)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **Espaço (Memória)** | $O(n)$ | $O(n)$ | $O(n)$ |
| **Espaço Auxiliar (Pilha)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |

---

## 3. Exemplo de inserção e remoção

### 📋 Conceito e Fator de Balanço
O **Fator de Balanço (FB)** determina se a árvore precisa ou não ser rebalanceada. Ele é calculado para cada nó da seguinte forma:

```unset
FB = altura(subárvore_esquerda) - altura(subárvore_direita)
```

*   **Árvore Balanceada:** -1 ≤ FB ≤ 1
*   **Árvore Desbalanceada:** FB = -2 ou FB = +2 (Exige rotação imediata)

---

### 📈 Exemplo Prático de Inserção

Iremos construir uma árvore inserindo a sequência de números: **10, 20, 30, 40 e 25**.

### Passo 1 --- Inserir 10

Como a árvore está vazia, `10` torna-se a raiz.

``` text
10
```

Fator de balanceamento:

-   `FB(10) = 0`

A árvore está balanceada.

### Passo 2 --- Inserir 20

Como `20 > 10`, o novo nó é inserido à direita de 10.

``` text
10
  \
   20
```

Fatores de balanceamento:

-   `FB(20) = 0`
-   `FB(10) = -1`

A árvore continua balanceada. Nenhuma rotação é necessária.

### Passo 3 --- Inserir 30

Como `30 > 10` e `30 > 20`, o novo nó é inserido à direita de 20.

Antes do balanceamento:

``` text
10
  \
   20
     \
      30
```

Fatores de balanceamento:

-   `FB(30) = 0`
-   `FB(20) = -1`
-   `FB(10) = -2`

O nó 10 está desbalanceado. A inserção ocorreu na subárvore direita do
filho direito, caracterizando o caso **RR (Right-Right)**.

**Correção: rotação simples à esquerda no nó 10.**

Após a rotação:

``` text
    20
   /  \
 10    30
```

Agora, os fatores de balanceamento dos três nós são iguais a zero.

### Passo 4 --- Inserir 40

Como `40 > 20` e `40 > 30`, o novo nó é inserido à direita de 30.

``` text
    20
   /  \
 10    30
         \
          40
```

Fatores de balanceamento:

-   `FB(10) = 0`
-   `FB(40) = 0`
-   `FB(30) = -1`
-   `FB(20) = -1`

A árvore continua balanceada. Nenhuma rotação é necessária.

### Passo 5 --- Inserir 25

A busca pela posição de inserção segue este caminho:

-   `25 > 20`: segue para a direita;
-   `25 < 30`: segue para a esquerda.

Assim, 25 é inserido como filho esquerdo de 30.

``` text
       20
      /  \
    10    30
         /  \
        25   40
```

Fatores de balanceamento:

-   `FB(10) = 0`
-   `FB(25) = 0`
-   `FB(40) = 0`
-   `FB(30) = 0`
-   `FB(20) = -1`

A árvore continua balanceada. Nenhuma rotação é necessária.

### Resultado após as inserções

``` text
       20
      /  \
    10    30
         /  \
        25   40
```

A única rotação realizada durante as inserções foi a rotação simples à
esquerda no nó 10, após a inserção de 30.

## Remoção do valor 30

Partimos da árvore:

``` text
       20
      /  \
    10    30
         /  \
        25   40
```

### Passo 1 --- Localizar o nó 30

O nó 30 possui dois filhos: 25 à esquerda e 40 à direita.

Quando um nó com dois filhos é removido de uma árvore binária de busca,
uma possibilidade é substituí-lo pelo seu **sucessor em ordem**, isto é,
o menor valor da sua subárvore direita.

Nesse caso, o sucessor em ordem de 30 é 40.

### Passo 2 --- Substituir 30 por 40

O valor 40 assume a posição de 30. O nó original 40 é então removido de
sua posição anterior.

``` text
       20
      /  \
    10    40
         /
        25
```

### Passo 3 --- Verificar o balanceamento

  Nó     Altura da esquerda   Altura da direita   FB
  ---- -------------------- ------------------- ----
  10                     -1                  -1    0
  25                     -1                  -1    0
  40                      0                  -1   +1
  20                      0                   1   -1

Todos os fatores estão no intervalo permitido, `[-1, +1]`.

Portanto, **nenhuma rotação é necessária**.

### Resultado após remover 30

``` text
       20
      /  \
    10    40
         /
        25
```

## 4. Remoção do valor 10

Agora partimos da árvore resultante da remoção de 30:

``` text
       20
      /  \
    10    40
         /
        25
```

### Passo 1 --- Localizar e remover o nó 10

O nó 10 é uma folha, pois não possui filhos. Portanto, basta removê-lo.

Após a remoção:

``` text
       20
         \
          40
         /
        25
```

### Passo 2 --- Verificar o balanceamento

  Nó     Altura da esquerda   Altura da direita   FB
  ---- -------------------- ------------------- ----
  25                     -1                  -1    0
  40                      0                  -1   +1
  20                     -1                   1   -2

O nó 20 está desbalanceado:

\[ FB(20) = -1 - 1 = -2 \]

Seu filho direito, o nó 40, apresenta:

\[ FB(40) = +1 \]

Como o nó desbalanceado está pesado à direita e seu filho direito está
pesado à esquerda, temos o caso **RL (Right-Left)**.

A correção exige uma rotação dupla: primeiro à direita no filho direito
e depois à esquerda no nó desbalanceado.

### Passo 3 --- Primeira rotação: rotação à direita no nó 40

A subárvore com raiz em 40 é rotacionada à direita. O nó 25 passa a
ocupar a posição de 40, e 40 torna-se seu filho direito.

``` text
    20
      \
       25
         \
          40
```

### Passo 4 --- Segunda rotação: rotação à esquerda no nó 20

Agora realizamos uma rotação à esquerda no nó 20. O nó 25 torna-se a
nova raiz da árvore.

``` text
       25
      /  \
    20    40
```

### Passo 5 --- Verificar o balanceamento final

  Nó     Altura da esquerda   Altura da direita   FB
  ---- -------------------- ------------------- ----
  20                     -1                  -1    0
  40                     -1                  -1    0
  25                      0                   0    0

Todos os nós estão balanceados.

### Resultado após remover 10

``` text
       25
      /  \
    20    40
```

A remoção de 10 provocou um desbalanceamento no nó 20, corrigido por uma
rotação dupla RL.

## 4. Resumo das operações

  -----------------------------------------------------------------------
  Operação                Situação                Balanceamento
  ----------------------- ----------------------- -----------------------
  Inserir 10              Criação da raiz         Nenhuma rotação

  Inserir 20              Inserção à direita de   Nenhuma rotação
                          10                      

  Inserir 30              Caso RR no nó 10        Rotação simples à
                                                  esquerda em 10

  Inserir 40              Inserção à direita de   Nenhuma rotação
                          30                      

  Inserir 25              Inserção à esquerda de  Nenhuma rotação
                          30                      

  Remover 30              Nó com dois filhos;     Nenhuma rotação
                          substituição pelo       
                          sucessor 40             

  Remover 10              Remoção de uma folha;   Rotação à direita em 40
                          caso RL no nó 20        e, depois, à esquerda
                                                  em 20
  -----------------------------------------------------------------------

## 5. Os quatro casos de desbalanceamento AVL

  -----------------------------------------------------------------------
  Caso                    Onde ocorre a inserção  Rotação corretiva
                          (ou o aumento de        
                          altura)                 
  ----------------------- ----------------------- -----------------------
  LL (Left-Left)          Subárvore esquerda do   Simples à direita
                          filho esquerdo          

  RR (Right-Right)        Subárvore direita do    Simples à esquerda
                          filho direito           

  LR (Left-Right)         Subárvore direita do    Dupla: esquerda no
                          filho esquerdo          filho e direita no nó
                                                  desbalanceado

  RL (Right-Left)         Subárvore esquerda do   Dupla: direita no filho
                          filho direito           e esquerda no nó
                                                  desbalanceado
  -----------------------------------------------------------------------

**Observação:** durante uma remoção, o desbalanceamento pode propagar-se
para os ancestrais. Por isso, pode ser necessário realizar rotações em
mais de um nível da árvore.

## 6. Complexidade

Em uma árvore AVL, a altura é `O(log n)`. Consequentemente, as operações
de busca, inserção e remoção possuem complexidade de tempo:

\[ `\boxed{O(\log n)}`{=tex} \]

As rotações são operações locais e possuem custo `O(1)` cada. O custo
total da atualização permanece `O(log n)`, pois pode ser necessário
percorrer o caminho entre o nó alterado e a raiz.
---

## 7. Implementação Completa em Python

Este script implementa a árvore AVL com todas as operações (inserção, remoção, busca, percursos, contagem de nós, busca por mínimos/máximos e folhas), incluindo um menu interativo via terminal.

```python
import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print(f"\n⚠️ O valor {key} já existe na árvore!")
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def get_max_value_node(self, node):
        if node is None or node.right is None:
            return node
        return self.get_max_value_node(node.right)

    def delete(self, root, key):
        if not root:
            print(f"\n❌ O valor {key} não foi encontrado.")
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(f"{root.key}", end=" ")
            self.in_order(root.right)

    def pre_order(self, root):
        if root:
            print(f"{root.key}(H={root.height})", end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(f"{root.key}", end=" ")

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def calculate_height_direct(self, root):
        if root is None:
            return 0
        return 1 + max(self.calculate_height_direct(root.left), self.calculate_height_direct(root.right))

    def print_leaves(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.key, end=" ")
            return
        self.print_leaves(root.left)
        self.print_leaves(root.right)

def menu():
    tree = AVLTree()
    root = None

    while True:
        print("\n==============================")
        print("      MENU ÁRVORE AVL (PYTHON)")
        print("==============================")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Buscar elemento")
        print("4. Mostrar Percursos e Estatísticas")
        print("5. Sair")
        print("==============================")
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            try:
                val = int(input("Digite o valor para inserir: "))
                root = tree.insert(root, val)
            except ValueError:
                print("⚠️ Digite um número inteiro válido.")
        elif opcao == "2":
            try:
                val = int(input("Digite o valor para remover: "))
                root = tree.delete(root, val)
            except ValueError:
                print("⚠️ Digite um número inteiro válido.")
        elif opcao == "3":
            try:
                val = int(input("Digite o valor para buscar: "))
                res = tree.search(root, val)
                if res:
                    print(f"🔍 Encontrado! Altura do nó: {res.height}")
                else:
                    print("❌ Elemento não existe na árvore.")
            except ValueError:
                print("⚠️ Digite um número inteiro válido.")
        elif opcao == "4":
            if not root:
                print("Árvore vazia.")
            else:
                print("\n--- PERCURSOS ---")
                print("Em Ordem:  ", end=""); tree.in_order(root); print()
                print("Pré-Ordem: ", end=""); tree.pre_order(root); print()
                print("Pós-Ordem: ", end=""); tree.post_order(root); print()
                print(f"\nTotal de nós: {tree.count_nodes(root)}")
                print(f"Altura Máxima (Direta): {tree.calculate_height_direct(root)}")
                print(f"Mínimo: {tree.get_min_value_node(root).key} | Máximo: {tree.get_max_value_node(root).key}")
                print("Nós Folha: ", end=""); tree.print_leaves(root); print()
        elif opcao == "5":
            break
        else:
            print("⚠️ Opção inválida.")

if __name__ == "__main__":
    menu()
```

---

## 8. Implementação Completa em C

Esta versão em C gerencia ponteiros, desalocação de memória dinamicamente no encerramento do programa e oferece o mesmo menu interativo.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    struct Node *left;
    struct Node *right;
    int height;
} Node;

int max(int a, int b) {
    return (a > b) ? a : b;
}

int getHeight(Node *n) {
    if (n == NULL) return 0;
    return n->height;
}

Node* createNode(int key) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (!node) {
        printf("Erro de memória!\n");
        exit(1);
    }
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
    return node;
}

int getBalance(Node *n) {
    if (n == NULL) return 0;
    return getHeight(n->left) - getHeight(n->right);
}

Node *rotateRight(Node *y) {
    Node *x = y->left;
    Node *T2 = x->right;
    x->right = y;
    y->left = T2;
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    return x;
}

Node *rotateLeft(Node *x) {
    Node *y = x->right;
    Node *T2 = y->left;
    y->left = x;
    x->right = T2;
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
    return y;
}

Node* insert(Node* node, int key) {
    if (node == NULL) return createNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else {
        printf("\n⚠️ O valor %d já existe na árvore!\n", key);
        return node;
    }

    node->height = 1 + max(getHeight(node->left), getHeight(node->right));
    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key) return rotateRight(node);
    if (balance < -1 && key > node->right->key) return rotateLeft(node);
    if (balance > 1 && key > node->left->key) {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }
    if (balance < -1 && key < node->right->key) {
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }
    return node;
}

Node* getMinValueNode(Node* node) {
    Node* current = node;
    while (current && current->left != NULL) current = current->left;
    return current;
}

Node* getMaxValueNode(Node* node) {
    Node* current = node;
    while (current && current->right != NULL) current = current->right;
    return current;
}

Node* deleteNode(Node* root, int key) {
    if (root == NULL) {
        printf("\n❌ Valor %d não encontrado.\n", key);
        return root;
    }

    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    else {
        if ((root->left == NULL) || (root->right == NULL)) {
            Node *temp = root->left ? root->left : root->right;
            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else {
                *root = *temp;
            }
            free(temp);
        } else {
            Node* temp = getMinValueNode(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }

    if (root == NULL) return root;

    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    int balance = getBalance(root);

    if (balance > 1 && getBalance(root->left) >= 0) return rotateRight(root);
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }
    if (balance < -1 && getBalance(root->right) <= 0) return rotateLeft(root);
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }
    return root;
}

Node* search(Node* root, int key) {
    if (root == NULL || root->key == key) return root;
    if (key < root->key) return search(root->left, key);
    return search(root->right, key);
}

void inOrder(Node *root) {
    if (root) { inOrder(root->left); printf("%d ", root->key); inOrder(root->right); }
}

void preOrder(Node *root) {
    if (root) { printf("%d(H=%d) ", root->key, root->height); preOrder(root->left); preOrder(root->right); }
}

void postOrder(Node *root) {
    if (root) { postOrder(root->left); postOrder(root->right); printf("%d ", root->key); }
}

int countNodes(Node* root) {
    if (root == NULL) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

int calculateHeightDirect(Node* root) {
    if (root == NULL) return 0;
    return 1 + max(calculateHeightDirect(root->left), calculateHeightDirect(root->right));
}

void printLeaves(Node* root) {
    if (root == NULL) return;
    if (root->left == NULL && root->right == NULL) { printf("%d ", root->key); return; }
    printLeaves(root->left);
    printLeaves(root->right);
}

void freeTree(Node* root) {
    if (root) { freeTree(root->left); freeTree(root->right); free(root); }
}

int main() {
    Node *root = NULL;
    int opcao, valor;

    while (1) {
        printf("\n==============================\n");
        printf("      MENU ÁRVORE AVL (C)\n");
        printf("==============================\n");
        printf("1. Inserir elemento\n");
        printf("2. Remover elemento\n");
        printf("3. Buscar elemento\n");
        printf("4. Mostrar Percursos e Estatísticas\n");
        printf("5. Sair\n");
        printf("==============================\n");
        printf("Escolha uma opção: ");

        if (scanf("%d", &opcao) != 1) {
            printf("⚠️ Entrada inválida.\n");
            while (getchar() != '\n');
            continue;
        }

        switch (opcao) {
            case 1:
                printf("Valor para inserir: "); scanf("%d", &valor);
                root = insert(root, valor); break;
            case 2:
                printf("Valor para remover: "); scanf("%d", &valor);
                root = deleteNode(root, valor); break;
            case 3:
                printf("Valor para buscar: "); scanf("%d", &valor);
                Node* res = search(root, valor);
                if (res) printf("🔍 Encontrado (Altura: %d).\n", res->height);
                else printf("❌ Não existe.\n");
                break;
            case 4:
                if (!root) { printf("Árvore vazia.\n"); }
                else {
                    printf("\n--- PERCURSOS ---\n");
                    printf("Em Ordem:  "); inOrder(root); printf("\n");
                    printf("Pré-Ordem: "); preOrder(root); printf("\n");
                    printf("Pós-Ordem: "); postOrder(root); printf("\n");
                    printf("\nTotal de nós: %d\n", countNodes(root));
                    printf("Altura Máxima (Direta): %d\n", calculateHeightDirect(root));
                    printf("Mínimo: %d | Máximo: %d\n", getMinValueNode(root)->key, getMaxValueNode(root)->key);
                    printf("Nós Folha: "); printLeaves(root); printf("\n");
                }
                break;
            case 5:
                freeTree(root); return 0;
            default:
                printf("⚠️ Opção inválida.\n");
        }
    }
}
```

---

## 9. Exemplo Prático de Inserção

Iremos construir uma árvore inserindo sequencialmente a lista de números: `[10, 20, 30, 40, 50, 25]`.

### Passo 1: Inserir 10
Raiz inicial da árvore.
```text
  10 (FB=0)
```

### Passo 2: Inserir 20
Como $20 > 10$, vai para a direita.
```text
  10 (FB=-1)
    \
     20 (FB=0)
```

### Passo 3: Inserir 30 $\rightarrow$ Rotação Simples à Esquerda (RR)
O número 30 vai para a direita do 20. O nó 10 fica com $\text{FB} = -2$ (Peso à direita).
```text
    10                        20 (FB=0)
      \       Rotação        /  \
       20     --->         10    30
         \                (FB=0) (FB=0)
          30
```

### Passo 4: Inserir 40
O número 40 vai para a direita do 30.
```text
      20 (FB=-1)
     /  \
   10    30 (FB=-1)
           \
            40 (FB=0)
```

### Passo 5: Inserir 50 $\rightarrow$ Rotação Simples à Esquerda (RR)
O número 50 vai para a direita do 40. O nó 30 fica com $\text{FB} = -2$. Aplicamos a rotação simples à esquerda no nó 30.
```text
      20                      20 (FB=-1)
     /  \                    /  \
   10    30                 10   40 (FB=0)
           \      --->          /  \
            40                30    50
              \             (FB=0) (FB=0)
               50
```

### Passo 6: Inserir 25 $\rightarrow$ Rotação Dupla à Esquerda (RL)
O número 25 navega na árvore até a esquerda do 30. A raiz principal 20 fica com $\text{FB} = -2$ (peso à direita), enquanto seu filho 40 possui $\text{FB} = +1$ (peso à esquerda). Sinais invertidos exigem rotação dupla:
1. Rotação Simples à Direita no nó filho (40).
2. Rotação Simples à Esquerda no nó raiz desbalanceado (20).

```text
      20 (FB=-2)                    30 (FB=0)
     /  \                          /  \
   10    40                      20    40
        /  \         --->       /  \     \
       30   50                10   25     50
      /
     25
```

---

## 10. Passo a Passo Prático: Remoção Standard

Trabalhando sobre o resultado final obtido na inserção, simulamos três cenários comuns de remoção.

### Caso A: Remoção de um Nó Folha
Ao remover o nó **25** (que não possui nenhum filho), a remoção é direta. O nó pai (20) passa a ter $\text{FB} = +1$. Como está dentro do limite $[-1, 1]$, nenhuma rotação é necessária.
```text
        30 (FB=0)
       /  \
     20    40
    /        \
  10          50
```

### Caso B: Remoção Gerando Desbalanceamento (Rotação Simples)
A partir da estrutura anterior, removemos o nó **10**.
O nó pai (20) fica sem filhos. O cálculo do fator de balanço na raiz **30** acusa desvio crítico: $\text{FB} = 0 - 2 = -2$. Como seu filho da direita (40) possui $\text{FB} = -1$, fazemos uma **Rotação Simples à Esquerda** trazendo o 40 para o topo.
```text
        30 (FB=-2)                    40 (FB=0)
       /  \                          /  \
     20    40         --->         30    50
             \                    /
              50                 20
```

### Caso C: Remoção de Nó com Dois Filhos
Removendo o nó raiz **40**.  
Para remover um elemento com dois filhos, substituímos seu valor pelo **antecessor em-ordem** (o maior elemento da subárvore esquerda, que é o **30**) ou pelo **sucessor em-ordem** (o menor da direita, que seria o **50**). Escolhendo o antecessor 30:
1. Copiamos o valor 30 para o lugar do 40.
2. Apagamos o nó 30 antigo da sua posição original, fazendo o 20 subir.
```text
        30 (FB=0)
       /  \
     20    50
```

---

## 11. Cenário Complexo: Remoção Provocando Rotação Dupla

Este cenário demonstra um caso avançado onde a retirada de um nó cria uma quebra na árvore estruturada em "zigue-zague", ativando um rebalanceamento de dois passos.

### Estrutura Inicial Base
Partimos de uma nova árvore AVL com os nós `[30, 15, 40, 10, 35, 45]`:
```text
        30 (FB=0)
       /  \
     15    40 (FB=1)
    /     /  \
   10    35   45
```

### Etapa 1: Remoção do nó folha 10
O nó **10** é deletado diretamente da folha esquerda.  
* O nó 15 passa a ter altura 1.
* A raiz **30** passa a ter $\text{FB} = 1 - 2 = -1$ (Ainda balanceada).
```text
        30 (FB=-1)
       /  \
     15    40 (FB=1)
          /  \
        35    45
```

### Etapa 2: Remoção do nó 15 $\rightarrow$ Desbalanceamento Crítico!
Removemos o nó **15**. Agora, a subárvore esquerda da raiz perde toda a sua altura (torna-se 0).
* O nó raiz **30** agora tem $\text{FB} = 0 - 2 = -2$. **Árvore desbalanceada à direita!**
* Analisamos o filho da direita (**40**): ele possui $\text{FB} = +1$, o que significa que o seu peso acumulado está apontado para o lado interno (**para a esquerda, no nó 35**).

```text
        30 (FB=-2)  <-- Erro crítico (Esquerda vazia)
          \
           40 (FB=1)  <-- Filho com sinal contrário (Peso interno)
          /  \
        35    45
```

Como os sinais estão trocados (Raiz $-2$ e Filho $+1$), o algoritmo classifica como um caso **Direita-Esquerda (RL)**, exigindo uma **Rotação Dupla à Esquerda**.

### Etapa 3: Execução da Rotação Dupla

#### Sub-passo A: Rotação Simples à Direita no nó filho (40)
O nó **35** rotaciona para cima, assumindo o papel de filho direito da raiz 30. O nó 40 desce virando seu filho direito.
```text
        30
          \
           35
             \
              40
                \
                 45
```

#### Sub-passo B: Rotação Simples à Esquerda no nó raiz (30)
O nó **35** rotaciona novamente, desta vez subindo para o topo absoluto da árvore. O antigo nó raiz (30) desce para a sua esquerda.

```text
        35 (FB=0)
       /  \
     30    40 (FB=-1)
             \
              45
```

A árvore foi rebalanceada com sucesso e voltou a respeitar todas as restrições AVL, mantendo os fatores de balanço estáveis e a busca eficiente em tempo logarítmico.
