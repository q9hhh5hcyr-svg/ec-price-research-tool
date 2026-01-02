# 02_login_limit.py
# 回数制限付き認証ツール（ログイン原型）

CORRECT_PIN = "1234"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    pin = input("暗証番号を入力してください: ")

    if pin == CORRECT_PIN:
        print("認証成功")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"認証失敗。残り試行回数: {remaining}")

else:
    print("試行回数上限に達しました。ロックされました。")
