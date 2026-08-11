import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score

# --- Load data ---
ticker = yf.Ticker("AAPL")
df = ticker.history(period="2y") 

# --- Target: did price go UP the next day? ---
df["NextClose"] = df["Close"].shift(-1)
df["Target"] = (df["NextClose"] > df["Close"]).astype(int)

# --- Feature 1: Daily return ---
df["DailyReturn"] = df["Close"].pct_change()

# --- Feature 2 & 3: Moving averages ---
df["MA10"] = df["Close"].rolling(window=10).mean()
df["MA200"] = df["Close"].rolling(window=200).mean()

# --- Feature 4: Volume change ---
df["VolumeChange"] = df["Volume"].pct_change()

# --- Feature 5: Volatility ---
df["Volatility"] = df["Close"].rolling(window=5).std()

# --- Feature 6: RSI ---
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df["RSI"] = calculate_rsi(df["Close"])

# --- Drop rows with missing values ---
# Early rows won't have full moving averages/RSI yet, and the last row has no "next day"
df = df.dropna()

print(df[["Close", "DailyReturn", "MA10", "MA200", "VolumeChange", "Volatility", "RSI", "Target"]].head(10))
print(f"\nTotal rows after cleaning: {len(df)}")
print(f"Target distribution:\n{df['Target'].value_counts()}")

features = ["DailyReturn", "MA10", "MA200", "VolumeChange", "Volatility", "RSI"]
X = df[features]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10, shuffle=False)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"\n\n\n\n----Model evaluation-----\n")
print(f"Accuracy: {accuracy:.2f}")
print(confusion_matrix(y_test, predictions))

print(y_train.value_counts())
print(y_test.value_counts())