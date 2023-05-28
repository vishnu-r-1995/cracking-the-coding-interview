class StockBuySellManager(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(0, len(prices)):
            if (i == len(prices) - 1):
                continue
            profit = max(prices[i+1:]) - prices[i]
            if (profit > max_profit):
                max_profit = profit
        return max_profit
    
    def maxProfit2(self,prices):
        #More optimized solution
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit