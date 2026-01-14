"""
Digital Correlation Analyzer
Correlates Digital Infrastructure Metrics (Proxy) with Tech Imports (HS 85)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging
from scipy import stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DigitalCorrelation:
    def __init__(self, trade_path: str, proxy_path: str, output_dir: str = "output/derisking_analysis"):
        self.trade_path = Path(trade_path)
        self.proxy_path = Path(proxy_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.figures_dir = self.output_dir / "figures"
        self.figures_dir.mkdir(parents=True, exist_ok=True)

    def run_analysis(self):
        logger.info("[Digital] Running Correlation Analysis...")
        
        # 1. Load Trade Data (HS 85 Imports from China)
        # Note: We need aggregate HS 85 imports (volume) or TDI? The reviewer asks for "Surge in HS 85/84 imports".
        # Let's track Total Import Value of HS 85 from World (Demand) and China (Dependency).
        
        df_trade = pd.read_csv(self.trade_path)
        df_trade.columns = df_trade.columns.str.strip()
        
        # Filter HS 85 (Electronics) | Reporter=IND or Partner=IND (Export flow)
        # Assuming Data has Partner=IND, Flow=Export for India Imports
        # Need to be careful with dataset structure.
        
        # Logic: Get India Imports of HS 85
        # 1. Filter: Partner=IND, Flow=Export (Reporters exporting to India)
        # 2. Filter: ProductCode starts with '85'
        
        # Check ProductCode format. It seems to be 2-digit int or string.
        # "85" might be int 85.
        
        hs85_imports = []
        years = range(2014, 2025)
        
        for y in years:
            # We need *Total* imports of HS 85 to represent "Demand" created by digitization
            # (Partner=IND, Flow=Export, Product=85)
            
            subset = df_trade[
                (df_trade['PartnerISO3'] == 'IND') & 
                (df_trade['TradeFlowName'] == 'Export') & 
                (df_trade['Year'] == y)
            ]
            
            # Filter product 85
            # Product codes can be mixed. We saw '85' in prev turns.
            # Safe way: convert to string and check
            
            tech_subset = subset[subset['ProductCode'].astype(str) == '85']
            val = tech_subset['TradeValue in 1000 USD'].sum()
            
            # Also get HS 84
            mech_subset = subset[subset['ProductCode'].astype(str) == '84']
            val_84 = mech_subset['TradeValue in 1000 USD'].sum()
            
            hs85_imports.append({
                'Year': y,
                'HS85_Value': val / 1e6, # Billions
                'HS84_Value': val_84 / 1e6 # Billions
            })
            
        df_imports = pd.DataFrame(hs85_imports)
        
        # 2. Load Proxy Data
        df_proxy = pd.read_csv(self.proxy_path)
        
        # 3. Merge
        merged = pd.merge(df_imports, df_proxy, on='Year')
        
        if len(merged) < 5:
            logger.warning("Not enough data for correlation.")
            return

        # 4. Correlation
        r_sub, p_sub = stats.pearsonr(merged['Subscribers_Millions'], merged['HS85_Value'])
        r_dat, p_dat = stats.pearsonr(merged['Data_Usage_GB_Per_User'], merged['HS85_Value'])
        
        logger.info(f"Correlation (Subscribers vs HS85): r={r_sub:.2f}, p={p_sub:.4f}")
        logger.info(f"Correlation (Data Usage vs HS85): r={r_dat:.2f}, p={p_dat:.4f}")
        
        # 5. Plot
        self._plot_correlation(merged, r_sub, p_sub)
        
        # Save stats
        with open(self.output_dir / "digital_correlation_stats.txt", "w") as f:
            f.write(f"Correlation Analysis Results\n")
            f.write(f"HS 85 Imports vs Digital Subscribers: r={r_sub:.4f}, p={p_sub:.4f}\n")
            f.write(f"HS 85 Imports vs Data Usage: r={r_dat:.4f}, p={p_dat:.4f}\n")

    def _plot_correlation(self, df, r, p):
        fig, ax1 = plt.subplots(figsize=(10, 6))
        
        color = 'tab:red'
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Electronics Imports (HS 85) [$ Billion]', color=color)
        ax1.plot(df['Year'], df['HS85_Value'], 'o-', color=color, linewidth=2, label='HS 85 Imports')
        ax1.tick_params(axis='y', labelcolor=color)
        
        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('4G/5G Subscribers (Millions) [Proxy]', color=color)
        ax2.plot(df['Year'], df['Subscribers_Millions'], 's--', color=color, linewidth=2, label='Digital Subs')
        ax2.tick_params(axis='y', labelcolor=color)
        
        plt.title(f'Figure 10: The Digital Paradox Mechanism\nCorrelation(Import Vol, Digital Subs) = {r:.2f} (p<{p:.3f})', fontweight='bold')
        
        fig.tight_layout()
        plt.savefig(self.figures_dir / 'figure10_digital_correlation.png', dpi=300)
        logger.info("Saved Figure 10")

def main():
    analyzer = DigitalCorrelation(
        'data/merged/consolidated_trade_data.csv',
        'data/external/digital_subscribers_proxy.csv'
    )
    analyzer.run_analysis()

if __name__ == "__main__":
    main()
