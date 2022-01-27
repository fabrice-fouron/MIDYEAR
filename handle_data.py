import json
from hashlib import sha256


def to_hash(arg):
    """Turn the info entered into a hash code"""
    hashed = sha256()  # Hashing algorithm
    arg = bytearray(arg, encoding="utf-8")  # Change argument into binary
    hashed.update(arg)  # Input the binary argument in to the hashing algorithm
    return hashed.hexdigest()  # Return the hash code


def createaccount(fullname, username, password):
    """A user is creating an account"""
    with open("data.json", "r") as f:
        temp = json.load(f)

    actual_name = fullname  # User enters his name

    username = to_hash(username)
    password = to_hash(password)

    try:
        ind = [j["username"] for j in temp["users"]].index(username) # index method raises ValueError if username is not found
    except ValueError:  # Add new information if the user is not found
        temp["users"].append({
            "id": len(temp["users"]) + 1,
            "name": actual_name,
            "username": username,
            "password": password
        })

        with open("data.json", "w") as f:
            json.dump(temp, f, indent=4, separators=(",", ": "))
        return False



def sign_in(username, password):
    """The user is signing in into his/her account"""
    with open("data.json", "r") as f:
        temp = json.load(f)

    try:
        ind = [j["username"] for j in temp["users"]].index(to_hash(username)) # index method raises ValueError if username is not found
    except ValueError:  # Return False if value not found
        return False
    if to_hash(password) == [j["password"] for j in temp["users"]][ind]:
        return True
    else:
        return False
