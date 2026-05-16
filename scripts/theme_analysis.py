import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),
    max_features=50
)

X = vectorizer.fit_transform(df["review"].astype(str))

keywords = vectorizer.get_feature_names_out()

print(keywords)