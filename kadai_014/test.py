# 変数スコープを正しく使おう

price1 = 100
price2 = 200

def total():
    tax = 1.1
    return price1 + price2

print (total() * tax)

