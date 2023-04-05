import pyodbc

class sqlConnection:
	
	def __init__(self, server, database):
		self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=admindb;PWD=Medellin01*')
		self.cursor = self.conn.cursor()
		
	def insert_data_sql(self, table_name, columns, df_name):
		string_truncate = f"TRUNCATE TABLE {table_name}"
		self.cursor.execute(string_truncate)
		string_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?']*len(columns))})"
		for row in df_name.values.tolist():
			self.cursor.execute(string_sql, row)
		self.conn.commit()