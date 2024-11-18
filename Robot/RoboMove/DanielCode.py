from machine import Pin, PWM
from time import sleep
from ultralytics import YOLO
import cv2
import serial
import time
import math
from imutils.video import FPS

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
     

# Function to smoothly move a servo from its current position to a target position
def smooth_move_servo(servo_name, target_angle, step_delay=0.02):
    current_angle = current_angles[servo_name]  # Fetch the current angle from the dictionary
    
    # Determine the direction to move
    step = 1 if target_angle > current_angle else -1
    
    # Gradually move the servo in small steps
    for angle in range(current_angle, target_angle + step, step):
        move_servo(servo_name, angle)  # Use move_servo function to update position
        sleep(step_delay)  # Delay to control smoothness of movement

# Method to smoothly pick up a metal object in front of the robotic arm
def PickUpMetal():
    
    # Step 1: Align the base of the arm to center (assuming object is in front)
 #   smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smooth_move_servo('base_servo', 70, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smooth_move_servo('mid_servo', 80, step_delay=0.05)   # Angle mid arm forward
    smooth_move_servo('top_servo', 85, step_delay=0.05)# Lower top arm to approach object
    #trying somthing
    #smooth_move_servo('grip_base_servo', current_angles['grip_base_servo'] + 50, step_delay=0.03)  # Adjust grip position
    smooth_move_servo('grip_servo', 70, step_delay=0.03) #open
    smooth_move_servo('top_servo', 20, step_delay=0.05)
    smooth_move_servo('mid_servo', 120, step_delay=0.05)
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    # this will be to close the gripper and then to drop what it has
    smooth_move_servo('grip_servo', 60, step_delay=0.03)
    smooth_move_servo('grip_servo',  90, step_delay=0.03) #closed
    smooth_move_servo('btm_servo', 100, step_delay=0.05)
    smooth_move_servo('base_servo', 160, step_delay=0.05)
    smooth_move_servo('grip_servo',  60, step_delay=0.03) #open
    smooth_move_servo('grip_servo', 90, step_delay=0.03) #closed
    

def PickUpCardboard():
    
    # Step 1: Align the base of the arm to center (assuming object is in front)
 #   smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smooth_move_servo('base_servo', 90, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smooth_move_servo('mid_servo', 80, step_delay=0.05)   # Angle mid arm forward
    smooth_move_servo('top_servo', 85, step_delay=0.05)# Lower top arm to approach object
    #trying somthing
    #smooth_move_servo('grip_base_servo', current_angles['grip_base_servo'] + 50, step_delay=0.03)  # Adjust grip position
    smooth_move_servo('grip_servo', 60, step_delay=0.03) #open
    smooth_move_servo('top_servo', 20, step_delay=0.05)
    smooth_move_servo('mid_servo', 115, step_delay=0.05)  #bend down part
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    # this will be to close the gripper and then to drop what it has
    smooth_move_servo('grip_servo', 60, step_delay=0.03)
    smooth_move_servo('grip_servo',  120, step_delay=0.03) #closed
    smooth_move_servo('mid_servo', 100, step_delay=0.05)
    smooth_move_servo('btm_servo', 70, step_delay=0.05)
    smooth_move_servo('base_servo', 35, step_delay=0.05)
    smooth_move_servo('grip_servo',  60, step_delay=0.03) #open
    smooth_move_servo('grip_servo', 90, step_delay=0.03) #closed
        # go back to orignial position:
    smooth_move_servo('top_servo', 85, step_delay=0.05)
    smooth_move_servo('mid_servo', 80, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)
    smooth_move_servo('base_servo', 90, step_delay=0.05)
  
  
