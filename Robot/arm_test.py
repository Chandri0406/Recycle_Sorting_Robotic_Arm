from machine import Pin, PWM
from time import sleep

base_servo = PWM(Pin(16))
btm_servo = PWM(Pin(17))

# Pin setup for servo motors
servo_pins = {
    'mid_servo': PWM(Pin(18)),
    'top_servo': PWM(Pin(19)),
    'grip_base_servo': PWM(Pin(20)),
    'grip_servo': PWM(Pin(21))
    }

# Function to set the PWM frequency and duty cycle for a servo
def set_servo_angle(servo, angle):
    duty = int(1000 + (angle / 180.0) * 8000)
    servo.duty_u16(duty)

# Setup PWM frequency
def setup_servos():
    base_servo.freq(50)
    btm_servo.freq(50)
    mid_servo.freq(50)
    top_servo.freq(50)
    grip_base_servo.freq(50)
    grip_servo.freq(50)

# Function to set the PWM frequency and duty cycle for a servo
def set_servo_angle(servo, angle):
    duty = int(1000 + (angle / 180.0) * 8000)
    servo.duty_u16(duty)

# Setup PWM frequency for all servos
def setup_servos():
    for servo in servo_pins.values():
        servo.freq(50)


# Initialize servos and set them all to 90 degrees
setup_servos()
current_angles = {
    'base_servo': 90,
    'btm_servo': 90,
    'mid_servo': 90,
    'top_servo': 70,
    'grip_base_servo': 70,
    'grip_servo': 70
}

# Function to move all servos by 10 degrees
def move_servos():
    for servo_name, angle in current_angles.items():
        new_angle = angle + 10 if angle + 10 <= 180 else 0  # Reset to 0 after 180 degrees
        current_angles[servo_name] = new_angle
        set_servo_angle(servo_pins[servo_name], new_angle)  # Directly access the servo from the dictionary

# Loop to move the servos by 10 degrees every 40 seconds
while True:
    move_servos()
    sleep(10)  # Wait for 40 seconds before the next movement
