"""
Metrics Calculator Module
Implements 7 metrics to measure India's derisking effectiveness
"""

import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




class DeriskingMetrics:
    """
    Calculate derisking metrics for India's trade data
    """
    
    def __init__(self, data_path: str):
        """
        Initialize with consolidated trade data
        
        Args:
            data_path: Path to consolidated CSV file
        """
        self.data_path = Path(data_path)
        self.df = self._load_data()

        self.country_to_region = {
                # --- SOUTH ASIA ---
                "AFG": "South Asia", "BGD": "South Asia", "BTN": "South Asia", "IND": "South Asia",
                "MDV": "South Asia", "NPL": "South Asia", "PAK": "South Asia", "LKA": "South Asia",

                # --- EAST ASIA & PACIFIC ---
                "ASM": "East Asia & Pacific", "AUS": "East Asia & Pacific", "BRN": "East Asia & Pacific",
                "KHM": "East Asia & Pacific", "CHN": "East Asia & Pacific", "CXR": "East Asia & Pacific",
                "CCK": "East Asia & Pacific", "COK": "East Asia & Pacific", "FJI": "East Asia & Pacific",
                "PYF": "East Asia & Pacific", "GUM": "East Asia & Pacific", "HKG": "East Asia & Pacific",
                "IDN": "East Asia & Pacific", "JPN": "East Asia & Pacific", "KIR": "East Asia & Pacific",
                "PRK": "East Asia & Pacific", "KOR": "East Asia & Pacific", "LAO": "East Asia & Pacific",
                "MAC": "East Asia & Pacific", "MYS": "East Asia & Pacific", "MHL": "East Asia & Pacific",
                "FSM": "East Asia & Pacific", "MNG": "East Asia & Pacific", "MMR": "East Asia & Pacific",
                "NRU": "East Asia & Pacific", "NCL": "East Asia & Pacific", "NZL": "East Asia & Pacific",
                "NIU": "East Asia & Pacific", "NFK": "East Asia & Pacific", "MNP": "East Asia & Pacific",
                "PLW": "East Asia & Pacific", "PNG": "East Asia & Pacific", "PHL": "East Asia & Pacific",
                "PCN": "East Asia & Pacific", "WSM": "East Asia & Pacific", "SGP": "East Asia & Pacific",
                "SLB": "East Asia & Pacific", "TWN": "East Asia & Pacific", "THA": "East Asia & Pacific",
                "TLS": "East Asia & Pacific", "TKL": "East Asia & Pacific", "TON": "East Asia & Pacific",
                "TUV": "East Asia & Pacific", "VUT": "East Asia & Pacific", "VNM": "East Asia & Pacific",
                "WLF": "East Asia & Pacific",

                # --- EUROPE ---
                "ALB": "Europe", "AND": "Europe", "AUT": "Europe", "BEL": "Europe", "BIH": "Europe",
                "BGR": "Europe", "HRV": "Europe", "CYP": "Europe", "CZE": "Europe", "DNK": "Europe",
                "EST": "Europe", "FRO": "Europe", "FIN": "Europe", "FRA": "Europe", "DEU": "Europe",
                "GIB": "Europe", "GRC": "Europe", "GGY": "Europe", "VAT": "Europe", "HUN": "Europe",
                "ISL": "Europe", "IRL": "Europe", "IMN": "Europe", "ITA": "Europe", "JEY": "Europe",
                "LVA": "Europe", "LIE": "Europe", "LTU": "Europe", "LUX": "Europe", "MLT": "Europe",
                "MDA": "Europe", "MCO": "Europe", "MNE": "Europe", "NLD": "Europe", "MKD": "Europe",
                "NOR": "Europe", "POL": "Europe", "PRT": "Europe", "ROU": "Europe", "SMR": "Europe",
                "SRB": "Europe", "SVK": "Europe", "SVN": "Europe", "ESP": "Europe", "SJM": "Europe",
                "SWE": "Europe", "CHE": "Europe", "UKR": "Europe", "GBR": "Europe", "ALA": "Europe",

                # --- AMERICAS ---
                "AIA": "Americas", "ATG": "Americas", "ARG": "Americas", "ABW": "Americas",
                "BHS": "Americas", "BRB": "Americas", "BLZ": "Americas", "BMU": "Americas",
                "BOL": "Americas", "BES": "Americas", "BRA": "Americas", "VGB": "Americas",
                "CAN": "Americas", "CYM": "Americas", "CHL": "Americas", "COL": "Americas",
                "CRI": "Americas", "CUB": "Americas", "CUW": "Americas", "DMA": "Americas",
                "DOM": "Americas", "ECU": "Americas", "SLV": "Americas", "FLK": "Americas",
                "GUF": "Americas", "GRL": "Americas", "GRD": "Americas", "GLP": "Americas",
                "GTM": "Americas", "GUY": "Americas", "HTI": "Americas", "HND": "Americas",
                "JAM": "Americas", "MTQ": "Americas", "MEX": "Americas", "MSR": "Americas",
                "NIC": "Americas", "PAN": "Americas", "PRY": "Americas", "PER": "Americas",
                "PRI": "Americas", "BLM": "Americas", "KNA": "Americas", "LCA": "Americas",
                "MAF": "Americas", "SPM": "Americas", "VCT": "Americas", "SXM": "Americas",
                "SUR": "Americas", "TTO": "Americas", "TCA": "Americas", "USA": "Americas",
                "URY": "Americas", "VEN": "Americas", "VIR": "Americas",

                # --- MENA (Middle East & North Africa) ---
                "DZA": "MENA", "BHR": "MENA", "EGY": "MENA", "IRN": "MENA", "IRQ": "MENA",
                "ISR": "MENA", "JOR": "MENA", "KWT": "MENA", "LBN": "MENA", "LBY": "MENA",
                "MAR": "MENA", "OMN": "MENA", "PSE": "MENA", "QAT": "MENA", "SAU": "MENA",
                "SYR": "MENA", "TUN": "MENA", "TUR": "MENA", "ARE": "MENA", "YEM": "MENA",

                # --- SUB-SAHARAN AFRICA ---
                "AGO": "Sub-Saharan Africa", "BEN": "Sub-Saharan Africa", "BWA": "Sub-Saharan Africa",
                "BFA": "Sub-Saharan Africa", "BDI": "Sub-Saharan Africa", "CPV": "Sub-Saharan Africa",
                "CMR": "Sub-Saharan Africa", "CAF": "Sub-Saharan Africa", "TCD": "Sub-Saharan Africa",
                "COM": "Sub-Saharan Africa", "COG": "Sub-Saharan Africa", "COD": "Sub-Saharan Africa",
                "CIV": "Sub-Saharan Africa", "DJI": "Sub-Saharan Africa", "GNQ": "Sub-Saharan Africa",
                "ERI": "Sub-Saharan Africa", "SWZ": "Sub-Saharan Africa", "ETH": "Sub-Saharan Africa",
                "GAB": "Sub-Saharan Africa", "GMB": "Sub-Saharan Africa", "GHA": "Sub-Saharan Africa",
                "GIN": "Sub-Saharan Africa", "GNB": "Sub-Saharan Africa", "KEN": "Sub-Saharan Africa",
                "LSO": "Sub-Saharan Africa", "LBR": "Sub-Saharan Africa", "MDG": "Sub-Saharan Africa",
                "MWI": "Sub-Saharan Africa", "MLI": "Sub-Saharan Africa", "MRT": "Sub-Saharan Africa",
                "MUS": "Sub-Saharan Africa", "MYT": "Sub-Saharan Africa", "MOZ": "Sub-Saharan Africa",
                "NAM": "Sub-Saharan Africa", "NER": "Sub-Saharan Africa", "NGA": "Sub-Saharan Africa",
                "REU": "Sub-Saharan Africa", "RWA": "Sub-Saharan Africa", "SHN": "Sub-Saharan Africa",
                "STP": "Sub-Saharan Africa", "SEN": "Sub-Saharan Africa", "SYC": "Sub-Saharan Africa",
                "SLE": "Sub-Saharan Africa", "SOM": "Sub-Saharan Africa", "ZAF": "Sub-Saharan Africa",
                "SSD": "Sub-Saharan Africa", "SDN": "Sub-Saharan Africa", "TZA": "Sub-Saharan Africa",
                "TGO": "Sub-Saharan Africa", "UGA": "Sub-Saharan Africa", "ZMB": "Sub-Saharan Africa",
                "ZWE": "Sub-Saharan Africa",

                # --- RUSSIA & CENTRAL ASIA ---
                "ARM": "Russia & Central Asia", "AZE": "Russia & Central Asia", "BLR": "Russia & Central Asia",
                "GEO": "Russia & Central Asia", "KAZ": "Russia & Central Asia", "KGZ": "Russia & Central Asia",
                "RUS": "Russia & Central Asia", "TJK": "Russia & Central Asia", "TKM": "Russia & Central Asia",
                "UZB": "Russia & Central Asia",

                # --- ANTARCTIC / OTHER ---
                "ATA": "Antarctic", "BVT": "Antarctic", "HMD": "Antarctic", "ATF": "Antarctic",
                "SGS": "Antarctic", "UMI": "Americas" # US Minor Outlying Islands
            }
        logger.info(f"Loaded {len(self.df)} trade records")
    
    def _load_data(self) -> pd.DataFrame:
        """Load and parse trade data using pandas"""
        df = pd.read_csv(self.data_path)
        # Clean column names
        df.columns = df.columns.str.strip()
        return df
    
    def _filter_india_imports(self, year: int = None) -> pd.DataFrame:
        """
        Filter data for India's imports
        
        Args:
            year: Optional year filter
            
        Returns:
            DataFrame of import records
        """
        # India as partner, TradeFlowName = Export means reporter is exporting TO India
        # This is equivalent to India importing FROM reporter
        mask = (self.df['PartnerISO3'] == 'IND') & (self.df['TradeFlowName'] == 'Export')
        
        if year is not None:
            mask = mask & (self.df['Year'] == year)
        
        return self.df[mask].copy()
    
    def _get_trade_value(self, value) -> float:
        """Extract trade value"""
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0
    
    # ========================================================================
    # METRIC 1: Trade Dependency Index (TDI)
    # ========================================================================
    
    def calculate_tdi(self, year: int, partner_iso: str = 'CHN') -> float:
        """
        Calculate Trade Dependency Index for a specific partner
        
        TDI = (Imports from Partner / Total Imports) × 100
        
        Args:
            year: Year to calculate
            partner_iso: Partner country ISO3 code (default: CHN for China)
            
        Returns:
            TDI percentage
        """
        imports_df = self._filter_india_imports(year)

        
        
        # Total imports (sum of all trade values)
        total_imports = imports_df['TradeValue in 1000 USD'].sum()
        
        # Imports from specific partner
        partner_imports = imports_df[imports_df['ReporterISO3'] == partner_iso]['TradeValue in 1000 USD'].sum()
        
        if total_imports == 0:
            return 0.0
        
        tdi = (partner_imports / total_imports) * 100
        logger.info(f"TDI ({partner_iso}, {year}): {tdi:.2f}%")
        return tdi
    
    def calculate_tdi_trend(self, start_year: int, end_year: int, 
                           partner_iso: str = 'CHN') -> Dict[int, float]:
        """
        Calculate TDI trend over multiple years
        
        Args:
            start_year: Start year
            end_year: End year
            partner_iso: Partner country ISO3 code
            
        Returns:
            Dictionary mapping year to TDI
        """
        trend = {}
        for year in range(start_year, end_year + 1):
            trend[year] = self.calculate_tdi(year, partner_iso)
        return trend
    
    # ========================================================================
    # METRIC 2: Herfindahl-Hirschman Index (HHI)
    # ========================================================================
    
    def calculate_hhi(self, year: int) -> float:
        """
        Calculate Herfindahl-Hirschman Index for trade concentration
        
        HHI = Σ(market_share_i)²
        
        Args:
            year: Year to calculate
            
        Returns:
            HHI value (0-10000)
        """
        imports_df = self._filter_india_imports(year)
        
        # Calculate total imports by partner
        partner_imports = imports_df.groupby('ReporterISO3')['TradeValue in 1000 USD'].sum()
        total_imports = partner_imports.sum()
        
        if total_imports == 0:
            return 0.0
        
        # Calculate market shares and HHI
        shares = (partner_imports / total_imports) * 100
        hhi = (shares ** 2).sum()
        
        logger.info(f"HHI ({year}): {hhi:.2f}")
        return hhi
    
    def calculate_hhi_trend(self, start_year: int, end_year: int) -> Dict[int, float]:
        """Calculate HHI trend over multiple years"""
        trend = {}
        for year in range(start_year, end_year + 1):
            trend[year] = self.calculate_hhi(year)
        return trend
    
    # ========================================================================
    # METRIC 3: China-Plus-One Diversification Score (CPODS)
    # ========================================================================
    
    def calculate_cpods(self, baseline_year: int, current_year: int,
                       alternative_partners: List[str] = None) -> float:
        """
        Calculate China-Plus-One Diversification Score
        
        CPODS = Σ(Δ share_alternatives) / |Δ share_China|
        
        Args:
            baseline_year: Baseline year
            current_year: Current year
            alternative_partners: List of alternative partner ISO3 codes
            
        Returns:
            CPODS value
        """
        if alternative_partners is None:
            # Default alternative partners
            alternative_partners = ['USA', 'JPN', 'DEU', 'SGP', 'KOR', 
                                   'ARE', 'AUS', 'GBR', 'FRA', 'ITA']
        
        # Get shares for baseline and current
        baseline_shares = self._get_partner_shares(baseline_year)
        current_shares = self._get_partner_shares(current_year)
        
        # Calculate China's share change
        china_baseline = baseline_shares.get('CHN', 0.0)
        china_current = current_shares.get('CHN', 0.0)
        china_change = china_current - china_baseline
        
        # Calculate alternatives' share change
        alternatives_change = 0.0
        for partner in alternative_partners:
            baseline = baseline_shares.get(partner, 0.0)
            current = current_shares.get(partner, 0.0)
            alternatives_change += (current - baseline)
        
        if china_change == 0:
            return 0.0
        
        cpods = alternatives_change / abs(china_change)
        logger.info(f"CPODS ({baseline_year}->{current_year}): {cpods:.2f}")
        return cpods
    
    def _get_partner_shares(self, year: int) -> Dict[str, float]:
        """Get import share by partner for a given year"""
        imports_df = self._filter_india_imports(year)
        
        # Calculate partner shares
        partner_imports = imports_df.groupby('ReporterISO3')['TradeValue in 1000 USD'].sum()
        total_imports = partner_imports.sum()
        
        if total_imports == 0:
            return {}
        
        # Convert to percentages
        shares = ((partner_imports / total_imports) * 100).to_dict()
        return shares
    
    # ========================================================================
    # METRIC 4: Domestic Manufacturing Substitution Index (DMSI)
    # ========================================================================
    
    def calculate_dmsi_proxy(self, product_code: str, baseline_year: int, 
                            current_year: int) -> float:
        """
        Calculate DMSI proxy based on import reduction
        
        DMSI_proxy = (Imports_baseline - Imports_current) / Imports_baseline
        
        Args:
            product_code: HS product code
            baseline_year: Baseline year
            current_year: Current year
            
        Returns:
            DMSI proxy value (-∞ to 1)
        """
        baseline_imports = self._get_product_imports(product_code, baseline_year)
        current_imports = self._get_product_imports(product_code, current_year)
        
        if baseline_imports == 0:
            return 0.0
        
        dmsi = (baseline_imports - current_imports) / baseline_imports
        logger.info(f"DMSI ({product_code}, {baseline_year}->{current_year}): {dmsi:.2f}")
        return dmsi
    
    def _get_product_imports(self, product_code: str, year: int) -> float:
        """Get total imports for a product in a given year"""
        imports_df = self._filter_india_imports(year)
        product_imports = imports_df[imports_df['ProductCode'] == product_code]['TradeValue in 1000 USD'].sum()
        return product_imports
    
    # ========================================================================
    # METRIC 5: Strategic Sector Vulnerability Index (SSVI)
    # ========================================================================
    
    def calculate_ssvi(self, year: int, sector_products: List[str],
                      criticality_weight: float = 1.0) -> float:
        """
        Calculate Strategic Sector Vulnerability Index
        
        SSVI = (China_imports / Total_imports) × Criticality_weight
        
        Args:
            year: Year to calculate
            sector_products: List of HS codes in the sector
            criticality_weight: Importance weight (1-5)
            
        Returns:
            SSVI value
        """
        imports_df = self._filter_india_imports(year)
        
        # Filter for sector products
        sector_df = imports_df[imports_df['ProductCode'].isin(sector_products)]
        
        sector_total = sector_df['TradeValue in 1000 USD'].sum()
        sector_china = sector_df[sector_df['ReporterISO3'] == 'CHN']['TradeValue in 1000 USD'].sum()
        
        if sector_total == 0:
            return 0.0
        
        dependency = (sector_china / sector_total) * 100
        ssvi = dependency * criticality_weight
        
        logger.info(f"SSVI ({year}): {ssvi:.2f}")
        return ssvi
    
    # ========================================================================
    # METRIC 6: Trade Balance Improvement Index (TBII)
    # ========================================================================
    
    def calculate_tbii(self, baseline_year: int, current_year: int,
                      partner_iso: str = 'CHN') -> float:
        """
        Calculate Trade Balance Improvement Index
        
        TBII = (Deficit_baseline - Deficit_current) / Deficit_baseline × 100
        
        Args:
            baseline_year: Baseline year
            current_year: Current year
            partner_iso: Partner country ISO3 code
            
        Returns:
            TBII percentage
        """
        baseline_deficit = self._get_trade_deficit(baseline_year, partner_iso)
        current_deficit = self._get_trade_deficit(current_year, partner_iso)
        
        if baseline_deficit == 0:
            return 0.0
        
        tbii = ((baseline_deficit - current_deficit) / baseline_deficit) * 100
        logger.info(f"TBII ({partner_iso}, {baseline_year}->{current_year}): {tbii:.2f}%")
        return tbii
    
    def _get_trade_deficit(self, year: int, partner_iso: str) -> float:
        """Calculate trade deficit with a partner"""
        # Get India's imports from partner (Reporter exports to India)
        imports_mask = (
            (self.df['PartnerISO3'] == 'IND') &
            (self.df['ReporterISO3'] == partner_iso) &
            (self.df['TradeFlowName'] == 'Export') &
            (self.df['Year'] == year)
        )
        imports = self.df[imports_mask]['TradeValue in 1000 USD'].sum()
        
        # Get India's exports to partner (India exports to partner)
        exports_mask = (
            (self.df['ReporterISO3'] == 'IND') &
            (self.df['PartnerISO3'] == partner_iso) &
            (self.df['TradeFlowName'] == 'Export') &
            (self.df['Year'] == year)
        )
        exports = self.df[exports_mask]['TradeValue in 1000 USD'].sum()
        
        deficit = imports - exports
        return deficit
    
    # ========================================================================
    # METRIC 7: Supply Chain Resilience Score (SCRS)
    # ========================================================================
    
    def calculate_scrs(self, year: int, w1: float = 0.4, w2: float = 0.3,
                      w3: float = 0.3) -> float:
        """
        Calculate Supply Chain Resilience Score
        
        SCRS = w1×Source_diversity + w2×Geographic_diversity + w3×Critical_redundancy
        
        Args:
            year: Year to calculate
            w1: Weight for source diversity
            w2: Weight for geographic diversity
            w3: Weight for critical product redundancy
            
        Returns:
            SCRS value (0-100)
        """
        source_diversity = self._calculate_source_diversity(year)
        geographic_diversity = self._calculate_geographic_diversity(year)

        critical_redundancy = self._calculate_critical_redundancy(year)
        
        scrs = (w1 * source_diversity + 
                w2 * geographic_diversity + 
                w3 * critical_redundancy)
        
        logger.info(f"SCRS ({year}): {scrs:.2f}")
        return scrs
    
    def _calculate_source_diversity(self, year: int, max_sources: int = 20) -> float:
        """
        Source diversity based on effective number of suppliers (inverse HHI)

        Returns a 0–100 score
        """
        shares = self._get_partner_shares(year)

        if not shares:
            return 0.0

        # Convert percentages to fractions
        hhi = sum((s / 100) ** 2 for s in shares.values())

        if hhi == 0:
            return 0.0

        effective_sources = 1 / hhi

        # Normalize to 0–100
        return min(effective_sources / max_sources * 100, 100)

    def _calculate_geographic_diversity(self, year: int, max_regions: int = 7) -> float:
        """
        Geographic diversity based on regional concentration (Simpson index)
        """
        imports_df = self._filter_india_imports(year)

        if imports_df.empty:
            return 0.0

        # Map countries to regions (you must define this)
        imports_df['Region'] = imports_df['ReporterISO3'].map(self.country_to_region)

        # Aggregate by region
        region_imports = imports_df.groupby('Region')['TradeValue in 1000 USD'].sum()
        total = region_imports.sum()

        if total == 0:
            return 0.0

        shares = region_imports / total

        # Simpson geographic diversity
        simpson = 1 - (shares ** 2).sum()

        # Normalize to 0–100
        return min(simpson / (1 - 1 / max_regions) * 100, 100)


    def _calculate_geographic_diversity1(self, year: int) -> float:
        """Calculate regional distribution of imports"""
        shares = self._get_partner_shares(year)
        
        # Proxy: more partners = more geographic diversity
        num_partners = len(shares)

        return min(num_partners / 50 * 100, 100)
    
    def _calculate_critical_redundancy(self, year: int) -> float:
        """
        Calculate availability of alternative sources for critical products
        
        Simplified proxy: diversity of suppliers for top imported products
        """
        imports_df = self._filter_india_imports(year)
        
        # Count suppliers per product
        product_suppliers = imports_df.groupby('ProductCode')['ReporterISO3'].nunique()
        
        if len(product_suppliers) == 0:
            return 0.0
        
        # Average number of suppliers per product
        avg_suppliers = product_suppliers.mean()
        
        # Normalize (assume max 10 suppliers per product is excellent)
        return min(avg_suppliers / 10 * 100, 100)


