def count_words(sentence):
    """ 
    :type sentence: str
    :rtype: int 
    """
    dict1 = {}
    words = sentence.split()
    
    for n in words:
        dict1[n] = dict1.get(n, 0) + 1
        
    return sorted(dict1.items(), key=lambda x: x[1], reverse= True)

print(count_words("apple banana apple orange banana apple"))