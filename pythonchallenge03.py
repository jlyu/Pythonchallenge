
import re
content = ''.join([line.rstrip() for line in open('03.txt')])
print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content))
#print (''.join(x[3:4] for x in re.findall(patten,content)))