def PickUpPlastic():
    
    # Step 1: Align the base of the arm to center (assuming object is in front)
 #   smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smooth_move_servo('base_servo', 90, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smooth_move_servo('mid_servo', 80, step_delay=0.05)   # Angle mid arm forward
    smooth_move_servo('top_servo', 85, step_delay=0.05)# Lower top arm to approach object
    #trying somthing
    #smooth_move_servo('grip_base_servo', current_angles['grip_base_servo'] + 50, step_delay=0.03)  # Adjust grip position
    smooth_move_servo('grip_servo', 60, step_delay=0.03) #open
    smooth_move_servo('top_servo', 20, step_delay=0.05)
    smooth_move_servo('mid_servo', 135, step_delay=0.05)  #bend down part
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    # this will be to close the gripper and then to drop what it has
    smooth_move_servo('grip_servo', 60, step_delay=0.03)
    smooth_move_servo('grip_servo',  120, step_delay=0.03) #closed
    smooth_move_servo('mid_servo', 100, step_delay=0.05)
    smooth_move_servo('btm_servo', 70, step_delay=0.05)
    smooth_move_servo('base_servo', 50, step_delay=0.05)
    smooth_move_servo('grip_servo',  60, step_delay=0.03) #open
    smooth_move_servo('grip_servo', 90, step_delay=0.03) #closed
    
        # go back to orignial position:
    smooth_move_servo('top_servo', 85, step_delay=0.05)
    smooth_move_servo('mid_servo', 80, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)
    smooth_move_servo('base_servo', 90, step_delay=0.05)
  
  
def PickUpPaper():
    
    # Step 1: Align the base of the arm to center (assuming object is in front)
 #   smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smooth_move_servo('base_servo', 90, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smooth_move_servo('mid_servo', 80, step_delay=0.05)   # Angle mid arm forward
    smooth_move_servo('top_servo', 85, step_delay=0.05)# Lower top arm to approach object
    #trying somthing
    #smooth_move_servo('grip_base_servo', current_angles['grip_base_servo'] + 50, step_delay=0.03)  # Adjust grip position
    smooth_move_servo('grip_servo', 60, step_delay=0.03) #open
    smooth_move_servo('top_servo', 20, step_delay=0.05)
    smooth_move_servo('mid_servo', 135, step_delay=0.05)  #bend down part
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    # this will be to close the gripper and then to drop what it has
    smooth_move_servo('grip_servo', 60, step_delay=0.03)
    smooth_move_servo('grip_servo',  120, step_delay=0.03) #closed
    smooth_move_servo('mid_servo', 120, step_delay=0.05)
    smooth_move_servo('btm_servo', 70, step_delay=0.05)    
    smooth_move_servo('base_servo', 120, step_delay=0.05)    #rotate the base of the robot
    smooth_move_servo('grip_servo',  50, step_delay=0.03) #open
    smooth_move_servo('grip_servo', 90, step_delay=0.03) #closed
    # go back to orignial position:
    smooth_move_servo('top_servo', 85, step_delay=0.05)
    smooth_move_servo('mid_servo', 80, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)
    smooth_move_servo('base_servo', 90, step_delay=0.05)
    
def PickUpGlass():
    
    # Step 1: Align the base of the arm to center (assuming object is in front)
 #   smooth_move_servo('base_servo', 70, step_delay=0.05)  # Rotate base to center at 90 degrees

    # Step 2: Lower the arm to reach the object's height
    smooth_move_servo('base_servo', 90, step_delay=0.05)
    smooth_move_servo('btm_servo', 85, step_delay=0.05)  # Lower base shoulder slightly
    smooth_move_servo('mid_servo', 80, step_delay=0.05)   # Angle mid arm forward
    smooth_move_servo('top_servo', 85, step_delay=0.05)# Lower top arm to approach object
    #trying somthing
    #smooth_move_servo('grip_base_servo', current_angles['grip_base_servo'] + 50, step_delay=0.03)  # Adjust grip position
    smooth_move_servo('grip_servo', 60, step_delay=0.03) #open
    smooth_move_servo('top_servo', 20, step_delay=0.05)
    smooth_move_servo('mid_servo', 135, step_delay=0.05)  #bend down part
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    # this will be to close the gripper and then to drop what it has
    smooth_move_servo('grip_servo', 60, step_delay=0.03)
    smooth_move_servo('grip_servo',  120, step_delay=0.03) #closed
    smooth_move_servo('mid_servo', 120, step_delay=0.05)
    smooth_move_servo('btm_servo', 70, step_delay=0.05)    
    smooth_move_servo('base_servo', 0, step_delay=0.05)    #rotate the base of the robot
    smooth_move_servo('grip_servo',  50, step_delay=0.03) #open
    smooth_move_servo('grip_servo', 90, step_delay=0.03) #closed
    # go back to orignial position:
    smooth_move_servo('top_servo', 85, step_delay=0.05)
    smooth_move_servo('mid_servo', 80, step_delay=0.05)
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    smooth_move_servo('base_servo', 90, step_delay=0.05)


