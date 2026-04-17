# AI on the Edge - Lesson 6
# Class Code: Blink LED
# Lori Pfahler
# April 2026

from fusion_hat.pin import Pin, Mode
import time

# setup red led
red_led = Pin(17, mode = Mode.OUT)

try:
    while True:
        red_led.high()
        time.sleep(0.5)
        red_led.low()
        time.sleep(0.5)

except KeyboardInterrupt:
    red_led.low()


