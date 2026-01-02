# 成果物⑧：エラーハンドリング強化（落ちないコード）
# file: 08_safe_input_and_calc.py

def safe_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("数字で入力してください。")


def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


def main():
    a = safe_int("割られる数 a: ")
    b = safe_int("割る数 b: ")

    result = safe_divide(a, b)
    if result is None:
        print("0では割れません（落ちないように処理しました）")
        return

    print("結果:", result)


if __name__ == "__main__":
    main()
