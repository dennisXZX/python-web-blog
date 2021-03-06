from src.common.database import Database
from src.models.user import User

from flask import Flask, render_template, request, session

# __name__ == __main__
app = Flask(__name__)
app.secret_key = "dennis"


@app.route('/')
def hello_method():
    return render_template('login.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/login', methods=['POST'])
def login_user():
    # get the form values associated with  the name property
    email = request.form['email']
    password = request.form['password']

    # TODO - somehow this code result in an internal server error
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template('profile.html', email=session['email'])


if __name__ == '__main__':
    app.run(port=4999)
