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

Vamos construir uma árvore inserindo a sequência de números: **10, 20, 30, 40 e 25**.

#### 1. Inserir 10
Primeiro elemento torna-se a raiz.
*   **FB(10):** 0 - 0 = 0 (Balanceado)
```text
  10 (FB: 0)
```

#### 2. Inserir 20
20 é maior que 10, entra à direita.
*   **FB(20):** 0
*   **FB(10):** 0 - 1 = -1 (Balanceado)
```text
  10 (FB: -1)
    \
    20 (FB: 0)
```

#### 3. Inserir 30 (Gera Rotação Simples à Esquerda)
30 entra à direita de 20.
*   **FB(30):** 0
*   **FB(20):** 0 - 1 = -1
*   **FB(10):** 0 - 2 = **-2** 🔴 *Desbalanceado!*
```text
      10 (FB: -2)
        \
        20
          \
          30
```
**Solução (Caso RR):** Rotação Simples à Esquerda no nó 10. O nó 20 sobe para a raiz.
```text
    20 (FB: 0)
   /  \
 10    30  (Ambos FB: 0)
```

#### 4. Inserir 40
40 entra à direita de 30.
*   **FB(40):** 0
*   **FB(30):** 0 - 1 = -1
*   **FB(20):** 1 - 2 = -1 (Balanceado)
```text
      20 (FB: -1)
     /  \
   10    30 (FB: -1)
           \
           40 (FB: 0)
```

#### 5. Inserir 25 (Gera Rotação Dupla à Esquerda)
25 entra à esquerda de 30.
*   **FB(25):** 0
*   **FB(30):** 1 - 1 = 0
*   **FB(20):** 1 - 3 = **-2** 🔴 *Desbalanceado!*
```text
        20 (FB: -2)
       /  \
     10    30
          /  \
        25    40
```
**Solução (Caso RL):** Rotação Dupla à Esquerda no nó 20 (Primeiro rotaciona 30 à direita, depois 20 à esquerda). O nó 25 sobe para a raiz.
```text
        25 (FB: 0)
       /  \
     20    30
    /        \
  10          40
```

---

### 📉 Exemplo Prático de Remoção

Partindo da árvore final obtida acima, faremos a **remoção do nó 30**.

### 1. Remover o Nó 30
O número 30 é um nó folha, logo é removido diretamente.
```text
        25 
       /  \
     20    [Vazio]
    /        
  10          
```

#### 2. Recálculo e Rebalanceamento
Análise dos fatores de balanço de baixo para cima após a perda do nó direito:
*   **FB(10):** 0
*   **FB(20):** 1 - 0 = 1
*   **FB(25):** 2 - 0 = **+2** 🔴 *Desbalanceado!*
```text
        25 (FB: +2)
       /
     20 (FB: 1)
    /
  10 (FB: 0)
```
**Solução (Caso LL):** Rotação Simples à Direita no nó 25. O nó 20 assume a raiz.

#### 🌳 Configuração Final da Árvore:
```text
    20 (FB: 0)
   /  \
 10    25 (Ambos FB: 0)
```

---

## 4. Implementação Completa em Python

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

## 4. Implementação Completa em C

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
