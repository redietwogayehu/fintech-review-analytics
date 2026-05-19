import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/reviews_with_sentiment_themes.csv")

# -----------------------------
# 1. SENTIMENT DISTRIBUTION BY BANK
# -----------------------------
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("outputs/sentiment_distribution.png", dpi=300)
plt.close()

# -----------------------------
# 2. THEME FREQUENCY DISTRIBUTION
# -----------------------------
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    y="identified_theme",
    order=df["identified_theme"].value_counts().index
)

plt.title("Theme Frequency Distribution")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.tight_layout()
plt.savefig("outputs/theme_distribution.png", dpi=300)
plt.close()

# -----------------------------
# 3. SENTIMENT BY THEME
# -----------------------------
plt.figure(figsize=(12, 6))

sns.countplot(
    data=df,
    y="identified_theme",
    hue="sentiment_label",
    order=df["identified_theme"].value_counts().index
)

plt.title("Sentiment Distribution Across Themes")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.tight_layout()
plt.savefig("outputs/sentiment_by_theme.png", dpi=300)
plt.close()

print("All visualizations saved successfully in outputs/")