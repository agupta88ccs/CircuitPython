import time
import board
import pulseio
import touchio
from adafruit_motor import servo

# create a PWMOut object on Pin D8.
pwm = pulseio.PWMOut(board.D8, duty_cycle=2 ** 15, frequency=50)
angle = 5

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

my_servo = servo.Servo(pwm)  # Create a servo object, my_servo.

while True:
    if touch_A1.value:
        if angle < 180:
            angle = angle+1
        my_servo.angle = angle
        #time.sleep(0.01)
        print(angle)
    if touch_A2.value:
        if angle > 0:
            angle = angle-1
        my_servo.angle = angle
        #time.sleep(0.01)
        print(angle)
    time.sleep(0.01)