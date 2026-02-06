# Guia Técnico: Segmentação de Vias Aéreas

## 📋 Índice
1. [Introdução](#introdução)
2. [Principais Arquiteturas](#principais-arquiteturas)
3. [Funções de Loss](#funções-de-loss)
4. [Datasets Comuns](#datasets-comuns)
5. [Implementação Prática](#implementação-prática)

---

## Introdução

A segmentação de vias aéreas é uma tarefa crucial em análise de imagens médicas, especialmente em tomografias computadorizadas (CT) do tórax. O objetivo é identificar e delinear automaticamente a árvore brônquica, desde a traqueia até os bronquíolos mais finos.

### Desafios Principais

- **Estruturas finas e ramificadas**: As vias aéreas diminuem progressivamente de diâmetro
- **Baixo contraste**: Dificuldade em distinguir vias aéreas de tecidos adjacentes
- **Artefatos de imagem**: Ruído e artefatos podem confundir o modelo
- **Variabilidade anatômica**: Diferenças entre pacientes

---

## Principais Arquiteturas

### 1. **U-Net e Variantes**

A U-Net é a arquitetura base para segmentação médica:

```
Características:
- Encoder-decoder com skip connections
- Preserva informações de diferentes escalas
- Eficiente para imagens médicas

Variantes populares:
- U-Net++ (nested skip connections)
- Attention U-Net (mecanismos de atenção)
- ResU-Net (blocos residuais)
```

**Vantagens para vias aéreas:**
- Skip connections preservam detalhes das estruturas finas
- Captura contexto em múltiplas escalas
- Treinamento eficiente com poucos dados

### 2. **V-Net e 3D U-Net**

Extensões 3D para processamento volumétrico:

```
Características:
- Convoluções 3D
- Processa volumes completos
- Melhor compreensão espacial

Aplicação:
- Ideal para CT torácica (dados volumétricos)
- Captura continuidade das vias aéreas em 3D
```

### 3. **nnU-Net**

Framework auto-configurável:

```
Características:
- Configuração automática de hiperparâmetros
- Adaptação ao dataset
- Estado da arte em várias tarefas

Pontos fortes:
- Não requer expertise em ajuste fino
- Generaliza bem para diferentes modalidades
```

### 4. **Transformers para Segmentação**

Arquiteturas baseadas em atenção:

```
Exemplos:
- TransUNet
- Swin-UNet
- SegFormer

Vantagens:
- Modelagem de dependências de longo alcance
- Captura relações globais na imagem
```

---

## Funções de Loss

### 1. **Dice Loss**

A função de loss mais popular para segmentação médica:

```python
def dice_loss(pred, target, smooth=1e-6):
    """
    Dice Loss = 1 - Dice Coefficient
    
    Dice = 2 * |X ∩ Y| / (|X| + |Y|)
    """
    intersection = (pred * target).sum()
    union = pred.sum() + target.sum()
    
    dice = (2.0 * intersection + smooth) / (union + smooth)
    return 1 - dice
```

**Por que funciona bem para vias aéreas:**
- Lida com desbalanceamento de classes (vias aéreas são pequena parte da imagem)
- Foca em sobreposição entre predição e ground truth
- Derivável e otimizável

### 2. **Focal Loss**

Focada em exemplos difíceis:

```python
def focal_loss(pred, target, alpha=0.25, gamma=2.0):
    """
    FL = -α(1-p_t)^γ log(p_t)
    
    α: balanceia classes
    γ: foca em exemplos difíceis
    """
    bce = F.binary_cross_entropy(pred, target, reduction='none')
    p_t = pred * target + (1 - pred) * (1 - target)
    focal = alpha * (1 - p_t) ** gamma * bce
    
    return focal.mean()
```

**Uso em vias aéreas:**
- Útil para bronquíolos finos (pixels difíceis de classificar)
- Reduz influência de regiões fáceis (background)

### 3. **Tversky Loss**

Generalização do Dice Loss com controle de FP/FN:

```python
def tversky_loss(pred, target, alpha=0.7, beta=0.3, smooth=1e-6):
    """
    TL = 1 - Tversky Index
    
    TI = TP / (TP + α*FN + β*FP)
    
    α: peso para falsos negativos
    β: peso para falsos positivos
    """
    tp = (pred * target).sum()
    fp = (pred * (1 - target)).sum()
    fn = ((1 - pred) * target).sum()
    
    tversky = (tp + smooth) / (tp + alpha*fn + beta*fp + smooth)
    return 1 - tversky
```

**Aplicação específica:**
- α > β: penaliza mais falsos negativos (importante para não perder ramificações)
- Ajustável conforme objetivo clínico

### 4. **Boundary Loss**

Focada em bordas e limites:

```python
def boundary_loss(pred, target):
    """
    Penaliza erros próximos às bordas
    Usa mapas de distância
    """
    # Calcular mapa de distância do ground truth
    dist_map = calculate_distance_transform(target)
    
    # Multiplicar predições pelo mapa de distância
    loss = (pred * dist_map).sum()
    
    return loss
```

**Benefício para vias aéreas:**
- Melhora precisão das bordas
- Crucial para ramificações finas

### 5. **Centerline Dice Loss**

Específica para estruturas tubulares:

```python
def centerline_dice_loss(pred, target, centerline):
    """
    Combina Dice tradicional com Dice ao longo da linha central
    
    Centerline: esqueleto da árvore brônquica
    """
    # Dice global
    dice_global = dice_coefficient(pred, target)
    
    # Dice na região da linha central
    centerline_region = dilate(centerline, radius=3)
    pred_cl = pred * centerline_region
    target_cl = target * centerline_region
    dice_centerline = dice_coefficient(pred_cl, target_cl)
    
    # Combinação
    return 1 - (0.5 * dice_global + 0.5 * dice_centerline)
```

**Por que é importante:**
- Garante conectividade da árvore brônquica
- Evita descontinuidades

### 6. **Combo Loss**

Combinação de múltiplas losses:

```python
def combo_loss(pred, target, alpha=0.5, beta=0.5):
    """
    Combina Dice Loss e Cross-Entropy
    """
    dice = dice_loss(pred, target)
    ce = F.binary_cross_entropy(pred, target)
    
    return alpha * dice + beta * ce
```

**Estratégia comum:**
- Dice: foca em sobreposição global
- CE: otimiza pixel a pixel
- Combinação aproveita vantagens de ambas

---

## Datasets Comuns

### 1. **ATM'22 (Airway Tree Modeling)**
- Challenge de segmentação de vias aéreas
- CT de alta resolução
- Anotações detalhadas

### 2. **LIDC-IDRI**
- 1018 casos de CT torácica
- Originalmente para detecção de nódulos
- Útil para pré-treinamento

### 3. **EXACT09**
- Dataset antigo mas importante
- 20 casos de CT
- Benchmark estabelecido

### 4. **BAS (Bronchus Airway Segmentation)**
- Dados sintéticos e reais
- Várias resoluções
- Útil para validação

---

## Implementação Prática

### Pipeline Típico

```python
import torch
import torch.nn as nn
from monai.networks.nets import UNet

class AirwaySegmentationPipeline:
    def __init__(self):
        # 1. Definir modelo
        self.model = UNet(
            spatial_dims=3,
            in_channels=1,
            out_channels=1,
            channels=(16, 32, 64, 128, 256),
            strides=(2, 2, 2, 2),
        )
        
        # 2. Definir função de loss
        self.dice_loss = DiceLoss()
        self.focal_loss = FocalLoss()
        
        # 3. Otimizador
        self.optimizer = torch.optim.Adam(
            self.model.parameters(), 
            lr=1e-4
        )
    
    def combined_loss(self, pred, target):
        """Loss combinada para melhor performance"""
        dice = self.dice_loss(pred, target)
        focal = self.focal_loss(pred, target)
        
        # Peso balanceado
        return 0.7 * dice + 0.3 * focal
    
    def train_step(self, batch):
        """Um passo de treinamento"""
        images, masks = batch
        
        # Forward
        predictions = self.model(images)
        loss = self.combined_loss(predictions, masks)
        
        # Backward
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        return loss.item()
```

### Pré-processamento Recomendado

```python
def preprocess_ct(ct_volume):
    """
    Pré-processamento padrão para CT torácica
    """
    # 1. Windowing (ajuste de contraste)
    ct_windowed = window_ct(
        ct_volume, 
        window_center=-450,  # HU para pulmão
        window_width=1500
    )
    
    # 2. Normalização
    ct_normalized = (ct_windowed - ct_windowed.mean()) / ct_windowed.std()
    
    # 3. Resampling para resolução uniforme
    ct_resampled = resample_volume(
        ct_normalized,
        target_spacing=(1.0, 1.0, 1.0)  # 1mm isotropic
    )
    
    return ct_resampled
```

### Pós-processamento

```python
def postprocess_segmentation(pred_mask, min_volume=100):
    """
    Pós-processamento para refinar segmentação
    """
    # 1. Threshold
    binary_mask = (pred_mask > 0.5).astype(int)
    
    # 2. Remover componentes pequenos
    labeled = label(binary_mask)
    props = regionprops(labeled)
    
    for region in props:
        if region.area < min_volume:
            binary_mask[labeled == region.label] = 0
    
    # 3. Preservar maior componente conectado (traqueia)
    labeled = label(binary_mask)
    largest_cc = labeled == (np.bincount(labeled.flat)[1:].argmax() + 1)
    
    # 4. Morfologia para suavizar
    smoothed = morphology.binary_closing(largest_cc, ball(2))
    
    return smoothed
```

### Métricas de Avaliação

```python
def evaluate_segmentation(pred, target):
    """
    Métricas padrão para segmentação de vias aéreas
    """
    metrics = {}
    
    # Dice Score
    metrics['dice'] = dice_coefficient(pred, target)
    
    # Sensitivity (Recall)
    tp = (pred * target).sum()
    fn = ((1 - pred) * target).sum()
    metrics['sensitivity'] = tp / (tp + fn + 1e-6)
    
    # Precision
    fp = (pred * (1 - target)).sum()
    metrics['precision'] = tp / (tp + fp + 1e-6)
    
    # Tree Length Detected (específico para vias aéreas)
    centerline_pred = skeletonize_3d(pred)
    centerline_target = skeletonize_3d(target)
    metrics['tree_length_detected'] = (
        centerline_pred * centerline_target
    ).sum() / centerline_target.sum()
    
    # Branch Detected (número de ramificações capturadas)
    metrics['branches_detected'] = count_branches(centerline_pred)
    
    return metrics
```

---

## Recomendações Práticas

### 1. **Escolha da Arquitetura**

Para vias aéreas:
- **Começar com**: 3D U-Net ou nnU-Net
- **Se computação limitada**: 2.5D U-Net (patches 3D pequenos)
- **Para SOTA**: Experimentar Transformers (TransUNet)

### 2. **Escolha da Loss Function**

Recomendação hierárquica:
1. **Base**: Dice Loss
2. **Melhorar ramificações**: Combo Loss (Dice + Focal)
3. **Refinar bordas**: Adicionar Boundary Loss
4. **Garantir conectividade**: Centerline Dice Loss

### 3. **Estratégias de Treinamento**

```python
# Progressive training
epochs_stage1 = 50  # Apenas Dice Loss
epochs_stage2 = 30  # Adicionar Focal Loss
epochs_stage3 = 20  # Adicionar Boundary Loss

# Learning rate scheduling
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer,
    mode='min',
    factor=0.5,
    patience=5
)
```

### 4. **Data Augmentation**

Técnicas recomendadas:
- Rotações (±15°)
- Translações
- Elastic deformations (cuidado para não distorcer anatomia)
- Ajustes de intensidade
- Crop aleatório

---

## Referências e Recursos

### Papers Fundamentais
- Ronneberger et al. (2015) - U-Net original
- Milletari et al. (2016) - V-Net e Dice Loss
- Isensee et al. (2021) - nnU-Net

### Bibliotecas Úteis
- **MONAI**: Framework médico para PyTorch
- **TorchIO**: Augmentation para imagens médicas
- **SimpleITK**: Processamento de imagens médicas

### Competitions
- ATM Challenge (MICCAI)
- EXACT09 Challenge

---

*Documento técnico sobre segmentação de vias aéreas usando Deep Learning*
*Versão 1.0 - Fevereiro 2026*
