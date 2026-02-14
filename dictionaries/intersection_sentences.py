import string

def find_common_words(input):
    # Extract sentences
    sentence1 = input[0]
    sentence2 = input[1]

    def clean_and_split(sentence):

        cleaned_words = []
        for word in sentence.split():
            cleaned = word.strip(string.punctuation).lower()
            cleaned_words.append(cleaned)

        return set(cleaned_words)

    words1 = clean_and_split(sentence1)
    words2 = clean_and_split(sentence2)
    
    common_words = words1.intersection(words2)
    return sorted(list(common_words))  # Returns a sorted list of common words

if __name__ == "__main__":
    sentences = [
        "Apple banana orange!",
        "Banana apple grape."
    ]

    result = find_common_words(sentences)
    print(result)