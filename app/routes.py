from app import app, mysql
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_value')
def add_value():
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO add_value (value) values(%s) ''', ('3'))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('index'))