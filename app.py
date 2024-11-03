import random
from DB1 import register_acc, login_acc, add_pass, delete_pass, edit_pass, list_of_passwords
from flask import Flask, render_template, request
from flask import redirect, url_for, session
from generate import generate
from review import review
app = Flask(__name__)
app.secret_key = 'Insert_Your_Secret_Key_Here'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/review')
def review_page():
    return render_template('review.html', rating="--")
@app.route('/review_user')
def review_user_page():
    return render_template('review_user.html', rating="--")
@app.route('/review_pass', methods=['POST'])
def calculate_score():
    if request.method == 'POST':
        password = request.form['password']
        if (password == ""):
            score = review(password)
            return render_template('review.html', rating="--")
        else:
            score = review(password)
            return render_template('review.html', rating=score)

@app.route('/generate')
def generate_page():
    return render_template('generate.html', password="")
@app.route('/generate_pass', methods=['POST'])
def generate_password_route():
    password_keyword = request.form.get('password')
    quantity = request.form.get('quantity')
    if quantity is None:
        length = 6
    else:
        length = int(quantity)
    include_special_symbols = request.form.get('specialsymbol') == "True"   
    password = generate(length, include_special_symbols, password_keyword)
    return render_template('generate.html', password=password)

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html', auth = 2)
@app.route('/login_user', methods=['POST'])
def verify_user():
    email = request.form.get('email')
    password = request.form.get('password')
    auth = login_acc(email, password)
    if auth == 0:
        return render_template('login.html', auth=auth)
    elif auth == 1:
        return render_template('login.html', auth=auth)
    else:
        if auth == 2:
            session['user'] = email
            return redirect(url_for('profile'))

@app.route('/signup', methods=['GET'])
def register_page():
    return render_template('signup.html', acc = False)
@app.route('/signup_user', methods=['POST'])
def add_user():
    email = request.form.get('email')
    password = request.form.get('password')
    acc = register_acc(email, password)
    if acc == True:
        return render_template('signup.html', acc = acc)
    else:
        session['user'] = email
        return redirect(url_for('profile'))

@app.route('/profile', methods=['GET'])
def profile():
    email = session.get('user')
    x = list_of_passwords(email)
    return render_template('profile_user.html', user = email, passwords = x)
@app.route('/profile_add', methods=['POST'])
def add_password():
    email = session.get('user')
    username = request.form.get('username')
    passkey = request.form.get('password')
    s = add_pass(username, passkey, email)
    x = list_of_passwords(email)
    return render_template('profile_user.html', user = email, passwords = x)
@app.route('/profile_delete', methods=['POST'])
def delete_password():
    email = session.get('user')
    username = request.form.get('passid')
    s = delete_pass(username, email)
    x = list_of_passwords(email)
    return render_template('profile_user.html', user = email, passwords = x)
@app.route('/profile_edit', methods=['POST'])
def edit_password():
    email = session.get('user')
    username = request.form.get('passid')
    password = request.form.get('value')
    s = edit_pass(username, email, password)
    x = list_of_passwords(email)
    return render_template('profile_user.html', user = email, passwords = x)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    app.run(debug=True)