import requests
import pprint
import ssl
import urllib3
import os
import glob

from flask import Flask
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLSv1
        )

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

s = requests.Session()
s.mount("https://10.31.70.210:55443", Ssl1HttpAdapter())

r = s.post(
    "https://10.31.70.210:55443/api/v1/auth/token-services",
    auth=("restapi", "j0sg1280-7@"),
    verify=False
)

token = r.json()['token-id']
header = {"content-type": "application/json", "X-Auth-Token": token}
r = s.get(
    "https://10.31.70.210:55443/api/v1/global/memory/processes",
    headers=header,
    verify=False
)
processes=r.json()['processes']
ps_sorted= sorted(processes, key=lambda ps: int(ps['memory-used']), reverse=True)
pprint.pprint(ps_sorted[0:10])

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
    files = os.listdir('C:\\Users\\sa.podsoblyaeva.JETINF\\Desktop\\Configs\\')
    pprint.pprint(files)
    return(files)

@app.route('/memory')

def memory():
    m = ps_sorted[0:10]
    pprint.pprint(m)
    return (m)

if __name__=='__main__':
    #app.run()
    app.run(debug=True)

