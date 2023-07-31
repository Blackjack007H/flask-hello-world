from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def db_testing():
    conn = psycopg2.connect("postgres://blackjack007h_user:u1uVis0w9op35qYYRVBSm8GlVt3UpkFc@dpg-cj3sj0h8g3n1jkk4pc4g-a/blackjack007h")
    conn.close()
    return "Database connection works properly!"