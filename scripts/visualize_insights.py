import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/reviews_with_sentiment_themes.csv")


# ----------------------------
# PLOT 1: Theme Distribution
# ----------------------------
plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    y="identified_theme",
    order=df["identified_theme"].value_counts().index
)

plt.title("Top User Issues Across Banks")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.tight_layout()
plt.show()


# ----------------------------
# PLOT 2: Sentiment by Bank
# ----------------------------
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")

plt.tight_layout()
plt.show()