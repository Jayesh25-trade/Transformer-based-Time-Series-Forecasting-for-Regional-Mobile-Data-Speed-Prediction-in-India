import pandas as pd
filename = r"D:\mobile-speed-forecast\data\raw\merged_output.csv"

try:
    df = pd.read_csv(filename, sep="\t", header=None)
    if df.shape[1] == 1:
        df = pd.read_csv(filename, sep=",", header=None)
except Exception as e:
    print("Error reading file:", e)
    raise

print(df.head())

print(df.info())
rows, cols = df.shape
print(f"\nNumber of rows: {rows}")
print(f"Number of columns: {cols}")

##########################################################################

df = pd.read_csv(filename, sep=",", header=0, low_memory=False)

# Convert numeric columns
df["output"] = pd.to_numeric(df["output"], errors='coerce')
df["signal_strength"] = pd.to_numeric(df["signal_strength"], errors='coerce')

# Preview first rows
print(df.head())

# Show number of rows and columns
rows, cols = df.shape
print(f"\nNumber of rows: {rows}")
print(f"Number of columns: {cols}")

#######################################################################################################

# Extract month from Source File
df["Month"] = df["Source File"].str.extract(r'([a-zA-Z]+)25_publish\.csv')

# Map month name to numeric
month_map = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}
df["Month"] = df["Month"].str.lower().map(month_map)

# Pivot upload/download into separate columns and aggregate using sum
df_clean = df.pivot_table(
    index=["service_provider", "tech", "signal_strength", "circle", "Month"],
    columns="test_type",
    values="output",
    aggfunc="sum"  # sums multiple entries
).reset_index()

# Save cleaned file
output_file = "cleaned_data.csv"
df_clean.to_csv(output_file, index=False)

# Preview cleaned data
print(df_clean.head())

###########################################################################################
df_clean["Year"] = 2024

# Build a proper datetime column (first day of each month)
df_clean["Date"] = pd.to_datetime(
    dict(year=df_clean["Year"], month=df_clean["Month"], day=1)
)

# Sort by operator, region, and date
df_clean = df_clean.sort_values(["service_provider", "circle", "tech", "Date"]).reset_index(drop=True)

# Preview
print(df_clean.head())

# Save updated dataset
df_clean.to_csv("cleaned_data_with_date.csv", index=False)
print("\nSaved cleaned_data_with_date.csv")