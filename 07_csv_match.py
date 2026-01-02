# 成果物⑦：CSVを使った複数ユーザー照合
# file: 07_csv_user_match.py
# users.csv 例: user_id,name
# 1,Alice
# 2,Bob
# 3,Charlie
# targets.csv 例: user_id
# 2
# 4
# 1

import csv

USERS_CSV = "users.csv"
TARGETS_CSV = "targets.csv"


def load_users(path: str) -> dict[str, str]:
    users = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = (row.get("user_id") or "").strip()
            name = (row.get("name") or "").strip()
            if uid and name:
                users[uid] = name
    return users


def load_targets(path: str) -> list[str]:
    targets = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = (row.get("user_id") or "").strip()
            if uid:
                targets.append(uid)
    return targets


def main():
    users = load_users(USERS_CSV)
    targets = load_targets(TARGETS_CSV)

    found = []
    not_found = []

    for uid in targets:
        if uid in users:
            found.append((uid, users[uid]))
        else:
            not_found.append(uid)

    print("--- 一致（存在するユーザー） ---")
    for uid, name in found:
        print(uid, name)

    print("\n--- 不一致（存在しないユーザー） ---")
    for uid in not_found:
        print(uid)


if __name__ == "__main__":
    main()
