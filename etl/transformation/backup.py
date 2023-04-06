from sql_connection import sqlConnection
from adls_connection import upload_file_adls
from fastavro import writer, parse_schema, reader
import pandas as pd

db = sqlConnection('sqlglobantpoc.database.windows.net', 'GlobantPoC')

schema_jobs = {
    'doc' : 'jobs',
    'name' : 'jobs',
    'namespace' : 'jobs',
    'type' : 'record',
    'fields' : [
        {'name' : 'id', 'type' : 'int'},
        {'name' : 'job', 'type' : 'string'}
    ]
}

ps_jobs = parse_schema(schema_jobs)

schema_departments = {
    'doc' : 'jobs',
    'name' : 'jobs',
    'namespace' : 'jobs',
    'type' : 'record',
    'fields' : [
        {'name' : 'id', 'type' : 'int'},
        {'name' : 'department', 'type' : 'string'}
    ]
}

ps_departments = parse_schema(schema_departments)

schema_hired_employees = {
    'doc' : 'jobs',
    'name' : 'jobs',
    'namespace' : 'jobs',
    'type' : 'record',
    'fields' : [
        {'name' : 'id', 'type' : 'int'},
        {'name' : 'name', 'type' : 'string'},
        {'name' : 'datetime', 'type' : 'string'},
        {'name' : 'department_id', 'type' : 'int'},
        {'name' : 'job_id', 'type' : 'int'}
    ]
}

ps_hired_employees = parse_schema(schema_hired_employees)

df_jobs = pd.read_sql('SELECT * FROM dbo.jobs', db.conn)
records_jobs = df_jobs.to_dict('records')
with open('jobs.avro', 'wb') as data:
    writer(data, ps_jobs, records_jobs)
upload_file_adls('jobs.avro', 'backup/jobs/jbos.avro')

df_departments = pd.read_sql('SELECT * FROM dbo.departments', db.conn)
records_departments = df_departments.to_dict('records')
with open('departments.avro', 'wb') as data:
    writer(data, ps_departments, records_departments)
upload_file_adls('departments.avro', 'backup/departments/departments.avro')

df_hired_employees = pd.read_sql('SELECT * FROM dbo.hired_employees', db.conn)
records_hired_employees = df_hired_employees.to_dict('records')
with open('hired_employees.avro', 'wb') as data:
    writer(data, ps_hired_employees, records_hired_employees)
upload_file_adls('hired_employees.avro', 'backup/hired_employees/hired_employees.avro')