def judge_age(age):
    if age < 0:
        return "不正な年齢です"
    elif age < 20:
        return "未成年"
    else:
        return "成人"
    
while True:
    age = int(input("年齢を入力（-1で終了）："))

    if age == -1:
        print("終了します")
        break

    result = judge_age(age)
    print(result)
    