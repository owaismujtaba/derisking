# PEER REVIEW: "Measuring India's Derisking Initiative: A Novel Multi-Metric Approach"

**Journal**: *International Organization* / *World Politics* / *International Studies Quarterly*  
**Reviewer**: Anonymous  
**Date**: January 14, 2026  
**Recommendation**: **MAJOR REVISIONS REQUIRED**

---

## Overall Assessment

This manuscript attempts to develop a quantitative framework to measure India's trade derisking efforts vis-à-vis China. While the multi-metric approach shows promise and the data collection is commendable, **critical methodological flaws, contradictory findings, and insufficient theoretical grounding prevent publication in its current form**. The authors must address fundamental issues before this work can contribute meaningfully to the literature on economic statecraft and trade policy evaluation.

**Overall Score**: 4/10 (Reject with invitation to resubmit after major revisions)

---

## MAJOR CONCERNS

### 1. **CRITICAL DATA INTERPRETATION ERROR** ⚠️

**Issue**: The manuscript contains **contradictory results** that suggest fundamental data processing errors.

**Evidence**:
- The report (Section 3.1) claims China TDI **decreased** from 4.48% (2015) to 3.44% (2022)
- However, the actual analysis output shows China TDI **increased** from 18.01% (2015) to 21.72% (2022)
- The walkthrough document confirms the corrected interpretation shows **opposite findings**

**Impact**: This is a **fatal flaw**. The entire analysis and all conclusions are based on incorrect data filtering. The authors appear to have confused:
- India's **exports** (what other countries import FROM India)
- India's **imports** (what India imports FROM other countries)

**Required Action**:
1. **Immediate data validation** - Verify TradeFlow definitions in UN Comtrade
2. **Rerun entire analysis** with corrected filtering
3. **Reverse all conclusions** if the corrected data shows increased dependency
4. **Explain the error** transparently in methodology section

**Verdict**: **REJECT until this is resolved**

---

### 2. **Weak Theoretical Framework**

**Issue**: The paper lacks grounding in international political economy theory.

**Missing Elements**:
- No engagement with **economic interdependence** literature (Keohane & Nye, Hirschman)
- No discussion of **weaponized interdependence** (Farrell & Newman, 2019)
- No connection to **strategic trade policy** frameworks
- No theoretical justification for why these 7 metrics matter

**Consequences**:
- Metrics appear ad-hoc rather than theory-driven
- No clear hypothesis testing
- Unclear what "success" means theoretically

**Required**:
- Add Section 1.3: "Theoretical Framework"
- Ground metrics in asymmetric interdependence theory
- Develop testable hypotheses BEFORE presenting results
- Cite: Hirschman (1945), Drezner (2021), Farrell & Newman (2019)

---

### 3. **Methodological Weaknesses**

#### 3.1 **Arbitrary Metric Selection**

**Problem**: Why these 7 metrics? Why not others?

