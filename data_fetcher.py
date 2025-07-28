import ccxt

class DataFetcher:
    def __init__(self):
        self.exchange = ccxt.binance({
            'enableRateLimit': True,
        })
    
    def fetch_ohlcv(self, symbol='BTC/USDT', timeframe='1m', limit=100):
        return self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
