# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Count: '))
pos = int(input('Position: '))


for i in range(count):
	if i == 0: html = urllib.request.urlopen(url, context=ctx).read()
	else: html = urllib.request.urlopen(tags[pos-1].get('href', None), context=ctx).read()

	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')

print(tags[pos-1].contents[0])