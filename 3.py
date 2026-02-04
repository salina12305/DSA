def maxProfit(max_trades, daily_prices):
    if not daily_prices or max_trades == 0:
        return 0

    n = len(daily_prices)
    dp = [[0] * n for _ in range(max_trades + 1)]

    for t in range(1, max_trades + 1):
        max_diff = -daily_prices[0]
        for d in range(1, n):
            dp[t][d] = max(dp[t][d - 1], daily_prices[d] + max_diff)
            max_diff = max(max_diff, dp[t - 1][d] - daily_prices[d])
    return dp[max_trades][n - 1]
if __name__ == "__main__":
    max_trades_input = 2
    prices_input = [2000, 4000, 1000] 
    
    result = maxProfit(max_trades_input, prices_input)
    
    print("-" * 40)
    print(f"Daily Prices: {prices_input} NPR")
    print(f"Max Trades Allowed: {max_trades_input}")
    print(f"Maximum Achievable Profit: {result} NPR")
    print("-" * 40)