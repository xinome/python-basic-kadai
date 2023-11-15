# クラスを使いこなそう

# クラスを定義する
class Human:
  def __init__(self):
    self.name = ""
    self.age = 0

  def printinfo(self, name, age):
    self.name = name
    self.age = age
    print(self.name)
    print(self.age)

# インスタンス化する
instance = Human()

instance.printinfo("侍太郎", 25)
