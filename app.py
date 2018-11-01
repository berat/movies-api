from flask import Flask, render_template, json, request
import requests

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        text1 = request.form["ara"]
        url = 'http://www.omdbapi.com/?apikey=270f8198&t='+text1
        url = requests.get(url)
        return render_template("index.html", movies=json.loads(url.text))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)