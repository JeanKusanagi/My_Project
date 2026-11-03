# Árvore Rubro-Negra (Red-Black Tree)
Este arquivo contém a especificação teórica, a prova matemática de complexidade e as implementações em Python e C++ para uma Árvore Rubro-Negra completa.

---

## 1. 🛑 Regras Fundamentais e Características
Uma árvore rubro-negra é uma árvore binária de busca auto-balanceada onde cada nó possui um bit extra de armazenamento que define sua cor: **Vermelho** ou **Preto**. Para garantir o balanço estrutural, ela obrigatoriamente segue as seguintes regras:
1. Todo nó é ou vermelho ou preto.
2. A raiz é sempre preta.
3. Todas as folhas (nós nulos ou `NIL`) são pretas.
4. Se um nó é vermelho, então ambos os seus filhos são pretos (não há nós vermelhos consecutivos).
5. Para cada nó, todos os caminhos simples dele até as folhas descendentes contêm o mesmo número de nós pretos (altura negra).

---

## 2. Prova Matemática da Altura Máxima: $h \le 2 \log_2(n + 1)$

### Definições:
* $h(x)$: Altura total do nó $x$ (número de arestas até a folha mais distante).
* $bh(x)$: Altura negra (*black height*) de $x$ (número de nós pretos do caminho de $x$ até as folhas, excluindo o próprio $x$ e incluindo as folhas $NIL$).

### Passo 1: Limitação da Altura pela Altura Negra
Devido à regra que proíbe nós vermelhos consecutivos, pelo menos metade dos nós em qualquer caminho da raiz até uma folha deve ser preta. Assim:
$$bh(\text{raiz}) \ge \frac{h}{2} \implies h \le 2 \cdot bh(\text{raiz})$$

### Passo 2: Lema da Quantidade Mínima de Nós Internos
**Lema:** *A subárvore enraizada em qualquer nó $x$ contém pelo menos $2^{bh(x)} - 1$ nós internos.*

**Prova por Indução sobre a altura de $x$:**
* **Base (altura = 0):** Se $x$ é uma folha ($NIL$), sua altura negra $bh(x) = 0$. O número de nós internos é $0$. Pela fórmula: $2^0 - 1 = 0$. Válido.
* **Passo Indutivo:** Considere um nó interno $x$ com altura positiva e dois filhos. Cada filho possui altura menor que $x$. 
  Se um filho for vermelho, sua altura negra é igual à de $x$. Se for preto, sua altura negra é $bh(x) - 1$. Portanto, a altura negra de qualquer filho é no mínimo $bh(x) - 1$.
  Pela hipótese de indução, cada filho tem pelo menos $2^{bh(x) - 1} - 1$ nós internos.
  O total de nós internos da subárvore de $x$ é a soma dos nós dos filhos mais o próprio $x$:
  $$\text{Nós internos}(x) \ge (2^{bh(x) - 1} - 1) + (2^{bh(x) - 1} - 1) + 1$$
  $$\text{Nós internos}(x) \ge 2 \cdot (2^{bh(x) - 1}) - 2 + 1 = 2^{bh(x)} - 1$$
O lema está provado.

### Passo 3: Conclusão Logarítmica
Aplicando o lema para a raiz da árvore onde $n$ é o total de nós internos:
$$n \ge 2^{bh(\text{raiz})} - 1 \implies n + 1 \ge 2^{bh(\text{raiz})}$$
$$\log_2(n + 1) \ge bh(\text{raiz})$$
Substituindo $bh(\text{raiz}) \ge \frac{h}{2}$:
$$\log_2(n + 1) \ge \frac{h}{2} \implies h \le 2 \log_2(n + 1)$$

---

## Exemplo de inserção e remoção

### 🛠️ Funcionamento da Inserção
Todo novo nó é inserido inicialmente como **Vermelho (V)**. Se o pai do novo nó também for vermelho, ocorre uma violação que é corrigida avaliando a cor do **tio** (irmão do pai):

*   **Caso 1: O Tio é Vermelho (Recoloração)**
    *   *Ação:* Pai e Tio viram **Pretos**. Avô vira **Vermelho** (e a verificação sobe para o avô).
*   **Caso 2: O Tio é Preto e forma "Ziguezague"**
    *   *Ação:* Rotação simples no Pai na direção oposta ao novo nó para alinhá-los em linha reta.
