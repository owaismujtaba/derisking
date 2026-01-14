"""
Sensitivity Analysis Module
Tests robustness of findings against alternative definitions (e.g., including HS 29)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from pathlib import Path
from scipy import stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SensitivityAnalyzer:
    """Run sensitivity checks for Nature revision"""
    
    def __init__(self, data_path: str, output_dir: str = "output/derisking_analysis"):
        self.data_path = Path(data_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.df = pd.read_csv(data_path)
        self.df.columns = self.df.columns.str.strip()
        
        # Define Pandemic Goods (Original Strict Definition)
        self.pandemic_hs = ['22', '28', '29', '30', '34', '38', '39', '40', '62', '63', '65', '90']
        
    def run_hs29_test(self):
        """
        Test: Does the 'Digital Paradox' (acceleration) hold if we include 
        HS 29 (Organic Chemicals) in the Non-Pandemic basket?
        
        The reviewer suggests HS 29 shouldn't be excluded as 'pandemic' 
        because it's also a structural success story.
        """
        logger.info("\n[Sensitivity] Running HS 29 Inclusion Test...")
        
        # Definition 1: Original (Exclude All Pandemic)
        exclude_original = self.pandemic_hs
        
        # Definition 2: Sensitivity (Exclude All EXCEPT HS 29)
        exclude_sensitivity = [code for code in self.pandemic_hs if code != '29']
        
        # Calculate Trends
        res_orig = self._calculate_trend(exclude_original, "Original (Excl HS 29)")
        res_sens = self._calculate_trend(exclude_sensitivity, "Sensitivity (Incl HS 29)")
        
        # Compare Slopes
        logger.info("\nRESULTS:")
        logger.info(f"Original Slope (Post-2020): {res_orig['slope_post']:.4f}")
        logger.info(f"Sensitivity Slope (Post-2020): {res_sens['slope_post']:.4f}")
        
        # Plot
        self._plot_sensitivity(res_orig, res_sens)
        
        # Save Results
        pd.DataFrame([res_orig, res_sens]).to_csv(self.output_dir / 'sensitivity_hs29.csv', index=False)

    def _calculate_trend(self, excluded_codes, label):
        """Calculate TDI trend excluding specific codes"""
        # Filter Logic
        # Convert ProductCode to string 2-digit matching
        mask = ~self.df['ProductCode'].astype(str).str.pad(2, fillchar='0').isin(excluded_codes)
        subset = self.df[mask]
        
        # Get India Imports
        # Assuming Partner=IND, Flow=Export based on previous analysis data structure
        india_imports = subset[
            (subset['PartnerISO3'] == 'IND') & 
            (subset['TradeFlowName'] == 'Export')
        ]
        
        years = sorted(india_imports['Year'].unique())
        tdi_values = []
        
        for y in years:
            yd = india_imports[india_imports['Year'] == y]
            total = yd['TradeValue in 1000 USD'].sum()
            chn = yd[yd['ReporterISO3'] == 'CHN']['TradeValue in 1000 USD'].sum()
            tdi = (chn / total * 100) if total > 0 else 0
            tdi_values.append(tdi)
            
        # Calculate Slopes
        y_arr = np.array(years)
        t_arr = np.array(tdi_values)
        
        # Post-2020 Slope
        post_mask = y_arr >= 2020
        slope_post, _, _, _, _ = stats.linregress(y_arr[post_mask], t_arr[post_mask])
        
        # Pre-2020 Slope
        pre_mask = y_arr < 2020
        slope_pre, _, _, _, _ = stats.linregress(y_arr[pre_mask], t_arr[pre_mask])
        
        return {
            'Label': label,
            'slope_pre': slope_pre,
            'slope_post': slope_post,
            'acceleration': slope_post - slope_pre,
            'years': years,
            'tdi': tdi_values
        }

    def _plot_sensitivity(self, res1, res2):
        """Plot sensitivity comparison"""
        plt.style.use('seaborn-v0_8-whitegrid')
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Original
        ax.plot(res1['years'], res1['tdi'], 'o-', label=f"{res1['Label']} (Slope={res1['slope_post']:.2f})", color='#E64B35')
        
        # Sensitivity
        ax.plot(res2['years'], res2['tdi'], 's--', label=f"{res2['Label']} (Slope={res2['slope_post']:.2f})", color='#4DBBD5')
        
        ax.axvline(x=2020, color='black', linestyle=':', alpha=0.5)
        ax.set_title('Figure 9: Sensitivity Analysis - Effect of HS 29 Inclusion\nDoes re-adding Organic Chemicals change the trend?', fontweight='bold')
        ax.set_ylabel('Trade Dependency Index (%)')
        ax.set_xlabel('Year')
        ax.legend()
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'figures/figure9_sensitivity_hs29.png', dpi=300)
        logger.info("Saved Figure 9")

def main():
    analyzer = SensitivityAnalyzer('data/merged/consolidated_trade_data.csv')
    analyzer.run_hs29_test()

if __name__ == "__main__":
    main()
