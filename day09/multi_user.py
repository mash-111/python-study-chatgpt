# 複数ユーザーをリストで管理

users = [
    {"name": "Mash", "age": 34},
    {"name": "Taro", "age": 15},
    {"name": "Hanako", "age": 28}
]

#保存
with open("users.txt", "w", encoding="utf-8") as f:
    for user in users:
        f.write(f'{user["name"]},{user["age"]}\n')

print("ユーザー情報を書き込みました。")

#読み込み
loaded_users = []
with open("users.txt", "r", encoding="utf-8") as f:
    print(f)
    for line in f:
        line = line.strip()
        if line: #空行を除外
            name, age = line.split(",")
            loaded_users.append({"name": name, "age": int(age)})

print("読み込んだユーザー情報:")
for user in loaded_users:
    print(f'{user["name"]}さん:{user["age"]}歳')

