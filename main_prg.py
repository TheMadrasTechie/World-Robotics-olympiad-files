from __future__ import division
from scipy.spatial import distance as dist
from imutils.video import VideoStream
import numpy as np
import cv2
import math
import imutils
import find_blocks
import time
#import locomotion

blks = []
cap = cv2.VideoCapture(0)       
# cap.set(cv2.CV_CAP_PROP_FPS, 10);    
# def getFrame(sec):
#     cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
#     hasFrames,image = cap.read()
#     if hasFrames:
#         cv2.imshow("dd",image)
#         cv2.imwrite("frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
#     return hasFrames
sec = 0
frameRate = 0.5
#success = getFrame(sec)
font = cv2.FONT_HERSHEY_SIMPLEX
S_Lower = (46, 100, 100)
S_Upper = (66, 255, 255)
Z_Lower = (168, 100, 100)
Z_Upper = (188, 255, 255)
I_Lower = (88, 100, 100)
I_Upper = (108, 255, 255)       
L_Lower = (1, 100, 100)
L_Upper = (21, 255, 255)
J_Lower = (108, 100, 100)
J_Upper = (128, 255, 255)
O_Lower = (18, 100, 100)
O_Upper = (38, 255, 255)
T_Lower = (140, 100, 100)
T_Upper = (160, 255, 255)
def angle(p1,p2):
    return int(math.atan((p2[1]-p1[1])/(p2[0]-p1[0]))*180/math.pi)
def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
def auto_cam(c,frame):
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])      
    T_B_mid = midpoint(extTop,extBot)
    R_L_mid = midpoint(extLeft,extRight)
    mid = midpoint(R_L_mid,T_B_mid)
    ang = angle(extBot,extRight)
    print(str(ang))
    #print(str(extTop)+"\t"+str(extBot)+"\t"+str(extRight)+"\t"+str(extLeft))

    cv2.imshow("ss",cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB))
def x_align(x,y,area,w,h,char_name,word,y_max,y_min,x_max,x_min,area_min,area_max):
    if(char_name==word):
        if(x_min<x<x_max):
           y_align(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)
           y_mvmnt(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max) 
        elif(x_max<x):
           print("Bot rotate Right")
           locomotion.right()
        elif(x_min>x):
           print("Bot rotate Left")   
           locomotion.left()
        else:
           print("Block not found \t Bot rotate Right")   
def can(gray_image,img):
    ret,thresh = cv2.threshold(gray_image,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
   
        M = cv2.moments(c)
   
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
def shape_det(frame,char_name,c,x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max):
    
    x_align(x,y,area,w,h,char_name,'O',y_max,y_min,x_max,x_min,area_min,area_max)
    canny = cv2.Canny(frame,80,240,3)
    canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    can(canny,frame)
def shape_deter(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max):
        if((((h>50)and(w>50))and(140<y<160))or((area>2000)and(140<y<160))):
            print("Katham \t Katham")
        elif((y_max<y)and(area>area_min)):     
            print("Camera down")   
            print("Bot Backward") 
            locomotion.backward()
        elif(y_min<y<y_max):    
            print("Camera down") 
        elif(y_min>y):
            print("Bot Forward") 
            locomotion.forward()
def align_objs(x,y,area,key,w,h,y_max,y_min,x_max,x_min,area_min,area_max):    
    if(area_min<area):
            print("Bot Forward") 
            locomotion.forward()
            shape_deter(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)
    elif(y_min<y<y_max):

            shape_deter(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)
                    
def y_align(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max):  
    if((y_max<y)and(area<area_min)):
            print("Camera down") 
            align_objs(x,y,area,'s',w,h,y_max,y_min,x_max,x_min,area_min,area_max)              
    elif(y<y_min):
            y_mvmnt(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)
            align_objs(x,y,area,'s',w,h,y_max,y_min,x_max,x_min,area_min,area_max)        
    elif((y_min<y<y_max)and(area>area_min)):            
            shape_deter(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)          
def y_mvmnt(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max):    
    if(area<area_min):
            print("Bot forward")
            locomotion.forward()
            align_objs(x,y,area,'i',w,h,y_max,y_min,x_max,x_min,area_min,area_max)
    elif((y<y_min)and(area<area_max)):
            print("Camera down") 
            print("Bot forward") 
            locomotion.forward()
            align_objs(x,y,area,'i',w,h,y_max,y_min,x_max,x_min,area_min,area_max)
    elif(y>y_max):
            y_align(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)
            align_objs(x,y,area,'i',w,h,y_max,y_min,x_max,x_min,area_min,area_max)
    elif((y_min<y<y_max)and(area>area_min)):            
            shape_deter(x,y,area,w,h,y_max,y_min,x_max,x_min,area_min,area_max)        
def clr_det(cam,frame,Lower,Upper,hsv,char_name,B,G,R):
    mask2 = cv2.inRange(hsv, Lower, Upper)
    mask1 = cv2.erode(mask2, None, iterations=2)
    mask = cv2.dilate(mask1, None, iterations=2)
    y_min = (frame.shape[1]/16)*7
    y_max = (frame.shape[1]/16)*9
    x_min = (frame.shape[0]/16)*7
    x_max = (frame.shape[0]/16)*9
    area_min = (frame.shape[0]*frame.shape[1])/20
    area_max = (frame.shape[0]*frame.shape[1])/5
    cnt = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        #c1 = max(cnt, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            if(cam=='a'):
                 x1,y1,w,h = cv2.boundingRect(cnt) 
                 rect_area = w*h
                 global blks
                 #frame,blk_val = find_blocks.search_blks(x, y,frame,char_name,blks)
                 print(blk_val)
                 # if(not(blk_val=='d')):
                 #    blks.append(blk_val)
                 #auto_cam(c,mask1)
                 shape_det(mask1,char_name,c,x,y,rect_area,w,h,y_max,y_min,x_max,x_min,area_min,area_max) 
            cv2.putText(frame, char_name, (int(x-2), int(y-2)), font, 0.8, (B,G,R), 2, cv2.LINE_AA)
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (B,G,R), 2)
            
while True:
    #time.sleep(0.2) 
    arm = cap.read()
    #success = getFrame(5)
    arm = arm[1]
    # transpose(image, image)
    # arm = cv2.flip(arm,-5)
    M = cv2.getRotationMatrix2D((int(arm.shape[0]/2),int(arm.shape[1]/2)), 90, 1)
    arm = cv2.warpAffine(arm, M, (int(arm.shape[0]),int(arm.shape[1])))
    blurI_ = cv2.GaussianBlur(arm, (11, 11), 0)
    hsv_arm = cv2.cvtColor(blurI_, cv2.COLOR_BGR2HSV)
    clr_det("a",arm,S_Lower,S_Upper,hsv_arm,"S",44,214,68)
    clr_det("a",arm,Z_Lower,Z_Upper,hsv_arm,"Z",55,39,238)
    clr_det("a",arm,I_Lower,I_Upper,hsv_arm,"I",206,154,0)
    clr_det("a",arm,L_Lower,L_Upper,hsv_arm,"L",0,94,254)
    clr_det("a",arm,J_Lower,J_Upper,hsv_arm,"J",159,6,16)    
    clr_det("a",arm,O_Lower,O_Upper,hsv_arm,"O",0,233,254)
    clr_det("a",arm,T_Lower,T_Upper,hsv_arm,"T",187,41,187)                  
    cv2.imshow("ARM", arm)
    key = cv2.waitKey(1) & 0xFF 
    if key == ord("q"):
        break
cv2.destroyAllWindows()
print(blks)