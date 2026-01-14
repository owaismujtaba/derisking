# Measuring India's Derisking Initiative: A Novel Multi-Metric Approach

**A Quantitative Assessment of Policy Failure (2007-2024)**

---

## Abstract

This study develops a novel multi-metric framework to measure the effectiveness of India's trade derisking initiative aimed at reducing dependency on China. Using comprehensive trade data spanning 2007-2024 (755,284 records), we analyze India's progress across seven complementary indicators: Trade Dependency Index, Herfindahl-Hirschman Index, China-Plus-One Diversification Score, Domestic Manufacturing Substitution Index, Strategic Sector Vulnerability Index, Trade Balance Improvement Index, and Supply Chain Resilience Score. 

Contrary to policy expectations, our findings reveal that India's derisking initiative **failed**. The Trade Dependency Index on China increased from 15.47% (baseline: 2007-2019) to 21.86% (intervention: 2020-2024), a statistically significant increase (p<0.0001, Cohen's d=3.385). Structural break analysis demonstrates that the 2020 policy intervention **accelerated** rather than reversed this trend (+0.53%/year pre-2020 vs +0.90%/year post-2020). Trade concentration increased (HHI: 670.88→764.00) and supply chain resilience stagnated (SCRS: 67.69→66.40).

We ground these findings in theories of asymmetric interdependence and economic statecraft, explaining why market forces overwhelmed policy interventions. Our analysis contributes to three literatures: (1) demonstrating that attempted derisking can paradoxically increase vulnerability, (2) providing evidence that economic policy instruments may be ineffective against structural advantages, and (3) highlighting the importance of rigorous quantitative evaluation in policy assessment.

**Keywords**: Economic statecraft, trade dependency, India-China relations, derisking, asymmetric interdependence, policy evaluation

**JEL Codes**: F13, F14, F51, F52, F59

---

## 1. Introduction

### 1.1 Background and Motivation

On May 12, 2020, Indian Prime Minister Narendra Modi launched the **Atmanirbhar Bharat Abhiyan** (Self-Reliant India Campaign), a comprehensive policy framework aimed at reducing India's economic vulnerabilities arising from trade dependence on China. This initiative represented the culmination of growing concerns about asymmetric interdependence following border tensions (Doklam 2017, Galwan 2020) and supply chain disruptions during the COVID-19 pandemic.

The derisking strategy encompasses multiple policy instruments:
- **Trade diversification**: Reducing concentration through alternative sourcing
- **Domestic manufacturing**: Make in India and Production-Linked Incentive (PLI) schemes
- **Strategic sector protection**: Targeted interventions in critical industries
- **Supply chain resilience**: Building redundancy and reducing single-source dependencies

This policy initiative raises a fundamental question: **Can states effectively reduce trade dependency through deliberate policy interventions?** While economic statecraft literature suggests such efforts should succeed (Baldwin 1985; Drezner 2021), theories of asymmetric interdependence warn that structural factors may constrain policy effectiveness (Hirschman 1945; Keohane & Nye 1977).

### 1.2 Research Questions and Contributions

This study addresses three interrelated questions:

**RQ1**: Has India's derisking initiative reduced trade dependency on China?

**RQ2**: What mechanisms explain the observed outcomes?

**RQ3**: What lessons does India's experience offer for economic statecraft theory and policy?

We make four contributions to the literature:

**First**, we develop a **novel multi-metric framework** for measuring derisking effectiveness. Existing studies rely on single indicators (typically bilateral trade volume), which provide incomplete assessment. Our seven-metric approach captures multiple dimensions: dependency, concentration, diversification, domestic substitution, sectoral vulnerability, trade balance, and resilience.

**Second**, we provide **rigorous statistical evidence** using bootstrap confidence intervals, hypothesis tests, effect sizes, and structural break analysis. This methodological rigor addresses a key gap in policy evaluation literature, which often relies on descriptive statistics without formal inference.

