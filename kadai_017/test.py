# 学習したことを組み合わせてコードを書こう

# クラスを定義する
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}は大人です")
    else:
      print(f"{self.name}は大人ではありません")

# インスタンス化 + リスト化
members = [
    Human("侍太郎", 36),
    Human("侍一郎", 13),
    Human("侍二郎", 29),
    Human("侍三郎", 25),
    Human("侍四郎", 12),
]

for member in members:
  member.check_adult()