- No justification for SCRS weights (w1=0.4, w2=0.3, w3=0.3)
- CPODS denominator uses absolute value - why? This obscures direction
- SSVI criticality weights (1-5) appear subjective with no validation
- Geographic diversity proxy (# of partners / 50) lacks theoretical basis

**Required**:
- Sensitivity analysis for all weights
- Robustness checks with alternative specifications
- Expert validation of criticality weights (Delphi method?)

#### 3.2 **Temporal Specification Issues**

**Problem**: The baseline/intervention split is problematic.

- **2020 as intervention start** is arbitrary
  - Make in India launched in 2014
  - Border tensions began in 2017 (Doklam)
  - COVID-19 confounds 2020 as policy intervention point
  
- **No interrupted time series analysis**
- **No counterfactual** - what would have happened without policy?

**Required**:
- Multiple intervention points (2014, 2017, 2020)
- Difference-in-differences with comparable countries
- Synthetic control method (Abadie et al., 2010)

#### 3.3 **Endogeneity Concerns**

**Problem**: Reverse causality not addressed.

- Did policy cause trade shifts, or did trade shifts cause policy?
- China's own export restrictions (rare earths, APIs) may drive results
- Global supply chain restructuring post-COVID affects all countries

**Required**:
- Instrumental variables approach
- Event study methodology
- Control for global trends (compare with Vietnam, Bangladesh)

---

### 4. **Data Quality Issues**

#### 4.1 **UN Comtrade Limitations**

**Unaddressed Problems**:
- **Mirror data discrepancies** - India's reported imports ≠ China's reported exports
- **Re-exports** - Singapore/Hong Kong intermediation not accounted for
- **Misclassification** - HS code changes over time (2007, 2012, 2017, 2022 revisions)
- **Informal trade** - Not captured in official statistics

**Required**:
- Reconcile mirror data
- Adjust for re-exports using OECD TiVA data
- Use concordance tables for HS code changes
- Acknowledge informal trade limitations

#### 4.2 **Missing Variables**

**Critical Omissions**:
- **Domestic production data** - DMSI is only a proxy
- **FDI flows** - Chinese investment in India manufacturing
- **Technology transfer** - Quality of imports matters
- **Price data** - Import values may reflect price changes, not volume

**Required**:
- Incorporate ASI (Annual Survey of Industries) data
- Add FDI analysis from RBI
- Quality-adjusted trade indices
- Separate price and quantity effects

---

### 5. **Statistical Rigor Deficiencies**

**Missing**:
- **No confidence intervals** - Are changes statistically significant?
- **No hypothesis tests** - Informal "eyeballing" of trends
- **No regression analysis** - Just descriptive statistics
- **No standard errors** - Measurement uncertainty ignored

**Required**:
- Bootstrap confidence intervals for all metrics
- t-tests for period comparisons
- Panel regression: TDI_it = α + β·Post2020_t + γ·Controls_it + ε_it
- Granger causality tests for policy → trade relationship

---

### 6. **Contradictory Findings Not Explained**

**Internal Inconsistencies**:

1. **TDI decreased BUT HHI increased**
   - If China share fell, why did concentration rise?
   - Suggests USA replaced China (not diversification)
   
2. **CPODS = 1.70 BUT SCRS declined**
   - If diversification successful, why did resilience fall?
   - Metrics contradict each other
   
3. **Sector improvements BUT aggregate dependency increased**
   - Electronics SSVI fell 46%, yet overall TDI rose?
   - Composition effects not explained

**Required**:
- Reconcile contradictions
- Decomposition analysis (which sectors drive aggregate trends?)
- Explain USA concentration vs. diversification paradox

---

### 7. **Policy Implications Overstated**

**Problems**:

- **Causal claims without causal identification**
  - "PLI schemes demonstrate effectiveness" - no counterfactual
  - "China-Plus-One strategy working" - correlation ≠ causation
  
- **Recommendations not evidence-based**
  - "Expand PLI to pharmaceuticals" - but pharma dependency INCREASED
  - "Monitor USA concentration" - but no threshold defined
  
- **Ignores political constraints**
  - No discussion of WTO compatibility
  - No cost-benefit analysis
  - No consideration of Chinese retaliation

**Required**:
- Tone down causal language
- Acknowledge policy trade-offs
- Discuss implementation challenges
- Add cost estimates

---

## MODERATE CONCERNS

### 8. **Literature Review Inadequate**

**Missing Citations**:
- **Economic statecraft**: Baldwin (1985), Blanchard & Ripsman (2013)
- **Trade policy evaluation**: Goldstein & Gulotty (2021)
- **China's trade power**: Norris (2016), Kastner (2016)
- **India-China relations**: Mohan (2021), Pant (2021)

**Required**: Comprehensive lit review in Section 1.4

### 9. **Measurement Validity Questions**

**SCRS Components**:
- "Geographic diversity" = # of partners - but Qatar and USA both count as 1?
- "Critical redundancy" = suppliers per product - but ignores switching costs
- Weights (0.4, 0.3, 0.3) not validated

**CPODS**:
- Assumes all alternatives equally valuable
- Ignores quality differences (German vs. Vietnamese machinery)
- No adjustment for product sophistication

**Required**: Construct validity discussion

### 10. **Presentation Issues**

**Clarity**:
- Executive summary contradicts actual findings
- Figures/tables missing (only referenced, not shown)
- Technical jargon not defined (HS codes, TiVA)

**Reproducibility**:
- Code available (good!) but not peer-reviewed
- No replication package with raw data
- Computational environment not specified

**Required**:
- Align summary with findings
- Add visualizations (time series plots, heatmaps)
- Deposit replication materials in Dataverse

---

## MINOR CONCERNS

### 11. **Scope Limitations**

- **Bilateral focus** ignores multilateral dynamics (RCEP, Quad)
- **Trade-only** analysis misses investment, technology, people flows
- **India-centric** - no comparison with other countries' derisking

### 12. **Temporal Coverage**

- **2024 data incomplete** (analysis run in January 2026)
- **Too short intervention period** (2020-2024 = 4 years)
- **Need longer time series** for robust trend identification

---

## POSITIVE ASPECTS

**Strengths**:
1. ✅ **Comprehensive data** - 755K records, 18 years
2. ✅ **Multi-dimensional approach** - 7 metrics better than single indicator
3. ✅ **Sector-specific analysis** - SSVI by industry useful
4. ✅ **Reproducible** - Code and data available
5. ✅ **Policy-relevant** - Addresses important question

---

## SPECIFIC RECOMMENDATIONS

### Short-term (Required for Resubmission):

1. **FIX DATA INTERPRETATION ERROR** - This is non-negotiable
2. Add theoretical framework (5-7 pages)
3. Implement basic statistical tests (t-tests, regressions)
4. Reconcile contradictory findings
5. Tone down causal claims
6. Add comprehensive literature review

### Medium-term (Strengthen Analysis):

7. Synthetic control or DiD analysis
8. Incorporate domestic production data
9. Adjust for re-exports and HS code changes
10. Sensitivity analysis for all parameters
11. Add visualizations (time series, heatmaps)

### Long-term (Future Research):

12. Compare with other countries (Vietnam, Japan, EU)
13. Extend to FDI and technology flows
14. Develop predictive models
15. Qualitative case studies of specific sectors

---

## VERDICT

**Decision**: **REJECT AND RESUBMIT**

**Rationale**: 
The fundamental data interpretation error is **disqualifying**. Until the authors verify their filtering logic and rerun the analysis with correct data, this manuscript cannot be evaluated on its merits. The corrected results may show the **opposite** conclusion (dependency increased, not decreased), which would require a complete rewrite.

**If corrected data confirms increased dependency**:
- This would be a **more interesting finding** (policy failure)
- Requires explanation of why derisking failed
- More valuable contribution to literature

**If corrected data confirms decreased dependency**:
- Must still address all other methodological concerns
- Add causal identification strategy
- Reconcile internal contradictions

**Estimated time to resubmission**: 6-9 months

---

## RECOMMENDATION TO AUTHORS

1. **Immediately validate data** - This is urgent
2. **Consult with trade economist** - Need econometric rigor
3. **Consider co-authoring** with political scientist specializing in India-China relations
4. **Aim for working paper first** - Get feedback before journal submission
5. **Be transparent about error** - Acknowledge and explain in revised version

**Potential**: If fundamental issues are addressed, this could become a **strong contribution** to the literature on economic statecraft and trade policy evaluation.

---

**Reviewer Recommendation**: **Major Revisions Required**  
**Confidence**: High  
**Expertise**: International Political Economy, Trade Policy, Quantitative Methods
