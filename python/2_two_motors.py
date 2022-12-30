#!/usr/bin/python3

# Include a library so the program knows how to run the pins
import RPi.GPIO as GPIO
# Include a library so the program understands about time
import time
# Include a library so the program understands keyboard inputs
from getkey import getkey, keys

# Define some constants for the pi numbers
motor1_a = 16
motor1_b = 22
motor1_c = 18
motor1_direction = 1
motor1_speed = 0

motor2_a = 21
motor2_b = 19
motor2_c = 23
motor2_direction = 1
motor2_speed = 0

def motor1_move():
	# Set the direction for the motors
	if motor1_direction == 1:
		GPIO.output(motor1_a, GPIO.LOW)
		GPIO.output(motor1_c, GPIO.HIGH)
	else:
		GPIO.output(motor1_a, GPIO.HIGH)
		GPIO.output(motor1_c, GPIO.LOW)
	p.ChangeDutyCycle(motor1_speed)
def motor2_move():
	# Set the direction for the motors
	if motor2_direction == 1:
		GPIO.output(motor2_a, GPIO.LOW)
		GPIO.output(motor2_c, GPIO.HIGH)
	else:
		GPIO.output(motor2_a, GPIO.HIGH)
		GPIO.output(motor2_c, GPIO.LOW)
	q.ChangeDutyCycle(motor2_speed)

# Set the library to know how to number the pins
GPIO.setmode(GPIO.BOARD)
# Setup if the pins are reading or writing information
GPIO.setup(motor1_a, GPIO.OUT)
GPIO.setup(motor1_b, GPIO.OUT)
GPIO.setup(motor1_c, GPIO.OUT)
# Create a power management variable for the pin
p = GPIO.PWM(motor1_b, 50)

# Setup if the pins are reading or writing information
GPIO.setup(motor2_a, GPIO.OUT)
GPIO.setup(motor2_b, GPIO.OUT)
GPIO.setup(motor2_c, GPIO.OUT)
# Create a power management variable for the pin
q = GPIO.PWM(motor2_b, 50)

# Output high and low for the pins
GPIO.output(motor1_a, GPIO.HIGH)
GPIO.output(motor1_c, GPIO.LOW)
# Start the power controlling pin to start the motor
p.start(motor1_speed);
# Sleep so we can see the motor move
time.sleep(0.1)

# Output high and low for the pins
GPIO.output(motor2_a, GPIO.HIGH)
GPIO.output(motor2_c, GPIO.LOW)
# Start the power controlling pin to start the motor
q.start(50);
# Sleep so we can see the motor move
time.sleep(2)

# Tell the user what to do
print("Press a key to control the motor")

# Continue forever
while True:
	# Read the key pressed
	keypressed = getkey()

	# If the user wants to quit
	if keypressed == "q":
		print("You chose to quit")
		break;

	if keypressed == "7":
		#print("Forward")
		if ( motor1_direction == 1 ):
			motor1_speed += 10
		else:
			motor1_speed -= 10

	if keypressed == "4":
		#print("Stop")
		motor1_speed = 0

	if keypressed == "1":
		print("Back")
		if ( motor1_direction == 1 ):
			motor1_speed -= 10
		else:
			motor1_speed += 10

	# If the speed is less than 0
	if motor1_speed < 0:
		# Switch the direction of the motor
		motor1_direction = abs(motor1_direction - 1)
		motor1_speed = 0
	# If the speed is more than 100
	if motor1_speed > 100:
		# Limit the speed to 100
		motor1_speed = 100

	# Call the function to change the motor settings
	motor1_move()

# Turn everything off
GPIO.cleanup()
