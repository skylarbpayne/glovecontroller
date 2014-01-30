#Author: Skylar Payne
#This file provides a demonstration of the glove project for Hacktech.io
#By Skylar Payne, Yvonne Fung, Max Camacho, and Allen Sallinger.

from GloveController import Glove
import win32api
import win32con
import math

glove = Glove(5)

while True:
    glove.update()
    x, y = win32api.GetCursorPos()

    if glove.thumbFlex > 1 and glove.middleFlex > 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
    elif glove.middleFlex > 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        
    elif glove.thumbFlex > 1:
        if glove.orientationX > 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, math.floor(-win32con.WHEEL_DELTA / 2), 0)
        elif glove.orientationX < 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, math.floor(win32con.WHEEL_DELTA / 2), 0)

    else:
        dy = glove.orientationX
        dx = glove.orientationY

##        sz = (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
##
##        if dx > 0:
##            x = x + 20 * (sz[0] - x) * dx // sz[0]
##        else:
##            x = x + 20 * x * dx // sz[0]
##        if dy > 0:
##            y = y + 20 * (sz[1] - y) * dy // sz[1]
##        else:
##            y = y + 20 * y * dy // sz[1]
            
        x = x + 9 * dx
        y = y + 9 * dy

        win32api.SetCursorPos((x, y))

##    if glove.indexFlex > 1:
##        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
##        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
##
##    elif glove.middleFlex > 1:
##        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
##        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
##
##    if glove.indexFlex > 1 and glove.thumbFlex > 1 and glove.middleFlex > 1:
##        break
##    else:
        print(glove.thumbFlex)
        
