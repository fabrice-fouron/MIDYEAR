from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<center><h1>Hello world</h1></center>"


@app.route("/login")
def login():
    return


@app.route("/create_account")
def create_account():
    return


@app.route("/dashboard")
def dashboard():
    return


if __name__ == '__main__':
    app.run(debug=True)
