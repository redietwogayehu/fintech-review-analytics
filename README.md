#  Fintech Review Analytics

##  Overview

This project analyzes Google Play Store reviews of major Ethiopian banking applications — **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank** — to extract actionable insights on user experience, sentiment, and recurring product issues.

The goal is to transform unstructured customer feedback into structured business intelligence that supports mobile banking reliability improvements, user satisfaction enhancement, and feature prioritization.

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
- Removed duplicate entries
- Handled missing values
- Standardized date format (YYYY-MM-DD)

### 3. Sentiment Analysis
- DistilBERT sentiment classifier
- Labels: Positive / Negative
- Confidence score generated per review

### 4. Thematic Analysis
- Rule-based keyword extraction
- Business-aligned theme mapping:
  - Transaction Issues
  - Authentication Issues
  - App Stability Issues
  - Compatibility Issues
  - UI/UX Feedback
  - Feature Requests
  - Positive Feedback

### 5. Database Engineering (PostgreSQL)
- Designed relational schema:
  - `banks` table
  - `reviews` table
- Data inserted using Python (SQLAlchemy pipeline)

### 6. Visualization & Insight Generation
- Matplotlib + Seaborn used for exploratory and comparative analysis
- Outputs support cross-bank benchmarking and decision-making

---

#  Task 4: Insights and Recommendations

##  Sentiment Overview (All Banks)

- Positive sentiment is dominant in general usability feedback
- Negative sentiment is concentrated in:
  - Transaction failures
  - Authentication (OTP/login) issues

###  Key Insight
System reliability issues are the primary driver of dissatisfaction across all banks, outweighing UI/UX concerns.

---

##  Commercial Bank of Ethiopia (CBE)

###  Key Drivers
- Convenient mobile banking experience
- General usability satisfaction

###  Key Pain Points
- Transaction failures and delays
- Device compatibility issues (especially Android/Huawei devices)

###  Recommendations
- Improve transaction failure handling and retry mechanisms
- Expand device compatibility testing across Android variants

---

##  Bank of Abyssinia (BOA)

###  Key Drivers
- Simple and intuitive interface
- Positive digital banking experience

###  Key Pain Points
- App crashes and instability
- OTP/login authentication failures

###  Recommendations
- Improve backend stability and API reliability
- Strengthen OTP delivery and authentication fallback mechanisms

---

##  Dashen Bank

###  Key Drivers
- Clean and intuitive UI
- General usability satisfaction

###  Key Pain Points
- Login/authentication inconsistencies
- Transaction processing delays

###  Recommendations
- Stabilize authentication system
- Optimize transaction processing speed and reliability

---

##  Cross-Bank Comparative Insights

| Bank | Primary Issue | Secondary Issue |
|------|--------------|----------------|
| CBE | Transaction failures | Device compatibility |
| BOA | App instability | Authentication failures |
| Dashen | Authentication issues | Transaction delays |

###  Key Insight
Across all banks, core system reliability (authentication + transaction processing) is the dominant driver of negative user experience, not UI/UX design.

---

##  Visualizations

Run all plots using:

```bash
python scripts/task4_visuals.py
