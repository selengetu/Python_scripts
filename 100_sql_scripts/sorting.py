def sort_by_price(books):
    return sorted(books, key=lambda b: b[1])

def top_3(prices):
    return sorted(prices, reverse=True)[:3]

def largest_number(number):
    return int("".join(sorted(str(number), reverse=True)))

def smallest_odd_digits(number):
    odd = sorted([d for d in str(number) if int(d) % 2 != 0])
    return int("".join(odd)) if odd else 0

def max_books(prices, budget):
    prices.sort()
    count = total = 0
    for p in prices:
        if total + p <= budget:
            total += p
            count += 1
        else:
            break
    return count


def min_books_for_target(prices, target):
    prices.sort(reverse=True)
    total = count = 0
    for p in prices:
        total += p
        count += 1
        if total >= target:
            return count
    return -1  # can't reach target


def sort_by_spend(transactions):
    totals = {}
    for cid, amount in transactions:
        totals[cid] = totals.get(cid, 0) + amount
    return sorted(totals, key=lambda k: totals[k], reverse=True)


def sort_genres(purchases):
    freq = {}
    for g in purchases:
        freq[g] = freq.get(g, 0) + 1
    return sorted(freq, key=lambda k: freq[k], reverse=True)

from functools import cmp_to_key
def largest_combined(nums):
    nums = [str(n) for n in nums]
    nums.sort(key=cmp_to_key(lambda a,b: 1 if a+b < b+a else -1))
    return "".join(nums)

widths = [1, 3, 2, 4, 1]
capacity = 5
def min_shelves(widths, capacity):
    shelves = 1
    current = 0
    for w in widths:
        if current + w <= capacity:
            current += w
        else:
            shelves += 1
            current = w
    return shelves