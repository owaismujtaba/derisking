"""
Derisking Analyzer
Main analysis orchestrator for India's derisking project
"""

import csv
import json
from pathlib import Path
from typing import Dict, List
import logging
from src.metrics_calculator import DeriskingMetrics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import pdb

class DeriskingAnalyzer:
    """
    Orchestrate complete derisking analysis
    """
    
    def __init__(self, data_path: str, output_dir: str = "output/derisking_analysis"):
        """
        Initialize analyzer
        
        Args:
            data_path: Path to consolidated trade data
            output_dir: Directory for output files
        """
        self.calculator = DeriskingMetrics(data_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Define analysis periods
        self.baseline_start = 2007
        self.baseline_end = 2019
        self.intervention_start = 2020
        self.intervention_end = 2024
        
        logger.info(f"Analyzer initialized. Output: {self.output_dir}")
    
    def run_complete_analysis(self):
        """Run all analyses and generate reports"""
        logger.info("=" * 80)
        logger.info("STARTING COMPLETE DERISKING ANALYSIS")
        logger.info("=" * 80)
        
        # 1. Time series analysis
        logger.info("\n[1/5] Calculating time series metrics...")
        metrics_summary = self.analyze_time_series()
        pdb.set_trace()
        self._save_csv(metrics_summary, "metrics_summary.csv")
        
        # 2. Partner diversification analysis
        logger.info("\n[2/5] Analyzing partner diversification...")
        partner_analysis = self.analyze_partner_diversification()
        self._save_csv(partner_analysis, "partner_diversification.csv")
        
        # 3. Sector analysis
        logger.info("\n[3/5] Analyzing strategic sectors...")
        sector_analysis = self.analyze_strategic_sectors()
        self._save_csv(sector_analysis, "sector_analysis.csv")
        
        # 4. Period comparison
        logger.info("\n[4/5] Comparing baseline vs intervention periods...")
        comparison = self.compare_periods()
        self._save_json(comparison, "period_comparison.json")
        
        # 5. Generate summary report
        logger.info("\n[5/5] Generating summary report...")
        self.generate_report(metrics_summary, partner_analysis, comparison)
        
        logger.info("\n" + "=" * 80)
        logger.info("ANALYSIS COMPLETE")
        logger.info(f"Results saved to: {self.output_dir}")
        logger.info("=" * 80)
    
    def analyze_time_series(self) -> List[Dict]:
        """Calculate all metrics for each year"""
        results = []
        
        for year in range(self.baseline_start, self.intervention_end + 1):
            logger.info(f"  Processing year {year}...")
            
            row = {
                'Year': year,
                'Period': 'Baseline' if year <= self.baseline_end else 'Intervention',
                'TDI_China': self.calculator.calculate_tdi(year, 'CHN'),
                'HHI': self.calculator.calculate_hhi(year),
                'SCRS': self.calculator.calculate_scrs(year)
            }
            pdb.set_trace()
            results.append(row)
        
        return results
    
    def analyze_partner_diversification(self) -> List[Dict]:
        """Analyze trade partner shares over time"""
        results = []
        
        # Key partners to track
        partners = {
            'CHN': 'China',
            'USA': 'United States',
            'ARE': 'UAE',
            'SAU': 'Saudi Arabia',
            'IRQ': 'Iraq',
            'CHE': 'Switzerland',
            'KOR': 'South Korea',
            'JPN': 'Japan',
            'DEU': 'Germany',
            'SGP': 'Singapore'
        }
        
        for year in range(self.baseline_start, self.intervention_end + 1):
            shares = self.calculator._get_partner_shares(year)
            
            for iso, name in partners.items():
                results.append({
                    'Year': year,
                    'Partner_ISO': iso,
                    'Partner_Name': name,
                    'Import_Share': shares.get(iso, 0.0)
                })
        
        return results
    
    def analyze_strategic_sectors(self) -> List[Dict]:
        """Analyze dependency in strategic sectors"""
        results = []
        
        # Define strategic sectors (HS 2-digit codes)
        sectors = {
            '84': {'name': 'Machinery & Mechanical Appliances', 'criticality': 5},
            '85': {'name': 'Electrical Machinery & Equipment', 'criticality': 5},
            '29': {'name': 'Organic Chemicals', 'criticality': 4},
            '30': {'name': 'Pharmaceutical Products', 'criticality': 5},
            '39': {'name': 'Plastics', 'criticality': 3},
            '72': {'name': 'Iron & Steel', 'criticality': 4},
            '90': {'name': 'Optical & Medical Instruments', 'criticality': 4}
        }
        
        for year in [2019, 2024]:  # Compare key years
            for code, info in sectors.items():
                ssvi = self.calculator.calculate_ssvi(
                    year, 
                    [code], 
                    info['criticality']
                )
                
                results.append({
                    'Year': year,
                    'Sector_Code': code,
                    'Sector_Name': info['name'],
                    'Criticality': info['criticality'],
                    'SSVI': ssvi
                })
        
        return results
    
    def compare_periods(self) -> Dict:
        """Compare baseline vs intervention periods"""
        baseline_mid = 2015  # Mid-point of baseline
        intervention_mid = 2022  # Mid-point of intervention
        
        comparison = {
            'baseline_period': f"{self.baseline_start}-{self.baseline_end}",
            'intervention_period': f"{self.intervention_start}-{self.intervention_end}",
            'metrics': {}
        }
        
        # TDI comparison
        tdi_baseline = self.calculator.calculate_tdi(baseline_mid, 'CHN')
        tdi_intervention = self.calculator.calculate_tdi(intervention_mid, 'CHN')
        comparison['metrics']['TDI'] = {
            'baseline': float(tdi_baseline),
            'intervention': float(tdi_intervention),
            'change': float(tdi_intervention - tdi_baseline),
            'improvement': 'Yes' if tdi_baseline > tdi_intervention else 'No'
        }
        
        # HHI comparison
        hhi_baseline = self.calculator.calculate_hhi(baseline_mid)
        hhi_intervention = self.calculator.calculate_hhi(intervention_mid)
        comparison['metrics']['HHI'] = {
            'baseline': float(hhi_baseline),
            'intervention': float(hhi_intervention),
            'change': float(hhi_intervention - hhi_baseline),
            'improvement': 'Yes' if hhi_baseline > hhi_intervention else 'No'
        }
        
        # CPODS
        cpods = self.calculator.calculate_cpods(baseline_mid, intervention_mid)
        comparison['metrics']['CPODS'] = {
            'value': float(cpods),
            'interpretation': 'Successful' if cpods > 1 else 'Partial'
        }
        
        # SCRS comparison
        scrs_baseline = self.calculator.calculate_scrs(baseline_mid)
        scrs_intervention = self.calculator.calculate_scrs(intervention_mid)
        comparison['metrics']['SCRS'] = {
            'baseline': float(scrs_baseline),
            'intervention': float(scrs_intervention),
            'change': float(scrs_intervention - scrs_baseline),
            'improvement': 'Yes' if scrs_intervention > scrs_baseline else 'No'
        }
        
        return comparison
    
    def generate_report(self, metrics_summary: List[Dict], 
                       partner_analysis: List[Dict],
                       comparison: Dict):
        """Generate markdown summary report"""
        report_path = self.output_dir / "analysis_report.md"
        
        with open(report_path, 'w') as f:
            f.write("# India Derisking Analysis Report\n\n")
            f.write(f"**Analysis Period**: {self.baseline_start}-{self.intervention_end}\n\n")
            f.write(f"**Baseline Period**: {self.baseline_start}-{self.baseline_end}\n\n")
            f.write(f"**Intervention Period**: {self.intervention_start}-{self.intervention_end}\n\n")
            
            f.write("---\n\n")
            f.write("## Executive Summary\n\n")
            
            # TDI summary
            tdi_data = comparison['metrics']['TDI']
            f.write(f"### Trade Dependency on China\n\n")
            f.write(f"- **Baseline**: {tdi_data['baseline']:.2f}%\n")
            f.write(f"- **Current**: {tdi_data['intervention']:.2f}%\n")
            f.write(f"- **Change**: {tdi_data['change']:+.2f}%\n")
            f.write(f"- **Status**: {'✅ Improved' if tdi_data['improvement'] else '❌ Worsened'}\n\n")
            
            # HHI summary
            hhi_data = comparison['metrics']['HHI']
            f.write(f"### Trade Diversification (HHI)\n\n")
            f.write(f"- **Baseline**: {hhi_data['baseline']:.2f}\n")
            f.write(f"- **Current**: {hhi_data['intervention']:.2f}\n")
            f.write(f"- **Change**: {hhi_data['change']:+.2f}\n")
            f.write(f"- **Status**: {'✅ More Diversified' if hhi_data['improvement'] else '❌ More Concentrated'}\n\n")
            
            # CPODS summary
            cpods_data = comparison['metrics']['CPODS']
            f.write(f"### China-Plus-One Strategy\n\n")
            f.write(f"- **CPODS Score**: {cpods_data['value']:.2f}\n")
            f.write(f"- **Interpretation**: {cpods_data['interpretation']}\n\n")
            
            # SCRS summary
            scrs_data = comparison['metrics']['SCRS']
            f.write(f"### Supply Chain Resilience\n\n")
            f.write(f"- **Baseline**: {scrs_data['baseline']:.2f}\n")
            f.write(f"- **Current**: {scrs_data['intervention']:.2f}\n")
            f.write(f"- **Change**: {scrs_data['change']:+.2f}\n")
            f.write(f"- **Status**: {'✅ Improved' if scrs_data['improvement'] else '❌ Declined'}\n\n")
            
            f.write("---\n\n")
            f.write("## Key Findings\n\n")
            
            # Top partners
            f.write("### Top Import Partners (2024)\n\n")
            partners_2024 = [p for p in partner_analysis if p['Year'] == 2024]
            partners_2024.sort(key=lambda x: x['Import_Share'], reverse=True)
            
            f.write("| Rank | Country | Import Share |\n")
            f.write("|------|---------|-------------|\n")
            for i, partner in enumerate(partners_2024[:10], 1):
                f.write(f"| {i} | {partner['Partner_Name']} | {partner['Import_Share']:.2f}% |\n")
            
            f.write("\n---\n\n")
            f.write("## Data Files\n\n")
            f.write("- [metrics_summary.csv](file:///home/owais/projects/derisking/output/derisking_analysis/metrics_summary.csv)\n")
            f.write("- [partner_diversification.csv](file:///home/owais/projects/derisking/output/derisking_analysis/partner_diversification.csv)\n")
            f.write("- [sector_analysis.csv](file:///home/owais/projects/derisking/output/derisking_analysis/sector_analysis.csv)\n")
            f.write("- [period_comparison.json](file:///home/owais/projects/derisking/output/derisking_analysis/period_comparison.json)\n")
        
        logger.info(f"Report generated: {report_path}")
    
    def _save_csv(self, data: List[Dict], filename: str):
        """Save data to CSV"""
        if not data:
            logger.warning(f"No data to save for {filename}")
            return
        
        filepath = self.output_dir / filename
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        logger.info(f"  Saved: {filepath}")
    
    def _save_json(self, data: Dict, filename: str):
        """Save data to JSON"""
        filepath = self.output_dir / filename
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"  Saved: {filepath}")


def main():
    """Run complete derisking analysis"""
    analyzer = DeriskingAnalyzer('data/merged/consolidated_trade_data.csv')
    analyzer.run_complete_analysis()


if __name__ == "__main__":
    main()
