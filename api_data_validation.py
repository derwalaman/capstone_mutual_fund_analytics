import os
import pandas as pd

RAW_FOLDER = "data/raw"


def validate_live_nav_files():

    print("=" * 80)
    print("LIVE NAV DATA VALIDATION")
    print("=" * 80)

    files = [
        file
        for file in os.listdir(RAW_FOLDER)
        if file.startswith("live_nav_") and file.endswith(".csv")
    ]

    for file in files:

        print("\n" + "-" * 80)
        print(f"File : {file}")
        print("-" * 80)

        file_path = os.path.join(RAW_FOLDER, file)

        df = pd.read_csv(file_path)

        print(f"Rows               : {len(df)}")
        print(f"Columns            : {len(df.columns)}")

        print("\nColumns")
        print(df.columns.tolist())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

        print("\nLatest NAV Record")

        print(df.iloc[0])

        print("\nOldest NAV Record")

        print(df.iloc[-1])

        print("\nDate Range")

        print(
            f"{df.iloc[-1]['date']}  --->  {df.iloc[0]['date']}"
        )

    print("\n" + "=" * 80)
    print("Validation Completed Successfully")
    print("=" * 80)


if __name__ == "__main__":

    validate_live_nav_files()