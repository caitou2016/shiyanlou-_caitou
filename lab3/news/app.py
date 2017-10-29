#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json
from flask import Flask,render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/caitou'
app.config['TEMPLATES_AUTO_RELOAD']= True
db = SQLAlchemy(app)
   
class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',backref=db.backref('file_b',lazy = 'dynamic'))
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
if Category.query.all() and File.query.all() is None:
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
#app.run(port=3000)

#dir_path = '/home/shiyanlou/files'
#file_list = []
@app.route('/')
def index():
    
    file_list = [file1,file2]
    # file_name = 'helloshiyanlou.json'
    #files = os.listdir(dir_path)
   # for news_file in file_list:
    #    file_name = os.path.join(dir_path,news_file)
     #   with open(file_name,'r') as file_read:
     #       file_list.append(json.loads(file_read.read())['title'])
    return render_template('index.html',files=file_list)

@app.route('/files/<file_id>')
def file(file_id):
   # file_path = os.path.join(dir_path,filename+'.json')
    file_list=[file1,file2]
    files_id=[file1.id,file2.id]
   # for file_n in file_list:
    if file1.id == file_id:
        #with open(file_path,'r') as file_read2:
         #   file_connect = json.loads(file_read2.read())
        return render_template('file.html',file_n=file1)
       # else:
       #     return render_template('404.html')
#app.run(port=3000)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
