from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

@app.route("/")
def index():
    api_key = "315ca6b38c7d035939800745"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    dic = data["conversion_rates"]
    return render_template("index.html", dict=dic)

@app.route("/submit", methods=["POST"])
def convert():
    api_key = "315ca6b38c7d035939800745"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    
    code1 = request.form.get('from')
    rate1 = data["conversion_rates"][code1]
    
    code2 = request.form.get('to')
    rate2 = data["conversion_rates"][code2]
       
    const = (rate2/rate1)
    
    am = request.form.get("from-am")
    value = float(am)*const
        
    output = f"{am} {code1} = {value} {code2}"
    return output

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)