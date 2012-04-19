import urllib,re
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
suffix=pre_suffix='12345'
for i in range(400):
	data = urllib.urlopen(url+suffix).read()
	suffix="".join(re.findall(r'\D[g-z]{7}\D[i|s]{2}\D(\d+)$', data))
	if not suffix:
		suffix = str(int(pre_suffix) / 2)
		print url + suffix
	pre_suffix = suffix