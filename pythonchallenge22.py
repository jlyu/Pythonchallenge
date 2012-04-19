import Image,ImageSequence
import turtle, time
im=Image.open("C:\\Python27\\pythonchallenge\\white.gif")
locations=[]
for frame in ImageSequence.Iterator(im):
	data=list(frame.getdata())
	index=data.index(8)
	y,x=divmod(index,200)
	locations.append((x,y))
#print locations
EXP=2
x=y=0 
for pilx,pily in locations:
	dx=(pilx-100)//2
	dy=(100-pily)//2
	x+=dx*EXP
	y+=dy*EXP
	turtle.goto(x,y)
	if dx==dy==0:
		time.sleep(1)
		turtle.reset()
		x=y=0