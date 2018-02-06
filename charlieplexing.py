import RPi.GPIO as GPIO
import time;
pins = [18, 23, 24]
pin_led_status = [
    [1, 0, -1],  # A
    [0, 1, -1],  # B
    [-1, 1, 0],  # C
    [-1, 0, 1],  # D
    [1, -1, 0],  # E
    [0, -1, 1],  # F
]

GPIO.setmode(GPIO.BCM)


def set_pin(pin_index, pin_state):
    if pin_state == -1:
        GPIO.setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)


def light_led(led_number):
    for pin_index, pin_state in enumerate(pin_led_status[led_number]):
        set_pin(pin_index, pin_state)


set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)


round_times = [0, 0, 3, 2, 5, 1, 3, 2, 3, 3, 3, 1, 3, 2, 3, 5, 2, 2];

while True:
    for t in round_times:
        light_led(t)
        time.sleep(0.5)
