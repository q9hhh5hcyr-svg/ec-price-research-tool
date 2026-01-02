def is_valid_email(email: str) -> bool:
    email = email.strip()

    if "@" not in email:
        return False

    local, domain = email.split("@", 1)

    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if email.count("@") != 1:
        return False

    return True


def main():
    email = input("メールアドレスを入力してください: ").strip()
    if is_valid_email(email):
        print("OK: 形式としては問題なさそうです")
    else:
        print("NG: メールアドレスの形式が不正です")


if __name__ == "__main__":
    main()