def Tester():
 
     # Puts the arm in the upright position 
    smooth_move_servo('base_servo', 90, step_delay=0.05) # THis is the rotation part of the arm
    smooth_move_servo('btm_servo', 83, step_delay=0.05)  # This is the shoulder of the arm
    smooth_move_servo('mid_servo', 85, step_delay=0.05)  # This is the elbow of the arm 
    smooth_move_servo('top_servo', 90, step_delay=0.05)  # This is the lower wrist of the arm 
    # Moves the arm to the position of the item and opens up the gripper
    smooth_move_servo('grip_base_servo', 145, step_delay=0.03) 
    smooth_move_servo('grip_servo', 60, step_delay=0.03) 
    smooth_move_servo('top_servo', 20, step_delay=0.05)
    smooth_move_servo('mid_servo', 135, step_delay=0.05)  #bend down part
    smooth_move_servo('btm_servo', 90, step_delay=0.05)
    # Closes the gripper, picks up the item and moves to where it needs to be dropped and drops it.
    smooth_move_servo('grip_servo', 60, step_delay=0.03)
    smooth_move_servo('grip_servo', 120, step_delay=0.03) 
    smooth_move_servo('mid_servo', 90, step_delay=0.05)
    smooth_move_servo('btm_servo', 90, step_delay=0.05)    
    smooth_move_servo('base_servo', 120, step_delay=0.05)    
    smooth_move_servo('grip_servo', 50, step_delay=0.03) 
    smooth_move_servo('grip_servo', 90, step_delay=0.03) 
    # Moves it back to orignial position after droping the item:
    smooth_move_servo('top_servo', 80, step_delay=0.05) 
    smooth_move_servo('btm_servo', 80, step_delay=0.05)
    smooth_move_servo('mid_servo', 85, step_delay=0.05)
    smooth_move_servo('base_servo', 90, step_delay=0.05)
    smooth_move_servo('grip_base_servo', 140, step_delay=0.03) 

# Initialize material counts
material_counts = { "cardboard": 0, "glass": 0, "metal": 0, "paper": 0, "plastic": 0 }

# Serial communication setup
ser = serial.Serial("COM9", 9600)
ser.flushInput()
pico_responses = ["Done Moving\r\n", "Connected to Pico\r\n"]

# Load YOLO model
model = YOLO("../runs/detect/train7/weights/best.pt")  # Update path as needed

# Start video stream and FPS counter
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
time.sleep(2)
fps = FPS().start()

done = 1

while True:
    success, frame = cap.read()
    if not success:
        break

    # YOLO detection
    results = model(frame, stream=True)
    for result in results:
        boxes = result.boxes  # YOLO result boxes
        for box in boxes:
            # Get class label and confidence
            cls_id = int(box.cls[0])
            label = model.names[cls_id] if cls_id < len(model.names) else "Unknown"
            confidence = math.ceil(box.conf[0] * 100) / 100

            # Draw bounding box and label on frame
            (x1, y1, x2, y2) = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Call the specific method based on the label and confidence
            if confidence >= 0.85:
                if label.lower() == "metal":
                    PickUpMetal()
                elif label.lower() == "paper":
                    PickUpPaper()
                elif label.lower() == "plastic":
                    PickUpPlastic()
                elif label.lower() == "glass":
                    PickUpGlass()
                elif label.lower() == "cardboard":
                    PickUpCardboard()

    # Communication with Pico
    if ser.inWaiting() > 0:
        pico_response = ser.readline().decode().strip()
        if pico_response in pico_responses:
            done = 1

    # Display frame
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    fps.update()

# Cleanup
fps.stop()
cap.release()
cv2.destroyAllWindows()

