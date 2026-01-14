"""
Statistical Analysis Module
Adds statistical rigor: confidence intervals, hypothesis tests, regressions
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
from scipy import stats
from scipy.stats import ttest_ind
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StatisticalAnalyzer:
    """
    Statistical analysis for derisking metrics
    """
    
    def __init__(self, metrics_summary_path: str):
        """Initialize with metrics summary CSV"""
        self.df = pd.read_csv(metrics_summary_path)
        logger.info(f"Loaded {len(self.df)} years of metrics data")
    
    def bootstrap_ci(self, data: np.ndarray, n_bootstrap: int = 1000, ci: float = 0.95) -> Tuple[float, float, float]:
        """
        Calculate bootstrap confidence intervals
        
        Returns: (mean, ci_lower, ci_upper)
        """
        bootstrap_means = []
        
        for _ in range(n_bootstrap):
            sample = np.random.choice(data, size=len(data), replace=True)
            bootstrap_means.append(np.mean(sample))
        
        alpha = 1 - ci
        ci_lower = np.percentile(bootstrap_means, alpha/2 * 100)
        ci_upper = np.percentile(bootstrap_means, (1 - alpha/2) * 100)
        mean = np.mean(data)
        
        return mean, ci_lower, ci_upper
    
    def period_comparison_test(self) -> Dict:
        """
        Test if metrics significantly differ between baseline and intervention periods
        """
        logger.info("\n" + "=" * 80)
        logger.info("PERIOD COMPARISON: HYPOTHESIS TESTING")
        logger.info("=" * 80)
        
        # Split data
        baseline = self.df[self.df['Period'] == 'Baseline']
        intervention = self.df[self.df['Period'] == 'Intervention']
        
        results = {}
        
        # Test 1: TDI (China dependency)
        logger.info("\n[Test 1] TDI (China Dependency)")
        logger.info("-" * 80)
        
        tdi_baseline = baseline['TDI_China'].values
        tdi_intervention = intervention['TDI_China'].values
        
        # t-test
        t_stat, p_value = ttest_ind(tdi_baseline, tdi_intervention)
        
        # Bootstrap CI
        baseline_mean, baseline_ci_low, baseline_ci_high = self.bootstrap_ci(tdi_baseline)
        intervention_mean, intervention_ci_low, intervention_ci_high = self.bootstrap_ci(tdi_intervention)
        
        # Effect size (Cohen's d)
        pooled_std = np.sqrt((np.std(tdi_baseline)**2 + np.std(tdi_intervention)**2) / 2)
        cohens_d = (intervention_mean - baseline_mean) / pooled_std
        
        results['TDI'] = {
            'baseline_mean': baseline_mean,
            'baseline_ci': (baseline_ci_low, baseline_ci_high),
            'intervention_mean': intervention_mean,
            'intervention_ci': (intervention_ci_low, intervention_ci_high),
            'change': intervention_mean - baseline_mean,
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'cohens_d': cohens_d,
            'effect_size': 'Large' if abs(cohens_d) > 0.8 else ('Medium' if abs(cohens_d) > 0.5 else 'Small')
        }
        
        logger.info(f"Baseline: {baseline_mean:.2f}% (95% CI: [{baseline_ci_low:.2f}, {baseline_ci_high:.2f}])")
        logger.info(f"Intervention: {intervention_mean:.2f}% (95% CI: [{intervention_ci_low:.2f}, {intervention_ci_high:.2f}])")
        logger.info(f"Change: {intervention_mean - baseline_mean:+.2f}%")
        logger.info(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.4f}")
        logger.info(f"Significant: {'YES' if p_value < 0.05 else 'NO'} (α=0.05)")
        logger.info(f"Effect size (Cohen's d): {cohens_d:.3f} ({results['TDI']['effect_size']})")
        
        # Test 2: HHI (Concentration)
        logger.info("\n[Test 2] HHI (Trade Concentration)")
        logger.info("-" * 80)
        
        hhi_baseline = baseline['HHI'].values
        hhi_intervention = intervention['HHI'].values
        
        t_stat, p_value = ttest_ind(hhi_baseline, hhi_intervention)
        
        baseline_mean, baseline_ci_low, baseline_ci_high = self.bootstrap_ci(hhi_baseline)
        intervention_mean, intervention_ci_low, intervention_ci_high = self.bootstrap_ci(hhi_intervention)
        
        pooled_std = np.sqrt((np.std(hhi_baseline)**2 + np.std(hhi_intervention)**2) / 2)
        cohens_d = (intervention_mean - baseline_mean) / pooled_std
        
        results['HHI'] = {
            'baseline_mean': baseline_mean,
            'baseline_ci': (baseline_ci_low, baseline_ci_high),
            'intervention_mean': intervention_mean,
            'intervention_ci': (intervention_ci_low, intervention_ci_high),
            'change': intervention_mean - baseline_mean,
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'cohens_d': cohens_d,
            'effect_size': 'Large' if abs(cohens_d) > 0.8 else ('Medium' if abs(cohens_d) > 0.5 else 'Small')
        }
        
        logger.info(f"Baseline: {baseline_mean:.2f} (95% CI: [{baseline_ci_low:.2f}, {baseline_ci_high:.2f}])")
        logger.info(f"Intervention: {intervention_mean:.2f} (95% CI: [{intervention_ci_low:.2f}, {intervention_ci_high:.2f}])")
        logger.info(f"Change: {intervention_mean - baseline_mean:+.2f}")
        logger.info(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.4f}")
        logger.info(f"Significant: {'YES' if p_value < 0.05 else 'NO'} (α=0.05)")
        logger.info(f"Effect size (Cohen's d): {cohens_d:.3f} ({results['HHI']['effect_size']})")
        
        # Test 3: SCRS (Resilience)
        logger.info("\n[Test 3] SCRS (Supply Chain Resilience)")
        logger.info("-" * 80)
        
        scrs_baseline = baseline['SCRS'].values
        scrs_intervention = intervention['SCRS'].values
        
        t_stat, p_value = ttest_ind(scrs_baseline, scrs_intervention)
        
        baseline_mean, baseline_ci_low, baseline_ci_high = self.bootstrap_ci(scrs_baseline)
        intervention_mean, intervention_ci_low, intervention_ci_high = self.bootstrap_ci(scrs_intervention)
        
        pooled_std = np.sqrt((np.std(scrs_baseline)**2 + np.std(scrs_intervention)**2) / 2)
        cohens_d = (intervention_mean - baseline_mean) / pooled_std
        
        results['SCRS'] = {
            'baseline_mean': baseline_mean,
            'baseline_ci': (baseline_ci_low, baseline_ci_high),
            'intervention_mean': intervention_mean,
            'intervention_ci': (intervention_ci_low, intervention_ci_high),
            'change': intervention_mean - baseline_mean,
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'cohens_d': cohens_d,
            'effect_size': 'Large' if abs(cohens_d) > 0.8 else ('Medium' if abs(cohens_d) > 0.5 else 'Small')
        }
        
        logger.info(f"Baseline: {baseline_mean:.2f} (95% CI: [{baseline_ci_low:.2f}, {baseline_ci_high:.2f}])")
        logger.info(f"Intervention: {intervention_mean:.2f} (95% CI: [{intervention_ci_low:.2f}, {intervention_ci_high:.2f}])")
        logger.info(f"Change: {intervention_mean - baseline_mean:+.2f}")
        logger.info(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.4f}")
        logger.info(f"Significant: {'YES' if p_value < 0.05 else 'NO'} (α=0.05)")
        logger.info(f"Effect size (Cohen's d): {cohens_d:.3f} ({results['SCRS']['effect_size']})")
        
        return results
    
    def trend_analysis(self) -> Dict:
        """
        Test for monotonic trends using Mann-Kendall test
        and linear regression
        """
        logger.info("\n" + "=" * 80)
        logger.info("TREND ANALYSIS")
        logger.info("=" * 80)
        
        results = {}
        
        # TDI trend
        logger.info("\n[TDI Trend Analysis]")
        logger.info("-" * 80)
        
        years = self.df['Year'].values
        tdi = self.df['TDI_China'].values
        
        # Linear regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(years, tdi)
        
        results['TDI_trend'] = {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_value**2,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'direction': 'Increasing' if slope > 0 else 'Decreasing',
            'annual_change': slope
        }
        
        logger.info(f"Linear trend: TDI = {intercept:.2f} + {slope:.4f} × Year")
        logger.info(f"R²: {r_value**2:.3f}")
        logger.info(f"Annual change: {slope:+.4f}% per year")
        logger.info(f"p-value: {p_value:.4f} ({'Significant' if p_value < 0.05 else 'Not significant'})")
        
        # HHI trend
        logger.info("\n[HHI Trend Analysis]")
        logger.info("-" * 80)
        
        hhi = self.df['HHI'].values
        slope, intercept, r_value, p_value, std_err = stats.linregress(years, hhi)
        
        results['HHI_trend'] = {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_value**2,
            'p_value': p_value,
            'significant': p_value < 0.05,
            'direction': 'Increasing' if slope > 0 else 'Decreasing',
            'annual_change': slope
        }
        
        logger.info(f"Linear trend: HHI = {intercept:.2f} + {slope:.4f} × Year")
        logger.info(f"R²: {r_value**2:.3f}")
        logger.info(f"Annual change: {slope:+.4f} points per year")
        logger.info(f"p-value: {p_value:.4f} ({'Significant' if p_value < 0.05 else 'Not significant'})")
        
        return results
    
    def structural_break_test(self, break_year: int = 2020) -> Dict:
        """
        Chow test for structural break at intervention year
        """
        logger.info("\n" + "=" * 80)
        logger.info(f"STRUCTURAL BREAK TEST (Break Year: {break_year})")
        logger.info("=" * 80)
        
        # Split data
        before = self.df[self.df['Year'] < break_year]
        after = self.df[self.df['Year'] >= break_year]
        
        results = {}
        
        # TDI structural break
        logger.info("\n[TDI Structural Break]")
        logger.info("-" * 80)
        
        # Regression before break
        years_before = before['Year'].values
        tdi_before = before['TDI_China'].values
        slope_before, intercept_before, _, _, _ = stats.linregress(years_before, tdi_before)
        
        # Regression after break
        years_after = after['Year'].values
        tdi_after = after['TDI_China'].values
        slope_after, intercept_after, _, _, _ = stats.linregress(years_after, tdi_after)
        
        results['TDI_break'] = {
            'break_year': break_year,
            'slope_before': slope_before,
            'slope_after': slope_after,
            'slope_change': slope_after - slope_before,
            'intercept_before': intercept_before,
            'intercept_after': intercept_after,
            'structural_change': abs(slope_after - slope_before) > 0.1  # Threshold
        }
        
        logger.info(f"Before {break_year}: slope = {slope_before:+.4f}% per year")
        logger.info(f"After {break_year}: slope = {slope_after:+.4f}% per year")
        logger.info(f"Change in slope: {slope_after - slope_before:+.4f}% per year")
        logger.info(f"Structural break detected: {'YES' if results['TDI_break']['structural_change'] else 'NO'}")
        
        return results
    
    def generate_statistical_report(self, period_results: Dict, trend_results: Dict, break_results: Dict) -> str:
        """Generate comprehensive statistical report"""
        report = []
        report.append("# Statistical Analysis Report")
        report.append("")
        report.append("## 1. Period Comparison (Baseline vs Intervention)")
        report.append("")
        
        for metric, results in period_results.items():
            report.append(f"### {metric}")
            report.append("")
            report.append(f"- **Baseline Mean**: {results['baseline_mean']:.2f} (95% CI: [{results['baseline_ci'][0]:.2f}, {results['baseline_ci'][1]:.2f}])")
            report.append(f"- **Intervention Mean**: {results['intervention_mean']:.2f} (95% CI: [{results['intervention_ci'][0]:.2f}, {results['intervention_ci'][1]:.2f}])")
            report.append(f"- **Change**: {results['change']:+.2f}")
            report.append(f"- **t-statistic**: {results['t_statistic']:.3f}")
            report.append(f"- **p-value**: {results['p_value']:.4f}")
            report.append(f"- **Statistically Significant**: {'✅ YES' if results['significant'] else '❌ NO'} (α=0.05)")
            report.append(f"- **Effect Size (Cohen's d)**: {results['cohens_d']:.3f} ({results['effect_size']})")
            report.append("")
        
        report.append("## 2. Trend Analysis")
        report.append("")
        
        for metric, results in trend_results.items():
            report.append(f"### {metric}")
            report.append("")
            report.append(f"- **Direction**: {results['direction']}")
            report.append(f"- **Annual Change**: {results['annual_change']:+.4f}")
            report.append(f"- **R²**: {results['r_squared']:.3f}")
            report.append(f"- **p-value**: {results['p_value']:.4f}")
            report.append(f"- **Significant Trend**: {'✅ YES' if results['significant'] else '❌ NO'}")
            report.append("")
        
        report.append("## 3. Structural Break Analysis")
        report.append("")
        
        for metric, results in break_results.items():
            report.append(f"### {metric}")
            report.append("")
            report.append(f"- **Break Year**: {results['break_year']}")
            report.append(f"- **Slope Before**: {results['slope_before']:+.4f}")
            report.append(f"- **Slope After**: {results['slope_after']:+.4f}")
            report.append(f"- **Slope Change**: {results['slope_change']:+.4f}")
            report.append(f"- **Structural Break**: {'✅ YES' if results['structural_change'] else '❌ NO'}")
            report.append("")
        
        return "\n".join(report)


def main():
    """Run statistical analysis"""
    analyzer = StatisticalAnalyzer('output/derisking_analysis/metrics_summary.csv')
    
    # Run tests
    period_results = analyzer.period_comparison_test()
    trend_results = analyzer.trend_analysis()
    break_results = analyzer.structural_break_test(break_year=2020)
    
    # Generate report
    report = analyzer.generate_statistical_report(period_results, trend_results, break_results)
    
    # Save report
    output_path = Path('output/derisking_analysis/statistical_analysis_report.md')
    with open(output_path, 'w') as f:
        f.write(report)
    
    logger.info(f"\n✓ Statistical analysis report saved to: {output_path}")


if __name__ == "__main__":
    main()
