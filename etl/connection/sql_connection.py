# Import libraries
import pyodbc

# set up SQL Server connection
server = 'sqlglobantpoc.database.windows.net'
database = 'GlobantPoC'
username = 'admindb'
password = 'Medellin01*'

#Create SQL Server connection
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    print("Successful connection")
except Exception as ex:
    print(ex)