import zipfile,re,urllib

name='90052'
suffix='.txt'
'''
with zipfile.ZipFile('C:\\Python27\\pythonchallenge\\channel.zip', 'r') as myzip:
	while True:
		content = myzip.open(name+suffix,'r').read()
		name="".join(re.findall(r'nothing is (\d+)$', content)) #name = z.read(name).split()[-1] + '.txt'
		if not name:
			print content
			break
'''
comments=[]
with zipfile.ZipFile('C:\\Python27\\pythonchallenge\\channel.zip', 'r') as myzip:
	while True:
		try:
			comments.append(myzip.getinfo(name+suffix).comment)
			content = myzip.open(name+suffix,'r').read()
			name="".join(re.findall(r'nothing is (\d+)$', content))
		except:
			print ''.join(comments)
			break
	

'''
f = file('comments.txt', 'r').read()
list = re.split(r'[^a-zA-Z]',f)
for word in list:
	if word:
		url = 'http://www.pythonchallenge.com/pc/def/'+word+'.html'
		data = urllib.urlopen(url).read()
		print data+'\r\n'
'''