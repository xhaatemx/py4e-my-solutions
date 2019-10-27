import ssl
import json
import urllib.error, urllib.request, urllib.parse


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

Sum = 0
# enter the url
url = input('Enter url - ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_313862.json'

# return data from the url request
data = urllib.request.urlopen(url, context=ctx).read()

jObject = json.loads(data)

# extract each count using json lst object
for e in jObject['comments']:
	Sum += int(e['count'])

print(Sum)

