from flask import Flask, request, redirect, render_template_string
import mysql.connector
import time

app = Flask(__name__)

def connect_db():
    while True:
        try:
            return mysql.connector.connect(
                host='mysql-container',
                user='root',
                password='Raj2002#',
                database='users_db'
            )
        except:
            print("Waiting for MySQL...")
            time.sleep(2)

@app.route('/')
def form():
    return render_template_string('''
        <h2>Register</h2>
        <form method="post" action="/register">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <button type="submit">Submit</button>
        </form>
        <br>
        <a href="/users">View Users</a>
    ''')

@app.route('/register', methods=['POST'])
def register():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                   (request.form['username'], request.form['password']))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/users')
def users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template_string('<h2>Registered Users</h2><ul>' +
                                  ''.join(f'<li>{u[0]}</li>' for u in users) +
                                  '</ul><a href="/">Go Back</a>')

if __name__ == '__main__':
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        )
    ''')
    conn.commit()
    conn.close()
    app.run(host='0.0.0.0', port=5000)
