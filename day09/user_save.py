user = {"name": "Mash", "age": 34}

#保存
with open("user.txt", "w", encoding = "utf-8") as f:
    f.write(f'{user["name"]},{user["age"]}\n')

#読み込み
with open("user.txt", "r", encoding = "utf-8") as f:
    line = f.readline().strip()
    name, age = line.split(",")
    age = int(age)

print("読み込んだユーザー情報：", name ,age)