from flask import Flask, render_template, request, jsonify, redirect, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homes.html')

@app.route('/about.html', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/study')
def study():
    return render_template('study.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def login():
    return render_template('regiter.html')

@app.route('/home')
def login():
    return render_template('home.html')

if __name__ == "__main__":
    #app.run(host = "0.0.0.0", port = 5500, debug = True)
    app.run(debug = True)
