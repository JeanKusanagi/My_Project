"""
Agente de IA para Busca e Análise de Segmentação de Vias Aéreas
================================================================

Este agente realiza buscas inteligentes sobre técnicas de segmentação de vias aéreas,
focando em arquiteturas de redes neurais e funções de loss utilizadas.
"""

import os
import json
import re
from datetime import datetime
from typing import List, Dict, Any, Optional
import anthropic


class AirwaySegmentationAgent:
    """
    Agente especializado em buscar e analisar informações sobre segmentação de vias aéreas.
    """
    
    def __init__(self):
        """Inicializa o agente com conhecimento sobre o domínio."""
        self.client = anthropic.Anthropic()
        self.model = "claude-sonnet-4-20250514"
        
        # Base de conhecimento sobre técnicas comuns
        self.techniques_db = {
            "architectures": [
                "U-Net", "U-Net++", "Attention U-Net", "ResU-Net",
                "V-Net", "3D U-Net", "nnU-Net", "TransUNet",
                "Swin-UNet", "SegFormer", "DeepLabV3+"
            ],
            "loss_functions": [
                "Dice Loss", "Cross-Entropy Loss", "Focal Loss",
                "Tversky Loss", "Combo Loss", "Weighted Cross-Entropy",
                "Boundary Loss", "Topology-Preserving Loss",
                "Centerline Dice Loss", "Clipped Dice Loss"
            ],
            "imaging_modalities": [
                "CT (Computed Tomography)", "HRCT (High-Resolution CT)",
                "MRI", "X-Ray"
            ]
        }
        
        # Queries de busca especializadas
        self.search_queries = [
            "airway segmentation deep learning techniques",
            "airway tree segmentation loss function",
            "bronchial tree segmentation neural network",
            "pulmonary airway segmentation U-Net",
            "trachea bronchus segmentation CNN",
            "3D airway segmentation medical imaging"
        ]
    
    def search_literature(self, query: str) -> Dict[str, Any]:
        """
        Realiza busca na web sobre um tópico específico de segmentação de vias aéreas.
        
        Args:
            query: Termo de busca
            
        Returns:
            Dicionário com resultados estruturados
        """
        print(f"\n🔍 Buscando: {query}")
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            tools=[
                {
                    "type": "web_search_20250305",
                    "name": "web_search"
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": f"""Busque informações recentes e detalhadas sobre: {query}

Foque em:
1. Arquiteturas de redes neurais utilizadas
2. Funções de loss específicas para segmentação de vias aéreas
3. Datasets públicos disponíveis
4. Métricas de avaliação (Dice Score, Sensitivity, etc.)
5. Desafios e soluções propostas

Retorne APENAS um JSON estruturado sem preamble ou markdown:
{{
    "techniques": ["lista de técnicas encontradas"],
    "loss_functions": ["funções de loss mencionadas"],
    "datasets": ["datasets citados"],
    "metrics": ["métricas de avaliação"],
    "key_findings": ["descobertas principais"],
    "sources": ["URLs ou referências"]
}}"""
                }
            ]
        )
        
        # Extrair conteúdo da resposta
        full_text = ""
        for block in response.content:
            if block.type == "text":
                full_text += block.text
        
        # Tentar parsear o JSON
        try:
            # Remover markdown se presente
            clean_text = re.sub(r'```json\s*|\s*```', '', full_text).strip()
            result = json.loads(clean_text)
            return result
        except json.JSONDecodeError:
            print("⚠️ Não foi possível parsear JSON, retornando texto bruto")
            return {"raw_response": full_text}
    
    def analyze_techniques(self, search_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analisa os resultados de busca e consolida informações sobre técnicas.
        
        Args:
            search_results: Lista de resultados das buscas
            
        Returns:
            Análise consolidada
        """
        print("\n📊 Analisando técnicas encontradas...")
        
        # Consolidar todas as técnicas e funções de loss
        all_techniques = set()
        all_losses = set()
        all_datasets = set()
        all_metrics = set()
        
        for result in search_results:
            if isinstance(result, dict):
                all_techniques.update(result.get("techniques", []))
                all_losses.update(result.get("loss_functions", []))
                all_datasets.update(result.get("datasets", []))
                all_metrics.update(result.get("metrics", []))
        
        return {
            "unique_techniques": sorted(list(all_techniques)),
            "unique_loss_functions": sorted(list(all_losses)),
            "unique_datasets": sorted(list(all_datasets)),
            "unique_metrics": sorted(list(all_metrics)),
            "total_searches": len(search_results)
        }
    
    def generate_report(self, analysis: Dict[str, Any]) -> str:
        """
        Gera relatório detalhado sobre as técnicas de segmentação encontradas.
        
        Args:
            analysis: Análise consolidada
            
        Returns:
            Relatório em formato markdown
        """
        print("\n📝 Gerando relatório...")
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=6000,
            messages=[
                {
                    "role": "user",
                    "content": f"""Com base nos seguintes dados sobre segmentação de vias aéreas, 
crie um relatório técnico detalhado em português:

{json.dumps(analysis, indent=2, ensure_ascii=False)}

O relatório deve incluir:
1. Introdução à segmentação de vias aéreas
2. Principais arquiteturas de deep learning utilizadas
3. Funções de loss específicas e suas vantagens
4. Datasets disponíveis para treinamento
5. Métricas de avaliação padrão
6. Recomendações práticas para implementação

Use formato markdown com seções bem organizadas."""
                }
            ]
        )
        
        report = ""
        for block in response.content:
            if block.type == "text":
                report += block.text
        
        return report
    
    def run_search_pipeline(self, custom_queries: Optional[List[str]] = None) -> str:
        """
        Executa pipeline completo de busca e análise.
        
        Args:
            custom_queries: Queries personalizadas (opcional)
            
        Returns:
            Relatório final
        """
        print("=" * 70)
        print("🤖 AGENTE DE SEGMENTAÇÃO DE VIAS AÉREAS")
        print("=" * 70)
        
        queries = custom_queries or self.search_queries
        search_results = []
        
        # Fase 1: Buscar informações
        print("\n📚 FASE 1: Coletando informações...")
        for query in queries[:3]:  # Limitar a 3 buscas para não exceder limites
            try:
                result = self.search_literature(query)
                search_results.append(result)
            except Exception as e:
                print(f"❌ Erro na busca '{query}': {str(e)}")
        
        # Fase 2: Analisar resultados
        print("\n🔬 FASE 2: Analisando resultados...")
        analysis = self.analyze_techniques(search_results)
        
        print(f"\n✅ Encontradas:")
        print(f"   - {len(analysis['unique_techniques'])} técnicas únicas")
        print(f"   - {len(analysis['unique_loss_functions'])} funções de loss únicas")
        print(f"   - {len(analysis['unique_datasets'])} datasets únicos")
        
        # Fase 3: Gerar relatório
        print("\n📄 FASE 3: Gerando relatório final...")
        report = self.generate_report(analysis)
        
        # Adicionar metadados ao relatório
        final_report = f"""# Relatório de Segmentação de Vias Aéreas
**Gerado em:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
**Buscas realizadas:** {len(search_results)}

---

{report}

---

## Dados Brutos da Análise

### Técnicas Identificadas
{chr(10).join(f'- {t}' for t in analysis['unique_techniques'])}

### Funções de Loss Identificadas
{chr(10).join(f'- {l}' for l in analysis['unique_loss_functions'])}

### Datasets Mencionados
{chr(10).join(f'- {d}' for d in analysis['unique_datasets'])}

### Métricas de Avaliação
{chr(10).join(f'- {m}' for m in analysis['unique_metrics'])}

---

*Relatório gerado automaticamente pelo Agente de Segmentação de Vias Aéreas*
"""
        
        return final_report
    
    def search_specific_topic(self, topic: str) -> str:
        """
        Busca informações sobre um tópico específico.
        
        Args:
            topic: Tópico para buscar
            
        Returns:
            Resumo das informações encontradas
        """
        print(f"\n🎯 Busca direcionada: {topic}")
        
        result = self.search_literature(topic)
        
        # Gerar resumo
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""Resuma as informações encontradas sobre '{topic}' 
em formato claro e objetivo:

{json.dumps(result, indent=2, ensure_ascii=False)}"""
                }
            ]
        )
        
        summary = ""
        for block in response.content:
            if block.type == "text":
                summary += block.text
        
        return summary


def main():
    """Função principal para demonstração do agente."""
    
    print("\n" + "="*70)
    print("🚀 INICIANDO AGENTE DE SEGMENTAÇÃO DE VIAS AÉREAS")
    print("="*70)
    
    # Criar instância do agente
    agent = AirwaySegmentationAgent()
    
    # Executar pipeline completo
    report = agent.run_search_pipeline()
    
    # Salvar relatório
    output_path = "/mnt/user-data/outputs/airway_segmentation_report.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Relatório salvo em: {output_path}")
    print("\n" + "="*70)
    print("🎉 ANÁLISE CONCLUÍDA!")
    print("="*70)
    
    return output_path


if __name__ == "__main__":
    # Executar agente
    report_path = main()
    print(f"\n📊 Confira o relatório completo: {report_path}")
