from getpass import getpass  # hides password input (optional)

def check_password_strength(password):
    # Rules
    length_rule = len(password) >= 8
    upper_rule = any(ch.isupper() for ch in password)
    lower_rule = any(ch.islower() for ch in password)
    digit_rule = any(ch.isdigit() for ch in password)
    special_rule = any(ch in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for ch in password)

    # Track missing criteria
    missing = []
    if not length_rule:
        missing.append("❌ At least 8 characters")
    if not upper_rule:
        missing.append("❌ At least 1 uppercase letter")
    if not lower_rule:
        missing.append("❌ At least 1 lowercase letter")
    if not digit_rule:
        missing.append("❌ At least 1 digit")
    if not special_rule:
        missing.append("❌ At least 1 special character (!@#$ etc.)")

    # Strength logic
    if all([length_rule, upper_rule, lower_rule, digit_rule, special_rule]):
        strength = "Strong ✅"
    elif length_rule and (upper_rule or lower_rule) and (digit_rule or special_rule):
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❗"

    return strength, missing


if __name__ == "__main__":

    pwd = input("Enter a password to check: ")
    strength, missing_criteria = check_password_strength(pwd)

    print(f"\nPassword Strength: {strength}")
    if missing_criteria:
        print("Improve by fixing:")
        for item in missing_criteria:
            print("  -", item)
    else:
        print("Great! Your password meets all the criteria.")
