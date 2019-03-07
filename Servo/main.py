import RPi.GPIO as GPIO
import time

LED_PIN = 18
PWM_FREQ = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, PWM_FREQ)
pwm.start(0)

try:
    print('Ctrl-C to Cancel')
    while True:
        for duty_cycle in range(0, 20, 1):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.2)
        for duty_cycle in range(20, 0, -1):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.2)
except KeyboardInterrupt:
    print('Closed')
finally:
    pwm.stop()
    GPIO.cleanup()
