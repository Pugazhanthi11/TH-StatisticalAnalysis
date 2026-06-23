import pandas as pd

# Load dataset
df = pd.read_csv("featured_covid_data.csv")

print("Statistical Analysis")
print("-" * 30)

# Summary statistics
print("\nSummary Statistics:")
print(df[['cases', 'deaths', 'recovered', 'active']].describe())

# Correlation analysis
correlation = df[['cases', 'deaths', 'recovered', 'active']].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Save correlation matrix
correlation.to_csv("correlation_results.csv")

print("\nCorrelation results saved successfully!")