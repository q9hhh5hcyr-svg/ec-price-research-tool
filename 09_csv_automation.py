# 成果物⑨：定型作業の自動化（CSV → 集計 → 新CSV出力）
# file: 09_csv_to_report_csv.py
# 入力CSV例（sales.csv）: item,amount
# apple,100
# banana,200
# apple,50

import csv

INPUT_CSV = "sales.csv"
OUTPUT_CSV = "sales_report.csv"


def main():
    sums: dict[str, float] = {}

    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            item = (row.get("item") or "").strip()
            amt_raw = (row.get("amount") or "").strip()

            if not item:
                continue

            try:
                amt = float(amt_raw)
            except ValueError:
                # 不正値はスキップ
                continue

            sums[item] = sums.get(item, 0.0) + amt

    # 出力
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["item", "total_amount"])
        writer.writeheader()
        for item, total in sorted(sums.items()):
            writer.writerow({"item": item, "total_amount": total})

    print("出力しました:", OUTPUT_CSV)


if __name__ == "__main__":
    main()
