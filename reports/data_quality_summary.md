# Day 1 - Data Quality Summary

## Dataset Overview

- Successfully loaded all 10 provided CSV datasets.
- Successfully fetched live NAV data from MF API.
- Successfully fetched NAV history for 5 key mutual fund schemes.

## Data Quality Checks

### Missing Values

- Most datasets contain no missing values.
- `04_monthly_sip_inflows.csv` contains 12 missing values in the `yoy_growth_pct` column.
- These missing values are expected because Year-over-Year growth cannot be calculated for the first 12 months.

### Duplicate Records

- No duplicate rows were found in any dataset.

### AMFI Code Validation

- Total AMFI Codes in fund_master: 40
- Total AMFI Codes in nav_history: 40
- All AMFI codes successfully validated.

### Fund Master Exploration

- Total Schemes: 40
- Total Fund Houses: 10
- Total Categories: 2
- Total Sub Categories: 12
- Total Risk Categories: 5

## API Validation

Successfully downloaded and stored live NAV history for:

- HDFC Top 100 Direct
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

## Conclusion

All datasets passed the initial ingestion and validation checks.
The project is ready for further preprocessing, SQL analysis, and dashboard development.