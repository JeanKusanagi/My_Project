# 🤖 Agente de IA para Segmentação de Vias Aéreas

Um agente inteligente especializado em buscar, analisar e consolidar informações sobre técnicas de segmentação de vias aéreas usando Deep Learning, com foco em arquiteturas de redes neurais e funções de loss.

## 📦 Conteúdo do Projeto

Este projeto contém três componentes principais:

### 1. **airway_segmentation_agent.py**
Agente de IA que realiza:
- ✅ Buscas web inteligentes sobre segmentação de vias aéreas
- ✅ Extração automática de técnicas e funções de loss
- ✅ Consolidação e análise de múltiplas fontes
- ✅ Geração de relatórios técnicos detalhados

### 2. **airway_segmentation_guide.md**
Guia técnico completo incluindo:
- 📚 Principais arquiteturas (U-Net, V-Net, Transformers)
- 🎯 Funções de loss detalhadas (Dice, Focal, Tversky, etc.)
- 💾 Datasets públicos disponíveis
- 💻 Implementações práticas em Python
- 📊 Métricas de avaliação
- 🛠️ Recomendações para desenvolvimento

### 3. **usage_example.md**
Exemplos práticos de uso:
- 🚀 Como executar o agente
- 🔧 Personalização de buscas
- 💡 Casos de uso específicos
- ⚙️ Configurações avançadas

## 🎯 Principais Características

### Arquiteturas Cobertas

- **U-Net e variantes**: U-Net++, Attention U-Net, ResU-Net
- **Modelos 3D**: V-Net, 3D U-Net, nnU-Net
- **Transformers**: TransUNet, Swin-UNet, SegFormer
- **Híbridos**: CoTr, MedFormer, UNETR

### Funções de Loss Implementadas

#### 1. **Dice Loss**
```python
Dice Loss = 1 - (2 * |X ∩ Y|) / (|X| + |Y|)

✅ Ideal para: Desbalanceamento de classes
✅ Uso: Base para segmentação médica
```

#### 2. **Focal Loss**
```python
Focal Loss = -α(1-p_t)^γ log(p_t)

✅ Ideal para: Exemplos difíceis (bronquíolos finos)
✅ Uso: Complementar ao Dice Loss
```

#### 3. **Tversky Loss**
```python
Tversky = 1 - TP / (TP + α*FN + β*FP)

✅ Ideal para: Controle fino de FP/FN
✅ Uso: Quando ramificações são críticas
```

#### 4. **Boundary Loss**
```python
Boundary Loss baseada em mapas de distância

✅ Ideal para: Precisão de bordas
✅ Uso: Refinar limites das vias aéreas
```

#### 5. **Centerline Dice Loss**
```python
Combina Dice global + Dice na linha central

✅ Ideal para: Estruturas tubulares
✅ Uso: Garantir conectividade da árvore brônquica
```

#### 6. **Combo Loss**
```python
α * Dice Loss + β * Cross-Entropy

✅ Ideal para: Aproveitar vantagens de múltiplas losses
✅ Uso: Configuração padrão recomendada
```

## 🚀 Como Usar

### Passo 1: Instalar Dependências

```bash
pip install anthropic --break-system-packages
```

### Passo 2: Configurar API Key (se necessário)

```python
import os
os.environ['ANTHROPIC_API_KEY'] = 'sua-chave-aqui'
```

### Passo 3: Executar o Agente

```python
from airway_segmentation_agent import AirwaySegmentationAgent

# Criar instância
agent = AirwaySegmentationAgent()

# Executar pipeline completo
report = agent.run_search_pipeline()

# O relatório é salvo automaticamente em:
# /mnt/user-data/outputs/airway_segmentation_report.md
```

### Exemplo de Busca Personalizada

```python
# Definir queries customizadas
custom_queries = [
    "3D U-Net airway segmentation pytorch implementation",
    "Tversky loss function medical imaging",
    "centerline extraction bronchial tree"
]

# Executar com queries personalizadas
report = agent.run_search_pipeline(custom_queries=custom_queries)
```

## 📊 Exemplo de Output

O agente gera um relatório markdown estruturado:

```markdown
# Relatório de Segmentação de Vias Aéreas
**Gerado em:** 04/02/2026 14:30:00
**Buscas realizadas:** 3

## 1. Introdução
...

## 2. Principais Arquiteturas
- U-Net 3D
- Attention U-Net
- TransUNet
...

## 3. Funções de Loss
- Dice Loss: Para desbalanceamento
- Focal Loss: Para exemplos difíceis
- Boundary Loss: Para bordas precisas
...

## 4. Datasets
- ATM'22 Challenge
- EXACT09
- LIDC-IDRI
...

## 5. Métricas
- Dice Score
- Tree Length Detected
- Branch Detection Rate
...
```

## 🔬 Técnicas Detalhadas

### Pipeline Completo de Segmentação

```python
# 1. Pré-processamento
ct_preprocessed = preprocess_ct(
    ct_volume,
    window_center=-450,  # HU para pulmão
    window_width=1500,
    target_spacing=(1.0, 1.0, 1.0)
)

# 2. Modelo
model = UNet3D(
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128, 256)
)

# 3. Loss Function
def combined_loss(pred, target):
    dice = dice_loss(pred, target)
    focal = focal_loss(pred, target)
    boundary = boundary_loss(pred, target)
    
    return 0.5*dice + 0.3*focal + 0.2*boundary

# 4. Treinamento
for epoch in epochs:
    loss = train_epoch(model, dataloader, combined_loss)
    
# 5. Pós-processamento
segmentation = postprocess(
    prediction,
    remove_small_components=True,
    morphological_closing=True
)
```

