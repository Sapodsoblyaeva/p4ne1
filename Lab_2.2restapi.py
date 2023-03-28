#rest api

import requests
import pprint
import ssl
import urllib3

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
    "https://10.31.70.210:55443/api/v1/interfaces",
    headers=header,
    verify=False
)
pprint.pprint(r.json())

