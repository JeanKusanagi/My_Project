# SIMULADO — Ética, Transparência, Avaliação e Regulamentação em IA
### Vieses algorítmicos | Interpretabilidade | Responsabilidade social | LGPD | Regulamentação da IA no Brasil (PL 2338/2023)

---

**1.** Viés algorítmico, no contexto de sistemas de IA, refere-se a:

a) Erros de sintaxe no código-fonte do modelo<br>
b) Distorções sistemáticas nos resultados de um modelo que favorecem ou desfavorecem injustamente determinados grupos, geralmente refletindo padrões presentes nos dados de treinamento ou no desenho do sistema<br>
c) A velocidade de processamento de um algoritmo<br>
d) A quantidade de parâmetros de uma rede neural

> **Gabarito: b.** Viés algorítmico é uma distorção sistemática — não aleatória — que produz resultados injustos para certos grupos, geralmente por refletir desigualdades presentes nos dados históricos ou escolhas de design do sistema.

---

**2.** **(Pegadinha)** Um sistema de IA para triagem de currículos é treinado com dados históricos de contratação de uma empresa que, no passado, contratou majoritariamente homens para cargos técnicos. Mesmo sem nenhuma variável explícita de gênero no conjunto de dados, o modelo passa a penalizar currículos associados a mulheres. Esse fenômeno ilustra:

a) Um erro de programação isolado, sem relação com os dados<br>
b) Viés algorítmico por proxy — variáveis correlacionadas (como nome de faculdade, hobbies, palavras usadas) atuam como substitutas indiretas de um atributo sensível, mesmo que este não esteja explicitamente presente<br>
c) Impossibilidade de haver viés quando a variável sensível é removida da base<br>
d) Um caso de interpretabilidade, não de viés

> **Gabarito: b.** Pegadinha: remover a variável sensível não elimina o viés se houver variáveis "proxy" correlacionadas a ela — é um dos problemas mais conhecidos de fairness em ML.

---

**3.** Interpretabilidade de modelos de IA refere-se principalmente à capacidade de:

a) Executar o modelo mais rapidamente<br>
b) Compreender e explicar como um modelo chega a determinada decisão ou previsão<br>
c) Aumentar o número de camadas de uma rede neural<br>
d) Reduzir o tamanho do conjunto de dados de treinamento

> **Gabarito: b.** Interpretabilidade/explicabilidade (XAI) trata de tornar compreensível o processo decisório do modelo, para humanos.

---

**4.** **(Pegadinha)** Sobre modelos "caixa-preta" (black-box), como redes neurais profundas, é correto afirmar que:

a) Eles nunca podem ser auditados ou explicados de forma alguma<br>
b) Sua alta acurácia elimina a necessidade de qualquer explicabilidade<br>
c) Embora sejam intrinsecamente mais difíceis de interpretar do que modelos simples (como árvores de decisão), técnicas de explicabilidade *post-hoc* (como LIME e SHAP) podem ser aplicadas para aproximar explicações sobre suas decisões<br>
d) São sempre proibidos por lei em qualquer país

> **Gabarito: c.** Pegadinha: "difícil de interpretar" não é o mesmo que "impossível de explicar" — existem técnicas post-hoc para gerar explicações aproximadas mesmo em modelos complexos.

---

**5.** Qual das opções é um exemplo de técnica de explicabilidade (XAI) amplamente citada na literatura?

a) SHAP (SHapley Additive exPlanations)<br>
b) TCP/IP<br>
c) HTML5<br>
d) UDP

> **Gabarito: a.** SHAP é uma das técnicas mais conhecidas de XAI, baseada em valores de Shapley da teoria dos jogos, usada para explicar a contribuição de cada variável em uma previsão.

---

**6.** Responsabilidade social em IA está mais diretamente relacionada a:

