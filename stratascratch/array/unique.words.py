from collections import Counter

def non_repeated_words(input):
    sentence1 = input[0]
    sentence2 = input[1]
    
    word_counts = Counter(sentence1.split() + sentence2.split())
    
    res = []
    for w, n in word_counts.items():
        if n == 1:
            res.append(w)
    return res
            