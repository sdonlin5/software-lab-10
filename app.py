""" 
Flask Basketball Database Module

Creates, populates, reads and deletes a PostgresSQL database of basketball players via http endpoints. 

"""

from flask import Flask
import psycopg2

# Initialize the Flask application
app = Flask(__name__)

# Database URL for PostgreSQL connection
db_url = #--! INSERT YOUR DATABASE LOCATION HERE !--#

@app.route('/')
def hello_world():
    """
    Index route - returns greeting.
    """
    return 'Hello World from Stephen Donlin in 3308'

@app.route('/db_test')
def testing():
    """
    Route to test database connectivity.
    Attempts to connect to the database and then closes the connection.
    Returns a success message if no exceptions occur.
    """
    conn = psycopg2.connect(db_url)
    conn.close()
    return "Database connection successful."

@app.route('/db_create')
def create():
    """
    Route to create a Basketball table in the database.
    Includes columns for first name, last name, city, team name, and jersey number.
    """
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

@app.route('/db_insert')
def inserting():
    """
    Route to insert predefined records into the Basketball table.
    Inserts player data for Jayson Tatum, Stephen Curry, Nikola Jokic, and Kawhi Leonard.
    """
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

@app.route('/db_select')
def select():
    """
    Route to select all records from the Basketball table and display them in an HTML table.
    Calls create_table function to format the output.
    """
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball") # To select all data
    results = list(cur.fetchall())
    conn.close()
    table = create_table(results)
    return table

@app.route('/db_drop')
def drop():
    """
    Route to drop the Basketball table from the database.
    """
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("DROP TABLE Basketball;")
    conn.commit()
    conn.close()
    return "Basketball table dropped successfully."

def create_table(data):
    """
    Utility function to convert a list of tuples into an HTML table.
    Each tuple represents a row from the database query result.

    Args:
        data (list of tuples): Data retrieved from a SQL query.

    Returns:
        str: HTML string representing the table.
    """
    table = '<table>\n'
    for row in data:
        table += '  <tr>\n'
        for col in row:
            table += '  <td style="padding-top: 5px; padding-bottom: 5px; padding-right: 10px; padding-left: 10px">{}</td>\n'.format(col)
        table += '  </tr>\n'
    table += '</table>'
    return table
