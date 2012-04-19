''' 
dict={}
 
file = open('03.txt','r')
while True:
	line = file.readline()
	lineLen = len(line)
	if lineLen==0:
		break
	for i in range(0, lineLen):
		dict[line[i]] = 0
file.close()

file = open('03.txt','r')
while True:
	line = file.readline()
	lineLen = len(line)
	if lineLen==0:
		break
	for i in range(0, lineLen):
		dict[line[i]] += 1
file.close()

print dict
'''

s = ''.join([line.rstrip() for line in open('02.txt')]) #声明字符串s读入文件全部内容，对空格换行做处理
OCCURRENCES = {}                                        #声明字典
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1  #对S中每一个字符c处理，已存在字典中+1，初始化0
avgOC = len(s) // len(OCCURRENCES)       				#除法取整 97545//24
print ''.join([c for c in s if OCCURRENCES[c] < avgOC]) #再次遍历s,字符如果在字典中出现次数小于平均，join             
# equality