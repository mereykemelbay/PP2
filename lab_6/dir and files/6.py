import os

for i in range(26):
    n = chr(i + 65) + ".txt"
    print(n)
    file = open(n, 'w')
    file.close()