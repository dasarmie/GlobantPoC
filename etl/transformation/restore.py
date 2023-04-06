from sql_connection import sqlConnection
import pandas as pd
from fastavro import reader

db = sqlConnection('sqlglobantpoc.database.windows.net', 'GlobantPoC')

table = 'departments'
table_db = f"dbo.{table}"
avro_records = []

with open(f"{table}.avro", 'rb') as data:
    avro_reader = reader(data)
    for record in avro_reader:
        avro_records.append(record)

df_avro = pd.DataFrame(avro_records)
df_columns = df_avro.columns.to_list()
db.insert_data_sql(table_name=table_db, columns=df_columns, df_name=df_avro)


