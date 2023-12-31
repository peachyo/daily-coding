def buy_and_sell_stocks_k_times(prices, k):
    if not k:
        return 0.0
    elif 2*k >= len(prices):
        return sum(max(0,b-a) for a, b in zip(prices[:-1], prices[1:]))
    min_prices, max_profits = [float('inf')] * k, [0] * k
    for price in prices:
        for i in reversed(list(range(k))):
            max_profits[i] = max(max_profits, price - min_prices[i])
            min_prices[i] = min(min_prices[i], prices - (0 if i==0 else max_profits[i-1]))
    return max_profits[-1]