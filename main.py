from flask import Flask, render_template, url_for, request, redirect
from hashlib import sha256
from handle_data import *


class User:
    def __init__(self, fullname, username, password) -> None:
        self.fullname = fullname
        self.username = username
        self.password = password

    def get_fullname(self) -> str:
        return self.fullname
    
    def get_username(self) -> str:
        return self.username
    
    def get_password(self) -> str:
        return self.password
    
    def set_fullname(self, param) -> str:
        self.fullname = param
    
    def set_username(self, param) -> str:
        self.username = param
    
    def set_password(self, param) -> str:
        self.password = param


app = Flask(__name__)
user1 = User("None", "None", "None")



@app.route("/")  # Main page
@app.route("/home")
def index():
    user1.set_fullname("None")
    user1.set_username("None")
    user1.set_password("None")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])  # Login Page
def login():
    if request.method == "POST":
        username = get_login_data()[0]
        password = get_login_data()[1]
        if sign_in(username, password):
            user1.set_username(username)
            user1.set_password(password)
            return redirect(url_for("dashboard"))
        else:
            return f"Credentials non-existent: {username}, {password}"
        
    return render_template("login.html")


@app.route("/create-account", methods=["GET", "POST"])  # Page for creating an account
def create_account():
    if request.method == "POST":
        fullname = get_register_data()[0]
        username = get_register_data()[1]
        password = get_register_data()[2]
        if not createaccount(fullname, username, password):
            user1.set_fullname(fullname)
            user1.set_username(username)
            return redirect(url_for("dashboard"))
    return render_template("create_account.html")


@app.route("/dashboard")  # Page for displaying a dashboard
def dashboard():
    return render_template("dashboard.html")


@app.route("/email")  # Page for writing an email
def email():
    return render_template("email.html")


@app.route("/account_info")  # PAge to see the account info
def account_info():
    return render_template("account_info.html", fullname=user1.get_fullname(), username=user1.get_username())


def get_login_data():  
    username = request.form["username"]
    password = request.form["password"]
    return username, password


def get_register_data():
    fullname = request.form["fullname"]
    username = request.form["username"]
    password = request.form["password"]
    return fullname, username, password


if __name__ == '__main__':  # Run the code from this file
    app.run(debug=True) # Debug makes sure to re-run the server whenever the code has been changed
