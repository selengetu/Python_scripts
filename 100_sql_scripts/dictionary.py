words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

def find_freq(words):
    freq = {}

    for w in words:
        freq[w] = 1 + freq.get(w, 0)
    print(max(freq, key=lambda k: freq[k]))



d = {"a": 1, "b": 2, "c": 3}


def swap(d):
    s = {}
    print({v: k for k, v in d.items()})

transactions = [("c1", 20), ("c2", 15), ("c1", 30), ("c3", 10), ("c2", 25)]

def total_spend(transactions):
    totals = {}
    for cid, amount in transactions:
        totals[cid] = totals.get(cid, 0) + amount
    print(max(totals, key = lambda k:totals[cid]))
total_spend(transactions)

words = ["apple", "banana", "apple", "cherry", "banana", "date"]

def first_unique(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    for w in words:
        if freq[w] == 1:
            return w

def top_two_genres(purchases):
    freq = {}
    for g in purchases:
        freq[g] = freq.get(g, 0) + 1
    sorted_genres = sorted(freq, key=lambda k: freq[k], reverse=True)
    return sorted_genres[:2]


def group_by_customer(transactions):
    groups = {}
    for cid, amount in transactions:
        if cid not in groups:
            groups[cid] = []
        groups[cid].append(amount)
    return groups
