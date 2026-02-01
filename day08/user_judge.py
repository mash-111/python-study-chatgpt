def judge_user(user):
    if user["age"] >= 20:
        return f'{user["name"]}は成人です'
    else:
        return f'{user["name"]}は未成年です'
    
user1 = {"name": "Mash", "age": 34}
user2 = {"name": "Taro", "age": 15}

print(judge_user(user1))
print(judge_user(user2))