import time
from data_fetcher import DataFetcher
from signal_generator import SignalGenerator
from risk_manager import RiskManager

# Ask user for coin symbol
target_symbol = input("Enter target coin pair (e.g., SOL/USDT): ").strip().upper()
if '/' not in target_symbol:
    target_symbol = target_symbol + '/USDT'

anchor_symbols = ['BTC/USDT', 'ETH/USDT']

print(f"Running strategy for target: {target_symbol} with anchors: {anchor_symbols}")

# Initialize components
fetcher = DataFetcher()
signal_gen = SignalGenerator()
risk_mgr = RiskManager()

balance = 1000  # Example USD balance for position sizing

def get_close_prices(ohlcv):
    return [candle[4] for candle in ohlcv]

while True:
    try:
        target_ohlcv = fetcher.fetch_ohlcv(target_symbol, limit=100)
        target_close = get_close_prices(target_ohlcv)

        signals = []
        for anchor in anchor_symbols:
            anchor_ohlcv = fetcher.fetch_ohlcv(anchor, limit=100)
            anchor_close = get_close_prices(anchor_ohlcv)
            signal = signal_gen.generate_signal(anchor_close, target_close)
            signals.append(signal)

        combined_signal = sum(signals)
        action = "HOLD"
        if combined_signal > 0:
            action = "BUY"
        elif combined_signal < 0:
            action = "SELL"

        print(f"[{target_symbol}] Signals per anchor: {signals} → Combined Signal: {action}")
        time.sleep(60)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
