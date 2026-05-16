from google_play_scraper import reviews
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():

    print(f"Scraping reviews for {bank}...")

    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        count=500
    )

    for review in result:

        all_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"],
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

print(df.head())

df.to_csv(
    "data/raw/bank_reviews_raw.csv",
    index=False
)

print("Scraping completed successfully.")