### Avaliação Completa

```python
metrics = {
    'dice': dice_coefficient(pred, target),
    'sensitivity': recall(pred, target),
    'precision': precision(pred, target),
    'tree_length_detected': centerline_metric(pred, target),
    'branch_detected': count_branches(pred)
}
```

## 📚 Recursos Incluídos

### Implementações Práticas

- ✅ Classes PyTorch para todas as losses
- ✅ Pipeline completo de treinamento
- ✅ Funções de pré e pós-processamento
- ✅ Métricas de avaliação específicas
- ✅ Exemplos de data augmentation

### Guias e Documentação

- ✅ Comparação detalhada de arquiteturas
- ✅ Quando usar cada função de loss
- ✅ Best practices de implementação
- ✅ Troubleshooting comum
- ✅ Referências bibliográficas

## 🎓 Aplicações

### Pesquisa Acadêmica
- Revisão sistemática de técnicas
- Identificação de gaps na literatura
- Benchmarking de métodos

### Desenvolvimento Clínico
- Seleção de arquitetura apropriada
- Configuração de função de loss
- Validação de resultados

### Educação
- Material didático sobre segmentação médica
- Exemplos práticos de implementação
- Compreensão de trade-offs técnicos

## 🔍 Datasets Suportados

| Dataset | Casos | Modalidade | Anotações | Público |
|---------|-------|------------|-----------|---------|
| ATM'22 | 300+ | HRCT | Detalhadas | ✅ |
| EXACT09 | 20 | CT | Benchmark | ✅ |
| LIDC-IDRI | 1018 | CT | Nódulos | ✅ |
| BAS | Variado | CT/Sintético | Completas | ✅ |

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem base
- **Claude API**: Busca e análise inteligente
- **PyTorch**: Framework de deep learning
- **MONAI**: Biblioteca médica
- **SimpleITK**: Processamento de imagens

## 📈 Métricas de Performance

### Métricas Padrão
- **Dice Score**: Sobreposição entre predição e ground truth
- **Sensitivity**: Verdadeiros positivos capturados
- **Precision**: Acurácia das predições positivas

### Métricas Específicas para Vias Aéreas
- **Tree Length Detected**: % da árvore brônquica capturada
- **Branch Detection Rate**: Ramificações identificadas corretamente
- **Centerline Accuracy**: Precisão da linha central

## 🎯 Recomendações por Cenário

### Cenário 1: Recursos Computacionais Limitados
```
Arquitetura: 2.5D U-Net
Loss: Dice Loss
Batch Size: 2-4
Resolução: Reduzida (downsampling)
```

### Cenário 2: Máxima Acurácia
```
Arquitetura: 3D nnU-Net ou TransUNet
Loss: Combo (Dice + Focal + Boundary)
Batch Size: 1-2
Resolução: Original ou isotropic 1mm
```

### Cenário 3: Rápido Protótipo
```
Arquitetura: U-Net 3D padrão
Loss: Dice Loss
Batch Size: 4-8
Resolução: Moderada
```

## 🚨 Desafios Comuns e Soluções

### Desafio 1: Ramificações Finas Perdidas
**Solução**: 
- Usar Focal Loss (γ=2)
- Adicionar Centerline Dice Loss
- Aumentar resolução de entrada

### Desafio 2: Descontinuidades na Árvore
**Solução**:
- Topology-preserving loss
- Pós-processamento morfológico
- Conectividade forçada via grafos

### Desafio 3: Overfitting
**Solução**:
- Data augmentation agressivo
- Dropout/BatchNorm
- Regularização L2
- Early stopping

## 📖 Leitura Recomendada

### Papers Fundamentais
1. U-Net (Ronneberger et al., 2015)
2. V-Net (Milletari et al., 2016)
3. nnU-Net (Isensee et al., 2021)
4. Attention U-Net (Oktay et al., 2018)

### Surveys Recentes
- Deep Learning for Medical Image Segmentation (2023)
- Airway Segmentation: Challenges and Solutions (2024)

## 🤝 Contribuições

Este é um projeto educacional e de pesquisa. Sugestões:
- Adicionar novas arquiteturas
- Implementar novas funções de loss
- Expandir base de conhecimento
- Melhorar documentação

## 📄 Licença

Projeto educacional - Material para pesquisa e aprendizado

## 📧 Suporte

Para dúvidas técnicas:
1. Consultar `airway_segmentation_guide.md`
2. Ver exemplos em `usage_example.md`
3. Executar o agente para buscar informações atualizadas

---

## 🎉 Início Rápido (3 passos)

```python
# 1. Import
from airway_segmentation_agent import AirwaySegmentationAgent

# 2. Criar agente
agent = AirwaySegmentationAgent()

# 3. Executar
report = agent.run_search_pipeline()

# Pronto! Relatório gerado em /mnt/user-data/outputs/
```

---

**Desenvolvido com Claude AI - Anthropic**  
*Última atualização: Fevereiro 2026*
