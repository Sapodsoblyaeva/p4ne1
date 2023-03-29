from flask import Flask
import requests
import pprint

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    s = """
    This is a server with config files. 
    Hello there"""
    return(s)

if __name__=='__main__':
    app.run(debug=True)


from flask import Flask
import requests
import pprint

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    s = """
    This is a server with config files. 
    Hello there"""
    return(s)

if __name__=='__main__':
    app.run(debug=True)