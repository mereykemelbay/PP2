import re
txt = input()
string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt).lower() 
print(string)