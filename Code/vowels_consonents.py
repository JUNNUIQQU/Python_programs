def count_vowels_and_consonants(text):
    vowels = 0
    consonants = 0

    for character in text.lower():
        if character in "aeiou":
            vowels += 1
        elif character.isalpha():
            consonants += 1

    return vowels, consonants


text = "Hello World"
print(count_vowels_and_consonants(text))