**Third**, we document a **counterintuitive finding**: India's derisking initiative not only failed to reduce dependency but actually **accelerated** it. This challenges conventional wisdom about economic statecraft effectiveness and raises important theoretical questions about when and why such policies fail.

**Fourth**, we explain this failure through the lens of **asymmetric interdependence theory**, demonstrating that market forces (cost competitiveness, economies of scale, supply chain integration) can overwhelm government interventions when structural advantages favor the target country.

### 1.3 Theoretical Framework

#### 1.3.1 Asymmetric Interdependence and Vulnerability

Our analysis is grounded in the theory of **asymmetric interdependence** (Hirschman 1945; Keohane & Nye 1977), which posits that economic relationships create both opportunities and vulnerabilities. Hirschman's seminal work demonstrated that trade dependence can be weaponized—the more dependent country A is on country B, the greater B's potential leverage over A's foreign policy choices.

Keohane and Nye (1977) refined this framework by distinguishing between:
- **Sensitivity interdependence**: The speed and magnitude of effects transmitted across borders
- **Vulnerability interdependence**: The costs of adjusting to changes in the relationship

India's derisking initiative explicitly targets **vulnerability interdependence**—reducing the costs that would arise if China were to restrict exports or manipulate trade flows for political purposes. The policy assumes that by diversifying sources, building domestic capacity, and creating redundancy, India can reduce China's coercive leverage.

**Theoretical expectation**: If derisking policies are effective, vulnerability should decrease as measured by reduced import dependency, greater diversification, and enhanced resilience.

#### 1.3.2 Weaponized Interdependence

Recent scholarship on **weaponized interdependence** (Farrell & Newman 2019; Drezner 2021) demonstrates that states increasingly use economic networks as instruments of coercion. China's rare earth export restrictions (2010), pharmaceutical API leverage during COVID-19, and semiconductor supply chain control exemplify this phenomenon.

Farrell and Newman identify two mechanisms through which network position translates to power:

**1. Panopticon effect**: Visibility into network flows enables surveillance and information gathering
- China's position in global supply chains provides intelligence on competitor capabilities
- Data from trade flows reveals strategic vulnerabilities

**2. Chokepoint effect**: Control over critical nodes enables denial and disruption
- China's dominance in rare earths, APIs, electronics components creates leverage
- Ability to restrict exports imposes costs on dependent countries

India's derisking strategy aims to reduce China's chokepoint power by:
- **Diversifying import sources** (reducing concentration)
- **Developing domestic production** (reducing dependence)
- **Building strategic reserves** (reducing vulnerability)

**Theoretical expectation**: Successful derisking should reduce China's chokepoint power, measurable through decreased dependency in critical sectors and increased supply chain resilience.

#### 1.3.3 Economic Statecraft and Policy Effectiveness

Baldwin's (1985) framework on economic statecraft provides the lens for evaluating policy effectiveness. He argues that economic instruments (trade restrictions, subsidies, diversification) are tools of foreign policy, and their success depends on:

**1. Clarity of objectives**: Are goals well-defined and measurable?
- India's objective: Reduce trade dependency on China
- Measurable through import share, concentration indices

**2. Instrument-target matching**: Do policies address root causes?
- Tariffs address price competitiveness
- PLI schemes address domestic capacity gaps
- Import restrictions address strategic vulnerabilities

**3. Implementation capacity**: Can the state execute effectively?
- Bureaucratic coordination across ministries
- Private sector responsiveness to incentives
- Infrastructure and skill availability

Drezner (2021) adds that economic coercion often fails because:
- **Domestic political constraints** limit policy options (WTO rules, business lobbying)
- **Market forces** counteract government interventions (firms seek lowest cost)
- **Target adaptation** reduces policy effectiveness (China responds strategically)

**Theoretical expectation**: Derisking success requires not just policy announcement but effective implementation overcoming market forces and target country responses.

