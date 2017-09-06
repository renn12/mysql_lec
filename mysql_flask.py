import MySQLdb
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
	db = MySQLdb.connect('192.168.0.124', 'root', '1111', 'raspberry')
	cur = db.cursor()
	sql = 'select id, name, phone from mysql_test'
	cur.execute(sql)
	rs = cur.fetchall()
	templateData = {'data': rs}
        cur.close()
        db.close()

	return render_template('mysql_flask.html', **templateData)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888)
