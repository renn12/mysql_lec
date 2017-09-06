import MySQLdb
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
        cur = db.cursor()
        sql = "select id, name, phone from mysql_test"
        cur.execute(sql)
        rs = cur.fetchall()
        cur.close()
        db.close()
        return render_template('select_id.html', data = rs)


@app.route('/GET/ID/<string:id>')
def get_id(id):
	db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
	cur = db.cursor()
	sql = "select id, name, phone from mysql_test where id = '%s'" % id
	cur.execute(sql)
	rs = cur.fetchall()
	cur.close()
	db.close()
	return render_template('select_id.html', data = rs)

@app.route('/POST')
def post():
	db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
        cur = db.cursor()
	id = request.args.get('id')
	name = request.args.get('name')
	phone = request.args.get('phone')
        sql = "insert into mysql_test value('%s', '%s', '%s')" % (id, name, phone)
	try:
		cur.execute(sql)
		db.commit()
	except:
		db.rollback()

        cur.close()
        db.close()
	
        #return "<script>document.location.href='/'</script>"
	return index()

@app.route('/PUT')
def put():
	db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
        cur = db.cursor()
	id = request.args.get('id')
	newid = request.args.get('newid')
        sql = "update mysql_test set id='%s' where id='%s'" % (newid, id)
        try:
                cur.execute(sql)
                db.commit()
        except:
                db.rollback()

        cur.close()
        db.close()
        return index()

@app.route('/DELETE')
def delete():
        db = MySQLdb.connect('localhost', 'root', '1111', 'raspberry')
        cur = db.cursor()
	id = request.args.get('id')
        sql = "delete from mysql_test where id='%s'" % (id)
        try:
                cur.execute(sql)
                db.commit()
        except:
                db.rollback()

        cur.close()
        db.close()
        return index()


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
