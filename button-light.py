import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# button
GPIO.setup(24, GPIO.IN)

# lights ========================================
# green light
GPIO.setup(25, GPIO.OUT)
# red light
GPIO.setup(23, GPIO.OUT)
# turn any lights on, off
GPIO.output(25, GPIO.LOW)
GPIO.output(23, GPIO.LOW)

while True:
	input_value = GPIO.input(24)
	#print(input_value)
	if (input_value == True):
		# turn green light on
		GPIO.output(25, GPIO.HIGH)
		# turn red light on
		GPIO.output(23, GPIO.LOW)
		print("Turning green light on...")
	else:
		# turn green light off
		GPIO.output(25, GPIO.LOW)
		# turn red light on
		GPIO.output(23, GPIO.HIGH)
		print("Turning red light on...")

	time.sleep(0.01)
