from machine import Pin, PWM
from time import sleep


# Initialize servos
baseServo = PWM(Pin(16))
btmServo = PWM(Pin(17))

# Pin setup for servo motors
servo_pins = {
    'midServo': PWM(Pin(18)),
    'topServo': PWM(Pin(19)),
    'gripBaseServo': PWM(Pin(20)),
    'gripServo': PWM(Pin(21)),
    'baseServo': baseServo,
    'btmServo': btmServo
}

# Function to set the PWM frequency and duty cycle for a servo
def set_servo_angle(servo, angle):
    duty = int(1000 + (angle / 180.0) * 8000)
    servo.duty_u16(duty)

# Setup PWM frequency for all servos
def setup_servos():
    for servo in servo_pins.values():
        servo.freq(50)

# Initialize servos and set them all to their default positions
setup_servos()
current_angles = {
    'baseServo': 80,
    'btmServo': 90,
    'midServo': 90,
    'topServo': 90,
    'gripBaseServo': 90,
    'gripServo': 120
}

# Function to move a specific servo
def moveServo(servo_name, angle):
    current_angles[servo_name] = angle
    set_servo_angle(servo_pins[servo_name], angle)

# Method to move servos in a group - all servos in sync
def moveAllServosBy(offset):
    for servo_name, angle in current_angles.items():
        new_angle = angle + offset
        if 0 <= new_angle <= 180:  # Ensure angle stays within bounds
            moveServo(servo_name, new_angle)

def idle():
    moveServo('baseServo', 90)
    moveServo('btmServo', 90)
    moveServo('midServo', 90)
    moveServo('topServo', 90)
    moveServo('gripBaseServo', 90)

def rotateLeft():
    moveServo('baseServo', current_angles['baseServo'] + 20)
    
def rotateRight():
    moveServo('baseServo', current_angles['baseServo'] - 20)

def moveUp():
    moveServo('baseServo',100)
    moveServo('btmServo', current_angles['btmServo'] + 5)
    moveServo('midServo', current_angles['midServo'] - 5)
    moveServo('topServo', current_angles['topServo'] + 5)
    
def moveDown():
    moveServo('baseServo',100)
    moveServo('btmServo', current_angles['btmServo'] - 5)
    moveServo('midServo', current_angles['midServo'] + 5)
    moveServo('topServo', current_angles['topServo'] - 5)

def grip():
    # Example: Move grip servos to close the grip
    moveServo('gripBaseServo', current_angles['gripBaseServo'] + 10)
    moveServo('gripServo', current_angles['gripServo'] + 10)

def release_grip():
    # Example: Move grip servos to open the grip
    moveServo('gripBaseServo', current_angles['gripBaseServo'] - 10)
    moveServo('gripServo', current_angles['gripServo'] - 10)

def pickUp():
    idle()
    sleep(5)
    
    moveDown()
    sleep(2)
    moveDown()
    sleep(2)
    moveDown()
    sleep(2)
    moveDown()
    sleep(2)
    moveDown()
    sleep(2)
    moveDown()
    sleep(2)
    moveDown()
    sleep(2)

    
    moveUp()
    sleep(2)
    moveUp()
    sleep(2)
    moveUp()
    sleep(2)
    moveUp()
    sleep(2)
    moveUp()
    sleep(2)
    moveUp()
    sleep(2)
    
def basicLoop():
    idle()
    sleep(5)
    
    rotateLeft()
    sleep(1)
    rotateLeft()
    sleep(3)
    
    moveDown()
    sleep(1)
    moveDown()
    sleep(1)
    moveDown()
    sleep(1)
    moveDown()
    sleep(1)
    
    moveUp()
    sleep(1)
    moveUp()
    sleep(1)
    moveUp()
    sleep(1)
    moveUp()
    sleep(1)
    
    rotateRight()
    sleep(1)
    rotateRight()
    sleep(1)


# Loop through different actions
while True:
    idle()
