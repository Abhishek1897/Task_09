# 📊 City of Syracuse – City Streets 2011 Analysis

## 📌 Project Overview

This project analyzes the **City of Syracuse – City Streets (2011)** dataset from the Syracuse Open Data Portal. The objective is to build a structured, reproducible data analysis pipeline that evaluates data quality, explores patterns, and prepares the dataset for further infrastructure and neighborhood-level analysis.

The project follows a disciplined workflow including:

- Data acquisition and documentation
- Data cleaning and validation
- Exploratory Data Analysis (EDA)
- Statistical summaries and visualization
- LLM-assisted hypothesis generation (with safeguards)
- Modular, reproducible pipeline architecture

---

# 🏗 Project Structure


---

## Reproducible Analysis Pipeline

The project uses a deterministic pipeline:

1. Load raw dataset from `data_raw/`
2. Clean dataset using `src/clean.py`
3. Generate summary statistics using `src/analyze.py`
4. Create visualizations using `src/plots.py`
5. Log LLM prompts using `src/llm_log.py`
6. Save all outputs to disk

Run the pipeline from the project root:

```bash
python run_pipeline.py

---

# 🔄 Reproducible Analysis Pipeline

The pipeline is deterministic and reproducible.

### Data Flow


### Run the Pipeline

From the project root:

```bash
python run_pipeline.py
