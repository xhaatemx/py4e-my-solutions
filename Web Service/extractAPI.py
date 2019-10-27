import ssl
import urllib.parse as up, urllib.request as ur, urllib.error as ue
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input("Address: ")
if len(address) < 1: address = 'Payame Noor University'
serviceurl = "http://python-data.dr-chuck.net/geojson?"
url = serviceurl + up.urlencode({'address': address})

connection = ur.urlopen(url, context=ctx).read()
data = connection.decode()
try:
    js = json.loads(data)
except:
    js = None

if js is None or 'status' not in js or js['status'] != 'OK': print('error!!...Not Found :(')
else: print ("Place-ID:", js["results"][0]["place_id"])
