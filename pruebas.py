import cv2 as cv
import numpy as np
import acciones as ac
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



    screenshot_muerte = wincap.get_screenshot()
    rectangles_muerte = vision_muerte.find(screenshot_muerte, 0.70)
    output_image=vision_muerte.draw_rectangles(screenshot_muerte,rectangles_muerte)
    point_muerte=vision_muerte.get_click_points(rectangles_muerte)

    if len(rectangles_muerte)>0:
        pydirectinput.click(point_muerte[0][0],point_muerte[0][1]-90)
        subirse_caballo()
        pydirectinput.keyDown("s")
        time.sleep(2)
        pydirectinput.keyUp("s")
        time.sleep(2)
        checar_muerte()

wincap = WindowCapture() 
vision_limestone = Vision('pelota.jpg')


time.sleep(2)
historial=0 

  

for i in range(50000):
    pydirectinput.press("z")
    
    if i%10==0:
        checar_muerte()
    if i %100==0:
        cancelar_habilidad("1") 
        cancelar_habilidad("2")    
        
        
        
    screenshot = wincap.get_screenshot()
    rectangles = vision_limestone.find(screenshot, 0.80)
    output_image=vision_limestone.draw_rectangles(screenshot,rectangles)
    point=vision_limestone.get_click_points(rectangles)
   
   
         
    if len(rectangles)>0  :
        if (historial!=point[0][0]):
            pydirectinput.press("z")
            pydirectinput.click(point[0][0],point[0][1])
            pydirectinput.press("4")
            pydirectinput.press("z")
            time.sleep(2)
            pydirectinput.keyDown("space")
            time.sleep(1.4) 
            ac.buscar("pelota.jpg",.7)
            pydirectinput.press("z")
            pydirectinput.keyUp("space")
            pydirectinput.press("z")
            historial=point[0][0]
        else: 
            pydirectinput.press("z")
            pydirectinput.keyDown("s")
            pydirectinput.keyDown("q")
            time.sleep(1)
            pydirectinput.keyUp("s")
            pydirectinput.press("z")
            pydirectinput.keyUp("q")
            

    else:
        pydirectinput.press("z")
        pydirectinput.keyDown("s")
        pydirectinput.keyDown("q")
        time.sleep(1.5)
        pydirectinput.keyUp("s")
        pydirectinput.press("z")
        pydirectinput.keyUp("q")
            
         
    
    pydirectinput.press("z")
    
    


    

    

    
print('Done.')
