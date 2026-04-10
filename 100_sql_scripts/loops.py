def above_threshold(sales, threshold):
    count = 0
    for s in sales:
        if s > threshold:
            count += 1
    return count

def running_total(sales):
    result = []
    total = 0
    for s in sales:
        total += s
        result.append(total)
    return result

def pair(customers, orders):
    return list(zip(customers, orders))

def longest_streak(daily):
    best = current = 0
    for d in daily:
        if d > 0:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def moving_avg(prices, k):
    result = []
    for i in range(len(prices) - k + 1):
        window = prices[i:i+k]
        result.append(sum(window) / k)
    return result

def missing_id(ids):
    n = len(ids) + 1
    return n * (n + 1) // 2 - sum(ids)

def net_profit(revenues, costs):
    return [r - c for r, c in zip(revenues, costs)]

def flatten(nested):
    return [item for sublist in nested for item in sublist]

def max_window(sales, k):
    current = sum(sales[:k])
    best = current
    for i in range(k, len(sales)):
        current += sales[i] - sales[i - k]
        best = max(best, current)
    return best