*   **Caso 3: O Tio é Preto e forma "Linha Reta"**
    *   *Ação:* Rotação no Avô na direção oposta ao Pai. Inverte as cores do antigo Avô e do antigo Pai.

---

### 🛠️ Funcionamento da Remoção

Se excluirmos um nó **vermelho**, nenhuma propriedade da árvore é violada. O problema real ocorre quando removemos um nó **preto**, pois isso altera a altura negra da árvore (Regra 5), criando um desbalanceamento conhecido como **"duplo preto"** (o nó substituto fica com um "peso" preto a mais para compensar a perda).

Para eliminar esse duplo preto, analisamos a cor do **irmão (I)** do nó substituto e dos **filhos desse irmão**.

#### Os 4 Casos Principais de Correção
Considere que **X** é o nó com o duplo preto, **P** é o pai de X, **I** é o irmão de X, e **E** e **D** são os filhos esquerdo e direito de I, respectivamente. Assumiremos que X é o filho esquerdo de P.

#### Caso 1: O Irmão (I) é Vermelho
* **Condição:** I é vermelho. Isso implica que P, E e D devem ser pretos.
* **Ação:**
  * Inverta as cores de P e I (P vira vermelho, I vira preto).
  * Faça uma **rotação à esquerda no pai (P)**.
* **Efeito:** X continua duplo preto, mas agora ele ganhou um novo irmão que é preto. Isso transforma a situação em um dos casos seguintes (2, 3 ou 4).

```text
      P (Preto)                     I (Preto)
     / \                           / \
  X(DB) I (Verm)     ======>      P (Verm)  D (Preto)
       / \                       / \
      E   D                     X(DB) E
```

#### Caso 2: O Irmão (I) e seus Filhos (E, D) são Pretos
* **Condição:** I é preto, e ambos os seus filhos (E e D) também são pretos.
* **Ação:**
  * Remova um "preto" de X (ele vira preto normal) e um "preto" de I (ele vira vermelho).
  * Passe o "preto extra" para o pai (P).
* **Efeito:** Se P era vermelho, ele vira preto normal e o algoritmo **termina**. Se P já era preto, ele se torna o novo nó "duplo preto", e o algoritmo continua subindo na árvore.

```text
      P (Qualquer)                  P (Qualquer + Preto) <-- Novo foco
     / \                           / \
  X(DB) I (Preto)    ======>     X (Preto) I (Verm)
       / \                            / \
    E(Pr) D(Pr)                    E(Pr) D(Pr)
```

#### Caso 3: O Irmão (I) é Preto, o Filho Distante (D) é Preto, mas o Próximo (E) é Vermelho
* **Condição:** I é preto, D é preto, mas E é vermelho (um "triângulo").
* **Ação:**
  * Inverta as cores de I e E (I vira vermelho, E vira preto).
  * Faça uma **rotação à direita no irmão (I)**.
* **Efeito:** O duplo preto X continua no mesmo lugar, mas essa manobra transforma a estrutura no Caso 4.

```text
      P (Qualquer)                  P (Qualquer)
     / \                           / \
  X(DB) I (Preto)    ======>     X(DB) E (Preto)
       / \                            \
   E(Verm) D(Pr)                       I (Verm)
                                        \
                                        D(Pr)
```

#### Caso 4: O Irmão (I) é Preto e o Filho Distante (D) é Vermelho
* **Condição:** I é preto e D é vermelho (uma "linha"). O filho E pode ser de qualquer cor.
* **Ação:**
  * I assume a cor atual do pai (P).
  * P vira preto e D vira preto.
  * Faça uma **rotação à esquerda no pai (P)**.
* **Efeito:** O duplo preto de X é completamente eliminado. A árvore fica perfeitamente balanceada e o algoritmo **termina**.

```text
      P (Qualquer)                  I (Cor antiga de P)
     / \                           / \
  X(DB) I (Preto)    ======>     P(Preto)  D (Preto)
         \                      / \
        D(Verm)                X   E
```

---