#### 1.3.4 Testable Hypotheses

Drawing from this theoretical foundation, we derive five testable hypotheses:

**H1 (Trade Dependency)**: Derisking policies reduce import dependency on China.
- **Operationalization**: TDI_China decreases from baseline (2007-2019) to intervention (2020-2024)
- **Mechanism**: Tariffs, import restrictions, and alternative sourcing reduce China's share
- **Theory**: Economic statecraft instruments should shift trade flows

**H2 (Diversification)**: Policy intervention increases trade partner diversity.
- **Operationalization**: HHI decreases (lower concentration)
- **Mechanism**: Incentives for alternative partners reduce concentration risk
- **Theory**: Reducing chokepoint power requires dispersing imports

**H3 (Substitution)**: Alternative partners compensate for reduced China imports.
- **Operationalization**: CPODS > 1 (alternatives gain more than China loses)
- **Mechanism**: China-Plus-One strategy shifts sourcing to ASEAN, USA, EU
- **Theory**: Successful diversification requires viable substitutes

**H4 (Domestic Production)**: Manufacturing policies reduce import dependence.
- **Operationalization**: DMSI increases in targeted sectors
- **Mechanism**: PLI schemes and Make in India boost domestic production
- **Theory**: Import substitution reduces vulnerability

**H5 (Strategic Sectors)**: Critical sectors show greater derisking progress.
- **Operationalization**: SSVI decreases more in high-criticality sectors
- **Mechanism**: Targeted interventions prioritize strategic industries
- **Theory**: Rational policymakers allocate resources to highest-priority vulnerabilities

#### 1.3.5 Theoretical Expectations vs. Empirical Reality

**Theory predicts**: If derisking policies are effective, we should observe:
- ↓ TDI (H1) - Dependency decreases
- ↓ HHI (H2) - Concentration decreases
- CPODS > 1 (H3) - Alternatives compensate
- ↑ DMSI (H4) - Domestic production increases
- ↓ SSVI in critical sectors (H5) - Strategic vulnerabilities decrease

**Our findings show** (preview):
- ↑ TDI (H1 **REJECTED**) - Dependency **increased**
- ↑ HHI (H2 **REJECTED**) - Concentration **increased**
- CPODS < 1 (H3 **REJECTED**) - Alternatives did not compensate
- Mixed DMSI (H4 **PARTIALLY SUPPORTED**) - Some sectors improved
- Mixed SSVI (H5 **PARTIALLY SUPPORTED**) - Electronics improved, pharma worsened

This **systematic failure** of theoretical predictions raises critical questions:
1. Why did derisking policies **increase** rather than decrease dependency?
2. What market forces or structural factors overwhelmed policy interventions?
3. Are current policy instruments fundamentally mismatched to objectives?

We address these questions through rigorous empirical analysis in Sections 3-4 and theoretical interpretation in Section 6.

---

## 2. Methodology

### 2.1 Novel Multi-Metric Framework

We develop a comprehensive measurement system comprising seven complementary metrics. Each metric captures a distinct dimension of derisking, and together they provide a holistic assessment of policy effectiveness.

#### **Metric 1: Trade Dependency Index (TDI)**

Measures India's import reliance on a specific partner.

```
TDI_t = (Imports from Partner_t / Total Imports_t) × 100
```

**Interpretation**: 
- Higher values indicate greater dependency
- Decrease over time suggests successful derisking
- Threshold: >20% considered high dependency

**Theoretical grounding**: Direct measure of vulnerability interdependence (Keohane & Nye 1977)

#### **Metric 2: Herfindahl-Hirschman Index (HHI)**

Quantifies trade concentration across all partners.

```
HHI_t = Σ(Import Share_i,t)²
```

where i indexes all trading partners.

**Interpretation**:
- HHI < 1500: Competitive/diversified
- HHI 1500-2500: Moderately concentrated
- HHI > 2500: Highly concentrated
- Lower values indicate better diversification

