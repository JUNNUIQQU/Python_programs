def is_palindrome_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return text == reversed_text


text = "madam"
print(is_palindrome_string(text))