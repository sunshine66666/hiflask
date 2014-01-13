__author__ = 'lanjun'

from app import app
from flask import redirect, url_for, session, request, render_template, flash

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'username' in session:
        flash('You were logged in')
        return redirect(url_for('hello', name=session['username']))
        #return render_template('hello.html', name=escape(session['username']))
        #return 'Logged in as %s' % escape(session['username'])
        pass
    error = None
    if request.method == 'GET':
        app.logger.debug('forward to the login page. ')
        return render_template('login.html')
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
             app.logger.debug('login ok, forward to the hello page. ')
             session['username'] = request.form['username']
             return redirect(url_for('hello', name=request.form['username']))
             #return render_template('hello.html', name=request.form['username'])
        else:
            name = request.form['username']
            error = 'Invalid username/password'
            return render_template('error.html', name=name, error=error)

def valid_login(username, password):
    return True

@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name=None):
    if request.method == 'GET':
        return render_template('hello.html', name=name)
    if request.method == 'POST':
        session.pop('username', None)
        return redirect(url_for('login'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)