from flask import Flask, render_template, request
from settings import sql_setting
import pymysql.cursors
app = Flask(__name__)
conn = pymysql.connect(host=sql_setting.host,
                       user=sql_setting.user,
                       db=sql_setting.db,
                       password=sql_setting.password)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/table')
def Table():
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        ins = "SELECT * FROM users"
        cursor.execute(ins)
        users = cursor.fetchall()
        print(users)
    return render_template('table.html', members=users)


@app.route('/register', methods=["POST", "GET"])
def Register():
    if request.method == "POST":
        form_data = request.form.to_dict()
        with conn.cursor() as cursor:
            ins = "SELECT max(id) from users"
            cursor.execute(ins)
            form_data['id'] = cursor.fetchone()[0]+1
        with conn.cursor() as cursor:
            ins = "INSERT INTO users VALUES(%s,%s,%s)"
            cursor.execute(ins,
                           (form_data['id'],
                            form_data['username'],
                            form_data['grade']))
            conn.commit()
    return render_template('register.html')


if __name__ == "__main__":

    app.run(debug=True)
