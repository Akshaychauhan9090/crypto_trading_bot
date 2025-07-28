# crypto_trading_bot

# 📈 Multi-Anchor Lagged Correlation Arbitrage Bot

A real-time cryptocurrency arbitrage signal bot that uses **lagged correlation** between a **target coin** and multiple **anchor coins** (like BTC, ETH) to generate **Buy, Sell, or Hold** signals based on live Binance data.

Built with:
- 🐍 Python
- 📊 Pandas, NumPy
- 🌐 Streamlit (interactive UI)
- 📡 CCXT (real-time crypto data from Binance)

---

## 🔧 Features

- 🔍 Select your **target coin** from dropdown (e.g., MATIC/USDT, SOL/USDT)
- 📡 Fetch **real-time OHLCV data** (1-minute timeframe) from Binance
- 📈 Calculate **lagged correlation signals**
- 🧠 Combine multiple signals to decide **BUY / SELL / HOLD**
- ⏱️ Auto-refreshes every **60 seconds**
- 🖥️ Interactive **Streamlit dashboard**
- 🧪 Clean architecture (modular files)

---

## 📂 Folder Structure

crypto_trading_bot/
│
├── main.py # (Optional) CLI version with signal loop
├── app.py # ✅ Streamlit UI for real-time signals
├── data_fetcher.py # Handles Binance OHLCV data fetching
├── signal_generator.py # Lagged correlation logic & signal generation
├── risk_manager.py # Basic position sizing module
├── requirements.txt # All required Python packages
└── README.md # You are here

yaml
Copy
Edit

---

## 🚀 How to Run

### 1. Clone the repository or unzip the project

```bash
cd crypto_trading_bot
2. Create a virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Linux/Mac
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
🛠️ How It Works
The app pulls 1-minute OHLCV data for a selected target coin and compares it with anchor coins (e.g., BTC/USDT, ETH/USDT)

It calculates lagged correlations (delayed influence) to detect leading price movements

If anchor coins move significantly and correlate with the target coin, a buy/sell signal is generated

Signals are shown every minute via the UI

📦 Dependencies
ccxt – real-time market data from Binance

pandas, numpy – time-series & math processing

streamlit – UI interface

streamlit-autorefresh – to auto-refresh UI every 60s

📌 Sample Usage
Open the app in your browser

Select a target coin from the dropdown (e.g., MATIC/USDT)

Wait or click 🔄 to refresh signal

View:

Combined Signal: BUY / SELL / HOLD

Anchor-wise signal table
