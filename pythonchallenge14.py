import Image

im=Image.open('C:\\Python27\\pythonchallenge\\wire.png')
new=Image.new(im.mode,(100,100))
seq=[x/2 for x in range(200,0,-1)]


for edge in range(len(seq)): #index 0-199
	for pixel in range(seq[edge]):
		if(100-seq[edge])%2==0:
			x=pixel+(100-seq[edge])/2
		else:
			x=pixel+(100-seq[edge])/2+1
		y=edge//4
		new.putpixel((x,y),im.getpixel((sum(seq[:edge])+pixel,0)))
	new=new.rotate(90)
new.show()
