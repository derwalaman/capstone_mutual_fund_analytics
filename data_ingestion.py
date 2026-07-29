import os
import pandas as pd

# =============================================================================
# Configuration
# =============================================================================

DATA_FOLDER = "data/raw"

CSV_FILES = sorted(
    [file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")]
)

# =============================================================================
# Dataset Analysis
# =============================================================================


def analyse_dataset(df, file_name):
    """Perform basic exploratory analysis on a dataset."""

    print("=" * 80)
    print(f"Dataset : {file_name}")
    print("=" * 80)

    print(f"\nShape : {df.shape}")

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst Five Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print(f"\nDuplicate Rows : {df.duplicated().sum()}")

    print("\nSummary Statistics")
    print(df.describe())

    print("\nColumns")
    print(df.columns.tolist())


# =============================================================================
# Fund Master Exploration
# =============================================================================


def explore_fund_master(df):
    """Explore master mutual fund dataset."""

    print("\n" + "=" * 80)
    print("FUND MASTER EXPLORATION")
    print("=" * 80)

    print(f"\nTotal Schemes : {len(df)}")

    print(f"\nTotal Fund Houses : {df['fund_house'].nunique()}")
    print(df["fund_house"].unique())

    print(f"\nTotal Categories : {df['category'].nunique()}")
    print(df["category"].unique())

    print(f"\nTotal Sub Categories : {df['sub_category'].nunique()}")
    print(df["sub_category"].unique())

    print(f"\nTotal Risk Categories : {df['risk_category'].nunique()}")
    print(df["risk_category"].unique())

    print(f"\nTotal AMFI Codes : {df['amfi_code'].nunique()}")


# =============================================================================
# AMFI Validation
# =============================================================================


def validate_amfi_codes(fund_master_df, nav_history_df):
    """Validate that every AMFI code exists in NAV history."""

    print("\n" + "=" * 80)
    print("AMFI CODE VALIDATION")
    print("=" * 80)

    fund_master_codes = set(fund_master_df["amfi_code"])
    nav_history_codes = set(nav_history_df["amfi_code"])

    missing_codes = fund_master_codes - nav_history_codes

    print(f"\nTotal Fund Master Codes : {len(fund_master_codes)}")
    print(f"Total NAV History Codes : {len(nav_history_codes)}")

    if not missing_codes:
        print("\n✅ Validation Successful")
        print("Every AMFI code exists in nav_history.csv")
    else:
        print("\n❌ Missing AMFI Codes")
        print(sorted(missing_codes))


# =============================================================================
# Main ETL Pipeline
# =============================================================================


def main():

    fund_master_df = None
    nav_history_df = None

    print("=" * 80)
    print("MUTUAL FUND DATA INGESTION PIPELINE")
    print("=" * 80)

    for file in CSV_FILES:

        file_path = os.path.join(DATA_FOLDER, file)

        print(f"\nReading : {file}")

        try:

            df = pd.read_csv(file_path)

            if file == "01_fund_master.csv":
                fund_master_df = df

            elif file == "02_nav_history.csv":
                nav_history_df = df

            analyse_dataset(df, file)

            if file == "01_fund_master.csv":
                explore_fund_master(df)

        except Exception as e:

            print(f"\n❌ Failed to read {file}")
            print(f"Reason : {e}")

    if fund_master_df is not None and nav_history_df is not None:
        validate_amfi_codes(fund_master_df, nav_history_df)
    else:
        print("\n❌ Unable to perform AMFI validation.")


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    main()