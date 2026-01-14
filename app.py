from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)



@app.route('/')
def home():
    return "Flask is running with MySQL!"

@app.route('/users')
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")  # replace 'users' with your table
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
