from flask import Flask, flash, render_template, redirect, session, url_for, request

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash(f"Already logged in as {session['username']}")
        return redirect(url_for('index'))
    if request.method == 'POST':
        session['username'] = request.form['username']
        flash(f"Logged in as {session['username']}")
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        username = session.pop('username', None)
        flash(f"{username} logged out")
    else:
        flash(f"You are not logged in.")
    return redirect(url_for('index'))

@app.route('/my_account')
def my_account():
    if 'username' in session:
        return render_template('my_account.html', username=session['username'])
    else:
        flash(f"You are not logged in.")
    return redirect(url_for('index'))
    

