from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # Create a new user object
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')







app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


if __name__ == '__main__':
  app.run(debug=True)