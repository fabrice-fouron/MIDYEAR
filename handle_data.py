import json
from hashlib import sha256


def to_hash(arg):
    hashed = sha256()  # Hashing algorithm
    arg = bytearray(arg, encoding="utf-8")  # Change argument into binary
    hashed.update(arg)  # Input the binary argument in to the hashing algorithm
    return hashed.hexdigest()  # Return the hash code


def create_account():
    with open("data.json", "r") as f:
        temp = json.load(f)

    actual_name = input("Enter your full name: ")  # User enters his name

    username = to_hash(input("Enter your username: "))
    password = to_hash(input("Enter your password: "))

    temp["users"].append({
        "id": len(temp["users"]) + 1,
        "name": actual_name,
        "username": username,
        "password": password,
        "sent": 0
    })

    with open("data.json", "w") as f:
        json.dump(temp, f, indent=4, separators=(",", ": "))


def sign_in(username, password):
    with open("data.json", "r") as f:
        temp = json.load(f)

    if to_hash(username) in [j["username"] for j in temp["users"]]:
        if to_hash(password) in [j["password"] for j in temp["users"]]:
            return True
        else:
            return False
    else:
        return

