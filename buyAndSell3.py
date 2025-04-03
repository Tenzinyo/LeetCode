def maxProfit(self, prices: List[int]) -> int:
        s1,b1,s2,b2 = 0,float('-inf'),0,float('-inf')
        for i in range(len(prices)):
            price = prices[i]
            b1 = max(b1,-price)
            s1 = max(s1,b1+price)
            b2 = max(b2,s1-price)
            s2 = max(s2,b2+price)
        return s2
