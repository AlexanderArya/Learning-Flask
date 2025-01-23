from flask import Flask, request

app = Flask(__name__)

@app.route('/data')
def data():
    return [{
        'id': 101,
        'name': 'Mario',
        'umur': 24,
        'alamat': 'Tangerang'
    }]

@app.route('/send-data', methods=['POST'])
def sendData():
    print(request.form)
    # TODO: memasukan data ke database
    
    status = True
    return {
        "status": status,
        "message": "Insert data berhasil"
    }


if __name__ == '__main__':
    app.run(host="localhost",debug=True, port=8081)