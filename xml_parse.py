import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = ' http://py4e-data.dr-chuck.net/comments_1001839.xml'

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = sum((int(i.text) for i in counts))
print('Sum: ',sum)
