import math
x=int(input())
y=int(input())

a = 2 * math.tan((180/x) * (math.pi/180))
b = y / a
A = x*y*b * (1/2)
print(A)