a) O dever das organizações de considerar os impactos éticos, sociais e ambientais dos sistemas de IA que desenvolvem ou utilizam, para além do mero cumprimento legal mínimo<br>
b) A obrigação exclusiva de reduzir custos de infraestrutura computacional<br>
c) A proibição total do uso de IA em qualquer setor<br>
d) A responsabilidade apenas dos usuários finais, nunca das empresas desenvolvedoras

> **Gabarito: a.** Responsabilidade social vai além da conformidade legal estrita, envolvendo compromissos éticos com impactos sociais, ambientais e sobre grupos vulneráveis.

---

**7.** A LGPD (Lei nº 13.709/2018) tem como um de seus fundamentos centrais:

a) A proibição total de qualquer tratamento de dados pessoais no Brasil<br>
b) A proteção dos direitos fundamentais de liberdade, privacidade e livre desenvolvimento da personalidade da pessoa natural<br>
c) A obrigatoriedade de todo dado pessoal ser armazenado apenas em servidores públicos<br>
d) A regulamentação exclusiva de dados de empresas multinacionais

> **Gabarito: b.** Esse é um dos fundamentos expressos no art. 2º da LGPD.

---

**8.** **(Pegadinha)** De acordo com a LGPD, o titular de dados submetido a decisões tomadas unicamente com base em tratamento automatizado de dados pessoais (art. 20) tem o direito de:

a) Impedir para sempre qualquer uso de IA pela empresa<br>
b) Solicitar revisão de decisões tomadas unicamente com base em tratamento automatizado que afetem seus interesses, podendo pedir informações claras e adequadas sobre os critérios e procedimentos utilizados<br>
c) Exigir que a empresa revele o código-fonte completo do algoritmo, incluindo segredos industriais, sem qualquer ressalva<br>
d) Receber automaticamente indenização financeira sempre que um algoritmo for usado

> **Gabarito: b.** Pegadinha: o direito é à *revisão* e à explicação sobre critérios/procedimentos — a LGPD ressalva segredo comercial e industrial (não obriga a revelar o código-fonte integral).

---

**9.** Qual princípio da LGPD está relacionado à limitação do tratamento de dados pessoais ao mínimo necessário para a realização de suas finalidades?

a) Princípio da livre iniciativa<br>
b) Princípio da necessidade<br>
c) Princípio da publicidade irrestrita<br>
d) Princípio da anterioridade tributária

> **Gabarito: b.** O princípio da necessidade (art. 6º, III, da LGPD) limita o tratamento ao mínimo necessário para atingir suas finalidades.

---

**10.** **(Pegadinha)** Dados anonimizados, segundo a LGPD, são:

a) Sempre equivalentes a dados pessoais para todos os efeitos legais<br>
b) Dados relativos a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento — deixando, em regra, de ser considerados dados pessoais<br>
c) Dados que foram apenas criptografados, mas que continuam plenamente identificáveis<br>
d) Dados pessoais sensíveis por definição

> **Gabarito: b.** Pegadinha: anonimização não é sinônimo de criptografia ou pseudonimização — a LGPD exige que a reidentificação seja inviável com meios técnicos razoáveis disponíveis; dados pseudonimizados, ao contrário, continuam sendo dados pessoais.

---

**11.** O órgão responsável por fiscalizar e aplicar a LGPD no Brasil é:

a) O Conselho Nacional de Justiça (CNJ)<br>
b) A Autoridade Nacional de Proteção de Dados (ANPD)<br>
c) O Banco Central do Brasil (BACEN)<br>
d) A Agência Nacional de Telecomunicações (Anatel)

> **Gabarito: b.** A ANPD é a autoridade responsável por zelar pela proteção de dados pessoais e fiscalizar o cumprimento da LGPD.

---

**12.** **(Pegadinha)** Em agosto de 2026, o Marco Legal da Inteligência Artificial no Brasil (PL 2338/2023):

a) Já está em pleno vigor como lei desde 2023<br>
b) Foi aprovado pelo Senado Federal em dezembro de 2024 e, até o momento, ainda tramita na Câmara dos Deputados, não tendo sido promulgado como lei<br>
c) Foi definitivamente rejeitado e arquivado pelo Congresso Nacional<br>
d) É uma resolução da ANPD, e não um projeto de lei

