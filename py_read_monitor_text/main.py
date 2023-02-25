from platform import python_version_tuple
import re
import cv2
import pytesseract
import pyautogui as pag
from pynput.mouse import Button, Controller 
import pynput

if __name__ == "__main__":

    # 1. how to detect 
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

    ADDR = [
        'img1.png',
        'img2.png',
        'img3.png',
    ]

    # for a in ADDR:
    #     img = cv2.imread(a)
    #     txt = pytesseract.image_to_string(img)
        
    #     res = 'not yet!'
    #     for t in txt.split('\n'):
    #         if re.match(r'Started at [\d-]+ [\d:]+ and completed', t):
    #             res = t
        
    #     print(res)
        
    # 2. goto and click
    # goto = pag.locateOnScreen('goto.png')
    # pag.moveTo(goto)
    # pag.rightClick()
    
    # goto2 = pag.locateOnScreen('goto2.png')
    # pag.moveTo(goto2)
    # pag.rightClick()
    
    pag.screenshot('shot.png', region=(0,0,300,400))
    # print(help(pag.screenshot))