

from unicodedata import name
import pyautogui as pag
from pynput.mouse import Button, Controller


mouse = Controller()

if __name__ == "__main__":
    
    print('mouse position: ', mouse.position)
    mouse.move(100,10)
    mouse.press(Button.right)
    mouse.release(Button.right)
    
    print(pag.position())
    pag.moveTo(10,10)
    pag.rightClick()
    
    