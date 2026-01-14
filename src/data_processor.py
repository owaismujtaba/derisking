"""
Data Processing Module
Handles extraction, concatenation, and saving of trade data
"""

import os
import pandas as pd
import zipfile
import glob
from pathlib import Path
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataProcessor:
    """
    Handles extraction and processing of India derisking trade data
    """
    
    def __init__(self, data_dir: str = "data/raw", output_dir: str = "data/merged"):
        """
        Initialize the DataProcessor
        
        Args:
            data_dir: Directory containing ZIP files
            output_dir: Directory to save processed data
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"DataProcessor initialized with data_dir={data_dir}, output_dir={output_dir}")
    
    def extract_zip_files(self, pattern: str = "*.ZIP") -> List[Path]:
        """
        Extract all ZIP files in the data directory
        
        Args:
            pattern: Glob pattern for ZIP files
            
        Returns:
            List of paths to extracted CSV files
        """
        zip_files = list(self.data_dir.glob(pattern))
        logger.info(f"Found {len(zip_files)} ZIP files to extract")
        
        extracted_files = []
        
        for zip_path in zip_files:
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # Extract only CSV files
                    csv_files = [f for f in zip_ref.namelist() if f.endswith('.csv')]
                    
                    for csv_file in csv_files:
                        zip_ref.extract(csv_file, self.data_dir)
                        extracted_path = self.data_dir / csv_file
                        extracted_files.append(extracted_path)
                        logger.info(f"Extracted: {csv_file} from {zip_path.name}")
                        
            except Exception as e:
                logger.error(f"Error extracting {zip_path}: {e}")
                
        logger.info(f"Total CSV files extracted: {len(extracted_files)}")
        return extracted_files
    
    def get_csv_files(self, pattern: str = "DataJobID-*.csv") -> List[Path]:
        """
        Get all CSV files matching the pattern
        
        Args:
            pattern: Glob pattern for CSV files
            
        Returns:
            List of CSV file paths
        """
        csv_files = sorted(self.data_dir.glob(pattern))
        logger.info(f"Found {len(csv_files)} CSV files matching pattern '{pattern}'")
        return csv_files
    
    def concatenate_csv_files(
        self, 
        csv_files: Optional[List[Path]] = None,
        output_filename: str = "consolidated_trade_data.csv"
    ) -> Path:
        """
        Concatenate multiple CSV files into a single file using pandas
        
        Args:
            csv_files: List of CSV file paths (if None, will find all DataJobID CSVs)
            output_filename: Name of the output file
            
        Returns:
            Path to the consolidated CSV file
        """
        if csv_files is None:
            csv_files = self.get_csv_files()
        
        if not csv_files:
            logger.warning("No CSV files found to concatenate")
            return None
        
        output_path = self.output_dir / output_filename
        
        # Read all CSV files into DataFrames
        dfs = []
        for csv_file in csv_files:
            try:
                df = pd.read_csv(csv_file)
                dfs.append(df)
                logger.info(f"Read {len(df)} rows from {csv_file.name}")
            except Exception as e:
                logger.error(f"Error reading {csv_file}: {e}")
                continue
        
        if not dfs:
            logger.error("No valid CSV files to concatenate")
            return None
        
        # Concatenate all DataFrames
        consolidated_df = pd.concat(dfs, ignore_index=True)
        
        # Save to CSV
        consolidated_df.to_csv(output_path, index=False)
        
        total_rows = len(consolidated_df)
        logger.info(f"✓ Consolidated {len(csv_files)} files into {output_filename}")
        logger.info(f"✓ Total rows written: {total_rows:,}")
        logger.info(f"✓ Output saved to: {output_path}")
        
        return output_path
    
    def get_data_summary(self, csv_path: Path) -> Dict:
        """
        Get summary statistics for a CSV file using pandas
        
        Args:
            csv_path: Path to CSV file
            
        Returns:
            Dictionary with summary statistics
        """
        try:
            df = pd.read_csv(csv_path)
            
            # Extract years
            years = sorted(df['Year'].dropna().unique().astype(int).tolist())
            
            summary = {
                'file': csv_path.name,
                'total_rows': len(df),
                'columns': len(df.columns),
                'years': years,
                'year_range': f"{min(years)}-{max(years)}" if years else "N/A"
            }
            
            return summary
        except Exception as e:
            logger.error(f"Error getting summary for {csv_path}: {e}")
            return {}
    
    def cleanup_extracted_files(self) -> int:
        """
        Remove extracted CSV and XML files from data directory
        
        Returns:
            Number of files removed
        """
        patterns = ["DataJobID-*.csv", "[Content_Types].xml"]
        removed_count = 0
        
        for pattern in patterns:
            files = list(self.data_dir.glob(pattern))
            for file in files:
                try:
                    file.unlink()
                    logger.info(f"Removed: {file.name}")
                    removed_count += 1
                except Exception as e:
                    logger.error(f"Error removing {file}: {e}")
        
        logger.info(f"✓ Cleaned up {removed_count} temporary files")
        return removed_count
    
    def process_all(self, extract: bool = True, cleanup: bool = True) -> Path:
        """
        Complete processing pipeline: extract, concatenate, cleanup, and save
        
        Args:
            extract: Whether to extract ZIP files first
            cleanup: Whether to remove temporary files after processing
            
        Returns:
            Path to consolidated output file
        """
        logger.info("=" * 80)
        logger.info("STARTING DATA PROCESSING PIPELINE")
        logger.info("=" * 80)
        
        # Step 1: Extract ZIP files
        if extract:
            logger.info("\n[Step 1/4] Extracting ZIP files...")
            self.extract_zip_files()
        else:
            logger.info("\n[Step 1/4] Skipping extraction (extract=False)")
        
        # Step 2: Get CSV files
        logger.info("\n[Step 2/4] Finding CSV files...")
        csv_files = self.get_csv_files()
        
        if not csv_files:
            logger.error("No CSV files found!")
            return None
        
        # Step 3: Concatenate
        logger.info("\n[Step 3/4] Concatenating CSV files...")
        output_path = self.concatenate_csv_files(csv_files)
        
        # Step 4: Cleanup
        if cleanup:
            logger.info("\n[Step 4/4] Cleaning up temporary files...")
            self.cleanup_extracted_files()
        else:
            logger.info("\n[Step 4/4] Skipping cleanup (cleanup=False)")
        
        # Generate summary
        if output_path and output_path.exists():
            logger.info("\n" + "=" * 80)
            logger.info("PROCESSING COMPLETE")
            logger.info("=" * 80)
            summary = self.get_data_summary(output_path)
            logger.info(f"\nConsolidated File Summary:")
            logger.info(f"  - File: {summary.get('file')}")
            logger.info(f"  - Total Rows: {summary.get('total_rows'):,}")
            logger.info(f"  - Columns: {summary.get('columns')}")
            logger.info(f"  - Years: {summary.get('years')}")
            logger.info(f"  - Year Range: {summary.get('year_range')}")
        
        return output_path


def main():
    """
    Main function to run the data processing pipeline
    """
    # Initialize processor
    processor = DataProcessor(data_dir="data", output_dir="output")
    
    # Run complete pipeline
    output_file = processor.process_all(extract=True)
    
    if output_file:
        print(f"\n✓ Success! Consolidated data saved to: {output_file}")
    else:
        print("\n✗ Processing failed. Check logs for details.")


if __name__ == "__main__":
    main()
