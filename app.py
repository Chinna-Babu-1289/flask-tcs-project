from configparser import ConfigParser
from flask import Flask, render_template, redirect, request, url_for, session
from models import User, db

app = Flask(__name__)

# Config's
# sqlite : "sqlite:///localhost/databaseName"
# mysql = 'mysql+pymysql://username:password@localhost/db_name'
config_path = 'config.ini'
config = ConfigParser()
config.read(config_path)
dbHost = config['database']['dbhost']
dbUser = config['database']['dbuser']
dbPass = config['database']['dbpass']
dbName = config['database']['dbname']

conn = f'mysql+pymysql://{dbUser}:{dbPass}@{dbHost}/{dbName}'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0
app.config['SECRET_KEY'] = "abcdabcd"

db.init_app(app)


@app.route('/')
def home():
    return render_template('register.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginDetails = request.form
        # print(loginDetails)
        email = loginDetails['email']
        password = loginDetails['password']
        dbuser = User.query.filter_by(
            email=email, password=password).first()
        if dbuser:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        signupDetails = request.form
        print(signupDetails)
        username = signupDetails['username']
        email = signupDetails['email']
        password = signupDetails['password']
        confirmpassword = signupDetails['password2']
        user = User(username=username, email=email,
                    password=password, confirmpassword=confirmpassword)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
