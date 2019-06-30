#!/usr/bin/python3

import requests
import re 
import os

proxy = 'http://localhost:8080'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

resp1 = requests.get("http://docker.hackthebox.eu:33664/")
#print(resp1.cookies)
print(resp1.headers)

"""

{'Date': 'Sun, 30 Jun 2019 12:14:31 GMT', 'Server': 'Apache/2.4.18 (Ubuntu)', 'Set-Cookie': 'PHPSESSID=k234akmenva3b507tptlpcsrd6; path=/', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate', 'Pragma': 'no-cache', 'Vary': 'Accept-Encoding', 'Content-Length': '388', 'Connection': 'close', 'Content-Type': 'text/html; charset=UTF-8'}

"""
header =

md5 = resp1.text[167:187]
param = "hash="+md5

mycookie = "PHPSESSID=lqreq6rd41kg0ins1fpuhr5ra"
for x in range(0,3):

    #resp = requests.get("http://docker.hackthebox.eu:33664/")

    rqst = requests.post("http://docker.hackthebox.eu:33664/", params=param)
    print(rqst.text)

    md5 = rqst.text[167:187]
    print(md5)

    param = "hash="+md5
    print(param)
