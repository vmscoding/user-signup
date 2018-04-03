from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    if not username:
        error_user = "Please enter a username."
        return redirect("/?error=" + error_user)
    if not password:
        error_pass = "Please enter a valid password."
        return redirect("/?error=" + error_pass)
    if not password_confirm:
        error_conf = "Please confirm your password."
        return redirect("/?error=" + error_conf)

    return render_template('welcome.html', username=username)

@app.route('/')
def index():
    error_user = request.args.get('error_user')
    error_pass = request.args.get('error_pass')
    error_conf = request.args.get('error_conf')
    return render_template('home.html', error_user=error_user, error_pass=error_pass, error_conf=error_conf)

app.run()