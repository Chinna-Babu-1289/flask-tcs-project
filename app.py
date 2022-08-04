from flask import Flask, render_template, redirect, request, url_for, session
from models import User, db, formatUser
from sqlalchemy import values

app = Flask(__name__)

# Config's
# sqlite : "sqlite:///localhost/databaseName"
# mysql = 'mysql+pymysql://username:password@localhost/db_name ' 
dbHost = "localhost"
dbUser = "praveen"
dbPass = "praveen!1"
dbName = "flaskdb"
conn = f'mysql+pymysql://{dbUser}:{dbPass}@{dbHost}/{dbName}'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0
app.config['SECRET_KEY'] = "abcdabc"

db.init_app(app)

@app.route('/create')
def create():
    db.create_all()
    return "<h1> Created database successfully </h1>"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        dbuser = User.query.filter_by(email=email, password=password).first()
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
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')


# @app.route('/add_user', methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'POST':
#         userDetails = request.json
#         username = userDetails['username']
#         email = userDetails['email']
#         password = userDetails['password']
#         confirmPassword = userDetails['confirmPassword']
#         user = User(username=username, email=email,
#                      password=password, confirmPassword=confirmPassword)
#         db.session.add(user)
#         db.session.commit()
#         return formatUser(user)

#     if request.method == 'GET':
#         users = User.query.all()
#         user_list = [format(user) for user in users]
#         return {"result": user_list}


if __name__ == '__main__':
    app.run(debug=True)