> **Gabarito: b.** Pegadinha temporal: o PL 2338/2023 foi aprovado no Senado em dezembro de 2024, mas ainda está em tramitação na Câmara dos Deputados, sem ter sido promulgado como lei até o momento — não confundir "aprovado em uma casa legislativa" com "lei em vigor".

---

**13.** O PL 2338/2023 adota, como estrutura central de regulamentação, um modelo:

a) De proibição total do uso de IA no Brasil<br>
b) Baseado em risco, classificando sistemas de IA por níveis (como excessivo, alto e demais riscos), com obrigações proporcionais ao risco — inspirado, entre outras referências, no AI Act europeu<br>
c) Exclusivamente voluntário, sem qualquer sanção prevista<br>
d) Aplicável apenas a empresas estrangeiras que atuam no Brasil

> **Gabarito: b.** O PL 2338/2023 segue uma abordagem regulatória baseada em risco, com inspiração no modelo europeu (AI Act), adaptado ao contexto brasileiro.

---

**14.** **(Pegadinha)** Segundo o texto do PL 2338/2023 aprovado no Senado, entre os direitos previstos aos afetados por sistemas de IA está o direito à explicação sobre decisões automatizadas. Isso significa que:

a) O usuário tem direito a obter informações claras e adequadas sobre os critérios e procedimentos utilizados por um sistema de IA que o afete, podendo contestar tais decisões<br>
b) O usuário tem direito de exigir que nenhuma IA seja usada em qualquer circunstância<br>
c) Esse direito é idêntico ao direito de propriedade intelectual sobre o algoritmo<br>
d) Esse direito só se aplica a sistemas de IA generativa

> **Gabarito: a.** Pegadinha: o direito à explicação é sobre critérios e procedimentos de decisões que afetam a pessoa, não uma garantia irrestrita contra qualquer uso de IA nem equivalente a propriedade intelectual.

---

**15.** O PL 2338/2023 prevê a criação de uma estrutura de governança e fiscalização do uso de IA no Brasil, comumente referida como:

a) SIA — Sistema Nacional de Regulação e Governança de Inteligência Artificial<br>
b) SUS — Sistema Único de Saúde<br>
c) SFH — Sistema Financeiro da Habitação<br>
d) SISU — Sistema de Seleção Unificada

> **Gabarito: a.** O texto prevê a criação do SIA, com papel de coordenação atribuído, entre outros órgãos, à ANPD.

---

**16.** **(Pegadinha)** Sobre a relação entre a ANPD e o Marco Legal da IA no Brasil, é correto afirmar que:

a) A ANPD não possui qualquer papel proposto na regulamentação de IA<br>
b) O texto do PL 2338/2023 atribui à ANPD papel de coordenação do sistema regulatório de IA (SIA), o que inclusive gerou um apontamento de vício de iniciativa por parte do Poder Executivo, por tratar de competências normativas atribuídas a um órgão federal<br>
c) A ANPD foi extinta após a aprovação do texto no Senado<br>
d) A ANPD só pode atuar em casos de IA generativa

> **Gabarito: b.** O texto aprovado no Senado atribuiu à ANPD papel de coordenação do SIA; o Executivo apontou um vício de iniciativa por tratar de competência normativa de órgão federal, o que levou ao envio de um projeto complementar para sanar o problema.

---

**17.** Qual das alternativas descreve corretamente um "sistema de IA de alto risco", segundo a lógica regulatória baseada em risco adotada por propostas como o PL 2338/2023 e o AI Act europeu?

a) Qualquer sistema de IA, sem distinção, é automaticamente classificado como de alto risco<br>
b) Sistemas cujo uso pode impactar significativamente direitos fundamentais, saúde, segurança ou acesso a serviços essenciais (como concessão de crédito, processos seletivos, saúde, justiça), exigindo obrigações mais rigorosas de governança e transparência<br>
c) Apenas sistemas usados por órgãos públicos são considerados de alto risco<br>
d) Sistemas de IA de alto risco são isentos de qualquer fiscalização

