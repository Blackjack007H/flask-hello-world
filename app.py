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

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://blackjack007h_user:u1uVis0w9op35qYYRVBSm8GlVt3UpkFc@dpg-cj3sj0h8g3n1jkk4pc4g-a/blackjack007h")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Table Basketball was successfully created!"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgres://blackjack007h_user:u1uVis0w9op35qYYRVBSm8GlVt3UpkFc@dpg-cj3sj0h8g3n1jkk4pc4g-a/blackjack007h")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    """)
    conn.commit()
    conn.close()
    return "Basketball Table successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://blackjack007h_user:u1uVis0w9op35qYYRVBSm8GlVt3UpkFc@dpg-cj3sj0h8g3n1jkk4pc4g-a/blackjack007h") 
    connection string
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')  
    records = cur.fetchall()
    conn.close()
    response_string = ""    
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgres://blackjack007h_user:u1uVis0w9op35qYYRVBSm8GlVt3UpkFc@dpg-cj3sj0h8g3n1jkk4pc4g-a/blackjack007h")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Dropped!'

