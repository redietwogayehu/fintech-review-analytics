-- =========================================
-- Fintech Review Analytics - Task 3 Schema
-- =========================================

-- =========================================
-- Banks Table
-- =========================================
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name TEXT NOT NULL,
    app_name TEXT
);

-- =========================================
-- Reviews Table
-- =========================================
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label TEXT,
    sentiment_score FLOAT,
    identified_theme TEXT,
    source TEXT
);