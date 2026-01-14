#!/usr/bin/env python3
"""
Script to check for missing years in India derisking trade data
"""

import csv
import glob
from collections import defaultdict

def check_years_in_csv(filename):
    """Extract and analyze years from a CSV file"""
    years = set()
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'Year' in row:
                try:
                    year = int(row['Year'])
                    years.add(year)
                except (ValueError, KeyError):
                    continue
    
    return sorted(years)

def main():
    csv_files = sorted(glob.glob('data/DataJobID-*.csv'))
    
    print("=" * 80)
    print("INDIA DERISKING DATA - YEAR ANALYSIS")
    print("=" * 80)
    
    all_years = set()
    file_years = {}
    
    for csv_file in csv_files:
        years = check_years_in_csv(csv_file)
        file_years[csv_file] = years
        all_years.update(years)
        
        print(f"\n📄 {csv_file}")
        print(f"   Years found: {years}")
        if years:
            print(f"   Range: {min(years)} - {max(years)}")
            print(f"   Total: {len(years)} years")
            
            # Check for gaps within the range
            if years:
                full_range = set(range(min(years), max(years) + 1))
                missing = sorted(full_range - set(years))
                if missing:
                    print(f"   ⚠️  MISSING YEARS IN RANGE: {missing}")
                else:
                    print(f"   ✓ No gaps in year range")
    
    print("\n" + "=" * 80)
    print("OVERALL SUMMARY")
    print("=" * 80)
    
    if all_years:
        all_years_sorted = sorted(all_years)
        print(f"\nAll years across all files: {all_years_sorted}")
        print(f"Overall range: {min(all_years_sorted)} - {max(all_years_sorted)}")
        print(f"Total unique years: {len(all_years_sorted)}")
        
        # Check for missing years in overall range
        full_range = set(range(min(all_years_sorted), max(all_years_sorted) + 1))
        missing_overall = sorted(full_range - all_years)
        
        if missing_overall:
            print(f"\n⚠️  MISSING YEARS IN OVERALL RANGE: {missing_overall}")
        else:
            print(f"\n✓ No missing years in overall range")
            
        # Expected range based on conversation history (2018-2025)
        expected_years = set(range(2018, 2026))  # 2018-2025 inclusive
        if all_years_sorted:
            actual_min = min(all_years_sorted)
            actual_max = max(all_years_sorted)
            
            if actual_min < 2018 or actual_max > 2025:
                print(f"\n📊 Note: Data extends beyond expected 2018-2025 range")
                print(f"   Actual range: {actual_min}-{actual_max}")
            
            missing_from_expected = sorted(expected_years - all_years)
            if missing_from_expected:
                print(f"\n⚠️  MISSING YEARS FROM EXPECTED 2018-2025 RANGE: {missing_from_expected}")
    else:
        print("\n⚠️  No year data found in any files!")

if __name__ == "__main__":
    main()
