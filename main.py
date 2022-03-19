#from genericpath import isfile
import pyautogui
import keyboard
import random
import time

fishCought = 0

def CheckBoxOfPixelsForGivenColorForGivenRange(x, y, r, g, b, tol):
    for i in range(0,4):
        for j in range(0,4):
            if pyautogui.pixelMatchesColor(x+j, y+i, (r, g, b), tolerance=tol):
                return 1
    return 0

i = 0
while True:
    if pyautogui.pixelMatchesColor(960, 480, (245, 200, 122), tolerance=20):
        fishCought+=1
        i += 1
        print(fishCought)
        time.sleep(0.1 + random.uniform(0.0,0.3))
        keyboard.press_and_release('e')
        time.sleep(6.5 + random.uniform(0.0,0.3))
        keyboard.press_and_release('e')
    #if pyautogui.pixelMatchesColor(910, 925, (0, 0, 0), tolerance=5):
    #    sys.exit("rod about to break, stopping program, fish cought: "+ str(fishCought))
    # screenshot = pyautogui.screenshot()
    # screenshot.save(str(i)+".png")

    if CheckBoxOfPixelsForGivenColorForGivenRange(1045, 520, 115, 220, 4, 20):
        time.sleep(1 + random.uniform(0.0,0.1))
        keyboard.press_and_release('e')
    elif CheckBoxOfPixelsForGivenColorForGivenRange(820, 788, 180,180,1, 40):
        time.sleep(1 + random.uniform(3.0,3.1))
        print("huj")
        keyboard.press_and_release('e')

    time.sleep(0.1)




