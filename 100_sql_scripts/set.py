purchases = ["fiction", "sci-fi", "fiction", "mystery", "sci-fi"]

def unique_genres(purchases):
    return set(purchases)

def common_books(c1, c2):
    return set(c1) & set(c2)

def all_books(c1, c2):
    return set(c1) | set(c2)

location_comments = {
    "Austin":  ["great", "slow", "great"],
    "Seattle": ["great", "clean"],
    "Houston": ["slow", "clean", "slow"]
}

def most_common_comment(location_comments):
    freq = {}
    for comments in location_comments.values():
        for comment in set(comments):      # deduplicate per location
            freq[comment] = freq.get(comment, 0) + 1
    return max(freq, key=lambda k: freq[k])


transactions = [("c1","fiction"),("c1","sci-fi"),("c1","mystery"),("c2","fiction"),("c2","sci-fi")]

def loyal_customer(transactions):
    genres = {}
    for cid, genre in transactions:
        if cid not in genres:
            genres[cid] = set()
        genres[cid].add(genre)
    return [cid for cid, g in genres.items() if len(g) >= 3]

