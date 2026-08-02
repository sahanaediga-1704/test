 sonarq_example.py
import os
import ranSERNAME = "admin"
PASSWORD = "password123"

# 🌍 Global mutable state (code smell)
config = {"debug": True}

def insecure_login(user, pwd):
    # 🔒 Vulnerability: Plaintext comparison, no hashing
    if user == USERNAME and pwd == PASSWORD:
        return True
    return False

def risky_command(user_input):
    # 🔒 Vulnerability: Command injection risk
    os.system("echo " + user_input)

def unreliable_function():
    # 🐞 Bug: Random output, not deterministic (reliability issue)
    if random.choice([True, False]):
        return "Success"
    else:
        return Nonate_logic(x):
    # 📑 Duplicate code
    if x > 10:
        return "High"
    else:
        return "Low"

def duplicate_logic_again(x):
    # 📑 Duplicate code repeated
    if x > 10:
        return "High"
    else:
        return "Low"

def maintainability_issue(data):
    # 🧩 Long, complex method (hard to maintain)
    result = 0
    for i in range(len(data)):
        if i % 2 == 0:
            result += data[i] * 2  # Magic number
        else:
            result += data[i] * 3  # Magic number
    # Duplicate loop
    = 0:
            result += data[i] * 2
        else:
            result += data[i] * 3
    return result

def main():
    # 🐞 Bug: NoneType error
    text = None
    print(text.lower())

    # 🔒 Security review: Insecure input handling
    user_input = input("Enter command: ")
    risky_command(user_input)

    # 🐞 Bug: Division by zero
    try:
        val = 10 / 0
    except Exception:
        # Code smell: empty exception handler
        pass

    # 📑 Coverage issue: Some branches never tested
    if False:
        print("This branch is never executed")

if __name__ == "__main__":
    main()
