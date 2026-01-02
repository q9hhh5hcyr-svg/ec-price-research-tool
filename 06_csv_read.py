# 成果物⑥：CSV読み込み＋集計（Excel代替）
# file: 06_csv_sum_avg.py
# 入力CSV例（scores.csv）: name,score
# A,10
# B,20
# C,30

import csv

INPUT_CSV = "scores.csv"


def main():
    total = 0.0
    count = 0

    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                score = float(row["score"])
            except (KeyError, ValueError):
                print("スキップ（scoreが不正）:", row)
                continue

            total += score
            count += 1

    if count == 0:
        print("有効データがありません。")
        return

    avg = total / count
    print(f"件数: {count}")
    print(f"合計: {total}")
    print(f"平均: {avg}")


if __name__ == "__main__":
    main()
