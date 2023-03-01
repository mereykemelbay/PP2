N = int(input())
class generator:
  def __iter__(self):
    self.a = N
    return self

  def __next__(self):
    if self.a >= 0:
      x = self.a
      self.a -= 1
      return x
    else:
      raise StopIteration

jq = generator()
myiter = iter(jq)

for x in myiter:
  print(x)