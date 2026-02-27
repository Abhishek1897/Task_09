# City of Syracuse Streets Data Analysis (2011)

## Project Overview

This project presents a reproducible analytical pipeline built to explore and evaluate the **City of Syracuse Streets (2011)** dataset from the Syracuse Open Data Portal.

The goal of this project is to:
- Assess data quality and completeness
- Generate descriptive statistics and visual insights
- Identify meaningful patterns within municipal street data
- Demonstrate responsible integration of LLM-assisted hypothesis generation
- Deliver a fully reproducible and well-documented data analysis system

This project was completed as part of a structured multi-phase data analysis assignment including discovery, development, validation, and documentation.

---

# Problem Statement

Municipal open data is valuable for transparency, planning, and community engagement. However, before drawing conclusions, it is critical to assess:

- How complete is the dataset?
- What inconsistencies or limitations exist?
- What patterns are visible in the available street attributes?
- How reliable are automated or LLM-generated interpretations?

This project answers those questions using structured exploratory data analysis and reproducible pipeline design.

---

# Data Source

**Dataset:** City Streets (2011)  
**Source:** Syracuse Open Data Portal  
**Acquisition Method:** Manual download  
**Acquisition Logged In:** `acquisition_log.txt`  

The raw dataset is stored in:


---

# System Architecture

The project follows a modular, deterministic pipeline:

data_raw/
city_streets_2011.csv
↓
src/clean.py
↓
data_clean/city_streets_2011_clean.csv
↓
src/analyze.py
↓
outputs/tables/
↓
src/plots.py
↓
outputs/figures/
↓
src/llm_log.py
↓
prompts/prompt_log.jsonl


### Key Design Principles

- Raw data remains unchanged
- Clear separation of cleaning, analysis, visualization
- Deterministic outputs (no randomness)
- All artifacts written to disk
- LLM outputs validated against ground truth statistics

---

# Analytical Approach

## Data Quality Assessment

- Missing value analysis per column
- Missing percentage calculation
- Identification of incomplete attributes
- Review of categorical consistency
- Evaluation of numeric distributions

## Statistical Analysis

For numeric fields:
- Count
- Mean
- Standard deviation
- Min / Max
- Quartiles

## Visualization

Generated outputs include:
- Histogram of numeric attributes
- Missing value distribution chart
- Summary tables

All figures are saved to:
outputs/figures/
All statistical tables are saved to:
outputs/tables/


---

# LLM Integration & Validation

LLMs are used strictly for:
- Hypothesis generation
- Narrative drafting

LLMs are NOT used for:
- Numerical computation
- Statistical calculation
- Final claims

Safeguards implemented:
- Prompt logging (`prompt_log.jsonl`)
- Ground-truth statistics computed via Pandas
- Validation of LLM outputs against computed results
- Explicit documentation of uncertainty

---

# Running the Project

## 1. Install Dependencies
pip install -r requirements.txt


## 2. Run the Pipeline

From the project root:
python run_pipeline.py


This will:

- Load raw dataset
- Clean the data
- Generate summary statistics
- Create visualizations
- Log LLM prompts
- Save all outputs to structured directories

---

# Testing

Unit tests verify:

- Data cleaning behavior
- Missing value calculations
- Numeric summary outputs

Run tests with:
pytest -q


---

# Repository Structure
city_streets_project/
│
├── data_raw/
├── data_clean/
├── outputs/
│ ├── figures/
│ └── tables/
├── prompts/
├── src/
├── tests/
│
├── run_pipeline.py
├── requirements.txt
├── README.md
├── TECHNICAL.md
├── METHODOLOGY.md
├── data_dictionary.csv
├── acquisition_log.txt


---

# Key Findings (Exploratory Phase)

- Certain attributes contain significant missing values
- Dataset is limited in size (162 records)
- Numeric distributions are uneven and may reflect categorical encoding
- Data completeness varies across fields
- Careful interpretation is required before policy conclusions

---

# Limitations

- Dataset covers only year 2011
- Limited sample size (162 rows)
- Some attributes contain missing or inconsistent values
- No spatial visualization implemented
- No integration with housing dataset (future extension)

---

# Future Work

- Integrate housing dataset for cross-analysis
- Add spatial mapping
- Build interactive dashboard interface
- Expand to multi-year comparison
- Deploy web-based visualization tool

---

# Project Status

✔ Reproducible pipeline implemented  
✔ Modular architecture  
✔ Data cleaning + EDA completed  
✔ Statistical summaries generated  
✔ Visualizations created  
✔ LLM guardrails implemented  
✔ Documentation complete  
✔ Tests implemented  

This project is ready for submission and demonstration.

---

# Contact

Abhishek Shinde  
Applied Data Science  
Syracuse University  

