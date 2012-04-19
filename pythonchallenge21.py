import zlib, bz2
reverse=lambda x:x[::-1]
reverse.__module__='reverse'
decompressors=[zlib.decompress,bz2.decompress, reverse]
step=True
last=None
logs=[]
data=open("package.pack",'rb').read()
while step:
    step=False
    for decompress in decompressors:
        try:
            if last==decompress.__module__ in ('reverse',): raise Exception()
            data=decompress(data)
            step=True
            last=decompress.__module__
            logs.append((len(data),last))
            #print last
            break
        except:
            pass
mark=dict(zlib='.',bz2='*',reverse='\r\n')
print "".join([mark[log[1]] for log in logs])

cj=cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
res = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
#print cj