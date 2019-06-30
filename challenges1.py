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

resp1 = requests.get("http://docker.hackthebox.eu:33970/")
#print(resp1.cookies)
#print(resp1.headers)

"""

{'Date': 'Sun, 30 Jun 2019 12:14:31 GMT', 'Server': 'Apache/2.4.18 (Ubuntu)', 'Set-Cookie': 'PHPSESSID=k234akmenva3b507tptlpcsrd6; path=/', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate', 'Pragma': 'no-cache', 'Vary': 'Accept-Encoding', 'Content-Length': '388', 'Connection': 'close', 'Content-Type': 'text/html; charset=UTF-8'}

cookies
 _ga=GA1.2.364128487.1559249777; __auc=6126f6b216b28b68d65b544cdb6; _gid=GA1.2.1301747270.1561920761; PHPSESSID=jlbs0onk81chdegk5dljdfk475


=-=-=-=-=-=-=-=-=--==-=-=
new headers
POST / HTTP/1.1
'Host': docker.hackthebox.eu:33970
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
'Accept-Language: 'en-US,en;q=0.5'
'Accept-Encoding: 'gzip, deflate'
'Referer: 'http://docker.hackthebox.eu:33970/'
'Content-Type: 'application/x-www-form-urlencoded'
Cookie: _ga=GA1.2.364128487.1559249777; __auc=6126f6b216b28b68d65b544cdb6; _gid=GA1.2.1301747270.1561920761; PHPSESSID=jlbs0onk81chdegk5dljdfk475
Connection: close
Upgrade-Insecure-Requests: 1
"""
header = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
,'Accept-Language': 'en-US,en;q=0.5'
,'Accept-Encoding': 'gzip, deflate'
,'Referer': 'http://docker.hackthebox.eu:33970/'
,'Content-Type': 'application/x-www-form-urlencoded'
}



md5 = resp1.text[167:187]
param = "hash="+md5

myphpsessid = resp1.headers['Set-Cookie']
sid = myphpsessid[10:36]
print(sid)

cookie = {'_ga':'GA1.2.364128487.1559249777', '__auc':'6126f6b216b28b68d65b544cdb6',' _gid':'GA1.2.1301747270.1561920761', 'PHPSESSID': sid
}

for x in range(0,1000):

    #resp = requests.get("http://docker.hackthebox.eu:33664/")

    rqst = requests.post("http://docker.hackthebox.eu:33970/", headers=header, params=param,cookies=cookie)
    #print(rqst.text)

    notmd5d = rqst.text[167:187]
    #print(md5)
    notmd5 = base64.b64decode(notmd5d)
    print("notmd5 b64de\n")
    print(notmd5)
    md5r = hashlib.md5()
    #md5r = hashlib.md5(notmd5.encode()) 
    md5r.update(notmd5)
    print("md5r hex diges..\n"+md5r.hexdigest())
    notE = md5r.hexdigest()
    #encodedBytes = base64.b64encode(notE.encode("utf-8"))
    #encodedStr = str(encodedBytes, "utf-8")
    param = "hash="+notE
    print("hash\n"+param)
    #print(param)
    s = "HTB"
    if s in rqst.text:
        print("\n\n\n\n\n\n\n"+"HTB")
        print("\n\n\n"+rqst.text)
