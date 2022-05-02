import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision
import pydirectinput

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
def subirse_caballo():
    pydirectinput.keyDown("ctrl")
    pydirectinput.press("h")
    pydirectinput.keyUp("ctrl")

def bajarse_caballo():
    pydirectinput.keyDown("ctrl")
    pydirectinput.press("h")
    pydirectinput.keyUp("ctrl")


def letras(letra,numero):
    for i in range(numero):
        pydirectinput.press(letra)

        
def cancelar_habilidad(habilidad):
    bajarse_caballo()
    time.sleep(.3)
    pydirectinput.press(habilidad)
    time.sleep(.3)
    subirse_caballo()
    time.sleep(.3)

def voltear_camara():
    pydirectinput.keyDown("q")
    time.sleep(2)
    pydirectinput.keyUp("q")
time.sleep(3)
for i in range(500000):
    if i%30==0:
        cancelar_habilidad("1")
        cancelar_habilidad("2")
        cancelar_habilidad("3")
        cancelar_habilidad("1")
        pydirectinput.click()
        
    pydirectinput.press("4")
    pydirectinput.press("z")
    pydirectinput.keyDown("space")
    time.sleep(15)
    pydirectinput.keyUp("space")
    pydirectinput.press("z")