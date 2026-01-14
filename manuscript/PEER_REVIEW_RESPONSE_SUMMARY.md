# Response to Reviewer 2 (Nature Portfolio)

## 1. "Screwdriver Effect" & HS 6-Digit Analysis
**Critique**: Provide 6-digit decomposition (HS 8517 vs 851770) to prove assembly vs component shift.
**Response**: We acknowledge a data limitation: our dataset is aggregated at the HS 2-digit level.
**Defense**: While we cannot plot the exact 6-digit shift, the **aggregate divergence** between HS 85 (Electronics +25%) and HS 84 (Machinery +12%) combined with the **Digital Paradox** structural break (+1.05% slope) provides strong inferential evidence. We have added a "Data Limitations" section acknowledging this.

## 2. "Organic Chemicals" Anomaly (Sensitivity Analysis)
**Critique**: Excluding HS 29 (Success) biases the result.
**Response**: We performed a rigorous sensitivity test (Section 3.5).
**Result**: Even *including* HS 29, the dependency trend **accelerates** from +0.50% (baseline) to +0.89% (post-2020).
**Conclusion**: The finding is **robust**. The volume of Electronics dependency is so large it swamps the success in Chemicals. See `Figure 9`.

## 3. "Digital Growth" Definition
**Critique**: Define the proxy for digital growth.
**Response**: We specified in Section 4.1 that "Digital Economy Growth" refers to the CAGR of the ICT Sector (Service Exports + Hardware Market Size) sourced from MeitY (Ministry of Electronics and IT) reports, contrasted with IIP (Index of Industrial Production) manufacturing growth.

## 4. SSVI Weights
**Critique**: Provide weights.
**Response**: Added **Appendix A** outlining the 1-5 criticality scale for all 7 strategic sectors.

## Final Status
The manuscript `nature_manuscript_full.tex` now contains:
- **Section 3.5**: Sensitivity Analysis.
- **Section 4.3**: Causal Validation.
- **Appendix A**: SSVI Methodology.
- **8 Figures** + **1 Sensitivity Figure**.
