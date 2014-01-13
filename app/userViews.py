__author__ = 'lanjun'
from app import app
from app import dao
from flask import render_template

@app.route('/init')
def create():
    dao.create()
    return 'init ok'

@app.route('/add')
def add():
    dao.add()
    return 'add ok'

@app.route('/allusers')
def findAll():
    users = dao.query()
    return render_template('users.html', users=users)

@app.route('/user/<username>')
def findByName(username):
    user = dao.queryByName(username)
    print user['name']
    return render_template('user.html', user=user)