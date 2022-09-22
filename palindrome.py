def is_pal(input1):
    phrase = input1.lower()

    if phrase == phrase[::-1]:
        return f"{phrase} reversed is {phrase[::-1]}"

    else:
        return "No"


word = input("Enter a word: ")
print(f"Is '{word}' a palindrome? {is_pal(word)}")