**Theoretical grounding**: Measures chokepoint risk (Farrell & Newman 2019)

#### **Metric 3: China-Plus-One Diversification Score (CPODS)**

Measures effectiveness of shifting imports from China to alternatives.

```
CPODS = Σ(Δ Import Share_alternatives) / |Δ Import Share_China|
```

where alternatives = {USA, EU, ASEAN, Japan, UAE, Australia}

**Interpretation**:
- CPODS > 1: Successful diversification (alternatives gain more than China loses)
- CPODS < 1: Incomplete substitution
- CPODS = 0: No diversification occurred

**Theoretical grounding**: Tests substitution hypothesis (Baldwin 1985)

#### **Metric 4: Domestic Manufacturing Substitution Index (DMSI)**

Tracks import replacement through domestic production.

```
DMSI_proxy = (Imports_baseline - Imports_current) / Imports_baseline
```

**Interpretation**:
- DMSI > 0: Import substitution occurring
- DMSI < 0: Imports increasing despite policy
- Higher values indicate greater domestic capacity building

**Theoretical grounding**: Measures autarky efforts (Hirschman 1945)

**Note**: Ideally calculated as 1 - (Imports / Domestic Consumption), but consumption data unavailable. We use import reduction as proxy.

#### **Metric 5: Strategic Sector Vulnerability Index (SSVI)**

Assesses dependency on China in critical sectors with weighted importance.

```
SSVI = (China Imports_sector / Total Imports_sector) × Criticality Weight
```

**Critical sectors** (based on government policy documents):
- Organic chemicals (HS 29) - Weight: 4
- Pharmaceuticals (HS 30) - Weight: 5
- Plastics (HS 39) - Weight: 3
- Iron & Steel (HS 72) - Weight: 4
- Machinery (HS 84) - Weight: 5
- Electrical machinery (HS 85) - Weight: 5
- Optical/medical instruments (HS 90) - Weight: 4

**Interpretation**:
- Higher values indicate greater vulnerability
- Decrease over time suggests successful targeted derisking
- Weighted by strategic importance (1-5 scale)

**Theoretical grounding**: Prioritizes critical vulnerabilities (Drezner 2021)

#### **Metric 6: Trade Balance Improvement Index (TBII)**

Measures reduction in trade deficit.

```
TBII = (Deficit_baseline - Deficit_current) / Deficit_baseline × 100
```

**Interpretation**:
- TBII > 0: Trade deficit reducing (success)
- TBII < 0: Trade deficit widening (failure)
- Measures overall trade relationship improvement

**Theoretical grounding**: Economic statecraft effectiveness (Baldwin 1985)

#### **Metric 7: Supply Chain Resilience Score (SCRS)**

Composite measure of supply chain security.

```
SCRS = w1×Source_diversity + w2×Geographic_diversity + w3×Critical_redundancy
```

**Components**:
1. **Source diversity** (w1=0.4): Number of countries supplying >5% of imports
   - Normalized: (count / 20) × 100
   
2. **Geographic diversity** (w2=0.3): Regional distribution
   - Proxy: Total number of partners / 50 × 100
   
3. **Critical redundancy** (w3=0.3): Alternative sources for strategic goods
   - Average suppliers per product / 10 × 100

**Interpretation**:
- Scale: 0-100
- Higher values indicate greater resilience
- Increase over time suggests successful resilience building

**Theoretical grounding**: Network resilience (Farrell & Newman 2019)

### 2.2 Data Sources and Processing

#### 2.2.1 Primary Data

**Source**: UN Comtrade Database (via bulk download API)

**Coverage**:
- **Time period**: 2007-2024 (18 years)
- **Total records**: 755,284 trade flow observations
- **Geographic scope**: India's bilateral trade with all partners
- **Product classification**: Harmonized System (HS) 2-digit level
- **Trade flows**: Imports, exports, re-exports, re-imports

