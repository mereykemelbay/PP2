s = input()

p = "".join(reversed(s))
if s==p:
    print("palindrome")
else:
    print("not palindrome")