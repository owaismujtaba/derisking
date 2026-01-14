#!/usr/bin/env python3
"""
Main script to process India derisking trade data
"""

from src.data_processor import DataProcessor


def main():
    """
    Process trade data: extract ZIPs, concatenate CSVs, and save consolidated file
    """
    print("=" * 80)
    print("INDIA DERISKING TRADE DATA PROCESSOR")
    print("=" * 80)
    
    # Initialize the data processor
    processor = DataProcessor(
        data_dir="data/raw",
        output_dir="data/merged"
    )
    
    # Run the complete processing pipeline
    # extract=True will extract ZIP files first
    output_file = processor.process_all(extract=True)
    
    if output_file:
        print(f"\n{'=' * 80}")
        print("✓ SUCCESS!")
        print(f"{'=' * 80}")
        print(f"\nConsolidated data saved to: {output_file}")
        print(f"File size: {output_file.stat().st_size / (1024*1024):.2f} MB")
    else:
        print("\n✗ Processing failed. Check the logs above for details.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
