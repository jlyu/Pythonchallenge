'''
import re
curr = '1'
for each in range(30):
	curr = "".join([str(len(k+y))+k  for k,y in re.findall(r"(\d)(\1*)",curr)])
print len(curr)
'''





a = ['1', '11', '21', '1211', '111221']

while len(a)<=30:
	s = a[-1] 
	next=''
	for i in range(len(s)-1):
		next += s[i]
		if s[i]<>s[i+1]:
			next += '#'
	next += s[-1]
	nextword=''
	for group in next.split('#'):
		nextword += str(len(group))+group[0]
	a.append(nextword)
print len(a[-1])


	