# 成果物④：偶数・奇数判定＋条件分岐ツール
# file: 04_even_odd_tool.py

def parse_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("数字で入力してください。")


def main():
    n = parse_int("整数を入力してください: ")

    if n % 2 == 0:
        print(f"{n} は偶数です。")
    else:
        print(f"{n} は奇数です。")

    # 条件分岐例（ついでに実務っぽく）
    if n >= 100:
        print("→ 100以上なので“大きめの値”として扱います")
    elif n >= 0:
        print("→ 0以上100未満です")
    else:
        print("→ 負の数です")


if __name__ == "__main__":
    main()
