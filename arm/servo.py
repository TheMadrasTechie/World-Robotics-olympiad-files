from pyfirmata import Arduino, util
import time
import sys
csv = open("Servo.csv", "w") 
csv.write("Time,servo-1,servo-2")
current_angle=[0,0]
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

tim = time.time()
ser0 = board.get_pin('d:2:s')
ser3 = board.get_pin('d:4:s')




def l0(deg):
    current_angle[0] += deg
    if (current_angle[0] > 180):
        current_angle[0]=180
    if (current_angle[0]<0):
        current_angle[0]=0
    ser0.write(abs(current_angle[0]))
    csv.write(str(int(time.time()-tim))","str(current_angle[0])",")
    print('rotates...')
    time.sleep(0.1)
    return current_angle[0]



def l3(deg):
    current_angle[1] += deg
    if (current_angle[1] > 180):
        current_angle[1]=180
    if (current_angle[1]<0):
        current_angle[1]=0
    ser3.write(abs(current_angle[1]))
    csv.write(str(int(time.time()-tim))",,"str(current_angle[1]))
    print('rotates...')
    time.sleep(0.1)
    return current_angle[1]