> **Gabarito: b.** A lógica de classificação por risco associa obrigações mais rigorosas a sistemas com maior potencial de impacto sobre direitos fundamentais e serviços essenciais.

---

**18.** **(Pegadinha)** Um hospital utiliza um sistema de IA para auxiliar na priorização de pacientes em fila de espera para cirurgia. Do ponto de vista da regulamentação baseada em risco, esse sistema tenderia a ser classificado como:

a) Risco mínimo, pois é apenas um "auxílio" e não decide nada por conta própria<br>
b) Alto risco, dado o impacto direto sobre a saúde e a vida das pessoas afetadas, ainda que a decisão final seja humana<br>
c) Impossível de ser regulado, por se tratar de área médica<br>
d) Risco inexistente, pois hospitais são sempre isentos de regulação de IA

> **Gabarito: b.** Pegadinha: o fato de "apenas auxiliar" a decisão humana não reduz automaticamente o nível de risco quando o impacto potencial sobre direitos fundamentais (saúde, vida) é elevado — o critério é o impacto, não apenas a autonomia total do sistema.

---

**19.** Auditoria algorítmica, como prática de governança de IA, consiste em:

a) Apagar os dados de treinamento do modelo após seu uso<br>
b) Analisar sistematicamente o funcionamento, os dados e os resultados de um sistema de IA para identificar riscos, vieses, erros ou não conformidades<br>
c) Aumentar a velocidade de inferência do modelo<br>
d) Trocar o modelo de IA por outro modelo aleatoriamente

> **Gabarito: b.** Auditoria algorítmica é o exame sistemático de um sistema de IA (dados, lógica, resultados) para identificar riscos, vieses e não conformidades.

---

**20.** **(Pegadinha)** Uma equipe de desenvolvimento afirma: "Nosso modelo é justo porque removemos todas as variáveis sensíveis, como raça e gênero, do conjunto de dados." Essa afirmação:

a) Está correta e encerra completamente a discussão sobre fairness (justiça algorítmica)<br>
b) Pode ser insuficiente, pois, como no fenômeno de viés por proxy, outras variáveis podem estar correlacionadas às sensíveis e reproduzir a discriminação indiretamente<br>
c) É desnecessária, pois viés algorítmico não existe em modelos estatísticos<br>
d) É verdadeira apenas para modelos de regressão linear, mas nunca para redes neurais

> **Gabarito: b.** Pegadinha recorrente no tema: remover variáveis sensíveis é necessário, mas não suficiente para garantir ausência de discriminação — o problema do proxy discutido na questão 2 se aplica aqui novamente.

---

**21.** Qual das opções representa uma métrica ou abordagem comumente discutida para avaliar *fairness* (justiça) em modelos de IA?

a) Paridade demográfica (demographic parity) entre grupos<br>
b) Tempo de resposta do servidor em milissegundos<br>
c) Tamanho do arquivo do modelo em megabytes<br>
d) Número de desenvolvedores na equipe

> **Gabarito: a.** Paridade demográfica é uma das métricas de fairness discutidas na literatura, buscando taxas semelhantes de resultados positivos entre grupos.

---

**22.** **(Pegadinha)** Sobre métricas de fairness em IA, é correto afirmar que:

a) Existe uma única métrica de justiça, universalmente aceita e aplicável a todos os contextos, sem qualquer trade-off<br>
b) Diferentes métricas de fairness (como paridade demográfica e igualdade de oportunidades) podem ser matematicamente incompatíveis entre si, exigindo escolhas conscientes sobre qual noção de justiça priorizar em cada contexto<br>
c) Métricas de fairness são irrelevantes quando o modelo tem alta acurácia geral<br>
d) Fairness é um conceito exclusivamente jurídico, sem qualquer formalização técnica

