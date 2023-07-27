def is_palindrome(word):
    palindrome = ''
    index = len(word)
    while index > 0:
        index -= 1
        palindrome += word[index]
    # if word.lower() == palindrome.lower():
    #     return True
    # else:
    #     return False
    return word.lower() == palindrome.lower()
