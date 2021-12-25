from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class UserModel(db.Model):
    __tablename__ = 'user_table'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
 
    def __repr__(self):
        return '<User %r>' % self.name