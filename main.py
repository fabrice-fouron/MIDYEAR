from flask import Flask, render_template, url_for
from hashlib import sha256
from handle_data import *


app = Flask(__name__)


@app.route("/")  # Main page
def index():
    return render_template("index.html")


@app.route("/login")  # Login Page
def login():
    return render_template("login.html")


@app.route("/create-account")  # Page for creating an account
def create_account():
    return render_template("create_account.html")


@app.route("/dashboard")  # Page for displaying a dashboard
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':  # Run the code from this file
    app.run(debug=True)
