import pandas as pd
from sqlalchemy import create_engine

# ----------------------------
# LOAD CSV DATA
# ----------------------------
df = pd.read_csv("data/raw/reviews_with_sentiment_themes.csv")

print("CSV loaded successfully.")
print(df.head())

# ----------------------------
# CONNECT TO POSTGRESQL
# ----------------------------
engine = create_engine("postgresql://localhost/fintech_reviews")

print("Connected to PostgreSQL.")

# ----------------------------
# INSERT DATA INTO DATABASE
# ----------------------------
df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully.")