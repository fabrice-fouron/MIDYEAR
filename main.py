from flask import Flask, render_template, url_for
from hashlib import sha256

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/create_account")
def create_account():
    return render_template("create_account")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)
