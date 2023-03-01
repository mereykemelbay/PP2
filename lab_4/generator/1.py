N = int(input())
class numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x*x
    else:
      raise StopIteration

myclass = numbers()
myiter = iter(myclass)

for x in myiter:
  print(x)