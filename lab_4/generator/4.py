a = int(input())
b = int(input())
class squares:
  def __iter__(self):
    self.a = a
    return self

  def __next__(self):
    if self.a <= b:
      x = self.a
      self.a += 1
      return x*x
    else:
      raise StopIteration

sq = squares()
myiter = iter(sq)

for x in myiter:
    
      print(x)