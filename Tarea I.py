# For Python 3.0 and later
import urllib.request
import urllib.parse
import re
    
"""
try:
    url = 'http://www.telcom.es/~gacias/naveg/iataicao.html'
    headers = {}
    headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    req=urllib.request.Request(url,headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))



etiqueta = '</strong><br>'


where True:
"""

url = 'http://pythonprograming.net'
values = {'s':'basics','submit':'search'}
data= urllib.parse.rlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)



