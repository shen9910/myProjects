from flask import Flask, render_template, request
import requests, json


app = Flask(__name__, template_folder='./views')

access_token = "fced0ebd4e9c14176a9dd8df70b35b9c"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods = ["POST"])
def get_value():
    base = request.form.get("base")
    goal = request.form.get("rate")
    amount = int(request.form.get("amount"))

    url = "http://data.fixer.io/latest?access_key={}&{}&{}".format(access_token, base, goal)


    res = requests.get(url)
    
    if res.status_code != 200:
        return "ERROR: API request unsuccesful."
      

    data = res.json()
    rate = data["rates"][goal]

    return "Your {} {}s is currently {} {}s".format(str(amount), base, str(amount*rate), goal)



if __name__ == "__main__":
    app.run(debug=True)



    