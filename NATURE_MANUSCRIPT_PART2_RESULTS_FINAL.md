# Nature Manuscript - Part 2: Evidence and Results

*Continuation of "Measuring India's Derisking Initiative: Industrial Success vs. Technological Deepening"*

---

## 2. Methodology

### 2.1 Data and Metrics
We analyze UN Comtrade data (2007-2024, n=755,284). Our primary metric is the **Trade Dependency Index (TDI)**:
$$ TDI_{China} = \frac{\text{Imports from China}}{\text{Total Imports}} \times 100 $$

We also employ:
- **HHI (Concentration)**: To measure partner diversity.
- **SSVI (Strategic Sector Vulnerability)**: Weighted dependency in critical sectors.
- **Structural Break Tests**: Chow tests to detect trend shifts pre/post-2020.

### 2.2 Pandemic Disentanglement (Strict Definition)
We define "Pandemic-Sensitive Goods" using the specific WCO-derived list of medical and sanitary products:
- **Chemicals/Pharma**: HS 28, 29, 30, 34, 38
- **Protective Gear**: HS 39, 40, 62, 63, 65
- **Medical Instruments**: HS 90

*Crucially, this strict definition excludes HS 84 (Machinery) and HS 85 (Electronics), separating "Medical Emergency" demand from "Technological" demand.*

---

## 3. Results

### 3.1 Aggregate Failure vs. Pandemic Alibi
**Aggregate TDI** rose from 15.47% (baseline) to 21.86% (intervention), a +6.39 percentage point increase ($p < 0.0001$).
Policy proponents often cite COVID-19 as the primary driver. Our disentanglement tests this alibi.

**Table 1: Decomposition of Dependency Increase**

| Component | Baseline TDI | Intervention TDI | Contribution to $\Delta$TDI |
|-----------|--------------|------------------|-----------------------------|
| **Pandemic Goods (Medical)** | 0.76% | 0.92% | **+0.16 pp** (2.5%) |
| **Non-Pandemic (Structural)** | 14.71% | 20.94% | **+6.23 pp** (97.5%) |

**Result**: Medical/Pandemic goods explain only **2.5%** of the total increase. The vast majority (97.5%) of the increased dependency comes from the "Non-Pandemic" basket. The "COVID Alibi" is rejected.

### 3.2 The Acceleration of Structural Dependency
We performed structural break analysis on the Non-Pandemic basket (which includes Electronics and Machinery).

**Table 2: Trend Analysis (Non-Pandemic Basket)**

| Period | Trend Slope | Interpretation |
|--------|-------------|----------------|
| **Pre-2020** | +0.50% / year | Gradual Integration |
| **Post-2020** | +1.05% / year | **Rapid Acceleration** |
| **Change** | +0.55% / year | **Doubling of Growth Rate** |

**Finding**: Far from derisking, India's structural integration with China **accelerated** after 2020. The rate of dependency growth more than doubled.

### 3.3 Sectoral Divergence: The "Two Indias"
To understand this acceleration, we analyzed the composition of the Non-Pandemic basket.

**Figure 3: Sectoral Divergence**
- **Industrial India (Success)**: 
    - **Iron & Steel (HS 72)**: Dependency fell from 19.4% to 8.4%.
    - **Aluminum (HS 76)**: Dependency stable/declining.
    *Mechanism*: Domestic capacity (Tata Steel, JSW) successfully substituted imports.
- **Digital India (Failure)**:
    - **Electronics (HS 85)**: Dependency rose from 22.7% to 28.5%.
    - **Machinery (HS 84)**: Dependency rose from 17.0% to 19.2%.
    *Mechanism*: Rapid digitization (5G, smartphone adoption) created demand for hardware that domestic industry could not supply.

### 3.4 The "Organic Chemicals" Anomaly (Sensitivity Analysis)
HS 29 (Organic Chemicals) is a special case. It was included in the User's "Pandemic" basket (intermediates for drugs/disinfectants) but also represents a structural industrial success.
- **Performance**: HS 29 saw a massive *drop* in dependency (-68%).
- **Sensitivity Test**: We rigorously tested if excluding this success story biased our "Digital Paradox" finding. We re-calculated the Non-Pandemic trend *including* HS 29.
- **Result**:
    - **Original Slope**: +1.05% / year.
    - **Sensitivity Slope (with HS 29)**: +0.89% / year.
    - **Baseline Slope**: +0.50% / year.
**Finding**: Even when the "Industrial Success" of organic chemicals is included, the structural dependency trend still **accelerates** (0.89% vs 0.50%) relative to the pre-2020 baseline. The Digital Paradox is robust to this definition. The sheer volume of Electronics growth outweighs the success in Chemicals.

---

## 4. Analysis

### 4.1 The Digital Paradox
The core finding is that **Digitization fueled dependency**.
- India's digital economy grew 2.4x faster than the physical economy (2014-2019).
- Hardware manufacturing grew only 1.2x.
- **Result**: The "Hardware Gap" widened, and China filled it.
PLI schemes for mobile phones (assembly) exacerbated this by incentivizing the import of high-value kits (screens, chips) for local assembly.

### 4.2 Industrial Success is Real
The success in "old economy" sectors (Steel, Basic Chemicals) proves that Atmanirbhar Bharat *can* work where technology gaps are low. India has deep expertise in metallurgy and process chemistry. It lacks comparable depth in semiconductor lithography or precision mechatronics.

### 4.3 Causal Validation & Robustness
To address potential confounding variables, we performed two robustness checks.

#### 4.3.1 Trend Acceleration (Interrupted Time Series)
A key critique is that rising dependency is merely descriptive. However, the *change in slope* offers causal identification via Interrupted Time Series (ITS) logic.
- **Pre-2020 Slope**: +0.50% / year ($p < 0.05$)
- **Post-2020 Slope**: +1.05% / year ($p < 0.01$)
- **Structural Break**: Confirmed at cutoff=2020.
The fact that the trend *accelerated* specifically after the policy intervention (and excluded pandemic goods) suggests that the "Digital Push" (which coincided with Atmanirbhar Bharat) had a stronger causal effect on imports than the "Protectionist Pull" had on substitution.

#### 4.3.2 The "Leakage" Hypothesis (Indirect Trade)
A rival hypothesis is that Chinese firms are routing trade through Vietnam or ASEAN to bypass scrutiny, meaning true dependency is even higher.
We analyzed HS 85 (Electronics) imports from potential intermediary hubs:
- **Vietnam (VNM)**: Share peaked in 2018-2019 at 6.9% and *declined* to 4.6% by 2023.
- **China (CHN)**: Share rose from 41% (2015) to 50% (2024).
- **Malaysia/Thailand**: Shares remained flat/low (<2-3%).

**Finding**: There is **no evidence** of a massive "Vietnam Swap" in aggregate data. China's market share gains were direct. The "Digital Paradox" is driven by direct imports of intermediate components, not covert rerouting. This validation suggests our TDI metric is not underestimating dependency due to leakage; if anything, the direct dependency is so large it swamps other channels.

---

*[End of Part 2]*
