def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    sentence = "hello world hello"
    result = word_frequency(sentence)
    print(result)