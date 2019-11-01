import board
import time
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
hat.frequency = 60
led_channel = hat.channels[0]
led_channel.duty_cycle = 0xffff
# kit = ServoKit(channels=16)
# kit.continuous_servo[0].throttle = 1
# time.sleep(1)
# kit.continuous_servo[0].throttle = -1
# time.sleep(1)
# kit.continuous_servo[0].throttle = 0