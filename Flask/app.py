from flask import Flask, render_template, request, session, url_for, redirect
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniadalahsecretkeyku"
# ID USER
id_unik = 0

def saveData(data):
    with open("Flask/data.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

@app.route("/", methods=["POST", "GET"])
def index():
    if session.get('userMasuk'):
        return redirect(url_for('landingPage'))
    else:
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            if username == "admin" and password == "1234":
                session["userMasuk"] = username
                return redirect(url_for('landingPage'))
            else:
                return redirect(url_for('index'))
        return render_template("index.html")


@app.route("/insertData", methods=["POST", "GET"])
def insertData():
    global id_unik
    if session.get('userMasuk'):
        if request.method == "POST":
            id_unik += 1
            id_user = request.form.get('id_user')
            username = request.form.get('username')
            nominal = int(request.form.get('nominal'))
            diamond = int(nominal / 1000)

            data_list = session.get('data_list', [])
            data_list.append({'id_user': id_user, 'username': username, 'nominal': nominal, 'diamond': diamond, 'id': id_unik})
            session['data_list'] = data_list

            saveData(data_list)
            
            return redirect(url_for('landingPage'))
        return render_template("insertData.html")
    else:
        return redirect(url_for('index'))
    
@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        # Ambil data dari form
        id_entry = request.form.get('id_entry') 
        new_id_user = request.form.get('new_id_user')
        new_username = request.form.get('new_username')
        new_nominal = int(request.form.get('new_nominal'))
        
        if id_entry:
            id_entry = int(id_entry)
            data_entry = next((item for item in session['data_list'] if item['id'] == id_entry), None)
            if data_entry:
                # Update data yang ditemukan
                data_entry['id_user'] = new_id_user
                data_entry['username'] = new_username
                data_entry['nominal'] = new_nominal
                data_entry['diamond'] = int(new_nominal / 1000)
                # Simpan kembali data_list yang telah diperbarui ke dalam session
                session['data_list'] = session['data_list']
                
                saveData(session['data_list'])    

                # Redirect kembali ke landingPage setelah update
                return redirect(url_for('landingPage'))
            else:
                return "Data dengan ID {} tidak ditemukan.".format(id_entry)    
    else:
        id_entry = request.args.get('id_entry')  # Ambil ID unik dari query string
        if id_entry:
            id_entry = int(id_entry)
            data_entry = next((item for item in session['data_list'] if item['id'] == id_entry), None)
            if data_entry:
                return render_template('update.html', data_entry=data_entry)
        return "ID unik tidak ditemukan dalam query string."

            
        

# Tabel
@app.route("/landingPage", methods=["POST", "GET"])
def landingPage():    
    nilai = session.get('userMasuk')
    data_list = session.get('data_list', [])
    
    return render_template("landingPage.html", nilai=nilai, data_list=data_list )

# Fungsi delete
@app.route("/delete/<string:id_user>")
def delete(id_user):
    if not session.get('userMasuk'):
        return redirect(url_for('index'))
    data_list = session.get('data_list', [])    
    for item in data_list:
        if item["id_user"] == id_user:
            data_list.remove(item)
            break
    session['data_list'] = data_list    
    saveData(data_list)
    return redirect(url_for('landingPage'))


@app.route("/logout")
def logout():
    if session.get('userMasuk') is None:
        return redirect(url_for('index'))
    global id_unik
    id_unik = 0  
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
