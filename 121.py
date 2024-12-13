def maxProfit(prices: list[int]) -> int:  # Sliding Window problem
    p1, p2 = 0, 1  # Initialize two pointers: p1 (buy day pointer), p2 (sell day pointer)
    max_profit = 0

    while p2 < len(prices):
        if prices[p1] < prices[p2]:
            profit = prices[p2] - prices[p1]
            max_profit = max(max_profit, profit)  # Comparison between p2 and p1 with the current max_profit
        else:
            p1 = p2  # If p2 points to a lower price, move p1 to the current p2
        p2 += 1  # Always move p2 forward
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))

# Complexity:
# Time: O(n)
# Space: O(1)
