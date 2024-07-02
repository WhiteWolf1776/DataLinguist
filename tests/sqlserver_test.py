import pytest
from azure_dl import sqlserver

with open("tests/config/dev_sqlserver.cfg", 'r') as f:
	global azure_sql_server
	azure_sql_server = f.readline().strip()
	global azure_sql_port
	azure_sql_port = f.readline().strip()
	global azure_sql_database
	azure_sql_database = f.readline().strip()
	global azure_sql_schema
	azure_sql_schema = f.readline().strip()
	global azure_sql_table
	azure_sql_table = f.readline().strip()

def testConnection():
	conn = sqlserver.connect(azure_sql_server, azure_sql_port, azure_sql_database)
	query = f"select * from [{azure_sql_schema}].[{azure_sql_table}]"
	sqlserver.print_data(conn, query)
	assert False
