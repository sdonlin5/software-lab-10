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
@app.route('/db-select')
def select():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball")
    results = cur.fetchall()
    conn.close()
    table = create_table(results)
    return table











# Helper function to create a table from queried data
def create_table(data):
    table = '<table> \n'

    # Create the header
    table_header = data[0].split(',')
    table += '  <tr> \n'
    for c in table_header:
        table += '      <th>{0}</th>\n'.format(c.strip())
    table += '  </tr>\n'

    # Get table data
    for row in data[1:]:
        r = row.split(',') # split on comma
        table += '  <tr>\n' # open row tag
        for column in r:
            table += '    <td>{0}</td>\n'.format(column.strip())
        table += '  </tr>\n' # close row tag\

    # Close table tag
    table += '</table>'
    return table
