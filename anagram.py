def is_anagram(string1, string2):

    if set(string1.lower()) - set(string2.lower()) == set():
        print(f"Yes, '{string1}' and '{string2}' are anagrams.")
    else:
        print("No they are not anagrams.")


word1 = input("Word 1: ")
word2 = input("Word 2: ")
is_anagram(word1, word2)
