from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Stephen Donlin in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://render_db_52tl_user:qQfI0Iz8EuSisgvBnslUQWSBU0hUV2No@dpg-co66dt8l5elc73aclde0-a/render_db_52tl")
    conn.close()
    return "Database connection successful."

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://render_db_52tl_user:qQfI0Iz8EuSisgvBnslUQWSBU0hUV2No@dpg-co66dt8l5elc73aclde0-a/render_db_52tl")
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
    return "Basketball table created successfully."