### Resumo Visual da Remoção (Fluxograma)
```text
O nó removido/substituído era PRETO?
   │
   ├── Não ──> Fim (Não quebra nenhuma regra)
   │
   └── Sim ──> Nó atual vira Duplo Preto (DB). Analisar o Irmão (I):
        │
        ├── I é Vermelho ──> Caso 1: Rotaciona o Pai, atualiza cores ──> Reavalia
        │
        └── I é Preto:
             │
             ├── Filhos de I são Pretos ──> Caso 2: Puxa o preto para o Pai ──> Sobe na árvore
             │
             ├── Filho oposto é Preto, filho próximo é Vermelho ──> Caso 3: Rotaciona Irmão ──> Vai para Caso 4
             │
             └── Filho oposto é Vermelho ──> Caso 4: Rotaciona o Pai, ajusta cores ──> Perfeito / Fim
```

---
### 🔄 Exemplo Prático Passo a Passo

#### 1. Inserção dos elementos: 10, 20, 30, 15

#### Passo A: Inserir 10
Torna-se a raiz. Pela regra 2, vira preto.
```text
  10(P)
```

##### Passo B: Inserir 20
Inserido à direita de 10 como vermelho. Nenhuma regra violada.
```text
  10(P)
        20(V)
```

##### Passo C: Inserir 30
Inserido à direita de 20. Conflito de vermelhos (20 e 30). Tio é `NIL` (preto) em linha reta. Rotação à esquerda no avô (10) e recoloração.
```text
      20(P)
     /      10(V)   30(V)
```

##### Passo D: Inserir 15
Inserido à direita de 10. Conflito de vermelhos (10 e 15). Tio (30) é vermelho. Recoloração do pai (10) e do tio (30) para preto. O avô (20) tenta virar vermelho, mas permanece preto por ser a raiz.
```text
      20(P)
     /      10(P)   30(P)
        15(V)
```

---

#### 2. Remoção do elemento: 20

#### Passo A: Substituição pelo sucessor
O nó 20 (raiz) é substituído pelo seu sucessor imediato (30). O nó original 30 vira uma folha `NIL`.
```text
      30(P) 
     /      10(P)   NIL(P)
        15(V)
```
*Nota: A remoção do nó preto causou um déficit negro no caminho da direita.*

##### Passo B: Rotação no Irmão
O irmão da folha deficitária é o 10 (preto), que possui um filho direito vermelho (15). Fazemos uma rotação à esquerda no 10 para alinhar a estrutura.
```text
      30(P)
     /      15(P)   NIL(P)
  /
10(V)
```

##### Passo C: Rotação na Raiz e Ajuste Final
Uma rotação à direita na raiz (30) é executada, e as cores são balanceadas para restabelecer a altura negra idêntica em todos os caminhos.
```text
      15(P)
     /      10(P)   30(P)
```

**Árvore perfeitamente balanceada e válida!**

---

## 4. Implementação em Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1 = Vermelho, 0 = Preto

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 0
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, data):
        z = self.root
        while z != self.NIL and z.data != data:
            if z.data > data:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 0:
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def print_tree(self, node, indent="", last=True):
        if node != self.NIL:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            color = "VERMELHO" if node.color == 1 else "PRETO"
            print(f"{node.data}({color})")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)
```

---

## 4. Implementação em C++

```cpp
#include <iostream>
#include <string>

enum Color { RED, BLACK };

struct Node {
    int data;
    Color color;
    Node *left, *right, *parent;
    Node(int data) : data(data), color(RED), left(nullptr), right(nullptr), parent(nullptr) {}
};

class RedBlackTree {
private:
    Node *root;
    Node *NIL;

    void leftRotate(Node *x) {
        Node *y = x->right;
        x->right = y->left;
        if (y->left != NIL) y->left->parent = x;
        y->parent = x->parent;
        if (x->parent == nullptr) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->left = x;
        x->parent = y;
    }

    void rightRotate(Node *x) {
        Node *y = x->left;
        x->left = y->right;
        if (y->right != NIL) y->right->parent = x;
        y->parent = x->parent;
        if (x->parent == nullptr) root = y;
        else if (x == x->parent->right) x->parent->right = y;
        else x->parent->left = y;
        y->right = x;
        x->parent = y;
    }

    void fixInsert(Node *k) {
        while (k->parent->color == RED) {
            if (k->parent == k->parent->parent->right) {
                Node *u = k->parent->parent->left;
                if (u->color == RED) {
                    u->color = BLACK;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;
                } else {
                    if (k == k->parent->left) {
                        k = k->parent;
                        rightRotate(k);
                    }
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    leftRotate(k->parent->parent);
                }
            } else {
                Node *u = k->parent->parent->right;
                if (u->color == RED) {
                    u->color = BLACK;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;
                } else {
                    if (k == k->parent->right) {
                        k = k->parent;
                        leftRotate(k);
                    }
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    rightRotate(k->parent->parent);
                }
            }
            if (k == root) break;
        }
        root->color = BLACK;
    }

