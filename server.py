from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
#@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "main":
    app.run(host = "0.0.0.0", port = 8000)