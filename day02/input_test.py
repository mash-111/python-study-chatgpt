# name = input("名前を入力してください：")
# age = int(input("年齢を入力してください："))

# print(name)
# print(age)
# print(type(name))
# print(type(age))

import math

age2 = float(input("年齢（小数OK）を入力してください："))

print("切り捨て", math.floor(age2))
print("切り上げ", math.ceil(age2))
print("四捨五入", round(age2))