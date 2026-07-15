import pandas as pd

# File paths
data_file = "/Users/nirajlondhe/Downloads/2019_production_reports.csv"
dictionary_file = "/Users/nirajlondhe/Downloads/Production_file_data_dictionary - Sheet1.csv"

# Load the production data
df = pd.read_csv(data_file)

# Optional: load data dictionary to inspect column definitions
data_dictionary = pd.read_csv(dictionary_file)

# Check available columns
print(df.columns)

dates = pd.to_datetime(df["report_date"], format="%m/%Y", errors="coerce")
flared = pd.to_numeric(df["flared"], errors="coerce")

total_2019_flared = flared[dates.dt.year == 2019].sum()

print(total_2019_flared)

dates = pd.to_datetime(df["report_date"], format="%m/%Y", errors="coerce")
df_2019 = df[dates.dt.year == 2019].copy()

df_2019["gas_prod"] = pd.to_numeric(df_2019["gas_prod"], errors="coerce")

totals = (
    df_2019.groupby(["operator_num", "name"])["gas_prod"]
    .sum()
    .sort_values(ascending=False)
)

top_operator = totals.head(1)

print(top_operator)


dates = pd.to_datetime(df["report_date"], format="%m/%Y", errors="coerce")
oil = pd.to_numeric(df["oil_vol"], errors="coerce")

work = pd.DataFrame({
    "date": dates,
    "oil_vol": oil
})

work_2019 = work[work["date"].dt.year == 2019]

monthly_totals = work_2019.groupby(work_2019["date"].dt.to_period("M"))["oil_vol"].sum()

print(monthly_totals)
print("month with most oil:", monthly_totals.idxmax())
print("oil production:", monthly_totals.max())


dates = pd.to_datetime(df["report_date"], format="%m/%Y", errors="coerce")

df_2019 = df[dates.dt.year == 2019].copy()

df_2019["oil_vol"] = pd.to_numeric(df_2019["oil_vol"], errors="coerce").fillna(0)
df_2019["gas_prod"] = pd.to_numeric(df_2019["gas_prod"], errors="coerce").fillna(0)

df_2019["well_id"] = (
    df_2019["api_county_code"].astype(str) + "-" +
    df_2019["api_seq_num"].astype(str) + "-" +
    df_2019["sidetrack_num"].astype(str)
)

operating = df_2019[
    (df_2019["oil_vol"] > 0) | (df_2019["gas_prod"] > 0)
]

county_counts = (
    operating.groupby("api_county_code")["well_id"]
    .nunique()
    .sort_values(ascending=False)
)

print(county_counts.head(1))