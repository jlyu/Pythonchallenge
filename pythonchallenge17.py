import cookielib,urllib,urllib2, re,bz2,xmlrpclib
from urllib2 import Request
from urllib import quote_plus
#a chain of problem4,13,

cj=cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
res = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
#print cj
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
seed='12345'
info=''
while 1:
	req=urllib.urlopen(url+seed)
	content=req.read()
	seed=''.join(re.findall(r"busynothing is (\d+)", content))
	cookies=req.info().getheaders('Set-Cookie')[0]
	#print cookies
	byte=cookies.split(';')[0].split('=')[1]
	info+=byte
	try:
		int(seed)
		print "Info:",byte,"	Next:",seed
	except:
		print "Info:",byte,"	Last:",content
		break
#print info
print "info:",bz2.decompress(urllib.unquote_plus(info))

'''
info: is it the 26th already? call his father and inform him that "the flowers a
re on their way". he'll understand.
'''

server=xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('Leopold')

inform='the flowers are on their way'
url='http://www.pythonchallenge.com/pc/stuff/violin.php'
req=Request(url,headers={'Cookie' :'info='+quote_plus(inform)})
print urllib2.urlopen(req).read()
#oh well, don't you dare to forget the balloons.


