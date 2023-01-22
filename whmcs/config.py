import mysql.connector

host_db = ''
name_db = ''
user_db = ''
pass_db = ''

db = mysql.connector.connect(
  host = host_db,
  user = user_db,
  password = pass_db,
  database = name_db
)