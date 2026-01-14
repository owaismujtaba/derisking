#!/usr/bin/env python3
"""
Analyze India's Derisking Project
Main entry point for complete derisking analysis
"""

from src.derisking_analyzer import DeriskingAnalyzer


def main():
    """
    Run complete derisking analysis
    """
    print("=" * 80)
    print("INDIA DERISKING PROJECT ANALYSIS")
    print("=" * 80)
    print()
    print("This analysis measures the effectiveness of India's derisking initiative")
    print("aimed at reducing trade dependency on China.")
    print()
    print("Analysis covers: 2007-2024")
    print("Baseline period: 2007-2019")
    print("Intervention period: 2020-2024 (post-Atmanirbhar Bharat)")
    print()
    print("=" * 80)
    print()
    
    # Run analysis
    analyzer = DeriskingAnalyzer('data/merged/consolidated_trade_data.csv')
    analyzer.run_complete_analysis()
    
    print()
    print("=" * 80)
    print("✓ ANALYSIS COMPLETE")
    print("=" * 80)
    print()
    print("Results saved to: output/derisking_analysis/")
    print()
    print("Key outputs:")
    print("  - analysis_report.md          (Summary report)")
    print("  - metrics_summary.csv         (Time series metrics)")
    print("  - partner_diversification.csv (Trade partner analysis)")
    print("  - sector_analysis.csv         (Strategic sector analysis)")
    print("  - period_comparison.json      (Baseline vs intervention)")
    print()
    
    return 0


if __name__ == "__main__":
    exit(main())
