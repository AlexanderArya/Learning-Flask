from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti 'your_secret_key' dengan kunci rahasia yang benar

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/registers", methods=["POST"])
def register():
    pass

@app.route("/login", methods=["POST"])
def login():
    username_db = "admin"
    password_db = "123"

    username = request.form["username"]
    password = request.form["password"]

    if username_db == username and password_db == password:
        session['logged_in'] = True
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html", error="Username atau password salah")

@app.route("/dashboard")
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template("dashboard-visualisasi.html")

if __name__ == "__main__":
    app.run(debug=True)
