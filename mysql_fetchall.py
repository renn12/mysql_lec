import MySQLdb

db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
cur = db.cursor()
sql = "select id, name, phone from mysql_test"

cur.execute(sql)
rs = cur.fetchall()

for item in rs:
	print item, type(item)

#print rs
#print type(rs)

cur.close()
db.close()
