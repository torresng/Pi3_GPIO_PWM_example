import RPi.GPIO as GPIO
import time

CONTROL_PIN = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(CONTROL_PIN, GPIO.OUT)

try:
    print('Ctrl-C to stop')
    while True:
        print('start')
        GPIO.output(CONTROL_PIN, GPIO.HIGH)
        time.sleep(3)
        print('stop')
        GPIO.output(CONTROL_PIN, GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:
    print('closed')
finally:
    GPIO.cleanup()
