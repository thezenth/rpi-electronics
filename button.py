#this script checks every 0.01 for a button press, and then icnrements count each time the button is pressed
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

count = 0

while True:
	input_value = GPIO.input(24)
	#print(input_value)
	if (input_value == True):
		count = count + 1
		print("Button pressed " + str(count) + " times.")
	time.sleep(0.01)
