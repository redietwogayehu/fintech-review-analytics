#  Fintech Review Analytics

##  Overview

This project analyzes Google Play Store reviews of major Ethiopian banking applications — **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank** — to extract actionable insights on user experience, sentiment, and recurring product issues.

The goal is to transform unstructured customer feedback into structured business intelligence that helps improve mobile banking reliability, user satisfaction, and feature prioritization.

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

##  Tech Stack

- Python 3
- pandas
- google-play-scraper
- transformers (HuggingFace)
- distilbert-base-uncased-finetuned-sst-2-english
- matplotlib
- seaborn
- PostgreSQL
- SQLAlchemy

---

##  End-to-End Pipeline

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
- Confidence scoring added per review

### 4. Thematic Analysis
- Rule-based keyword extraction
- Business-relevant themes:
  - Transaction Issues
  - Authentication Issues
  - App Stability Issues
  - Compatibility Issues
  - UI/UX Feedback
  - Feature Requests
  - Positive Feedback

### 5. Database Engineering (PostgreSQL)
- Designed relational schema with:
  - banks table
  - reviews table
- Inserted processed dataset using Python (SQLAlchemy)

### 6. Visualization & Insights
All visualizations are generated using Matplotlib and Seaborn.

---

##  Task 4: Insights and Recommendations

###  Sentiment Overview
- Positive sentiment dominates general usability feedback
- Negative sentiment is mainly driven by transaction and authentication issues

**Key Insight:**  
Reliability issues outweigh feature-related concerns across all banks.

---

##  Commercial Bank of Ethiopia (CBE)

###  Drivers
- Convenient mobile banking experience
- General usability satisfaction

###  Pain Points
- Transaction failures and delays
- Device compatibility issues (Android-specific reports)

###  Recommendations
- Improve transaction reliability and error handling
- Expand device compatibility testing

---

##  Bank of Abyssinia (BOA)

###  Drivers
- Easy-to-use interface
- Positive digital banking experience

###  Pain Points
- App crashes and instability
- OTP/login authentication failures

###  Recommendations
- Strengthen backend stability
- Improve OTP and authentication reliability

---

##  Dashen Bank

###  Drivers
- Simple and intuitive UI
- Positive usability feedback

###  Pain Points
- Login/authentication issues
- Occasional transaction delays

###  Recommendations
- Improve login system stability
- Optimize transaction processing speed

---

##  Cross-Bank Comparison

- **CBE** → Highest transaction failure complaints
- **BOA** → Highest app instability issues
- **Dashen** → Strong UI feedback but weaker authentication reliability

**Key Insight:**  
All banks face major challenges in core banking reliability rather than UI/UX design.

---

##  Visualizations

All plots are generated using:
