import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from data_fetcher import DataFetcher
from signal_generator import SignalGenerator
from risk_manager import RiskManager

# 🔄 Auto-refresh every 60 seconds (60000 ms)
st_autorefresh(interval=60000, key="refresh")

# Initialize strategy components
fetcher = DataFetcher()
signal_gen = SignalGenerator()
risk_mgr = RiskManager()

# Anchor coins and target dropdown options
anchor_symbols = ['BTC/USDT', 'ETH/USDT']
target_options = ['SOL/USDT', 'MATIC/USDT', 'XRP/USDT', 'DOGE/USDT', 'LTC/USDT']

# Page setup
st.set_page_config(page_title="Crypto Arbitrage Bot", layout="centered")
st.title("📈 Multi-Anchor Lagged Correlation Bot")
st.write("⏱️ Auto-refreshes every 60 seconds using Binance 1-minute OHLCV")

# Select target coin
target_symbol = st.selectbox("🎯 Select Target Coin", target_options)

# Extract closing prices
def get_close_prices(ohlcv):
    return [candle[4] for candle in ohlcv]

# Run signal logic
try:
    target_ohlcv = fetcher.fetch_ohlcv(target_symbol, limit=100)
    target_close = get_close_prices(target_ohlcv)

    signals = []
    for anchor in anchor_symbols:
        anchor_ohlcv = fetcher.fetch_ohlcv(anchor, limit=100)
        anchor_close = get_close_prices(anchor_ohlcv)
        signal = signal_gen.generate_signal(anchor_close, target_close)
        signals.append(signal)

    # Decision logic
    combined_signal = sum(signals)
    action = "HOLD"
    if combined_signal > 0:
        action = "BUY ✅"
    elif combined_signal < 0:
        action = "SELL ⚠️"

    # Show results
    st.subheader(f"📊 Combined Signal: **{action}**")
    result_df = pd.DataFrame({
        'Anchor Coin': anchor_symbols,
        'Signal': signals
    })
    st.dataframe(result_df)

except Exception as e:
    st.error(f"❌ Error fetching data: {e}")
