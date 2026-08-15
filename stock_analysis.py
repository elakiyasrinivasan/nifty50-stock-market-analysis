import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download NIFTY 50 data
nifty = yf.download(
    "^NSEI",
    start="2020-01-01",
    end="2026-08-15",
    auto_adjust=False
)
print(nifty.head())


nifty["MA20"] = nifty["Close"].rolling(window=20).mean()
nifty["MA50"] = nifty["Close"].rolling(window=50).mean()
print(nifty[["Close", "MA20", "MA50"]].tail())


nifty["Daily_Return"] = nifty["Close"].pct_change()
print(nifty[["Close", "Daily_Return"]].tail())


nifty["Volatility"] = nifty["Daily_Return"].rolling(window=20).std()
print(nifty[["Daily_Return", "Volatility"]].tail())


plt.figure(figsize=(12, 6))
plt.plot(nifty.index, nifty["Close"], label="NIFTY 50")
plt.plot(nifty.index, nifty["MA20"], label="20-Day Moving Average")
plt.plot(nifty.index, nifty["MA50"], label="50-Day Moving Average")
plt.title("NIFTY 50 Stock Market Analysis")
plt.xlabel("Date")
plt.ylabel("Index Value")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(12, 5))
plt.plot(
    nifty.index,
    nifty["Volatility"],
    label="20-Day Volatility")
plt.title("NIFTY 50 Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.grid(True)
plt.show()


print("\nNIFTY 50 Statistics")
print("--------------------")
print("Average Price:", nifty["Close"].mean())
print("Maximum Price:", nifty["Close"].max())
print("Minimum Price:", nifty["Close"].min())
print(
    "Average Daily Return:",
    nifty["Daily_Return"].mean())
print(
    "Average Volatility:",
    nifty["Volatility"].mean())


print("=" * 50)
print("       NIFTY 50 STOCK MARKET ANALYSIS")
print("=" * 50)


print("=" * 50)
print("Analysis completed successfully!")
print("=" * 50)


nifty.to_csv("nifty50_analysis.csv")
print("Data saved as nifty50_analysis.csv")  
