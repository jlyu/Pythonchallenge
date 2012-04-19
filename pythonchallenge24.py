import Image

def BFS(maze, path):
	dirs=[(0,1),(0,-1),(1,0),(-1,0)]
	wall=(255,)*4
	w,h=maze.size
	maze.putpixel((1,h-1),wall)
	maze.putpixel((w-2,0),wall)
	queue=[(1,h-2)] #enter
	path[queue[0]]='exit'
	while queue:
		pos=queue.pop(0)
		for d in dirs:
			new_pos=(pos[0]+d[0], pos[1]+d[1])
			if not path.has_key(new_pos) and maze.getpixel(new_pos)!=wall:
				path[new_pos]=pos
				queue.append(new_pos)
				
maze=Image.open('C:\\Python27\\pythonchallenge\\maze.png')
path={}
BFS(maze,path)
maze.show()
#print path
w=maze.size[0]
pos=(w-2,1)
while pos!='exit':
	maze.putpixel(pos,(0,0,255,255))
	pos=path[pos]
maze.show()