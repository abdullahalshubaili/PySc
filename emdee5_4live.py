#!/usr/bin/python3
import hashlib
import requests
import re 
import os
import base64
proxy = 'http://localhost:8080'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

url = ""


resp1 = requests.get(url)

header = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
,'Accept-Language': 'en-US,en;q=0.5'
,'Accept-Encoding': 'gzip, deflate'
,'Referer': 'http://docker.hackthebox.eu/'
,'Content-Type': 'application/x-www-form-urlencoded'
}

md5forfirsttime = resp1.text[167:187]
param = "hash="

# cookie stuff
myphpsessid = resp1.headers['Set-Cookie']
sid = myphpsessid[10:36]
#to print cookie
#print("sessid\n"+sid)
cookie = {'_ga':'GA1.2.364128487.1559249777', '__auc':'6126f6b216b28b68d65b544cdb6',' _gid':'GA1.2.1301747270.1561920761', 'PHPSESSID': sid
}
### end of cookie stuff


for x in range(0,2000):


    rqst = requests.post(url, headers=header, data=param,cookies=cookie)
    
    md5 = rqst.text[167:187]
    print("print plain string from resp")
    print(md5)

    hash = hashlib.md5(md5.encode())
    print(hash.hexdigest())
    param = "hash="+hash.hexdigest()
    print(param)
    s = "HTB"
    if s in rqst.text:
        print("\n\n\n\n\n HTB \n\n\n\n\n\n")
        print("\n\n\n"+rqst.text)
        exit()
