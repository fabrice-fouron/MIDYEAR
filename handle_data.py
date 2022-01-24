import json
from hashlib import sha256


def to_hash(arg):
    """Turn the info entered into a hash code"""
    hashed = sha256()  # Hashing algorithm
    arg = bytearray(arg, encoding="utf-8")  # Change argument into binary
    hashed.update(arg)  # Input the binary argument in to the hashing algorithm
    return hashed.hexdigest()  # Return the hash code


def createaccount():
    """A user is creating an account"""
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
    """The user is signing in into his/her account"""
    with open("data.json", "r") as f:
        temp = json.load(f)

    var = find_correspondence("users", "username")
    if to_hash(password) == [j["password"] for j in temp["users"]][var]:
        return True
    else:
        return False


def find_correspondence(obj, param):
    with open("data.json", "r") as f:
        temp = json.load(f)

    try:
        ind = [j[obj] for j in temp["users"]].index(to_hash(param)) # index method raises ValueError if value is not found
    except ValueError:  # Return False if value not found
        return False
    return ind


def update_account_status():
    """Updates the account of a user"""
    pass
