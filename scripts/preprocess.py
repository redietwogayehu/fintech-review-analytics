import pandas as pd

df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna(subset=["review", "rating"])

# Normalize date
df["date"] = pd.to_datetime(
    df["date"],
    dayfirst=True
).dt.strftime("%Y-%m-%d")

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/raw/bank_reviews_cleaned.csv",
    index=False
)

print("Preprocessing completed.")