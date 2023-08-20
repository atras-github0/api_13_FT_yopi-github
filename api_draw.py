import sys
from mine import *
from PIL import Image
import cv2
import numpy as np
import os
from tkinter import filedialog
import time

search_posx = 150
search_posy = 150
mc = Minecraft()
mc.postToChat("A")
def getargv():
    length = len(sys.argv)
    if length == 1:
        filename = filedialog.askopenfilename()
        size_X = "100"
        size_Y = "100"
    elif length == 2:
        filename = filedialog.askopenfilename()
        size_X = sys.argv[1]
        size_Y = sys.argv[1]
    elif length == 3:
        filename = filedialog.askopenfilename()
        size_X = sys.argv[1]
        size_Y = sys.argv[2]

    #print(filename)
    if filename.endswith('.mp4') or filename.endswith('.wav'):
        cap = cv2.VideoCapture(filename)
        posx = mc.player.getPos().x
        posy = mc.player.getPos().y
        posz = mc.player.getPos().z
        video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        video_len_sec = video_frame_count / fps
        for i in range(round(video_len_sec * 2)):
            if not cap.isOpened():
                return
            cap.set(cv2.CAP_PROP_POS_FRAMES, round(fps * (i + 1)) / 2)
            ret, frame = cap.read()
            img2 = cv2.resize(frame,(int(size_X),int(size_Y))) 
            img3 = cv2.flip(img2,1)
            #cv2.circle(img2,center=(search_posx,search_posy),radius=10,color=(255,255,255),thickness=3)
            #cv2.imwrite('img_point_'+str(search_posx)+'_'+str(search_posy)+'.jpg',img2)
            imghsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV_FULL)
            drawpicture(posx,posz,size_Y,size_X,imghsv)
            time.sleep(0.5)
    else:
        print(filename)
        img = cv2.imread(filename,cv2.IMREAD_COLOR)
        img2 = cv2.resize(img,(int(size_X),int(size_Y))) 
        img3 = cv2.flip(img2,1)
        #cv2.circle(img2,center=(search_posx,search_posy),radius=10,color=(255,255,255),thickness=3)
        #cv2.imwrite('img_point_'+str(search_posx)+'_'+str(search_posy)+'.jpg',img2)
        imghsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV_FULL)
        posx = mc.player.getPos().x
        posy = mc.player.getPos().y
        posz = mc.player.getPos().z
        drawpicture(posx,posz,size_Y,size_X,imghsv)
                #print("red")
            #if color != 0:
             #   print(f"{int(color)}:{int(saturation)}:{int(value)}")

    #check=np.zeros((256,256,3),np.uint8)
    #check[:,:]=imghsv[search_posy,search_posx]
    #check = cv2.cvtColor(check, cv2.COLOR_HSV2BGR)
    #cv2.imwrite('img_check_'+str(search_posx)+'_'+str(search_posy)+'.jpg',check)

def drawpicture(posx,posz,size_Y,size_X,imghsv):
    for x in range(int(size_Y)):
        for y in range(int(size_X)):
            color = imghsv[x,y,0]
            saturation = imghsv[x,y,1]
            value = imghsv[x,y,2]
            if value < 20:
                #print(f"{int(color)}:{int(saturation)}:{int(value)}")
                mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_BLACK)
                #print("white")
            elif saturation < 20 and not (color >= 158 and color < 173):
                if saturation < 10:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_WHITE)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.STONE)
            elif color >= 0 and color < 8:
                if value < 170 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_RED)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_RED)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_RED)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_RED)
                #print("red")
            elif color >= 8 and color < 23:
                if value < 240 and value > 190:
                    mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_WHITE)
                elif value <= 190 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_BROWN)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_BROWN)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_BROWN)
                else:
                    if saturation < 200:
                        mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_WHITE)
                    else:
                        mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_RED)
                #print("red")
            elif color >= 23 and color < 38:
                if value < 170 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_ORANGE)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_BROWN)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_BROWN)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_ORANGE)
                #print("red")
            elif color >= 38 and color < 53:
                if value < 170 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_YELLOW)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_ORANGE)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_BROWN)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_YELLOW)
                #print("red")
            elif color >= 53 and color < 61:
                if value < 170 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_LIME)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_LIME)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_GREEN)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_LIME)
                #print("red")
            elif color >= 61 and color < 90:
                if value < 170 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_GREEN)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_GREEN)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_GREEN)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_GREEN)
                #print("red")
            elif color >= 90 and color < 98:
                if value < 170 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_CYAN)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_CYAN)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_CYAN)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_CYAN)
                #print("red")
            elif color >= 98 and color < 113:
                if value < 160 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_LIGHT_BLUE)
                elif value <= 100 and value > 55:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_LIGHT_BLUE)
                elif value <= 55:
                    mc.setBlock(posx+x,0,posz+y,block.DIAMOND_BLOCK)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_LIGHT_BLUE)
                #print("red")
            elif color >= 113 and color < 128:
                if value < 160 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_BLUE)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_BLUE)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_BLUE)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_LIGHT_BLUE)
                #print("red")
            elif color >= 128 and color < 143:
                mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_LIGHT_GRAY)
                #print("red")
            elif color >= 143 and color < 158:
                if saturation < 50:
                    if saturation < 20:
                        mc.setBlock(posx+x,0,posz+y,block.WOOL_GRAY)
                    else:
                        mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_CYAN)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_PURPLE)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_PURPLE)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_POWDER_BLUE)
                #print("red")
            elif color >= 158 and color < 173:
                if saturation < 80:
                    if saturation < 20:
                        mc.setBlock(posx+x,0,posz+y,block.WOOL_GRAY)
                    else:
                        mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_CYAN)
                elif value < 160 and value > 100:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_MAGENTA)
                elif value <= 100 and value > 75:
                    mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_MAGENTA)
                elif value <= 75:
                    mc.setBlock(posx+x,0,posz+y,block.WOOL_PURPLE)
                else:
                    mc.setBlock(posx+x,0,posz+y,block.HARDENED_CLAY_STAINED_LIGHT_BLUE)
                #print("red")
            elif color >= 173 and color < 181:
                mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_RED)
            else:
                mc.setBlock(posx+x,0,posz+y,block.CONCRETE_BLOCK_PURPLE)
getargv()



