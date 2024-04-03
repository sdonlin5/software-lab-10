from flask import Flask
import psycopg2

app = Flask(__name__)

# Set the db_url for re-use
db_url = "postgres://render_db_52tl_user:qQfI0Iz8EuSisgvBnslUQWSBU0hUV2No@dpg-co66dt8l5elc73aclde0-a/render_db_52tl"

@app.route('/')
def hello_world():
    return 'Hello World from Stephen Donlin in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(db_url)
    conn.close()
    return "Database connection successful."

# db_create
@app.route('/db_create')
def create():
    conn = psycopg2.connect(db_url)
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

#db_insert
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    conn.commit()
    conn.close()
    return "Successfully populated basketball table."


# db_select
@app.route('/db_select')
def select():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball")
    results = list(cur.fetchall())
    conn.close()
    table = create_table(results)
    return table

# db_drop
@app.rout()('/db_drop')
def drop():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("DROP TABLE Basketball;")
    conn.commit()
    conn.close()
    return "dropped"

"""
    table = '<table>\n'
    for row in results:
        table += '    <tr>\n'
        for col in row:
            table += '        <td>{}</td>\n'.format(col)
        table += '    </tr>\n'
    table += '</table>'
"""

def create_table(data):
    table = '<table style="border: 2px solid black; border-spacing: 5; padding: 10px;">\n'
    for row in data:
        table += '  <tr>\n'
        for col in row:
            table += '  <td>{}</td>\n'.format(col)
        table += '  </tr>\n'
    table += '</table>'

    return table