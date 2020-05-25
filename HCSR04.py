import RPi.GPIO as GPIO
from time import sleep, time

class HCSR04Provider():
    def __init__(self,echo, trigger):
        self.echo=echo
        self.trigger=trigger
        GPIO.setmode(GPIO.BCM)

    def getValue(self):
        # Get distance measurement
        GPIO.output(self.trigger, GPIO.LOW)            # Set TRIG LOW
        sleep(0.1)                                     # Min gap between measurements
        # Create 10 us pulse on TRIG
        GPIO.output(self.trigger, GPIO.HIGH)           # Set TRIG HIGH
        sleep(0.00001)                                 # Delay 10 us
        GPIO.output(self.trigger, GPIO.LOW)            # Set TRIG LOW
        # Measure return echo pulse duration
        while GPIO.input(self.echo) == GPIO.LOW:
            pulse_start = time()

        while GPIO.input(self.echo) == GPIO.HIGH:
            pulse_end = time()

        pulse_duration = pulse_end - pulse_start
        # Distance = 17160.5 * Time (unit cm) at sea level and 20C
        distance = pulse_duration * 17160.5
        distance = round(distance, 2)

        if distance > 2 and distance < 400:
            distance = distance + self.offset
        else:
            distance = 0
        return distance
