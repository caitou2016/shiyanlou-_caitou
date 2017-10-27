#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json
from flask import Flask,render_template

app = Flask(__name__)
#app.run(port=3000)

app.config['TEMPLATES_AUTO_RELOAD']= True
files_path = '/home/shiyanlou/files'
#file_list = []
@app.route('/')
def index():
    file_list = []
    # file_name = 'helloshiyanlou.json'
    files = os.listdir(files_path)
    for news_file in files:
        file_name = os.path.join(files_path,news_file)
        with open(file_name,'r') as file_read:
            file_list.append(json.loads(file_read.read()))
    return render_template('index.html',files=file_list)


