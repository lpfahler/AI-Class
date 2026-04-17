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
# take the median (middle value) of three readings to show on shell
n_readings = 3
while True:
    readings = []
    for i in range(n_readings):
        reading = potentiometer.read()
        readings.append(reading)
        sleep(0.1)
    print(f'Potentiometer Median Value: {median(readings):4d}', end = '\r')
