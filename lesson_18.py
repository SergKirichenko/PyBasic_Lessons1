class Statement:
    def __int__(self):
        self.balance_uah = 1000.0
        self.balance_usd = 0.0
        self.rate = 29.25

    def reset(self):
        pass

class Trader:
    def __init__(self):
        self.statement = Statement()

    def get_balance_uah(self):
        return self.statement.balance_uah

    def reset(self):
        self.statement.reset()


class Trader_2(Statement):
    def get_balance_uah(self):
        return self.balance_uah
