def is_palindrome(text: str):
    cleaned = text.replace(" ", "").lower()

    return cleaned == cleaned[::-1]

print(is_palindrome("hello"))
print(is_palindrome("raceCar"))