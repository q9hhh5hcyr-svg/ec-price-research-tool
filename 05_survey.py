# 成果物⑤：簡易アンケート（入力 → 集計 → 表示）
# file: 05_survey.py

def ask_choice(prompt: str, choices: list[str]) -> str:
    choices_str = "/".join(choices)
    while True:
        s = input(f"{prompt} ({choices_str}): ").strip()
        if s in choices:
            return s
        print("選択肢から入力してください。")


def main():
    print("簡易アンケート（3人分）")

    results = {"はい": 0, "いいえ": 0}
    names: list[str] = []

    for i in range(3):
        name = input(f"{i+1}人目の名前: ").strip() or f"匿名{i+1}"
        ans = ask_choice("Python学習を継続できそうですか？", ["はい", "いいえ"])
        names.append(name)
        results[ans] += 1

    print("\n--- 集計 ---")
    for k, v in results.items():
        print(f"{k}: {v}")

    print("\n--- 回答者 ---")
    print(", ".join(names))


if __name__ == "__main__":
    main()
