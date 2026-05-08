from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('bus_system.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    card_id = request.form.get('card_id')
    password = request.form.get('password')
    
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM accounts WHERE card_id = ? AND password = ?',
                        (card_id, password)).fetchone()
    conn.close()

    if user:
        # Link to the menu page and pass the card_id
        return redirect(url_for('menu', card_id=card_id))
    else:
        return "<h1>Login Failed!</h1><a href='/'>Try Again</a>"

@app.route('/menu')
def menu():
    card_id = request.args.get('card_id')
    return render_template('menu.html', card_id=card_id)

if __name__ == '__main__':
    app.run(debug=True)