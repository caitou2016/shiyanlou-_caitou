import os
from flask import Flask

def create_app():
    app = Flask("rmon")
    file = os.environ.get("RMON_CONFIG")
    dic = {}
    with open(file,'r') as file:
        for line in file:
            if not "#" in line and ":" in line:
                cf = line.strip().split(":",1)
                dic[eval(cf[0])] = eval(cf[1])
    
    for key in dic:
        app.config[key.upper()] = dic.get(key)

    return app

if __name__ == '__main__':
    create_app

