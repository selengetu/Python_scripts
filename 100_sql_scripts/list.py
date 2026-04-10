prices = [12, 5, 22, 8, 3, 17, 5, 9, 22, 3]

def find_avg_price(prices):
    if len(prices) >0:
        avg_price = round((sum(prices)/ len(prices)),2)
        print(avg_price)

budget = 10

def find_under_budget_price(prices):
    under_budget = []
    for p in prices:
        if p< budget:
            under_budget.append(p)
    print(len(under_budget))

def second_most_expensive(prices):
    unique = list(set(prices))
    unique.sort(reverse=True)
    return unique[1]

orders = [1,2,3,4,5,6,7]
n = 3

def chunk_list(orders, n):
    return [orders[i:i+n] for i in range(0, len(orders), n)]

