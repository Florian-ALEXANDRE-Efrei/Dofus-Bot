import pynput.mouse
from pynput import mouse
from pynput.mouse import Controller, Button
import time
import keyboard
from PIL import Image
import PIL.ImageGrab

mouse = Controller()

def DoAClick(x,y):
    mouse.position = (x,y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

def GoRight():
    DoAClick(1182, 429)
    time.sleep(20)
def GoUp():
    DoAClick(664, 46)
    time.sleep(20)
def GoLeft():
    DoAClick(72, 477)
    time.sleep(20)
def GoDown():
    DoAClick(689, 794)
    time.sleep(20)





def GetPosition():
    fichier = open("Position.txt", "a")
    while 1:
        print(mouse.position)
        if keyboard.is_pressed("s"):break
        if keyboard.is_pressed("p"):
            fichier.write("\n"+str(mouse.position))
            time.sleep(1)  # Sleep for 3 seconds
    fichier.close()

#MAP [6,-2]
"""
DoAClick(150,763)
time.sleep(2) # Sleep for 3 seconds
DoAClick(265,742)
time.sleep(2) # Sleep for 3 seconds
DoAClick(422,704)
time.sleep(2) # Sleep for 3 seconds
DoAClick(497,667)
time.sleep(2) # Sleep for 3 seconds
DoAClick(726,704)
time.sleep(2) # Sleep for 3 seconds
DoAClick(769,764)
time.sleep(2) # Sleep for 3 seconds
DoAClick(919,803)

while 1:
    #MAP [10,1]
    DoAClick(150, 340)
    DoAClick(111, 396)
    DoAClick(382, 379)
    DoAClick(764, 570)
    DoAClick(806, 589)
    DoAClick(804, 627)
    DoAClick(804, 666)
    DoAClick(729, 666)
    DoAClick(919, 763)

    time.sleep(100)
    GoDown()

    DoAClick(843, 109)
    DoAClick(882, 165)
    DoAClick(958, 279)
    DoAClick(919, 299)
    DoAClick(920, 378)
    DoAClick(766, 415)
    DoAClick(805, 434)
    DoAClick(689, 494)
    DoAClick(767, 531)
    DoAClick(732, 629)
    DoAClick(764, 649)
    DoAClick(803, 590)
    DoAClick(845, 610)
    DoAClick(958, 667)

    time.sleep(100)
    GoDown()


    DoAClick(1078, 148)
    DoAClick(1000, 187)
    DoAClick(997, 222)

    time.sleep(100)
    GoRight()


    DoAClick(304, 304)
    DoAClick(535, 494)
    DoAClick(574, 512)
    DoAClick(962, 592)

    time.sleep(100)
    GoDown()
    GoRight()
    GoUp()


    DoAClick(227, 264)
    DoAClick(574, 358)
    DoAClick(767, 454)
    DoAClick(846, 454)
    DoAClick(922, 457)
    DoAClick(148, 610)
    DoAClick(189, 630)

    time.sleep(100)
    GoDown()
    GoLeft()
    GoLeft()
    GoUp()
    GoUp()
    GoUp()


while 1:
    rgb = PIL.ImageGrab.grab().load()[mouse.position[0],mouse.position[1]]
    if keyboard.is_pressed("s"):
        print(rgb)
        time.sleep(1)

print(PIL.ImageGrab.grab().load()[588, 450])
print(PIL.ImageGrab.grab().load()[770, 450])
print(PIL.ImageGrab.grab().load()[948, 450])
print(PIL.ImageGrab.grab().load()[1136, 450])


value = PIL.ImageGrab.grab().load()[200, 450]
for i in range(588, 1200):
    print(PIL.ImageGrab.grab().load()[588, i],"à la position : ",i)
"""
# sur l'axe x : changement à 383 -> 384
# sur l'axe y : changement à 899 -> 900


print(PIL.ImageGrab.grab().load()[400*0.8, 500*0.8])
print(PIL.ImageGrab.grab().load()[383*0.8, 450*0.8])

# sur l'axe x : changement à 306 -> 307
# sur l'axe y : changement à 719 -> 720