> **Gabarito: b.** Pegadinha: é um resultado conhecido na literatura de ML que certas métricas de fairness podem ser mutuamente incompatíveis (trade-offs), tornando necessária uma escolha contextual e não puramente técnica.

---

**23.** Transparência algorítmica, no debate ético e regulatório sobre IA, refere-se principalmente a:

a) Tornar públicos e acessíveis, na medida do possível, informações sobre o funcionamento, os critérios e os limites de um sistema de IA para os afetados por ele<br>
b) Divulgar obrigatoriamente todo o código-fonte de qualquer sistema, incluindo segredos comerciais, sem exceção<br>
c) Tornar o modelo mais lento<br>
d) Reduzir a quantidade de dados utilizados no treinamento

> **Gabarito: a.** Transparência não significa necessariamente divulgação irrestrita de código-fonte, mas sim informações compreensíveis sobre funcionamento, critérios e limites do sistema.

---

**24.** **(Pegadinha)** "A exigência de transparência algorítmica é incompatível com a proteção de segredo comercial e industrial das empresas." Sobre essa afirmação:

a) Ela é verdadeira, pois toda transparência exige divulgação total de algoritmos proprietários<br>
b) Ela é falsa — arcabouços como a LGPD e propostas regulatórias explicitamente ressalvam o segredo comercial e industrial, buscando equilibrar o direito à explicação com a proteção da propriedade intelectual<br>
c) Ela é verdadeira, pois não há qualquer previsão legal sobre segredo comercial no Brasil<br>
d) Ela é falsa, mas apenas porque não existe segredo comercial em sistemas de IA

> **Gabarito: b.** Pegadinha de "verdadeiro ou falso" disfarçada de múltipla escolha: a LGPD (art. 20, §2º) e propostas regulatórias buscam equilibrar transparência com proteção de segredo comercial/industrial — não são mutuamente exclusivos.

---

**25.** Accountability (responsabilização) em IA está relacionada a:

a) A garantia de que exista(m) responsável(is) identificável(is) — pessoas físicas ou jurídicas — pelos impactos e consequências de um sistema de IA, com possibilidade de responder por eles<br>
b) A eliminação de qualquer forma de responsabilidade humana quando um algoritmo comete um erro<br>
c) A obrigação exclusiva do usuário final, isentando completamente os desenvolvedores<br>
d) Um conceito que se aplica apenas a robôs físicos, não a softwares

> **Gabarito: a.** Accountability implica a existência de agentes responsáveis e identificáveis pelos impactos do sistema, permitindo atribuição de responsabilidade.

---

**26.** **(Pegadinha)** Uma empresa argumenta: "Não somos responsáveis pelas decisões discriminatórias do nosso algoritmo de concessão de crédito, pois ele apenas aprendeu padrões dos dados históricos, sem intervenção humana direta na regra final." Do ponto de vista da responsabilidade social e da regulamentação em discussão no Brasil, essa alegação:

a) É juridicamente inatacável, pois algoritmos "aprendem por conta própria" e não podem gerar responsabilidade para quem os desenvolve ou utiliza<br>
b) Tende a não eximir a empresa de responsabilidade, já que a responsabilização recai sobre os agentes que desenvolvem, implementam ou se beneficiam do sistema, independentemente do grau de automação do processo decisório<br>
c) É válida apenas se o algoritmo for de código aberto<br>
d) É válida apenas para instituições financeiras públicas

> **Gabarito: b.** Pegadinha: a "autonomia" do algoritmo em aprender padrões não transfere a responsabilidade para "o algoritmo" — ela permanece com os agentes humanos e organizacionais envolvidos em seu desenvolvimento e uso.

---

**27.** Avaliação de impacto algorítmico (AIA), citada em debates sobre governança de IA, é um instrumento que busca:

