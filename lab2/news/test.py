#!/usr/bin/env python3

import os
import json

files_path = '/home/shiyanlou/files'
def index():
    file_list = []
      # file_name = 'helloshiyanlou.json'
    files = os.listdir(files_path)
    for news_file in files:
        file_name = os.path.join(files_path,news_file)
#        print(file_name)
        with open(file_name,'r') as file_read:
            file_list.append(json.loads(file_read.read()))
    for i in file_list:
        print(i)
if __name__ == '__main__':
    index()
