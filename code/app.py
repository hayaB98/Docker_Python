import os
from flask import Flask
from functools import wraps
from flaskext.mysql import MySQL
import os, json, subprocess, yaml, logging

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = 'newdatabase'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)
log_file = "./logfile.log"
log_level = logging.DEBUG
logging.basicConfig(level=log_level, filename=log_file, filemode="w+", format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger("logger")

def wrap(pre, post): 
    def decorate(func):
         @wraps(func)
         def call(*args, **kwargs):
             pre(func)
             result = func(*args, **kwargs)
             post(func)
             return result
         return call
    return decorate

def entering(func):
   logger.debug("Entered %s", func.__name__)

def exiting(func):
   logger.debug("Exited %s", func.__name__)

@app.route('/')
@wrap(entering,exiting)
def inp():
     return "hello world"

@app.route('/cpu')
@wrap(entering,exiting)
def cpu():
     cursor = mysql.connect().cursor()
     cursor.execute(''' SELECT * FROM cpu_usage WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 1 DAY); ''')
     result = list(cursor.fetchall())
     result = [{'usage': usage, 'taken at': taken_at} for usage, taken_at in result]
     return json.dumps(result, indent=4, default=str)

@app.route('/disk')
@wrap(entering,exiting)
def disk():
     cursor = mysql.connect().cursor()
     cursor.execute(''' SELECT * FROM disk_usage WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 1 DAY); ''')
     result = list(cursor.fetchall())
     result = [{'usage':usage,'free':free,'taken at':taken_at } for usage,free,taken_at in result]
     return json.dumps(result, indent=4, default=str)

@app.route('/memory')
@wrap(entering,exiting)
def mem():
     cursor = mysql.connect().cursor()
     cursor.execute(''' SELECT * FROM mem_usage WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 1 DAY); ''')
     result = list(cursor.fetchall())
     result = [{'usage':usage,'free':free,'taken_at':taken_at} for usage,free,taken_at in result]
     return json.dumps(result, indent=4, default=str)

@app.route('/now')
@wrap(entering,exiting)
def datanow():
     result = subprocess.check_output(['bash', '/project/currentvalues.sh'])
     result = yaml.load(result)
     return json.dumps(result, indent=4, default=str)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)), debug=True)
