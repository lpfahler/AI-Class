# AI on the Edge - Lesson 8
# HW Code: Text to Speech (TTS) with RGB LED dimmer
# Lori Pfahler
# May 2026

from fusion_hat.tts import Piper
from fusion_hat.adc import ADC
from fusion_hat.pwm import PWM
from time import sleep
from statistics import median
  
# create text to speech object and set specific voice model
tts = Piper()
tts.set_model('en_US-amy-low')

# set up the red led for the RGB LED
red_rgbled = PWM(5)

# set the frequency for PWM
red_rgbled.freq(200)

# turn off led
red_rgbled.pulse_width_percent(0)

# set up potentiometer on ADC pin zero
potentiometer = ADC(0)

# number of reading to get to reduce noise
n_readings = 3

# delays 
reading_delay = 0.05
loop_delay = 0.25

# variable to determine if we have changed the message
previous_msg = ''

# function to determine appropriate level of brightness
# for speech model to "say" - assuming reading is on 0-100 scale
def set_message(reading):
    if reading < 11:
        msg = 'level 1'
    elif reading < 22:
        msg = 'level 2'
    elif reading < 33:
        msg = 'level 3'
    elif reading < 44:
        msg = 'level 4'
    elif reading < 55:
        msg = 'level 5'
    elif reading < 66:
        msg = 'level 6'
    elif reading < 77:
        msg = 'level 7'
    elif reading < 88:
        msg = 'level 8'
    else:
        msg = 'level 9'
    return(msg)


try:
    while True:
        # read potentiometer - use median of n_readings to reduce noise
        readings = []
        for i in range(n_readings):
            reading = potentiometer.read()
            readings.append(reading)
            sleep(reading_delay)
        median_reading = median(readings)
        
        # place median reading on 0 - 100 scale
        reading_100 = (median_reading/4095)*100
        
        # apply a nonlinear dimming equation making sure we get fully off and on settings
        if median_reading < 50:
            percent = 0 # fully off
            msg = 'off'
        elif median_reading > 4000:
            percent = 100 # fully on
            msg = 'full brightness'
        else:
            # use nonlinear dimming equation
            percent = 100**(reading_100/100)
            # set appropriate message
            msg = set_message(reading_100)
            
        # set led brightness    
        red_rgbled.pulse_width_percent(percent)
         
        # create the message
        final_msg = f'Brightness setting is {msg}.'
        # activate speech if  message has changed
        if msg != previous_msg:
            # say the message
            tts.say(final_msg, stream = False)          
        # print results to shell
        print(f'Pot Reading: {median_reading:4d}, Read100: {reading_100:>5.1f}, Percent: {percent:>5.1f}, message: {msg}                  ', end = '\r')
           
        # slow it down a bit
        sleep(loop_delay)
        # update the previous reading
        previous_msg = msg

except KeyboardInterrupt:
    # turn off led
    red_rgbled.pulse_width_percent(0)
