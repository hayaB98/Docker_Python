import os
from flask import Flask
from flaskext.mysql import MySQL
import os, json, subprocess, yaml, logging

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'newdatabase'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)

@app.route('/')
def inp():
     return "hello world"

@app.route('/cpu')
def cpu():
     cursor = mysql.connect().cursor()
     cursor.execute(''' SELECT * FROM cpu_usage WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 1 DAY); ''')
     result = list(cursor.fetchall())
     result = [{'usage': usage, 'taken at': taken_at} for usage, taken_at in result]
     return json.dumps(result, indent=4, default=str)

@app.route('/disk')
def disk():
     cursor = mysql.connect().cursor()
     cursor.execute(''' SELECT * FROM disk_usage WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 1 DAY); ''')
     result = list(cursor.fetchall())
     result = [{'usage':usage,'free':free,'taken at':taken_at } for usage,free,taken_at in result]
     return json.dumps(result, indent=4, default=str)

@app.route('/memory')
def mem():
     cursor = mysql.connect().cursor()
     cursor.execute(''' SELECT * FROM mem_usage WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 1 DAY); ''')
     result = list(cursor.fetchall())
     result = [{'usage':usage,'free':free,'taken_at':taken_at} for usage,free,taken_at in result]
     return json.dumps(result, indent=4, default=str)

@app.route('/now')
def datanow():
 #    dir = os.path.dirname(os.path.realpath(__file__)
     result = subprocess.check_output(['bash', '/project/currentvalues.sh'])
     result = yaml.load(result)
     return json.dumps(result, indent=4, default=str)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)), debug=True)
