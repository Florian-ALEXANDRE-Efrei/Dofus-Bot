import pynput.mouse
from pynput import mouse
from pynput.mouse import Controller, Button
import time
import keyboard
from PIL import Image
import PIL.ImageGrab
import colorama
from colorama import Fore
from colorama import Style

mouse = Controller()

def DoAClick(x,y):
    mouse.position = (x,y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

#and PIL.ImageGrab.grab().load()[round(638 * 1.25), round(445 * 1.25)]==(3, 3, 0)
def WeAreInChargingScreen():
    if PIL.ImageGrab.grab().load()[round(636 * 1.25), round(445 * 1.25)] == (3, 3, 0) :
        return True
    else : return False

def GoRight():
    mouse.position = (1182, 429)
    mouse.press(Button.left)
    mouse.release(Button.left)
    compteur = 0
    while WeAreInChargingScreen() == False:
        if WeAreInChargingScreen(): break
        compteur = compteur + 1
        if compteur % 50 == 0:
            mouse.position = (1182, 429)
            mouse.press(Button.left)
            mouse.release(Button.left)


def GoUp():
    mouse.position = (664, 46)
    mouse.press(Button.left)
    mouse.release(Button.left)
    compteur = 0
    while WeAreInChargingScreen() == False:
        if WeAreInChargingScreen(): break
        compteur = compteur + 1
        if compteur % 50 == 0:
            mouse.position = (664, 46)
            mouse.press(Button.left)
            mouse.release(Button.left)


def GoLeft():
    mouse.position = (72, 477)
    mouse.press(Button.left)
    mouse.release(Button.left)
    compteur = 0
    while WeAreInChargingScreen() == False:
        if WeAreInChargingScreen(): break
        compteur = compteur + 1
        if compteur % 50 == 0:
            mouse.position = (72, 477)
            mouse.press(Button.left)
            mouse.release(Button.left)


def GoDown():
    mouse.position = (689, 794)
    mouse.press(Button.left)
    mouse.release(Button.left)
    compteur = 0
    while WeAreInChargingScreen() == False:
        if WeAreInChargingScreen(): break
        compteur = compteur + 1
        if compteur % 50 == 0:
            mouse.position = (689, 794)
            mouse.press(Button.left)
            mouse.release(Button.left)


def WePassALevelCheck():
    if PIL.ImageGrab.grab().load()[round(557*1.25), round(391*1.25)]==(46, 45, 40) and PIL.ImageGrab.grab().load()[round(554*1.25), round(470*1.25)]==(46, 45, 40) and PIL.ImageGrab.grab().load()[round(930*1.25), round(393*1.25)]==(46, 45, 40) and PIL.ImageGrab.grab().load()[round(924*1.25), round(463*1.25)]==(46, 45, 40) and PIL.ImageGrab.grab().load()[round(804*1.25), round(482*1.25)]==(197, 240, 86) and PIL.ImageGrab.grab().load()[round(705*1.25), round(482*1.25)]==(197, 240, 86):
        return True
    else :
        return False

def GetPosition():
    fichier = open("Position.txt", "a")
    while 1:
        print(mouse.position)
        if keyboard.is_pressed("s"):break
        if keyboard.is_pressed("p"):
            fichier.write("\n"+str(mouse.position))
            time.sleep(1)  # Sleep for 3 seconds
    fichier.close()

def Moving():
    while 1:
        if keyboard.is_pressed("m"):break
        if keyboard.is_pressed("q"):
            GoLeft()
            time.sleep(0.1)  # Sleep for 3 seconds
        elif keyboard.is_pressed("z"):
            GoUp()
            time.sleep(0.1)  # Sleep for 3 seconds
        elif keyboard.is_pressed("d"):
            GoRight()
            time.sleep(0.1)  # Sleep for 3 seconds
        elif keyboard.is_pressed("s"):
            GoDown()
            time.sleep(0.1)  # Sleep for 3 seconds

tours = 0
"""
while 1:
    print("Nombre de tour : ",tours)
    print("MAP [10,1]")
    DoAClick(150, 340)
    DoAClick(111, 396)
    DoAClick(382, 379)
    DoAClick(764, 570)
    DoAClick(806, 589)
    DoAClick(804, 627)
    DoAClick(804, 666)
    DoAClick(729, 666)
    DoAClick(919, 763)

    time.sleep(120)

    if WePassALevelCheck():
        print("We Pass A Level")
        DoAClick(754, 482)

    GoDown()
    time.sleep(0.5)

    print("MAP [10,2]")
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

    time.sleep(130)
    if WePassALevelCheck():
        print("We Pass A Level")
        DoAClick(754, 482)

    GoDown()
    time.sleep(0.5)

    print("MAP [10,3]")
    DoAClick(1078, 148)
    DoAClick(1000, 187)
    DoAClick(997, 222)

    time.sleep(40)
    if WePassALevelCheck():
        print("We Pass A Level")
        DoAClick(754, 482)

    GoRight()
    time.sleep(0.5)

    print("MAP [11,3]")

    DoAClick(304, 304)
    DoAClick(535, 494)
    DoAClick(574, 512)
    DoAClick(962, 592)

    time.sleep(50)
    if WePassALevelCheck():
        print("We Pass A Level")
        DoAClick(754, 482)

    GoDown()
    time.sleep(0.5)
    print("MAP [11,4]")
    GoRight()
    time.sleep(0.5)
    print("MAP [12,4]")
    GoUp()
    time.sleep(0.5)
    print("MAP [12,3]")


    DoAClick(227, 264)
    DoAClick(574, 358)
    DoAClick(767, 454)
    DoAClick(846, 454)
    DoAClick(922, 457)
    DoAClick(148, 610)
    DoAClick(189, 630)

    time.sleep(80)
    if WePassALevelCheck():
        print("We Pass A Level")
        DoAClick(754, 482)
        
    GoDown()
    time.sleep(0.5)
    print("MAP [12,4]")
    GoLeft()
    time.sleep(0.5)
    print("MAP [11,4]")
    GoLeft()
    time.sleep(0.5)
    print("MAP [10,4]")
    GoUp()
    time.sleep(0.5)
    print("MAP [10,3]")
    GoUp()
    time.sleep(0.5)
    print("MAP [10,2]")
    GoUp()
    time.sleep(0.5)
    print("MAP [10,1]")

    tours+=1
"""

# haut à gauche (6, 38)
# bas à gauche (6, 808)
# bas à droite (1195, 810)
# haut à droite (1195, 37)
#print(PIL.ImageGrab.grab().load()[round(1198 * 1.25), round(33 * 1.25)])
"""
FirstPoint=[147,786]
x=FirstPoint[0]
y=FirstPoint[1]
for n in range (1,15):
    print(n," => x = ",x," => ",PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)])
    x+=77
FirstPoint[0]-=38
FirstPoint[1]-=18
x=FirstPoint[0]
y=FirstPoint[1]
print(FirstPoint)
for n in range (1,15):
    print(n," => x = ",x," => ",PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)])
    x+=77

"""

Tab = [['0' for x in range(14)] for i in range(40)]

FirstPoint=[147,786]
for i in range(0,40):
    #print("\n--------------- Ligne ",i+1," ---------------\n")
    print("chargement ", ((i + 1) * 100) / 40, "%")
    x = FirstPoint[0]
    y = FirstPoint[1]
    for j in range (0,14):
        Tab[abs(i-39)][j]=PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]
        """
        #print(j+1," => x = ",x," => ",PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)])
        if PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (129, 118, 86) or \
                PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (147, 135, 98):
            Tab[abs(i-39)][j]="0"
            print(" =>  zone de jeu")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (91, 83, 61):
            Tab[abs(i-39)][j]="M"
            print(" =>  mur")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (0, 0, 0):
            Tab[abs(i-39)][j]="V"
            print(" =>  vide")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (193, 49, 35) or \
                PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (189, 46, 33):
            Tab[abs(i-39)][j]="J"
            print(" =>  zone pour joueur")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (25, 126, 204) or \
                PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (29, 129, 206):
            Tab[abs(i-39)][j]="E"
            print(" =>  zone pour ennemie")
        else :
            Tab[i][j]="A"
            print(" =>  indescriptible")
        #print("ligne : ",i+1," / Colonne : ",j+1)
        """
        """
        mouse.position = (x, y)
        
        if PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (129, 118, 86) or \
                PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (147, 135, 98):
            print(PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]," =>  zone de jeu")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (91, 83, 61):
            print(PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]," =>  mur")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (0, 0, 0):
            print(PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]," =>  vide")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (193, 49, 35):
            print(PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]," =>  zone pour joueur")
        elif PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)] == (98, 66, 123):
            print(PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]," =>  zone pour ennemie")
        else:
            print(PIL.ImageGrab.grab().load()[round(x * 1.25), round(y * 1.25)]," =>  indescriptible")
        """
        """
        press = False
        while press == False:
            if keyboard.is_pressed("p"):
                press = True
            else:
                continue
        """
        if keyboard.is_pressed("s"): break
        #time.sleep(0.01)
        x+=77

    if i%2==0 :
        FirstPoint[0] -= 38
        FirstPoint[1] -= 19
    else :
        FirstPoint[0] += 38
        FirstPoint[1] -= 19




