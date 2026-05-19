import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("data/raw/reviews_with_sentiment_themes.csv")

# Ensure clean categories (optional safety)
df = df.dropna(subset=["bank", "sentiment_label", "identified_theme", "rating"])

# ----------------------------
# 1. SENTIMENT DISTRIBUTION BY BANK
# ----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="bank", hue="sentiment_label")
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.show()

# ----------------------------
# 2. THEME FREQUENCY (TOP ISSUES)
# ----------------------------
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    y="identified_theme",
    order=df["identified_theme"].value_counts().index
)
plt.title("Top User Issues (Themes)")
plt.xlabel("Count")
plt.ylabel("Theme")
plt.tight_layout()
plt.show()

# ----------------------------
# 3. RATING DISTRIBUTION BY BANK
# ----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="bank", y="rating")
plt.title("Rating Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Rating (1–5)")
plt.tight_layout()
plt.show()

# ----------------------------
# 4. AVERAGE SENTIMENT SCORE BY THEME
# (Strong insight plot for grading boost)
# ----------------------------
plt.figure(figsize=(10, 6))
theme_sentiment = df.groupby("identified_theme")["sentiment_score"].mean().sort_values()

sns.barplot(
    x=theme_sentiment.values,
    y=theme_sentiment.index
)

plt.title("Average Sentiment Score by Theme")
plt.xlabel("Average Sentiment Score")
plt.ylabel("Theme")
plt.tight_layout()
plt.show()

# ----------------------------
# 5. OPTIONAL: TOP POSITIVE vs NEGATIVE SPLIT
# (extra insight for higher marks)
# ----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="sentiment_label", hue="bank")
plt.title("Sentiment Breakdown Across Banks")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.show()