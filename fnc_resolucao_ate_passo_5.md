# Exemplo completo: Skolemização, FNC e Resolução em Lógica de Predicados

## 1. Definir a base de conhecimento e a consulta

Vamos demonstrar, passo a passo, como utilizar a Skolemização, a Forma Normal Conjuntiva (FNC) e a resolução para provar uma conclusão a partir de uma base de conhecimento.

## Exemplo 1 — Silogismo de Sócrates

1. Todo ser humano é mortal.
2. Sócrates é um ser humano.

Queremos demonstrar que Sócrates é mortal.

**Base de conhecimento (BC):**

$$
\[
\forall x\,(Humano(x)\rightarrow Mortal(x))
\]
$$

$$
\[
Humano(Socrates)
\]
$$

**Consulta:**

$$
\[
\alpha = Mortal(Socrates)
\]
$$

Nosso objetivo é provar que:

$$
\[
\boxed{BC \models Mortal(Socrates)}
\]
$$

Para isso, utilizaremos uma prova por contradição: adicionaremos a negação da consulta à base de conhecimento e tentaremos obter uma contradição por resolução.

## Passo 1 — Negar a consulta

A consulta original é:

$$
\[
\alpha = Mortal(Socrates)
\]
$$

Negando-a:

$$
\[
\neg\alpha = \neg Mortal(Socrates)
\]
$$

Adicionamos essa negação à base de conhecimento:

