from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/display")
def display():
    return render_template("display.html")

if __name__ == "__main__":
    app.run(debug=True)