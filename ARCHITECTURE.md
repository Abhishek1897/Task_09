@'
# Architecture Review — City Streets 2011 (Week 6)

## System Architecture (Data Flow)

data_raw/city_streets_2011.csv  
→ **src/clean.py** (clean_city_streets)  
→ data_clean/city_streets_2011_clean.csv  
→ **src/analyze.py** (missing_summary, numeric_summary, plot_hist)  
→ outputs/tables/missing_summary.csv  
→ outputs/tables/numeric_summary.csv  
→ outputs/figures/hist_OBJECTID.png (example)  
→ **src/llm_log.py** (prompt logging only)  
→ prompts/prompt_log.jsonl  

## Key Design Decisions (with rationale)

- **Raw data is immutable**: input CSV stays in `data_raw/` so results are reproducible.
- **Separation of stages**:
  - acquisition/storage: `data_raw/`
  - cleaning: `src/clean.py` → `data_clean/`
  - analysis outputs: `outputs/`
  - LLM prompt logging: `prompts/`
- **Deterministic pipeline**: no randomness; same input → same outputs.
- **LLM guardrails**: LLM is used only for hypothesis generation (no numeric claims). All numbers must come from ground-truth tables.

## Dependencies & Environment

- Python 3.8+
- pandas
- matplotlib
- (optional for QA) pytest

## Deployment / Execution

Run from project root:

```bash
python -u run_pipeline.py
