import cv2
import numpy
import mask_clr
cap = cv2.VideoCapture(0)

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

while True:
    arm = cap.read()
    arm = arm[1]
    blurI_ = cv2.GaussianBlur(arm, (11, 11), 0)
    hsv_arm = cv2.cvtColor(blurI_, cv2.COLOR_BGR2HSV)    
    arm = mask_clr.srch("a",arm,O_Lower,O_Upper,hsv_arm,"O",0,233,254)
    cv2.imshow("ARM", arm)
    key = cv2.waitKey(1) & 0xFF 
    if key == ord("q"):
        break

cv2.destroyAllWindows()