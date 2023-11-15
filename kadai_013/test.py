# 関数を使いこなそう

# 関数の定義
def calc_tax(price: int, tax: int):
  return price + (price * tax / 100)

# 設定値
price = 1500
tax = 10

# 出力
result = int(calc_tax(price, tax))
print(f"{result}円")
