import MySQLdb

db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
cur = db.cursor()
sql = "select id, name, phone from mysql_test"

cur.execute(sql)
rs = cur.fetchall()

result = []

for item in rs:
	result.append(list(item))

for item2 in result:
	#print item2, type(item2)
	print 'id: ' + str(item2[0]), 'name: ' + str(item2[1]), 'phone: ' + str(item2[2])

#print rs
#print type(rs)

cur.close()
db.close()
