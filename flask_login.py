from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return redirect('/loginpage')

@app.route('/login')
def server_login():
    return render_template("login.html")

@app.route('/login_process', methods = ["POST", "GET"])
def get_form_data():
    return jsonify({"username": request.form.get("username"), "password": request.form.get("password")})

if __name__ == '__main__':
    app.run(debug=True)