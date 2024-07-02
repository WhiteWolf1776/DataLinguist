import os;
import pyodbc, struct
from azure_dl import az_credential

def connect(server, port, database):
	authentication = 'ActiveDirectoryMsi'
	token_bytes = az_credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
	token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
	SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
	connection_string = f'Driver={{ODBC Driver 18 for SQL Server}};Server={server},{port};Database={database};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'	
	conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
	return conn

def print_data(connection, query):
	cursor = connection.cursor()
	cursor.execute(query)
	records = cursor.fetchall()
	for r in records:
		print(r)

