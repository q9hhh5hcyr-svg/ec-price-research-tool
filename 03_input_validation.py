# 03_input_validation.py
# 汎用入力チェック（空欄・文字数）

def validate_input(text, min_length=1, max_length=20):
    if not text:
        return "入力が空です"

    if len(text) < min_length:
        return f"{min_length}文字以上で入力してください"

    if len(text) > max_length:
        return f"{max_length}文字以内で入力してください"

    return "OK"


user_input = input("文字を入力してください: ")
result = validate_input(user_input, min_length=3, max_length=10)

print(result)
