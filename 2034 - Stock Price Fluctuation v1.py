class StockPrice:

    def __init__(self):
        self.prices = {}
        self.latestTime = 0
        self.maxPrice = float('-inf')
        self.minPrice = float('inf')
    def update(self, timestamp: int, price: int) -> None:
        old_price = self.prices.get(timestamp)

        need_recalc_max = (old_price is not None and old_price == self.maxPrice)
        need_recalc_min = (old_price is not None and old_price == self.minPrice)

        self.prices[timestamp] = price
        self.latestTime = max(self.latestTime, timestamp)

        self.maxPrice = max(self.maxPrice, price)
        self.minPrice = min(self.minPrice, price)

        if need_recalc_max:
            self.maxPrice = max(self.prices.values())
        if need_recalc_min:
            self.minPrice = min(self.prices.values())



    def current(self) -> int:
        return self.prices[self.latestTime]
        

    def maximum(self) -> int:
        return self.maxPrice
        

    def minimum(self) -> int:
        return self.minPrice

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
