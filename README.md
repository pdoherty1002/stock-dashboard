# Stock Analysis Dashboard

A Streamlit web app for viewing historical price data and charts for a small set of pre-selected tech stocks.

## What it does
- Choose a stock from a fixed list (AAPL, MSFT, GOOGL, AMZN, NVDA)
- Choose a time period (1mo to 5y)
- View the latest price with change indicator
- View a formatted price history table
- View a line chart of closing price over time

## Tools
Python, Streamlit, yfinance, pandas

## Run it locally
```
pip install streamlit yfinance pandas
streamlit run app.py
```
## Run online
https://stock-dashboard-6ueahhi3aeobagxnunb8ak.streamlit.app/

## Known limitations
Uses Yahoo Finance's free, unofficial API via `yfinance`. Occasionally rate-limited when running on shared cloud infrastructure (Streamlit Community Cloud) — works reliably when run locally.

## Status
v1 — data display and visualization. No predictive/analytical features yet by design; this version focuses on a clean, reliable data pipeline first.
