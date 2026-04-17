# AI on the Edge - Lesson 6
# Class Code: servos
# Lori Pfahler
# April 2026

from fusion_hat.servo import Servo
from time import sleep

# set up servo objects
pan_servo = Servo(2)
tilt_servo = Servo(3)

# move pan servo; goes from -90 to 90; negative is right looking at camera
pan_servo.angle(-90)
sleep(1)
pan_servo.angle(0)
sleep(1)
pan_servo.angle(90)
sleep(1)
pan_servo.angle(0)
sleep(1)

# move tilt servo; goes from -90 to 90; negative is up
# don't go past 45 for down; will hit the platform 
for i in range(0, -90, -5):
    tilt_servo.angle(i)
    sleep(0.2)
for i in range(-90, 46, 5):
    tilt_servo.angle(i)
    sleep(0.2)

# move both
pan_servo.angle(45)
tilt_servo.angle(-45)

sleep(1)

# return to zero
pan_servo.angle(0)
tilt_servo.angle(0)

