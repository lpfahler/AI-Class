# AI on the Edge - Lesson 6
# Class Code: PWM
# Lori Pfahler
# April 2026

from fusion_hat.pwm import PWM
from time import sleep

# setup the red, green and blue leds in rgbled
red_rgbled = PWM(5)
green_rgbled = PWM(6)
blue_rgbled = PWM(7)

# set the frequency for PWM
red_rgbled.freq(200)
green_rgbled.freq(200)
blue_rgbled.freq(200)

red_rgbled.pulse_width_percent(0)
green_rgbled.pulse_width_percent(0)
blue_rgbled.pulse_width_percent(0)

try: 
    while True:
        # pulse red
        for bright in range(0, 100, 1):
            red_rgbled.pulse_width_percent(bright)
            sleep(0.01)
        for bright in range(100, 0, -1):
            red_rgbled.pulse_width_percent(bright)
            sleep(0.01)
        # pulse red and blue together
        for bright in range(0, 100, 1):
            red_rgbled.pulse_width_percent(bright)
            blue_rgbled.pulse_width_percent(bright)        
            sleep(0.01)
        for bright in range(100, 0, -1):
            red_rgbled.pulse_width_percent(bright)
            blue_rgbled.pulse_width_percent(bright)
            sleep(0.01)

except KeyboardInterrupt:
    red_rgbled.pulse_width_percent(0)
    green_rgbled.pulse_width_percent(0)
    blue_rgbled.pulse_width_percent(0)    





