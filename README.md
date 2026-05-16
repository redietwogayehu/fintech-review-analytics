# fintech-review-analytics

# Customer Experience Analytics for Fintech Apps

## Overview

This project analyzes customer reviews from Ethiopian banking mobile applications to identify user satisfaction drivers, recurring complaints, and actionable product insights.

The analysis focuses on:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Project Objectives

- Scrape Google Play Store reviews
- Clean and preprocess review data
- Perform sentiment analysis
- Identify recurring customer experience themes
- Store processed data in PostgreSQL
- Generate business insights and recommendations

## Technologies Used

- Python
- pandas
- google-play-scraper
- PostgreSQL
- matplotlib
- scikit-learn
- transformers
- GitHub Actions

## Data Collection Methodology

Reviews were collected using the `google-play-scraper` library from the Google Play Store.

Collected fields include:

- Review text
- Rating
- Review date
- Bank name
- Source

A minimum of 400 reviews were collected for each bank application.

## Preprocessing Steps

The preprocessing pipeline included:

- Removing duplicate reviews
- Removing missing values
- Standardizing date formats
- Exporting cleaned datasets for downstream analysis

## Current Progress

- Task 1 completed:
  - Scraping pipeline
  - Data preprocessing
  - Clean dataset generation

- Task 2 in progress:
  - Sentiment analysis
  - Theme extraction

## Limitations

- Some reviews may contain mixed-language content.
- Google Play review availability may vary over time.
- Review sentiment may contain user bias.