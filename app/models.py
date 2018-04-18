from . import db

class User(db.Model):
    __tablename__='blogger'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