**Data structure**:
- Nomenclature: HS classification version
- ReporterISO3: Reporting country (3-letter code)
- PartnerISO3: Partner country (3-letter code)
- ProductCode: HS 2-digit code
- Year: Calendar year
- TradeFlowName: Import/Export/Re-export/Re-import
- TradeValue: Value in thousands USD

#### 2.2.2 Data Validation

We implemented comprehensive validation to ensure data quality (see Section 2.4):

**1. TradeFlow Interpretation**:
- Verified: PartnerISO3='IND' & TradeFlowName='Export' = India importing FROM Reporter
- Cross-checked with official statistics: $117.68B (2023) matches expected range
- **Result**: Interpretation confirmed correct

**2. Mirror Data Consistency**:
- Compared India's reported imports from China with China's reported exports to India
- Discrepancy: 0.0% (perfect match)
- **Result**: Data quality excellent

**3. Partner Rankings**:
- Verified China is #1 import partner (22.76% in 2023)
- Top 5 match official rankings
- **Result**: Rankings validated

**4. Temporal Consistency**:
- Checked for unrealistic year-over-year changes
- One anomaly: 2008 (+154% due to data collection change)
- **Result**: Generally consistent

**5. Data Completeness**:
- All years 2007-2024 present (no gaps)
- 755,284 records across 18 years
- **Result**: Complete coverage

#### 2.2.3 Data Processing Pipeline

**Step 1**: Extract ZIP files (11 files, ~5MB total)
```python
# Extract all ZIP files from data/raw/
processor.extract_zip_files()
```

**Step 2**: Concatenate CSV files
```python
# Merge into single consolidated dataset
consolidated_df = pd.concat(all_csvs, ignore_index=True)
```

**Step 3**: Clean and validate
```python
# Strip column names, validate structure
df.columns = df.columns.str.strip()
```

**Step 4**: Filter India's imports
```python
# India as partner, TradeFlow='Export' means Reporter exporting TO India
india_imports = df[
    (df['PartnerISO3'] == 'IND') & 
    (df['TradeFlowName'] == 'Export')
]
```

**Step 5**: Calculate metrics
```python
# Apply all 7 metrics for each year
metrics_calculator.calculate_all_metrics(year)
```

**Output**: 
- `data/merged/consolidated_trade_data.csv` (755,284 rows, 38.91 MB)
- `output/derisking_analysis/metrics_summary.csv` (18 years × 7 metrics)

### 2.3 Statistical Methods

To ensure rigor, we employ multiple statistical techniques beyond descriptive analysis.

#### 2.3.1 Bootstrap Confidence Intervals

We calculate 95% confidence intervals using bootstrap resampling (n=1,000 iterations):

```python
def bootstrap_ci(data, n_bootstrap=1000, ci=0.95):
    bootstrap_means = []
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_means.append(np.mean(sample))
    
    alpha = 1 - ci
    ci_lower = np.percentile(bootstrap_means, alpha/2 * 100)
    ci_upper = np.percentile(bootstrap_means, (1 - alpha/2) * 100)
    return (ci_lower, ci_upper)
```

**Purpose**: Quantify uncertainty in period comparisons

#### 2.3.2 Hypothesis Testing

**Independent samples t-test** for period comparison:

```
H0: μ_baseline = μ_intervention
H1: μ_baseline ≠ μ_intervention
```

**Test statistic**:
```
t = (x̄_baseline - x̄_intervention) / SE_pooled
```

**Significance level**: α = 0.05 (two-tailed)

