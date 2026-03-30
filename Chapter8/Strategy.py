import yfinance as yf
import pandas as pd
import numpy as np

# Download Data (4H safer than 1H)
df = yf.download("EURUSD=X", period="1y", interval="4h")

df = df[['Close']]
df.dropna(inplace=True)

# ----- EMA 200 -----
df['EMA200'] = df['Close'].ewm(span=200, adjust=False).mean()

# ----- RSI 14 -----
delta = df['Close'].diff()
gain = np.where(delta > 0, delta, 0)
loss = np.where(delta < 0, -delta, 0)

gain_avg = pd.Series(gain).rolling(14).mean()
loss_avg = pd.Series(loss).rolling(14).mean()

rs = gain_avg / loss_avg
df['RSI'] = 100 - (100 / (1 + rs))

df.dropna(inplace=True)

# ----- Backtest -----
balance = 10000
risk = 0.01
wins = 0
losses = 0
position = None

for i in range(len(df)):

    price = df['Close'].iloc[i]
    ema = df['EMA200'].iloc[i]
    rsi = df['RSI'].iloc[i]

    if position is None:
        if price > ema and 40 < rsi < 50:
            entry = price
            sl = price - 0.0030
            tp = price + 0.0060
            position = "buy"

    elif position == "buy":
        if price <= sl:
            balance -= balance * risk
            losses += 1
            position = None

        elif price >= tp:
            balance += balance * risk * 2
            wins += 1
            position = None

total = wins + losses
winrate = (wins / total) * 100 if total > 0 else 0

print("Final Balance:", round(balance, 2))
print("Trades:", total)
print("Wins:", wins)
print("Losses:", losses)
print("Win Rate:", round(winrate, 2), "%")