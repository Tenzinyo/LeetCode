def stocks(stock_price):
    l,r=0,1
    max_profit=0
    while r<len(stock_price):
        if stock_price[l]<stock_price[r]:
            profit = stock_price[l]-stock_price[r]
            max_profit = max(max_profit,profit)
        else:
            l+=r
        r+=1
    return max_profit

def stocks(stock_price):
    max_profit=0
    i=0
    j=i+1
    for i in stock_price:
        for j in stock_price:
            if i<j:
                profit = stock_price[i]-stock_price[j]
                max_profit = max(max_profit, profit)
            else:
                i=j
            j+=1
    return max_profit
