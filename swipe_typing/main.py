'''
    Swipe typing example:
        suppose s = "hgferyjkllkop" and dictionary = ["coffee", "coding", "happy", "hello", "hop"]
        then the only possible valid words that are subsequence of the given string are:
         - "hello"
         - "hop"
'''

def is_subsequence(word, s):
    i, j = 0, 0
    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1
        j += 1
    return i == len(word)

def getValidWord(s, dictionary):
    valid_words = []
    for word in dictionary:
        if is_subsequence(word, s):
            valid_words.append(word)
    return valid_words[0] if valid_words else ""

if __name__ == '__main__':
    s = input("Enter the sequence: ")

    dictionary_count = int(input("Enter the number of words in the dictionary: ").strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input("Enter dictionary word: ")
        dictionary.append(dictionary_item)

    result = getValidWord(s, dictionary)
    print("Valid word:", result)

