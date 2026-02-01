# "sample.txt"に書き込む

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("こんにちは、Python!\n")
    f.write("ファイル操作のテストです。\n")

print("書き込み完了")

