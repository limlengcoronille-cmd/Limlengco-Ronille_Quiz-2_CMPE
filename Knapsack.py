def knapsack(items, max_weight, max_items):
    """
    items: list of tuples (name, weight, value)
    max_weight: maximum weight the bag can carry
    max_items: maximum number of items allowed
    """
    n = len(items)

    dp = [[[0 for _ in range(max_items + 1)]
           for _ in range(max_weight + 1)]
           for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(max_weight + 1):
            for k in range(max_items + 1):
            
                dp[i][w][k] = dp[i - 1][w][k]

                if weight <= w and k > 0:
                    dp[i][w][k] = max(
                        dp[i][w][k],
                        value + dp[i - 1][w - weight][k - 1]
                    )
    chosen_items = []
    w = max_weight
    k = max_items

    for i in range(n, 0, -1):
        if dp[i][w][k] != dp[i - 1][w][k]:
            name, weight, value = items[i - 1]
            chosen_items.append(name)
            w -= weight
            k -= 1

    chosen_items.reverse()
    return dp[n][max_weight][max_items], chosen_items

items = [
    ("Bucket", 1, 10),
    ("Fried Chicken", 2, 15),
    ("Brick", 3, 40)
]

max_weight = 5
max_items = 2

max_value, stolen_items = knapsack(items, max_weight, max_items)

print("Maximum value stolen:", max_value)
print("Items stolen:", stolen_items)