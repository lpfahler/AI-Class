# AI on the Edge - Lesson 6
# Class Code: potentiometer
# Lori Pfahler
# April 2026


from fusion_hat.adc import ADC
from time import sleep
from statistics import median

# setup potentiometer on ADC pin zero
potentiometer = ADC(0)

# read the value from potentiometer
while True:
    reading = potentiometer.read()
    print(f'Potentiometer Value: {reading:4d}', end = '\r')
    sleep(0.1)

