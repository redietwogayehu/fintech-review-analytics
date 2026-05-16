import pandas as pd
from transformers import pipeline

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("data/raw/bank_reviews_cleaned.csv")

print("Shape:", df.shape)
print(df.head())


# ----------------------------
# SENTIMENT MODEL
# ----------------------------
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


# ----------------------------
# SENTIMENT ANALYSIS
# ----------------------------
sentiments = []

for text in df["review"].astype(str):
    result = sentiment_pipeline(text[:512])[0]

    sentiments.append({
        "sentiment_label": result["label"],
        "sentiment_score": result["score"]
    })

sentiment_df = pd.DataFrame(sentiments)
df = pd.concat([df, sentiment_df], axis=1)


# ----------------------------
# THEME FUNCTION (DEFINE ONCE)
# ----------------------------
def identify_theme(review):

    review = str(review).lower()

    # Authentication / login issues
    if any(word in review for word in ["login", "log in", "otp", "password", "pin"]):
        return "Authentication Issues"

    # Transfer / transaction problems
    elif any(word in review for word in ["transfer", "send money", "payment", "slow", "delay", "failed"]):
        return "Transaction Issues"

    # App crashes / technical errors
    elif any(word in review for word in ["crash", "bug", "error", "not working", "stuck", "freeze"]):
        return "App Stability Issues"

    # Device compatibility issues
    elif any(word in review for word in ["huawei", "device", "android", "iphone"]):
        return "Compatibility Issues"

    # UI / experience feedback
    elif any(word in review for word in ["ui", "design", "interface", "easy", "simple"]):
        return "UI/UX Feedback"

    # Positive generic feedback
    elif any(word in review for word in ["good", "great", "best", "excellent", "love", "nice", "amazing"]):
        return "Positive Feedback"

    # Feature requests
    elif "feature" in review:
        return "Feature Requests"

    else:
        return "Other"

# ----------------------------
# APPLY THEME FUNCTION
# ----------------------------
df["identified_theme"] = df["review"].apply(identify_theme)


# ----------------------------
# SAVE OUTPUT
# ----------------------------
df.to_csv("data/raw/reviews_with_sentiment_themes.csv", index=False)

print("Done.")