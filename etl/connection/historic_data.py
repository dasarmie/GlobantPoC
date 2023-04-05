from adls_connection import read_file_adls
from sql_connection import sqlConnection
import pandas as pd
from datetime import datetime

# Define columns
columns_jobs = ['id', 'job']

columns_departments = ['id', 'department']

columns_hired_employees = ['id', 'datetime', 'name', 'department_id', 'job_id']

# Read files from adls and create dataframes
jobs = read_file_adls('files/history/', 'jobs.csv')
df_jobs = pd.read_csv(jobs, names=columns_jobs, na_values='NA')
# Filter rows with null values
df_jobs = df_jobs[~df_jobs.isnull().any(axis=1)]

departments = read_file_adls('files/history/', 'departments.csv')
df_departments = pd.read_csv(departments, names=columns_departments, na_values='NA')
# Filter rows with null values
df_departments = df_departments[~df_departments.isnull().any(axis=1)]

hired_employees = read_file_adls('files/history/', 'hired_employees.csv')
df_hired_employees = pd.read_csv(hired_employees, names=columns_hired_employees, sep=',', na_values='NA')
# Filter rows with null values
df_hired_employees = df_hired_employees[~df_hired_employees.isnull().any(axis=1)]

# Azure SQL Server connection
db = sqlConnection('sqlglobantpoc.database.windows.net', 'GlobantPoC')

# Insert historic data into tables on Azure SQL Database
db.insert_data_sql('dbo.departments', columns_departments, df_departments)

db.insert_data_sql('dbo.jobs', columns_jobs, df_jobs)

db.insert_data_sql('dbo.hired_employees', columns_hired_employees, df_hired_employees)

# Close to connection SQL Database
db.close()