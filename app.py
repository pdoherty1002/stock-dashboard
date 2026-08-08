import streamlit as st
import yfinance as yf

# Page config MUST be the very first Streamlit command in the file
st.set_page_config(page_title="Stock Dashboard", page_icon="📈", layout="wide")

st.title("Stock Analysis Dashboard")

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
PERIODS = ["1mo", "3mo", "6mo", "1y", "2y", "5y"]

col_a, col_b = st.columns(2)
with col_a:
    selected_ticker = st.selectbox("Choose a stock", TICKERS)
with col_b:
    selected_period = st.selectbox("Time period", PERIODS, index=1)
try:

    ticker = yf.Ticker(selected_ticker)
    history = ticker.history(period=selected_period)

    if history.empty:
        st.warning(f"No data found for {selected_ticker}")
        st.stop()

except Exception as e:
    st.error(f"Something went wrong fetching data: {e}")

# Metric - goes wherever you want it to visually appear, e.g. right after the selectbox
latest_price = history["Close"].iloc[-1]
previous_price = history["Close"].iloc[-2]
change = latest_price - previous_price
st.metric(label=f"{selected_ticker} Price", value=f"${latest_price:.2f}", delta=f"${change:.2f}")

# Columns - goes wherever you want the table/chart to appear

display_history = history.copy()
display_history.index = display_history.index.strftime("%Y-%m-%d")
display_history = display_history.round(2)

col1, col2 = st.columns(2)
with col1:
    st.write(display_history)
with col2:
    st.line_chart(history["Close"], color="red")