import os
import requests
import pandas as pd

# =============================================================================
# Configuration
# =============================================================================

BASE_URL = "https://api.mfapi.in/mf"

OUTPUT_FOLDER = "data/raw"

SCHEME_CODES = {
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip",
    125497: "HDFC_Top_100_Direct"
}


# =============================================================================
# Function to Fetch NAV Data
# =============================================================================

def fetch_nav(amfi_code, scheme_name):

    url = f"{BASE_URL}/{amfi_code}"

    print(f"\nFetching NAV for {scheme_name} ({amfi_code})...")

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        # Extract NAV history
        nav_history = data.get("data", [])

        if not nav_history:
            print(f"⚠️ No NAV data available for {scheme_name}")
            return

        # Convert JSON to DataFrame
        df = pd.DataFrame(nav_history)

        # Add AMFI code column
        df["amfi_code"] = amfi_code

        # Add scheme name column
        df["scheme_name"] = scheme_name.replace("_", " ")

        # Create output directory if it doesn't exist
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        # Save CSV
        output_path = os.path.join(
            OUTPUT_FOLDER,
            f"live_nav_{amfi_code}.csv"
        )

        df.to_csv(output_path, index=False)

        print(f"✅ Saved successfully -> {output_path}")

        print(f"Total NAV Records: {len(df)}")

    except requests.exceptions.RequestException as e:

        print(f"❌ Failed to fetch {scheme_name}")

        print(e)


# =============================================================================
# Main Program
# =============================================================================

print("=" * 80)
print("LIVE NAV DATA FETCH")
print("=" * 80)

for code, scheme in SCHEME_CODES.items():

    fetch_nav(code, scheme)

print("\n" + "=" * 80)
print("All API requests completed.")
print("=" * 80)