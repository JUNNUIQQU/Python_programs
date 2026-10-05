def reverse_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


text = "Hello"
print(reverse_string(text))