from machine import Pin, PWM, UART
from time import sleep

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))
uart.init(bits=8, parity=None, stop=1)

# Pin setup for servo motors
servoPins = {
    'baseServo': PWM(Pin(16)),
    'btmServo': PWM(Pin(17)),
    'midServo': PWM(Pin(18)),
    'topServo': PWM(Pin(19)),
    'gripBaseServo': PWM(Pin(20)),
    'gripServo': PWM(Pin(21))
}

# Function to set the PWM frequency and duty cycle for a servo
def setServoAngle(servo, angle):
    duty = int(1000 + (angle / 180.0) * 8000)
    servo.duty_u16(duty)

# Setup PWM frequency for all servos
def setupServos():
    for servo in servoPins.values():
        servo.freq(50)
    
# Initialize servos and set them all to their default positions
setupServos()
currentAngles = {
    'baseServo': 90,
    'btmServo': 90,
    'midServo': 90,
    'topServo': 90,
    'gripBaseServo': 90,
    'gripServo': 120
}

# Function to move a specific servo
def moveServo(servoName, angle):
    currentAngles[servoName] = angle
    setServoAngle(servoPins[servoName], angle)

# Method to move servos in a group - all servos in sync
def moveAllServosBy(offset):
    for servoName, angle in currentAngles.items():
        newAngle = angle + offset
        if 0 <= newAngle <= 180:  # Ensure angle stays within bounds
            moveServo(servoName, newAngle)

# Function to smoothly move a servo from its current position to a target position
def smoothMoveServo(servoName, targetAngle, stepDelay=0.02):
    currentAngle = currentAngles[servoName]  # Fetch the current angle from the dictionary
    
    # Determine the direction to move
    step = 1 if targetAngle > currentAngle else -1
    
    # Gradually move the servo in small steps
    for angle in range(currentAngle, targetAngle + step, step):
        moveServo(servoName, angle)  # Use move_servo function to update position
        sleep(stepDelay)  # Delay to control smoothness of movement

# Function to move servos to 90 degrees
def defualtPos():
    smoothMoveServo('baseServo', 90, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('midServo', 80, stepDelay=0.05)
    smoothMoveServo('topServo', 85, stepDelay=0.05)
    smoothMoveServo('gripBaseServo', 90, stepDelay=0.05)
    smoothMoveServo('gripServo', 110, stepDelay=0.03)

    sleep(2)
    searchForMat()

# Function to lower the arm to search for materials
def searchForMat():
    smoothMoveServo('baseServo', 75, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('topServo', 20, stepDelay=0.05)
    sleep(15)

# Function to smoothly pick up a metal object in front of the robotic arm
def pickUpMetal():

    #searchForMat()

    # Pick up what is infront of it
    smoothMoveServo('gripBaseServo', 90, stepDelay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 60, stepDelay=0.03) # open grip
    smoothMoveServo('topServo', 20, stepDelay=0.05)
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('gripServo', 90, stepDelay=0.03) # closed

    # Drop into selected area
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('btmServo', 100, stepDelay=0.05)
    smoothMoveServo('baseServo', 160, stepDelay=0.05)
    smoothMoveServo('gripServo',  60, stepDelay=0.03) # open

    defualtPos()

def pickUpCardboard():

    #searchForMat()
    
    # Pick up what is infront of it
    smoothMoveServo('gripBaseServo', 90, stepDelay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 60, stepDelay=0.03) # open grip
    smoothMoveServo('topServo', 20, stepDelay=0.05)
    smoothMoveServo('midServo', 115, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('gripServo', 120, stepDelay=0.03) # closed grip

    # Drop into selected area
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('btmServo', 100, stepDelay=0.05)
    smoothMoveServo('baseServo', 35, stepDelay=0.05)
    smoothMoveServo('gripServo', 60, stepDelay=0.03) # open grip

    defualtPos()

def pickUpPlastic():

    #searchForMat()
    
    # Pick up what is infront of it
    smoothMoveServo('gripBaseServo', 90, stepDelay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 60, stepDelay=0.03) # open grip
    smoothMoveServo('topServo', 20, stepDelay=0.05)
    smoothMoveServo('midServo', 135, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('gripServo', 90, stepDelay=0.03) # closed grip

    # Drop into selected area
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('btmServo', 70, stepDelay=0.05)
    smoothMoveServo('baseServo', 50, stepDelay=0.05)
    smoothMoveServo('gripServo', 60, stepDelay=0.03) # open grip

    defualtPos()

def pickUpPaper():

    #searchForMat()
    
    # Pick up what is infront of it
    smoothMoveServo('gripBaseServo', 90, stepDelay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 60, stepDelay=0.03) # open grip
    smoothMoveServo('topServo', 20, stepDelay=0.05)
    smoothMoveServo('midServo', 135, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('gripServo', 120, stepDelay=0.03) # closed grip

    # Drop into selected area
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('btmServo', 100, stepDelay=0.05)
    smoothMoveServo('baseServo', 120, stepDelay=0.05)
    smoothMoveServo('gripServo', 50, stepDelay=0.03) # open grip

    defualtPos()

def pickUpGlass():

    #searchForMat()
    
    # Pick up what is infront of it
    smoothMoveServo('gripBaseServo', 90, stepDelay=0.03)  # Adjust grip position
    smoothMoveServo('gripServo', 60, stepDelay=0.03)# open grip
    smoothMoveServo('topServo', 20, stepDelay=0.05)
    smoothMoveServo('midServo', 135, stepDelay=0.05)
    smoothMoveServo('btmServo', 90, stepDelay=0.05)
    smoothMoveServo('gripServo', 90, stepDelay=0.03) #closed grip

    # Drop into selected area
    smoothMoveServo('midServo', 100, stepDelay=0.05)
    smoothMoveServo('btmServo', 100, stepDelay=0.05)
    smoothMoveServo('baseServo', 5, stepDelay=0.05)
    smoothMoveServo('gripServo', 50, stepDelay=0.03) #open grip

    defualtPos()

# Loop through different actions
while True:
    matID = None

    if uart.any():
       matID = uart.read()
       print(f"Signal received: {matID}")
       matID = matID[:4]

    if matID == b'6510':
        print("Cardboard detected")
        pickUpCardboard()
    elif matID == b'6610':
        print("Glass detected")
        pickUpGlass()
    elif matID == b'6710':
        print("Metal detected")
        pickUpMetal()
    elif matID == b'6810': 
        print("Paper detected")
        pickUpPaper()
    elif matID == b'6910':
        print("Plastic detected")
        pickUpPlastic()
    else:
        print(f"Unknown object: {matID}")
        defualtPos()