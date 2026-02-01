def introduce(name, age):
    print("名前：", name)
    print("年齢：", age)

introduce("Mash", 34)

def add(a, b):
    return a + b

total = add(10, 20)
print("合計:", total)


def judge_age(age):
    if age < 0:
        return "不正な年齢です"
    elif age < 20:
        return "未成年"
    else:
        return "成人"
    
result = judge_age(34)
print(result)

result = judge_age(15)
print(result)

result = judge_age(-1)
print(result)