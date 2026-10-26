# Quantitative Risk Analysis (QRA) Data Pipeline Practice

## Overview

This repository contains Python scripts demonstrating the core data engineering pipeline for Quantitative Risk Analysis (QRA). The pipeline handles ingestion, raw data validation, cleaning, and post-cleaning validation, ensuring data integrity before it is used in risk models.

## Project Structure

- `data/raw/`: Original, unmodified datasets (ignored by Git).
- `data/processed/`: Cleaned and validated datasets ready for modeling.
- `src/`: Python scripts for the data pipeline.
- `requirements.txt`: Python dependencies required to run the scripts.

## Implemented Pipelines

- **Source:** [Hugging Face](https://huggingface.co/datasets/Kickmuncher/economic_resilience_risk_model)
- **Script:** `src/data_analysis.py`
- **Key Operations:**
  - **Ingestion:** Loaded 10,000 rows and 22 columns (CSV). Identified that the JSON file contained metadata, not entity data.
  - **Validation (Raw):** Checked for duplicate EntityIDs and negative resource values. Identified `ResourceVolatilityIndex` as a zero-variance column (95.7% of values were 1.0).
  - **Cleaning:** Dropped `ResourceVolatilityIndex` (zero variance) and `RelativeAdaptationIndex` (multicollinearity).
  - **Validation (Clean):** Confirmed the final shape (10,000 rows, 20 columns) and verified 0 nulls.

## Data Quality Notes

- **Project Risk Dataset:** 72 statistical outliers were found in project budgets. Upon investigation, they were legitimate high-budget Construction and R&D projects, so they were retained.
- **Economic Resilience Dataset:** The JSON file in the raw data is a simulation metadata dictionary, not the primary dataset. The CSV file is used as the single source of truth.