$$
\[
F =
\forall x\,(Humano(x)\rightarrow Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
\]
$$

Se conseguirmos demonstrar que \(F\) é insatisfatível, teremos provado que a consulta é consequência lógica da base de conhecimento.

## Passo 2 — Eliminar as implicações

A fórmula contém a implicação:

$$
\[
Humano(x)\rightarrow Mortal(x)
\]
$$

Utilizamos a equivalência lógica:

$$
\[
P\rightarrow Q \equiv \neg P\lor Q
\]
$$

Logo:

$$
\[
Humano(x)\rightarrow Mortal(x)
\]
$$

torna-se:

$$
\[
\neg Humano(x)\lor Mortal(x)
\]
$$

A fórmula completa passa a ser:

$$
\[
F =
\forall x\,(\neg Humano(x)\lor Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
\]
$$

Observe que eliminamos a implicação, substituindo-a por uma disjunção.

## Passo 3 — Mover as negações para dentro

A fórmula resultante já está na forma normal negativa (FNN): as negações aparecem diretamente diante dos predicados.

Temos:

$$
\[
F =
\forall x\,(\neg Humano(x)\lor Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
\]
$$

Não precisamos aplicar nenhuma outra lei de De Morgan neste exemplo.

**Observação:** a forma normal negativa não é a mesma coisa que a Forma Normal Conjuntiva. Ainda precisamos verificar as etapas seguintes da conversão.

## Passo 4 — Padronizar as variáveis

A padronização consiste em renomear variáveis ligadas por quantificadores quando necessário, evitando ambiguidades entre variáveis distintas.

Neste exemplo, temos apenas uma variável universal, \(x\). Portanto, **não é necessário renomear nenhuma variável**.

A fórmula permanece:

$$
\[
F =
\forall x\,(\neg Humano(x)\lor Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
\]
$$

## Passo 5 — Aplicar a Skolemização

A Skolemização elimina os quantificadores existenciais, substituindo suas variáveis por constantes ou funções de Skolem.

Entretanto, observe que nossa fórmula contém apenas o quantificador universal:

$$
\[
\forall x
\]
$$

Não existem quantificadores existenciais neste exemplo. Portanto, **a Skolemização não altera a fórmula**.

Temos:

$$
\[
F =
\forall x\,(\neg Humano(x)\lor Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
\]
$$

Isso é importante: nem todo exemplo de resolução precisa modificar a fórmula durante a Skolemização.

---

### Passo 6 — Eliminar os quantificadores universais

Após a Skolemização, eliminamos os símbolos explícitos dos quantificadores universais. As variáveis que aparecem nas cláusulas são consideradas universalmente quantificadas.

A fórmula

$$
\[
\forall x\,(\neg Humano(x)\lor Mortal(x))
\]
$$

passa a ser representada por:

$$
\[
\neg Humano(x)\lor Mortal(x)
\]
$$

Assim, a fórmula completa fica:

$$
\[
F =
(\neg Humano(x)\lor Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
\]
$$

### Passo 7 — Transformar para a Forma Normal Conjuntiva (FNC)

A FNC é uma conjunção de cláusulas, e cada cláusula é uma disjunção de literais.

Neste exemplo, a fórmula já está na FNC:

$$
\[
\boxed{
F =
(\neg Humano(x)\lor Mortal(x))
\land Humano(Socrates)
\land \neg Mortal(Socrates)
}
\]
$$

Não é necessário distribuir disjunções sobre conjunções.

### Passo 8 — Separar a FNC em cláusulas

Separando cada componente da conjunção, obtemos:

$$
\[
C_1 = \neg Humano(x)\lor Mortal(x)
\]
$$

$$
\[
C_2 = Humano(Socrates)
\]
$$

$$
\[
C_3 = \neg Mortal(Socrates)
\]
$$

O conjunto de cláusulas é:

\[
S=\{C_1,C_2,C_3\}
\]

### Passo 9 — Aplicar a regra de resolução

A resolução combina cláusulas que contêm literais complementares. Na Lógica de Predicados, os literais devem poder ser unificados.

#### Resolução 1 — Usar \(C_1\) e \(C_2\)

Temos:

$$
\[
C_1=\neg Humano(x)\lor Mortal(x)
\]
$$

$$
\[
C_2=Humano(Socrates)
\]

Os literais \(\neg Humano(x)\) e \(Humano(Socrates)\) são complementares pela substituição:

\[
x=Socrates
\]
$$

Aplicando a resolução:

$$
\[
\frac{
\neg Humano(x)\lor Mortal(x)
\qquad Humano(Socrates)
}{
Mortal(Socrates)
}
\]
$$

Obtemos:

$$
\[
C_4=Mortal(Socrates)
\]
$$

#### Resolução 2 — Usar \(C_4\) e \(C_3\)

Temos:

$$
\[
C_4=Mortal(Socrates)
\]
$$

\[
C_3=\neg Mortal(Socrates)
\]

Os literais são complementares. Pela resolução:

$$
\[
\frac{
Mortal(Socrates)
\qquad
\neg Mortal(Socrates)
}{
\Box
}
\]
$$

A cláusula vazia $\(\Box\)$ representa uma contradição.

### Passo 10 — Interpretar o resultado

A fórmula inicial era:

$$
\[
F=BC\land\neg\alpha
\]
$$

Como a resolução produziu a cláusula vazia, \(BC\land\neg\alpha\) é insatisfatível. Logo:

$$
\[
\boxed{BC\models Mortal(Socrates)}
\]
$$

**Conclusão:** demonstramos que Sócrates é mortal.

---

## Exemplo 2 — Todo ser humano tem uma mãe

1. Todo ser humano tem uma mãe.
2. Sócrates é um ser humano.

Considere a base de conhecimento, em que a primeira afirmação é representada por:

$$
\[
\forall x\,(Humano(x)\rightarrow \exists y\,Mae(x,y))
\]
$$

A segunda afirmação é:

$$
\[
Humano(Socrates)
\]
$$

A consulta é:

$$
\[
\alpha=\exists y\,Mae(Socrates,y)
\]
$$

### Passo 6 — Eliminar os quantificadores universais

Após eliminar a implicação e aplicar a Skolemização, temos:

$$
\[
\forall x\,(\neg Humano(x)\lor Mae(x,f(x)))
\]
$$

Eliminando o símbolo explícito do quantificador universal, obtemos a cláusula:

$$
\[
C_1=\neg Humano(x)\lor Mae(x,f(x))
\]
$$

A afirmação de que Sócrates é humano gera:

$$
\[
C_2=Humano(Socrates)
\]
$$

A negação da consulta, $\(\neg\exists y\,Mae(Socrates,y)\)$, equivale a:

$$
\[
\forall y\,\neg Mae(Socrates,y)
\]
$$

Eliminando o quantificador universal explícito, obtemos:

$$
\[
C_3=\neg Mae(Socrates,y)
\]
$$

Portanto, o conjunto de cláusulas é:

$$
\[
S=\{C_1,C_2,C_3\}
\]
$$

### Passo 7 — Verificar a Forma Normal Conjuntiva (FNC)

A fórmula está na FNC, pois consiste em uma conjunção de cláusulas. Cada cláusula contém um literal ou uma disjunção de literais:

$$
\[
\boxed{
\begin{aligned}
C_1&=\neg Humano(x)\lor Mae(x,f(x))\\
C_2&=Humano(Socrates)\\
C_3&=\neg Mae(Socrates,y)
\end{aligned}
}
\]
$$

### Passo 8 — Separar em cláusulas

O conjunto final é:

$$
\[
\boxed{
S=
\{
\neg Humano(x)\lor Mae(x,f(x)),
Humano(Socrates),
\neg Mae(Socrates,y)
\}
}
\]
$$

### Passo 9 — Aplicar a regra de resolução

#### Resolução 1 — Usar $\(C_1\)$ e $\(C_2\)$

Temos:

$$
\[
C_1=\neg Humano(x)\lor Mae(x,f(x))
\]
$$

$$
\[
C_2=Humano(Socrates)
\]
$$

Unificamos os literais complementares usando:

$$
\[
x=Socrates
\]
$$

A resolução produz:

$$
\[
C_4=Mae(Socrates,f(Socrates))
\]
$$

#### Resolução 2 — Usar $\(C_4\) e \(C_3\)$

Temos:

$$
\[
C_4=Mae(Socrates,f(Socrates))
\]
$$

$$
\[
C_3=\neg Mae(Socrates,y)
\]
$$

Os literais são complementares com a substituição:

$$
\[
y=f(Socrates)
\]
$$

Aplicando a resolução:

$$
\[
\frac{
Mae(Socrates,f(Socrates))
\qquad
\neg Mae(Socrates,y)
}{
\Box
}
\]
$$

Obtemos a cláusula vazia:

$$
\[
\boxed{\Box}
\]
$$

### Passo 10 — Interpretar o resultado

A cláusula vazia mostra que a base de conhecimento, combinada com a negação da consulta, é insatisfatível. Portanto:

$$
\[
\boxed{
BC\models\exists y\,Mae(Socrates,y)
}
\]
$$

**Conclusão:** demonstramos que Sócrates tem uma mãe.

---

## Resumo das etapas

| Etapa | Silogismo de Sócrates | Exemplo da mãe |
|---|---|---|
| 6. Eliminar quantificadores universais | As variáveis universais ficam implícitas | As variáveis universais ficam implícitas |
| 7. Obter/verificar a FNC | A fórmula já está na FNC | A fórmula já está na FNC após a Skolemização |
| 8. Separar em cláusulas | Três cláusulas iniciais | Três cláusulas iniciais |
| 9. Aplicar resolução | Deriva \(Mortal(Socrates)\) e depois $\(\Box\)$ | Deriva \(Mae(Socrates,f(Socrates))\) e depois $\(\Box\)$ |
| 10. Concluir | $\(BC\models Mortal(Socrates)\)$ | $\(BC\models\exists y\,Mae(Socrates,y)\)$ |

**Para memorizar:** a Skolemização elimina quantificadores existenciais; a FNC organiza a fórmula em cláusulas; e a resolução tenta derivar a cláusula vazia para demonstrar a conclusão por refutação.

> **Nota:** a Skolemização preserva a satisfatibilidade, mas não necessariamente a equivalência lógica da fórmula original.
