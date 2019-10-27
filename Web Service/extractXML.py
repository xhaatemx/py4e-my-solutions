import ssl
import urllib.error, urllib.request, urllib.parse
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

Sum = 0
# enter the url
url = input('Enter url - ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_313861.xml'
# return data from the url request
data = urllib.request.urlopen(url, context=ctx).read()
xmlTree = ET.fromstring(data)
lst = xmlTree.findall('.//count')

# Extract each count in the list and add to Sum
for e in lst:
	Sum += int(e.text)

print(Sum)

