from flask import Flask, redirect, render_template, request, url_for
import mysql.connector as conn
app = Flask(__name__)

connection = conn.connect(user = 'root', password = 'root123', host='127.0.0.1', db = 'mydatabase')
cursor = connection.cursor()

@app.route('/')
def login():
    return redirect('/login')

@app.route('/login')
def serve_login():
    return render_template("login.html", error='')

@app.route('/login_process', methods = ["POST"])
def get_form_data():
    username = request.form.get("username")
    password = request.form.get("password")
    cursor.execute(f"select * from user where user_id = '{username}' and password_user = '{password}';")
    result = cursor.fetchall()
    print(result)
    
    if len(result) == 1:
        cursor.execute(f'select * from `user` where user_id = "{username}"')
        user_details = cursor.fetchall()
        print(user_details)
        return "Success!"
    else:
        return render_template("login.html", error = "Incorrect username or password")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)