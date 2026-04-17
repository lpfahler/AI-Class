# AI on the Edge - Lesson 6
# Homework Code: Dimmer for RGB LED
# Lori Pfahler
# April 2026

from fusion_hat.adc import ADC
from fusion_hat.pwm import PWM
from time import sleep
from statistics import median

# set up the red led for the RGB LED
red_rgbled = PWM(5)

# set the frequency for PWM
red_rgbled.freq(200)

# turn off leds
red_rgbled.pulse_width_percent(0)

# set up potentiometer on ADC pin zero
potentiometer = ADC(0)

# number of reading to get to reduce noise
n_readings = 3

try:
    while True:
        # read potentiometer - use median of n_readings to reduce noise
        readings = []
        for i in range(n_readings):
            reading = potentiometer.read()
            readings.append(reading)
            sleep(0.05)
        median_reading = median(readings)
        
        # apply a nonlinear dimming equation making sure we get fully off and on settings
        if median_reading < 10:
            percent = 0 # fully off
        elif median_reading > 4000:
            percent = 100 # fully on
        else:
            # place median reading on 0 - 100 scale
            reading_100 = (median_reading/4095)*100
            # use nonlinear dimming equation
            percent = 100**(reading_100/100)
            
        # set led brightness    
        red_rgbled.pulse_width_percent(percent)
        
        # print results to shell
        print(f'Potentiometer Reading: {median_reading:4d}, Percent: {percent:>5.1f}', end = '\r')

except KeyboardInterrupt:
    # turn off leds
    red_rgbled.pulse_width_percent(0)
 