from flask import Flask,flash, render_template, url_for, request,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'ragav'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3308
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Valarmathy'
app.config['MYSQL_DB'] = 'studentsdatabase'

mysql = MySQL(app)

@app.route('/')
def index():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students_data")
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', students_data=data)

@app.route('/insert', methods =["POST"])
def insert():
        if request.method == "POST":
          flash("Data Inserted Successfully")
          id=request.form['id']
          sname = request.form['sname']
          department=request.form['department']
          mobile=request.form['mobile']
          email=request.form['email']
          cur=mysql.connection.cursor()
          cur.execute("INSERT INTO students_data(id,sname,department,mobile,email) VALUES (%s,%s,%s,%s,%s)",(id,sname,department,mobile,email))
          mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ["GET"])
def delete(id_data):
    flash("Record has been deleted Succefully")
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM students_data WHERE id=%s",(id_data))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method =='POST':
        id= request.form['id']
        sname = request.form['sname']
        department = request.form['department']
        mobile = request.form['mobile']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE students_data SET sname=%s, department=%s, mobile=%s, email=%s WHERE id=%s ",(sname, department,mobile, email, id))
        mysql.connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
