import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks=[]
students_finished = set()

@app.route("/") 
def show_join():
    return render_template("join.html", page_title = "Index")

@app.route("/join")
def join():
    user = request.args["user"].lower()
    return redirect("/app/" + user)
    
@app.route("/app/<user>")
def show_app(user):
    if user == "teacher":
        return render_template("teacher.html", students_finished=students_finished)
    else:
        return render_template("student.html", tasks=tasks, user=user)

@app.route("/new-task", methods = ["POST"])
def show_task():
    if len(tasks) >= 1:
        del tasks[0]
    task = request.form["task"]
    tasks.append(task)
    return redirect("/app/teacher")

@app.route("/done")
def student_done():
    user = request.args["user"].lower()
    students_finished.add(user)
    
    return redirect("/app/" + user)
    
if __name__ == '__main__':
    app.run(host = os.environ.get("IP"),
            port =  os.environ.get("PORT"),
            debug = True)