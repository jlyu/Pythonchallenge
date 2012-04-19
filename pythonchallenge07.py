import Image,re

im=Image.open('C:\\Python27\\pythonchallenge\\oxygen.png')
pixel = [im.getpixel((x,im.size[1]/2)) for x in range(0, im.size[0], 7)]
mash=[r for r,g,b,a in pixel if r==g==b]
print ''.join(map(chr, map(int, re.findall(r'\d{3}', ''.join(map(chr, mash))))))
