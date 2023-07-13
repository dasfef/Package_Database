import pymysql
conn, cur = None, None

try:
    conn = pymysql.connect(host="localhost", user="root", password="1234", db="shopdb", charset="utf8")
    cur = conn.cursor()
except:
    print("Error: Couldn't connect to DB server")

sql = "select * from test;"
cur.execute(sql)

result = cur.fetchall()
# result = cur.fetchone()

print(result)
print(result[0][0])
# for row in result:
#     print(row[1])

# ========== DB 내용 집어넣기 ==========
# while True:
#     idData = input("ID: ")
#     pwData = input("PW: ")

#     if (idData==""):
#         break
#     sql = f"insert into test values('{idData}', '{pwData}')"
#     cur.execute(sql)

conn.commit()
conn.close()
