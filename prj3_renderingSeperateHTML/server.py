from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/home")
def home():
    return "home page not implemented yet"

@app.route("/about")
def about():
    return "about page not implemented"