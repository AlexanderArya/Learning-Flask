from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = requests.get('http://localhost:8081/data')
    return data.json()

@app.route('/send-data', methods=['POST'])
def sendData():
    nama = request.form.get('name')
    print(18, nama)
    return ''
    # responseDariServer = requests.post(
    #     'http://localhost:8081/send-data',
    #     data={"name": nama}
    # )
    # return responseDariServer.json()

if __name__ == '__main__':
    app.run(debug=True, port=8080)