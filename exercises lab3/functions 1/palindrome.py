def palindrome(s):
    t = s[::-1]
    if t == s:
        return True
    return False

s = input()
print(palindrome(s))