from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/study')
def study():
    return render_template('study.html')

if __name__ == "__main__":
    #app.run(host = "0.0.0.0", port = 5500, debug = True)
    app.run()
