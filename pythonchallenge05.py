import cPickle as p

content = p.load(file('banner.p'))
f=file('result.txt','w')
for line in content:
	f.write(''.join(map(lambda x:x[0]*x[1], line))+'\r\n')
f.close()
		