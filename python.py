import mysql.connector

conn =mysql.connector.connect(host="localhost",database="apidevelop",user="root",password="123456")
cursor = conn.cursor()
print(conn.is_connected())
mysql = "select * from customerinfo"
cursor.execute(mysql)
# demo=cursor.execute(mysql)
# print(demo)
rows = cursor.fetchall()
print(rows)