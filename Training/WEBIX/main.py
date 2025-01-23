from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/send-data', methods=['POST'])
# def sendData():
#     print(request.form)
#     return ''

# @app.route('/get-data', methods=['GET'])
# def getData():
#     os.environ['NO_PROXY'] = 'localhost'
#     data = requests.get('http://localhost:8081/data', headers={})
#     return data.json()

app.run(host="localhost",port=8080, debug=True)