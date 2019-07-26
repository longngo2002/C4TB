import datetime
import pyglet
print("Nhap thoi gian bao thuc:")
print("Example:06:30:00")
a = input()
stop = False
while stop == False:
    b = str(datetime.datetime.now().time())
    print(b)
    if b > a :
        stop = True
        music = pyglet.resource.media('sample.wav')
        music.play()
        pyglet.app.run()