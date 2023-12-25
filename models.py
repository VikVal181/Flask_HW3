from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False) 
 
    def __repr__(self):
        return f'{self.name} {self.email} {self.password}'
    
    def set_pass(self, password):
        self.password = generate_password_hash(password)
        
    def check_pass(self, password):
        return check_password_hash(self.password, password)
        