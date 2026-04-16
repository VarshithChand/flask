from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


# ✅ FIX: create tables safely
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

        return redirect('/users')

    return render_template('index.html')


@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


if __name__ == '__main__':
    app.run(host='0.0.0.0')