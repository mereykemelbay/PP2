x = input()

l = sum([1 for i in x if i.islower()])
u = sum([1 for j in x if j.isupper()])


print("lower", l)
print("upper", u)