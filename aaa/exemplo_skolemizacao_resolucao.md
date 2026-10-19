## 12. Exemplo adicional: como a Skolemização funciona efetivamente

O exemplo anterior não exigiu a substituição de variáveis existenciais. Vamos considerar agora uma base de conhecimento que contém um quantificador existencial.

### Base de conhecimento

Considere as afirmações:

1. Todo ser humano tem uma mãe.
2. Sócrates é um ser humano.

Queremos demonstrar que Sócrates tem uma mãe.

Representamos a primeira afirmação por:

\[
\forall x\,(Humano(x)\rightarrow
\exists y\,Mae(x,y))
\]

A segunda afirmação é:

\[
Humano(Socrates)
\]

A consulta é:

\[
\alpha=\exists y\,Mae(Socrates,y)
\]

O predicado \(Mae(x,y)\) significa que \(y\) é mãe de \(x\).

### Etapa A — Negar a consulta

A consulta é:

\[
\exists y\,Mae(Socrates,y)
\]

Negando-a:

\[
\neg\exists y\,Mae(Socrates,y)
\]

Pela regra de negação do quantificador existencial:

\[
\boxed{\forall y\,\neg Mae(Socrates,y)}
\]

Adicionamos essa negação à base de conhecimento.

### Etapa B — Eliminar a implicação

A primeira fórmula é:

\[
\forall x\,(Humano(x)\rightarrow
\exists y\,Mae(x,y))
\]

Utilizando:

\[
P\rightarrow Q\equiv\neg P\lor Q
\]

Obtemos:

\[
\boxed{
\forall x\,(\neg Humano(x)\lor
\exists y\,Mae(x,y))
}
\]

### Etapa C — Aplicar a Skolemização

Temos a fórmula:

\[
\forall x\,(\neg Humano(x)\lor
\exists y\,Mae(x,y))
\]

Observe que \(y\) é existencial e está dentro do escopo do quantificador universal de \(x\).

Isso significa que o indivíduo que satisfaz \(Mae(x,y)\) pode depender de \(x\).

Portanto, substituímos \(y\) por uma função de Skolem:

\[
y=f(x)
\]

A fórmula transforma-se em:

\[
\boxed{
\forall x\,(\neg Humano(x)\lor Mae(x,f(x)))
}
\]

A função \(f(x)\) representa um indivíduo que pode ser escolhido para cada valor de \(x\), de modo que \(Mae(x,f(x))\) seja satisfeita.

**Atenção:** \(f\) não é necessariamente uma função de parentesco conhecida do mundo real. É um símbolo lógico introduzido para preservar a satisfatibilidade da fórmula durante a transformação.

### Etapa D — Eliminar os quantificadores universais

A fórmula skolemizada:

\[
\forall x\,(\neg Humano(x)\lor Mae(x,f(x)))
\]

passa a ser representada pela cláusula:

\[
C_1=\neg Humano(x)\lor Mae(x,f(x))
\]

A segunda afirmação gera:

\[
C_2=Humano(Socrates)
\]

A negação da consulta gera:

\[
C_3=\neg Mae(Socrates,y)
\]

Assim, o conjunto de cláusulas é:

\[
\boxed{
S=
\left\{
\begin{array}{l}
\neg Humano(x)\lor Mae(x,f(x))\\
Humano(Socrates)\\
\neg Mae(Socrates,y)
\end{array}
\right.
}
\]

### Etapa E — Aplicar a resolução

Resolvemos \(C_1\) e \(C_2\):

\[
\frac{
\neg Humano(x)\lor Mae(x,f(x))
\qquad Humano(Socrates)
}{
Mae(Socrates,f(Socrates))
}
\]

A substituição utilizada é:

\[
x=Socrates
\]

Obtemos:

\[
C_4=Mae(Socrates,f(Socrates))
\]

Agora, resolvemos \(C_4\) com \(C_3\):

\[
C_4=Mae(Socrates,f(Socrates))
\]

\[
C_3=\neg Mae(Socrates,y)
\]

Os literais são complementares mediante a substituição:

\[
y=f(Socrates)
\]

Portanto:

\[
\frac{
Mae(Socrates,f(Socrates))
\qquad
\neg Mae(Socrates,y)
}{
\Box
}
\]

Encontramos a cláusula vazia:

\[
\boxed{\Box}
\]

Logo, a fórmula formada pela base de conhecimento e pela negação da consulta é insatisfatível.

Concluímos que:

\[
\boxed{
BC\models\exists y\,Mae(Socrates,y)
}
\]

Demonstramos que Sócrates tem uma mãe, utilizando a Skolemização e a resolução.

---

## 13. Resumo do procedimento

| Etapa | Silogismo de Sócrates | Exemplo da mãe |
|---|---|---|
| 1. Negar a consulta | \(\neg Mortal(Socrates)\) | \(\forall y\,\neg Mae(Socrates,y)\) |
| 2. Eliminar implicações | \(\neg Humano(x)\lor Mortal(x)\) | \(\neg Humano(x)\lor\exists y\,Mae(x,y)\) |
| 3. Preparar a fórmula | Já está na forma normal negativa | Já está na forma normal negativa |
| 4. Skolemizar | Nenhuma alteração necessária | \(y=f(x)\) |
| 5. Eliminar universais | Variáveis ficam implícitas | Variáveis ficam implícitas |
| 6. Converter para FNC | Já está na FNC | Já está na FNC após a Skolemização |
| 7. Separar em cláusulas | Três cláusulas iniciais | Três cláusulas iniciais |
| 8. Aplicar resolução | Obter \(Mortal(Socrates)\) | Obter \(Mae(Socrates,f(Socrates))\) |
| 9. Obter a cláusula vazia | \(\Box\) | \(\Box\) |
| 10. Concluir | \(BC\models Mortal(Socrates)\) | \(BC\models\exists y\,Mae(Socrates,y)\) |

**Para memorizar:** a Skolemização elimina os quantificadores existenciais; a FNC organiza a fórmula em uma conjunção de cláusulas; e a resolução utiliza essas cláusulas para tentar obter a cláusula vazia, demonstrando a conclusão por refutação.
