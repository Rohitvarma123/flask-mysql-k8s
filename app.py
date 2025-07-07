from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host="mysql-service",
            user="admin",
            password="admin123",
            database="testdb"
        )
        return "✅ Connected to MySQL!"
    except:
        return "❌ Failed to connect to MySQL"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
