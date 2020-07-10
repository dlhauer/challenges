def stockRun(prices):
    max_run = cur_run = prev_price =  0
    for i, price in enumerate(prices):    
        cur_run += 1
        if (i < len(prices)-1
            and (prev_price < prices[i] > prices[i+1]
            or prev_price > prices[i] < prices[i+1])):
            max_run = max(cur_run, max_run)
            cur_run = 1
        prev_price = price
    return max(cur_run, max_run)

prices = [1]
print(stockRun(prices))
             