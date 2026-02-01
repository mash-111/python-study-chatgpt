import os

FILENAME = "user.txt"

# --- 既存データ読み込み ---
users = []
if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                name, age = line.split(",")
                users.append({"name": name, "age": int(age)})

# --- ユーザー登録ループ ---
while True:
    name = input("名前を入力（exitで終了）:")
    if name.lower() == "exit":
        break
    age_input = input("年齢を入力：")

    try:
        age = int(age_input)
        if age < 0:
            print("年齢は０以上で入力してください")
            continue
    except ValueError:
        print("数字を入力してください")
        continue

    users.append({"name": name, "age": age})

# --- ファイル保存 ---
with open(FILENAME, "w", encoding="utf-8") as f:
    for user in users:
        f.write(f'{user["name"]},{user["age"]}\n')

# --- ユーザー一覧表示 ---
print("\n登録されているユーザー一覧：")
for user in users:
    print(f'{user["name"]}さん：{user["age"]}歳')
    