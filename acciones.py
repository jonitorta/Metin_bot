import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision
import pydirectinput




def subirse_caballo():
    pydirectinput.keyDown("ctrl")
    pydirectinput.press("h")
    pydirectinput.keyUp("ctrl")

def cancelar_habilidad(habilidad):
    subirse_caballo()
    time.sleep(.2)
    pydirectinput.press(habilidad)
    time.sleep(.5)
    subirse_caballo()
    time.sleep(.2) 

def voltear_camara():
    pydirectinput.keyDown("q")
    time.sleep(2)
    pydirectinput.keyUp("q")

def checar_muerte():
    wincap = WindowCapture() 
    vision_muerte = Vision('muerte.png')

def buscar(imagen,tolerancia,des):
    wincap = WindowCapture() 
    vision_limestone = Vision(imagen)
    screenshot = wincap.get_screenshot()
    rectangles = vision_limestone.find(screenshot,tolerancia)
    output_image=vision_limestone.draw_rectangles(screenshot,rectangles)
    point=vision_limestone.get_click_points(rectangles)
    if len(rectangles)>0:
        pydirectinput.click(point[0][0],point[0][1]+des)
    else :
        return 0

def matar_metin(ataque,movimiento,metin,contador,tolerancia=.8):
    point=buscar(metin,tolerancia)
    if point!=0:
        pydirectinput.press("z")
        pydirectinput.click(point[0][0],point[0][1])
        time.sleep(movimiento)
        pydirectinput.keyDown("space")
        time.sleep(ataque)
        pydirectinput.keyUp("space")
        pydirectinput.press("z")
        contador=0

    else:
        if contador==0:
            voltear_camara()
            contador+=1
            matar_metin(ataque,movimiento,metin,contador,tolerancia=.8)
        if contador==1:
            pydirectinput.keyDown("s")
            time.sleep(1.5)
            pydirectinput.keyUp("s")
            contador+=1
            matar_metin(ataque,movimiento,metin,contador,tolerancia=.8)
        if contador>=3:
            pydirectinput.press("z")
            pydirectinput.keyDown("s")
            pydirectinput.keyDown("q")
            time.sleep(1.5)
            pydirectinput.keyUp("s")
            pydirectinput.press("z")
            pydirectinput.keyUp("q")





