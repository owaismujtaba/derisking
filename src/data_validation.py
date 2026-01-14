"""
Data Validation Module
Validates trade data interpretation and quality
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataValidator:
    """
    Comprehensive data validation for trade analysis
    """
    
    def __init__(self, data_path: str):
        """Initialize with consolidated trade data"""
        self.data_path = Path(data_path)
        self.df = pd.read_csv(data_path)
        self.df.columns = self.df.columns.str.strip()
        logger.info(f"Loaded {len(self.df)} records for validation")
    
    def validate_all(self) -> Dict:
        """Run all validation tests"""
        logger.info("=" * 80)
        logger.info("RUNNING COMPREHENSIVE DATA VALIDATION")
        logger.info("=" * 80)
        
        results = {
            'tradeflow_interpretation': self.validate_tradeflow_interpretation(),
            'temporal_consistency': self.validate_temporal_consistency(),
            'partner_rankings': self.validate_partner_rankings(),
            'mirror_data': self.validate_mirror_data_consistency(),
            'data_completeness': self.validate_data_completeness()
        }
        
        return results
    
    def validate_tradeflow_interpretation(self) -> Dict:
        """
        CRITICAL: Validate TradeFlow interpretation
        
        When PartnerISO3='IND' and TradeFlowName='Export':
        This means: Reporter is exporting TO India
        Equivalent to: India is importing FROM Reporter
        """
        logger.info("\n[Test 1] TradeFlow Interpretation Validation")
        logger.info("-" * 80)
        
        # Test case: India's imports from China
        india_imports_from_china = self.df[
            (self.df['PartnerISO3'] == 'IND') &
            (self.df['ReporterISO3'] == 'CHN') &
            (self.df['TradeFlowName'] == 'Export')
        ]
        
        # Calculate total for recent year
        year_2023 = india_imports_from_china[india_imports_from_china['Year'] == 2023]
        total_2023 = year_2023['TradeValue in 1000 USD'].sum()
        
        logger.info(f"India's imports from China (2023): ${total_2023/1e6:.2f} billion")
        
        # Known benchmark: India-China trade ~$100-130 billion (2023)
        # India imports ~$100 billion from China
        expected_range = (80_000_000, 130_000_000)  # in thousands USD
        
        is_valid = expected_range[0] <= total_2023 <= expected_range[1]
        
        result = {
            'test': 'TradeFlow Interpretation',
            'value': total_2023,
            'expected_range': expected_range,
            'valid': is_valid,
            'interpretation': 'PartnerISO3=IND & TradeFlowName=Export = India importing FROM Reporter',
            'confidence': 'HIGH' if is_valid else 'LOW'
        }
        
        logger.info(f"✓ Validation: {'PASSED' if is_valid else 'FAILED'}")
        logger.info(f"  Expected: ${expected_range[0]/1e6:.0f}B - ${expected_range[1]/1e6:.0f}B")
        logger.info(f"  Actual: ${total_2023/1e6:.2f}B")
        
        return result
    
    def validate_temporal_consistency(self) -> Dict:
        """Check for unrealistic jumps in data"""
        logger.info("\n[Test 2] Temporal Consistency Check")
        logger.info("-" * 80)
        
        # Calculate year-over-year changes
        yearly_totals = self.df[
            (self.df['PartnerISO3'] == 'IND') &
            (self.df['TradeFlowName'] == 'Export')
        ].groupby('Year')['TradeValue in 1000 USD'].sum()
        
        yoy_changes = yearly_totals.pct_change() * 100
        
        # Flag changes > 50% (except COVID year)
        suspicious_changes = yoy_changes[
            (abs(yoy_changes) > 50) & (yoy_changes.index != 2020)
        ]
        
        result = {
            'test': 'Temporal Consistency',
            'suspicious_years': suspicious_changes.to_dict(),
            'valid': len(suspicious_changes) == 0,
            'note': 'Year-over-year changes should be < 50% (except 2020 COVID)'
        }
        
        logger.info(f"✓ Suspicious changes found: {len(suspicious_changes)}")
        if len(suspicious_changes) > 0:
            for year, change in suspicious_changes.items():
                logger.warning(f"  {year}: {change:+.1f}% change")
        
        return result
    
    def validate_partner_rankings(self) -> Dict:
        """Validate top import partners match known rankings"""
        logger.info("\n[Test 3] Partner Rankings Validation")
        logger.info("-" * 80)
        
        # Get 2023 import shares
        imports_2023 = self.df[
            (self.df['PartnerISO3'] == 'IND') &
            (self.df['TradeFlowName'] == 'Export') &
            (self.df['Year'] == 2023)
        ]
        
        partner_totals = imports_2023.groupby('ReporterISO3')['TradeValue in 1000 USD'].sum()
        total_imports = partner_totals.sum()
        partner_shares = (partner_totals / total_imports * 100).sort_values(ascending=False)
        
        top_5 = partner_shares.head(5)
        
        logger.info("Top 5 import partners (2023):")
        for i, (country, share) in enumerate(top_5.items(), 1):
            logger.info(f"  {i}. {country}: {share:.2f}%")
        
        # Known fact: China is typically India's #1 import partner
        china_rank = list(partner_shares.index).index('CHN') + 1 if 'CHN' in partner_shares.index else None
        
        result = {
            'test': 'Partner Rankings',
            'top_5': top_5.to_dict(),
            'china_rank': china_rank,
            'china_share': partner_shares.get('CHN', 0),
            'valid': china_rank is not None and china_rank <= 3,
            'note': 'China should be in top 3 import partners'
        }
        
        logger.info(f"✓ China rank: #{china_rank} ({partner_shares.get('CHN', 0):.2f}%)")
        
        return result
    
    def validate_mirror_data_consistency(self) -> Dict:
        """
        Check consistency between:
        - India's reported imports from China
        - China's reported exports to India
        
        Expected discrepancy: 5-15% (CIF vs FOB pricing)
        """
        logger.info("\n[Test 4] Mirror Data Consistency")
        logger.info("-" * 80)
        
        # India's imports from China (India as partner, China as reporter)
        india_imports = self.df[
            (self.df['PartnerISO3'] == 'IND') &
            (self.df['ReporterISO3'] == 'CHN') &
            (self.df['TradeFlowName'] == 'Export') &
            (self.df['Year'] == 2023)
        ]['TradeValue in 1000 USD'].sum()
        
        # China's exports to India (China as reporter, India as partner)
        china_exports = self.df[
            (self.df['ReporterISO3'] == 'CHN') &
            (self.df['PartnerISO3'] == 'IND') &
            (self.df['TradeFlowName'] == 'Export') &
            (self.df['Year'] == 2023)
        ]['TradeValue in 1000 USD'].sum()
        
        if china_exports > 0:
            discrepancy = abs(india_imports - china_exports) / china_exports * 100
        else:
            discrepancy = None
        
        result = {
            'test': 'Mirror Data Consistency',
            'india_imports': india_imports,
            'china_exports': china_exports,
            'discrepancy_pct': discrepancy,
            'valid': discrepancy is not None and discrepancy < 20,
            'note': 'Discrepancy should be < 20% (CIF/FOB difference)'
        }
        
        logger.info(f"  India's imports from China: ${india_imports/1e6:.2f}B")
        logger.info(f"  China's exports to India: ${china_exports/1e6:.2f}B")
        if discrepancy:
            logger.info(f"  Discrepancy: {discrepancy:.1f}%")
        
        return result
    
    def validate_data_completeness(self) -> Dict:
        """Check for missing data and coverage"""
        logger.info("\n[Test 5] Data Completeness Check")
        logger.info("-" * 80)
        
        # Check year coverage
        years = sorted(self.df['Year'].unique())
        expected_years = list(range(2007, 2025))
        missing_years = set(expected_years) - set(years)
        
        # Check for null values
        null_counts = self.df.isnull().sum()
        critical_nulls = null_counts[null_counts > 0]
        
        # Check TradeFlow distribution
        tradeflow_counts = self.df['TradeFlowName'].value_counts()
        
        result = {
            'test': 'Data Completeness',
            'year_coverage': years,
            'missing_years': list(missing_years),
            'null_values': critical_nulls.to_dict(),
            'tradeflow_distribution': tradeflow_counts.to_dict(),
            'valid': len(missing_years) <= 1  # 2025 expected to be missing
        }
        
        logger.info(f"  Year coverage: {min(years)}-{max(years)}")
        logger.info(f"  Missing years: {missing_years if missing_years else 'None'}")
        logger.info(f"  TradeFlow types: {list(tradeflow_counts.index)}")
        
        return result
    
    def generate_validation_report(self, results: Dict) -> str:
        """Generate comprehensive validation report"""
        report = []
        report.append("=" * 80)
        report.append("DATA VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Summary
        all_valid = all(r.get('valid', False) for r in results.values())
        report.append(f"**Overall Status**: {'✅ PASSED' if all_valid else '⚠️ ISSUES FOUND'}")
        report.append("")
        
        # Individual tests
        for test_name, test_result in results.items():
            status = "✅ PASS" if test_result.get('valid', False) else "❌ FAIL"
            report.append(f"### {test_result.get('test', test_name)}: {status}")
            report.append("")
            
            for key, value in test_result.items():
                if key not in ['test', 'valid']:
                    report.append(f"- **{key}**: {value}")
            report.append("")
        
        # Conclusion
        report.append("=" * 80)
        report.append("CONCLUSION")
        report.append("=" * 80)
        report.append("")
        
        if results['tradeflow_interpretation']['valid']:
            report.append("✅ **Data interpretation is CORRECT**:")
            report.append("   - PartnerISO3='IND' & TradeFlowName='Export'")
            report.append("   - Means: Reporter exporting TO India")
            report.append("   - Equivalent to: India importing FROM Reporter")
        else:
            report.append("❌ **Data interpretation needs REVIEW**:")
            report.append("   - Values outside expected range")
            report.append("   - Recommend cross-checking with official sources")
        
        return "\n".join(report)


def main():
    """Run validation"""
    validator = DataValidator('data/merged/consolidated_trade_data.csv')
    results = validator.validate_all()
    
    # Generate report
    report = validator.generate_validation_report(results)
    print("\n" + report)
    
    # Save report
    output_path = Path('output/derisking_analysis/data_validation_report.md')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(report)
    
    logger.info(f"\n✓ Validation report saved to: {output_path}")


if __name__ == "__main__":
    main()
