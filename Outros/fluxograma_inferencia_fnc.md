# Fluxograma de Inferência na Forma Normal Conjuntiva (FNC)

Este documento apresenta o processo estruturado de inferência lógica proposicional utilizando a **Forma Normal Conjuntiva (FNC)**, amplamente aplicada em provadores automáticos de teoremas através do algoritmo de **Resolução**.

## O Fluxograma Lógico

```text
 [ Início: Base de Conhecimento (BC) e Consulta (α) ]
                          │
                          ▼
         [ Passo 1: Negar a Consulta (¬α) ]
                          │
                          ▼
 [ Passo 2: Adicionar à Base (BC ∧ ¬α) — Prova por Contradição ]
                          │
                          ▼
  [ Passo 3: Transformar toda a expressão para FNC (CNF) ]
     ├─ Substituir $A \leftrightarrow B$ por $(\neg A \lor B) \land (\neg B \lor A)$
     ├─ Trocar $A ↔ B$ por ($¬A ∨ B$) $\wedge$ $(B \rightarrow A)$.
     ├─ Eliminar implicações (A ─> B vira ¬A ∨ B)
     ├─ Mover negações para dentro (Leis de De Morgan)
     └─ Distribuir disjunções (∧ sobre ∨)
                          │
                          ▼
        [ Passo 4: Separar a FNC em Cláusulas ]
                          │
                          ▼
        [ Passo 5: Aplicar a Regra de Resolução ]
                          │
                          ▼
            < Encontrou Cláusula Vazia (□)? >
                  |                      |
                 Sim                    Não
                  |                      |          
                  ▼                      ▼
    [ Sucesso: BC implica α ]   [ Erro: Não é possível inferir α ]
    (Contradição Encontrada)   (Não há mais cláusulas para resolver)
                          │
                          ▼
                       [ Fim ]
```

---

## Detalhamento das Etapas do Fluxo

### 1. Definição das Entradas
O sistema recebe a **Base de Conhecimento (BC)** contendo as premissas conhecidas e a proposição **$\alpha$** (consulta) que se deseja provar.

### 2. Negação do Alvo (Refutação)
Adota-se o princípio da *reducio ad absurdum* (prova por contradição). Em vez de tentar provar $\alpha$ diretamente, tenta-se provar que a inclusão de sua negação ($BC ∧ ¬\alpha$) gera uma inconsistência ou absurdo lógico.

### 3. Conversão para FNC
A expressão inteira é padronizada. Uma fórmula está em FNC (Forma Normal Conjuntiva) quando é composta por uma conjunção ("E") de cláusulas, onde cada cláusula é uma disjunção ("OU") de literais. Os passos internos de conversão são:
* **Eliminar Equivalências:** Substituir $A$ $\leftrightarrow$ $B$ por ($B \rightarrow A$) $\wedge$ $(B$ 
$\rightarrow$ $A)$.
* **Eliminar Implicações:** Substituir $A$ $\rightarrow$ $B$ por $¬A ∨ B$.
* **Internalizar Negações:** Aplicar as Leis de De Morgan (ex: $¬(A \wedge B)$ vira $¬A ∨ ¬B$) e eliminar dupla negação ($¬¬A$ vira $A$).
* **Distribuir Disjunções:** Aplicar a propriedade distributiva do operador $\lor$ (OU) sobre o operador $\land$ (E), de modo que as conjunções fiquem no nível mais externo da fórmula, enquanto as disjunções conectam os literais dentro de cada cláusula:
   * $\[A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)\]$
   * $\[A \land (B \lor C) \equiv (A \land B) \lor (A \land C)\]$

### 4. Separação em Cláusulas
O operador $\wedge$ (E) global é descartado, quebrando a fórmula final em um conjunto de cláusulas independentes e simplificadas dentro do sistema.

Assim, a fórmula:

$$
\[
(A \lor B) \land (\neg A \lor C) \land (\neg B \lor C)
\]
$$

Transforma-se no conjunto:

$$
\[
\boxed{
S = \{(A \lor B), (\neg A \lor C), (\neg B \lor C)\}
}
\]
$$

### 5. Loop de Resolução
O motor de inferência busca iterativamente pares de cláusulas que contenham literais complementares (por exemplo, uma cláusula com $P$ e outra com $P$). Elas são combinadas (resolvidas) gerando uma nova cláusula (resolvente) que exclui o par complementar.

### 6. Condição de Parada
* **Sucesso (Cláusula Vazia $\square$):** Se a resolução de duas cláusulas complementares diretas (como $P$ e $¬\neg P$) gerar o símbolo vazio, significa que a contradição foi alcançada. Isso prova que **$\alpha$ é uma consequência lógica da base de conhecimento (BC)**.
* **Falha:** Se nenhuma cláusula nova puder ser gerada e a cláusula vazia ($\square$) não for obtida, significa que não foi possível demonstrar que $\alpha$ é uma consequência lógica da base de conhecimento (BC).
