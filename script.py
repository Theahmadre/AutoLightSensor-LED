#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin_to_circuit = 17
led_pin = 6
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.LOW)

LIGHT_THRESHOLD = 450000
TIMEOUT_COUNT = 500000
CONSECUTIVE_READS = 3
dark_count = 0
light_count = 0
previous_led_state = GPIO.LOW
dark_warning_printed = False

def rc_time(pin_to_circuit):
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)
    while GPIO.input(pin_to_circuit) == GPIO.LOW and count < TIMEOUT_COUNT:
        count += 1
    if count >= TIMEOUT_COUNT:
        return count, True
    return count, False

try:
    while True:
        light_level, dark_warning = rc_time(pin_to_circuit)
        print(f"\rLight Level: {light_level}", end="")
        if dark_warning and not dark_warning_printed:
            print("\nWarning: Very dark environment detected (timeout).")
            dark_warning_printed = True
        elif not dark_warning:
            dark_warning_printed = False
        if light_level >= LIGHT_THRESHOLD:
            dark_count = 0
            light_count += 1
            if light_count >= CONSECUTIVE_READS:
                if previous_led_state == GPIO.LOW:
                    GPIO.output(led_pin, GPIO.HIGH)
                    print("\nLight level exceeds threshold. LED turned ON.")
                    previous_led_state = GPIO.HIGH
        else:
            light_count = 0
            dark_count += 1
            if dark_count >= CONSECUTIVE_READS:
                if previous_led_state == GPIO.HIGH:
                    GPIO.output(led_pin, GPIO.LOW)
                    print("\nLight level below threshold. LED turned OFF.")
                    previous_led_state = GPIO.LOW
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nScript interrupted. Cleaning up...")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Exiting program.")
