from flask import Flask, render_template, request
from models import db, User
from form import RegisterForm
from flask_wtf import CSRFProtect




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)



@app.route('/')
def index():
    return render_template('base.html')

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')
    

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(
            name = name,
            email=email,
            password=password
        )
        user.set_pass(password)
        db.session.add(user)
        db.session.commit()
    return render_template('form.html', form=form)

@app.route('/get_users/')
def get_users():
    users = User.query.all()
    context = {
        'users': users    }
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run()