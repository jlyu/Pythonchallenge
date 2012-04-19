binary=open('C:\\Python27\\pythonchallenge\\evil2.gfx','rb').read()
[open('C:\\Python27\\pythonchallenge\\evil%d.jpg' %i,'wb').write(binary[i::5]) for i in range(5)]
