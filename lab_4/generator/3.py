N = int(input())
class divisible:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

m = divisible()
myiter = iter(m)

for x in myiter:
    if(x % 3 == 0) and (x % 4 == 0):
      print(x)