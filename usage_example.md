# Exemplo de Uso do Agente de Segmentação de Vias Aéreas

## 🚀 Como Usar

### Instalação de Dependências

```bash
pip install anthropic --break-system-packages
```

### Uso Básico

```python
from airway_segmentation_agent import AirwaySegmentationAgent

# Criar instância do agente
agent = AirwaySegmentationAgent()

# Executar pipeline completo de busca e análise
report = agent.run_search_pipeline()
```

### Buscas Personalizadas

```python
# Buscar tópicos específicos
custom_queries = [
    "3D U-Net airway segmentation loss functions 2024",
    "attention mechanisms bronchial tree segmentation",
    "topology-preserving loss airway CT"
]

report = agent.run_search_pipeline(custom_queries=custom_queries)
```

### Busca Direcionada

```python
# Buscar um tópico específico
topic = "Tversky loss function for airway segmentation"
summary = agent.search_specific_topic(topic)
print(summary)
```

## 📊 Saídas do Agente

O agente gera um relatório markdown completo contendo:

1. **Técnicas de Deep Learning identificadas**
   - Arquiteturas de redes neurais
   - Variantes e modificações

2. **Funções de Loss encontradas**
   - Descrição de cada função
   - Aplicações específicas

3. **Datasets disponíveis**
   - Datasets públicos
   - Características

4. **Métricas de avaliação**
   - Dice Score
   - Sensitivity/Specificity
   - Métricas específicas para vias aéreas

5. **Recomendações práticas**
   - Melhores práticas
   - Sugestões de implementação

## 🔍 Funcionalidades

### 1. Busca Web Inteligente
- Utiliza a API Claude com web search
- Consultas otimizadas para literatura médica
- Extração automática de informações relevantes

### 2. Análise Consolidada
- Agrega resultados de múltiplas buscas
- Remove duplicatas
- Identifica padrões

### 3. Geração de Relatórios
- Formato markdown profissional
- Seções bem organizadas
- Referências incluídas

## 💡 Casos de Uso

### Pesquisador Iniciante
```python
# Obter visão geral do campo
agent = AirwaySegmentationAgent()
report = agent.run_search_pipeline()

# O relatório fornece:
# - Estado da arte atual
# - Técnicas mais utilizadas
# - Pontos de partida para pesquisa
```

### Implementação Prática
```python
# Buscar informações específicas para implementação
topics = [
    "best loss function for thin airway branches",
    "3D U-Net implementation pytorch airway",
    "data augmentation techniques CT segmentation"
]

for topic in topics:
    summary = agent.search_specific_topic(topic)
    print(f"\n{topic}:\n{summary}")
```

### Atualização de Conhecimento
```python
# Buscar desenvolvimentos recentes
recent_queries = [
    "airway segmentation 2024 advances",
    "transformer-based airway segmentation",
    "self-supervised learning airway CT"
]

report = agent.run_search_pipeline(custom_queries=recent_queries)
```

## 🛠️ Personalização

### Modificar Base de Conhecimento

```python
agent = AirwaySegmentationAgent()

# Adicionar novas arquiteturas conhecidas
agent.techniques_db["architectures"].extend([
    "CoTr", "MedFormer", "UNETR"
])

# Adicionar novas funções de loss
agent.techniques_db["loss_functions"].extend([
    "Hausdorff Distance Loss",
    "Clipped Dice Loss"
])
```

### Ajustar Queries de Busca

```python
# Definir suas próprias queries
my_queries = [
    "pediatric airway segmentation challenges",
    "airway segmentation with limited annotations",
    "multi-task learning airway and vessel segmentation"
]

agent = AirwaySegmentationAgent()
report = agent.run_search_pipeline(custom_queries=my_queries)
```

## 📈 Exemplo de Output

```markdown
# Relatório de Segmentação de Vias Aéreas
**Gerado em:** 04/02/2026 14:30:00
**Buscas realizadas:** 3

---

## 1. Introdução à Segmentação de Vias Aéreas

A segmentação automática de vias aéreas em imagens de TC torácica...

## 2. Principais Arquiteturas de Deep Learning

### U-Net e Variantes
- U-Net 3D: Processamento volumétrico completo
- Attention U-Net: Mecanismos de atenção...

### Transformers
- TransUNet: Combinação de CNN e Transformers...

## 3. Funções de Loss Específicas

### Dice Loss
Fórmula: 1 - (2*TP)/(2*TP + FP + FN)
Vantagens: Lida com desbalanceamento...

### Centerline Dice Loss
Específica para estruturas tubulares...

[... resto do relatório ...]
```

## ⚙️ Configurações Avançadas

### Limitar Número de Buscas

```python
# Para economizar recursos
agent = AirwaySegmentationAgent()
agent.search_queries = agent.search_queries[:2]  # Apenas 2 buscas
```

### Salvar Resultados Intermediários

```python
import json

agent = AirwaySegmentationAgent()
search_results = []

for query in agent.search_queries[:3]:
    result = agent.search_literature(query)
    search_results.append(result)
    
    # Salvar resultado intermediário
    with open(f'results_{query[:20]}.json', 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

# Depois analisar
analysis = agent.analyze_techniques(search_results)
```

## 🎯 Dicas de Uso

1. **Começar com queries amplas**: Para ter visão geral
2. **Refinar gradualmente**: Queries mais específicas depois
3. **Combinar com documentação técnica**: Use junto com o guia técnico
4. **Verificar fontes**: Sempre conferir URLs retornadas
5. **Atualizar regularmente**: Campo evolui rapidamente

## 📝 Estrutura do Código

```
airway_segmentation_agent.py
├── AirwaySegmentationAgent (classe principal)
│   ├── __init__: Inicialização e base de conhecimento
│   ├── search_literature: Busca web com Claude API
│   ├── analyze_techniques: Consolida resultados
│   ├── generate_report: Gera relatório final
│   ├── run_search_pipeline: Pipeline completo
│   └── search_specific_topic: Busca direcionada
└── main: Função de demonstração
```

## 🔄 Workflow Típico

```
1. Inicializar Agente
   ↓
2. Definir Queries (padrão ou customizadas)
   ↓
3. Executar Buscas Web
   ↓
4. Consolidar Resultados
   ↓
5. Analisar Dados
   ↓
6. Gerar Relatório
   ↓
7. Salvar Arquivo Markdown
```

## 🚨 Troubleshooting

### Erro: "API key not found"
```python
# Definir chave da API
import os
os.environ['ANTHROPIC_API_KEY'] = 'sua-chave-aqui'
```

### Buscas retornam pouco conteúdo
- Ajustar queries para serem mais específicas
- Tentar termos técnicos em inglês
- Verificar conectividade de rede

### JSON parsing error
- Normal para algumas respostas
- O agente retorna texto bruto como fallback
- Considerar melhorar prompt de extração

## 📚 Recursos Complementares

- **Guia Técnico**: `airway_segmentation_guide.md`
- **Documentação Claude API**: https://docs.anthropic.com
- **MONAI Docs**: https://docs.monai.io
- **Papers**: Buscar no Google Scholar ou PubMed

---

*Exemplo de uso do Agente de Segmentação de Vias Aéreas*
*Para dúvidas ou sugestões, consulte a documentação técnica*
