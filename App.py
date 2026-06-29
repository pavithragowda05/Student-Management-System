from flask import Flask, render_template , request

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

@app.route("/save", methods=["POST"])
def save():
    usn = request.form["usn"]
    name = request.form["name"]
    year = request.form["year"]
    # Write the student data to a file or database
    with open("studentdata.txt", "a") as file:
        file.write(f"{usn},{name},{year}\n")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)