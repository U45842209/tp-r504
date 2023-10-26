import mysql.connector
from mysql.connector import errorcode
from flask import Flask

class MYSQL:
    def __init__(self):
        self.cnx = None

    def connect_to_db(self):
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='172.59.0.2', database='demosql')
            self.cnx = cnx
            return 'Process made it to the end'
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return "Something is wrong with your user name or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return "Database does not exist"
            else:
                return err

    def is_connected(self):
        if self.cnx and self.cnx.is_connected():
            return 'We are connected !'
        else:
            return 'Not connected.. (Yet !)'

    def close_connection_to_db(self):
        if self.cnx and self.cnx.is_connected():
            try:
                self.cnx.close()
                return 'Connection closed !'
            except:
                return 'Something went wrong.. (Maybe we are not connected)'

    def testing(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("SHOW TABLES;")
            results = cursor.fetchall()
            table_names = [row[0] for row in results]
            return table_names


db = MYSQL()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/connect')
def connect():
    result = db.connect_to_db()
    return str(result)

@app.route('/is_connect')
def is_connect():
    result = db.is_connected()
    return str(result)

@app.route('/close')
def close():
    result = db.close_connection_to_db()
    return str(result)

@app.route('/test')
def test():
    result = db.testing()
    return str(result)

if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
