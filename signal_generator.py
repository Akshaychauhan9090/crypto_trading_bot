import pandas as pd
import numpy as np

class SignalGenerator:
    def __init__(self, max_lag=10):
        self.max_lag = max_lag
    
    def calculate_lagged_correlation(self, anchor_prices, target_prices):
        correlations = []
        for lag in range(1, self.max_lag + 1):
            corr = pd.Series(anchor_prices).corr(pd.Series(target_prices).shift(lag))
            correlations.append((lag, corr))
        best_lag, best_corr = max(correlations, key=lambda x: abs(x[1]) if x[1] is not None else -np.inf)
        return best_lag, best_corr
    
    def generate_signal(self, anchor_close, target_close):
        lag, corr = self.calculate_lagged_correlation(anchor_close, target_close)
        if corr is None or abs(corr) < 0.3:
            return 0
        if len(anchor_close) < 2:
            return 0
        if corr > 0 and anchor_close[-1] > anchor_close[-2]:
            return 1
        elif corr < 0 and anchor_close[-1] < anchor_close[-2]:
            return -1
        else:
            return 0
