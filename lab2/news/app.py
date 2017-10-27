#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json
from flask import Flask,render_template

app = Flask(__name__)
#app.run(port=3000)

app.config['TEMPLATES_AUTO_RELOAD']= True
dir_path = '/home/shiyanlou/files'
#file_list = []
@app.route('/')
def index():
    file_list = []
    # file_name = 'helloshiyanlou.json'
    files = os.listdir(dir_path)
    for news_file in files:
        file_name = os.path.join(dir_path,news_file)
        with open(file_name,'r') as file_read:
            file_list.append(json.loads(file_read.read())['title'])
    return render_template('index.html',files=file_list)

@app.route('/files/<filename>')
def file(filename):
    file_path = os.path.join(dir_path,filename+'.json')
    if os.path.exists(file_path):
        with open(file_path,'r') as file_read2:
            file_connect = json.loads(file_read2.read())
        return render_template('file.html',file_connect=file_connect)
    else:
        return render_template('404.html')
#app.run(port=3000)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
