from collections import Counter

def count_words(sentence):
    """ 
    :type sentence: str
    :rtype: int 
    """
    
    dict1 = Counter(sentence.split())
        
    return sorted(dict1.items(), key=lambda x: x[1], reverse= True)

print(count_words("apple banana apple orange banana apple"))