#   MySQL 연결
import pymysql

conn = pymysql.connect(host='localhost', user='zerock',
                       password='zerock', db='book_ex', charset='utf8')

curs = conn.cursor()

sql = "select * from tbl_board"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()
