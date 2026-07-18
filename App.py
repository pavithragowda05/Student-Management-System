from flask import Flask, redirect, render_template , request

app = Flask(__name__)
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anku123",
    database="StudentDB"
)
cursor = db.cursor()
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/add")
def add():
    
    return render_template("add.html")

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/display")
def display():
    sql = "SELECT * FROM Student"
    cursor.execute(sql)
    students = cursor.fetchall()
    return render_template("display.html", students=students)

@app.route("/save", methods=["POST"])
def save():
    usn = request.form["usn"]
    name = request.form["name"]
    year = request.form["year"]
    cgpa =request.form["cgpa"]
    # Write the student data to a file or database
    # with open("studentdata.txt", "a") as file:
    #     file.write(f"{usn},{name},{year}\n")
    # return render_template("index.html")

    #writing data into database

    sql="INSERT INTO Student(usn ,name ,year ,cgpa) VALUES(%s ,%s ,%s , %s)"
    values=(usn ,name ,year ,cgpa)
    cursor.execute(sql,values)
    db.commit()
    return render_template("index.html")

@app.route("/updatedata",methods=["POST"])
def updatedata():
    usn=request.form["usn"]
    cgpa=request.form["cgpa"]
    sql="UPDATE Student set cgpa=%s where usn=%s"
    values=(cgpa,usn)
    cursor.execute(sql,values)
    db.commit()
    return render_template("index.html")

@app.route("/deletedata",methods=["POST"])
def deletedata():
    usn=request.form["usn"]
    sql="DELETE FROM Student where usn=%s"
    values=(usn,)
    cursor.execute(sql,values)
    db.commit()
    return render_template("index.html")
@app.route("/search")
def searchpage():
    return render_template("search.html")

@app.route("/searchdata",methods=["GET","POST"])
def search():
    usn=request.form["usn"]
    sql="SELECT * FROM Student WHERE usn = %s"
    values=(usn,)
    cursor.execute(sql,values)
    student = cursor.fetchone()
    return render_template("search.html", student=student)

@app.route("/adminlogin")
def adminlogin():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":

        return render_template("index.html")

    else:

        return "Invalid Username or Password"
    
@app.route("/logout")
def logout():
    return redirect("/")    
if __name__ == "__main__":
    app.run(debug=True)