import Image
im=Image.open('C:\\Python27\\pythonchallenge\\mozart.gif')#640*480 
for height in range(im.size[1]):
	line=[im.getpixel((width,height)) for width in range(im.size[0])]
	#This is a GIF image, and thus uses a palette; the pink pixels are color #195
	pink=line.index(195)
	line=line[pink:]+line[:pink]
	[im.putpixel((width,height),pixel) for width,pixel in enumerate(line)]
im.show()
