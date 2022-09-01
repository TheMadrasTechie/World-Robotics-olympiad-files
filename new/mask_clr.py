import cv2
import numpy as np
import imutils
print("jhvjv")
font = cv2.FONT_HERSHEY_SIMPLEX
def srch(cam,frame,Lower,Upper,hsv,char_name,B,G,R):
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
                 #global blks
                 #frame = find_blocks.search_blks(x, y,frame)
                 #blks.append('jj')
                 #auto_cam(c,mask1)
                 #shape_det(mask1,char_name,c,x,y,rect_area,w,h,y_max,y_min,x_max,x_min,area_min,area_max) 
            cv2.putText(frame, char_name, (int(x-2), int(y-2)), font, 0.8, (B,G,R), 2, cv2.LINE_AA)
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (B,G,R), 2)
    
    return frame