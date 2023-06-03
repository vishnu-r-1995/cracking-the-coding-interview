class StockBuySellManager2(object):
    def maxProfit(self, prices):
        previous = 0
        later = 1
        total_profit = 0
        while later < len(prices):
            current_profit = prices[later] - prices[previous]
            if prices[previous] < prices[later]:
                total_profit += current_profit
                
            previous = later
            later += 1
        return total_profit