def main():
    """Demo usage of metrics calculator"""
    calculator = DeriskingMetrics('data/merged/consolidated_trade_data.csv')
    
    print("\n" + "="*80)
    print("DERISKING METRICS DEMO")
    print("="*80)
    
    # TDI
    print("\n1. Trade Dependency Index (China)")
    tdi_2019 = calculator.calculate_tdi(2019, 'CHN')
    tdi_2024 = calculator.calculate_tdi(2024, 'CHN')
    print(f"   2019: {tdi_2019:.2f}%")
    print(f"   2024: {tdi_2024:.2f}%")
    print(f"   Change: {tdi_2024 - tdi_2019:+.2f}%")
    
    # HHI
    print("\n2. Herfindahl-Hirschman Index")
    hhi_2019 = calculator.calculate_hhi(2019)
    hhi_2024 = calculator.calculate_hhi(2024)
    print(f"   2019: {hhi_2019:.2f}")
    print(f"   2024: {hhi_2024:.2f}")
    print(f"   Change: {hhi_2024 - hhi_2019:+.2f}")
    
    # CPODS
    print("\n3. China-Plus-One Diversification Score")
    cpods = calculator.calculate_cpods(2019, 2024)
    print(f"   2019->2024: {cpods:.2f}")
    
    # SCRS
    print("\n4. Supply Chain Resilience Score")
    scrs_2019 = calculator.calculate_scrs(2019)
    scrs_2024 = calculator.calculate_scrs(2024)
    print(f"   2019: {scrs_2019:.2f}")
    print(f"   2024: {scrs_2024:.2f}")
    print(f"   Change: {scrs_2024 - scrs_2019:+.2f}")


if __name__ == "__main__":
    main()
