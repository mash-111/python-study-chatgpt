score = int(input("点数を入力してください："))

if score < 0 or score > 100:
    print("エラー：０〜１００の範囲で入力してください")
elif score >= 90:
    print("評価：A")
elif score >= 80:
    print("評価：B")
elif score >= 70:
    print("評価：C")
else:
    print("評価：D")
