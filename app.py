from flask import Flask, jsonify
from config import Config
from calculator import add
from database import get_db_connection

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    db_status = get_db_connection()
    return jsonify({"message": "Welcome to DevSecOps App", "db": db_status})

@app.route('/add/<int:a>/<int:b>')
def addition(a, b):
    result = add(a, b)
    return jsonify({"operation": "addition", "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)