def AfficherTableau(Tab):
    for n in range(0, 40):
        if n % 2 != 0:
            Tab[n].reverse()
            Tab[n].append('')
            Tab[n].reverse()
        else:
            Tab[n].append('')

    colorama.init()
    for i in range(0,40):
        print("")
        for j in range(0,15):
            """
            if Tab[i][j]=="J" :
                print("[",Fore.BLUE + Style.BRIGHT + Tab[i][j] + Style.RESET_ALL,"]",end="")
            elif Tab[i][j]=="E":
                print("[", Fore.RED + Style.BRIGHT + Tab[i][j] + Style.RESET_ALL, "]", end="")
            elif Tab[i][j]=="M":
                print("[", Fore.YELLOW + Style.BRIGHT + Tab[i][j] + Style.RESET_ALL, "]", end="")
            elif Tab[i][j]=="V":
                print("[", Fore.BLACK + Style.BRIGHT + Tab[i][j] + Style.RESET_ALL, "]", end="")
            elif Tab[i][j]=="0":
                print("[", Fore.WHITE + Style.BRIGHT + Tab[i][j] + Style.RESET_ALL, "]", end="")
            else :
                print("[ A ]",end="")
            """
            if Tab[i][j] == (129, 118, 86) or Tab[i][j] == (147, 135, 98): #case vide
                print(" ", Fore.WHITE + Style.BRIGHT + "◊" + Style.RESET_ALL, " ", end="")
            elif Tab[i][j] == (91, 83, 61): # Mur
                print(" ", Fore.YELLOW + Style.BRIGHT + "◊" + Style.RESET_ALL, " ", end="")
            elif Tab[i][j] == (0, 0, 0): # Vide
                print(" ", Fore.BLACK + Style.BRIGHT + "◊" + Style.RESET_ALL, " ", end="")
            elif Tab[i][j] == (193, 49, 35) or Tab[i][j] == (189, 46, 33): # place pour le joueur
                print(" ",Fore.BLUE + Style.BRIGHT + "◊" + Style.RESET_ALL," ",end="")
            elif Tab[i][j] == (25, 126, 204) or Tab[i][j] == (29, 129, 206): # place pour les ennemies
                print(" ",Fore.RED + Style.BRIGHT + "◊" + Style.RESET_ALL," ", end="")
            elif Tab[i][j] == '':  # pour la beaute du tab
                print("  ", end="")
            else:
                print("  ◊  ",end="")
AfficherTableau(Tab)

# case vide : (129, 118, 86) ou (147, 135, 98)
# obstacle : (91, 83, 61)
# vide : (0, 0, 0)
# place pour le joueur : (193, 49, 35)
# place pour les ennemies : (98, 66, 123)
