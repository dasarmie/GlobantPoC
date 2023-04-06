from flask import Flask
from sql_connection import sqlConnection
import pandas as pd

db = sqlConnection('sqlglobantpoc.database.windows.net', 'GlobantPoC')

app = Flask(__name__)

@app.route('/')
def hired_employees_quarter():
    df = pd.read_sql('EXEC hired_employees_quarter', db.conn)
    result = df.to_html(index=False)
    return result

app.run()

'''
if __name__ == '__main__':
    app.run(debug=True)
'''