    void rbTransplant(Node *u, Node *v) {
        if (u->parent == nullptr) root = v;
        else if (u == u->parent->left) u->parent->left = v;
        else u->parent->right = v;
        v->parent = u->parent;
    }

    void fixDelete(Node *x) {
        while (x != root && x->color == BLACK) {
            if (x == x->parent->left) {
                Node *s = x->parent->right;
                if (s->color == RED) {
                    s->color = BLACK;
                    x->parent->color = RED;
                    leftRotate(x->parent);
                    s = x->parent->right;
                }
                if (s->left->color == BLACK && s->right->color == BLACK) {
                    s->color = RED;
                    x = x->parent;
                } else {
                    if (s->right->color == BLACK) {
                        s->left->color = BLACK;
                        s->color = RED;
                        rightRotate(s);
                        s = x->parent->right;
                    }
                    s->color = x->parent->color;
                    x->parent->color = BLACK;
                    s->right->color = BLACK;
                    leftRotate(x->parent);
                    x = root;
                }
            } else {
                Node *s = x->parent->left;
                if (s->color == RED) {
                    s->color = BLACK;
                    x->parent->color = RED;
                    rightRotate(x->parent);
                    s = x->parent->left;
                }
                if (s->right->color == BLACK && s->left->color == BLACK) {
                    s->color = RED;
                    x = x->parent;
                } else {
                    if (s->left->color == BLACK) {
                        s->right->color = BLACK;
                        s->color = RED;
                        leftRotate(s);
                        s = x->parent->left;
                    }
                    s->color = x->parent->color;
                    x->parent->color = BLACK;
                    s->left->color = BLACK;
                    rightRotate(x->parent);
                    x = root;
                }
            }
        }
        x->color = BLACK;
    }

    Node* minimum(Node *node) {
        while (node->left != NIL) node = node->left;
        return node;
    }

    void printHelper(Node *root, std::string indent, bool last) {
        if (root != NIL) {
            std::cout << indent;
            if (last) {
                std::cout << "R----";
                indent += "     ";
            } else {
                std::cout << "L----";
                indent += "|    ";
            }
            std::string sColor = (root->color == RED) ? "VERMELHO" : "PRETO";
            std::cout << root->data << "(" << sColor << ")" << std::endl;
            printHelper(root->left, indent, false);
            printHelper(root->right, indent, true);
        }
    }

public:
    RedBlackTree() {
        NIL = new Node(0);
        NIL->color = BLACK;
        root = NIL;
    }

    void insert(int key) {
        Node *node = new Node(key);
        node->left = NIL;
        node->right = NIL;

        Node *y = nullptr;
        Node *x = this->root;

        while (x != NIL) {
            y = x;
            if (node->data < x->data) x = x->left;
            else x = x->right;
        }

        node->parent = y;
        if (y == nullptr) root = node;
        else if (node->data < y->data) y->left = node;
        else y->right = node;

        if (node->parent == nullptr) {
            node->color = BLACK;
            return;
        }
        if (node->parent->parent == nullptr) return;

        fixInsert(node);
    }

    void deleteNode(int data) {
        Node *z = NIL;
        Node *x, *y;
        Node *curr = this->root;
        while (curr != NIL) {
            if (curr->data == data) { z = curr; break; }
            if (curr->data <= data) curr = curr->right;
            else curr = curr->left;
        }

        if (z == NIL) return;

        y = z;
        Color y_original_color = y->color;
        if (z->left == NIL) {
            x = z->right;
            rbTransplant(z, z->right);
        } else if (z->right == NIL) {
            x = z->left;
            rbTransplant(z, z->left);
        } else {
            y = minimum(z->right);
            y_original_color = y->color;
            x = y->right;
            if (y->parent == z) x->parent = y;
            else {
                rbTransplant(y, y->right);
                y->right = z->right;
                y->right->parent = y;
            }
            rbTransplant(z, y);
            y->left = z->left;
            y->left->parent = y;
            y->color = z->color;
        }
        delete z;
        if (y_original_color == BLACK) fixDelete(x);
    }

    void printTree() {
        if (root) printHelper(this->root, "", true);
    }
};
```
