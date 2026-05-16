# fintech-review-analytics

# 📊 Fintech Review Analytics

## 📌 Overview

This project analyzes Google Play Store reviews of major Ethiopian banking applications — **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank** — to extract actionable insights on user experience, sentiment, and recurring product issues.

The goal is to transform unstructured customer feedback into structured insights that can help product teams improve mobile banking services, reduce user frustration, and prioritize feature development.

---

## 🏦 Banks Analyzed

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

## 📊 Dataset

- **Total Reviews:** 1,500+
- **Source:** Google Play Store
- **Fields Collected:**
  - Review text
  - Rating (1–5 stars)
  - Review date
  - Bank name
  - Source (Google Play)

---

## 🧰 Tech Stack

- Python 3
- pandas
- google-play-scraper
- transformers (HuggingFace)
- distilbert-base-uncased-finetuned-sst-2-english
- seaborn
- matplotlib

---

## 🔄 Project Pipeline

The project follows a structured data engineering workflow:

### 1. Data Collection
- Scraping Google Play Store reviews using `google-play-scraper`
- Collecting at least 400+ reviews per bank

### 2. Data Preprocessing
- Removing duplicates
- Handling missing values
- Normalizing date formats (YYYY-MM-DD)

### 3. Sentiment Analysis
- Using HuggingFace DistilBERT model
- Classifying reviews into:
  - Positive
  - Negative
- Assigning confidence scores

### 4. Thematic Analysis
- Rule-based keyword extraction
- Mapping reviews into business-relevant categories:
  - Transaction Issues
  - Authentication Issues
  - App Stability Issues
  - Compatibility Issues
  - UI/UX Feedback
  - Feature Requests
  - Positive Feedback

### 5. Visualization
- Sentiment distribution by bank
- Theme distribution across all banks

---
### 🟢 Positive Drivers
- High volume of positive feedback across all banks
- Users appreciate convenience and general usability of mobile banking apps

### 🔴 Major Pain Points
- Transaction failures and delays
- App crashes and instability
- Authentication issues (OTP/login problems)
- Device compatibility issues (notably Huawei devices)

---

## 📊 Visualizations

The project generates the following insights:

- Sentiment distribution by bank
- Frequency of user-reported issues (themes)
- Comparison of user experience across CBE, BOA, and Dashen

