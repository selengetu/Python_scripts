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

transactions = [("c1","fiction"),("c1","sci-fi"),("c1","mystery"),("c2","fiction"),("c2","sci-fi")]
catalog = {"fiction", "sci-fi", "mystery"}
def bought_all(transactions, catalog):
    genres = {}
    for cid, genre in transactions:
        if cid not in genres:
            genres[cid] = set()
        genres[cid].add(genre)
    return [cid for cid, g in genres.items() if g == catalog]


def no_repeat_genre(transactions):
    from collections import defaultdict
    counts = defaultdict(list)
    for cid, genre in transactions:
        counts[cid].append(genre)
    return [cid for cid, genres in counts.items() if len(genres) == len(set(genres))]

def unique_words(reviews):
    words = set()
    for review in reviews:
        for word in review.split():
            words.add(word)
    return len(words)

def top_3_comments(location_comments):
    freq = {}
    for comments in location_comments.values():
        for c in set(comments):
            freq[c] = freq.get(c, 0) + 1
    sorted_comments = sorted(freq, key=lambda k: freq[k], reverse=True)
    return sorted_comments[:3]

def most_popular_book(purchases):
    book_customers = {}
    for cid, book_id in purchases:
        if book_id not in book_customers:
            book_customers[book_id] = set()
        book_customers[book_id].add(cid)
    return max(book_customers, key=lambda k: len(book_customers[k]))