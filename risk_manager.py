class RiskManager:
    def __init__(self, max_position_size=0.1):
        self.max_position_size = max_position_size
    
    def size_position(self, balance, price):
        amount = balance * self.max_position_size / price
        return amount
