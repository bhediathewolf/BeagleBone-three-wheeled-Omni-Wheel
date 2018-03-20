import Adafruit_BBIO.GPIO as gp
import pygame

class motor(object):
    def __init__(self, en, in1, in2):
        self.en = en
        self.in1 = in1
        self.in2 = in2
        gp.setup(self.en, gp.OUT)
        gp.setup(self.in1, gp.OUT)
        gp.setup(self.in2, gp.OUT)
        gp.output(self.en, 0)
        gp.output(self.in1, 0)
        gp.output(self.in2, 0)

    def update(self, enV, in1V, in2V):
        gp.output(self.en, enV)
        gp.output(self.in1, in1V)
        gp.output(self.in2, in2V)

class stick(object):
    def __init__(self, xAxis, yAxis):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.x = 0
        self.y = 0

    def get(self):
        self.x = joystick.get_axis(self.xAxis)
        self.y = joystick.get_axis(self.yAxis)

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
lStick = stick(0, 1)
rStick = stick(3, 4)
A = motor("P8_7", "P8_8", "P8_10")
print "Motor A done"
B = motor("P8_11", "P8_12", "P8_14")
print "Motor B done"
C = motor("P8_15", "P8_16", "P8_13")
print "Motor C done"

while True:
    pygame.event.pump()
    lStick.get()
    rStick.get()
    if(rStick.x > 0 and rStick.y > 0):
        A.update(0, 0, 0)
        B.update(1, 1, 0)
        C.update(1, 0, 1)
    elif(rStick.x > 0 and rStick.y == 0):
        A.update(1, 1, 0)
        B.update(1, 1, 0)
        C.update(1, 0, 1)
    elif(rStick.x > 0 and rStick.y < 0):
        A.update(1 ,1, 0)
        B.update(0, 0, 0)
        C.update(1, 0, 1)
    elif(rStick.x == 0 and rStick.y > 0):
        A.update(1, 0, 1)
        B.update(1, 1, 0)
        C.update(0, 0, 0)
    elif(rStick.x == 0 and rStick.y < 0):
        A.update(1, 1, 0)
        B.update(1, 0, 1)
        C.update(0, 0, 0)
    elif(rStick.x < 0 and rStick.y > 0):
        A.update(1, 0, 1)
        B.update(0, 0, 0)
        C.update(1, 1, 0)    
    elif(rStick.x < 0 and rStick.y == 0):
        A.update(1, 0, 1)
        B.update(1, 0, 1)
        C.update(1, 1, 0)
    elif(rStick.x < 0 and rStick.y < 0):
        A.update(0, 0, 0)
        B.update(1, 0, 1)
        C.update(1, 1, 0)
    else:
        A.update(0, 0, 0)
        B.update(0, 0, 0)
        C.update(0, 0, 0)

    if(lStick.x < 0):
        A.update(1, 0, 1)
        B.update(1, 0, 1)
        C.update(1, 0, 1)
    elif(lStick.x > 0):
        A.update(1, 1, 0)
        B.update(1, 1, 0)
        C.update(1, 1, 0)
    
    quit = joystick.get_button(7)
    if(quit != 0):
        A.update(0, 0, 0)
        B.update(0, 0, 0)
        C.update(0, 0, 0)
	gp.cleanup()
        exit()
