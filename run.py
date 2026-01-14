#!/usr/bin/env python3
"""
India Derisking Project - Main Runner
Executes the complete analysis pipeline from data processing to report generation
"""

import sys
import argparse
from pathlib import Path
from src.data_processor import DataProcessor
from src.derisking_analyzer import DeriskingAnalyzer


def print_header(text: str):
    """Print formatted header"""
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")


def print_step(step_num: int, total_steps: int, description: str):
    """Print step information"""
    print(f"\n[Step {step_num}/{total_steps}] {description}")
    print("-" * 80)


def run_data_processing(skip_extraction: bool = False):
    """
    Run data processing pipeline
    
    Args:
        skip_extraction: Skip ZIP extraction if CSVs already exist
    """
    print_step(1, 3, "DATA PROCESSING")
    
    processor = DataProcessor(data_dir="data/raw", output_dir="data/merged")
    
    if skip_extraction:
        print("⏭️  Skipping ZIP extraction (using existing CSVs)")
    else:
        print("📦 Extracting ZIP files...")
        processor.extract_zip_files()
    
    print("\n📊 Concatenating CSV files...")
    output_file = processor.concatenate_csv_files()
    
    if output_file:
        print(f"\n✅ Data processing complete!")
        print(f"   Output: {output_file}")
        
        # Show summary
        summary = processor.get_data_summary(output_file)
        print(f"\n   Summary:")
        print(f"   - Total rows: {summary.get('total_rows', 0):,}")
        print(f"   - Years: {summary.get('year_range', 'N/A')}")
        print(f"   - File size: {output_file.stat().st_size / (1024*1024):.2f} MB")
        
        # Cleanup
        print("\n🧹 Cleaning up temporary files...")
        processor.cleanup_extracted_files()
        
        return True
    else:
        print("\n❌ Data processing failed!")
        return False


def run_derisking_analysis():
    """Run derisking analysis"""
    print_step(2, 3, "DERISKING ANALYSIS")
    
    # Check if consolidated data exists
    data_file = Path("data/merged/consolidated_trade_data.csv")
    if not data_file.exists():
        print(f"❌ Error: Consolidated data file not found: {data_file}")
        print("   Please run data processing first.")
        return False
    
    print("📈 Running derisking metrics analysis...")
    analyzer = DeriskingAnalyzer(str(data_file))
    analyzer.run_complete_analysis()
    
    print("\n✅ Analysis complete!")
    return True


def show_results():
    """Display results summary"""
    print_step(3, 3, "RESULTS SUMMARY")
    
    report_file = Path("output/derisking_analysis/analysis_report.md")
    
    if report_file.exists():
        print("📄 Generated Reports:")
        print(f"   - Analysis Report: {report_file}")
        print(f"   - Metrics Summary: output/derisking_analysis/metrics_summary.csv")
        print(f"   - Partner Analysis: output/derisking_analysis/partner_diversification.csv")
        print(f"   - Sector Analysis: output/derisking_analysis/sector_analysis.csv")
        print(f"   - Full Report: DERISKING_REPORT.md")
        
        # Show quick summary
        print("\n📊 Quick Results:")
        try:
            with open(report_file, 'r') as f:
                lines = f.readlines()
                in_summary = False
                for line in lines:
                    if '## Executive Summary' in line:
                        in_summary = True
                    elif in_summary and line.startswith('##'):
                        break
                    elif in_summary and line.strip():
                        print(f"   {line.rstrip()}")
        except Exception as e:
            print(f"   Could not read summary: {e}")
    else:
        print("⚠️  Analysis report not found")
    
    return True


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description='India Derisking Project - Complete Analysis Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run complete pipeline
  %(prog)s --skip-extraction  # Skip ZIP extraction (use existing CSVs)
  %(prog)s --analysis-only    # Run only analysis (skip data processing)
        """
    )
    
    parser.add_argument(
        '--skip-extraction',
        action='store_true',
        help='Skip ZIP extraction step (use existing CSV files)'
    )
    
    parser.add_argument(
        '--analysis-only',
        action='store_true',
        help='Run only derisking analysis (skip data processing)'
    )
    
    parser.add_argument(
        '--process-only',
        action='store_true',
        help='Run only data processing (skip analysis)'
    )
    
    args = parser.parse_args()
    
    # Print welcome header
    print_header("INDIA DERISKING PROJECT")
    print("Measuring India's Trade Derisking Initiative (2007-2024)")
    print("Novel Multi-Metric Framework with 7 Complementary Indicators")
    
    try:
        # Step 1: Data Processing
        if not args.analysis_only:
            success = run_data_processing(skip_extraction=args.skip_extraction)
            if not success:
                print("\n❌ Pipeline failed at data processing stage")
                return 1
            
            if args.process_only:
                print_header("PROCESSING COMPLETE")
                return 0
        
        # Step 2: Derisking Analysis
        success = run_derisking_analysis()
        if not success:
            print("\n❌ Pipeline failed at analysis stage")
            return 1
        
        # Step 3: COVID Disentanglement (New Step)
        print("\n🦠 Running COVID-19 Disentanglement Analysis...")
        import src.covid_disentanglement as covid
        covid.main()
        
        # Step 4: Visualizations (New Step)
        print("\n📊 Generating Nature-Quality Visualizations...")
        import src.visualizations as viz
        viz.main()
        
        # Final Results Summary
        show_results()
        
        # Final summary
        print_header("✅ PIPELINE COMPLETE")
        print("All analysis results and figures are available in:")
        print("  - output/derisking_analysis/")
        print("  - output/derisking_analysis/figures/ (New High-Res Plots)")
        print("  - DERISKING_REPORT.md")
        print("\nTo re-run analysis:")
        print("  python3 run.py --analysis-only")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrupted by user")
        return 130
    except Exception as e:
        print(f"\n\n❌ Pipeline failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
