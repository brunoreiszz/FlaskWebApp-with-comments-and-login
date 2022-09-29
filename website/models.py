from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(150))
    #page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    # user_name ????????

    #def __repr__(self):
     #   return f'<Comment "{self.data[:20]}...">'

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #pages = db.relationship('Page', backref='user')
    comments = db.relationship('Comment', backref='user') #, backref='user'

    #def __repr__(self):
     #   return f'<User "{self.user}">'

#class Page(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  name = db.Column(db.String(150))
   # comments = db.relationship('Comment', backref='page')
# ...Tentativa de simular outra base de dados para os comentários funcionarem




