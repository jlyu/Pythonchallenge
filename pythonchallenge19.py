import base64,wave,array

file=open('C:\\Python27\\pythonchallenge\\19')
a=array.array('c',base64.b64decode(file.read()))
a.byteswap()
file.close()
wav=wave.open('C:\\Python27\\pythonchallenge\\indian.wav','wb')
wav.setnchannels(1)
wav.setsampwidth(1)
wav.setframerate(22050)
wav.writeframes(a.tostring())
wav.close()