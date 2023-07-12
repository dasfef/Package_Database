import pymysql

sql = "insert into test values('id01', 'password01');"
conn, cur = None, None
conn = pymysql.connect(host="localhost", user="root", password="1234", db="shopdb", charset="utf8")
cur = conn.cursor()

cur.execute(sql)
conn.commit()
conn.close()