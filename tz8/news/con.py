# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/caitou'
db = SQLAlchemy(app)
   
class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',backref=db.backref('file',lazy = 'dynamic'))
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__(self):
        return '<File (name=%s)>' % self.title
    
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category(name=%s)>' % self.name
    
db.create_all()
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java',datetime.utcnow(),java,'File Conten - java is cool!')
file2 = File('Hello Python',datetime.utcnow(),python,'File Content-Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
