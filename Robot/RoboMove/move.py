from machine import Pin, PWM, UART
from time import sleep

pin = Pin("LED", Pin.OUT)

# Initialize servos
baseServo = PWM(Pin(16))
btmServo = PWM(Pin(17))

# uart = UART(1, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Pin setup for servo motors
servo_pins = {
    'midServo': PWM(Pin(18)),
    'topServo': PWM(Pin(19)),
    'gripBaseServo': PWM(Pin(20)),
    'gripServo': PWM(Pin(22)),
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
    moveServo('btmServo', 150)
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

# Function to smoothly move a servo from its current position to a target position
def smoothMoveServo(servo_name, target_angle, step_delay=0.02):
    current_angle = current_angles[servo_name]  # Fetch the current angle from the dictionary
    
    # Determine the direction to move
    step = 1 if target_angle > current_angle else -1
    
    # Gradually move the servo in small steps
    for angle in range(current_angle, target_angle + step, step):
        moveServo(servo_name, angle)  # Use move_servo function to update position
        sleep(step_delay)  # Delay to control smoothness of movement

# Method to smoothly pick up a metal object in front of the robotic arm
def pickUpMetal():
    # Step 1: Align the base of the arm to center (assuming object is in front)
    # smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smoothMoveServo('baseServo', 70, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smoothMoveServo('midServo', 80, step_delay=0.05)   # Angle mid arm forward
    smoothMoveServo('topServo', 85, step_delay=0.05)# Lower top arm to approach object

    #trying somthing
    smoothMoveServo('gripBaseServo', current_angles['gripBaseServo'] + 50, step_delay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 70, step_delay=0.03) #open
    smoothMoveServo('topServo', 20, step_delay=0.05)
    smoothMoveServo('midServo', 120, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)

    # this will be to close the gripper and then to drop what it has
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 90, step_delay=0.03) #closed
    smoothMoveServo('btmServo', 70, step_delay=0.05)
    smoothMoveServo('baseServo', 160, step_delay=0.05)
    smoothMoveServo('gripServo',  60, step_delay=0.03) #open
    smoothMoveServo('gripServo', 90, step_delay=0.03) #closed

def pickUpCardboard():
    smoothMoveServo('baseServo', 90, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('topServo', 85, step_delay=0.05)
    
    smoothMoveServo('gripBaseServo', current_angles['gripBaseServo'] + 50, step_delay=0.03)
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('topServo', 20, step_delay=0.05)
    smoothMoveServo('midServo', 115, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)

    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 120, step_delay=0.03)
    smoothMoveServo('midServo', 100, step_delay=0.05)
    smoothMoveServo('btmServo', 70, step_delay=0.05)
    smoothMoveServo('baseServo', 35, step_delay=0.05)
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 90, step_delay=0.03)

    smoothMoveServo('topServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('baseServo', 90, step_delay=0.05)

def pickUpPlastic():
    smoothMoveServo('baseServo', 90, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('topServo', 85, step_delay=0.05)
    
    smoothMoveServo('gripBaseServo', current_angles['gripBaseServo'] + 50, step_delay=0.03)
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('topServo', 20, step_delay=0.05)
    smoothMoveServo('midServo', 135, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)

    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 120, step_delay=0.03)
    smoothMoveServo('midServo', 100, step_delay=0.05)
    smoothMoveServo('btmServo', 70, step_delay=0.05)
    smoothMoveServo('baseServo', 50, step_delay=0.05)
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 90, step_delay=0.03)

    smoothMoveServo('topServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('baseServo', 90, step_delay=0.05)

def pickUpPaper():
    pin.toggle()
    sleep(1)
    pin.off()

    smoothMoveServo('baseServo', 90, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('topServo', 85, step_delay=0.05)
    
    smoothMoveServo('gripBaseServo', current_angles['gripBaseServo'] + 50, step_delay=0.03)
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('topServo', 20, step_delay=0.05)
    smoothMoveServo('midServo', 135, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)

    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 120, step_delay=0.03)
    smoothMoveServo('midServo', 120, step_delay=0.05)
    smoothMoveServo('btmServo', 70, step_delay=0.05)
    smoothMoveServo('baseServo', 120, step_delay=0.05)
    smoothMoveServo('gripServo', 50, step_delay=0.03)
    smoothMoveServo('gripServo', 90, step_delay=0.03)

    smoothMoveServo('topServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('baseServo', 90, step_delay=0.05)

def pickUpGlass():
    smoothMoveServo('baseServo', 90, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('topServo', 85, step_delay=0.05)
    
    smoothMoveServo('gripBaseServo', current_angles['gripBaseServo'] + 50, step_delay=0.03)
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('topServo', 20, step_delay=0.05)
    smoothMoveServo('midServo', 135, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)

    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo', 120, step_delay=0.03)
    smoothMoveServo('midServo', 120, step_delay=0.05)
    smoothMoveServo('btmServo', 70, step_delay=0.05)
    smoothMoveServo('baseServo', 0, step_delay=0.05)
    smoothMoveServo('gripServo', 50, step_delay=0.03)
    smoothMoveServo('gripServo', 90, step_delay=0.03)

    smoothMoveServo('topServo', 85, step_delay=0.05)
    smoothMoveServo('midServo', 80, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)
    smoothMoveServo('baseServo', 90, step_delay=0.05)

    # Step 1: Align the base of the arm to center (assuming object is in front)
    # smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smoothMoveServo('baseServo', 70, step_delay=0.05)
    smoothMoveServo('btmServo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smoothMoveServo('midServo', 80, step_delay=0.05)   # Angle mid arm forward
    smoothMoveServo('topServo', 85, step_delay=0.05)# Lower top arm to approach object

    #trying somthing
    smoothMoveServo('gripBaseServo', current_angles['gripBaseServo'] + 50, step_delay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 70, step_delay=0.03) #open
    smoothMoveServo('topServo', 20, step_delay=0.05)
    smoothMoveServo('midServo', 120, step_delay=0.05)
    smoothMoveServo('btmServo', 90, step_delay=0.05)

    # this will be to close the gripper and then to drop what it has
    smoothMoveServo('gripServo', 60, step_delay=0.03)
    smoothMoveServo('gripServo',  90, step_delay=0.03) #closed
    smoothMoveServo('btmServo', 70, step_delay=0.05)
    smoothMoveServo('baseServo', 160, step_delay=0.05)
    smoothMoveServo('gripServo',  60, step_delay=0.03) #open
    smoothMoveServo('gripServo', 90, step_delay=0.03) #closed

'''
def detectAndSort(results):
    for detection in results:
        classID = detection['classID']
        match classID:
            case 0:
                print("metal detected")
                pickUpMetal()
            case 1:
                print("paper detected")
                pickUpPaper()
            case 2:
                print("plastic detected")
                pickUpPlastic()
            case 3:
                print("material detected")
                #call method/function
            case 4:
                print("material detected")
                #call method/function
            case _:
                idle()
 
'''
# Loop through different actions
while True:
    idle()


    '''
    try:
        #pickUpMetal()
        detectAndSort(results)    
    except KeyError as e:
        print(f"Key error: {e}")
        idle()  # Reset to a safe position
    except Exception as e:
        print(f"Unexpected error: {e}")
        idle()
'''