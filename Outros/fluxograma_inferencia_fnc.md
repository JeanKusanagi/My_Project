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
     ├─ Eliminar implicações (A ──> B vira ¬A ∨ B)
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
Adota-se o princípio da *reducio ad absurdum* (prova por contradição). Em vez de tentar provar $\alpha$ diretamente, tenta-se provar que a inclusão de sua negação ($BC \wedge 
eglpha$) gera uma inconsistência ou absurdo lógico.

### 3. Conversão para FNC
A expressão inteira é padronizada. Uma fórmula está em FNC (Forma Normal Conjuntiva) quando é composta por uma conjunção ("E") de cláusulas, onde cada cláusula é uma disjunção ("OU") de literais. Os passos internos de conversão são:
* **Eliminar Equivalências:** Substituir $A \leftrightarrow B$ por $(A 
ightarrow B) \wedge (B 
ightarrow A)$.
* **Eliminar Implicações:** Substituir $A 
ightarrow B$ por $
eg A ee B$.
* **Internalizar Negações:** Aplicar as Leis de De Morgan (ex: $
eg(A \wedge B)$ vira $
eg A ee 
eg B$) e eliminar dupla negação ($
eg
eg A$ vira $A$).
* **Distribuir Disjunções:** Distribuir o operador $ee$ sobre o $\wedge$ para que os "E" fiquem apenas no nível mais externo.

### 4. Separação em Cláusulas
O operador $\wedge$ (E) global é descartado, quebrando a fórmula final em um conjunto de cláusulas independentes e simplificadas dentro do sistema.

### 5. Loop de Resolução
O motor de inferência busca iterativamente pares de cláusulas que contenham literais complementares (por exemplo, uma cláusula com $P$ e outra com $
eg P$). Elas são combinadas (resolvidas) gerando uma nova cláusula (resolvente) que exclui o par complementar.

### 6. Condição de Parada
* **Sucesso (Cláusula Vazia $\square$):** Se a resolução de duas cláusulas complementares diretas (como $P$ e $
eg P$) gerar o símbolo vazio, significa que a contradição foi alcançada. Isso prova que **$\alpha$ é uma consequência lógica** da base.
* **Falha:** Se nenhuma cláusula nova puder ser gerada e o símbolo vazio não for alcançado, significa que a inferência falhou e $\alpha$ não pode ser provado a partir daquela BC.