a) Medir exclusivamente o desempenho técnico (acurácia) de um modelo<br>
b) Identificar, previamente ou durante o uso, os potenciais impactos — sociais, éticos, discriminatórios, de privacidade — de um sistema de IA sobre indivíduos e grupos afetados<br>
c) Substituir totalmente a necessidade de testes de software<br>
d) Aplicar-se apenas a sistemas de IA usados por governos estrangeiros

> **Gabarito: b.** A AIA é voltada à identificação prévia/contínua de impactos sociais, éticos e de direitos, e não apenas ao desempenho técnico do modelo.

---

**28.** **(Pegadinha)** O consentimento do titular de dados, previsto na LGPD como uma das bases legais para tratamento de dados pessoais, deve ser:

a) Genérico e implícito, bastando um termo de uso extenso que o titular provavelmente não lerá<br>
b) Livre, informado e inequívoco, para uma finalidade determinada, sendo nulas as autorizações genéricas<br>
c) Sempre presumido quando o titular utiliza um aplicativo, independentemente de manifestação expressa<br>
d) Irrevogável após ser concedido uma única vez

> **Gabarito: b.** Pegadinha: a LGPD exige consentimento livre, informado e inequívoco, para finalidade determinada — vedando autorizações genéricas — e o titular pode revogar seu consentimento a qualquer momento (o que torna a alternativa "d" incorreta).

---

**29.** Entre os fundamentos frequentemente citados para a regulamentação ética da IA (incluindo discussões que orientam o PL 2338/2023), está o princípio de:

a) Centralidade da máquina, subordinando decisões humanas às decisões automatizadas<br>
b) Centralidade do ser humano, buscando que sistemas de IA sejam desenvolvidos e utilizados de forma a proteger direitos fundamentais e o bem-estar das pessoas<br>
c) Irrelevância de impactos ambientais no desenvolvimento de IA<br>
d) Prevalência absoluta da inovação tecnológica sobre qualquer outro valor, sem ponderação

> **Gabarito: b.** A centralidade do ser humano (human-centric AI) é um princípio recorrente nas discussões éticas e regulatórias sobre IA, inclusive nas referências internacionais que inspiram o debate brasileiro.

---

**30.** **(Pegadinha)** Um gestor público afirma: "Enquanto o PL 2338/2023 não é promulgado como lei, o uso de IA pelo poder público e por empresas no Brasil está em um vácuo normativo total, sem qualquer regra aplicável." Essa afirmação está:

a) Correta, pois nenhuma norma brasileira atual trata de dados, algoritmos ou automação antes da eventual aprovação do Marco Legal da IA<br>
b) Incorreta, pois, mesmo sem uma lei específica e geral sobre IA ainda em vigor, já existem normas aplicáveis ao tema no Brasil, como a LGPD (tratamento de dados pessoais e decisões automatizadas), o Código de Defesa do Consumidor, o Marco Civil da Internet e regulações setoriais (como diretrizes do CNJ sobre uso de IA no Judiciário)<br>
c) Correta, pois a LGPD trata apenas de assuntos de telecomunicações<br>
d) Incorreta, mas apenas porque o Marco Civil da Internet já regulamenta integralmente a IA

> **Gabarito: b.** Pegadinha central da questão: a ausência de uma lei geral e específica sobre IA não significa ausência total de regulação — a LGPD, o CDC, o Marco Civil da Internet e normas setoriais (como as diretrizes do CNJ) já se aplicam a diversos aspectos do uso de IA no Brasil.

---

## Observações finais para o aplicador

- As respostas corretas foram distribuídas de forma não sequencial entre as alternativas (a), (b), (c) e (d), evitando padrões previsíveis (ex.: "a resposta certa é sempre a 'c'").
- Recomenda-se, ao aplicar esta prova, reforçar oralmente que o PL 2338/2023 é um **projeto de lei em tramitação** (não uma lei em vigor até o momento desta prova, agosto de 2026), para evitar que os alunos memorizem uma informação que pode se tornar rapidamente desatualizada caso o texto seja promulgado.
