import numpy as np
import cv2
import math
import imutils
val = 'd'
q_val = 0
font = cv2.FONT_HERSHEY_SIMPLEX
def search_blks(x,y,frame,char_name,blks):
        cv2.line(frame, (0,int(frame.shape[0]/2)), (int(frame.shape[1]), int(frame.shape[0]/2)), (0,255,0), 2)    
    #cv2.putText(frame, q_val, (int(x-2), int(y-2)), font, 0.8, (255,255,0), 2, cv2.LINE_AA)
    #if ((int(frame.shape[1]/2)-10)<x<(int(frame.shape[1]/2)+10)):
        cv2.line(frame, (0,int(frame.shape[0]/2)), (int(frame.shape[1]), int(frame.shape[0]/2)), (255,255,0), 2)    
        global val
        if(not(val==char_name)and(len(blks)==0)):
           val=char_name
           blks.append(char_name)
        return frame,char_name

        #return frame,'d' 