import os

from flask import Flask
import pprint
import glob

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    s = """
    This is a server with config files. 
    Hello there"""
    return(s)

@app.route('/configs')
def configs():
    files = os.listdir('/Users/sveta/Downloads/config_files/')
    pprint.pprint(files)
    return(files)

if __name__=='__main__':
    app.run(debug=True)


