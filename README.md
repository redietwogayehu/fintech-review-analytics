#  Fintech Review Analytics

##  Overview

This project analyzes Google Play Store reviews of major Ethiopian banking applications — **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank** — to extract actionable insights on user experience, sentiment, and recurring product issues.

The goal is to transform unstructured customer feedback into structured insights that help improve mobile banking services, reduce user frustration, and prioritize feature development.

---

##  Banks Analyzed

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

##  Dataset

- **Total Reviews:** 1,500+
- **Source:** Google Play Store
- **Fields Collected:**
  - Review text
  - Rating (1–5 stars)
  - Review date
  - Bank name
  - Source (Google Play)

---

## Tech Stack

- Python 3
- pandas
- google-play-scraper
- transformers (HuggingFace)
- distilbert-base-uncased-finetuned-sst-2-english
- matplotlib
- seaborn

---

##  Pipeline

### 1. Data Collection
- Scraped Google Play Store reviews
- Minimum 400+ reviews per bank

### 2. Data Preprocessing
- Removed duplicates
- Handled missing values
- Standardized date formats (YYYY-MM-DD)

### 3. Sentiment Analysis
- DistilBERT sentiment classifier
- Labels: Positive / Negative
- Confidence scoring

### 4. Thematic Analysis
- Rule-based keyword extraction
- Themes:
  - Transaction Issues
  - Authentication Issues
  - App Stability Issues
  - Compatibility Issues
  - UI/UX Feedback
  - Feature Requests
  - Positive Feedback

### 5. Visualization
- Sentiment distribution by bank
- Theme frequency analysis

---

## Key Pain Points
- Transaction failures and delays
- App crashes and instability
- OTP/login authentication issues
- Device compatibility issues

##  Positive Drivers
- Ease of use
- General satisfaction with mobile banking functionality

---

## 📌 Limitations
- Possible bias in Google Play reviews
- Mixed-language text in reviews
- Sentiment model limitations for short texts
