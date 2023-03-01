import re
txt = input()
x = re.search("a{1}.*b$", txt)

print(x.span())