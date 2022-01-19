from flask import Flask, render_template, url_for, flash, request, redirect
from hashlib import sha256
from handle_data import *


app = Flask(__name__)
app.secret_key = b"bruh, look at this dude"


@app.route("/")  # Main page
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])  # Login Page
def login():
    flash("Hello world")
    return render_template("login.html")


@app.route("/create-account")  # Page for creating an account
def create_account():
    return render_template("create_account.html")


@app.route("/dashboard")  # Page for displaying a dashboard
def dashboard():
    return render_template("dashboard.html")


def get_login_data():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # if username == "" or password == "":
        #     flash("At least one of the fields is empty")
        return username, password


def get_register_data():
    if request.method == "POST":
        fullname = request.form["fullname"]
        username = request.form["username"]
        password = request.form["password"]
        return fullname, username, password


if __name__ == '__main__':  # Run the code from this file
    app.run(debug=True)
