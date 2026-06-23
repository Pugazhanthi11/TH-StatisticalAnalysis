import pandas as pd

# Load dataset
df = pd.read_csv("covid_data.csv")

print("Original Dataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df = df.fillna(0)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_covid_data.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as cleaned_covid_data.csv")