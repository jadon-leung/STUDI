from flask import Flask, render_template, request, jsonify


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

@app.route('/getdata', method = ['GET'])
def get_data():
    return "Data fetched successfully   "

@app.route('/getjson')
def get_json():
    return jsonify({'key': 'value'})

@app.route('/', methods=['POST'])
def handle_data():
    class_type = request.form['classes']
    location = request.form['locations']
    return render_template('/study.html#', c = class_type, location = location )

if __name__ == "__main__":
    #app.run(host = "0.0.0.0", port = 5500, debug = True)
    app.run(debug = True)
