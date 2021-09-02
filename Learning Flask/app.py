import datetime

from flask import Flask, render_template, request,session
from flask_session import Session

app = Flask(__name__, template_folder='./views')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    headline = "Hello MidEarth!"
    return render_template("index.html", headline=headline)

@app.route("/inheritance")
def inheritance():
    return render_template("first.html")

@app.route("/inheritance/second")
def inheritance_second():
    return render_template("second.html")

@app.route("/forms")
def form():
    return render_template("forms.html")

@app.route("/form_hello", methods=['GET','POST'])
def form_hello():
    if request.method == "GET":
        return "Submit the form"
    name = request.form.get('name')
    return "Hello, " + name 


@app.route("/sessions", methods=['GET', 'POST'])
def session_test():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == 'POST':
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("session.html", notes = session["notes"])

@app.route("/isitnewyear")
def isitnewyear():
    now = datetime.datetime.now()
    newyear = (now.month==1) and (now.day==1)
    return render_template("newyear.html", newyear=newyear)


@app.route("/loops")
def loops():
    names = ["Slava", "Alice", "Linda"]
    return render_template("loops.html", names=names)
    

@app.route("/<name>")
def hello(name):
    return render_template("index.html", headline= "Hello " + name)

if __name__ == "__main__":
    app.run(debug=True)