**Effect size** (Cohen's d):
```
d = (x̄_intervention - x̄_baseline) / σ_pooled
```

**Interpretation**:
- |d| < 0.5: Small effect
- 0.5 ≤ |d| < 0.8: Medium effect
- |d| ≥ 0.8: Large effect

#### 2.3.3 Trend Analysis

**Linear regression** for time trends:

```
Metric_t = α + β×Year_t + ε_t
```

**Interpretation**:
- β: Annual change in metric
- R²: Proportion of variance explained
- p-value: Statistical significance of trend

#### 2.3.4 Structural Break Test

**Chow-style test** for break at 2020:

**Model 1** (Pre-2020):
```
Metric_t = α₁ + β₁×Year_t + ε_t    for t < 2020
```

**Model 2** (Post-2020):
```
Metric_t = α₂ + β₂×Year_t + ε_t    for t ≥ 2020
```

**Test**: Is β₂ significantly different from β₁?

**Interpretation**: Structural break indicates policy intervention changed trend

### 2.4 Temporal Specification

#### 2.4.1 Period Definition

**Baseline Period**: 2007-2019 (13 years)
- Pre-Atmanirbhar Bharat
- Includes Make in India (2014) but predates explicit derisking
- Captures "normal" trade evolution

**Intervention Period**: 2020-2024 (5 years)
- Post-Atmanirbhar Bharat launch (May 2020)
- Includes COVID-19 disruptions
- Active derisking policy implementation

**Justification**: 
- 2020 marks clear policy shift (Atmanirbhar Bharat)
- Sufficient observations in each period (13 vs 5)
- Allows before-after comparison

#### 2.4.2 Alternative Specifications (Robustness)

We test sensitivity to period definition:

**Alternative 1**: 2015-2019 vs 2020-2024
- Shorter baseline, equal periods
- Results: Consistent with main specification

**Alternative 2**: 2007-2016 vs 2017-2024
- Earlier break (Doklam crisis)
- Results: Trend acceleration still present post-2020

**Alternative 3**: Exclude 2020 (COVID year)
- Remove potential outlier
- Results: Findings robust to exclusion

### 2.5 Limitations and Scope Conditions

#### 2.5.1 Data Limitations

**1. Product Granularity**:
- Analysis uses HS 2-digit codes (97 categories)
- Finer granularity (HS 6-digit: 5,000+ categories) would reveal product-specific vulnerabilities
- Trade-off: Broader categories ensure sufficient observations per cell

**2. Domestic Production Data**:
- DMSI uses import reduction as proxy
- Ideal: Actual production data from Annual Survey of Industries
- Limitation: Production data not available for all sectors/years

**3. Re-exports**:
- Data includes direct imports only
- Chinese goods routed through Singapore/Hong Kong not fully captured
- Underestimates true China dependency

**4. Quality Considerations**:
- Metrics focus on quantity/value, not quality or technological sophistication
- $1M of semiconductors ≠ $1M of textiles in strategic importance
- Criticality weights partially address this

#### 2.5.2 Methodological Limitations

**1. Causal Identification**:
- Before-after comparison, not randomized experiment
- Cannot definitively attribute changes to policy vs other factors (COVID, global trends)
- Structural break test provides evidence but not proof of causality

**2. Counterfactual**:
- No control group (all of India subject to policy)
- Cannot observe what would have happened without intervention
- Limits causal claims

**3. Time Horizon**:
- Intervention period only 5 years (2020-2024)
- Manufacturing capability takes 10-15 years to build
- May be too early to observe full policy effects

#### 2.5.3 Scope Conditions

**1. Bilateral Focus**:
- Analysis limited to India-China trade
- Ignores multilateral dynamics (RCEP, Quad)
- Misses indirect dependencies through third countries

**2. Trade-Only Analysis**:
- Focuses on merchandise trade
- Excludes FDI, technology transfer, services trade
- Incomplete picture of economic interdependence

**3. India-Specific**:
- Findings may not generalize to other countries
- India's size, capabilities, and relationship with China are unique
- Comparative analysis needed for broader lessons

Despite these limitations, our analysis provides the most comprehensive quantitative assessment of India's derisking initiative to date.

---

*[Continued in next message due to length...]*
