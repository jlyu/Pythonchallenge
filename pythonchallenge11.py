from PIL import Image, ImageEnhance
from cStringIO import StringIO

#url='http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'
#im=Image.open(StringIO(urllib.urlopen(url).read()))
cave=Image.open('C:\\Python27\\pythonchallenge\\cave.jpg')

#method 1
for h in range(cave.size[1]):
	for w in range(cave.size[0]):
		cave.putpixel((h//2,w//2),cave.getpixel((w,h)))
cave.show()

#method 2
cave.transform((cave.size[0]//2, cave.size[1]//2),
                         Image.AFFINE, (2,0,0,0,2,0)).show()
						 
#method 3

final=ImageEnhance.Brightness(cave)
final.enhance(8).show()
