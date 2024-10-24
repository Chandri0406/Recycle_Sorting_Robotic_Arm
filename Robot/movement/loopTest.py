from machine import Pin, PWM
from time import sleep

# Initialize servos
base_servo = PWM(Pin(16))
btm_servo = PWM(Pin(17))

# Pin setup for servo motors
servo_pins = {
    'mid_servo': PWM(Pin(18)),
    'top_servo': PWM(Pin(19)),
    'grip_base_servo': PWM(Pin(20)),
    'grip_servo': PWM(Pin(21)),
    'base_servo': base_servo,
    'btm_servo': btm_servo
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
    'base_servo': 80,
    'btm_servo': 90,
    'mid_servo': 90,
    'top_servo': 90,
    'grip_base_servo': 90,
    'grip_servo': 120
}

# Function to move a specific servo
def move_servo(servo_name, angle):
    current_angles[servo_name] = angle
    set_servo_angle(servo_pins[servo_name], angle)

# Method to move servos in a group - all servos in sync
def move_all_servos_by(offset):
    for servo_name, angle in current_angles.items():
        new_angle = angle + offset
        if 0 <= new_angle <= 180:  # Ensure angle stays within bounds
            move_servo(servo_name, new_angle)

# Custom group movement functions for different actions
def idle():
    move_servo('base_servo',90)
    move_servo('btm_servo',90)
    move_servo('mid_servo',90)
    move_servo('top_servo',90)
    move_servo('grip_base_servo',90)
    
def rotateLeft():
    move_servo('base_servo', current_angles['base_servo'] + 20)
    
def rotateRight():
    move_servo('base_servo', current_angles['base_servo'] - 20)

def grip():
    # Example: Move grip servos to close the grip
    move_servo('grip_base_servo', current_angles['grip_base_servo'] + 10)
    move_servo('grip_servo', current_angles['grip_servo'] + 10)

def release_grip():
    # Example: Move grip servos to open the grip
    move_servo('grip_base_servo', current_angles['grip_base_servo'] - 10)
    move_servo('grip_servo', current_angles['grip_servo'] - 10)
    
def moveUp():
    move_servo('base_servo',100)
    move_servo('btm_servo', current_angles['btm_servo'] + 5)
    move_servo('mid_servo', current_angles['mid_servo'] - 5)
    move_servo('top_servo', current_angles['top_servo'] + 5)
    
def moveDown():
    move_servo('base_servo',100)
    move_servo('btm_servo', current_angles['btm_servo'] - 5)
    move_servo('mid_servo', current_angles['mid_servo'] + 5)
    move_servo('top_servo', current_angles['top_servo'] - 5)
     
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
    pickUp()
