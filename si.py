from pyfirmata import Arduino, util
from time import sleep
 
board = Arduino('COM9')
if (board):
    print("configured arduino")
#while True:
#   board.digital[13].write(1)
#    sleep(0.5)
#    board.digital[13].write(0)
#    sleep(0.5) 
def forward():
	 board.digital[2].write(1)
	 board.digital[3].write(0)
	 board.digital[4].write(1)
	 board.digital[5].write(0)
	 board.digital[6].write(1)
	 board.digital[7].write(0)
	 board.digital[8].write(1)
	 board.digital[9].write(0)
	 return
def backward():
	 board.digital[2].write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(0)
	 board.digital[7].write(1)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return	 
def left():
	 board.digital[2]
	 .write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(1)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(1)
	 board.digital[8].write(1)
	 board.digital[9].write(0)
	 return	 
def right():
	 board.digital[2].write(1)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(1)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return
def drag_left():
	 board.digital[2].write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(1)
	 board.digital[5].write(0)
	 board.digital[6].write(1)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return
def drag_right():
	 board.digital[2].write(1)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(0)
	 board.digital[7].write(1)
	 board.digital[8].write(1)
	 board.digital[9].write(0)
	 return
def front_right():
	 board.digital[2].write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(0)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return
def back_right():
	 board.digital[2].write(0)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(0)
	 board.digital[7].write(1)
	 board.digital[8].write(0)
	 board.digital[9].write(0)
	 return
def front_left():
	 board.digital[2].write(0)
	 board.digital[3].write(0)
	 board.digital[4].write(1)
	 board.digital[5].write(0)
	 board.digital[6].write(1)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(0)
	 return
def back_left():
	 board.digital[2].write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(0)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return	
def m4_right():
	 board.digital[2].write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(0)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(1)
	 board.digital[8].write(0)
	 board.digital[9].write(0)
	 return
def m4_left():
	 board.digital[2].write(1)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(1)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return		 
def m3_left():
	 board.digital[2].write(0)
	 board.digital[3].write(0)
	 board.digital[4].write(1)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(0)
	 board.digital[8].write(1)
	 board.digital[9].write(0)
	 return
def m3_right():
	 board.digital[2].write(0)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(0)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return
def bac_right():
	 board.digital[2].write(1)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(1)
	 board.digital[6].write(0)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(0)
	 return
def bac_left():
	 board.digital[2].write(0)
	 board.digital[3].write(1)
	 board.digital[4].write(1)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(0)
	 return
def fron_left():
	 board.digital[2].write(0)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(0)
	 board.digital[6].write(0)
	 board.digital[7].write(1)
	 board.digital[8].write(1)
	 board.digital[9].write(0)
	 return
def fron_right():
	 board.digital[2].write(0)
	 board.digital[3].write(0)
	 board.digital[4].write(0)
	 board.digital[5].write(0)
	 board.digital[6].write(1)
	 board.digital[7].write(0)
	 board.digital[8].write(0)
	 board.digital[9].write(1)
	 return		 		 		 		 	 		 		 		 	 		 		 		 		 	 	 
	
	
	 