#   oracle 연결
import cx_Oracle

connection = cx_Oracle.connect('SCOTT/TIGER@XE')
cursor = connection.cursor()
querystring = "SELECT*FROM DEPT"
cursor.execute(querystring)

print(cursor.fetchall())
connection.close()
