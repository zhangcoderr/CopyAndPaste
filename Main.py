# coding=utf-8
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time
import pyHook
import pythoncom
import xlrd
import pyperclip
from pynput import mouse, keyboard
import re
import xml.dom.minidom


def copy():
    k.press_key(k.control_l_key)
    k.tap_key("c")
    k.release_key(k.control_l_key)

def tapkey(key, count=1):
    for i in range(0, count):
        k.tap_key(key)
        time.sleep(0.05)
def Paste_Ch(string):
    pyperclip.copy(string)
    time.sleep(0.05)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)

def getCopy1(noresult=None,maxTime=1.3,isDone=False):
    # maxTime = 3  # 3秒复制 调用copy() 不管结果对错
    if(maxTime<=0 or isDone):
        return noresult
    pyperclip.copy('')
    time.sleep(0.3)
    # print('doing')
    copy()
    result = pyperclip.paste()
    if(result==''):
        return getCopy(noresult,maxTime-0.3,False)
    else:
        return getCopy(result,maxTime-0.3,True)

    #print('debug:'+str(result))
    return result
def getCopy(maxTime=1.6):
    # maxTime = 3  # 3秒复制 调用copy() 不管结果对错
    while (maxTime > 0):
        maxTime = maxTime - 0.5
        time.sleep(0.5)
        # print('doing')
        copy()
        m.move(0,0)
    result = pyperclip.paste()
    return result


def onpressed(key):
   # print(key)
    #if (key == keyboard.Key.caps_lock):

    if(key in keyboard.Key):
        #print(key)

        if (key == keyboard.Key.caps_lock):  # ctrl+---------
            if (len(copylist) == 0):
                return

            Paste_Ch(copylist[0])

            copylist.pop(0)
            print('剩下：')
            print(copylist)
        return

    if (key.char == '\x03'):
        print(1111111)
        time.sleep(0.2)
        # co= getCopy()
        co = pyperclip.paste()

        copylist.append(co)
        print(copylist)


copylist=[]
k = PyKeyboard()
m = PyMouse()

print('start')
with keyboard.Listener(on_press=onpressed) as listener:
    listener.join()