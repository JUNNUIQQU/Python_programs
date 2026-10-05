def count_character_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


text = "hello"
print(count_character_frequency(text))