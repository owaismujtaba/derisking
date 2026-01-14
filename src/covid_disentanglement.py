"""
COVID-19 Disentanglement Analysis
Separates pandemic effects from policy effects
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class COVIDDisentangler:
    """
    Disentangle COVID-19 effects from policy effects
    """
    
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        self.df = pd.read_csv(data_path)
        self.df.columns = self.df.columns.str.strip()
        
        # Define pandemic-sensitive HS codes (User Provided List)
        self.pandemic_sensitive_hs = {
            '22': 'Beverages, spirits, vinegar (alcohol for sanitizers)',
            '28': 'Inorganic chemicals; gases (medical oxygen)',
            '29': 'Organic chemicals (disinfectants/drugs)',
            '30': 'Pharmaceutical products (vaccines, medicines)',
            '34': 'Soap, cleaning, polishing preparations (sanitizers)',
            '38': 'Miscellaneous chemical products (disinfectants)',
            '39': 'Plastics and articles thereof (PPE components)',
            '40': 'Rubber and articles thereof (medical gloves)',
            '62': 'Articles of apparel, not knitted (medical gowns)',
            '63': 'Other made-up textile articles (face masks)',
            '65': 'Headgear and parts thereof (protective caps)',
            '90': 'Optical, medical, surgical instruments'
        }
        
        logger.info(f"Loaded {len(self.df)} records for COVID disentanglement")
    
    def exclude_pandemic_goods(self) -> pd.DataFrame:
        """
        Exclude pandemic-sensitive HS codes
        """
        # Filter out pandemic-sensitive sectors
        pandemic_codes = list(self.pandemic_sensitive_hs.keys())
        
        non_pandemic_df = self.df[~self.df['ProductCode'].astype(str).str[:2].isin(pandemic_codes)]
        
        logger.info(f"Excluded pandemic goods: {len(self.df) - len(non_pandemic_df)} records removed")
        logger.info(f"Remaining records: {len(non_pandemic_df)}")
        
        return non_pandemic_df
    
    def calculate_tdi_excluding_pandemic(self) -> pd.DataFrame:
        """
        Calculate TDI excluding pandemic-sensitive goods
        """
        logger.info("\n" + "=" * 80)
        logger.info("TDI CALCULATION EXCLUDING PANDEMIC-SENSITIVE GOODS")
        logger.info("=" * 80)
        
        # Get non-pandemic data
        non_pandemic_df = self.exclude_pandemic_goods()
        
        # Filter for India's imports
        india_imports = non_pandemic_df[
            (non_pandemic_df['PartnerISO3'] == 'IND') &
            (non_pandemic_df['TradeFlowName'] == 'Export')
        ]
        
        results = []
        
        for year in sorted(india_imports['Year'].unique()):
            year_data = india_imports[india_imports['Year'] == year]
            
            # Total imports
            total_imports = year_data['TradeValue in 1000 USD'].sum()
            
            # China imports
            china_imports = year_data[
                year_data['ReporterISO3'] == 'CHN'
            ]['TradeValue in 1000 USD'].sum()
            
            # TDI
            tdi = (china_imports / total_imports * 100) if total_imports > 0 else 0
            
            results.append({
                'Year': year,
                'TDI_Excluding_Pandemic': tdi,
                'China_Imports': china_imports,
                'Total_Imports': total_imports
            })
            
            logger.info(f"{year}: TDI = {tdi:.2f}%")
        
        return pd.DataFrame(results)
    
    def compare_with_vs_without_pandemic_goods(self, original_tdi: pd.DataFrame) -> dict:
        """
        Compare TDI with and without pandemic-sensitive goods
        """
        logger.info("\n" + "=" * 80)
        logger.info("COMPARISON: WITH vs WITHOUT PANDEMIC GOODS")
        logger.info("=" * 80)
        
        # Calculate excluding pandemic
        tdi_excl_pandemic = self.calculate_tdi_excluding_pandemic()
        
        # Merge with original
        comparison = original_tdi.merge(
            tdi_excl_pandemic[['Year', 'TDI_Excluding_Pandemic']],
            on='Year',
            how='left'
        )
        
        # Calculate difference
        comparison['Pandemic_Effect'] = comparison['TDI_China'] - comparison['TDI_Excluding_Pandemic']
        
        # Period analysis
        baseline = comparison[comparison['Year'] < 2020]
        intervention = comparison[comparison['Year'] >= 2020]
        
        results = {
            'baseline': {
                'tdi_with_pandemic': baseline['TDI_China'].mean(),
                'tdi_without_pandemic': baseline['TDI_Excluding_Pandemic'].mean(),
                'pandemic_effect': baseline['Pandemic_Effect'].mean()
            },
            'intervention': {
                'tdi_with_pandemic': intervention['TDI_China'].mean(),
                'tdi_without_pandemic': intervention['TDI_Excluding_Pandemic'].mean(),
                'pandemic_effect': intervention['Pandemic_Effect'].mean()
            }
        }
        
        logger.info("\nBASELINE PERIOD (2007-2019):")
        logger.info(f"  TDI with pandemic goods: {results['baseline']['tdi_with_pandemic']:.2f}%")
        logger.info(f"  TDI without pandemic goods: {results['baseline']['tdi_without_pandemic']:.2f}%")
        logger.info(f"  Pandemic effect: {results['baseline']['pandemic_effect']:.2f}%")
        
        logger.info("\nINTERVENTION PERIOD (2020-2024):")
        logger.info(f"  TDI with pandemic goods: {results['intervention']['tdi_with_pandemic']:.2f}%")
        logger.info(f"  TDI without pandemic goods: {results['intervention']['tdi_without_pandemic']:.2f}%")
        logger.info(f"  Pandemic effect: {results['intervention']['pandemic_effect']:.2f}%")
        
        # Test if trend persists without pandemic goods
        tdi_excl = tdi_excl_pandemic['TDI_Excluding_Pandemic'].values
        years = tdi_excl_pandemic['Year'].values
        
        # Pre-2020 trend
        pre_mask = years < 2020
        slope_pre, _, _, _, _ = stats.linregress(years[pre_mask], tdi_excl[pre_mask])
        
        # Post-2020 trend
        post_mask = years >= 2020
        slope_post, _, _, _, _ = stats.linregress(years[post_mask], tdi_excl[post_mask])
        
        results['trend_analysis'] = {
            'slope_pre_2020': slope_pre,
            'slope_post_2020': slope_post,
            'acceleration': slope_post - slope_pre,
            'trend_persists': slope_post > slope_pre
        }
        
        logger.info("\nTREND ANALYSIS (EXCLUDING PANDEMIC GOODS):")
        logger.info(f"  Pre-2020 slope: {slope_pre:+.4f}%/year")
        logger.info(f"  Post-2020 slope: {slope_post:+.4f}%/year")
        logger.info(f"  Acceleration: {slope_post - slope_pre:+.4f}%/year")
        logger.info(f"  Trend persists: {'YES' if results['trend_analysis']['trend_persists'] else 'NO'}")
        
        # Save comparison
        output_path = Path('output/derisking_analysis/covid_disentanglement.csv')
        comparison.to_csv(output_path, index=False)
        logger.info(f"\n✓ Saved comparison to: {output_path}")
        
        return results
    
    def generate_report(self, results: dict) -> str:
        """Generate COVID disentanglement report"""
        report = []
        report.append("# COVID-19 Disentanglement Analysis")
        report.append("")
        report.append("## Objective")
        report.append("")
        report.append("Separate the 'COVID Effect' from the 'Policy Effect' by excluding pandemic-sensitive HS codes.")
        report.append("")
        report.append("## Pandemic-Sensitive Sectors Excluded")
        report.append("")
        for code, desc in self.pandemic_sensitive_hs.items():
            report.append(f"- **HS {code}**: {desc}")
        report.append("")
        report.append("## Results")
        report.append("")
        report.append("### Period Comparison")
        report.append("")
        report.append("| Period | TDI (with pandemic) | TDI (without pandemic) | Pandemic Effect |")
        report.append("|--------|---------------------|------------------------|-----------------|")
        report.append(f"| Baseline | {results['baseline']['tdi_with_pandemic']:.2f}% | {results['baseline']['tdi_without_pandemic']:.2f}% | {results['baseline']['pandemic_effect']:.2f}% |")
        report.append(f"| Intervention | {results['intervention']['tdi_with_pandemic']:.2f}% | {results['intervention']['tdi_without_pandemic']:.2f}% | {results['intervention']['pandemic_effect']:.2f}% |")
        report.append("")
        report.append("### Trend Analysis (Excluding Pandemic Goods)")
        report.append("")
        report.append(f"- **Pre-2020 slope**: {results['trend_analysis']['slope_pre_2020']:+.4f}%/year")
        report.append(f"- **Post-2020 slope**: {results['trend_analysis']['slope_post_2020']:+.4f}%/year")
        report.append(f"- **Acceleration**: {results['trend_analysis']['acceleration']:+.4f}%/year")
        report.append("")
        report.append("## Conclusion")
        report.append("")
        if results['trend_analysis']['trend_persists']:
            report.append("✅ **The upward trend in TDI PERSISTS even after excluding pandemic-sensitive goods.**")
            report.append("")
            report.append("This suggests that the increase in China dependency is NOT solely due to COVID-19 demand spikes,")
            report.append("but reflects a broader structural trend that the derisking policy failed to reverse.")
        else:
            report.append("⚠️ **The upward trend is primarily driven by pandemic-sensitive goods.**")
            report.append("")
            report.append("This suggests that COVID-19 demand spikes significantly contributed to the observed increase.")
        
        return "\n".join(report)


def main():
    """Run COVID disentanglement analysis"""
    
    # Load original TDI results
    original_tdi = pd.read_csv('output/derisking_analysis/metrics_summary.csv')
    
    # Run disentanglement
    disentangler = COVIDDisentangler('data/merged/consolidated_trade_data.csv')
    results = disentangler.compare_with_vs_without_pandemic_goods(original_tdi)
    
    # Generate report
    report = disentangler.generate_report(results)
    
    # Save report
    output_path = Path('output/derisking_analysis/covid_disentanglement_report.md')
    with open(output_path, 'w') as f:
        f.write(report)
    
    logger.info(f"\n✓ COVID disentanglement report saved to: {output_path}")


if __name__ == "__main__":
    main()
