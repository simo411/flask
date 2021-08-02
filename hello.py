from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='simo'
app.config['MySQL_PASSWORD']='simo'
app.config['MySQL_DB']='test'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        id = userDetails['_id']
        name = userDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO test_1(id, firstname) VALUES(%d,%s)",(int(id), name))
        mysql.connection.commit()
        cur.close()
        return "SUCCESS"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
        