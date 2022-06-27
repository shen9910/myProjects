from flask import Flask, render_template, request, jsonify
import requests, json


app = Flask(__name__, template_folder='./views')

access_token = "fced0ebd4e9c14176a9dd8df70b35b9c"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods = ["POST"])
def get_value():
    base = "USD"
    currency = request.form.get("currency")

    url = "http://data.fixer.io/latest?access_key={}&{}&{}".format(access_token, base, currency)


    res = requests.get(url)
    
    if res.status_code != 200:
        return jsonify({"success": False})
      

    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})
    
    return jsonify({"success": True, "rate": data["rates"][currency]})




if __name__ == "__main__":
    app.run(debug=True)



    