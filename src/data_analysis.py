import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE_CSV = PROJECT_ROOT / "data" / "raw" / "FOM.csv"
# RAW_FILE_JSON = PROJECT_ROOT / "data" / "raw" / "FOM_metadata.json"
CLEAN_FILE = PROJECT_ROOT / "data" / "processed" / "FOM_clean.csv"

def ingest_data_csv(filepath):
  df_csv = pd.read_csv(filepath)
  print("Ingesting data ...")
  print(df_csv.shape)
  return df_csv

# def ingest_data_json(filepath):
#   df_json = pd.read_json(filepath)
#   print("Ingesting data ...")
#   print(df_json.shape)
#   print(df_json.head())
#   return df_json

def validate_raw_data(df):
  print(f"Duplicate EntityID: {df["EntityID"].duplicated().sum()}")
  print(df[["StartingResources", "SurvivalTime", "FinalResourceBalance"]].lt(0).sum())
  print(df["ResourceVolatilityIndex"].value_counts())

def clean_data(df):
  print("Cleaning data ...")
  df_clean = df.copy()
  df_clean = df_clean.drop(columns=["ResourceVolatilityIndex"])
  df_clean = df_clean.drop(columns=["RelativeAdaptationIndex"])
  print(df_clean.shape)
  return df_clean

def validate_clean_data(df):
  print("Validating data ...")
  print(f"Number of NULL values: {df.isnull().sum().sum()}")
  print("ResourceVolatilityIndex" in df.columns)
  print("RelativeAdaptationIndex" in df.columns)
  return True

if __name__ == "__main__":
  raw_df_csv = ingest_data_csv(RAW_FILE_CSV)
  validate_raw_data(raw_df_csv)
  clean_df = clean_data(raw_df_csv)
  validate_clean_data(clean_df)
  
  clean_df.to_csv(CLEAN_FILE, index=False)
  print(f"Pipeline complete. Clean data saved to {CLEAN_FILE}")